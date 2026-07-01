#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
对 5 张时间管理图片运行 PaddleOCR，输出每图的文本框和识别结果
"""
import json
from pathlib import Path
from paddleocr import PaddleOCR

INPUT_DIR = Path(r"C:\Users\Administrator\Desktop\wiki\00_inbox\时间管理")
OUTPUT_DIR = INPUT_DIR / "_processed"
OUTPUT_DIR.mkdir(exist_ok=True)

# 初始化 OCR（中文+英文，默认模型会自动下载）
ocr = PaddleOCR(
    use_angle_cls=True,
    lang="ch",
    show_log=False,
    use_gpu=False,
)

image_files = sorted(INPUT_DIR.glob("时间管理-*.png"))

results = {}
for img_path in image_files:
    print(f"OCR: {img_path.name}")
    result = ocr.ocr(str(img_path), cls=True)
    # result[0] 是识别结果列表，每个元素 [box, (text, score)]
    lines = []
    if result and result[0]:
        for line in result[0]:
            box, (text, score) = line
            lines.append({
                "text": text,
                "score": round(float(score), 4),
                "box": box,
            })
    results[img_path.name] = lines

    # 同时输出单个 txt
    txt_path = OUTPUT_DIR / f"{img_path.stem}_ocr.txt"
    txt_path.write_text(
        "\n".join(f"{l['text']}" for l in lines),
        encoding="utf-8",
    )

# 汇总 JSON
summary_path = OUTPUT_DIR / "ocr_summary.json"
summary_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nOCR 完成，结果保存在: {OUTPUT_DIR}")
