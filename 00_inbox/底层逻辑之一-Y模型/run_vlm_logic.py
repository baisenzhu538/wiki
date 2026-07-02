#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用 MiniMax-M3（通过 Anthropic SDK）对底层逻辑图片做 OCR + 结构化分析。
"""
import os
import json
import base64
from pathlib import Path
from anthropic import Anthropic

INPUT_DIR = Path(r"C:\Users\Administrator\Desktop\wiki\00_inbox\底层逻辑")
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


def analyze_image(image_path: Path) -> dict:
    """单图 OCR + 深度分析"""
    print(f"处理: {image_path.name}")
    b64 = encode_image(image_path)
    media_type = "image/png"

    system_prompt = """你是一位擅长底层逻辑、第一性原理、科学方法论的知识萃取专家。
请严格按以下格式输出：

【OCR原文】
提取图片中所有可见文字，保留版式与层级。

【图片类型】
判断属于：框架图/流程图/对比卡/雷达图/清单表/案例图/其他

【核心内容】
用3-5条 bullet points 总结图片核心信息。

【结构化解析】
如果图中有模型、矩阵、红卡蓝卡对比、阶段、清单，请用表格或分级列表呈现。

【与一堂科学理念的关联】
指出这张图在一堂科学理念体系中的位置和价值。

【落地应用建议】
给出1-3条可直接用于分析问题或做决策的建议。"""

    message = client.messages.create(
        model="MiniMax-M3",
        max_tokens=3000,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "image", "source": {"type": "base64", "media_type": media_type, "data": b64}},
                    {"type": "text", "text": "请对这张底层逻辑/科学理念课程图片进行 OCR + 结构化深度解析。"},
                ],
            }
        ],
    )
    text = "".join([block.text for block in message.content if block.type == "text"])
    return {"analysis": text}


def main():
    image_files = sorted(INPUT_DIR.glob("*.png"))
    all_results = {}

    for idx, img_path in enumerate(image_files, 1):
        try:
            result = analyze_image(img_path)
            all_results[img_path.name] = result

            md_path = OUTPUT_DIR / f"{img_path.stem}_vlm.md"
            md_path.write_text(
                f"# {img_path.stem}\n\n{result['analysis']}\n",
                encoding="utf-8",
            )
            print(f"  [{idx}/{len(image_files)}] 完成")
        except Exception as e:
            print(f"  [{idx}/{len(image_files)}] 失败: {e}")
            all_results[img_path.name] = {"error": str(e)}

    summary_path = OUTPUT_DIR / "vlm_summary.json"
    summary_path.write_text(json.dumps(all_results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n全部完成，结果保存在: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
