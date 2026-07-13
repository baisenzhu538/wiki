#!/usr/bin/env python3
"""
#182 OPC 销售域 × D 域回链批量落地脚本
- 正向：22 张 30_wiki 正式卡 → D 域目标卡
- 反向：D 域目标卡 → OPC 销售域卡（保证 related 双向闭合）
- 不碰 .agent/prompts/（按王语嫣裁定，prompts 独有 6 张随 #186 入库时统一处理）
- 不碰 index/digest（按任务单边界）
"""

from pathlib import Path
from ruamel.yaml import YAML
from collections import defaultdict

VAULT = Path("C:/Users/Administrator/Desktop/wiki")

# 正向映射：source 文件（相对 30_wiki） -> [target id, ...]
# target id 不加 [[ ]]，脚本会自动包装
FORWARD = {
    # ① op-mastercard + 助手
    "personal-os/opc-ai-sales-agent-architecture.md": [
        "framework-一堂-转化率黑客-总纲",
        "conversion-rate-domain-digest",
    ],
    "tools/tool-opc-sales-dialogue-assistant.md": [
        "framework-一堂-转化率黑客-总纲",
        "conversion-rate-domain-digest",
    ],
    # ② agent-spec 应用卡（30_wiki 正式卡 7 张）
    "tools/tool-agent-spec-yitang-opening-3min.md": [
        "framework-一堂-十指模型",
        "framework-一堂-触点本质论",
    ],
    "tools/tool-agent-spec-yitang-objection-handler.md": [
        "framework-一堂-阻力方法论骨架",
        "framework-一堂-12种阻力总表",
        "tool-一堂-阻力消除12策小抄",
    ],
    "tools/tool-agent-spec-yitang-customer-segmentation.md": [
        "tool-一堂-五种挖触点",
        "framework-一堂-12触点SABC分级",
    ],
    "tools/tool-agent-spec-yitang-value-proposition.md": [
        "framework-一堂-动力三曲线",
        "tool-一堂-FAB说服法",
        "framework-一堂-十指模型",
    ],
    "tools/tool-agent-spec-yitang-sales-process-tracker.md": [
        "framework-一堂-转化率提升六步法",
        "framework-一堂-12种阻力总表",
    ],
    "tools/tool-agent-spec-yitang-sales-performance-monitor.md": [
        "framework-一堂-动力三曲线",
        "framework-一堂-转化率提升六步法",
    ],
    "tools/tool-agent-spec-yitang-self-motivation.md": [
        "framework-一堂-动力三曲线",
        "tool-一堂-心理激励优先机制",
    ],
    # ③ 方法论卡（只加通过"一句话测试"的 5 张）
    "frameworks/framework-yitang-sales-incentive-6d.md": [
        "framework-一堂-动力三曲线",
    ],
    "tools/tool-yitang-sales-process-decomposition.md": [
        "framework-一堂-转化率提升六步法",
    ],
    "tools/tool-yitang-value-proposition-4step.md": [
        "framework-一堂-动力三曲线",
        "tool-一堂-FAB说服法",
    ],
    "tools/tool-yitang-sales-performance-management.md": [
        "framework-一堂-转化率提升六步法",
        "framework-一堂-动力三曲线",
    ],
    "tools/tool-yitang-payment-collection-playbook.md": [
        "framework-一堂-12种阻力总表",
        "tool-一堂-阻力消除12策小抄",
    ],
    # ④ 案例 + dk
    "cases/case-yitang-sales-transformation-jubensha-saas.md": [
        "case-一堂-阻力篇案例库",
        "case-一堂-触点篇案例库",
    ],
    "cases/case-yitang-sales-transformation-tuliaogongsi.md": [
        "case-一堂-触点篇案例库",
        "case-一堂-组合篇案例库",
    ],
    "cases/case-yitang-sales-transformation-meirongyuan.md": [
        "case-一堂-触点篇案例库",
        "case-一堂-动力篇案例库",
    ],
    "dark-knowledges/dk-yitang-sales-common-pitfalls.md": [
        "framework-一堂-12种阻力总表",
        "framework-一堂-转化率提升六步法",
    ],
}

# D 域目标卡所在子目录（用于反向定位）
TARGET_DIRS = {
    "frameworks": "frameworks",
    "tools": "tools",
    "cases": "cases",
    "dark-knowledges": "dark-knowledges",
    "domains": "domains",
}


def target_path(tid: str) -> Path:
    """根据 id 前缀推断文件路径。"""
    if tid.endswith("-domain-digest"):
        return VAULT / "30_wiki" / "domains" / f"{tid}.md"
    # 按第一个 - 之前的类型前缀推断
    prefix = tid.split("-")[0]
    if prefix == "case":
        return VAULT / "30_wiki" / "cases" / f"{tid}.md"
    if prefix == "dk":
        return VAULT / "30_wiki" / "dark-knowledges" / f"{tid}.md"
    if prefix == "framework":
        return VAULT / "30_wiki" / "frameworks" / f"{tid}.md"
    if prefix == "tool":
        return VAULT / "30_wiki" / "tools" / f"{tid}.md"
    raise ValueError(f"无法定位 target: {tid}")


def normalize_wikilink(item):
    """把 related 项统一成带 [[ ]] 的字符串。"""
    if isinstance(item, str):
        s = item.strip()
        if not s.startswith("[["):
            s = f"[[{s}]]"
        return s
    # ruamel 可能解析成其他类型，按字符串处理
    return f"[[{str(item).strip()}]]"


def load_frontmatter(path: Path):
    yaml = YAML()
    yaml.preserve_quotes = True
    text = path.read_text(encoding="utf-8-sig")  # 自动 strip BOM
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    fm = yaml.load(parts[1])
    body = parts[2]
    return fm, body


def save_frontmatter(path: Path, fm, body):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.default_flow_style = False
    yaml.width = 4096
    from io import StringIO
    s = StringIO()
    yaml.dump(fm, s)
    fm_text = s.getvalue()
    path.write_text(f"---\n{fm_text}---{body}", encoding="utf-8")


def id_from_path(path: Path) -> str:
    """从 30_wiki 文件路径反推 id。"""
    rel = path.relative_to(VAULT / "30_wiki")
    return rel.stem


def main():
    yaml = YAML()
    yaml.preserve_quotes = True

    # 汇总反向映射
    reverse = defaultdict(set)
    changed = defaultdict(list)

    for src_rel, targets in FORWARD.items():
        src_path = VAULT / "30_wiki" / src_rel
        src_id = id_from_path(src_path)
        fm, body = load_frontmatter(src_path)
        if fm is None:
            print(f"SKIP (no frontmatter): {src_rel}")
            continue
        related = fm.get("related", [])
        if related is None:
            related = []
            fm["related"] = related
        existing = {normalize_wikilink(x) for x in related}
        for tid in targets:
            link = f"[[{tid}]]"
            if link not in existing:
                related.append(link)
                changed[src_rel].append(tid)
                reverse[target_path(tid)].add(src_id)
        if src_rel in changed:
            save_frontmatter(src_path, fm, body)
            print(f"FWD {src_rel}: +{len(changed[src_rel])} {changed[src_rel]}")

    # 处理反向
    rev_changed = defaultdict(list)
    for tgt_path, src_ids in reverse.items():
        tgt_rel = tgt_path.relative_to(VAULT / "30_wiki").as_posix()
        fm, body = load_frontmatter(tgt_path)
        if fm is None:
            print(f"SKIP reverse (no frontmatter): {tgt_rel}")
            continue
        related = fm.get("related", [])
        if related is None:
            related = []
            fm["related"] = related
        existing = {normalize_wikilink(x) for x in related}
        for sid in sorted(src_ids):
            link = f"[[{sid}]]"
            if link not in existing:
                related.append(link)
                rev_changed[tgt_rel].append(sid)
        if tgt_rel in rev_changed:
            save_frontmatter(tgt_path, fm, body)
            print(f"REV {tgt_rel}: +{len(rev_changed[tgt_rel])} {rev_changed[tgt_rel]}")

    print("\n--- 统计 ---")
    print(f"正向文件数: {len(changed)}")
    print(f"反向文件数: {len(rev_changed)}")
    print(f"新增正向边: {sum(len(v) for v in changed.values())}")
    print(f"新增反向边: {sum(len(v) for v in rev_changed.values())}")


if __name__ == "__main__":
    main()
