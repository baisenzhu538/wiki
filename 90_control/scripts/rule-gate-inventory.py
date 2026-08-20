#!/usr/bin/env python3
"""
rule-gate-inventory.py — 残余文案规则门禁化盘点（#401）

扫描规则文案中的祈使句规则（"必须/禁止/记得"族），产出结构化候选清单，
供人工标注"门禁化状态"与"成本分档"，并按 friction-log 命中数排序。

用法：
    python rule-gate-inventory.py                    # 扫默认目标，人类可读输出
    python rule-gate-inventory.py --json             # JSON 输出（结构化，供报告生成）
    python rule-gate-inventory.py --friction-log .agent/friction-log.md  # 附带命中计数
    python rule-gate-inventory.py --list-sources     # 列出扫描目标

可复扫：同一输入文件集 + 同一关键词族 → 输出一致（#401 验收标准 1）。
"""

import argparse
import json
import re
import sys
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
DESKTOP = VAULT_ROOT.parent

# 扫描目标（规则文案层）
SOURCES = [
    VAULT_ROOT / "90_control" / "PROTOCOL.md",
    VAULT_ROOT / "90_control" / "AGENTS.md",
    VAULT_ROOT / "90_control" / "rules-core.md",
    VAULT_ROOT / "90_control" / "kdo-industrialization-manual.md",
    VAULT_ROOT / "90_control" / "tool-card-excellence-standard.md",
    VAULT_ROOT / ".agent" / "startup.md",
    *sorted((VAULT_ROOT / ".agent").glob("*-context.md")),
    *sorted((VAULT_ROOT / "agents").glob("*/SOUL.md")),
    *sorted((DESKTOP / "agent复盘").glob("*/错误模式库.md")),
]

# 祈使句/禁令关键词族（#401：必须/禁止/记得/一律）
KEYWORD_PATTERN = re.compile(
    r"(必须|禁止|不得|严禁|一律|务必|记得|一定要|不允许|绝不|切勿|任何时候|"
    r"不要(乱|再|擅|直接|随便|自行|单独|盲目|重复|跳过|修改|新建|删除|覆盖|合并|返回)|"
    r"禁止用|不许|铁律|红线)"
)

# 摩擦日志路径（用于命中计数）
DEFAULT_FRICTION_LOG = VAULT_ROOT / ".agent" / "friction-log.md"


def safe_read(path: Path) -> str | None:
    for enc in ("utf-8", "gbk", "latin-1"):
        try:
            return path.read_text(encoding=enc)
        except (UnicodeDecodeError, OSError):
            continue
    return None


def scan_sources(sources: list[Path]) -> list[dict]:
    """返回 [{file, line, text, keywords}]——按文件顺序、行号排序，可复扫。"""
    hits = []
    for fp in sources:
        if not fp.exists():
            continue
        text = safe_read(fp)
        if text is None:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            stripped = line.strip()
            if not stripped or stripped.startswith(("|", "```", ">", "#")):
                continue  # 跳过表格/代码块/引用/标题行——规则正文在普通段落与列表
            if "|" in stripped and stripped.count("|") >= 2:
                continue
            kw = sorted(set(KEYWORD_PATTERN.findall(stripped)))
            if kw:
                rel = fp.relative_to(VAULT_ROOT).as_posix() if str(fp).startswith(str(VAULT_ROOT)) else fp.as_posix()
                hits.append({
                    "file": rel,
                    "line": i,
                    "text": stripped[:200],
                    "keywords": kw,
                })
    return hits


def count_friction_hits(hits: list[dict], friction_text: str) -> dict[str, int]:
    """每条规则的摩擦命中计数：规则文本关键词与 friction-log 行的弱匹配。"""
    counts = {}
    log_lines = [l for l in friction_text.splitlines() if l.startswith("| 2026-")]
    for h in hits:
        # 用规则文本里的 2+ 字符中文词组做匹配键，降低泛词噪音
        tokens = set(re.findall(r"[一-鿿]{2,6}", h["text"]))
        n = 0
        for ll in log_lines:
            if any(t in ll for t in tokens):
                n += 1
        counts[h["file"] + f":{h['line']}"] = n
    return counts


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    p = argparse.ArgumentParser(description="残余文案规则门禁化盘点（#401）")
    p.add_argument("--json", action="store_true")
    p.add_argument("--list-sources", action="store_true")
    p.add_argument("--friction-log", type=Path, default=DEFAULT_FRICTION_LOG)
    args = p.parse_args()

    if args.list_sources:
        for s in SOURCES:
            print("OK " if s.exists() else "MISSING ", s)
        return 0

    hits = scan_sources(SOURCES)
    if not hits:
        print("无规则命中（检查扫描目标）")
        return 1

    if args.friction_log and args.friction_log.exists():
        counts = count_friction_hits(hits, safe_read(args.friction_log) or "")

    if args.json:
        out = {"rules": hits}
        if args.friction_log and args.friction_log.exists():
            out["friction_hits"] = counts
        print(json.dumps(out, ensure_ascii=True, indent=1))
        return 0

    print(f"扫描 {len([s for s in SOURCES if s.exists()])} 个文件，抽取 {len(hits)} 条规则候选")
    print("按文件分组（行号升序）：")
    cur = None
    for h in hits:
        if h["file"] != cur:
            cur = h["file"]
            print(f"\n== {cur}")
        hit_n = counts.get(h["file"] + f":{h['line']}", 0) if args.friction_log and args.friction_log.exists() else "-"
        print(f"  L{h['line']:<5} [friction×{hit_n}] {h['text']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
