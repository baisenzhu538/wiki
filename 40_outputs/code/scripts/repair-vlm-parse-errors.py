#!/usr/bin/env python3
"""
修复已有的 VLM 描述文件中的 parse error。

问题：MiniMax-M3 返回的 JSON 内部字符串值中常包含未转义的双引号
（如 description 字段里的中文引号），导致外层 json.loads 失败，
原脚本把 raw markdown 当作 description，confidence 降为 0.3。

本脚本不重新调用 API，而是直接修复已有 .md 文件中的内嵌 JSON。

使用方式：
    python repair-vlm-parse-errors.py -i "00_inbox/战略专题/冉鹏PPT截图"
"""
import re
import json
import argparse
from pathlib import Path


def _escape_inner_quotes_in_json_string(text: str) -> str:
    """
    对 JSON 字符串值内部未转义的双引号进行转义。
    只处理出现在中文字符或中文标点附近的内部引号，避免破坏 JSON 结构。
    """
    # 中文字符范围
    CJK = r"\u4e00-\u9fa5"
    # 中文标点
    CJK_PUNCT = r"\uff0c\u3002\u3001\uff1b\uff1a\uff01\uff1f\uff08\uff09\u3010\u3011\u300c\u300d\u300e\u300f\u201c\u201d\u2018\u2019"

    # 情况1：中文字符/中文标点 -> " -> 中文字符/中文标点（内部引号）
    text = re.sub(
        rf'(?<=[{CJK}{CJK_PUNCT}])"(?=[{CJK}{CJK_PUNCT}])',
        r'\\"',
        text,
    )
    # 情况2：中文冒号/西文冒号/逗号 -> " -> 中文字符（如 称为"xxx"）
    text = re.sub(
        rf'(?<=[{CJK}{CJK_PUNCT}:,"])"(?=[{CJK}])',
        r'\\"',
        text,
    )
    # 情况3：中文字符 -> " -> 中文冒号/中文标点（如 xxx"，）
    text = re.sub(
        rf'(?<=[{CJK}])"(?=[{CJK_PUNCT}])',
        r'\\"',
        text,
    )
    return text


def _robust_json_parse(text: str) -> dict | None:
    """多策略 JSON 解析，返回 dict 或 None。"""
    # 策略1：提取 markdown code fence
    fences = list(re.finditer(r"```(?:json)?\s*\n?(.*?)```", text, re.DOTALL))
    candidates = [m.group(1).strip() for m in fences]
    # 策略2：直接解析原始文本
    candidates.append(text.strip())

    for candidate in candidates:
        # 2a：json5（更宽容）
        try:
            import json5
            parsed = json5.loads(candidate)
            if isinstance(parsed, dict) and "category" in parsed:
                return parsed
        except Exception:
            pass

        # 2b：标准 json
        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            pass

        # 2c：修复中文内部引号后重试
        fixed = _escape_inner_quotes_in_json_string(candidate)
        if fixed != candidate:
            try:
                return json.loads(fixed)
            except json.JSONDecodeError:
                try:
                    import json5
                    parsed = json5.loads(fixed)
                    if isinstance(parsed, dict) and "category" in parsed:
                        return parsed
                except Exception:
                    pass

        # 2d：提取最外层平衡 JSON 对象
        # 使用计数器找到第一个匹配的 {}，而不是贪婪/懒惰正则
        chunk = _extract_balanced_json(candidate)
        if chunk:
            for parser in (json.loads, lambda x: json5.loads(x) if "json5" in globals() or __import__("json5").loads(x) else None):
                try:
                    parsed = json.loads(chunk)
                    if isinstance(parsed, dict):
                        return parsed
                except Exception:
                    try:
                        import json5
                        parsed = json5.loads(chunk)
                        if isinstance(parsed, dict):
                            return parsed
                    except Exception:
                        pass

    return None


def _extract_balanced_json(text: str) -> str | None:
    """用括号计数法提取第一个平衡的 JSON 对象。"""
    start = text.find("{")
    if start == -1:
        return None
    count = 0
    in_string = False
    escape = False
    for i, ch in enumerate(text[start:], start=start):
        if escape:
            escape = False
            continue
        if ch == "\\" and in_string:
            escape = True
            continue
        if ch == '"' and (i == start or text[i - 1] != "\\"):
            in_string = not in_string
            continue
        if not in_string:
            if ch == "{":
                count += 1
            elif ch == "}":
                count -= 1
                if count == 0:
                    return text[start : i + 1]
    return None


def _normalize_parsed(parsed: dict) -> dict:
    """确保所有期望的键都存在，置信度在合理范围。"""
    for key in ("key_elements", "tags"):
        if key not in parsed:
            parsed[key] = []
    for key in ("category", "title", "description", "visual_style", "usable_for"):
        if key not in parsed:
            parsed[key] = ""
    conf = parsed.get("confidence", 0.0)
    if not isinstance(conf, (int, float)) or conf <= 0 or conf > 1:
        parsed["confidence"] = max(0.0, min(1.0, float(conf) if conf else 0.5))
    return parsed


def _rewrite_desc_file(desc_path: Path, parsed: dict) -> None:
    """用解析后的结构化内容重写 .md 文件。"""
    image_path = parsed.get("_original_image_path", "")
    model = parsed.get("_model", "MiniMax-M3")

    with open(desc_path, "w", encoding="utf-8") as f:
        f.write(f"# VLM 描述：{desc_path.stem.replace('_vlm_desc', '')}\n\n")
        f.write(f"**原图**: `{image_path}`\n\n")
        f.write(f"**模型**: `{model}`\n\n")
        f.write("## 结构化描述\n\n")
        f.write(f"- **类型**: {parsed.get('category', '')}\n")
        f.write(f"- **标题**: {parsed.get('title', '')}\n")
        f.write(f"- **置信度**: {parsed.get('confidence', '')}\n")
        f.write(f"- **视觉风格**: {parsed.get('visual_style', '')}\n\n")
        f.write(f"### 描述\n\n{parsed.get('description', '')}\n\n")

        f.write("### 关键元素\n\n")
        for elem in parsed.get("key_elements", []):
            f.write(f"- {elem}\n")

        f.write("\n### 标签\n\n")
        for tag in parsed.get("tags", []):
            f.write(f"- {tag}\n")

        f.write(f"\n### 适用场景\n\n{parsed.get('usable_for', '')}\n\n")

        f.write("## 原始 JSON\n\n")
        f.write("```json\n")
        # 写回时确保是合法 JSON
        clean = {k: v for k, v in parsed.items() if not k.startswith("_")}
        f.write(json.dumps(clean, ensure_ascii=False, indent=2))
        f.write("\n```\n")


def repair_directory(input_dir: str, dry_run: bool = False) -> tuple[int, int]:
    """修复目录下所有 parse error 的 VLM 描述文件。"""
    input_path = Path(input_dir)
    files = sorted(input_path.glob("*_vlm_desc.md"))

    repaired = 0
    still_failed = 0

    for desc_path in files:
        content = desc_path.read_text(encoding="utf-8")
        # 检测 parse error：外层 confidence 0.3 且包含 _parse_error 或 title 为空且类型为未识别
        is_parse_error = (
            "_parse_error" in content
            or re.search(r'- \*\*类型\*\*: 未识别', content)
            and re.search(r'- \*\*置信度\*\*: 0\.3', content)
        )
        if not is_parse_error:
            continue

        # 尝试提取原图路径
        image_match = re.search(r"\*\*原图\*\*: `(.+?)`", content)
        image_path = image_match.group(1) if image_match else ""

        # 尝试修复
        parsed = _robust_json_parse(content)
        if parsed:
            parsed["_original_image_path"] = image_path
            parsed["_model"] = "MiniMax-M3"
            parsed = _normalize_parsed(parsed)
            if not dry_run:
                _rewrite_desc_file(desc_path, parsed)
            repaired += 1
            print(f"[FIXED] {desc_path.name} -> {parsed.get('category')} | {parsed.get('title')[:30]}")
        else:
            still_failed += 1
            print(f"[FAILED] {desc_path.name}")

    return repaired, still_failed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="修复 VLM 描述文件中的 parse error")
    parser.add_argument("-i", "--input", required=True, help="包含 *_vlm_desc.md 的目录")
    parser.add_argument("--dry-run", action="store_true", help="只检测不写入")
    args = parser.parse_args()

    repaired, still_failed = repair_directory(args.input, dry_run=args.dry_run)
    print(f"\n总计：修复 {repaired} 个，仍失败 {still_failed} 个")
