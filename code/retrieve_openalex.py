# -*- coding: utf-8 -*-
"""
OpenAlex 检索：AIGC/generative AI + e-commerce + consumer/user behavior
输出：openalex_raw.csv（合并去重后的原始语料）
"""
import urllib.request, urllib.parse, json, time, csv, os

BASE = "https://api.openalex.org/works"
MAILTO = "research@example.com"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "openalex_raw.csv")

QUERIES = [
    "generative artificial intelligence e-commerce",
    "generative ai e-commerce consumer",
    "large language model e-commerce consumer",
    "ChatGPT e-commerce consumer",
    "AI-generated content e-commerce",
    "generative ai online shopping consumer",
    "generative ai consumer purchase intention",
    "large language model consumer behavior online",
    "virtual influencer live streaming commerce",
    "AI avatar livestream shopping",
    "AI chatbot e-commerce consumer",
    "generative ai social commerce consumer",
    "generative ai online retail consumer",
    "AI-generated review consumer",
    "generative ai recommendation e-commerce consumer",
    "digital human live commerce",
    "virtual anchor e-commerce consumer",
    "conversational AI shopping consumer",
    "generative ai consumer decision making e-commerce",
    "text-to-image product consumer e-commerce",
]

def http_get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "mailto:" + MAILTO})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

def reconstruct_abstract(inv):
    if not inv:
        return ""
    pos = {}
    for w, idxs in inv.items():
        for i in idxs:
            pos[i] = w
    return " ".join(pos[i] for i in sorted(pos))

def main():
    seen = {}
    n_req = 0
    for q in QUERIES:
        cursor = "*"
        pages = 0
        while cursor and pages < 5:
            f = urllib.parse.quote(q)
            url = (f"{BASE}?filter=title_and_abstract.search:{f},"
                   f"from_publication_date:2015-01-01,type:article,language:en"
                   f"&per-page=200&select=id,doi,title,publication_year,publication_date,"
                   f"language,type,cited_by_count,abstract_inverted_index,authorships,"
                   f"primary_location,concepts&cursor={cursor}&mailto={MAILTO}")
            try:
                d = http_get(url)
            except urllib.error.HTTPError as e:
                print("HTTPError", e.code, q, file=sys.stderr if 'sys' in globals() else None)
                break
            except Exception as e:
                print("ERR", q, e)
                break
            n_req += 1
            for w in d.get("results", []):
                wid = w.get("id")
                if not wid or wid in seen:
                    continue
                pl = w.get("primary_location") or {}
                src = (pl.get("source") or {}).get("display_name", "")
                seen[wid] = {
                    "openalex_id": wid,
                    "doi": (w.get("doi") or "").replace("https://doi.org/", ""),
                    "title": w.get("title") or "",
                    "year": w.get("publication_year"),
                    "date": w.get("publication_date") or "",
                    "cited_by_count": w.get("cited_by_count"),
                    "journal": src,
                    "n_authors": len(w.get("authorships") or []),
                    "abstract": reconstruct_abstract(w.get("abstract_inverted_index")),
                    "concepts": "; ".join((c.get("display_name") or "") for c in (w.get("concepts") or [])[:6]),
                }
            cursor = d.get("meta", {}).get("next_cursor")
            pages += 1
            time.sleep(0.25)
        print(f"[{len(seen):>4} unique] {q}  (reqs={n_req})")

    cols = ["openalex_id", "doi", "title", "year", "date", "cited_by_count",
            "journal", "n_authors", "abstract", "concepts"]
    with open(OUT, "w", newline="", encoding="utf-8-sig") as fh:
        wr = csv.DictWriter(fh, fieldnames=cols)
        wr.writeheader()
        for wid, r in seen.items():
            wr.writerow({c: r.get(c, "") for c in cols})
    print(f"\nDONE. total unique={len(seen)}  saved -> {OUT}")

if __name__ == "__main__":
    import sys
    main()
