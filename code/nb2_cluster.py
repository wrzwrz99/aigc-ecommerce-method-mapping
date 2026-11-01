# -*- coding: utf-8 -*-
"""
负二项回归（NB2）+ 期刊聚类稳健标准误。
用法：把新语料的逐篇数据喂进来，一键输出 IRR / 聚类稳健 SE / p / 95%CI / alpha / 收敛状态。

设计要点（对照上一版 rerun_trend_nb.py 的缺陷，均已修正）：
1. 设计矩阵包含截距项；
2. 参数用 BFGS/L-BFGS-B 估计，标准误用聚类稳健 sandwich（按期刊聚类），非普通模型 SE；
3. 报告 alpha（离散参数）、收敛状态、95% CI，不凭空声称"控制期刊"（这里控制的是期刊复合影响因子；
   如需期刊固定效应，另跑一列 journal FE 敏感性）。
"""
import numpy as np
import pandas as pd
from scipy.special import gammaln
from scipy.optimize import minimize
from scipy import stats

def fit_nb2_cluster(df, xcols, ycol='cite', cluster_col='期刊', intercept=True):
    """返回 dict：系数表(DataFrame)、alpha、logLik、success、message。"""
    X0 = df[xcols].values.astype(float)
    X = np.column_stack([np.ones(len(X0)), X0]) if intercept else X0
    y = df[ycol].values.astype(float)
    n, k = X.shape
    names = (['Intercept'] if intercept else []) + list(xcols)

    def nll(params):
        beta = params[:k]
        a = np.exp(params[k])
        mu = np.exp(X @ beta)
        mu = np.clip(mu, 1e-8, None)
        r = 1.0 / a
        return -(gammaln(y + r) - gammaln(r) - gammaln(y + 1)
                 + r * np.log(r / (r + mu)) + y * np.log(mu / (r + mu))).sum()

    init = np.zeros(k + 1)
    if intercept:
        init[0] = np.log(max(y.mean(), 1.0))
    init[k] = np.log(1.0)
    res = minimize(nll, init, method='BFGS', options={'maxiter': 5000, 'gtol': 1e-8})
    beta = res.x[:k]
    alpha = np.exp(res.x[k])

    # ---- 聚类稳健 sandwich 标准误 ----
    mu = np.clip(np.exp(X @ beta), 1e-8, None)
    # 单个观测的对数似然梯度（对 beta）：score_i = x_i * (y_i - mu_i) / (1 + alpha*mu_i)
    g = (y - mu) / (1.0 + alpha * mu)
    score = X * g[:, None]                    # n x k

    def f(b):
        m = np.clip(np.exp(X @ b), 1e-8, None)
        rr = 1.0 / alpha
        return (gammaln(y + rr) - gammaln(rr) - gammaln(y + 1)
                + rr * np.log(rr / (rr + m)) + y * np.log(m / (rr + m))).sum()

    eps = 1e-5
    H = np.zeros((k, k))                      # 数值 Hessian（四点中心差分）
    for j in range(k):
        for l in range(k):
            bpp = beta.copy(); bpm = beta.copy(); bmp = beta.copy(); bmm = beta.copy()
            bpp[j] += eps; bpp[l] += eps
            bpm[j] += eps; bpm[l] -= eps
            bmp[j] -= eps; bmp[l] += eps
            bmm[j] -= eps; bmm[l] -= eps
            H[j, l] = (f(bpp) - f(bpm) - f(bmp) + f(bmm)) / (4 * eps * eps)
    bread = np.linalg.inv(H)                  # 观测信息矩阵的逆（面包）
    # meat：按聚类累加 score
    clusters = df[cluster_col].astype(str).values
    meat = np.zeros((k, k))
    for c in np.unique(clusters):
        sc = score[clusters == c].sum(axis=0)
        meat += np.outer(sc, sc)
    V = bread @ meat @ bread                # 聚类稳健协方差
    se = np.sqrt(np.diag(V))
    z = beta / se
    p = 2 * (1 - stats.norm.cdf(np.abs(z)))
    lo = np.exp(beta - 1.96 * se)
    hi = np.exp(beta + 1.96 * se)

    out = pd.DataFrame({
        'term': names, 'IRR': np.exp(beta), 'se_logIRR': se, 'z': z,
        'p': p, 'CI95_lo': lo, 'CI95_hi': hi,
    })
    return {
        'table': out, 'alpha': alpha, 'n': n, 'n_cluster': int(len(np.unique(clusters))),
        'logLik': -res.fun, 'success': bool(res.success), 'message': str(res.message),
    }

if __name__ == '__main__':
    # 自检：用当前旧数据跑一遍，验证实现能收敛并产出聚类稳健 SE
    import os
    BASE = r'D:\论文\电商综述'
    lab = pd.read_csv(BASE + r'\JIS_revision\final_labels_1328.csv', encoding='utf-8-sig')
    lab['title'] = lab['title'].astype(str).str.strip()
    m = dict(zip(lab['title'], lab['paradigm_cn']))
    nb = pd.read_csv(BASE + r'\AIGC文创电商\查新文本\_nb_data_calibrated.csv', encoding='utf-8-sig')
    nb['题名'] = nb['题名'].astype(str).str.strip()
    nb['pcn'] = nb['题名'].map(m)
    nb = nb.dropna(subset=['pcn', 'cite', 'ifac'])
    nb['cite'] = pd.to_numeric(nb['cite'], errors='coerce')
    nb = nb.dropna(subset=['cite'])
    for c in ['实证主义', '技术驱动', '人文解释']:
        nb['d_' + c] = (nb['pcn'] == c).astype(int)
    xcols = ['d_实证主义', 'd_技术驱动', 'd_人文解释', 'log_age', 'author_n', 'funded', 'kw_count', 'ifac']
    r = fit_nb2_cluster(nb, xcols, ycol='cite', cluster_col='期刊')
    print('N=%d clusters=%d success=%s alpha=%.3f logLik=%.1f' % (r['n'], r['n_cluster'], r['success'], r['alpha'], r['logLik']))
    print(r['table'].round(3).to_string(index=False))
