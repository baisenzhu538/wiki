#!/usr/bin/env python3
"""
KDO / 洪七公：用 fal.ai FLUX.1 [schnell] 把文章标题转成封面图/信息图。

使用方式：
1. 到 https://fal.ai 注册账号，获取 API key。
2. 设置环境变量：
     set FAL_KEY=your_fal_api_key          (Windows CMD)
     $env:FAL_KEY="your_fal_api_key"       (PowerShell)
     export FAL_KEY=your_fal_api_key       (Linux/Mac/WSL)
3. 运行：
     python 40_outputs/code/scripts/generate-images-fal.py

默认只处理前 3 篇文章作为测试，避免一次性消耗过多额度。
如需批量，可修改 MAX_ARTICLES。
"""

import os
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
import re
import json
import base64
import argparse
from pathlib import Path
from urllib.parse import urlparse

import requests

# ---------------------------------------------------------------------------
# 配置
# ---------------------------------------------------------------------------
WIKI_ROOT = Path(__file__).resolve().parents[3]  # 退到 wiki 根目录
ARTICLES_DIR = WIKI_ROOT / "40_outputs" / "content" / "articles"
OUTPUT_DIR = WIKI_ROOT / "40_outputs" / "content" / "images" / "generative"

# fal.ai 官方 hosted 模型端点
FAL_ENDPOINT = "https://fal.run/fal-ai/flux/schnell"

# 默认只跑 3 篇做测试
MAX_ARTICLES = 3

# 输出图片尺寸
IMAGE_SIZE = "1024x1024"

# 安全：最大 prompt 长度，避免意外超长消费
MAX_PROMPT_LEN = 800


# ---------------------------------------------------------------------------
# 工具函数
# ---------------------------------------------------------------------------
def get_env_key() -> str:
    key = os.environ.get("FAL_KEY")
    if not key:
        raise EnvironmentError(
            "请设置环境变量 FAL_KEY。获取地址：https://fal.ai/dashboard/keys"
        )
    return key.strip()


def extract_title_from_markdown(file_path: Path) -> str:
    """优先读取文章第一个 # 标题，没有则拿文件名做标题。"""
    try:
        text = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = file_path.read_text(encoding="gbk", errors="ignore")

    # 匹配第一个 Markdown H1
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if match:
        return match.group(1).strip()

    # 退化到文件名
    stem = file_path.stem
    stem = re.sub(r"^art_\d+_[a-f0-9]+-", "", stem)
    stem = re.sub(r"[-_]", " ", stem)
    return stem.strip()


def title_to_image_prompt(title: str) -> str:
    """把文章标题扩展成适合 FLUX 的视觉 prompt（英文效果更佳）。"""
    title = title.strip()
    if not title:
        title = "knowledge delivery"

    prompt = (
        f"A clean, modern editorial illustration for an article titled '{title}'. "
        "Minimalist infographic style, soft gradient background, "
        "iconic metaphors, professional knowledge-work aesthetic, "
        "high detail, 4k, suitable for blog cover and social sharing."
    )
    return prompt[:MAX_PROMPT_LEN]


def call_fal_schnell(api_key: str, prompt: str, image_size: str = IMAGE_SIZE) -> bytes:
    """调用 fal.ai FLUX.1 schnell，返回图片二进制。"""
    headers = {
        "Authorization": f"Key {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "prompt": prompt,
        "image_size": image_size,
        "num_inference_steps": 4,  # schnell 是蒸馏 4 步模型
        "seed": None,  # 随机种子
        "enable_safety_checker": False,
    }

    resp = requests.post(FAL_ENDPOINT, headers=headers, json=payload, timeout=120)

    if resp.status_code == 403 and "Exhausted balance" in resp.text:
        raise RuntimeError(
            "fal.ai 账户余额不足或已被锁定。请前往 https://fal.ai/dashboard/billing "
            "添加支付方式或充值后再试。"
        )
    if resp.status_code == 401:
        raise RuntimeError(
            "fal.ai API key 无效或格式错误。请检查 key 是否以 uuid:secret 格式完整复制。"
        )

    resp.raise_for_status()
    data = resp.json()

    # fal.ai 返回的图片通常是一个 URL 列表
    images = data.get("images", [])
    if not images:
        raise RuntimeError(f"fal.ai 返回异常，无图片数据：{json.dumps(data, ensure_ascii=False)[:500]}")

    image_url = images[0].get("url") if isinstance(images[0], dict) else images[0]
    if not image_url or not urlparse(image_url).scheme:
        raise RuntimeError(f"无法识别图片 URL：{image_url}")

    img_resp = requests.get(image_url, timeout=120)
    img_resp.raise_for_status()
    return img_resp.content


def sanitize_filename(title: str) -> str:
    """把标题转成合法文件名。"""
    name = re.sub(r"[^\w\u4e00-\u9fa5-]", "_", title)
    name = re.sub(r"_+", "_", name).strip("_")
    return name[:80]


def main(max_articles: int = MAX_ARTICLES, dry_run: bool = False):
    api_key = None if dry_run else get_env_key()

    if not ARTICLES_DIR.exists():
        raise FileNotFoundError(f"文章目录不存在：{ARTICLES_DIR}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 收集 markdown 文件，按修改时间倒序
    md_files = sorted(ARTICLES_DIR.rglob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    selected = md_files[:max_articles]

    print(f"共找到 {len(md_files)} 篇文章，本次处理前 {len(selected)} 篇\n")

    for idx, md_path in enumerate(selected, 1):
        title = extract_title_from_markdown(md_path)
        prompt = title_to_image_prompt(title)
        safe_name = sanitize_filename(title)
        out_path = OUTPUT_DIR / f"{idx:02d}_{safe_name}.png"

        print(f"[{idx}/{len(selected)}] {title}")
        print(f"       prompt: {prompt[:120]}...")

        if dry_run:
            print("       [DRY RUN] 跳过 API 调用\n")
            continue

        try:
            image_bytes = call_fal_schnell(api_key, prompt)
            out_path.write_bytes(image_bytes)
            print(f"       已保存：{out_path} ({len(image_bytes)} bytes)\n")
        except Exception as e:
            print(f"       [X] 失败：{e}\n")

    print(f"输出目录：{OUTPUT_DIR}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="用 fal.ai FLUX schnell 生成 KDO 文章封面图")
    parser.add_argument(
        "-n", "--count", type=int, default=MAX_ARTICLES,
        help=f"处理文章数量，默认 {MAX_ARTICLES}"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="只打印要处理的标题和 prompt，不真正调用 API"
    )
    args = parser.parse_args()

    main(max_articles=args.count, dry_run=args.dry_run)
