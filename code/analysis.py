# -*- coding: utf-8 -*-
import pandas as pd, numpy as np
from datetime import datetime
from scipy import stats

df = pd.read_csv('openalex_ssci_q12.csv', encoding='utf-8-sig')
df['year'] = df['year'].astype(int)

dub = ['International Journal of Computer Information Systems and Industrial Management Applications',
'Telematics and Informatics Reports','Indian Journal of Marketing','Journal of Marketing and Emerging Economics',
'International Journal of Marketing Studies','Canadian Journal of Marketing Research',
'American Journal of Information Science and Technology','International Journal of Marketing Communication and New Media',
'International Journal of Business and Management Sciences','Journal of Science Engineering Technology and Management Sciences',
'Journal of System and Management Sciences','Computers in Human Behavior Reports','Computers in Human Behavior Artificial Humans',
'Journal of Marketing Analytics']

before = len(df)
df = df[~df.journal.isin(dub)].copy()
print(f'剔除 18 篇: {before} -> {len(df)}')

# 修正误标: JTAER 2026 bibliometric review 质性->概念
mis = (df.doi == '10.3390/jtaer21030074')
print('修正误标(质性->概念)命中:', int(mis.sum()))
df.loc[mis, 'paradigm'] = 'conceptual'

# 保存 clean CSV
df.to_csv('openalex_ssci_q12_clean.csv', index=False, encoding='utf-8-sig')
print('已保存 openalex_ssci_q12_clean.csv:', len(df), '篇')

order = ['quantitative','conceptual','computational','qualitative']
print('\n=== 方法类别分布 ===')
pc = df['paradigm'].value_counts()
for k in order:
    print(f'{k:14s} {pc.get(k,0):4d}  {100*pc.get(k,0)/len(df):5.1f}%')

print('\n=== 年份分布 ===')
ct = pd.crosstab(df['year'], df['paradigm']).reindex(columns=order, fill_value=0)
for yr,row in ct.iterrows():
    print(yr, '|', ' '.join(f'{row[c]:>3}' for c in order), '| tot', int(row.sum()))

print('\n=== 期刊分布(前12) ===')
jc = df['journal'].value_counts()
print('unique journals:', len(jc))
for j,c in jc.head(12).items():
    print(f'{c:>3}  {j}')

print('\n=== Mann-Kendall(年度,并列校正) ===')
def mk(x):
    x=np.asarray(x,dtype=float); n=len(x); s=0
    for i in range(n):
        for j in range(i+1,n): s+=np.sign(x[j]-x[i])
    from collections import Counter
    cnt=Counter(x); vs=(n*(n-1)*(2*n+5))/18.0
    for v in cnt.values():
        if v>1: vs-=v*(v-1)*(2*v+5)/18.0
    sd=np.sqrt(vs); z=(s-1)/sd if s>0 else ((s+1)/sd if s<0 else 0.0)
    p=2*(1-stats.norm.cdf(abs(z))); return s,z,p
annual_tot = df.groupby('year').size().reindex(range(2015,2027), fill_value=0)
s,z,p = mk(annual_tot.values)
print(f'总量: S={s:.1f} z={z:.3f} p={p:.4f}')
ct_full = ct.reindex(range(2015,2027), fill_value=0)
tot = ct_full.sum(axis=1)
for k in order:
    share = (ct_full[k]/tot.replace(0,np.nan)).fillna(0).values
    s,z,p = mk(share)
    print(f'share {k:14s}: z={z:6.3f} p={p:.4f}')
    s,z,p = mk(ct_full[k].values)
    print(f'count {k:14s}: z={z:6.3f} p={p:.4f}')

print('\n=== 引用统计 ===')
df['log_age'] = np.log1p((pd.Timestamp('2026-11-01')-pd.to_datetime(df['date'],errors='coerce')).dt.days/30.44)
df['log_age'] = df['log_age'].fillna(np.log1p((2026-df['year'])*12+6))
for k in order:
    sub=df[df.paradigm==k]
    if len(sub)==0: print(f'{k}: n=0'); continue
    print(f'{k:14s} n={len(sub):3d} mean={sub.cited_by_count.mean():6.1f} median={sub.cited_by_count.median():5.1f} zero%={100*(sub.cited_by_count==0).mean():4.1f}%')
print(f'整体: mean={df.cited_by_count.mean():.1f} median={df.cited_by_count.median():.1f} zero%={100*(df.cited_by_count==0).mean():.1f}%')

# NB2
import sys; sys.path.insert(0,'.')
from nb2_cluster import fit_nb2_cluster
df['cite']=df['cited_by_count'].astype(float)
for k in ['conceptual','computational','qualitative']:
    df['d_'+k]=(df.paradigm==k).astype(int)
xcols=['d_conceptual','d_computational','d_qualitative','log_age']
r=fit_nb2_cluster(df, xcols, ycol='cite', cluster_col='journal')
nn = r['n']; nc = r['n_cluster']; al = r['alpha']
print('\n=== NB2 (N=%d, clusters=%d, alpha=%.2f) ===' % (nn, nc, al))
t=r['table'].copy(); t['IRR']=t['IRR'].round(3); t['p']=t['p'].round(3); t['se_logIRR']=t['se_logIRR'].round(3)
print(t[['term','IRR','se_logIRR','p']].to_string(index=False))
