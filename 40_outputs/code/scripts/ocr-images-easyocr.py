#!/usr/bin/env python3
"""
用 EasyOCR 批量识别图片中的文字，输出为 markdown 和结构化素材。
适用于 00_inbox/AI短剧创作 等图片素材的 OCR 处理。
"""
import os
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
import json
import argparse
from pathlib import Path
import easyocr


def ocr_image(reader, image_path: Path) -> list:
    """对单张图片进行 OCR，返回按 y 坐标排序的文本块列表。"""
    result = reader.readtext(str(image_path))
    blocks = []
    for bbox, text, score in result:
        # bbox: [[x1,y1],[x2,y1],[x2,y2],[x1,y2]]
        y = sum(p[1] for p in bbox) / 4
        x = sum(p[0] for p in bbox) / 4
        blocks.append({
            "text": text,
            "score": round(float(score), 3),
            "x": round(x, 1),
            "y": round(y, 1),
        })

    # 按从上到下、从左到右排序
    blocks.sort(key=lambda b: (b["y"] // 40, b["x"]))
    return blocks


def blocks_to_lines(blocks: list, y_threshold: float = 30.0) -> list:
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
            line_text = " ".join(b["text"] for b in sorted(current_line, key=lambda x: x["x"]))
            avg_score = sum(b["score"] for b in current_line) / len(current_line)
            lines.append({"text": line_text, "score": round(avg_score, 2)})
            current_line = [block]
            current_y = block["y"]

    if current_line:
        line_text = " ".join(b["text"] for b in sorted(current_line, key=lambda x: x["x"]))
        avg_score = sum(b["score"] for b in current_line) / len(current_line)
        lines.append({"text": line_text, "score": round(avg_score, 2)})

    return lines


def extract_sections(lines: list) -> dict:
    """简单提取标题和三板斧结构。"""
    title = ""
    sections = []
    current_section = None

    for line in lines:
        text = line["text"].strip()
        if not text:
            continue

        # 找主标题：通常在第一行，包含"罗盘"或"三板斧"
        if not title and ("罗盘" in text or "三板斧" in text or "对比" in text):
            title = text
            continue

        # 找分节标题：包含"第X板斧"或"一、"等
        if "板斧" in text or text.startswith("一、") or text.startswith("二、") or text.startswith("三、"):
            if current_section:
                sections.append(current_section)
            current_section = {"heading": text, "items": []}
            continue

        if current_section:
            current_section["items"].append(text)

    if current_section:
        sections.append(current_section)

    return {"title": title, "sections": sections, "raw_lines": [l["text"] for l in lines]}


def main(input_dir: str, output_dir: str):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    print("正在初始化 EasyOCR（中文+英文，CPU）...")
    reader = easyocr.Reader(["ch_sim", "en"], gpu=False)

    image_exts = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}
    images = sorted([p for p in input_path.iterdir() if p.suffix.lower() in image_exts])

    all_results = []
    summary_md = ["# AI 短剧创作 - 图片 OCR 识别结果\n"]
    summary_md.append(f"识别图片数: {len(images)}\n")
    summary_md.append("---\n")

    for idx, img_path in enumerate(images, 1):
        print(f"[{idx}/{len(images)}] OCR: {img_path.name}")
        blocks = ocr_image(reader, img_path)
        lines = blocks_to_lines(blocks)
        structured = extract_sections(lines)

        all_results.append({
            "image": img_path.name,
            "structured": structured,
            "blocks": blocks,
        })

        # 保存详细 JSON
        json_path = output_path / f"{img_path.stem}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump({
                "image": img_path.name,
                "structured": structured,
                "blocks": blocks,
            }, f, ensure_ascii=False, indent=2)

        # 保存 markdown
        md_path = output_path / f"{img_path.stem}.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# {img_path.stem}\n\n")
            f.write(f"**来源图片**: `{img_path}`\n\n")
            if structured["title"]:
                f.write(f"**主题**: {structured['title']}\n\n")

            f.write("## 结构化内容\n\n")
            if structured["sections"]:
                for sec in structured["sections"]:
                    f.write(f"### {sec['heading']}\n\n")
                    for item in sec["items"]:
                        f.write(f"- {item}\n")
                    f.write("\n")
            else:
                f.write("（未能自动划分章节，详见原始文本）\n\n")

            f.write("## 原始识别文本\n\n")
            for line in lines:
                f.write(f"- {line['text']}  (置信度: {line['score']})\n")

        # 汇总
        summary_md.append(f"## {idx}. {img_path.stem}\n")
        if structured["title"]:
            summary_md.append(f"**主题**: {structured['title']}\n")
        summary_md.append(f"- 识别文本行数: {len(lines)}")
        summary_md.append(f"- 详细文件: `{md_path}`")
        summary_md.append(f"- 结构化 JSON: `{json_path}`\n")

        if structured["sections"]:
            summary_md.append("**结构**: ")
            summary_md.append(" / ".join(sec["heading"] for sec in structured["sections"]))
            summary_md.append("\n")
        summary_md.append("\n---\n")

    # 保存汇总 README
    summary_path = output_path / "README.md"
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(summary_md))

    # 保存老顽童处理素材：合并所有方法论为一个文档
    cookbook_path = output_path / "老顽童-AI短剧创作方法论汇总.md"
    with open(cookbook_path, "w", encoding="utf-8") as f:
        f.write("# 老顽童处理素材：AI 短剧创作方法论汇总\n\n")
        f.write("> 来源：00_inbox/AI短剧创作 图片 OCR 识别\n\n")
        f.write("---\n\n")
        for r in all_results:
            structured = r["structured"]
            f.write(f"## {structured.get('title') or r['image']}\n\n")
            if structured["sections"]:
                for sec in structured["sections"]:
                    f.write(f"### {sec['heading']}\n\n")
                    for item in sec["items"]:
                        f.write(f"- {item}\n")
                    f.write("\n")
            else:
                for line in structured["raw_lines"]:
                    f.write(f"- {line}\n")
                f.write("\n")
            f.write("---\n\n")

    print(f"\n完成。输出目录: {output_path}")
    print(f"汇总文件: {summary_path}")
    print(f"老顽童素材: {cookbook_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="批量 OCR 图片并生成老顽童处理素材")
    parser.add_argument("-i", "--input", required=True, help="输入图片目录")
    parser.add_argument("-o", "--output", required=True, help="输出目录")
    args = parser.parse_args()
    main(args.input, args.output)
