# -*- coding: utf-8 -*-
"""#583 狗粮测试 · 语料抽样器
从 30_wiki 分层抽取 50 张真实卡片：
  frameworks(12) + concepts(14) + cases(12) + dark-knowledges(8) + methods(4)
规则：固定随机种子 20260831（可复现）；排除 index/digest 类索引卡（索引卡对检索评测是噪声）。
输出：corpus_manifest.json（路径+类型+字节数）
"""
import json, os, random

WS = r"C:\Users\Administrator\Desktop\wiki"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "corpus_manifest.json")

STRATA = [
    ("30_wiki/frameworks", 12),
    ("30_wiki/concepts", 14),
    ("30_wiki/cases", 12),
    ("30_wiki/dark-knowledges", 8),
    ("30_wiki/methods", 4),
]
EXCLUDE_TOKENS = ("index", "digest", "-latest", "README")

def is_index_card(name):
    low = name.lower()
    return any(t in low for t in EXCLUDE_TOKENS)

def main():
    rng = random.Random(20260831)
    manifest = []
    for rel, n in STRATA:
        d = os.path.join(WS, rel)
        files = [f for f in os.listdir(d) if f.endswith(".md") and not is_index_card(f)]
        files.sort()  # 先排序再抽样，保证与目录列表顺序无关
        picked = rng.sample(files, min(n, len(files)))
        for f in picked:
            p = os.path.join(d, f)
            manifest.append({
                "path": os.path.relpath(p, WS).replace("\\", "/"),
                "stratum": rel.split("/")[-1],
                "bytes": os.path.getsize(p),
            })
    total_bytes = sum(m["bytes"] for m in manifest)
    result = {"seed": 20260831, "count": len(manifest), "total_bytes": total_bytes, "cards": manifest}
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(result, fh, ensure_ascii=False, indent=1)
    print(f"sampled {len(manifest)} cards, {total_bytes} bytes -> {OUT}")
    for s, _ in STRATA:
        cnt = sum(1 for m in manifest if m["stratum"] == s.split("/")[-1])
        print(f"  {s}: {cnt}")

if __name__ == "__main__":
    main()
