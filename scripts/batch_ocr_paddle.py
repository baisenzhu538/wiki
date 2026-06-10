#!/usr/bin/env python3
"""批量OCR处理脚本
扫描00_inbox中未OCR的图片，用PaddleOCR 3.x处理后输出到ocr_ingest/
"""
import os
import sys
import re
from datetime import datetime, timezone

# 添加paddleocr所在路径
sys.path.insert(0, '/home/dministrator/.local/lib/python3.10/site-packages')

import warnings
warnings.filterwarnings('ignore')

from paddleocr import PaddleOCR

BASE = "/mnt/c/Users/Administrator/Desktop/wiki"
INBOX = os.path.join(BASE, "00_inbox")
OCR_DIR = os.path.join(INBOX, "ocr_ingest")
os.makedirs(OCR_DIR, exist_ok=True)

# 初始化PaddleOCR（禁用不需要的预处理）
print("[INIT] Loading PaddleOCR models...")
ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False
)
print("[INIT] PaddleOCR ready")

def simplify_name(name):
    """将文件名转换为OCR文件名的安全格式"""
    name = os.path.splitext(name)[0]
    # 替换非字母数字中文字符为下划线
    safe = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9]', '_', name)
    # 去掉连续下划线
    safe = re.sub(r'_+', '_', safe)
    safe = safe.strip('_')
    return safe

def get_all_images():
    """获取00_inbox中的所有图片"""
    images = []
    for root, dirs, files in os.walk(INBOX):
        # 只搜索两层（不进ocr_ingest）
        depth = root.count(os.sep) - INBOX.count(os.sep)
        if depth >= 2:
            continue
        if "ocr_ingest" in root:
            continue
        for f in files:
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                images.append(os.path.join(root, f))
    return sorted(images)

def get_existing_ocr_names():
    """获取已有OCR文件的名称集合"""
    if not os.path.exists(OCR_DIR):
        return set()
    names = set()
    for f in os.listdir(OCR_DIR):
        if f.startswith("src_ocr_") and f.endswith(".md"):
            core = f.replace("src_ocr_", "").replace(".md", "")
            names.add(core)
    return names

def has_ocr(img_path, existing_names):
    """检查图片是否已有OCR"""
    simp = simplify_name(os.path.basename(img_path))
    for ocr_name in existing_names:
        if simp == ocr_name or simp in ocr_name or ocr_name in simp:
            return True
    return False

def run_ocr(img_path):
    """对单张图片运行OCR"""
    try:
        result = ocr.predict(img_path)
        texts = []
        if result:
            for res in result:
                if hasattr(res, 'res') and res.res:
                    for item in res.res.get('rec_texts', []):
                        texts.append(item)
                elif isinstance(res, list):
                    for line in res:
                        if isinstance(line, list) and len(line) >= 2:
                            texts.append(line[1][0] if isinstance(line[1], tuple) else str(line[1]))
        return '\n'.join(texts) if texts else "[NO TEXT FOUND]"
    except Exception as e:
        return f"[OCR ERROR] {e}"

def write_ocr_file(img_path, text):
    """写入OCR结果文件"""
    rel_path = os.path.relpath(img_path, BASE)
    basename = os.path.basename(img_path)
    safe_name = simplify_name(basename)
    source_id = f"src_ocr_{safe_name}"
    output_file = os.path.join(OCR_DIR, f"{source_id}.md")

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
    char_count = len(text)

    content = f"""---
source_id: "{source_id}"
kind: "image_ocr"
captured_at: "{now}"
original_image: "{rel_path}"
ocr_engine: "paddleocr"
char_count: {char_count}
trust_level: "medium"
freshness: "{now[:7]}"
rights: "yitang_course_material"
---

# OCR: {os.path.splitext(basename)[0]}

原图: `{rel_path}`

## OCR 原文

{text}

## 备注

- 本文件由 PaddleOCR 自动提取
- 可能存在连字/误识，需要人工校对
- 视觉结构信息（标题/正文/表格分块）未在 OCR 中体现，需要结合原图理解
"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    return output_file

def main():
    print("[SCAN] Finding images...")
    all_images = get_all_images()
    existing_ocr = get_existing_ocr_names()

    # 过滤已处理的图片
    todo = [img for img in all_images if not has_ocr(img, existing_ocr)]

    print(f"[SCAN] Total images: {len(all_images)}")
    print(f"[SCAN] Existing OCR: {len(existing_ocr)}")
    print(f"[SCAN] To process: {len(todo)}")
    print()

    success = 0
    failed = 0
    skipped = len(all_images) - len(todo)

    for i, img_path in enumerate(todo, 1):
        basename = os.path.basename(img_path)
        print(f"[{i}/{len(todo)}] Processing: {basename}")

        text = run_ocr(img_path)
        if text.startswith("[OCR ERROR]"):
            print(f"  ❌ FAILED: {text[:100]}")
            failed += 1
            continue

        out_file = write_ocr_file(img_path, text)
        print(f"  ✅ OK: {len(text)} chars -> {os.path.basename(out_file)}")
        success += 1

    print()
    print("=" * 50)
    print(f"Batch OCR Complete")
    print(f"  Total images: {len(all_images)}")
    print(f"  Skipped (already OCR'd): {skipped}")
    print(f"  Success: {success}")
    print(f"  Failed: {failed}")
    print(f"  Output dir: {OCR_DIR}")
    print("=" * 50)

if __name__ == "__main__":
    main()
