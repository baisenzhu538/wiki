"""
Generate a 9-layer case card skeleton from VLM/OCR source files.

Usage:
    python bulk-generate-case-card.py --vlm <path> --ocr <path>               # From files
    python bulk-generate-case-card.py --card-id <id>                          # Rewrite existing card with 9-layer template
    python bulk-generate-case-card.py --vlm <path> --title "Case Title"       # Named output
    python bulk-generate-case-card.py --batch --domain <name>                 # Batch scan for thin cards

Output: Writes the card skeleton to 30_wiki/cases/ or stdout (--stdout).
Does NOT require LLM. Generates TEMPLATE with extraction hints.
"""
import argparse, re, sys
from pathlib import Path
from datetime import datetime

WIKI = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")
INBOX = Path(r"C:\Users\Administrator\Desktop\wiki\00_inbox")

NINE_LAYER_SECTIONS = [
    ("L1 业务公式/核心数字", """
从素材中提取所有定量数据：收入、成本、利润率、增长率、市场份额、用户数。
每个数字标注来源段落和置信度。缺失的数据标注"待核实"。
格式：| 指标 | 数值 | 来源 | 置信度 |
"""),
    ("L2 假设审计", """
对L1每个数字追问：
- 这个数字是事实、估算还是愿望？
- 保守/中性/乐观边界各是多少？
- 哪个数字变化10%会颠覆结论？
"""),
    ("L3 政策/行业/竞争边界", """
外部约束条件：
- 政策法规限制
- 行业准入标准
- 竞品格局和替代威胁
- 供应商/渠道依赖
"""),
    ("L4 失败模式库", """
真实失败案例中的共因和预警信号：
- 至少3个同类项目的失败案例
- 每个案例的根因
- 与你当前项目最像的失败模式是哪个？
"""),
    ("L5 隐性成本与替代方案", """
显性成本之外的：
- 机会成本
- 管理成本/沟通成本
- 用户的所有替代方案（不仅是竞品）
- 切换成本
"""),
    ("L6 执行能力缺口", """
需要的能力 vs 实际可调动的资源：
- 关键岗位人员
- 技术/供应链能力
- 时间窗口
- 资金储备
"""),
    ("L7 市场情绪/叙事风险", """
- 行业叙事是否过热？
- "躺赚""半年回本"等关键词是否出现？
- 资本是否在退出？
- 用户预期是否被拉高到不切实际？
"""),
    ("L8 边界案例与反例", """
- 看似能做但实际不能的场景
- 看似不能但实际可以的场景
- 极端情况下的表现
"""),
    ("L9 决策框架", """
综合前8层，给出：
- Go / No-Go / 需验证条件
- 最大单一风险
- 最小验证路径（最低成本获取关键信息的方法）
- 重新评估的触发信号
"""),
]

CASE_CARD_TEMPLATE = """---
id: {card_id}
title: "{title}"
type: case
status: draft
author: 老顽童
reviewed_by: 待审
confidence: 0.75
domain:
  - {domain}
created_at: {date}
source_refs:
  - {vlm_ref}
  - {ocr_ref}
related:
---

# {title}

> 一句话概括：<填>

## 背景

<项目/公司/行业背景，2-3句>

## {sections}

## Critique

### 内部局限
<素材本身的局限和盲区>

### 外部攻击者
| 攻击者 | 可能反驳 |
|--------|---------|
| <学者1> | <反驳观点> |
| <学者2> | <反驳观点> |

### 不适用的场景
<什么情况下这个案例的经验不适用>

## Synthesis

<与其他卡片的关联、矛盾、互补。本案例的核心教训是什么？>

## Action Triggers

<用户看到什么信号时应该读这个案例？>

## Source VLM/OCR Notes

### VLM 描述中的关键信息
<待提取>

### OCR 文本中的关键段落
<待提取>
"""

def safe_read(f):
    if not f.exists(): return None
    for enc in ['utf-8', 'gbk', 'latin-1']:
        try: return f.read_text(encoding=enc)
        except: continue
    return None

def extract_numbers(text):
    """Extract anything that looks like a number+unit pair."""
    patterns = [
        r'\d+[\d,.]*\s*[万亿千百兆]?[元美元港元欧元日元英镑]',  # currency
        r'\d+[\d,.]*\s*%',  # percentage
        r'\d+[\d,.]*\s*[个人次家台辆件笔单]',  # quantities
        r'\d+[\d,.]*\s*[年月日天周季度][以內内前后来]?',  # time
    ]
    found = []
    for pat in patterns:
        found.extend(re.findall(pat, text))
    return found

def generate(card_id, title, vlm_text, ocr_text, domain, stdout=False):
    """Generate a 9-layer case card skeleton."""
    all_text = (vlm_text or "") + "\n" + (ocr_text or "")
    numbers = extract_numbers(all_text)

    # Build sections
    sections_md = ""
    for section_name, hint in NINE_LAYER_SECTIONS:
        sections_md += f"## {section_name}\n\n"
        sections_md += f"<!-- {hint.strip()} -->\n\n"
        if numbers and "数字" in section_name:
            sections_md += "| 指标 | 数值 | 来源 | 置信度 |\n|------|------|------|--------|\n"
            for n in numbers[:10]:
                sections_md += f"| ? | {n} | <待标注> | 待核实 |\n"
        sections_md += "<待填充>\n\n"

    vlm_ref = "VLM_PATH"
    ocr_ref = "OCR_PATH"

    card = CASE_CARD_TEMPLATE.format(
        card_id=card_id,
        title=title,
        domain=domain or "<填>",
        date=datetime.now().strftime("%Y-%m-%d"),
        vlm_ref=vlm_ref,
        ocr_ref=ocr_ref,
        sections=sections_md,
    )

    if stdout:
        print(card)
    else:
        out_path = WIKI / "cases" / f"{card_id}.md"
        out_path.write_text(card, encoding="utf-8")
        print(f"Written: {out_path}")
        print(f"Numbers found in source: {len(numbers)}")
        if numbers:
            print(f"  Sample: {numbers[:8]}")

def batch_thin(domain, dry_run=True):
    """Find case cards in domain with <80 lines and generate templates."""
    thin_cards = []
    for f in sorted(WIKI.rglob("*.md")):
        if any(p in str(f) for p in ["_archive", "index.md", "log.md"]): continue
        text = safe_read(f)
        if not text: continue
        fm_end = text.find("---", 3)
        if fm_end == -1: continue
        body = text[fm_end+3:]
        lines = [l for l in body.split("\n") if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("<!--")]

        fm = {}
        for line in text[3:fm_end].split("\n"):
            if ":" in line:
                k, _, v = line.partition(":")
                fm[k.strip()] = v.strip()

        if fm.get("type") != "case": continue
        if domain and domain not in str(fm.get("domain", "")): continue

        if len(lines) < 80:
            thin_cards.append({"id": fm.get("id", f.stem), "path": str(f.relative_to(WIKI)), "lines": len(lines), "file": f})

    print(f"Thin case cards in '{domain or 'all'}': {len(thin_cards)}")
    for c in thin_cards:
        print(f"  [{c['lines']} lines] {c['id']}  ({c['path']})")
    return thin_cards

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--vlm")
    p.add_argument("--ocr")
    p.add_argument("--card-id")
    p.add_argument("--title", default="未命名案例")
    p.add_argument("--domain", default="")
    p.add_argument("--stdout", action="store_true")
    p.add_argument("--batch", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    if args.batch:
        batch_thin(args.domain, dry_run=args.dry_run)
        return

    vlm_text = safe_read(Path(args.vlm)) if args.vlm else None
    ocr_text = safe_read(Path(args.ocr)) if args.ocr else None

    if not vlm_text and not ocr_text and not args.card_id:
        print("ERROR: Need --vlm, --ocr, or --card-id")
        sys.exit(1)

    card_id = args.card_id or f"case-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

    if vlm_text: print(f"VLM: {len(vlm_text)} chars")
    if ocr_text: print(f"OCR: {len(ocr_text)} chars")

    generate(card_id, args.title, vlm_text, ocr_text, args.domain, stdout=args.stdout)

if __name__ == "__main__":
    main()
