"""Split prompt-best-practices-collection.md into domain-specific files."""
import re
from pathlib import Path

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
SRC = VAULT / "00_inbox" / "prompt-best-practices-collection.md"
OUT_DIR = VAULT / "00_inbox" / "prompts"
DESIGN_DIR = VAULT / "00_inbox" / "design" / "prompts"

# Section number → output filename
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
    29: "../design/prompts/ai-image-generation.md",  # NANO BANANA PRO
    30: "writing-content.md",
    31: "tools-workflows.md",
    32: "business-analysis.md",
    33: "business-analysis.md",
    34: "business-analysis.md",
    35: "learning-thinking.md",
    36: "tools-workflows.md",
    37: "writing-content.md",
    38: "product-ux.md",
    39: "tools-workflows.md",  # 图片反推提示词网站 → tools
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

SECTION_RE = re.compile(r"^## (\d+)\. ")

def main():
    text = SRC.read_text(encoding="utf-8")
    lines = text.split("\n")

    # Find section boundaries
    sections = {}  # num → (start_line, end_line, title)
    current_num = None
    current_start = None

    for i, line in enumerate(lines):
        m = SECTION_RE.match(line)
        if m:
            num = int(m.group(1))
            # Close previous section
            if current_num is not None:
                sections[current_num] = (current_start, i, current_title)
            # Start new section
            current_num = num
            current_start = i
            current_title = line

    # Close last section
    if current_num is not None:
        sections[current_num] = (current_start, len(lines), current_title)

    # Collect output files: filename → [(num, start, end)]
    outputs = {}
    for num, (start, end, title) in sections.items():
        fname = ROUTING.get(num)
        if fname is None:
            print(f"  WARNING: section {num} not routed — skipping")
            continue
        outputs.setdefault(fname, []).append((num, start, end, title))

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    DESIGN_DIR.mkdir(parents=True, exist_ok=True)

    total_sections = 0
    for fname, entries in sorted(outputs.items()):
        # Resolve path
        if fname.startswith(".."):
            out_path = OUT_DIR / fname
        else:
            out_path = OUT_DIR / fname

        # Build file: header + each section's lines
        header = f"# {fname.replace('.md','').replace('-',' ').title()}\n\n"
        header += "> 拆分自 `00_inbox/prompt-best-practices-collection.md`\n"
        header += f"> 条目数：{len(entries)}\n\n---\n\n"

        body_parts = [header]
        for num, start, end, title in sorted(entries, key=lambda x: x[0]):
            section_lines = lines[start:end]
            body_parts.append("\n".join(section_lines))
            body_parts.append("\n")

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
