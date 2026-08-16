#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""skill-* 卡片现状快速扫描脚本"""
import yaml
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
import glob
import os
import sys

VAULT_ROOT = r"C:\Users\Administrator\Desktop\wiki\30_wiki"

def extract_frontmatter(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---"):
        return None, text, "no frontmatter"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text, "incomplete frontmatter"
    try:
        data = yaml.safe_load(parts[1])
        return data if data else {}, text, None
    except Exception as e:
        return None, text, str(e)


def main():
    skill_files = glob.glob(os.path.join(VAULT_ROOT, "**", "skill-*.md"), recursive=True)
    total = len(skill_files)
    print(f"skill-* 卡片总数: {total}")
    print("=" * 70)

    yaml_errors = 0
    stats = {
        "by_type": {},
        "by_status": {},
        "by_trust": {},
        "by_reviewed_by": {},
        "has_diagnostic_signals": 0,
        "no_diagnostic_signals": 0,
        "has_constraints_boundaries": 0,  # 查找 Constraints & Boundaries 或 When NOT to Use
        "no_constraints_boundaries": 0,
        "type_tool": 0,
        "type_concept": 0,
        "type_other": 0,
        "type_missing": 0,
    }

    # 用于诊断的具体卡片列表
    close_to_a = []
    enriched_missing_structure = []
    pure_draft_skeleton = []
    yaml_error_files = []

    for path in skill_files:
        data, text, err = extract_frontmatter(path)
        basename = os.path.basename(path)
        cid = basename[:-3]

        if err:
            yaml_errors += 1
            yaml_error_files.append((cid, err))
            continue

        # type
        ctype = data.get("type", "missing")
        stats["by_type"][ctype] = stats["by_type"].get(ctype, 0) + 1
        if ctype == "tool":
            stats["type_tool"] += 1
        elif ctype == "concept":
            stats["type_concept"] += 1
        elif ctype == "missing":
            stats["type_missing"] += 1
        else:
            stats["type_other"] += 1

        # status
        status = data.get("status", "missing")
        stats["by_status"][status] = stats["by_status"].get(status, 0) + 1

        # trust_level
        trust = data.get("trust_level", "missing")
        stats["by_trust"][trust] = stats["by_trust"].get(trust, 0) + 1

        # reviewed_by
        reviewer = data.get("reviewed_by", "missing")
        stats["by_reviewed_by"][reviewer] = stats["by_reviewed_by"].get(reviewer, 0) + 1

        # diagnostic_signals
        has_ds = bool(data.get("diagnostic_signals"))
        if has_ds:
            stats["has_diagnostic_signals"] += 1
        else:
            stats["no_diagnostic_signals"] += 1

        # constraints & boundaries
        # 检查正文中是否包含 When NOT to Use、Constraints & Boundaries、不要用 等
        body = text.split("---", 2)[2] if len(text.split("---", 2)) >= 3 else text
        has_cb = any(k in body.lower() for k in [
            "when not to use", "constraints", "boundaries", "不要用",
            "不适用", "边界", "失败模式", "when not"
        ])
        if has_cb:
            stats["has_constraints_boundaries"] += 1
        else:
            stats["no_constraints_boundaries"] += 1

        # 分类
        is_enriched = status == "enriched"
        is_draft = status == "draft"
        is_low_trust = trust == "low"
        is_pending_reviewer = reviewer == "pending"

        # 接近 A 级：enriched + 有 DS + 有 C&B + reviewer 不是 pending + trust 不是 low + related>=5
        related = data.get("related", [])
        related_count = len(related) if isinstance(related, list) else 0

        score = 0
        if is_enriched: score += 1
        if has_ds: score += 1
        if has_cb: score += 1
        if not is_pending_reviewer: score += 1
        if not is_low_trust: score += 1
        if related_count >= 5: score += 1

        if score >= 5:
            close_to_a.append((cid, score, {
                "status": status, "ds": has_ds, "cb": has_cb,
                "reviewer": reviewer, "trust": trust, "related": related_count
            }))
        elif is_enriched and (not has_ds or not has_cb):
            enriched_missing_structure.append((cid, {
                "ds": has_ds, "cb": has_cb, "trust": trust, "reviewer": reviewer
            }))
        elif is_draft and is_low_trust and is_pending_reviewer and not has_ds and not has_cb:
            pure_draft_skeleton.append(cid)

    print("\n【按 type 分布】")
    for k, v in sorted(stats["by_type"].items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")

    print("\n【按 status 分布】")
    for k, v in sorted(stats["by_status"].items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")

    print("\n【按 trust_level 分布】")
    for k, v in sorted(stats["by_trust"].items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")

    print("\n【按 reviewed_by 分布】")
    for k, v in sorted(stats["by_reviewed_by"].items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")

    print(f"\n【diagnostic_signals】有: {stats['has_diagnostic_signals']} / 无: {stats['no_diagnostic_signals']}")
    print(f"【Constraints/Boundaries】有: {stats['has_constraints_boundaries']} / 无: {stats['no_constraints_boundaries']}")

    print(f"\n【YAML 解析失败】: {yaml_errors}")
    if yaml_error_files:
        for cid, err in yaml_error_files[:10]:
            print(f"  - {cid}: {err[:80]}")

    print(f"\n【接近 A 级（6 项中满足 ≥5）】: {len(close_to_a)} 张")
    for cid, score, detail in close_to_a[:15]:
        print(f"  - {cid} (score={score}): {detail}")

    print(f"\n【enriched 但缺结构（DS 或 C&B）】: {len(enriched_missing_structure)} 张")
    for cid, detail in enriched_missing_structure[:15]:
        print(f"  - {cid}: {detail}")

    print(f"\n【纯 draft 骨架（draft+low+pending+无DS+无C&B）】: {len(pure_draft_skeleton)} 张")
    for cid in pure_draft_skeleton[:20]:
        print(f"  - {cid}")

    # 关键发现：type=tool/concept 的 skill 前缀卡
    print(f"\n【关键发现】")
    print(f"  type=tool 但文件名 skill-*: {stats['type_tool']} 张")
    print(f"  type=concept 但文件名 skill-*: {stats['type_concept']} 张")
    print(f"  type=其他/missing 但文件名 skill-*: {stats['type_other'] + stats['type_missing']} 张")


if __name__ == "__main__":
    main()
