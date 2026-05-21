#!/usr/bin/env python3
"""
Deep Image Parser - 本地调度脚本
用于批量调用多模态AI视觉分析引擎（通过 Hermes agent执行）
或调用本地 PaddleOCR.js fallback。
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime

# === 配置 ===
WIKI_ROOT = Path("/mnt/c/Users/Administrator/Desktop/wiki")
PADDLE_OCR_DIR = Path("/mnt/c/Users/Administrator/ocr-pipeline")
INBOX_DIR = WIKI_ROOT / "00_inbox"
OUTPUT_DIR = WIKI_ROOT / "10_raw" / "parsed"

# === 工具函数 ===

def parse_with_paddle(image_path: str) -> dict:
    """调用本地 PaddleOCR.js 进行简单文字识别"""
    cmd = [
        "node",
        str(PADDLE_OCR_DIR / "ocr-paddle.cjs"),
        image_path
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return {
            "engine": "paddleocr-js",
            "text": result.stdout,
            "stderr": result.stderr,
            "success": result.returncode == 0
        }
    except Exception as e:
        return {"engine": "paddleocr-js", "success": False, "error": str(e)}


def generate_vision_prompt() -> str:
    """生成多模态AI视觉分析的标准 prompt"""
    return (
        "请深度解析这张图片中的全部内容。要求：\n"
        "1. 识别所有文字，包括小字号和密集文字；\n"
        "2. 如果发现表格，用 Markdown 表格格式还原；\n"
        "3. 如果发现公式，用 LaTeX 格式标注；\n"
        "4. 如果发现清单/步骤/条目，用有序或无序列表还原；\n"
        "5. 如果发现对比关系，说明对比维度；\n"
        "6. 识别视觉标记（高亮、红框、颜色等）的语义含义；\n"
        "7. 最终输出一份完整的结构化 Markdown 文档，"
        "保留原始层级和逻辑关系。"
    )


def save_result(image_path: str, result: dict, output_dir: Path) -> Path:
    """保存解析结果到文件"""
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = Path(image_path).stem
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 保存 JSON 元数据
    meta_path = output_dir / f"{stem}_deep_{timestamp}.json"
    meta = {
        "source_image": image_path,
        "parsed_at": timestamp,
        "engine": result.get("engine", "unknown"),
        "success": result.get("success", False)
    }
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    # 保存 Markdown 正文
    md_path = output_dir / f"{stem}_deep_{timestamp}.md"
    text = result.get("text", "")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"<!-- source: {image_path} -->\n")
        f.write(f"<!-- parsed_at: {timestamp} -->\n")
        f.write(f"<!-- engine: {meta['engine']} -->\n\n")
        f.write(text)

    return md_path


def main():
    parser = argparse.ArgumentParser(description="Deep Image Parser - 图片深度解析")
    parser.add_argument("--image", "-i", help="单张图片路径")
    parser.add_argument("--input-dir", "-d", help="批量处理目录")
    parser.add_argument("--output-dir", "-o", default=str(OUTPUT_DIR), help="输出目录")
    parser.add_argument("--engine", "-e", choices=["auto", "paddle", "vision"], default="auto",
                        help="引擎选择: auto=自动判断, paddle=本地OCR, vision=多模态AI")
    parser.add_argument("--prompt", "-p", action="store_true", help="只输出标准 prompt，不执行识别")
    args = parser.parse_args()

    if args.prompt:
        print(generate_vision_prompt())
        sys.exit(0)

    output_dir = Path(args.output_dir)

    # 收集待处理图片
    images = []
    if args.image:
        images = [args.image]
    elif args.input_dir:
        input_dir = Path(args.input_dir)
        images = sorted([
            str(p) for p in input_dir.iterdir()
            if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp", ".gif")
        ])
    else:
        print("错误: 请指定 --image 或 --input-dir")
        sys.exit(1)

    print(f"[深度图像解析] 共发现 {len(images)} 张图片")
    print(f"[输出目录] {output_dir}")
    print(f"[引擎模式] {args.engine}")
    print("")

    for img_path in images:
        print(f"处理中: {img_path} ...", end=" ")

        if args.engine == "paddle":
            result = parse_with_paddle(img_path)
            print("✅ PaddleOCR" if result["success"] else "❌ 失败")
        else:
            # auto / vision: 输出 prompt 说明需要手动调用 vision_analyze
            print("")
            print("  → 请使用 Hermes vision_analyze 工具调用：")
            print(f"     image_url: {img_path}")
            print(f"     prompt: [见下方标准提示词]")
            print("")
            print(generate_vision_prompt())
            continue

        if result.get("success"):
            saved = save_result(img_path, result, output_dir)
            print(f"  → 已保存: {saved}")

    print("\n[完成] 所有图片处理结束。")


if __name__ == "__main__":
    main()
