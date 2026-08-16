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
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
import json
import argparse
from pathlib import Path


def _fix_unescaped_quotes(text: str) -> str:
    """
    对 JSON 字符串值内部未转义的双引号进行转义。

    VLM 经常在中文描述里使用未转义的引号（如 description: "主题为"连续动作""），
    导致 json/json5 解析失败。本函数通过状态机遍历文本：进入字符串后，只有遇到
    后面跟着 JSON 结构字符（, : } ]）或文本结束的引号，才视为字符串结束；
    否则将该引号转义为内部引号。
    """
    result = []
    i = 0
    n = len(text)
    in_string = False
    while i < n:
        ch = text[i]
        if ch == '\\' and i + 1 < n:
            result.append(ch)
            result.append(text[i + 1])
            i += 2
            continue
        if ch == '"':
            if not in_string:
                in_string = True
                result.append(ch)
            else:
                # 判断此引号是否为字符串结束符：后面跟结构字符或已到结尾
                j = i + 1
                while j < n and text[j] in ' \t\n\r':
                    j += 1
                if j >= n or text[j] in ',:}]':
                    in_string = False
                    result.append(ch)
                else:
                    result.append('\\"')
            i += 1
        else:
            result.append(ch)
            i += 1
    return ''.join(result)


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

        # 2c：修复未转义内部引号后重试
        fixed = _fix_unescaped_quotes(candidate)
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

        # 2d：提取最外层平衡 JSON 对象（避开正则的贪婪/懒惰陷阱）
        chunk = _extract_balanced_json(candidate)
        if chunk:
            # 先对提取的 chunk 也做一次引号修复
            chunk_fixed = _fix_unescaped_quotes(chunk)
            for source in (chunk_fixed, chunk):
                try:
                    parsed = json.loads(source)
                    if isinstance(parsed, dict):
                        return parsed
                except Exception:
                    try:
                        import json5
                        parsed = json5.loads(source)
                        if isinstance(parsed, dict):
                            return parsed
                    except Exception:
                        pass

    # 终极兜底：字段级正则提取
    return _regex_field_extract(text)


def _regex_field_extract(text: str) -> dict | None:
    """不依赖 JSON 语法——逐字段正则匹配 VLM 固定结构的 8 个字段。"""
    KEYS = ["category", "title", "description", "key_elements",
            "visual_style", "tags", "usable_for", "confidence"]

    def _str(key):
        # 匹配 "key": "..."  — 值到下一个 key 或 } 为止
        m = re.search(
            rf'"{key}"\s*:\s*"((?:(?!",\s*(?:"(?:{"|".join(KEYS)}"|\}}))).)*)"',
            text, re.DOTALL
        )
        return m.group(1) if m else ""

    def _list(key):
        m = re.search(rf'"{key}"\s*:\s*\[(.*?)\]', text, re.DOTALL)
        if not m:
            return []
        return re.findall(r'"((?:(?!",).)*?)"', m.group(1))

    def _num(key):
        m = re.search(rf'"{key}"\s*:\s*([0-9.]+)', text)
        return float(m.group(1)) if m else 0.8

    cat = _str("category")
    if not cat or cat == "未识别":
        return None
    return {
        "category": cat,
        "title": _str("title"),
        "description": _str("description"),
        "key_elements": _list("key_elements"),
        "visual_style": _str("visual_style"),
        "tags": _list("tags"),
        "usable_for": _str("usable_for"),
        "confidence": _num("confidence"),
    }


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
        is_parse_error = (
            "_parse_error" in content
            or (re.search(r'- \*\*类型\*\*: 未识别', content)
                and re.search(r'- \*\*置信度\*\*: 0\.3', content))
        )
        if not is_parse_error:
            continue

        image_match = re.search(r"\*\*原图\*\*: `(.+?)`", content)
        image_path = image_match.group(1) if image_match else ""

        # 优先：从 "原始 JSON" 段提取内嵌 JSON（旧版 fallback 模式）
        inner = _extract_inner_from_raw_json(content)
        if inner:
            inner["_original_image_path"] = image_path
            inner["_model"] = "MiniMax-M3"
            inner = _normalize_parsed(inner)
            if not dry_run:
                _rewrite_desc_file(desc_path, inner)
            repaired += 1
            print(f"[FIXED:inner] {desc_path.name} -> {inner.get('category')} | {inner.get('title','')[:30]}")
            continue

        # 回退：全文解析
        parsed = _robust_json_parse(content)
        if parsed:
            parsed["_original_image_path"] = image_path
            parsed["_model"] = "MiniMax-M3"
            parsed = _normalize_parsed(parsed)
            if not dry_run:
                _rewrite_desc_file(desc_path, parsed)
            repaired += 1
            print(f"[FIXED] {desc_path.name} -> {parsed.get('category')} | {parsed.get('title','')[:30]}")
        else:
            still_failed += 1
            print(f"[FAILED] {desc_path.name}")

    return repaired, still_failed


def _extract_inner_from_raw_json(content: str) -> dict | None:
    """从 原始 JSON 段的 description 字段中提取内嵌 JSON。

    旧版 fallback 模式：外层 JSON 有 _parse_error=true，
    description 字段内含 markdown fence + 有效 JSON。
    """
    raw_match = re.search(
        r'## 原始 JSON\s*\n\s*```json\s*\n(.*?)\n```',
        content, re.DOTALL
    )
    if not raw_match:
        return None

    try:
        outer = json.loads(raw_match.group(1))
    except json.JSONDecodeError:
        # 外层的 JSON 本身可能损坏，尝试用 _robust_json_parse
        outer = _robust_json_parse(raw_match.group(1))
        if not outer:
            return None

    if not outer.get("_parse_error"):
        return None  # 不是 parse error 文件，不需要此路径

    desc = outer.get("description", "")
    if not desc:
        return None

    # 从 description 中提取内嵌 JSON
    return _robust_json_parse(desc)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="修复 VLM 描述文件中的 parse error")
    parser.add_argument("-i", "--input", required=True, help="包含 *_vlm_desc.md 的目录")
    parser.add_argument("--dry-run", action="store_true", help="只检测不写入")
    args = parser.parse_args()

    repaired, still_failed = repair_directory(args.input, dry_run=args.dry_run)
    print(f"\n总计：修复 {repaired} 个，仍失败 {still_failed} 个")
