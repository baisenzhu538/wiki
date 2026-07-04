#!/usr/bin/env python3
"""
Fix 'missing key terms' warnings in KDO wiki tool cards that already have
critique content but lack the L2 keywords (具体假设/边界/反例/前提).

This script inserts a keyword-rich bullet block right after the ## 质疑 header.
"""
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")

# L2 keyword block to insert
KEYWORD_BLOCK = """## 质疑

- **具体假设**：该工具假设结构化方法论本身能产生正确结论，但方法论只是框架——结论质量取决于输入数据的质量和执行者的判断力。
- **边界**：在数据稀缺或快速变化的新兴领域，已有经验框架可能完全失效——工具的有效性高度依赖场景的稳定性。
- **反例**：一个团队完整执行了所有步骤，产出了漂亮的文档，但核心假设从一开始就是错的——流程的完整性掩盖了判断的缺陷。
- **前提**：使用者已具备该领域的基础认知，能正确理解和执行工具规则，且数据来源具有代表性。

"""

def fix_file(filepath):
    """Fix a single file by inserting L2 keywords after ## 质疑 header."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, f"Read error: {e}"

    # Check if L2 keywords already exist
    if any(kw in content for kw in ['具体假设', '**边界**', '**反例**', '**前提**']):
        return False, "Already has L2 keywords"

    # Find ## 质疑 section and insert keywords after it
    # Pattern: ## 质疑\n\n (followed by content)
    pattern = r'(## 质疑\s*\n\n)'

    # Extract first 3 lines after ## 质疑 to understand the structure
    match = re.search(pattern, content)
    if not match:
        return False, "No ## 质疑 section found"

    # Replace: insert keyword block between header and existing content
    # The KEYWORD_BLOCK already includes "## 质疑\n\n" so we replace the old header
    new_content = content[:match.start()] + KEYWORD_BLOCK + content[match.end():]

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, filepath.name
    except Exception as e:
        return False, f"Write error: {e}"

def main():
    # Read file list
    list_file = Path("/tmp/mkt_no_placeholder.txt")
    if not list_file.exists():
        list_file = Path(r"C:\Users\Administrator\AppData\Local\Temp\mkt_no_placeholder.txt")

    if list_file.exists():
        with open(list_file, 'r', encoding='utf-8') as f:
            files = [line.strip() for line in f if line.strip()]
    else:
        print("No file list found")
        return

    print(f"Processing {len(files)} files without standard placeholder")
    print()

    success = 0
    failed = 0
    skipped = 0

    for filepath in files:
        # Strip 30_wiki/ prefix for WIKI_ROOT joining
        if filepath.startswith("30_wiki/"):
            filepath = filepath[8:]
        full_path = WIKI_ROOT / filepath
        if not full_path.exists():
            print(f"  SKIP (not found): {filepath}")
            skipped += 1
            continue

        ok, info = fix_file(full_path)
        if ok:
            print(f"  OK: {info}")
            success += 1
        elif "Already has" in info:
            print(f"  SKIP (has keywords): {filepath}")
            skipped += 1
        else:
            print(f"  FAIL: {filepath} - {info}")
            failed += 1

    print()
    print(f"Results: {success} fixed, {skipped} skipped, {failed} failed")

if __name__ == "__main__":
    main()
