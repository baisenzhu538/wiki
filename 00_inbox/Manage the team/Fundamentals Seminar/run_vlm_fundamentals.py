import os
import base64
import io
from pathlib import Path
from anthropic import Anthropic
from PIL import Image

INPUT_DIR = Path(r"C:\Users\Administrator\Desktop\wiki\00_inbox\Manage the team\Fundamentals Seminar")
OUTPUT_DIR = INPUT_DIR / "_vlm_output"
OUTPUT_DIR.mkdir(exist_ok=True)

# Load API key from .env (UTF-8 encoding to avoid GBK errors)
env_path = Path(r"C:\Users\Administrator\Desktop\wiki\.env")
api_key = None
with open(env_path, encoding="utf-8") as f:
    for line in f:
        if line.startswith("MINIMAX_API_KEY="):
            api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
            break

if not api_key:
    raise ValueError("MINIMAX_API_KEY not found in .env")

client = Anthropic(api_key=api_key, base_url="https://api.minimaxi.com/anthropic")

PROMPT = """你是一位专业的 OCR + 内容理解专家。请对这张图片进行以下处理：

1. **完整 OCR**：尽可能准确地识别图片中的所有文字，保持原文的段落和结构。特别注意：
   - 表格类图片要还原成 Markdown 表格
   - 框架图/流程图要保留层级关系
   - 品牌名用"一堂"，不要写成"一莹"
   - 英文用"Yitang"，不要写成"Yitanq"
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

## 一句话总结
[一句话]
"""


def encode_image(image_path: Path, max_size: int = 1600) -> tuple[str, str]:
    """Resize large images to control token cost. Returns (base64, media_type)."""
    with Image.open(image_path) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        w, h = img.size
        if max(w, h) > max_size:
            ratio = max_size / max(w, h)
            img = img.resize((int(w * ratio), int(h * ratio)), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=88)
        return base64.b64encode(buf.getvalue()).decode("utf-8"), "image/jpeg"


def process_image(image_path: Path) -> str:
    b64, media_type = encode_image(image_path)
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
                            "data": b64,
                        },
                    },
                    {"type": "text", "text": PROMPT},
                ],
            }
        ],
    )
    return response.content[0].text


def main():
    image_exts = {".png", ".jpg", ".jpeg", ".jfif", ".webp", ".bmp", ".gif"}
    image_files = sorted([f for f in INPUT_DIR.iterdir() if f.suffix.lower() in image_exts])
    print(f"Found {len(image_files)} images")

    success = 0
    failed = []
    skipped = 0

    for idx, img_path in enumerate(image_files, 1):
        output_path = OUTPUT_DIR / f"{img_path.stem}_vlm.md"
        if output_path.exists():
            print(f"[{idx}/{len(image_files)}] SKIP (exists): {img_path.name}")
            skipped += 1
            continue

        print(f"[{idx}/{len(image_files)}] Processing: {img_path.name}")
        try:
            result = process_image(img_path)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(f"# VLM 识别结果：{img_path.name}\n\n")
                f.write(result)
            print(f"       -> Saved: {output_path.name}")
            success += 1
        except Exception as e:
            print(f"       [X] Error: {e}")
            failed.append((img_path.name, str(e)))

    print(f"\n=== Done ===")
    print(f"Total: {len(image_files)}, Success: {success}, Skipped: {skipped}, Failed: {len(failed)}")
    if failed:
        print("Failed files:")
        for name, err in failed:
            print(f"  - {name}: {err}")


if __name__ == "__main__":
    main()
