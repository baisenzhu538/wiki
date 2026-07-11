import os
import base64
import io
from pathlib import Path
from anthropic import Anthropic
from PIL import Image

INPUT_DIR = Path(r"C:\Users\Administrator\Desktop\wiki\00_inbox\Handle the business\Business formula")
OUTPUT_DIR = INPUT_DIR / "_vlm_output"
OUTPUT_DIR.mkdir(exist_ok=True)

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

# 高重要度关键词：这些图用更高分辨率处理
HIGH_PRIORITY_KEYWORDS = ["极其重要", "武器库", "冰山", "十大经典范式", "逻辑关系", "落地策略", "统一管理", "案例"]

PROMPT = """你是一位专业的 OCR + 商业内容理解专家。这份素材是「一堂业务公式」课程的核心内容，极其重要，必须精确识别。

请对这张图片进行以下处理：

1. **完整 OCR（精确优先）**：尽可能准确地识别图片中的所有文字，保持原文的段落和结构。特别注意：
   - 表格类图片必须还原成 Markdown 表格，单元格内换行用 <br>
   - 框架图/流程图/冰山图必须保留层级关系
   - 品牌名用"一堂"，不要写成"一莹/一望"
   - 英文用"Yitang"，不要写成"Yitanq"
   - 数学公式、业务公式、变量符号必须逐字准确（如：GMV=流量×转化率×客单价）
   - 专有名词、案例名、数据必须准确，不能编造
2. **内容理解**：说明这张图片的核心主题或核心观点（2-3 句话）。
3. **结构化输出**：用 Markdown 还原图片的完整结构（标题、层级、表格、公式）。
4. **关键概念提取**：列出图片中的 3-8 个关键概念、公式、术语或参数。
5. **一句话总结**：用一句话总结这张图片最有价值的信息。

【重要准确性要求】：
- 所有内容必须基于图片实际出现的信息，**严禁编造、推断、补充图片里没有的公式、数据或内容**。
- 如果图片里只有"GMV"这个词而没有完整公式，就不要自行补全成"GMV = 流量 × 转化率 × 客单价"。
- 结构化内容和关键概念只能整理图片里已有的信息，不能额外添加。

请用中文输出，格式如下：

## 原文识别
[OCR 原文，含表格/公式/层级]

## 核心主题
[2-3 句话]

## 结构化内容
[Markdown 结构]

## 关键概念
- 

## 一句话总结
[一句话]
"""


def encode_image(image_path: Path) -> tuple[str, str]:
    """Resize to control token cost; keep higher res for high-priority images."""
    name = image_path.name
    max_size = 2200 if any(k in name for k in HIGH_PRIORITY_KEYWORDS) else 1600
    with Image.open(image_path) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        w, h = img.size
        if max(w, h) > max_size:
            ratio = max_size / max(w, h)
            img = img.resize((int(w * ratio), int(h * ratio)), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=90)
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
