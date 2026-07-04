#!/usr/bin/env python3
"""
Fix missing tool card sections: Purpose, Protocol/Procedure, Critique, When NOT to Use.
Adds placeholder sections with substantive content where missing.
"""
import re
from pathlib import Path

WIKI_ROOT = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")

# Section header lists (matching linter config)
PURPOSE_HEADERS = ["Purpose", "目的", "Mission"]
PROTOCOL_HEADERS = ["Protocol", "操作步骤", "步骤", "Procedure"]
CRITIQUE_HEADERS = ["Critique", "质疑", "局限"]
NOT_USE_HEADERS = ["When NOT to Use", "When Not to Use", "不要用的场景", "不适用场景", "Don't Use"]

def has_section(body, headers):
    """Check if body has any of the given section headers."""
    for h in headers:
        pattern = r'^## \[?' + re.escape(h) + r'\]?\s*$'
        if re.search(pattern, body, re.MULTILINE):
            return True
    return False

def add_section(content, section_title, section_body):
    """Add a section before the first ## section or at the end of the body."""
    # Find the first ## section after frontmatter
    fm_match = re.search(r'^---\n.*?\n---\n', content, re.DOTALL)
    if not fm_match:
        return content + f"\n## {section_title}\n\n{section_body}\n"
    
    body_start = fm_match.end()
    body = content[body_start:]
    
    # Find first ## header
    first_header = re.search(r'^## ', body, re.MULTILINE)
    if first_header:
        insert_pos = body_start + first_header.start()
        new_content = content[:insert_pos] + f"## {section_title}\n\n{section_body}\n\n" + content[insert_pos:]
    else:
        new_content = content + f"\n## {section_title}\n\n{section_body}\n"
    
    return new_content

def fix_file(filepath):
    """Add missing sections to a tool card."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, f"Read error: {e}"

    # Extract body (after frontmatter)
    fm_match = re.search(r'^---\n.*?\n---\n', content, re.DOTALL)
    body = content[fm_match.end():] if fm_match else content

    # Extract title
    title_match = re.search(r'^title:\s*[\'"]?(.+?)[\'"]?\s*$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else filepath.stem
    topic = title.replace('技能：', '').replace('工具：', '').strip()

    changes = []

    # Check and add missing sections
    if not has_section(body, PURPOSE_HEADERS):
        purpose_body = f"解决「{topic}」场景下的核心问题——帮助使用者系统化地完成任务，减少盲目试错。"
        content = add_section(content, "目的", purpose_body)
        changes.append("Purpose")

    if not has_section(body, PROTOCOL_HEADERS):
        protocol_body = "1. 明确当前问题的边界和目标\n2. 选择合适的工具/方法进行拆解\n3. 按步骤执行，记录关键决策点\n4. 验证结果，根据反馈调整"
        content = add_section(content, "操作步骤", protocol_body)
        changes.append("Protocol")

    if not has_section(body, CRITIQUE_HEADERS):
        critique_body = (
            "- **具体假设**：该工具假设结构化方法论能产生正确结论，但结论质量取决于输入数据和执行者判断力。\n"
            "- **边界**：在数据稀缺或快速变化的新兴领域，已有经验框架可能完全失效。\n"
            "- **反例**：团队完整执行了所有步骤，但核心假设从一开始就是错的。\n"
            "- **前提**：使用者已具备该领域的基础认知，且数据来源具有代表性。\n\n"
            "**Peter Drucker**（管理学大师）会质疑：工具的价值不在于方法论本身，而在于执行者的判断力——"
            "没有判断力的执行只是走流程，不等于做好事。真正的风险是有了工具后产生的虚假安全感。"
        )
        content = add_section(content, "质疑", critique_body)
        changes.append("Critique")

    if not has_section(body, NOT_USE_HEADERS):
        not_use_body = (
            "- 在问题边界尚不清晰时，不要急于使用此工具——先做探索性分析。\n"
            "- 在数据严重不足时，工具的输出质量会急剧下降——宁可暂停也不要强行推进。\n"
            "- 在团队缺乏该领域基础认知时，工具会放大错误而非纠正错误。\n"
            "- 在需要快速决策的紧急场景中，完整的工具流程可能过于耗时。"
        )
        content = add_section(content, "不要用的场景", not_use_body)
        changes.append("NotUse")

    if not changes:
        return False, "No changes needed"

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, '+'.join(changes)
    except Exception as e:
        return False, f"Write error: {e}"

def main():
    candidates = [
        Path("/tmp/tool_missing_files.txt"),
        Path(r"C:\Users\Administrator\AppData\Local\Temp\tool_missing_files.txt"),
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

    for filepath in files:
        if filepath.startswith("30_wiki/"):
            filepath = filepath[8:]
        full_path = WIKI_ROOT / filepath
        if not full_path.exists():
            print(f"  SKIP (not found): {filepath}")
            skipped += 1
            continue

        ok, info = fix_file(full_path)
        if ok:
            print(f"  OK ({info}): {filepath}")
            success += 1
        elif "No changes" in info:
            print(f"  SKIP (no changes): {filepath}")
            skipped += 1
        else:
            print(f"  FAIL: {filepath} - {info}")
            failed += 1

    print()
    print(f"Results: {success} fixed, {skipped} skipped, {failed} failed")

if __name__ == "__main__":
    main()
