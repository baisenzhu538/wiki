#!/usr/bin/env python3
"""check-vlm-two-section.py — VLM/OCR 卡两段式存量扫描（#540）。

扫描 30_wiki 全部 VLM/OCR 提取类卡（author 含 VLM/OCR），出两段式合规清单
（合规=正文含 AI 推断警示行）。WARNING 制不拦（exit 恒 0），清单交王语嫣裁定批次。

用法：
  python 90_control/scripts/check-vlm-two-section.py            # 扫描+清单落盘
  python 90_control/scripts/check-vlm-two-section.py --stdout   # 只打印
"""
import argparse
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
OUT_DIR = VAULT_ROOT / "60_feedback" / "auto" / "vlm-two-section"

# 与 KDO pre_submit._check_vlm_two_section 同判定（跨仓复刻，小而稳不引入跨仓依赖）
VLM_WARN_LINE = "⚠️ 以下为 AI 推断，未经交叉验证，不得作为事实引用"


def scan(root: Path) -> dict:
    """返回 {total_vlm, compliant, violations:[{path, domain}]}。"""
    total, compliant, violations = 0, 0, []
    wiki = root / "30_wiki"
    for fp in sorted(wiki.rglob("*.md")):
        if "_archive" in fp.parts:
            continue
        try:
            text = fp.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        head = text[:4096].lower()
        if "author:" not in head or ("vlm" not in head and "ocr" not in head):
            continue
        # author 行粗判（避免正文提到 VLM 误命中——只看 frontmatter author 行）
        import re
        m = re.search(r"^author:\s*(.+)$", text[:4096], re.M)
        if not m or ("vlm" not in m.group(1).lower() and "ocr" not in m.group(1).lower()):
            continue
        total += 1
        if VLM_WARN_LINE in text:
            compliant += 1
        else:
            rel = fp.relative_to(root).as_posix()
            violations.append({"path": rel, "domain": fp.parent.name})
    return {"total_vlm": total, "compliant": compliant, "violations": violations}


def main() -> int:
    ap = argparse.ArgumentParser(description="VLM/OCR 卡两段式存量扫描（#540）")
    ap.add_argument("--stdout", action="store_true")
    args = ap.parse_args()

    r = scan(VAULT_ROOT)
    n = len(r["violations"])
    print(f"📐 VLM/OCR 卡 {r['total_vlm']} 张：两段式合规 {r['compliant']} / 缺隔离 {n}（WARNING 制不拦）")
    if not args.stdout:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        (OUT_DIR / "inventory.json").write_text(json.dumps(r, ensure_ascii=False, indent=2),
                                                encoding="utf-8")
        lines = ["# VLM/OCR 卡两段式存量清单（#540）", "",
                 f"VLM 类卡 {r['total_vlm']} 张：合规 {r['compliant']} / 缺隔离 {n}。",
                 "批量挂警示段只加隔离标记不改内容——批次方案报王语嫣裁定后执行。", ""]
        for v in r["violations"]:
            lines.append(f"- `{v['path']}`")
        (OUT_DIR / "inventory.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"📄 清单落盘: {OUT_DIR}/inventory.(json|md)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
