#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""长图批量 OCR+VLM（Windows 版）——long-image-ocr skill 的 Windows 实现。

用法：
  python 40_outputs/code/scripts/batch-ocr-long-image-windows.py <素材目录> [--context-file 术语上下文.md]

- 长图切 600px 段（30px 重叠防切行），<=800px 直跑（黄金标准：600px 100% 成功+token 最优）
- 引擎：cap_hub.vlm（MiniMax-M3，密钥走 wiki/.env → cap_hub/config.py，零配置）
- 产出：每张图 OCR_{文件名}.md 直落素材目录（产出铁律：Obsidian 可见，不用 /tmp）
- 断点续跑：已有 OCR_*.md 的图跳过（注意：prompt 变更后需先作废旧版输出再续跑）
- --context-file：课程/主题术语上下文（纯文本），注入 prompt 防误读；
  自动附带 E025 禁令（词表仅供辨词，禁止替换图中标题/标注原文）

实战样本：00_inbox/爆炸式调研/（47 图 173 段零失败）、00_inbox/AI知识库/（25 图 42 段零失败）
WSL/Hermes 版见：~/.hermes/profiles/beikai/skills/creative/long-image-ocr/
"""
import argparse
import io
import os
import sys
import time

from PIL import Image

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
from cap_hub.vlm import process as vlm_process

CHUNK_H = 600
OVERLAP = 30
DIRECT_THRESHOLD = 800

BASE_PROMPT = """【要求】
1. 逐字转录图中全部文字（含标题、正文、表格、批注、小字），保持原有结构和顺序，用 Markdown 还原（标题/列表/表格）。
2. 只写图中真实存在的内容；背景词表仅供辨认词语，禁止用它替换图中标题/标注原文；看不清就标注[无法辨认]。
3. 若是聊天截图/文档截图/网页截图，注明界面类型。
4. 不要总结、不要分析、不要建议——只要原始识别文本。"""


def slice_image(path):
    im = Image.open(path).convert("RGB")
    w, h = im.size
    if h <= DIRECT_THRESHOLD:
        return [(im, "全图")]
    chunks = []
    top, i = 0, 0
    while top < h:
        bot = min(top + CHUNK_H, h)
        chunks.append((im.crop((0, top, w, bot)), f"段{i+1}"))
        if bot >= h:
            break
        top = bot - OVERLAP
        i += 1
    return chunks


def call_vlm(pil_img, label, prompt, tmp_path, retries=2):
    buf = io.BytesIO()
    pil_img.save(buf, format="PNG")
    with open(tmp_path, "wb") as f:
        f.write(buf.getvalue())
    full = prompt + f"\n【图片标识】{label}"
    txt = ""
    for _ in range(retries + 1):
        try:
            r = vlm_process(tmp_path, prompt=full, save=False)
            txt = r["content"]
            if "无法查看" not in txt and len(txt.strip()) > 30:
                return txt, True
        except Exception as e:
            txt = f"[ERROR] {e}"
        time.sleep(2)
    return txt, False


def main():
    ap = argparse.ArgumentParser(description="长图批量 OCR+VLM（Windows 版）")
    ap.add_argument("src_dir", help="素材目录（输出也落在这里）")
    ap.add_argument("--context-file", help="术语上下文文本文件（可选）")
    args = ap.parse_args()
    src = os.path.abspath(args.src_dir)

    prompt = BASE_PROMPT
    if args.context_file:
        ctx = open(args.context_file, encoding="utf-8").read().strip()
        prompt = f"【背景】{ctx}\n" + BASE_PROMPT

    pngs = sorted(f for f in os.listdir(src)
                  if f.lower().endswith((".png", ".jpg", ".jpeg")) and not f.startswith("_chunk"))
    todo = [f for f in pngs if not os.path.exists(os.path.join(src, f"OCR_{os.path.splitext(f)[0]}.md"))]
    print(f"共 {len(pngs)} 张，已完成 {len(pngs)-len(todo)}，待处理 {len(todo)}", flush=True)

    tmp_path = os.path.join(src, "_chunk_tmp.png")
    stats = {"chunks": 0, "ok": 0, "fail": 0}
    for fi, fn in enumerate(todo):
        path = os.path.join(src, fn)
        chunks = slice_image(path)
        w, h = Image.open(path).size
        print(f"[{fi+1}/{len(todo)}] {fn} ({w}x{h}) → {len(chunks)} 段", flush=True)
        out_md = os.path.join(src, f"OCR_{os.path.splitext(fn)[0]}.md")
        with open(out_md, "w", encoding="utf-8") as f:
            f.write(f"# OCR+VLM 识别：{fn}\n\n> {w}×{h} | {len(chunks)} 段 | MiniMax-M3\n\n")
            for ci, (cimg, clabel) in enumerate(chunks):
                txt, ok = call_vlm(cimg, f"{fn} {clabel}/{len(chunks)}", prompt, tmp_path)
                stats["chunks"] += 1
                stats["ok" if ok else "fail"] += 1
                print(f"  {clabel}: {'OK' if ok else 'FAIL'}", flush=True)
                f.write(f"## {clabel} {'✅' if ok else '❌'}\n\n{txt}\n\n---\n\n")
                f.flush()
                time.sleep(0.3)

    if os.path.exists(tmp_path):
        os.remove(tmp_path)
    print(f"\n完成：{stats['ok']}/{stats['chunks']} 段成功，失败 {stats['fail']}", flush=True)


if __name__ == "__main__":
    main()
