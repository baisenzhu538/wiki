#!/usr/bin/env python3
"""
kdo skill crystallize — 经验→技能自动结晶（#279 jarvis 模式）

扫描错误模式库 + 技能进化日志 + daily-context 复盘，
提取"重复出现的有效做法"（同主题 ≥2 次）→ draft skill 候选骨架。
不自动 publish——人审（黄药师）后走 skill_lifecycle publish。

用法:
  python kdo-tools/skill_crystallize.py scan [--min-count 2] [--dry-run]
  python kdo-tools/skill_crystallize.py list                  # 列出已结晶候选
"""
import argparse
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if sys.platform == "win32":
    try:
        import ctypes
        ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    except Exception:
        pass

WIKI = Path(__file__).resolve().parent.parent
HOME = Path.home()
SOURCES = {
    "错误模式库": WIKI / ".agent" / "huangyaoshi" / "daily_cognitive_review" / "错误模式库.md",
    "技能进化日志": HOME / "Desktop" / "agent复盘" / "黄药师" / "daily_cognitive_review" / "技能进化日志.md",
    "认知复盘": HOME / "Desktop" / "agent复盘" / "黄药师" / "daily_cognitive_review" / "每日复盘",
    "daily-context": HOME / "Desktop" / "agent复盘" / "huangyaoshi" / "daily-context",
}
OUT_DIR = WIKI / "40_outputs" / "capabilities" / "skills" / "crystallized-candidates"
OUT_DIR.mkdir(parents=True, exist_ok=True)
# 发布目录：skills/ 顶层（skill_lifecycle 可发现），带 crystallized- 前缀区分
PUBLISH_DIR = WIKI / "40_outputs" / "capabilities" / "skills"

# 主题关键词 → (技能名, 触发词描述)。匹配到同主题 ≥min_count 次 → 结晶候选
TOPICS = [
    {
        "name": "dry-run-before-batch",
        "title": "批量操作 dry-run 先行",
        "keywords": ["dry-run", "批量", "先预览", "全量扫描", "变异格式", "非空不覆盖", "声明范围"],
        "desc": "任何批量写操作前先 dry-run 预览 + 全量扫描所有格式变体 + 非空值不覆盖",
    },
    {
        "name": "dogfood-testing",
        "title": "狗粮测试三连",
        "keywords": ["狗粮", "index rebuild", "incremental lint", "end-to-end", "端到端", "实测", "复现"],
        "desc": "基建改动后跑 索引重建 + 增量 lint + 端到端搜索 三重验证，不假设索引重建=搜索修复",
    },
    {
        "name": "research-first",
        "title": "调研先行",
        "keywords": ["调研", "WebSearch", "最佳实践", "业界", "先查", "全网", "不凭记忆"],
        "desc": "任何基建/方案迭代第一步是调研业界最佳实践，不凭记忆做决策",
    },
    {
        "name": "round-trip-validation",
        "title": "frontmatter round-trip 校验",
        "keywords": ["round-trip", "yaml.safe_load", "回读", "无损", "解析器", "手写 YAML", "roundtrip"],
        "desc": "任何写 frontmatter 的工具必须带 round-trip 校验（写入后 yaml.safe_load 全量验证无损）",
    },
    {
        "name": "root-cause-not-symptom",
        "title": "先诊断根因再调参",
        "keywords": ["根因", "诊断", "先诊断", "公告", "不是", "调参", "P-21", "先造诊断工具"],
        "desc": "遇错先造诊断工具定位根因，不盲目调参；API 异常先查提供商公告",
    },
    {
        "name": "evidence-over-claims",
        "title": "证据先于声称",
        "keywords": ["声称", "验证", "独立验证", "git", "字节", "可复现", "P-15", "实测", "对账"],
        "desc": "任何完成声明必须可复现验证——git 字节 > 审查报告 > Agent 记忆；数字附带测量方法",
    },
    {
        "name": "encode-aware-file-io",
        "title": "编码感知文件 IO",
        "keywords": ["GBK", "BOM", "UTF-8", "编码", "乱码", "reconfigure", "PYTHONIOENCODING"],
        "desc": "Windows 终端/文件 IO 注意编码：脚本入口 reconfigure UTF-8、读文件剥离 BOM、避免 GBK 崩溃",
    },
    {
        "name": "friction-log-immediate",
        "title": "摩擦当下记录",
        "keywords": ["friction", "摩擦", "当下记录", "friction-log", "阻塞"],
        "desc": "遇摩擦/阻塞/返工当下记 friction-log 一行，不等会话结束（#276）",
    },
]


def collect_text() -> list[tuple[str, str]]:
    """读取所有数据源文本，返回 [(来源名, 文本)]。缺失源跳过。"""
    texts = []
    for name, path in SOURCES.items():
        if path.is_dir():
            for f in sorted(path.glob("*.md")):
                try:
                    texts.append((f"{name}/{f.stem}", f.read_text(encoding="utf-8", errors="ignore")))
                except OSError:
                    continue
        elif path.exists():
            try:
                texts.append((name, path.read_text(encoding="utf-8", errors="ignore")))
            except OSError:
                continue
    return texts


def scan(min_count: int) -> list[dict]:
    """按主题关键词统计出现次数，≥min_count 的生成候选。"""
    texts = collect_text()
    hits = {t["name"]: {"name": t["name"], "title": t["title"], "desc": t["desc"], "count": 0, "evidence": []} for t in TOPICS}
    for src, text in texts:
        for topic in TOPICS:
            kws = topic["keywords"]
            found = [kw for kw in kws if kw in text]
            if found:
                hits[topic["name"]]["count"] += 1
                hits[topic["name"]]["evidence"].append((src, found[:3]))
    candidates = [h for h in hits.values() if h["count"] >= min_count]
    return sorted(candidates, key=lambda h: -h["count"])


def render_skill(cand: dict) -> str:
    """生成 draft skill 骨架（frontmatter 用 skill_lifecycle 兼容格式）。"""
    evidence_lines = "\n".join(f"  - {src}（命中：{'、'.join(kws)}）" for src, kws in cand["evidence"][:5])
    return f"""---
name: {cand['title']}
type: capability/skill
status: draft
created_at: 2026-08-09
author: 黄药师（skill_crystallize 自动结晶）
source_refs: []
related: []
---

# {cand['title']}

> 由 `kdo skill crystallize` 从经验库自动结晶（#279 jarvis 模式）。**未人审，draft 状态，审后 publish。**

## 触发词

{cand['desc']}

## 使用方法

（待填——人审时根据证据补全操作步骤）

## 证据来源（出现 {cand['count']} 次）

{evidence_lines}

## 能力边界

（待填）

## 失败模式

（待填）
"""


def cmd_scan(args) -> int:
    candidates = scan(args.min_count)
    print(f"\n经验→技能结晶扫描（数据源 {len(collect_text())} 个，主题阈值 ≥{args.min_count} 次）\n")
    if not candidates:
        print("  （无候选——提高阈值或补充数据源）")
        return 0
    for c in candidates:
        print(f"  🟢 {c['title']}  (出现 {c['count']} 次)")
        for src, kws in c["evidence"][:3]:
            print(f"       {src}  ← {'、'.join(kws)}")
    if args.dry_run:
        print(f"\n（dry-run：不生成文件。加 --apply 写入 {len(candidates)} 个 draft 候选）")
    else:
        # draft 骨架写 OUT_DIR（工作区），发布时复制到 PUBLISH_DIR（skill_lifecycle 可发现）
        for c in candidates:
            (OUT_DIR / f"skill-{c['name']}.md").write_text(render_skill(c), encoding="utf-8")
            pub_dir = PUBLISH_DIR / f"crystallized-{c['name']}"
            pub_dir.mkdir(parents=True, exist_ok=True)
            (pub_dir / "SKILL.md").write_text(render_skill(c), encoding="utf-8")
        print(f"\n✅ 已生成 {len(candidates)} 个 draft 候选 → {OUT_DIR.relative_to(WIKI)}")
        print(f"   发布副本（skill_lifecycle 可发现）→ {PUBLISH_DIR.relative_to(WIKI)}/crystallized-*/")
        print("   人审：Read 候选 → 达标 → `python kdo-tools/skill_lifecycle.py set crystallized-<name> --status published --apply`")
    return 0


def cmd_list(_args) -> int:
    files = sorted(OUT_DIR.glob("skill-*.md"))
    print(f"\n已结晶候选（{len(files)} 个，draft 状态）：")
    for f in files:
        print(f"  📄 {f.stem}")
    return 0


def main():
    p = argparse.ArgumentParser(description="kdo skill crystallize — 经验→技能自动结晶（#279）")
    sub = p.add_subparsers(dest="cmd")
    s = sub.add_parser("scan", help="扫描并生成候选（默认 dry-run）")
    s.add_argument("--min-count", type=int, default=2, help="同主题最低出现次数（jarvis 阈值 3，存量少下调到 2）")
    s.add_argument("--apply", dest="dry_run", action="store_false", help="真正生成 draft 骨架")
    sub.add_parser("list", help="列出已结晶候选")
    args = p.parse_args()
    if args.cmd == "scan":
        return cmd_scan(args)
    if args.cmd == "list":
        return cmd_list(args)
    p.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
