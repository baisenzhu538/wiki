#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
aesthetic-library-builder.py

按照 Truman 在双三角课程中演示的审美建立方法，把「审美库建设」流程化：
1. 拆细颗粒度话题（topic）
2. 批量收集最佳实践案例（图片 / 网页 / 视频 / 文本）
3. 用 60-99 分标尺打分、筛选
4. 总结规律，生成可供 Agent 调用的 DataPack

用法示例：
    python kdo-tools/aesthetic-library-builder.py init ppt-commercial-training
    python kdo-tools/aesthetic-library-builder.py collect ppt-commercial-training --urls urls.txt --local ./raw_ppt_screenshots
    python kdo-tools/aesthetic-library-builder.py score ppt-commercial-training --criteria criteria.md
    python kdo-tools/aesthetic-library-builder.py curate ppt-commercial-training --top 50
    python kdo-tools/aesthetic-library-builder.py summarize ppt-commercial-training --output ./data_packs/ppt-aesthetic.md

环境要求：
    pip install requests beautifulsoup4 pillow
"""

import argparse
import base64
import hashlib
import json
import os
import shutil
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# 可选依赖：requests / bs4 / PIL
REQS = []
try:
    import requests
    REQS.append("requests")
except ImportError:  # pragma: no cover
    requests = None
try:
    from bs4 import BeautifulSoup
    REQS.append("bs4")
except ImportError:  # pragma: no cover
    BeautifulSoup = None
try:
    from PIL import Image
    REQS.append("pillow")
except ImportError:  # pragma: no cover
    Image = None


VAULT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_LIBS_DIR = VAULT_ROOT / "aesthetic-libs"
DEFAULT_DATA_PACKS_DIR = VAULT_ROOT / "data_packs"


def _ensure_deps() -> None:
    missing = []
    if requests is None:
        missing.append("requests")
    if BeautifulSoup is None:
        missing.append("beautifulsoup4")
    if Image is None:
        missing.append("pillow")
    if missing:
        print(f"[ERROR] 缺少依赖：{', '.join(missing)}")
        print("请运行：pip install " + " ".join(missing))
        sys.exit(1)


def _load_config(topic_dir: Path) -> Dict:
    config_path = topic_dir / "config.json"
    if not config_path.exists():
        print(f"[ERROR] 主题 {topic_dir.name} 尚未初始化")
        sys.exit(1)
    return json.loads(config_path.read_text(encoding="utf-8"))


def _save_config(topic_dir: Path, config: Dict) -> None:
    config_path = topic_dir / "config.json"
    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")


def _load_manifest(topic_dir: Path) -> List[Dict]:
    manifest_path = topic_dir / "manifest.jsonl"
    if not manifest_path.exists():
        return []
    items = []
    for line in manifest_path.read_text(encoding="utf-8").strip().splitlines():
        if line.strip():
            items.append(json.loads(line))
    return items


def _save_manifest(topic_dir: Path, items: List[Dict]) -> None:
    manifest_path = topic_dir / "manifest.jsonl"
    lines = [json.dumps(item, ensure_ascii=False) for item in items]
    manifest_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _hash_url(url: str) -> str:
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]


def _hash_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()[:16]


def _guess_mimetype(path: Path) -> str:
    suffix = path.suffix.lower()
    mapping = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".webp": "image/webp",
        ".mp4": "video/mp4",
        ".mov": "video/quicktime",
        ".pdf": "application/pdf",
        ".md": "text/markdown",
        ".txt": "text/plain",
        ".html": "text/html",
    }
    return mapping.get(suffix, "application/octet-stream")


def cmd_init(args: argparse.Namespace) -> None:
    topic_dir = DEFAULT_LIBS_DIR / args.topic
    if topic_dir.exists():
        print(f"[WARN] 主题 {args.topic} 已存在，将复用目录")
    else:
        (topic_dir / "assets").mkdir(parents=True)
        (topic_dir / "curated").mkdir(parents=True)
        print(f"[OK] 创建主题目录：{topic_dir}")

    config = {
        "topic": args.topic,
        "created_at": datetime.now().isoformat(),
        "description": args.description or "",
        "criteria": [],
        "score_model": args.score_model or os.getenv("AESTHETIC_SCORE_MODEL", "deepseek-chat"),
        "notes": "按照 Truman 审美建立法：拆细话题 → 收集案例 → 打分筛选 → 总结规律",
    }
    _save_config(topic_dir, config)
    print(f"[OK] 写入配置：{topic_dir / 'config.json'}")


def _fetch_url(url: str, timeout: int = 30) -> bytes:
    _ensure_deps()
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
    }
    resp = requests.get(url, headers=headers, timeout=timeout)
    resp.raise_for_status()
    return resp.content


def _collect_from_local(topic_dir: Path, local_path: Path, label: str = "local") -> List[Dict]:
    assets_dir = topic_dir / "assets"
    items = []
    for path in local_path.rglob("*"):
        if not path.is_file():
            continue
        mimetype = _guess_mimetype(path)
        if mimetype == "application/octet-stream":
            continue
        file_hash = _hash_file(path)
        dest = assets_dir / f"{file_hash}{path.suffix}"
        if not dest.exists():
            shutil.copy2(path, dest)
        items.append({
            "id": file_hash,
            "source": str(path),
            "source_type": label,
            "mimetype": mimetype,
            "local_path": str(dest.relative_to(topic_dir)),
            "collected_at": datetime.now().isoformat(),
            "score": None,
            "score_reason": "",
            "tags": [],
        })
    return items


def _collect_from_urls(topic_dir: Path, urls: List[str]) -> List[Dict]:
    _ensure_deps()
    assets_dir = topic_dir / "assets"
    items = []
    for url in urls:
        url = url.strip()
        if not url:
            continue
        uid = _hash_url(url)
        try:
            data = _fetch_url(url)
            # 尝试从 Content-Type 或 URL 推断后缀
            suffix = Path(url.split("?")[0]).suffix.lower()
            if not suffix or suffix not in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".mp4", ".mov", ".pdf", ".html"}:
                # 默认保存为 html，后续解析
                suffix = ".html"
            dest = assets_dir / f"{uid}{suffix}"
            dest.write_bytes(data)
            items.append({
                "id": uid,
                "source": url,
                "source_type": "url",
                "mimetype": _guess_mimetype(dest),
                "local_path": str(dest.relative_to(topic_dir)),
                "collected_at": datetime.now().isoformat(),
                "score": None,
                "score_reason": "",
                "tags": [],
            })
        except Exception as e:
            print(f"[WARN] 抓取失败 {url}: {e}")
        time.sleep(0.5)
    return items


def cmd_collect(args: argparse.Namespace) -> None:
    topic_dir = DEFAULT_LIBS_DIR / args.topic
    config = _load_config(topic_dir)
    items = _load_manifest(topic_dir)
    existing_ids = {it["id"] for it in items}

    new_items: List[Dict] = []
    if args.local:
        local_path = Path(args.local)
        if not local_path.exists():
            print(f"[ERROR] 本地路径不存在：{local_path}")
            sys.exit(1)
        new_items.extend(_collect_from_local(topic_dir, local_path, label="local"))

    if args.urls:
        url_file = Path(args.urls)
        if not url_file.exists():
            print(f"[ERROR] URL 文件不存在：{url_file}")
            sys.exit(1)
        urls = url_file.read_text(encoding="utf-8").strip().splitlines()
        new_items.extend(_collect_from_urls(topic_dir, urls))

    added = 0
    for it in new_items:
        if it["id"] not in existing_ids:
            items.append(it)
            existing_ids.add(it["id"])
            added += 1
        else:
            print(f"[SKIP] 已存在：{it['source']}")

    _save_manifest(topic_dir, items)
    print(f"[OK] 本次新增 {added} 条，主题 {args.topic} 共 {len(items)} 条")


def _image_to_base64(path: Path) -> str:
    _ensure_deps()
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def _resize_if_needed(path: Path, max_size: int = 1024) -> Path:
    _ensure_deps()
    try:
        img = Image.open(path)
        img.thumbnail((max_size, max_size))
        resized = path.parent / (path.stem + "_resized" + path.suffix)
        img.save(resized)
        return resized
    except Exception:
        return path


def _call_llm_score(prompt: str, model: str, api_key: Optional[str]) -> Optional[str]:
    _ensure_deps()
    api_key = api_key or os.getenv("DEEPSEEK_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("[ERROR] 未提供 API key。请设置 DEEPSEEK_API_KEY 或 OPENAI_API_KEY，或传 --api-key")
        sys.exit(1)

    base_url = os.getenv("DEEPSEEK_API_BASE", "https://api.deepseek.com/v1")
    client_type = os.getenv("AESTHETIC_CLIENT", "openai")

    if client_type == "requests":
        resp = requests.post(
            f"{base_url}/chat/completions",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.3,
            },
            timeout=120,
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]

    # 优先使用 openai SDK（如果已安装）
    try:
        import openai
        client = openai.OpenAI(api_key=api_key, base_url=base_url)
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        return completion.choices[0].message.content
    except ImportError:
        # 回退到 requests
        os.environ["AESTHETIC_CLIENT"] = "requests"
        return _call_llm_score(prompt, model, api_key)


def _build_score_prompt(item: Dict, criteria_text: str) -> str:
    topic = item.get("topic", "审美对象")
    source = item["source"]
    mimetype = item["mimetype"]
    if mimetype.startswith("image/"):
        content_desc = f"这是一张图片素材，来源：{source}"
    elif mimetype.startswith("video/"):
        content_desc = f"这是一个视频素材，来源：{source}"
    elif mimetype.startswith("text/"):
        content_desc = f"这是一个文本/网页素材，来源：{source}"
    else:
        content_desc = f"这是一个素材，来源：{source}"

    prompt = f"""你是一位严格的审美评委。请对以下素材在「{topic}」主题下进行打分。

{content_desc}

评分标准：
{criteria_text}

请只输出一个 60-99 之间的整数分数，以及一段不超过 100 字的简短理由。
输出格式必须严格如下：
分数：<整数>
理由：<理由>
"""
    return prompt


def _extract_score(text: str) -> Optional[int]:
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("分数：") or line.startswith("分数:"):
            try:
                return int(line.split("：")[-1].split(":")[-1].strip())
            except ValueError:
                continue
    # fallback：找第一个 60-99 的整数
    import re
    nums = [int(n) for n in re.findall(r"\b\d{2}\b", text) if 60 <= int(n) <= 99]
    return nums[0] if nums else None


def cmd_score(args: argparse.Namespace) -> None:
    topic_dir = DEFAULT_LIBS_DIR / args.topic
    config = _load_config(topic_dir)
    items = _load_manifest(topic_dir)

    criteria_text = ""
    if args.criteria:
        criteria_path = Path(args.criteria)
        if criteria_path.exists():
            criteria_text = criteria_path.read_text(encoding="utf-8")
    if not criteria_text:
        criteria_text = (
            "60-69：有明显缺陷，不建议参考；\n"
            "70-79：及格，有局部可取之处；\n"
            "80-89：优秀，可作为主要参考；\n"
            "90-99：顶尖，值得反复研究临摹。"
        )

    model = args.model or config.get("score_model", "deepseek-chat")
    api_key = args.api_key or os.getenv("DEEPSEEK_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key and not args.dry_run:
        print("[ERROR] 打分需要 LLM API key。请设置 DEEPSEEK_API_KEY 或传 --api-key")
        sys.exit(1)

    unscored = [it for it in items if it.get("score") is None or args.rescore]
    if not unscored:
        print("[OK] 所有素材已打分")
        return

    for idx, it in enumerate(unscored, 1):
        print(f"[{idx}/{len(unscored)}] 打分：{it['source']}")
        if args.dry_run:
            it["score"] = 75
            it["score_reason"] = "dry-run 默认分数"
            continue

        prompt = _build_score_prompt(it, criteria_text)
        # 如果是图片，把图片转成 base64 加入 prompt
        if it["mimetype"].startswith("image/") and Image is not None:
            asset_path = topic_dir / it["local_path"]
            resized = _resize_if_needed(asset_path)
            b64 = _image_to_base64(resized)
            # 简化：先调用纯文本 prompt；后续可升级为 vision model
            prompt += "\n\n[注意：图片素材已本地保存，请基于来源描述和常见审美标准评分。]"

        try:
            result = _call_llm_score(prompt, model, api_key)
            score = _extract_score(result) if result else None
            if score is None:
                print(f"[WARN] 无法解析分数：{result}")
                continue
            it["score"] = score
            it["score_reason"] = result
            print(f"       → {score}")
        except Exception as e:
            print(f"[WARN] 打分失败：{e}")

    _save_manifest(topic_dir, items)
    scored = [it for it in items if it.get("score") is not None]
    print(f"[OK] 已完成 {len(scored)}/{len(items)} 条打分")


def cmd_curate(args: argparse.Namespace) -> None:
    topic_dir = DEFAULT_LIBS_DIR / args.topic
    items = _load_manifest(topic_dir)
    scored = [it for it in items if it.get("score") is not None]
    if not scored:
        print("[ERROR] 没有已打分的素材，请先运行 score")
        sys.exit(1)
    scored.sort(key=lambda x: x["score"], reverse=True)
    top_n = args.top or len(scored)
    selected = scored[:top_n]

    curated_dir = topic_dir / "curated"
    curated_dir.mkdir(exist_ok=True)
    for it in selected:
        src = topic_dir / it["local_path"]
        dest = curated_dir / f"{it['score']:02d}_{it['id']}{Path(src).suffix}"
        if not dest.exists():
            shutil.copy2(src, dest)

    summary = {
        "topic": args.topic,
        "curated_at": datetime.now().isoformat(),
        "total_scored": len(scored),
        "selected_count": len(selected),
        "score_range": f"{selected[-1]['score']} - {selected[0]['score']}",
        "items": selected,
    }
    (topic_dir / "curated_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"[OK] 精选 {len(selected)} 条到 {curated_dir}，分数区间 {summary['score_range']}")


def cmd_summarize(args: argparse.Namespace) -> None:
    topic_dir = DEFAULT_LIBS_DIR / args.topic
    config = _load_config(topic_dir)
    items = _load_manifest(topic_dir)
    scored = sorted([it for it in items if it.get("score")], key=lambda x: x["score"], reverse=True)
    if not scored:
        print("[ERROR] 没有已打分素材")
        sys.exit(1)

    output = Path(args.output) if args.output else DEFAULT_DATA_PACKS_DIR / f"{args.topic}-aesthetic.md"
    output.parent.mkdir(parents=True, exist_ok=True)

    top_items = scored[: args.top]
    lines = [
        "---",
        f"id: datapack-{args.topic}-aesthetic",
        f"title: {config['topic']} 审美库 DataPack",
        "type: datapack",
        "status: enriched",
        f"source_refs:",
        f"- aesthetic-libs/{args.topic}",
        "---",
        "",
        f"# {config['topic']} 审美库 DataPack",
        "",
        f"> 主题：{config.get('description', '')}",
        f"> 精选数量：{len(top_items)} / {len(scored)}（按 60-99 分排序）",
        f"> 生成时间：{datetime.now().isoformat()}",
        "",
        "## 使用方式",
        "",
        "1. 在 Agent system prompt 中引用本 DataPack 作为审美参考。",
        "2. 生成输出前，要求 Agent 先对照本库中的高分布案例进行自我检查。",
        "3. 定期用 `aesthetic-library-builder.py collect/score/curate` 更新本库。",
        "",
        "## 审美要点（待人工补充）",
        "",
        "- 高分布案例共同特征：",
        "- 低分布案例共同问题：",
        "- 本主题下「好」的维度定义：",
        "",
        "## 精选案例",
        "",
    ]
    for it in top_items:
        local = topic_dir / it["local_path"]
        rel = local.relative_to(VAULT_ROOT) if local.exists() else it["local_path"]
        lines.append(f"### {it['score']} 分 · {it['id']}")
        lines.append(f"- 来源：{it['source']}")
        lines.append(f"- 类型：{it['mimetype']}")
        lines.append(f"- 本地路径：`{rel}`")
        if it.get("score_reason"):
            reason = it["score_reason"].replace("\n", " ")
            lines.append(f"- 评分理由：{reason}")
        lines.append("")

    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"[OK] 生成 DataPack：{output}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="审美库建设工具：拆话题 → 收案例 → 打分 → 精选 → 生成 DataPack",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--libs-dir", default=str(DEFAULT_LIBS_DIR), help="审美库根目录")
    parser.add_argument("--data-packs-dir", default=str(DEFAULT_DATA_PACKS_DIR), help="DataPack 输出根目录")
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", help="初始化一个审美主题")
    p_init.add_argument("topic", help="主题名称，如 ppt-commercial-training")
    p_init.add_argument("--description", default="", help="主题描述")
    p_init.add_argument("--score-model", default="deepseek-chat", help="打分模型")
    p_init.set_defaults(func=cmd_init)

    p_collect = sub.add_parser("collect", help="收集案例素材")
    p_collect.add_argument("topic")
    p_collect.add_argument("--local", help="本地素材目录")
    p_collect.add_argument("--urls", help="URL 列表文件，每行一个")
    p_collect.set_defaults(func=cmd_collect)

    p_score = sub.add_parser("score", help="用 LLM 给素材打分")
    p_score.add_argument("topic")
    p_score.add_argument("--criteria", help="评分标准 markdown 文件")
    p_score.add_argument("--model", help="覆盖默认打分模型")
    p_score.add_argument("--api-key", help="LLM API key")
    p_score.add_argument("--rescore", action="store_true", help="对已打分素材重新打分")
    p_score.add_argument("--dry-run", action="store_true", help="测试模式，给默认分数")
    p_score.set_defaults(func=cmd_score)

    p_curate = sub.add_parser("curate", help="精选高分布案例")
    p_curate.add_argument("topic")
    p_curate.add_argument("--top", type=int, default=50, help="精选数量")
    p_curate.set_defaults(func=cmd_curate)

    p_summarize = sub.add_parser("summarize", help="生成 DataPack")
    p_summarize.add_argument("topic")
    p_summarize.add_argument("--output", help="输出文件路径")
    p_summarize.add_argument("--top", type=int, default=50, help="写入 DataPack 的案例数量")
    p_summarize.set_defaults(func=cmd_summarize)

    args = parser.parse_args()
    args.libs_dir = Path(args.libs_dir)
    args.data_packs_dir = Path(args.data_packs_dir)
    # 更新模块级默认路径
    import sys
    sys.modules[__name__].DEFAULT_LIBS_DIR = args.libs_dir
    sys.modules[__name__].DEFAULT_DATA_PACKS_DIR = args.data_packs_dir
    args.func(args)


if __name__ == "__main__":
    main()
