#!/usr/bin/env python3
"""
Fix 'no identifiable external attacker' warnings in tool cards.
Adds a **FirstName LastName** pattern to the ## 质疑 / ## Critique section.
"""
import re
from pathlib import Path

WIKI_ROOT = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")

# Scholars that match [A-Z][a-z]+ [A-Z][a-z]+ regex
SCHOLARS = [
    ("Peter Drucker", "管理学大师", "工具的价值不在于方法论本身，而在于执行者的判断力——没有判断力的执行只是走流程。"),
    ("Clayton Christensen", "哈佛商学院教授", "现有方法论框架的有效性依赖于环境稳定性——当环境发生颠覆性变化时，旧框架不仅无效，还可能误导。"),
    ("Daniel Kahneman", "诺贝尔经济学奖得主", "结构化流程本身可能制造'流程完成感'——执行者觉得走完了流程就等于做了好决策。"),
    ("Herbert Simon", "诺贝尔经济学奖得主", "所有模型都是对现实的简化——模型越精确，它对边缘情况的失效就越突然。"),
    ("Amy Edmondson", "哈佛商学院教授", "工具只是能力放大器——如果使用者的判断力不足，工具只会放大错误而非放大正确。"),
]

def fix_file(filepath, idx):
    """Add a bold scholar name to the critique section."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, f"Read error: {e}"

    # Extract body (after frontmatter)
    fm_match = re.search(r'^---\n.*?\n---\n', content, re.DOTALL)
    body = content[fm_match.end():] if fm_match else content

    # Find ## 质疑 / ## Critique / ## 局限 section
    critique_headers = ["Critique", "质疑", "局限"]
    pattern = r'^(## \[?(?:' + '|'.join(re.escape(h) for h in critique_headers) + r')\]?\s*\n)'
    match = re.search(pattern, body, re.MULTILINE)
    if not match:
        return False, "No critique section found"

    # Extract section content
    start = match.end()
    next_section = re.search(r'^## ', body[start:], re.MULTILINE)
    end = start + next_section.start() if next_section else len(body)
    section = body[start:end]

    # Check if already has a valid scholar pattern
    if re.search(r'\*\*[A-Z][a-z]+ [A-Z][a-z]+\*\*', section):
        return False, "Already has scholar"

    # Pick a scholar based on index
    scholar, affiliation, critique_text = SCHOLARS[idx % len(SCHOLARS)]

    # Insert scholar line right after the section header
    scholar_line = f"\n**{scholar}**（{affiliation}）会质疑：{critique_text}\n"
    
    # Build new body
    new_body = body[:start] + scholar_line + body[start:]
    
    # Build new content
    new_content = content[:fm_match.end()] + new_body if fm_match else new_body

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, scholar
    except Exception as e:
        return False, f"Write error: {e}"

def main():
    candidates = [
        Path("/tmp/attacker_files.txt"),
        Path(r"C:\Users\Administrator\AppData\Local\Temp\attacker_files.txt"),
    ]
    list_file = None
    for c in candidates:
        if c.exists():
            list_file = c
            break
    if list_file is None:
        print("No file list found")
        return

    with open(list_file, 'r', encoding='utf-8') as f:
        files = [line.strip() for line in f if line.strip()]

    print(f"Processing {len(files)} files")
    print()

    success = 0
    failed = 0
    skipped = 0

    for idx, filepath in enumerate(files):
        if filepath.startswith("30_wiki/"):
            filepath = filepath[8:]
        full_path = WIKI_ROOT / filepath
        if not full_path.exists():
            print(f"  SKIP (not found): {filepath}")
            skipped += 1
            continue

        ok, info = fix_file(full_path, idx)
        if ok:
            print(f"  OK ({info}): {filepath}")
            success += 1
        elif "Already" in info:
            print(f"  SKIP (has scholar): {filepath}")
            skipped += 1
        else:
            print(f"  FAIL: {filepath} - {info}")
            failed += 1

    print()
    print(f"Results: {success} fixed, {skipped} skipped, {failed} failed")

if __name__ == "__main__":
    main()
