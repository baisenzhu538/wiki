#!/usr/bin/env python3
"""
用 PaddleOCR 批量识别图片中的文字，输出为 markdown。
适用于 00_inbox/AI短剧创作 等图片素材的 OCR 处理。
"""
import os
import json
import argparse
from pathlib import Path
from paddleocr import PaddleOCR


def ocr_image(ocr_engine, image_path: Path) -> list:
    """对单张图片进行 OCR，返回按 y 坐标排序的文本块列表。"""
    result = ocr_engine.ocr(str(image_path), cls=True)
    if not result or result[0] is None:
        return []

    blocks = []
    for line in result[0]:
        bbox, (text, score) = line
        # bbox: [[x1,y1],[x2,y1],[x2,y2],[x1,y2]]
        y = sum(p[1] for p in bbox) / 4
        x = sum(p[0] for p in bbox) / 4
        blocks.append({
            "text": text,
            "score": round(score, 3),
            "x": round(x, 1),
            "y": round(y, 1),
        })

    # 按从上到下、从左到右排序
    blocks.sort(key=lambda b: (b["y"] // 30, b["x"]))
    return blocks


def blocks_to_lines(blocks: list, y_threshold: float = 25.0) -> list:
    """把文本块按行合并。"""
    if not blocks:
        return []

    lines = []
    current_line = [blocks[0]]
    current_y = blocks[0]["y"]

    for block in blocks[1:]:
        if abs(block["y"] - current_y) <= y_threshold:
            current_line.append(block)
        else:
            lines.append(" ".join(b["text"] for b in sorted(current_line, key=lambda x: x["x"])))
            current_line = [block]
            current_y = block["y"]

    if current_line:
        lines.append(" ".join(b["text"] for b in sorted(current_line, key=lambda x: x["x"])))

    return lines


def main(input_dir: str, output_dir: str):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # 初始化 PaddleOCR，中文识别
    ocr_engine = PaddleOCR(
        use_textline_orientation=True,
        lang="ch",
    )

    image_exts = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}
    images = sorted([p for p in input_path.iterdir() if p.suffix.lower() in image_exts])

    summary_md = ["# 图片 OCR 识别结果\n"]

    for img_path in images:
        print(f"OCR: {img_path.name}")
        blocks = ocr_image(ocr_engine, img_path)
        lines = blocks_to_lines(blocks)

        # 保存详细 JSON
        json_path = output_path / f"{img_path.stem}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)

        # 保存 markdown
        md_path = output_path / f"{img_path.stem}.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# {img_path.stem}\n\n")
            f.write(f"**来源图片**: `{img_path}`\n\n")
            f.write("## 识别文本\n\n")
            for line in lines:
                f.write(f"{line}\n\n")

        summary_md.append(f"## {img_path.stem}\n")
        summary_md.append(f"- 识别块数: {len(blocks)}")
        summary_md.append(f"- 详细文件: `{md_path}`")
        summary_md.append(f"- JSON 文件: `{json_path}`\n")
        summary_md.append("### 关键内容摘要\n")
        summary_md.append("\n".join(f"- {line}" for line in lines[:10]))
        summary_md.append("\n---\n")

    # 保存汇总
    summary_path = output_path / "README.md"
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(summary_md))

    print(f"\n完成。输出目录: {output_path}")
    print(f"汇总文件: {summary_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="批量 OCR 图片")
    parser.add_argument("-i", "--input", required=True, help="输入图片目录")
    parser.add_argument("-o", "--output", required=True, help="输出目录")
    args = parser.parse_args()
    main(args.input, args.output)
