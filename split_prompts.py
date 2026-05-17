"""Split prompt-best-practices-collection.md into domain-specific files.

Key insight: top-level sections are separated by ``---\\n\\n## N.``.
Internal subsections (e.g. ``## 1. 分析结论`` inside section 34) are NOT
preceded by ``---`` and must be kept intact with their parent section.
"""
import re
from pathlib import Path

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
SRC = VAULT / "00_inbox" / "prompt-best-practices-collection.md"
OUT_DIR = VAULT / "00_inbox" / "prompts"
DESIGN_DIR = VAULT / "00_inbox" / "design" / "prompts"

ROUTING = {
    1:  "writing-content.md",
    2:  "learning-thinking.md",
    3:  "writing-content.md",
    4:  "business-analysis.md",
    5:  "business-analysis.md",
    6:  "writing-content.md",
    7:  "business-analysis.md",
    8:  "product-ux.md",
    9:  "writing-content.md",
    10: "writing-content.md",
    11: "business-analysis.md",
    12: "learning-thinking.md",
    13: "meta-prompt-eng.md",
    14: "meta-prompt-eng.md",
    15: "product-ux.md",
    16: "product-ux.md",
    17: "product-ux.md",
    18: "product-ux.md",
    19: "learning-thinking.md",
    20: "tools-workflows.md",
    21: "tools-workflows.md",
    22: "learning-thinking.md",
    23: "learning-thinking.md",
    24: "meta-prompt-eng.md",
    25: "learning-thinking.md",
    26: "tools-workflows.md",
    27: "business-analysis.md",
    28: "writing-content.md",
    29: "design/ai-image-generation.md",  # NANO BANANA PRO → design folder
    30: "writing-content.md",
    31: "tools-workflows.md",
    32: "business-analysis.md",
    33: "business-analysis.md",
    34: "business-analysis.md",
    35: "learning-thinking.md",
    36: "tools-workflows.md",
    37: "writing-content.md",
    38: "product-ux.md",
    39: "tools-workflows.md",
    40: "tools-workflows.md",
    41: "tools-workflows.md",
    42: "writing-content.md",
    43: "business-analysis.md",
    44: "business-analysis.md",
    45: "business-analysis.md",
    46: "business-analysis.md",
    47: "business-analysis.md",
    48: "business-analysis.md",
    49: "product-ux.md",
    50: "learning-thinking.md",
    51: "meta-prompt-eng.md",
    52: "learning-thinking.md",
    53: "learning-thinking.md",
    54: "meta-prompt-eng.md",
    55: "tools-workflows.md",
    56: "product-ux.md",
    57: "business-analysis.md",
    58: "writing-content.md",
}

# Top-level sections are separated by --- followed by ## N.
SECTION_SPLIT_RE = re.compile(r"\n---\n\n(?=## (\d+)\. )")


def main():
    text = SRC.read_text(encoding="utf-8")

    # Split at top-level separators
    parts = SECTION_SPLIT_RE.split(text)
    # parts is like: [header_before_first_section, "1", section1_body,
    #                  "2", section2_body, "3", section3_body, ...]

    if not parts:
        print("ERROR: no sections found")
        return

    header = parts[0]  # TOC + intro
    del parts[0]

    # Now parts alternates: num_str, body, num_str, body, ...
    sections = {}  # num → text
    for i in range(0, len(parts), 2):
        if i + 1 >= len(parts):
            break
        num_str = parts[i]
        body = parts[i + 1]
        num = int(num_str)
        # Reconstruct the full section including the ## header
        sections[num] = f"## {num}. {body.lstrip().split(chr(10), 1)[-1] if body.strip() else ''}"

    # Hmm, the regex splits BEFORE the ## N. heading, so the heading text is in the next part.
    # Let me re-read the split behavior...
    # Actually re.split with capture group: the separator match is removed, and captured groups are inserted.
    # Pattern: \n---\n\n(?=## (\d+)\. )
    # The (?=...) is a lookahead, not a capture. The only capture is (\d+).
    # So after split: [text_before], ["1", rest_of_section1_with_heading], ["2", rest_of_section2], ...
    # Where rest_of_sectionN starts with "## N. ..."

    # Wait, \n---\n\n is consumed (deleted), (?=## (\d+)\. ) is lookahead so NOT consumed.
    # Captured group (\d+) is inserted.
    # So:
    # parts[0] = everything before first "\n---\n\n## N."
    # parts[1] = "1" (captured digit)
    # parts[2] = "## 1. 自动化写文章\n\n..." (everything after the lookahead match, until next separator)
    # parts[3] = "2"
    # parts[4] = "## 2. 复盘大师提示词\n\n..."
    # ...

    # OK so the logic above needs fixing. Let me just redo this more carefully.
    # Actually my logic above was:
    # - parts[0] = header
    # - parts[1] = "1", parts[2] = section 1 body (which starts with "## 1. ...")
    # - parts[3] = "2", parts[4] = section 2 body
    # My code:
    # for i in range(0, len(parts), 2):
    #     if i+1 < len(parts): num_str = parts[i], body = parts[i+1]
    # This gets: num_str="1", body=section_1, then num_str=section_1_body (which fails int()), etc.
    # WRONG. The pattern is: parts[0]=header, parts[1]=capture1, parts[2]=body1, parts[3]=capture2, parts[4]=body2
    # Starting from index 1: i=1,3,5,... num_str=parts[i], body=parts[i+1]
    # Let me fix this starting index.

    print("Top-level sections detected:")
    for i in range(1, len(parts) - 1, 2):
        num_str = parts[i]
        body = parts[i + 1]
        num = int(num_str)
        # Extract the heading line
        body_lines = body.strip().split("\n", 1)
        heading = body_lines[0] if body_lines else f"## {num}."
        sections[num] = body.strip()
        print(f"  #{num}: {heading[:80]}")

    # Now group by output file
    outputs = {}
    for num, body in sections.items():
        fname = ROUTING.get(num)
        if fname is None:
            print(f"  WARNING: section {num} not routed — skipping")
            continue
        outputs.setdefault(fname, []).append((num, body))

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    DESIGN_DIR.mkdir(parents=True, exist_ok=True)

    total_sections = 0
    for fname, entries in sorted(outputs.items()):
        if fname.startswith("design/"):
            out_path = DESIGN_DIR / fname.replace("design/", "")
        else:
            out_path = OUT_DIR / fname

        safe_name = fname.replace(".md", "").replace("-", " ").replace("/", " / ").title()
        header = f"# {safe_name}\n\n"
        header += "> 拆分自 `00_inbox/prompt-best-practices-collection.md`\n"
        header += f"> 条目数：{len(entries)}\n\n---\n\n"

        body_parts = [header]
        for num, body in sorted(entries, key=lambda x: x[0]):
            body_parts.append(body)
            body_parts.append("\n---\n")

        out_path.write_text("\n".join(body_parts), encoding="utf-8")
        print(f"  {fname}: {len(entries)} sections → {out_path}")
        total_sections += len(entries)

    print(f"\nSplit {total_sections} sections into {len(outputs)} files.")
    print(f"  {OUT_DIR}/")
    for f in sorted(OUT_DIR.iterdir()):
        if f.is_file():
            size_kb = f.stat().st_size / 1024
            print(f"    {f.name}  ({size_kb:.0f} KB)")
    if DESIGN_DIR.exists():
        print(f"  {DESIGN_DIR}/")
        for f in sorted(DESIGN_DIR.iterdir()):
            if f.is_file():
                size_kb = f.stat().st_size / 1024
                print(f"    {f.name}  ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
