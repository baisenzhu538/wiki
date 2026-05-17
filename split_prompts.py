"""Split prompt-best-practices-collection.md into domain-specific files.

Top-level sections are detected by the ``---\\n\\n## N.`` boundary pattern.
Internal subsections lack the preceding ``---`` and stay with their parent.
"""
import re
from pathlib import Path

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
SRC = VAULT / "00_inbox" / "prompt-best-practices-collection.md"
OUT_DIR = VAULT / "00_inbox" / "prompts"
DESIGN_DIR = VAULT / "00_inbox" / "design" / "prompts"

ROUTING = {
    1:  "writing-content.md",      2:  "learning-thinking.md",
    3:  "writing-content.md",      4:  "business-analysis.md",
    5:  "business-analysis.md",    6:  "writing-content.md",
    7:  "business-analysis.md",    8:  "product-ux.md",
    9:  "writing-content.md",     10:  "writing-content.md",
    11: "business-analysis.md",   12:  "learning-thinking.md",
    13: "meta-prompt-eng.md",     14:  "meta-prompt-eng.md",
    15: "product-ux.md",          16:  "product-ux.md",
    17: "product-ux.md",          18:  "product-ux.md",
    19: "learning-thinking.md",   20:  "tools-workflows.md",
    21: "tools-workflows.md",     22:  "learning-thinking.md",
    23: "learning-thinking.md",   24:  "meta-prompt-eng.md",
    25: "learning-thinking.md",   26:  "tools-workflows.md",
    27: "business-analysis.md",   28:  "writing-content.md",
    29: "design/ai-image-generation.md",
    30: "writing-content.md",     31:  "tools-workflows.md",
    32: "business-analysis.md",   33:  "business-analysis.md",
    34: "business-analysis.md",   35:  "learning-thinking.md",
    36: "tools-workflows.md",     37:  "writing-content.md",
    38: "product-ux.md",          39:  "tools-workflows.md",
    40: "tools-workflows.md",     41:  "tools-workflows.md",
    42: "writing-content.md",     43:  "business-analysis.md",
    44: "business-analysis.md",   45:  "business-analysis.md",
    46: "business-analysis.md",   47:  "business-analysis.md",
    48: "business-analysis.md",   49:  "product-ux.md",
    50: "learning-thinking.md",   51:  "meta-prompt-eng.md",
    52: "learning-thinking.md",   53:  "learning-thinking.md",
    54: "meta-prompt-eng.md",     55:  "tools-workflows.md",
    56: "product-ux.md",          57:  "business-analysis.md",
    58: "writing-content.md",
}

BOUNDARY_RE = re.compile(r"\n---\n\n## (\d+)\. ")


def main():
    text = SRC.read_text(encoding="utf-8")

    # Find all top-level section boundaries
    matches = list(BOUNDARY_RE.finditer(text))
    if not matches:
        print("ERROR: no section boundaries found")
        return

    # Extract sections
    sections = {}
    for i, m in enumerate(matches):
        num = int(m.group(1))
        content_start = m.end()  # right after "## N. "
        if i + 1 < len(matches):
            content_end = matches[i + 1].start() + 1  # include the \n before next "---"
        else:
            content_end = len(text)
        section_text = f"## {num}. " + text[content_start:content_end]
        sections[num] = section_text.rstrip("\n") + "\n"
        heading = section_text.strip().split("\n")[0]
        print(f"  #{num:2d}: {heading[:90]}")

    # Group by output file
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
    for fname in sorted(outputs):
        entries = outputs[fname]
        if fname.startswith("design/"):
            out_path = DESIGN_DIR / fname.replace("design/", "")
        else:
            out_path = OUT_DIR / fname

        safe_name = fname.replace(".md", "").replace("-", " ").replace("/", " / ").title()
        header = (
            f"# {safe_name}\n\n"
            f"> 拆分自 `00_inbox/prompt-best-practices-collection.md`\n"
            f"> 条目数：{len(entries)}\n\n---\n\n"
        )

        parts = [header]
        for num, body in sorted(entries, key=lambda x: x[0]):
            parts.append(body.strip())
            parts.append("\n---\n")

        out_path.write_text("\n".join(parts), encoding="utf-8")
        print(f"  → {fname}: {len(entries)} sections ({out_path.stat().st_size // 1024} KB)")
        total_sections += len(entries)

    print(f"\n✓ Split {total_sections} sections into {len(outputs)} files.")
    print(f"  {OUT_DIR}/")
    for f in sorted(OUT_DIR.iterdir()):
        if f.is_file():
            print(f"    {f.name}  ({f.stat().st_size // 1024} KB)")
    if DESIGN_DIR.exists() and any(DESIGN_DIR.iterdir()):
        print(f"  {DESIGN_DIR}/")
        for f in sorted(DESIGN_DIR.iterdir()):
            if f.is_file():
                print(f"    {f.name}  ({f.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
