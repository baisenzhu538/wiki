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

try:
    import json5
except ImportError:
    json5 = None


def extract_inner_json_from_description(desc_text: str) -> dict | None:
    """从 fallback 写入的 description 字段中提取内嵌 JSON。"""
    candidates = []

    # 情况 1: description 里有 ```json ... ``` fence
    for m in re.finditer(r'```(?:json)?\s*\n?(.*?)```', desc_text, re.DOTALL):
        candidates.append(m.group(1).strip())

    # 情况 2: description 本身就是 JSON
    if desc_text.strip().startswith('{'):
        candidates.append(desc_text.strip())

    for chunk in candidates:
        parsed = _robust_parse(chunk)
        if parsed:
            return parsed

    return None


def _robust_parse(text: str) -> dict | None:
    """多策略 JSON 解析，专门处理中文引号未转义的问题。"""
    # Pass 1: 清洗中文语境下的裸双引号
    cleaned = _clean_chinese_quotes(text)

    for candidate in [cleaned, text]:
        # json5
        if json5:
            try:
                parsed = json5.loads(candidate)
                if isinstance(parsed, dict) and "category" in parsed:
                    return parsed
            except Exception:
                pass

        # stdlib json
        try:
            parsed = json.loads(candidate)
            if isinstance(parsed, dict) and "category" in parsed:
                return parsed
        except json.JSONDecodeError:
            pass

    return None


def _clean_chinese_quotes(text: str) -> str:
    """将 JSON 字符串值内、中文语境下的裸双引号转义。

    模式: 中文字符后面的 " 后面跟着中文字符 → 转义
    例如: 标题为"保密条款" → 标题为\"保密条款\"
         称为"xxx" → 称为\"xxx\"
         主题为"连续动作" → 主题为\"连续动作\"
    """
    # 模式: 中文字符 + 紧接的 " + 后续是中文 → 把 " 转义成 \"
    # 同时匹配: 中文的 " 中文 → 中文 \" 中文
    result = re.sub(
        r'([一-鿿　-〿＀-￯])'
        r'"'
        r'(?=[一-鿿　-〿＀-￯])',
        r'\1\\"',
        text
    )
    # 匹配: 中文的："中文 → 中文：\"中文
    result = re.sub(
        r'([：:])'
        r'"'
        r'(?=[一-鿿])',
        r'\1\\"',
        result
    )
    # 匹配: 中文。"中文 → 中文。\"中文
    result = re.sub(
        r'([。，、；！？）\)】\]、])'
        r'"'
        r'(?=[一-鿿])',
        r'\1\\"',
        result
    )
    return result


def repair_file(desc_path: Path, dry_run: bool = False) -> bool:
    """修复单个 VLM 描述文件。"""
    content = desc_path.read_text(encoding="utf-8")

    if '"_parse_error"' not in content.replace("true", "True"):
        return False

    # 提取 "原始 JSON" 段
    raw_match = re.search(
        r'## 原始 JSON\s*\n\s*```json\s*\n(.*?)\n```',
        content, re.DOTALL
    )
    if not raw_match:
        return False

    try:
        saved = json.loads(raw_match.group(1))
    except json.JSONDecodeError:
        return False

    if not saved.get("_parse_error"):
        return False

    desc_text = saved.get("description", "")
    if not desc_text:
        return False

    inner = extract_inner_json_from_description(desc_text)
    if not inner:
        return False

    if dry_run:
        print(f"  [DRY-RUN] {desc_path.name}  ->  {inner.get('title', '无标题')[:60]}")
        return True

    # 重建文件
    image_stem = desc_path.stem.replace("_vlm_desc", "")

    lines = []
    lines.append(f"# VLM 描述：{image_stem}\n")
    lines.append(f"**原图**: `{desc_path.parent / f'{image_stem}.png'}`\n")
    lines.append(f"**模型**: `MiniMax-M3`\n")
    lines.append("## 结构化描述\n")
    lines.append(f"- **类型**: {inner.get('category', '')}\n")
    lines.append(f"- **标题**: {inner.get('title', '')}\n")
    lines.append(f"- **置信度**: {inner.get('confidence', '')}\n")
    lines.append(f"- **视觉风格**: {inner.get('visual_style', '')}\n")
    lines.append(f"### 描述\n\n{inner.get('description', '')}\n")

    lines.append("### 关键元素\n\n")
    for elem in (inner.get("key_elements") or []):
        lines.append(f"- {elem}\n")

    lines.append("\n### 标签\n\n")
    for tag in (inner.get("tags") or []):
        lines.append(f"- {tag}\n")

    lines.append(f"\n### 适用场景\n\n{inner.get('usable_for', '')}\n")

    lines.append("## 原始 JSON\n\n")
    lines.append("```json\n")
    lines.append(json.dumps(inner, ensure_ascii=False, indent=2))
    lines.append("\n```\n")

    desc_path.write_text("".join(lines), encoding="utf-8")
    print(f"  OK: {desc_path.name}")
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
        text = df.read_text(encoding="utf-8")
        if '"_parse_error"' in text.replace("true", "True"):
            parse_errors.append(df)

    print(f"其中 {len(parse_errors)} 个含 parse error\n")

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
    print(f"\n{mode}修复成功: {repaired}  无法修复: {len(unfixable)}")
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
