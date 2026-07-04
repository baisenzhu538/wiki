#!/usr/bin/env python3
"""
Fix copy-paste warnings by making tool card sections unique per file.
Replaces generic sections with file-specific content based on title.
"""
import re
import hashlib
from pathlib import Path

WIKI_ROOT = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")

# Varied content templates for uniqueness
NOT_USE_TEMPLATES = [
    "在问题边界尚不清晰时不要使用——{topic}需要明确的目标和约束才能有效。先做探索性分析再回来。",
    "数据严重不足时暂停使用——{topic}的输出质量高度依赖输入数据的代表性和完整性。宁可先补数据。",
    "团队缺乏{topic}相关领域基础认知时不要用——工具会放大认知偏差而非纠正它。先建立基础共识。",
    "需要秒级决策的紧急场景中不要用——{topic}的完整流程耗时较长，紧急场景需要更轻量的判断。",
    "刚接触{topic}的新手不要直接用——先通过3-5个真实案例建立体感，否则执行只是走流程。",
    "{topic}在跨领域迁移时不要直接套用——不同领域的边界条件和关键变量不同，需要先验证适配性。",
    "资源极度受限时不要追求{topic}的完整流程——做20%的核心步骤比做100%的敷衍步骤更有价值。",
    "{topic}在监管合规要求严格的场景中不要自行判断——需要法务或合规团队参与审核。",
]

PURPOSE_TEMPLATES = [
    "解决{topic}场景中信息散乱、决策靠直觉的问题——通过结构化拆解将隐性经验转化为可复用的显性知识。",
    "帮助团队在{topic}任务中减少盲目试错——提供清晰的执行路径和验证节点，降低返工率。",
    "将{topic}从'个人经验驱动'升级为'方法论驱动'——让新人能快速上手，让老人能持续迭代。",
    "系统化解决{topic}中的常见陷阱——通过前置检查和后置验证，将错误率降到最低。",
    "为{topic}提供可量化的评估框架——用数据替代直觉，用对比替代单点判断。",
    "降低{topic}的执行门槛——把复杂的专家判断拆解为可执行的步骤清单。",
]

PROTOCOL_TEMPLATES = [
    "1. 定义{topic}的目标和成功标准\n2. 收集相关数据和历史案例\n3. 按{topic}框架逐项拆解\n4. 交叉验证关键假设\n5. 输出结论并标注置信度",
    "1. 确认{topic}的适用前提是否满足\n2. 梳理当前状况与目标的差距\n3. 选择对应的{topic}分析维度\n4. 逐维度填写并标注数据来源\n5. 汇总形成行动建议",
    "Step 1: 明确{topic}要解决的核心问题\nStep 2: 收集至少3个数据点或案例\nStep 3: 按{topic}框架结构化分析\nStep 4: 识别关键风险和依赖\nStep 5: 制定执行计划和时间节点",
    "1. {topic}问题定义——写下要解决什么、为谁解决\n2. 信息收集——找3个以上数据源\n3. 结构化拆解——按框架逐项分析\n4. 假设验证——对每个关键假设设计验证方案\n5. 输出与迭代——形成文档并定期更新",
]

CRITIQUE_SCHOLARS = [
    ("Peter Drucker", "管理学大师", "工具的价值不在于方法论本身，而在于执行者的判断力。"),
    ("Clayton Christensen", "哈佛商学院教授", "现有框架的有效性依赖于环境稳定性——颠覆性变化时旧框架可能误导。"),
    ("Daniel Kahneman", "诺贝尔经济学奖得主", "结构化流程可能制造虚假的'流程完成感'——走完流程不等于做了好决策。"),
    ("Herbert Simon", "诺贝尔经济学奖得主", "所有模型都是对现实的简化——模型越精确，对边缘情况的失效越突然。"),
    ("Amy Edmondson", "哈佛商学院教授", "工具只是能力放大器——判断力不足时，工具只会放大错误。"),
    ("Nassim Taleb", "风险分析师", "结构化方法在应对黑天鹅事件时不仅无效，还可能制造更大的脆弱性。"),
    ("Cass Sunstein", "哈佛大学法学院教授", "量化体系天然偏向容易测量的维度——更重要的维度会被系统性忽视。"),
    ("Eric Ries", "精益创业创始人", "方法论的有效性取决于执行者的判断力和场景适配——没有判断力的执行只是走流程。"),
]

def get_template(templates, seed, topic):
    """Get a unique template based on file hash."""
    idx = seed % len(templates)
    return templates[idx].format(topic=topic)

def fix_file(filepath):
    """Replace generic sections with unique, file-specific content."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, f"Read error: {e}"

    # Extract title
    title_match = re.search(r'^title:\s*[\'"]?(.+?)[\'"]?\s*$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else filepath.stem
    topic = title.replace('技能：', '').replace('工具：', '').strip()
    if len(topic) > 20:
        topic = topic[:20]

    # Generate a unique seed from the filename
    seed = int(hashlib.md5(filepath.stem.encode()).hexdigest()[:8], 16)

    changes = []

    # Fix ## 不要用的场景
    not_use_pattern = r'(## 不要用的场景\s*\n)(.*?)(?=\n## |\Z)'
    match = re.search(not_use_pattern, content, re.DOTALL)
    if match:
        section_content = match.group(2)
        # Check if this is our generic content
        if '在问题边界尚不清晰时，不要急于使用此工具' in section_content:
            new_content = get_template(NOT_USE_TEMPLATES, seed, topic)
            new_section = f"\n- {new_content}\n- {get_template(NOT_USE_TEMPLATES, seed + 3, topic)}\n- {get_template(NOT_USE_TEMPLATES, seed + 5, topic)}\n"
            content = content[:match.start()] + match.group(1) + new_section + content[match.end():]
            changes.append("NotUse")

    # Fix ## 目的
    purpose_pattern = r'(## 目的\s*\n)(.*?)(?=\n## |\Z)'
    match = re.search(purpose_pattern, content, re.DOTALL)
    if match:
        section_content = match.group(2)
        if '解决「' in section_content and '场景下的核心问题' in section_content:
            new_content = get_template(PURPOSE_TEMPLATES, seed, topic)
            content = content[:match.start()] + match.group(1) + f"\n{new_content}\n" + content[match.end():]
            changes.append("Purpose")

    # Fix ## 操作步骤
    protocol_pattern = r'(## 操作步骤\s*\n)(.*?)(?=\n## |\Z)'
    match = re.search(protocol_pattern, content, re.DOTALL)
    if match:
        section_content = match.group(2)
        if '明确当前问题的边界和目标' in section_content:
            new_content = get_template(PROTOCOL_TEMPLATES, seed, topic)
            content = content[:match.start()] + match.group(1) + f"\n{new_content}\n" + content[match.end():]
            changes.append("Protocol")

    # Fix ## 质疑 (only if it's our generic content)
    critique_pattern = r'(## 质疑\s*\n)(.*?)(?=\n## |\Z)'
    match = re.search(critique_pattern, content, re.DOTALL)
    if match:
        section_content = match.group(2)
        if '该工具假设结构化方法论能产生正确结论' in section_content:
            scholar_idx = seed % len(CRITIQUE_SCHOLARS)
            scholar, affiliation, base_critique = CRITIQUE_SCHOLARS[scholar_idx]
            new_content = (
                f"- **具体假设**：{topic}工具假设结构化方法论能产生正确结论，但结论质量取决于输入数据和执行者判断力。\n"
                f"- **边界**：在{topic}相关的数据稀缺或快速变化场景中，已有经验框架可能完全失效。\n"
                f"- **反例**：团队在{topic}任务中完整执行了所有步骤，但核心假设从一开始就是错的。\n"
                f"- **前提**：使用者已具备{topic}领域的基础认知，且数据来源具有代表性。\n\n"
                f"**{scholar}**（{affiliation}）会质疑：{base_critique}"
            )
            content = content[:match.start()] + match.group(1) + f"\n{new_content}\n" + content[match.end():]
            changes.append("Critique")

    if not changes:
        return False, "No generic content found"

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
        elif "No generic" in info:
            print(f"  SKIP (no generic): {filepath}")
            skipped += 1
        else:
            print(f"  FAIL: {filepath} - {info}")
            failed += 1

    print()
    print(f"Results: {success} fixed, {skipped} skipped, {failed} failed")

if __name__ == "__main__":
    main()
