#!/usr/bin/env python3
"""
用 MiniMax 多模态模型（MiniMax-VL-01 / M2.7）批量给图片生成结构化描述。

使用方式：
    export MINIMAX_API_KEY=your_key
    python describe-images-minimax.py -i "00_inbox/科学决策" -o "00_inbox/科学决策"
"""
import os
import json
import base64
import argparse
from pathlib import Path
import requests
from PIL import Image

API_BASE = "https://api.minimax.chat/v1"
MODEL = "MiniMax-M3"  # M3 原生支持图文理解

SYSTEM_PROMPT = """你是一位专业的视觉内容分析师。请仔细观察图片，并输出一段结构化描述。

要求：
1. 判断图片类型：教学示意图 / 框架图 / 流程图 / 信息图 / 海报 / 幻灯片 / 其他
2. 提取图片标题（如果有）
3. 描述图片的核心内容和视觉结构
4. 列出关键元素、文字、图表、人物等
5. 分析视觉风格（极简/商务/手绘/国潮/科技/教育等）
6. 给出 5-10 个关键词标签
7. 说明这张图片适合用于什么场景
8. 用 0-1 之间的数字给出你对描述的置信度

请严格按以下 JSON 格式输出，不要包含任何额外解释：

{
  "category": "",
  "title": "",
  "description": "",
  "key_elements": [],
  "visual_style": "",
  "tags": [],
  "usable_for": "",
  "confidence": 0.9
}
"""


def get_api_key():
    key = os.environ.get("MINIMAX_API_KEY")
    if not key:
        raise EnvironmentError("请设置环境变量 MINIMAX_API_KEY")
    return key.strip()


def resize_image(image_path: Path, max_size: int = 1024, quality: int = 85) -> bytes:
    """缩放图片并转为 JPEG bytes，控制 token 成本。"""
    img = Image.open(image_path)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    w, h = img.size
    if max(w, h) > max_size:
        ratio = max_size / max(w, h)
        new_size = (int(w * ratio), int(h * ratio))
        img = img.resize(new_size, Image.Resampling.LANCZOS)

    import io
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=quality)
    return buf.getvalue()


def image_to_base64(image_bytes: bytes) -> str:
    return base64.b64encode(image_bytes).decode("utf-8")


def describe_image(api_key: str, image_path: Path) -> dict:
    image_bytes = resize_image(image_path)
    b64_image = image_to_base64(image_bytes)

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{b64_image}",
                        },
                    },
                    {
                        "type": "text",
                        "text": "请分析这张图片，输出 JSON 格式的结构化描述。",
                    },
                ],
            },
        ],
        "max_tokens": 2000,
        "temperature": 0.3,
    }

    resp = requests.post(
        f"{API_BASE}/chat/completions",
        headers=headers,
        json=payload,
        timeout=120,
    )
    resp.raise_for_status()
    data = resp.json()
    content = data["choices"][0]["message"]["content"]

    import re
    think_match = re.search(r"<think>(.*?)</think>", content, flags=re.DOTALL)
    non_think = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()

    candidates = []
    if non_think:
        candidates.append(non_think)
    if think_match:
        candidates.append(think_match.group(1).strip())
    candidates.append(content.strip())

    for raw in candidates:
        result = _robust_json_parse(raw)
        if result:
            return result

    fallback_text = non_think if non_think else (think_match.group(1).strip() if think_match else content)
    return {
        "category": "未识别",
        "title": "",
        "description": fallback_text[:2000],
        "key_elements": [],
        "visual_style": "",
        "tags": [],
        "usable_for": "",
        "confidence": 0.3,
        "_parse_error": True,
    }


def _robust_json_parse(text: str) -> dict | None:
    """Multi-strategy JSON extraction from VLM output. Returns parsed dict or None."""
    import re

    # Strategy 1: Extract from markdown code fence (non-greedy, outermost match)
    fences = list(re.finditer(r"```(?:json)?\s*\n?(.*?)```", text, re.DOTALL))
    candidates = []
    for m in fences:
        candidates.append(m.group(1).strip())
    # Also try the raw text
    candidates.append(text.strip())

    for candidate in candidates:
        # Strategy 2a: json5 — handles unescaped quotes, trailing commas, unquoted keys
        try:
            import json5
            parsed = json5.loads(candidate)
            if isinstance(parsed, dict) and "category" in parsed:
                return _normalize_parsed(parsed)
        except Exception:
            pass

        # Strategy 2b: stdlib json with quote-fixing pre-pass
        try:
            return _normalize_parsed(json.loads(candidate))
        except json.JSONDecodeError:
            fixed = _fix_unescaped_chinese_quotes(candidate)
            if fixed != candidate:
                try:
                    return _normalize_parsed(json.loads(fixed))
                except json.JSONDecodeError:
                    pass

        # Strategy 2c: find first balanced JSON object
        match = re.search(r"\{[\s\S]*\}", candidate)
        if match:
            chunk = match.group(0)
            try:
                return _normalize_parsed(json.loads(chunk))
            except json.JSONDecodeError:
                try:
                    import json5
                    return _normalize_parsed(json5.loads(chunk))
                except Exception:
                    pass

        # Strategy 2d: find first balanced object with json5
        match = re.search(r"\{[\s\S]*?\}", candidate)
        if match:
            try:
                import json5
                return _normalize_parsed(json5.loads(match.group(0)))
            except Exception:
                pass

    return None


def _fix_unescaped_chinese_quotes(text: str) -> str:
    """Fix unescaped Chinese-context double quotes inside JSON string values.

    Pattern: inside a JSON string value (between unescaped " delimiters),
    Chinese text often contains raw double quotes like 标题为"xxx"
    These need to be escaped to avoid breaking the JSON parser.
    """
    import re

    def escape_inner_quotes(match):
        """Escape inner double quotes within a matched JSON string value pair."""
        prefix = match.group(1) + '"'  # key + colon + opening quote
        value = match.group(2)[1:-1]   # value without outer quotes
        # Find patterns like Chinese_char"Chinese_char and escape the inner quote
        # Also handle cases like 称为"xxx" where quotes surround Chinese text
        fixed_value = re.sub(
            r'(?<=[一-鿿])"(?=[一-鿿，。、；：！？）\)】\]"\'、])',
            r'\"',
            value
        )
        # Also fix quotes after certain Chinese punctuation
        fixed_value = re.sub(
            r'(?<=[：:])"(?=[一-鿿])',
            r'\"',
            fixed_value
        )
        return f'{prefix}{fixed_value}"'

    # Match "key": "value with potentially bad quotes"
    # This handles the common case where description/etc contain unescaped quotes
    result = re.sub(
        r'("(?:description|title|usable_for|visual_style)"\s*:\s*)"((?:[^"\\]|\\.)*?)"',
        escape_inner_quotes,
        text,
        flags=re.DOTALL
    )
    return result


def _normalize_parsed(parsed: dict) -> dict:
    """Ensure all expected keys exist and confidence is in range."""
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


def save_description(output_path: Path, image_path: Path, result: dict):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# VLM 描述：{image_path.stem}\n\n")
        f.write(f"**原图**: `{image_path}`\n\n")
        f.write(f"**模型**: `{MODEL}`\n\n")
        f.write("## 结构化描述\n\n")
        f.write(f"- **类型**: {result.get('category', '')}\n")
        f.write(f"- **标题**: {result.get('title', '')}\n")
        f.write(f"- **置信度**: {result.get('confidence', '')}\n")
        f.write(f"- **视觉风格**: {result.get('visual_style', '')}\n\n")
        f.write(f"### 描述\n\n{result.get('description', '')}\n\n")

        f.write("### 关键元素\n\n")
        for elem in result.get("key_elements", []):
            f.write(f"- {elem}\n")

        f.write("\n### 标签\n\n")
        for tag in result.get("tags", []):
            f.write(f"- {tag}\n")

        f.write(f"\n### 适用场景\n\n{result.get('usable_for', '')}\n\n")

        f.write("## 原始 JSON\n\n")
        f.write("```json\n")
        f.write(json.dumps(result, ensure_ascii=False, indent=2))
        f.write("\n```\n")


def main(input_dir: str, output_dir: str, limit: int = 0):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    api_key = get_api_key()

    image_exts = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif"}
    images = sorted([p for p in input_path.iterdir() if p.suffix.lower() in image_exts])

    if limit > 0:
        images = images[:limit]

    print(f"找到 {len(images)} 张图片，开始生成 VLM 描述...")

    summary = []
    failed = []

    for idx, img_path in enumerate(images, 1):
        out_path = output_path / f"{img_path.stem}_vlm_desc.md"

        print(f"[{idx}/{len(images)}] {img_path.name}")
        try:
            result = describe_image(api_key, img_path)
            save_description(out_path, img_path, result)
            print(f"       -> {out_path.name}")
            summary.append({
                "image": img_path.name,
                "title": result.get("title", ""),
                "category": result.get("category", ""),
                "confidence": result.get("confidence", ""),
                "desc_file": str(out_path),
            })
        except Exception as e:
            print(f"       [X] 失败：{e}")
            failed.append((img_path.name, str(e)))

    # 保存汇总
    summary_path = output_path / "README-VLM描述汇总.md"
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(f"# {input_path.name} - VLM 描述汇总\n\n")
        f.write(f"模型: `{MODEL}`\n\n")
        f.write(f"图片数: {len(images)}\n")
        f.write(f"成功: {len(summary)}\n")
        f.write(f"失败: {len(failed)}\n\n")

        f.write("## 描述清单\n\n")
        f.write("| 图片 | 类型 | 标题 | 置信度 | 描述文件 |\n")
        f.write("|---|---|---|---|---|\n")
        for item in summary:
            f.write(f"| {item['image']} | {item['category']} | {item['title']} | {item['confidence']} | `{item['desc_file']}` |\n")

        if failed:
            f.write("\n## 失败列表\n\n")
            for name, err in failed:
                f.write(f"- {name}: {err}\n")

    print(f"\n汇总文件: {summary_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="用 MiniMax 视觉模型批量描述图片")
    parser.add_argument("-i", "--input", required=True, help="输入图片目录")
    parser.add_argument("-o", "--output", required=True, help="输出目录")
    parser.add_argument("-n", "--limit", type=int, default=0, help="限制处理数量（0=全部）")
    args = parser.parse_args()
    main(args.input, args.output, args.limit)
