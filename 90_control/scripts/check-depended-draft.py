#!/usr/bin/env python3
"""check-depended-draft.py — 被依赖卡 draft 门禁（#527）。

口径：被消费端活依赖（agent-spec / CLAUDE.md / SOUL.md / 工具数据链硬引用）的
30_wiki 卡若 status: draft → 违反 E018 精神（被消费的资产必须先过审）。
- 存量违例（baseline 在册）→ WARNING 出清单（不拦截）
- 新引用违例（不在 baseline）→ ERROR（exit 1，只向前生效，红线 4 误拦优先）
- draft 本身无罪——无引用的 draft 卡不报警

数据源（引用面）：根 CLAUDE.md/AGENTS.md、agents/**/(CLAUDE|SOUL|AGENTS).md、
30_wiki/agent-specs/*.md、kdo-tools/*.py、cap_hub/*.py。
引用识别：30_wiki 相对路径字面量 + draft 卡 stem 词边界匹配（长 kebab 名误报率低）。

用法：
  python 90_control/scripts/check-depended-draft.py            # 门禁（exit 1=有新违例）
  python 90_control/scripts/check-depended-draft.py --update-baseline   # 存量登记为 baseline
  python 90_control/scripts/check-depended-draft.py --inventory         # 出存量清单（json+md）
"""
import argparse
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
BASELINE = VAULT_ROOT / "90_control" / "quality-gates" / "depended-draft-baseline.json"
INV_DIR = VAULT_ROOT / "60_feedback" / "auto" / "depended-draft"

REF_SOURCE_GLOBS = [
    "CLAUDE.md", "AGENTS.md",
    "agents/*/CLAUDE.md", "agents/*/SOUL.md", "agents/*/AGENTS.md",
    "30_wiki/agent-specs/*.md",
    "kdo-tools/*.py", "cap_hub/*.py",
]


def _card_meta(fp: Path) -> tuple[str, str]:
    """读 frontmatter 头部 → (status, type)。"""
    try:
        text = fp.read_text(encoding="utf-8", errors="replace")[:4096]
    except OSError:
        return "", ""
    m = re.search(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return "", ""
    s = re.search(r"^status:\s*(\S+)", m.group(1), re.M)
    t = re.search(r"^type:\s*(\S+)", m.group(1), re.M)
    return (s.group(1) if s else "", t.group(1) if t else "")


# 非卡资产（索引/日志）不算知识卡——log.md/index.md 是写入路径不是消费依赖（#527 初扫误报实证）
_NON_CARD_TYPES = {"index", "log"}


def scan_draft_cards(root: Path) -> dict[str, str]:
    """30_wiki 下 status:draft 的知识卡 → {stem: 相对路径}（index/log 类非卡资产除外）。"""
    out = {}
    wiki = root / "30_wiki"
    if not wiki.is_dir():
        return out
    for fp in wiki.rglob("*.md"):
        if "_archive" in fp.parts:
            continue
        status, ctype = _card_meta(fp)
        if status == "draft" and ctype not in _NON_CARD_TYPES:
            out[fp.stem] = fp.relative_to(root).as_posix()
    return out


def scan_references(root: Path) -> dict[str, str]:
    """引用面文件 → {相对路径: 全文}。"""
    out = {}
    for pattern in REF_SOURCE_GLOBS:
        for fp in root.glob(pattern):
            if fp.is_file():
                try:
                    out[fp.relative_to(root).as_posix()] = fp.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
    return out


def find_violations(root: Path) -> list[tuple[str, str]]:
    """返回 [(引用源, 被引 draft 卡路径)] 违例对。

    引用识别三路：①30_wiki 相对路径字面量 ②draft 卡 stem 词边界匹配
    ③30_wiki glob 模式（如 30_wiki/frameworks/framework-truman-feature-*.md——
    agent 配置的数据链常写 glob，fnmatch 展开匹配）。"""
    import fnmatch
    drafts = scan_draft_cards(root)
    if not drafts:
        return []
    refs = scan_references(root)
    violations = []
    for src, text in sorted(refs.items()):
        glob_pats = re.findall(r"30_wiki/[^\s`\"')]*\*[^\s`\"')]*", text)
        for stem, rel in drafts.items():
            if rel == src:
                continue  # 卡自身不算引用源
            if (rel in text
                    or re.search(rf"(?<![\w-]){re.escape(stem)}(?![\w-])", text)
                    or any(fnmatch.fnmatch(rel, pat) for pat in glob_pats)):
                violations.append((src, rel))
    return violations


def main() -> int:
    ap = argparse.ArgumentParser(description="被依赖卡 draft 门禁（#527）")
    ap.add_argument("--update-baseline", action="store_true", help="当前违例登记为 baseline（存量起步用）")
    ap.add_argument("--inventory", action="store_true", help="出存量清单（json+md 交王语嫣）")
    args = ap.parse_args()

    violations = find_violations(VAULT_ROOT)
    keys = sorted(f"{s} → {c}" for s, c in violations)

    if args.update_baseline:
        BASELINE.parent.mkdir(parents=True, exist_ok=True)
        BASELINE.write_text(json.dumps({"violations": keys}, ensure_ascii=False, indent=2),
                            encoding="utf-8")
        print(f"📋 baseline 已登记 {len(keys)} 条存量违例: {BASELINE}")
        return 0

    if args.inventory:
        INV_DIR.mkdir(parents=True, exist_ok=True)
        (INV_DIR / "inventory.json").write_text(
            json.dumps([{"source": s, "card": c} for s, c in violations], ensure_ascii=False, indent=2),
            encoding="utf-8")
        lines = ["# 被依赖 draft 卡存量清单（#527）", "",
                 f"共 {len(violations)} 条引用违例（被活依赖但 status=draft）。欧阳锋按此排优先过审。", ""]
        for s, c in violations:
            lines.append(f"- `{c}` ← 被 `{s}` 引用")
        (INV_DIR / "inventory.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"📄 清单落盘: {INV_DIR}/inventory.(json|md)（{len(violations)} 条）")
        return 0

    baseline = set()
    if BASELINE.exists():
        try:
            baseline = set(json.loads(BASELINE.read_text(encoding="utf-8")).get("violations", []))
        except (OSError, json.JSONDecodeError):
            pass
    new = [k for k in keys if k not in baseline]
    known = [k for k in keys if k in baseline]

    for k in known:
        print(f"🟡 WARNING（存量在册）: {k}")
    for k in new:
        print(f"🔴 ERROR（新引用违例）: {k}——被依赖卡须先过审（E018），或将引用源移出数据链")
    print(f"\n被依赖 draft 违例: 新 {len(new)} / 存量 {len(known)}（draft 无引用不报警）")
    return 1 if new else 0


if __name__ == "__main__":
    sys.exit(main())
