#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AI组织行为学的口述.pdf → 干净逐字稿（双源：原生文本层基线 + MiniMax-M3 严格逐字 VLM）
洪七公 2026-09-06 直派单。只转录不改写；VLM 原始输出落 _processed 备查。"""
import os, json, base64, time, urllib.request
import fitz
from pathlib import Path

PDF = Path(r"00_inbox/人机协作双三角/AI组织行为学的口述.pdf")
PAGE_DIR = Path(r"00_inbox/人机协作双三角/_processed/_pdf_pages")
OUT_DIR = Path(r"00_inbox/人机协作双三角/_processed")
MODEL = "MiniMax-M3"
KEY = os.environ["MINIMAX_API_KEY"]
os.environ.setdefault("NO_PROXY", "api.minimaxi.com")

# ---------- 1. 原生文本层 → 段落重建（ZWSP=段落尾标记，strip 其他 ZWSP） ----------
def textlayer_paragraphs():
    doc = fitz.open(str(PDF))
    pages = []
    for page in doc:
        raw = page.get_text()
        lines = []
        buf = []
        for ln in raw.splitlines():
            z = ln.count("​")
            clean = ln.replace("​", "").strip()
            if not clean:
                continue
            buf.append(clean)
            if z:  # 段落结束
                lines.append("".join(buf))
                buf = []
        if buf:
            lines.append("".join(buf))
        pages.append(lines)
    doc.close()
    return pages

# ---------- 2. 严格逐字 VLM ----------
SYSTEM = """你是逐字转录机。任务：把图片里的全部文字一字不差转录出来。

铁律：
1. 不增不删不改——原文是口述，可能有口语重复、语气词、病句，全部原样保留，禁止润色、禁止纠正、禁止总结。
2. 按原文的自然段落分行，一段一行，不要合并或拆分段落。
3. 看不清/不确定的字，用 [?] 原位标注，禁止猜测补全。
4. 只输出转录文本本身，不要任何说明、标题、标注、格式符号。"""

def call_vlm(img_path):
    b64 = base64.b64encode(img_path.read_bytes()).decode()
    body = json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": [
                {"type": "text", "text": "逐字转录这张页面图片的全部文字。"},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
            ]},
        ],
        "temperature": 0.1,
    }).encode()
    req = urllib.request.Request(
        "https://api.minimaxi.com/v1/text/chatcompletion_v2",
        data=body,
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=300) as r:
        result = json.loads(r.read())
    return result["choices"][0]["message"]["content"]

def main():
    tl = textlayer_paragraphs()
    print("文本层段落重建：", [len(p) for p in tl], "段/页")

    vlm_pages = []
    for i in range(1, 4):
        img = PAGE_DIR / f"AI组织行为学的口述_page{i:03d}.png"
        print(f"VLM page {i} ...", flush=True)
        try:
            txt = call_vlm(img)
        except Exception as e:
            print(f"  FAIL: {e}", flush=True)
            txt = f"[VLM_ERROR] {e}"
        vlm_pages.append(txt)
        out = OUT_DIR / f"AI组织行为学的口述_page{i:03d}_verbatim_vlm.md"
        out.write_text(f"# page{i} 严格逐字 VLM（{MODEL}）\n\n{txt}\n", encoding="utf-8")
        print(f"  saved {out.name} ({len(txt)} chars)", flush=True)
        time.sleep(1)

    # 基线也落盘备查
    baselines = []
    for i, paras in enumerate(tl, 1):
        baselines.append(f"=== PAGE {i} ===\n" + "\n".join(paras))
    (OUT_DIR / "AI组织行为学的口述_textlayer_baseline.md").write_text(
        "\n\n".join(baselines), encoding="utf-8")
    print("文本层基线已落盘")

if __name__ == "__main__":
    main()
