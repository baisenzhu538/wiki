#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
人机协作双三角素材识别与结构化
- 将 PDF 转换为图片
- 对所有图片进行 OCR + 基础结构化
- 输出：每文件独立 markdown + 汇总 JSON
"""
import os
import json
import base64
import fitz  # PyMuPDF
from pathlib import Path
from anthropic import Anthropic

INPUT_DIR = Path(r"C:\Users\Administrator\Desktop\wiki\00_inbox\人机协作双三角")
OUTPUT_DIR = INPUT_DIR / "_processed"
OUTPUT_DIR.mkdir(exist_ok=True)
PDF_IMG_DIR = OUTPUT_DIR / "_pdf_pages"
PDF_IMG_DIR.mkdir(exist_ok=True)

# 读取 API Key
env_path = Path(r"C:\Users\Administrator\Desktop\wiki\.env")
api_key = None
for line in env_path.read_text(encoding="utf-8").splitlines():
    if line.startswith("MINIMAX_API_KEY="):
        api_key = line.split("=", 1)[1].strip()
        break

if not api_key:
    raise RuntimeError("MINIMAX_API_KEY not found")

client = Anthropic(
    api_key=api_key,
    base_url="https://api.minimaxi.com/anthropic",
)


def encode_image(image_path: Path) -> str:
    return base64.b64encode(image_path.read_bytes()).decode("utf-8")


def pdf_to_images(pdf_path: Path) -> list[Path]:
    """将 PDF 每页转为 PNG，返回图片路径列表"""
    doc = fitz.open(str(pdf_path))
    image_paths = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        # 提高分辨率，确保文字清晰
        mat = fitz.Matrix(2.0, 2.0)
        pix = page.get_pixmap(matrix=mat)
        img_path = PDF_IMG_DIR / f"{pdf_path.stem}_page{page_num+1:03d}.png"
        pix.save(str(img_path))
        image_paths.append(img_path)
    doc.close()
    return image_paths


def analyze_image(image_path: Path, source_name: str) -> dict:
    """单图 OCR + 基础结构化"""
    print(f"  处理: {image_path.name}")
    b64 = encode_image(image_path)
    media_type = "image/png"

    system_prompt = """你是一位高精度文档识别与结构化助手。
任务：对图片中的文字内容进行 OCR 识别，并做基础结构化，便于后续专家标注。

请严格按以下格式输出，不要加入个人理解和引申：

【文档类型】
判断图片类型：封面/目录/正文/图表/流程图/案例页/清单表/画布/其他

【OCR原文】
完整提取图片中所有可见文字，尽可能保留原有版式、层级、表格结构。
如果是表格，请用 Markdown 表格输出。
如果是列表，请保留层级缩进。

【基础结构】
用 bullet points 列出：
- 标题
- 主要章节/段落
- 关键数字/案例名/人名
- 图表类型（如有）

【待标注提示】
只列出图片中可能值得后续人工标注的元素，不做判断。例如：
- 疑似双三角六要素对应关系
- 疑似案例主体
- 疑似关键结论
- 不清晰或可能OCR错误的文字

注意：不要解释概念，不要评价内容好坏，只忠实还原和结构化。"""

    message = client.messages.create(
        model="MiniMax-M3",
        max_tokens=3000,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "image", "source": {"type": "base64", "media_type": media_type, "data": b64}},
                    {"type": "text", "text": f"来源文件：{source_name}\n请对这张图进行 OCR + 基础结构化。"},
                ],
            }
        ],
    )
    text = "".join([block.text for block in message.content if block.type == "text"])
    return {"source": source_name, "analysis": text}


def main():
    all_results = {}
    processing_list = []  # (source_name, image_path)

    # 1. 收集原始 PNG
    for png_path in sorted(INPUT_DIR.glob("*.png")):
        processing_list.append((png_path.name, png_path))

    # 2. 收集 JPG（如果有）
    for jpg_path in sorted(INPUT_DIR.glob("*.jpg")):
        processing_list.append((jpg_path.name, jpg_path))

    # 3. 转换 PDF 并收集
    pdf_files = sorted(INPUT_DIR.glob("*.pdf"))
    print(f"发现 {len(pdf_files)} 个 PDF 文件，正在转换...")
    for pdf_path in pdf_files:
        print(f"转换 PDF: {pdf_path.name}")
        img_paths = pdf_to_images(pdf_path)
        for img_path in img_paths:
            processing_list.append((pdf_path.name, img_path))

    print(f"\n总共待处理 {len(processing_list)} 张图片\n")

    # 4. 批量处理
    for idx, (source_name, img_path) in enumerate(processing_list, 1):
        try:
            result = analyze_image(img_path, source_name)
            all_results[img_path.name] = result

            md_path = OUTPUT_DIR / f"{img_path.stem}_vlm.md"
            md_path.write_text(
                f"# {img_path.stem}\n\n**来源**: {source_name}\n\n{result['analysis']}\n",
                encoding="utf-8",
            )
            print(f"  [{idx}/{len(processing_list)}] 完成: {img_path.name}")
        except Exception as e:
            print(f"  [{idx}/{len(processing_list)}] 失败: {img_path.name} - {e}")
            all_results[img_path.name] = {"source": source_name, "error": str(e)}

    # 5. 保存汇总
    summary_path = OUTPUT_DIR / "vlm_summary.json"
    summary_path.write_text(json.dumps(all_results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n全部完成，结果保存在: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
