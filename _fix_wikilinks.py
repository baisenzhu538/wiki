"""Fix path-format wikilinks: [[30_wiki\\concepts\\file.md]] -> [[file]]"""
import re
from pathlib import Path

root = Path(".")

# Collect all existing wiki pages by stem
existing_pages = {}
for p in (root / "30_wiki").rglob("*.md"):
    existing_pages[p.stem.lower()] = p
for p in (root / "40_outputs").rglob("*.md"):
    existing_pages[p.stem.lower()] = p

# Pattern: [[path/to/file.md]] or [[path\to\file.md]]
full_path_link = re.compile(r"\[\[([^\]|]*[/\\][^\]|]*\.md)(?:\|([^\]]+))?\]\]")

total_fixable = 0
total_applied = 0
files_touched = 0

scan_dirs = [root / "30_wiki", root / "40_outputs", root / "60_feedback"]
for scan_dir in scan_dirs:
    if not scan_dir.exists():
        continue
    for md_file in scan_dir.rglob("*.md"):
        if ".git" in md_file.parts:
            continue
        try:
            text = md_file.read_text(encoding="utf-8")
        except Exception:
            continue

        new_text = text
        file_repairs = 0

        for m in full_path_link.finditer(text):
            target_path = m.group(1).replace("\\", "/")
            display = m.group(2)
            stem = Path(target_path).stem
            stem_lower = stem.lower()

            if stem_lower in existing_pages:
                if display:
                    correct_link = f"[[{stem}|{display}]]"
                else:
                    correct_link = f"[[{stem}]]"
                old_link = m.group(0)
                new_text = new_text.replace(old_link, correct_link, 1)
                file_repairs += 1

        if file_repairs > 0:
            md_file.write_text(new_text, encoding="utf-8")
            total_applied += file_repairs
            files_touched += 1
            if files_touched <= 10:
                print(f"  Fixed {file_repairs} path-format links in {md_file.name}")

if files_touched > 10:
    print(f"  ... and {files_touched - 10} more files")

print(f"\nTotal path-format repairs: {total_applied} across {files_touched} files")
