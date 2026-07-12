"""#163 改项按"读正文"二分重判 — 欧阳锋裁定口径"""
import re, json
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent.parent
manifest = json.loads((VAULT / "90_control/.sandbox/ocr_deadlink_manifest.json").read_text(encoding="utf-8"))

# Hardcoded paths — we know these exist
TARGETS = {
    "ocr-一堂-单元模型-单用户模型": {
        "path": "30_wiki/concepts/yt-entrepreneur-unit-model.md",
        "keywords": ["单用户模型", "单元模型", "单用户"],
        "from_ids": [p["from"] for p in manifest["pairs"] if p["to"] == "ocr-一堂-单元模型-单用户模型" and p["action"] == "改"],
    },
    "ocr-一堂y模型steps策略集": {
        "path": "30_wiki/tools/tool-yitang-Y-model-application.md",
        "keywords": ["策略集", "steps", "Y模型.*步骤", "应用"],
        "from_ids": [p["from"] for p in manifest["pairs"] if p["to"] == "ocr-一堂y模型steps策略集" and p["action"] == "改"],
    },
    "ocr-泛产品设计-落地卡片-攻坚会": {
        "path": "30_wiki/tools/yt-tool-business-formula-gongjianhui.md",
        "keywords": ["攻坚会"],
        "from_ids": [p["from"] for p in manifest["pairs"] if p["to"] == "ocr-泛产品设计-落地卡片-攻坚会" and p["action"] == "改"],
    },
    "ocr-一堂-人机协作-双三角模型": {
        "path": "30_wiki/concepts/concept-yihang-dual-triangle-core.md",
        "keywords": ["双三角"],
        "from_ids": [p["from"] for p in manifest["pairs"] if p["to"] == "ocr-一堂-人机协作-双三角模型" and p["action"] == "改"],
    },
    "ocr-一堂y模型-科学成事道理": {
        "path": "30_wiki/concepts/yt-decision-y-model.md",
        "keywords": ["科学成事", "Y模型"],
        "from_ids": [p["from"] for p in manifest["pairs"] if p["to"] == "ocr-一堂y模型-科学成事道理" and p["action"] == "改"],
    },
}

verdicts = {}
for ocr_target, info in TARGETS.items():
    f = VAULT / info["path"]
    content = f.read_text(encoding="utf-8", errors="replace")

    # Body only (after frontmatter)
    fm_end = content.find("\n---\n", 4)
    body = content[fm_end:] if fm_end > 0 else content

    # Direct card ID mentions in body
    direct = [fid for fid in info["from_ids"] if fid in body]

    # Keyword matches in body
    kw_hits = [kw for kw in info["keywords"] if re.search(kw, body)]

    # 欧阳锋口径: 正文实质引用 = direct mention 或 keywords >= 2
    has_substantial = bool(direct) or len(kw_hits) >= 2
    verdict = "KEEP_改" if has_substantial else "DOWNGRADE_摘"

    verdicts[ocr_target] = verdict

    print(f"{ocr_target}:")
    print(f"  from-cards: {len(info['from_ids'])}")
    print(f"  direct: {direct[:3] if direct else 'none'}")
    print(f"  keywords: {kw_hits}")
    print(f"  substantial: {has_substantial}")
    print(f"  verdict: {verdict}")
    print()

# Summary
keep = sum(1 for v in verdicts.values() if v == "KEEP_改")
downgrade = sum(1 for v in verdicts.values() if v == "DOWNGRADE_摘")
gai_pairs = [p for p in manifest["pairs"] if p["action"] == "改"]
keep_count = sum(1 for p in gai_pairs if verdicts.get(p["to"], "") == "KEEP_改")
downgrade_count = sum(1 for p in gai_pairs if verdicts.get(p["to"], "") == "DOWNGRADE_摘")

print(f"=== Summary ===")
print(f"Targets: KEEP={keep}, DOWNGRADE={downgrade}")
print(f"Pairs:   KEEP={keep_count}, DOWNGRADE={downgrade_count} (of {len(gai_pairs)} total gai)")
