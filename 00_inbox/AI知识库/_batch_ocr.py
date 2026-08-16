#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""爆炸式调研 批量 OCR+VLM（Windows 版，cap_hub.vlm / MiniMax-M3）
- 长图切 600px 段（30px 重叠防切行），<=800px 直跑（黄金标准：600px 100% 成功+token 最优）
- 产出 OCR_{文件名}.md 落素材目录（产出铁律：原料直出，Obsidian 可见）
- 断点续跑：已有 OCR_*.md 的图跳过
- 完全相同的两张重复图只识别一次
"""
import io, os, sys, time
from PIL import Image

sys.path.insert(0, r"C:\Users\Administrator\Desktop\wiki")
from cap_hub.vlm import process as vlm_process

SRC = os.path.dirname(os.path.abspath(__file__))
CHUNK_H = 600
OVERLAP = 30
DIRECT_THRESHOLD = 800

# 完全相同的重复文件（md5 一致）→ 只识别第一份
SKIP_DUP = {}  # 本目录无 md5 重复

# 课程上下文（来自口述稿+笔记的先验理解）——防编造纪律：仅作术语参照，禁止补全图中没有的内容
CONTEXT = """【背景】一堂"AI知识管理探索营"课程截图（讲师楚门/Truman）。主题：AI 时代知识管理——知识复利火箭模型（超长周期/数量/质量/自动化/协作化/可掌控）、五次知识管理飞跃（2013 电子化/2017 知识体系/2025 Obsidian+AI/2026 团队多Agent/2026 体系自动化）、Obsidian 多 Agent 协作链、事实层→规律层→洞察层。图中可能出现的术语：Obsidian、Markdown、双链、Antigravity、Trae、Claude、YAI、Opend(OpenClaw)、Truman、Stella、Skill 封装、DataPack、上下文模式、顶层文档、Session 依赖、读写关系、多 Agent、120万字笔记、双三角、五步法、KDO。
【要求】
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
    top = 0
    i = 0
    while top < h:
        bot = min(top + CHUNK_H, h)
        chunks.append((im.crop((0, top, w, bot)), f"段{i+1}"))
        if bot >= h:
            break
        top = bot - OVERLAP
        i += 1
    return chunks


def call_vlm(pil_img, label, retries=2):
    buf = io.BytesIO()
    pil_img.save(buf, format="PNG")
    tmp = os.path.join(SRC, "_chunk_tmp.png")
    with open(tmp, "wb") as f:
        f.write(buf.getvalue())
    prompt = CONTEXT + f"\n【图片标识】{label}"
    for attempt in range(retries + 1):
        try:
            r = vlm_process(tmp, prompt=prompt, save=False)
            txt = r["content"]
            ok = "无法查看" not in txt and len(txt.strip()) > 30
            if ok:
                return txt, True
        except Exception as e:
            txt = f"[ERROR] {e}"
        time.sleep(2)
    return txt, False


def main():
    pngs = sorted(f for f in os.listdir(SRC) if f.lower().endswith(".png") and not f.startswith("_chunk"))
    todo = []
    for fn in pngs:
        out_md = os.path.join(SRC, f"OCR_{os.path.splitext(fn)[0]}.md")
        if not os.path.exists(out_md):
            todo.append(fn)
    print(f"共 {len(pngs)} 张，已完成 {len(pngs)-len(todo)}，待处理 {len(todo)}", flush=True)

    stats = {"chunks": 0, "ok": 0, "fail": 0}
    for fi, fn in enumerate(todo):
        out_md = os.path.join(SRC, f"OCR_{os.path.splitext(fn)[0]}.md")
        if fn in SKIP_DUP:
            with open(out_md, "w", encoding="utf-8") as f:
                f.write(f"# {fn}\n\n> ⚠️ 与 `{SKIP_DUP[fn]}` 完全相同（md5 一致），识别结果见对应 OCR 文件。\n")
            print(f"[{fi+1}/{len(todo)}] {fn} → 重复，跳过", flush=True)
            continue

        path = os.path.join(SRC, fn)
        chunks = slice_image(path)
        w, h = Image.open(path).size
        print(f"[{fi+1}/{len(todo)}] {fn} ({w}x{h}) → {len(chunks)} 段", flush=True)

        with open(out_md, "w", encoding="utf-8") as f:
            f.write(f"# OCR+VLM 识别：{fn}\n\n> {w}×{h} | {len(chunks)} 段 | MiniMax-M3 | 课程上下文注入\n\n")
            for ci, (cimg, clabel) in enumerate(chunks):
                label = f"{fn} {clabel}/{len(chunks)}"
                txt, ok = call_vlm(cimg, label)
                stats["chunks"] += 1
                stats["ok" if ok else "fail"] += 1
                print(f"  {clabel}: {'OK' if ok else 'FAIL'}", flush=True)
                f.write(f"## {clabel} {'✅' if ok else '❌'}\n\n{txt}\n\n---\n\n")
                f.flush()
                time.sleep(0.3)

    tmp = os.path.join(SRC, "_chunk_tmp.png")
    if os.path.exists(tmp):
        os.remove(tmp)
    print(f"\n完成：{stats['ok']}/{stats['chunks']} 段成功，失败 {stats['fail']}", flush=True)


if __name__ == "__main__":
    main()
