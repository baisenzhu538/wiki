import os
import base64
import json
from pathlib import Path
from anthropic import Anthropic

INPUT_DIR = Path(r"C:\Users\Administrator\Desktop\wiki\00_inbox\人机协作双三角\codex")
OUTPUT_DIR = INPUT_DIR / "_vlm_output"
OUTPUT_DIR.mkdir(exist_ok=True)

# Load API key from .env
env_path = Path(r"C:\Users\Administrator\Desktop\wiki\.env")
api_key = None
if env_path.exists():
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("MINIMAX_API_KEY="):
                api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
                break

if not api_key:
    raise ValueError("MINIMAX_API_KEY not found in .env")

client = Anthropic(api_key=api_key, base_url="https://api.minimaxi.com/anthropic")

PROMPT = """你是一位专业的 OCR + 内容理解专家。请对这张图片进行以下处理：

1. **完整 OCR**：尽可能准确地识别图片中的所有文字，保持原文的段落和结构。
2. **内容理解**：简要说明这张图片的核心主题或核心观点（2-3 句话）。
3. **结构化输出**：如果图片是思维导图、框架图、流程图、表格或课程笔记，请用 Markdown 还原其结构。
4. **关键概念提取**：列出图片中出现的 3-7 个关键概念或术语。
5. **一句话总结**：用一句话总结这张图片最有价值的信息。

请用中文输出，格式如下：

## 原文识别
[OCR 原文]

## 核心主题
[2-3 句话]

## 结构化内容
[Markdown 结构]

## 关键概念
- 
- 

## 一句话总结
[一句话]
"""


def encode_image(image_path: Path) -> str:
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def process_image(image_path: Path) -> str:
    print(f"Processing: {image_path.name}")
    base64_image = encode_image(image_path)

    media_type = "image/jpeg"
    if image_path.suffix.lower() in [".png"]:
        media_type = "image/png"

    response = client.messages.create(
        model="MiniMax-M3",
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": base64_image,
                        },
                    },
                    {"type": "text", "text": PROMPT},
                ],
            }
        ],
    )

    return response.content[0].text


def main():
    image_files = sorted([f for f in INPUT_DIR.iterdir() if f.suffix.lower() in [".jfif", ".jpg", ".jpeg", ".png"]])
    print(f"Found {len(image_files)} images")

    for img_path in image_files:
        try:
            result = process_image(img_path)
            output_path = OUTPUT_DIR / f"{img_path.stem}_vlm.md"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(f"# VLM 识别结果：{img_path.name}\n\n")
                f.write(result)
            print(f"Saved: {output_path.name}")
        except Exception as e:
            print(f"Error processing {img_path.name}: {e}")


if __name__ == "__main__":
    main()
