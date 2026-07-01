#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用 MiniMax-M3（通过 Anthropic SDK）对时间管理图片做 OCR + 结构化分析。
本地 OCR 引擎因环境/网络问题无法运行，改用 VLM 内置的图文理解能力完成 OCR 与深度解析。
"""
import os
import json
import base64
from pathlib import Path
from anthropic import Anthropic

INPUT_DIR = Path(r"C:\Users\Administrator\Desktop\wiki\00_inbox\时间管理")
OUTPUT_DIR = INPUT_DIR / "_processed"
OUTPUT_DIR.mkdir(exist_ok=True)

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


def call_m3_for_ocr(image_path: Path) -> str:
    """OCR：提取图中所有可见文字，保持原有排版与层级"""
    print(f"  [OCR] {image_path.name}")
    b64 = encode_image(image_path)
    media_type = "image/png"
    message = client.messages.create(
        model="MiniMax-M3",
        max_tokens=2000,
        system="你是一个高精度 OCR 助手。请只输出图片中的文字内容，尽可能保留原有版式、层级和顺序，不要添加解释。",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "image", "source": {"type": "base64", "media_type": media_type, "data": b64}},
                    {"type": "text", "text": "请提取这张图片中的所有文字，按原有结构输出。只输出文字，不要解释。"},
                ],
            }
        ],
    )
    return "".join([block.text for block in message.content if block.type == "text"])


def call_m3_for_analysis(image_path: Path, ocr_text: str) -> str:
    """VLM：分析图片结构、模型含义与关键洞察"""
    print(f"  [VLM分析] {image_path.name}")
    b64 = encode_image(image_path)
    media_type = "image/png"
    prompt = f"""请对这张图片进行深度结构化分析。图片已 OCR 的文字如下：

--- OCR 文字 ---
{ocr_text}
---

请从以下几个维度给出分析：
1. 图片主题与核心模型/概念
2. 结构拆解（层级、模块、坐标/象限、箭头关系等）
3. 关键要点与策略含义
4. 与「科学时间管理」课程体系的关联
5. 适用场景与实践建议

用中文回答，条理清晰。"""

    message = client.messages.create(
        model="MiniMax-M3",
        max_tokens=3000,
        system="你是一位擅长知识萃取与图解分析的专家，能把复杂图示拆解为清晰、可落地的结构化知识。",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "image", "source": {"type": "base64", "media_type": media_type, "data": b64}},
                    {"type": "text", "text": prompt},
                ],
            }
        ],
    )
    return "".join([block.text for block in message.content if block.type == "text"])


def main():
    image_files = sorted(INPUT_DIR.glob("时间管理-*.png"))
    all_results = {}

    for img_path in image_files:
        print(f"\n处理: {img_path.name}")
        ocr_result = call_m3_for_ocr(img_path)
        analysis_result = call_m3_for_analysis(img_path, ocr_result)

        # 保存单图结果
        single = {
            "ocr": ocr_result,
            "analysis": analysis_result,
        }
        all_results[img_path.name] = single

        md_path = OUTPUT_DIR / f"{img_path.stem}_vlm.md"
        md_path.write_text(
            f"# {img_path.stem}\n\n## OCR 原文\n\n{ocr_result}\n\n## VLM 深度解析\n\n{analysis_result}\n",
            encoding="utf-8",
        )

    # 保存汇总 JSON
    summary_path = OUTPUT_DIR / "vlm_summary.json"
    summary_path.write_text(json.dumps(all_results, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n全部完成，结果保存在: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
