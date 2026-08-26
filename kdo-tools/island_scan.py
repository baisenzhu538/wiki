#!/usr/bin/env python3
"""island_scan.py — 孤岛卡扫描 lint（#528）：无出链（related 空）且无入链的卡定期出清单。

结构层治本（盲测第 1 问失败根因=OCR 卡孤岛死胡同）：定期扫描让孤岛上不了岸。
WARNING 制不拦流转（只出清单，挂链走编排批次）；agent-spec 类按口径豁免。

用法：
  python kdo-tools/island_scan.py              # 扫描+清单落盘（60_feedback/auto/island-cards/）
  python kdo-tools/island_scan.py --stdout     # 只打印不落盘
"""
import argparse
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "30_wiki"
OUT_DIR = ROOT / "60_feedback" / "auto" / "island-cards"

# 口径豁免：agent-spec 类（spec 被 CLAUDE.md/配置引用，不走进卡互链体系）
EXEMPT_TYPES = {"tool-agent-spec", "system-agent-spec", "index", "log"}  # index/log=非卡资产（#527 同款教训）
EXEMPT_DIRS = {"agent-specs"}


def _parse_fm(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    try:
        import yaml
        fm = yaml.safe_load(text[4:end])
        return fm if isinstance(fm, dict) else {}
    except Exception:
        return {}


def scan(root: Path) -> dict:
    """返回 {孤岛清单, 统计}。双无=related 空（出链）且无他卡 related 指向（入链）。"""
    cards = {}
    for fp in sorted(root.rglob("*.md")):
        if "_archive" in fp.parts:
            continue
        try:
            text = fp.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        fm = _parse_fm(text)
        if not fm.get("type"):  # 非卡（无 frontmatter type）不进扫描面
            continue
        rel = fp.relative_to(root).as_posix()
        related = fm.get("related") or []
        if isinstance(related, str):
            related = [related]
        outlinks = [str(r).strip() for r in related if str(r).strip()]
        cards[fp.stem] = {
            "path": rel, "type": str(fm.get("type", "")), "outlinks": outlinks,
            "exempt": str(fm.get("type", "")) in EXEMPT_TYPES or fp.parent.name in EXEMPT_DIRS,
        }

    # 入链反查：related 里的引用形态=stem 或路径片段
    linked = set()
    for stem, info in cards.items():
        for r in info["outlinks"]:
            linked.add(Path(r.replace("\\", "/")).stem)
    islands = []
    for stem, info in cards.items():
        if info["exempt"]:
            continue
        if not info["outlinks"] and stem not in linked:
            islands.append({"path": info["path"], "type": info["type"],
                            "domain": info["path"].split("/")[1] if "/" in info["path"] else ""})
    return {"islands": islands, "total_cards": len(cards)}


def render_md(result: dict) -> str:
    islands = result["islands"]
    by_domain: dict[str, list] = {}
    for i in islands:
        by_domain.setdefault(i["domain"] or "(根)", []).append(i)
    lines = ["# 孤岛卡清单（#528：无出链无入链=检索死胡同）", "",
             f"扫描面 {result['total_cards']} 卡，孤岛 {len(islands)} 张（agent-spec 类已豁免）。",
             "挂链批次由王语嫣编排——高优先=framework/tool 卡型（检索主靶）。", ""]
    for domain, items in sorted(by_domain.items()):
        lines.append(f"## {domain}（{len(items)}）")
        for i in items:
            lines.append(f"- `{i['path']}`（{i['type']}）")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="孤岛卡扫描（#528）")
    ap.add_argument("--stdout", action="store_true")
    args = ap.parse_args()

    result = scan(WIKI)
    n = len(result["islands"])
    print(f"🏝 孤岛卡 {n} 张 / 扫描面 {result['total_cards']} 卡（WARNING 制，不拦流转）")
    if not args.stdout:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        (OUT_DIR / "islands.json").write_text(json.dumps(result, ensure_ascii=False, indent=2),
                                              encoding="utf-8")
        (OUT_DIR / "islands.md").write_text(render_md(result), encoding="utf-8")
        print(f"📄 清单落盘: {OUT_DIR}/islands.(json|md)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
