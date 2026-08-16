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
SKIP_DUP = {
    "一堂DOC-20260816002729.png": "一堂DOC-20260816002727.png",
    "一堂DOC-20260816002757.png": "一堂DOC-20260816002751.png",
}

# 课程上下文（来自口述稿+笔记的先验理解）——防编造纪律：仅作术语参照，禁止补全图中没有的内容
CONTEXT = """【背景】这是一堂 Live259《爆炸式调研》课程截图（讲师 Truman）。课程主线：调研雷达图四维度（深=挖掘式/破案式、高=系统式/OSCAR 模型、宽=爆炸式、动态=自动式）；爆炸式调研=短时间海量收集（500-4000 个案例）+开一篇文档+合并同类项建模，直到规律稳定；案例：外卖 1000 家店筛选、4000 公众号标题提炼十大策略、Coze(扣子) 入门拆解笔记+段位图、VibeCoding 四级编程、OpenClaw(龙虾) 进阶体系、NanoBanana 文生图六七类玩法、Sora2 视频七八类范式、AI 短片 Top10 排行榜、Leo 润滑油经销商咨询（约 60 家三轮调研）。
图中可能出现的术语：OSCAR 模型、合并同类项、饱和覆盖/饱和式救援（流浪地球）、全策略集、十大策略、magic word、逻辑反差、段位图(L1-L6)、DataPack 数据包、讲香、十层解读、双三角、五步法（目标→范围→搜索⇄建模→交付）、单元模型、九字诀（定目标/控节奏/做纠偏）、14 策略超级小抄、灵感闪现、借假修真、分层自洽、拆推评算、红帽思考、WhyAI、YAI Partner（T/C/P/R 四型）、R 型研究型 Partner 五状态机、爆炸式研究建模资产报告、OPC 一人公司、串货、经销商生存状况图（横轴产品结构×纵轴网点覆盖，红黄绿三色）、即梦、可灵、Top10 排行榜、存成笔记。
【要求】
1. 逐字转录图中全部文字（含标题、正文、表格、批注、小字），保持原有结构和顺序，用 Markdown 还原（标题/列表/表格）。
2. 只写图中真实存在的内容，严禁凭课程背景补全或推测看不清的文字；看不清就标注[无法辨认]。
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
