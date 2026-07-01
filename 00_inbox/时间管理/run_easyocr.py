#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
对 5 张时间管理图片运行 EasyOCR（中文+英文），输出识别文本
"""
import json
from pathlib import Path
import easyocr

INPUT_DIR = Path(r"C:\Users\Administrator\Desktop\wiki\00_inbox\时间管理")
OUTPUT_DIR = INPUT_DIR / "_processed"
OUTPUT_DIR.mkdir(exist_ok=True)

# 初始化 EasyOCR：中文简体 + 英文
reader = easyocr.Reader(["ch_sim", "en"], gpu=False)

image_files = sorted(INPUT_DIR.glob("时间管理-*.png"))

results = {}
for img_path in image_files:
    print(f"OCR: {img_path.name}")
    result = reader.readtext(str(img_path))
    lines = []
    for (bbox, text, conf) in result:
        lines.append({
            "text": text,
            "score": round(float(conf), 4),
            "bbox": bbox,
        })
    results[img_path.name] = lines

    # 输出单个 txt
    txt_path = OUTPUT_DIR / f"{img_path.stem}_ocr.txt"
    txt_path.write_text(
        "\n".join(f"{l['text']}" for l in lines),
        encoding="utf-8",
    )

# 汇总 JSON
summary_path = OUTPUT_DIR / "easyocr_summary.json"
summary_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nOCR 完成，结果保存在: {OUTPUT_DIR}")
