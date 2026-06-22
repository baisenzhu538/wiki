#!/usr/bin/env python3
"""
修复 VLM 描述文件中的 parse error —— 从外层 description 字段提取内嵌 JSON 并重建文件。

使用方式:
    python repair-vlm-parse-errors.py --dir "00_inbox/战略专题/冉鹏PPT截图"
    python repair-vlm-parse-errors.py --dir "00_inbox/战略专题/冉鹏PPT截图" --dry-run
"""

import json
import re
import sys
from pathlib import Path

# 尝试加载 json5（更宽容的 JSON 解析器）
try:
    import json5
except ImportError:
    json5 = None


def extract_inner_json_from_description(desc_text: str) -> dict | None:
    """从 fallback 写入的 description 字段中提取内嵌 JSON。

    fallback 将 VLM 原始返回（含 markdown fence + JSON）写入了 description。
    这里反向提取。
    """
    # 情况 1: description 以 ```json 开头 → 整个就是被 fence 包裹的 JSON
    fence_inner = re.search(r'```(?:json)?\s*\n?(.*?)```', desc_text, re.DOTALL)
    if fence_inner:
        chunk = fence_inner.group(1).strip()
        parsed = _try_parse(chunk)
        if parsed:
            return parsed

    # 情况 2: description 本身就是 JSON 字符串（无 fence）
    if desc_text.strip().startswith('{'):
        parsed = _try_parse(desc_text)
        if parsed:
            return parsed

    # 情况 3: 从任意位置提取 JSON 对象
    for pattern in [r'\{[\s\S]*\}', r'\{[\s\S]*?\}']:
        for match in re.finditer(pattern, desc_text):
            parsed = _try_parse(match.group(0))
            if parsed:
                return parsed

    return None


def _try_parse(text: str) -> dict | None:
    """尝试解析 JSON，含中文引号修复 + json5 兜底。"""
    # 预处理：修复 JSON 字符串值内部的中文裸引号
    fixed = _escape_chinese_context_quotes(text)

    if json5:
        try:
            parsed = json5.loads(fixed)
            if isinstance(parsed, dict) and "category" in parsed:
                return parsed
        except Exception:
            pass
        # 原文本也试一次
        try:
            parsed = json5.loads(text)
            if isinstance(parsed, dict) and "category" in parsed:
                return parsed
        except Exception:
            pass

    for candidate in [fixed, text]:
        try:
            parsed = json.loads(candidate)
            if isinstance(parsed, dict) and "category" in parsed:
                return parsed
        except json.JSONDecodeError:
            pass

    return None


def _escape_chinese_context_quotes(text: str) -> str:
    """修复 JSON 字符串值内中文语境下的裸双引号。

    模式: 中文文字 " 中文文字  →  中文文字 \" 中文文字
    如: 标题为"保密条款" → 标题为\"保密条款\"
        称为"xxx" → 称为\"xxx\"
    """
    import re
    result = []
    i = 0
    in_string = False
    string_char = None
    escape_next = False

    while i < len(text):
        ch = text[i]
        if escape_next:
            result.append(ch)
            escape_next = False
            i += 1
            continue
        if ch == '\\' and in_string:
            result.append(ch)
            escape_next = True
            i += 1
            continue
        if ch == '"' and not in_string:
            in_string = True
            string_char = '"'
            result.append(ch)
            i += 1
            continue
        if ch == '"' and in_string:
            # 消耗后续空白看是不是真正的 JSON 键/分隔符
            after = i + 1
            while after < len(text) and text[after] in ' \t\n\r':
                after += 1
            if after < len(text) and text[after] in ':,':
                # 真正的 JSON 语法：字符串结束，后跟 : 或 ,
                in_string = False
                result.append(ch)
            elif after < len(text) and text[after] == '"':
                # 连续两个引号 → 下一个字符串开始（JSON 键值对之间）
                in_string = False
                result.append(ch)
            elif i > 0 and _has_chinese_context(text, i):
                # 中文语境下的裸引号 → 转义
                result.append('\\"')
            else:
                in_string = False
                result.append(ch)
            i += 1
            continue
        result.append(ch)
        i += 1

    return ''.join(result)


def _has_chinese_context(text: str, pos: int) -> bool:
    """检查位置 pos 的引号是否夹在中文语境中。"""
    # 向前找最近的中文字符
    for j in range(pos - 1, max(pos - 30, -1), -1):
        if '一' <= text[j] <= '鿿' or text[j] in '，。、；：！？）】》':
            # 有中文在前 → 中文语境
            return True
        if text[j] in '"\n{}[]':
            break
    # 向后找最近的中文字符
    for j in range(pos + 1, min(pos + 30, len(text))):
        if '一' <= text[j] <= '鿿' or text[j] in '，。、；：！？（【《':
            return True
        if text[j] in '"\n{}[]':
            break
    return False


def repair_file(desc_path: Path, dry_run: bool = False) -> bool:
    """修复单个 VLM 描述文件。返回是否成功。"""
    with open(desc_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 确认是 parse error 文件
    if '"_parse_error": true' not in content and '"_parse_error": True' not in content:
        return False

    # 从 "原始 JSON" 段提取当前保存的 JSON
    raw_json_match = re.search(
        r'## 原始 JSON\s*\n\s*```json\s*\n(.*?)\n```',
        content, re.DOTALL
    )
    if not raw_json_match:
        return False

    saved_json_text = raw_json_match.group(1)
    try:
        saved = json.loads(saved_json_text)
    except json.JSONDecodeError:
        return False

    if not saved.get("_parse_error"):
        return False

    # 从 description 字段提取内嵌 JSON
    desc_text = saved.get("description", "")
    if not desc_text:
        return False

    inner = extract_inner_json_from_description(desc_text)
    if not inner:
        return False

    if dry_run:
        print(f"  [DRY-RUN] 可修复: {desc_path.name}  ->  {inner.get('title', '无标题')[:60]}")
        return True

    # 重建 VLM 描述文件
    image_stem = desc_path.stem.replace("_vlm_desc", "")
    image_path = desc_path.parent / f"{image_stem}.png"

    with open(desc_path, "w", encoding="utf-8") as f:
        f.write(f"# VLM 描述：{image_stem}\n\n")
        f.write(f"**原图**: `{image_path}`\n\n")
        f.write(f"**模型**: `MiniMax-M3`\n\n")
        f.write("## 结构化描述\n\n")
        f.write(f"- **类型**: {inner.get('category', '')}\n")
        f.write(f"- **标题**: {inner.get('title', '')}\n")
        f.write(f"- **置信度**: {inner.get('confidence', '')}\n")
        f.write(f"- **视觉风格**: {inner.get('visual_style', '')}\n\n")
        f.write(f"### 描述\n\n{inner.get('description', '')}\n\n")

        f.write("### 关键元素\n\n")
        for elem in inner.get("key_elements", []) or []:
            f.write(f"- {elem}\n")

        f.write("\n### 标签\n\n")
        for tag in inner.get("tags", []) or []:
            f.write(f"- {tag}\n")

        f.write(f"\n### 适用场景\n\n{inner.get('usable_for', '')}\n\n")

        f.write("## 原始 JSON\n\n")
        f.write("```json\n")
        f.write(json.dumps(inner, ensure_ascii=False, indent=2))
        f.write("\n```\n")

    print(f"  修复成功: {desc_path.name}")
    return True


def main(target_dir: str, dry_run: bool = False):
    target = Path(target_dir)
    if not target.is_dir():
        print(f"错误：目录不存在 {target_dir}", file=sys.stderr)
        sys.exit(1)

    desc_files = sorted(target.glob("*_vlm_desc.md"))
    print(f"扫描到 {len(desc_files)} 个 VLM 描述文件")

    parse_errors = []
    for df in desc_files:
        with open(df, "r", encoding="utf-8") as f:
            if '"_parse_error": true' in f.read() or '"_parse_error": True' in f.read():
                parse_errors.append(df)

    print(f"其中 {len(parse_errors)} 个含 parse error")

    repaired = 0
    unfixable = []

    for df in parse_errors:
        try:
            ok = repair_file(df, dry_run=dry_run)
            if ok:
                repaired += 1
            else:
                unfixable.append(df.name)
        except Exception as e:
            print(f"  [X] {df.name}: {e}")
            unfixable.append(df.name)

    mode = "[DRY-RUN] " if dry_run else ""
    print(f"\n{mode}修复: {repaired}  无法修复: {len(unfixable)}")
    if unfixable:
        for name in unfixable:
            print(f"  - {name}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="修复 VLM parse error 文件")
    parser.add_argument("--dir", required=True, help="VLM 描述文件所在目录")
    parser.add_argument("--dry-run", action="store_true", help="仅预览，不实际修改")
    args = parser.parse_args()
    main(args.dir, args.dry_run)
