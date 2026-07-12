"""#163 改项逐卡判定 — 欧阳锋口径：每条 from→to 单独查正文"""
import re, json
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent.parent
manifest = json.loads((VAULT / "90_control/.sandbox/ocr_deadlink_manifest.json").read_text(encoding="utf-8"))

TARGET_PATH = VAULT / "30_wiki/concepts/yt-entrepreneur-unit-model.md"
target_content = TARGET_PATH.read_text(encoding="utf-8", errors="replace")
fm_end = target_content.find("\n---\n", 4)
target_body = target_content[fm_end:] if fm_end > 0 else target_content

# Get all改 pairs for this target
gai_pairs = [p for p in manifest["pairs"]
             if p["to"] == "ocr-一堂-单元模型-单用户模型" and p["action"] == "改"]

print(f"Target: ocr-一堂-单元模型-单用户模型 -> yt-entrepreneur-unit-model")
print(f"Total pairs: {len(gai_pairs)}")
print()

# Find each from-card file and check for substantive connection
results = []
for pair in gai_pairs:
    from_id = pair["from"]
    # Find from-card file
    from_file = None
    for d in ["concepts","frameworks","tools","cases","methods","systems","dark-knowledges"]:
        dpath = VAULT / "30_wiki" / d
        if not dpath.is_dir(): continue
        for f in dpath.rglob("*.md"):
            if f.stem == from_id:
                from_file = f
                break
        if from_file: break

    # Keywords: 单元模型, 单用户, unit model, 单用户模型
    keywords_hit = []
    from_body = ""
    from_title = ""

    if from_file:
        content = from_file.read_text(encoding="utf-8", errors="replace")
        fe = content.find("\n---\n", 4)
        from_body = content[fe:] if fe > 0 else content

        # Check title
        tm = re.search(r"title:\s*(.+)", content[:fe] if fe > 0 else "")
        if tm: from_title = tm.group(1).strip().strip("'\"")

        for kw in ["单元模型", "单用户", "unit.model", "单用户模型", "unit economics"]:
            if re.search(kw, from_body, re.IGNORECASE):
                keywords_hit.append(kw)

    # Also check: is from-card name in the same family? (concept/tool with "单元模型" in name)
    same_family = any(t in from_id for t in ["单元模型", "unit-model"])

    evidence = {
        "keywords": keywords_hit,
        "same_family": same_family,
        "title": from_title[:60] if from_title else "(not found)",
    }

    verdict = "KEEP_改" if (keywords_hit or same_family) else "DOWNGRADE_摘"
    results.append({"pair": pair, "verdict": verdict, "evidence": evidence})

# Print
keep_list = [r for r in results if r["verdict"] == "KEEP_改"]
down_list = [r for r in results if r["verdict"] == "DOWNGRADE_摘"]

print("=== KEEP_改 ===")
for r in keep_list:
    e = r["evidence"]
    basis = f"same_family={e['same_family']}, keywords={e['keywords']}" if e["keywords"] else f"same_family={e['same_family']}"
    print(f"  {r['pair']['from']}: {basis}")
    print(f"    title: {e['title']}")

print(f"\n=== DOWNGRADE_摘 ({len(down_list)}) ===")
for r in down_list:
    e = r["evidence"]
    print(f"  {r['pair']['from']}: no keywords, not same family")
    print(f"    title: {e['title']}")

print(f"\n=== SUMMARY ===")
print(f"KEEP: {len(keep_list)}, DOWNGRADE: {len(down_list)}")
print(f"Expected: KEEP=8, DOWNGRADE=11 per欧阳锋 manual check")

# Verify against欧阳锋's findings
ouyangfeng_keep = {
    "concept-单元模型", "yt-tob-unit-model", "tool-单元模型-单商圈",
    "tool-单元模型-单城市", "tool-单元模型-壁垒预判", "tool-单元模型-象限分析法",
    "dk-modeling-unit-pairs-milestone", "framework-TCPR底层网络协议"
}
actual_keep = {r["pair"]["from"] for r in keep_list}
missing = ouyangfeng_keep - actual_keep
extra = actual_keep - ouyangfeng_keep
if missing: print(f"\nMISSING from欧阳锋 list: {missing}")
if extra: print(f"EXTRA vs欧阳锋 list: {extra}")
if not missing and not extra: print(f"\n✅ Matches欧阳锋 manual check exactly")
