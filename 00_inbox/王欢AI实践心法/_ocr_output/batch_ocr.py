#!/usr/bin/env python3
"""
使用 _tmp/ocr_venv 中的 RapidOCR 批量识别王欢 AI 实战分享图片。
输出：每张图片一个 markdown 文件 + 汇总 README.md + 合并原始文本。
"""
import json
from pathlib import Path
from rapidocr import RapidOCR

INPUT_DIR = Path("00_inbox/王欢AI实践心法/_ocr_input")
OUTPUT_DIR = Path("00_inbox/王欢AI实践心法/_ocr_output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def ocr_image(engine, image_path: Path):
    """对单张图片 OCR，返回按阅读顺序排列的文本行。"""
    result = engine(str(image_path))
    if not result or not result.txts:
        return []

    blocks = []
    for box, text, score in zip(result.boxes, result.txts, result.scores):
        y = sum(p[1] for p in box) / 4
        x = sum(p[0] for p in box) / 4
        blocks.append({
            "text": text,
            "score": round(float(score), 3),
            "x": round(float(x), 1),
            "y": round(float(y), 1),
        })

    # 按从上到下、从左到右排序
    blocks.sort(key=lambda b: (b["y"] // 30, b["x"]))

    # 合并同一行
    lines = []
    if not blocks:
        return lines

    current_line = [blocks[0]]
    current_y = blocks[0]["y"]
    y_threshold = 25.0

    for block in blocks[1:]:
        if abs(block["y"] - current_y) <= y_threshold:
            current_line.append(block)
        else:
            line_text = " ".join(b["text"] for b in sorted(current_line, key=lambda x: x["x"]))
            lines.append({
                "text": line_text,
                "score": round(sum(b["score"] for b in current_line) / len(current_line), 2),
            })
            current_line = [block]
            current_y = block["y"]

    if current_line:
        line_text = " ".join(b["text"] for b in sorted(current_line, key=lambda x: x["x"]))
        lines.append({
            "text": line_text,
            "score": round(sum(b["score"] for b in current_line) / len(current_line), 2),
        })

    return lines


def main():
    engine = RapidOCR()
    images = sorted(INPUT_DIR.glob("*.png"))

    summary = ["# 王欢 AI 实战分享 — 图片 OCR 识别汇总\n"]
    summary.append(f"识别图片数：{len(images)}\n")
    summary.append("---\n")

    all_raw = ["# 王欢 AI 实战分享 — OCR 原始文本合并\n"]

    for idx, img_path in enumerate(images, 1):
        print(f"[{idx}/{len(images)}] OCR: {img_path.name}")
        lines = ocr_image(engine, img_path)

        # 保存单张图片结果
        md_path = OUTPUT_DIR / f"{img_path.stem}.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# {img_path.stem}\n\n")
            f.write(f"**来源图片**: `{img_path.name}`\n\n")
            f.write("## 识别文本\n\n")
            for line in lines:
                f.write(f"- {line['text']}  (置信度: {line['score']})\n")

        # 保存 JSON
        json_path = OUTPUT_DIR / f"{img_path.stem}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(lines, f, ensure_ascii=False, indent=2)

        # 汇总
        summary.append(f"## {idx}. {img_path.stem}\n")
        summary.append(f"- 识别行数: {len(lines)}")
        summary.append(f"- Markdown: `{md_path}`")
        summary.append(f"- JSON: `{json_path}`\n")
        if lines:
            summary.append("**关键内容预览**: \n")
            summary.append("\n".join(f"- {line['text']}" for line in lines[:8]))
            summary.append("\n")
        summary.append("\n---\n")

        # 合并原始文本
        all_raw.append(f"\n## {img_path.stem}\n")
        for line in lines:
            all_raw.append(line["text"])
        all_raw.append("")

    # 保存汇总
    readme_path = OUTPUT_DIR / "README.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(summary))

    # 保存合并原始文本
    raw_path = OUTPUT_DIR / "all_ocr_raw.md"
    with open(raw_path, "w", encoding="utf-8") as f:
        f.write("\n".join(all_raw))

    print(f"\n完成。输出目录: {OUTPUT_DIR}")
    print(f"汇总文件: {readme_path}")
    print(f"合并原始文本: {raw_path}")


if __name__ == "__main__":
    main()
