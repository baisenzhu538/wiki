#!/usr/bin/env python3
"""
用 MiniMax Image-01 国内 API 批量文生图。

使用方式：
    export MINIMAX_API_KEY=你的key
    python generate-images-minimax.py \
        -p "一张极简商务风格的信息图，主题是科学决策" \
        -o "40_outputs/content/images/generative/test.png"

环境变量：
    MINIMAX_API_KEY - MiniMax API key（格式 sk-api-...）
"""
import os
import sys
import json
import argparse
import requests
from pathlib import Path
from urllib.parse import urlparse

API_BASE = "https://api.minimax.chat/v1"
MODEL = "image-01"

DEFAULT_ASPECT_RATIOS = {
    "cover": "16:9",
    "poster": "3:4",
    "square": "1:1",
    "banner": "21:9",
}


def get_api_key():
    key = os.environ.get("MINIMAX_API_KEY")
    if not key:
        raise EnvironmentError("请设置环境变量 MINIMAX_API_KEY")
    return key.strip()


def generate_image(
    api_key: str,
    prompt: str,
    aspect_ratio: str = "16:9",
    n: int = 1,
    width: int = 0,
    height: int = 0,
    style_type: str = "",
    style_weight: float = 0.8,
    response_format: str = "url",
    prompt_optimizer: bool = False,
) -> dict:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "n": n,
        "aspect_ratio": aspect_ratio,
        "response_format": response_format,
        "prompt_optimizer": prompt_optimizer,
    }

    if width and height:
        payload["width"] = width
        payload["height"] = height

    if style_type:
        payload["style"] = {
            "style_type": style_type,
            "style_weight": style_weight,
        }

    resp = requests.post(
        f"{API_BASE}/image_generation",
        headers=headers,
        json=payload,
        timeout=180,
    )
    resp.raise_for_status()
    return resp.json()


def download_image(url: str, output_path: Path) -> Path:
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(r.content)
    return output_path


def main():
    parser = argparse.ArgumentParser(description="用 MiniMax Image-01 文生图")
    parser.add_argument("-p", "--prompt", required=True, help="生成提示词")
    parser.add_argument("-o", "--output", required=True, help="输出图片路径（支持 .png/.jpg）")
    parser.add_argument("-r", "--ratio", default="16:9", help="宽高比，如 16:9 / 1:1 / 3:4 / 21:9")
    parser.add_argument("-n", type=int, default=1, help="生成数量（1-9）")
    parser.add_argument("--style", default="", help="画风：漫画/元气/中世纪/水彩 等")
    parser.add_argument("--optimize", action="store_true", help="开启 prompt 自动优化")
    args = parser.parse_args()

    api_key = get_api_key()

    print(f"正在调用 MiniMax Image-01 ...")
    print(f"提示词: {args.prompt}")
    print(f"输出: {args.output}")

    result = generate_image(
        api_key=api_key,
        prompt=args.prompt,
        aspect_ratio=args.ratio,
        n=args.n,
        style_type=args.style,
        prompt_optimizer=args.optimize,
    )

    # 保存完整响应
    out_path = Path(args.output)
    meta_path = out_path.parent / f"{out_path.stem}_metadata.json"
    meta_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    images = result.get("data", {}).get("image_urls", [])
    if not images:
        # 兼容不同返回结构
        images = result.get("image_urls", []) or result.get("images", [])

    if not images:
        print("未返回图片 URL，完整响应已保存到:", meta_path)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        sys.exit(1)

    saved = []
    for idx, url in enumerate(images):
        if args.n == 1:
            target = out_path
        else:
            target = out_path.parent / f"{out_path.stem}_{idx+1}{out_path.suffix or '.png'}"
        download_image(url, target)
        saved.append(target)
        print(f"已保存: {target}")

    print(f"元数据: {meta_path}")


if __name__ == "__main__":
    main()
