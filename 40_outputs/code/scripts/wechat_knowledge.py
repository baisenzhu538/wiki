#!/usr/bin/env python3
"""视频号逐字稿 → 知识化（Phase 2，proj_20260816_wechat-collect）。

把 00_inbox/wechat-collect/ 里的逐字稿用 LLM 总结为楚门三层次（事实/规律/洞察），
产出研究文档（weixin-favor-kb 五段模板 + 三层次）——先落 inbox，validate 后再入 30_wiki/。

用法:
  python kdo-tools/wechat_knowledge.py <transcript_md> [--output <研究文档路径>]
  python kdo-tools/wechat_knowledge.py --all     # 处理所有未知识化的 src_wechat_*
"""
import argparse
import json
import os
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

# 系统代理(MITM 工具)会拦 API 直连——LLM 调用必须绕过代理
os.environ.setdefault("NO_PROXY", "api.deepseek.com,api.minimaxi.com")

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIKI = Path(__file__).resolve().parent.parent
# 铁律（用户 2026-08-17 纠偏）：新内容第一站必须是 00_inbox/，未经处理不放 10_raw/ 和 30_wiki/
INBOX_DIR = WIKI / "00_inbox" / "wechat-collect"
OUTPUTS_DIR = INBOX_DIR / "knowledge"  # 研究文档先落 inbox，validate 后再入 30_wiki/

# DeepSeek（与 Hermes 同款）
API_URL = "https://api.deepseek.com/v1/chat/completions"
MODEL = "deepseek-v4-flash"

TRIPLE_FRAMEWORK_PROMPT = """你是知识萃取专家。把下面的视频逐字稿按"事实 / 规律 / 洞察"三层次总结（楚门框架）：

1. **事实**：客观信息——说了什么、数据、事件、人名（只列原文有的事实，不推断）
2. **规律**：共性/模式——从事实中归纳的可复用规律、方法、步骤
3. **洞察**：底层认知——真正本质是什么、与业务/知识库有什么关系、能学会什么（偏主观但要有依据）

要求：
- 事实/规律/洞察各 3-5 条，每条一行，简洁
- 事实必须可溯源（与原文一致），禁止编造
- 洞察要有"为什么"和"对我们有什么用"
- 输出格式：三个小节，每节用 - 列表

逐字稿内容：
{transcript}"""


def get_api_key() -> str:
    # 从 Hermes profile env 或环境变量读
    for p in [Path.home() / ".hermes" / "profiles" / "laowantong" / "config.yaml",
              Path.home() / "AppData" / "Local" / "hermes" / "profiles" / "laowantong" / "config.yaml"]:
        if p.exists():
            try:
                import yaml
                cfg = yaml.safe_load(p.read_text(encoding="utf-8"))
                ak = cfg.get("model", {}).get("api_key", "")
                if ak and "${" not in str(ak):
                    return str(ak).strip()
            except Exception:
                pass
    return os.environ.get("DEEPSEEK_API_KEY", "")


def llm_summarize(transcript: str, api_key: str) -> str:
    """调用 DeepSeek 三层次总结。"""
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "你是严谨的知识萃取专家，只依据给定文本总结，不编造。"},
            {"role": "user", "content": TRIPLE_FRAMEWORK_PROMPT.format(transcript=transcript[:20000])},
        ],
        "temperature": 0.3,
        "max_tokens": 1500,
    }
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"  ⚠️ LLM 调用失败: {e}")
        return ""


def knowledge_ize(transcript_md: Path, output_path: Path | None = None) -> bool:
    """逐字稿 → 研究文档（三层次 + 五段模板）。"""
    if not transcript_md.exists():
        print(f"❌ 逐字稿不存在: {transcript_md}")
        return False

    transcript = transcript_md.read_text(encoding="utf-8")
    # 友好标题：tt_ → 头条视频、article_ → 文章；hash 段太丑，尝试从逐字稿内容提取第一句做标题
    stem = transcript_md.stem.replace("src_wechat_", "")
    src_kind = "wechat-video"
    if stem.startswith("tt_"):
        src_kind = "toutiao-video"
    elif stem.startswith("article_tt_"):
        src_kind = "toutiao-article"
    elif stem.startswith("article_"):
        src_kind = "wechat-article"
    title = stem
    # 从逐字稿/文章正文提取真实标题：
    #   1) 优先取 markdown 一级标题（文章通常 # 真标题；视频的 # 逐字稿太泛，跳过）
    #   2) 文章取第一个 # 标题
    #   3) 视频取第一个 [MM:SS] 时间戳行的口播内容
    md_title = ""
    for line in transcript.splitlines():
        s = line.strip()
        if s.startswith("# ") and "逐字稿" not in s[:20]:
            md_title = s.lstrip("# ").strip()
            break
    if md_title:
        title = md_title[:50]
    else:
        for line in transcript.splitlines():
            s = line.strip()
            m = re.match(r"^\[\d+:\d+\]\s*(.+)$", s)
            if m:
                title = m.group(1).strip()[:50]
                break

    api_key = get_api_key()
    if not api_key:
        print("⚠️ 未找到 DeepSeek API key——跳过 LLM 总结，只生成骨架")
        summary = "<!-- TODO: 配置 DEEPSEEK_API_KEY 后运行 wechat_knowledge.py 生成三层次总结 -->"
    else:
        print(f"🧠 LLM 三层次总结中（{MODEL}）...")
        summary = llm_summarize(transcript, api_key)
        if not summary:
            print("⚠️ LLM 总结失败——只生成骨架")
            summary = "<!-- LLM 总结失败，请重试 -->"

    if output_path is None:
        OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
        output_path = OUTPUTS_DIR / f"case-wechat-{transcript_md.stem.replace('src_wechat_', '')}.md"

    # 已有产出且非骨架 → 跳过（防 --all 重复调用浪费 LLM）
    if output_path.exists() and "<!--" not in output_path.read_text(encoding="utf-8"):
        print(f"⏭️  已知识化，跳过: {output_path.name}")
        return True
    # LLM 失败且已有产出文件 → 保留旧文件不覆盖（防 --all 重跑把好 case 降级成骨架）
    if ("<!--" in summary and output_path.exists()):
        print(f"⚠️ LLM 总结失败且已有旧文件——保留: {output_path}")
        return True

    note = f"""---
title: "{title}"
type: case
status: draft
domain: {src_kind}
source_refs:
- 00_inbox/wechat-collect/{transcript_md.name}
created_at: {date.today().isoformat()}
---

# {title}

> 偶遇采集内容知识化 · 楚门三层次框架

## 事实（客观信息）

{summary}

## 规律（可复用模式）

<!-- 见上方 LLM 总结 -->

## 洞察（底层认知）

<!-- 见上方 LLM 总结 -->

## ✅ 可行动建议

<!-- TODO: 行动项 -->

## 📜 原文链接

<details>
<summary>逐字稿（{transcript_md.name}）</summary>

见 `00_inbox/wechat-collect/{transcript_md.name}`

</details>
"""
    output_path.write_text(note, encoding="utf-8")
    print(f"✅ 研究文档已生成: {output_path}")
    return True


def main():
    ap = argparse.ArgumentParser(description="视频号逐字稿 → 知识化（三层次总结）")
    ap.add_argument("transcript", nargs="?", help="逐字稿路径")
    ap.add_argument("--all", action="store_true", help="处理所有未知识化的 src_wechat_*")
    ap.add_argument("--output", help="输出路径（默认 00_inbox/wechat-collect/knowledge/）")
    args = ap.parse_args()

    if args.all:
        done = 0
        for f in sorted(INBOX_DIR.glob("src_wechat_*.md")):
            if knowledge_ize(f):
                done += 1
        print(f"完成 {done} 个")
        return

    if args.transcript:
        knowledge_ize(Path(args.transcript), Path(args.output) if args.output else None)
        return

    ap.print_help()


if __name__ == "__main__":
    main()
