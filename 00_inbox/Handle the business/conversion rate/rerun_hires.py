import sys, fitz, base64, io
from pathlib import Path
from PIL import Image
from anthropic import Anthropic

env = Path(r"C:\Users\Administrator\Desktop\wiki\.env"); ak = None
for line in open(env, encoding="utf-8"):
    if line.startswith("MINIMAX_API_KEY="):
        ak = line.split("=", 1)[1].strip(); break
client = Anthropic(api_key=ak, base_url="https://api.minimaxi.com/anthropic")

jobs = [("《阻力消除策略小抄合集 · 持续更新版》.pdf", [0, 1]),
        ("转化率黑客5：组合落地篇.pdf", [4])]
PROMPT = """你是专业 OCR 专家。这是「一堂转化率黑客」课程小抄/图表，极其重要。请完整精确识别图中所有文字，表格还原成 Markdown 表格（单元格换行用<br>）。品牌名用"一堂"。策略深度三列是"动嘴/动手/动钱"。12种阻力权威名：觉得贵/没能力/没时间/门槛高/距离远/不靠谱/有风险/折面子/不专业/体验差/怕冲动/还不急。爬山地图六段：L1不想提升/L2有追求/L3全局分析/L4手段专业/L5迭代领先/L6广泛迁移。严禁编造，只识别图中实际内容。输出：
## 原文识别（含表格）
## 核心主题
## 关键概念"""

for pdf, pages in jobs:
    stem = Path(pdf).stem
    doc = fitz.open(pdf)
    for pi in pages:
        pix = doc[pi].get_pixmap(dpi=300)
        img = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")
        w, h = img.size
        if max(w, h) > 2400:
            r = 2400 / max(w, h); img = img.resize((int(w*r), int(h*r)), Image.Resampling.LANCZOS)
        buf = io.BytesIO(); img.save(buf, format="JPEG", quality=92)
        b64 = base64.b64encode(buf.getvalue()).decode()
        try:
            resp = client.messages.create(model="MiniMax-M3", max_tokens=4096,
                messages=[{"role": "user", "content": [
                    {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": b64}},
                    {"type": "text", "text": PROMPT}]}])
            out = Path("_vlm_output/pdf")/stem/f"{stem}__p{pi+1:03d}_vlm.md"
            out.write_text(f"# VLM 识别结果：PDF:{stem}/p{pi+1:03d}（300DPI高分辨率重跑）\n\n> 来源文件：{pdf} 第{pi+1}页\n\n" + resp.content[0].text, encoding="utf-8")
            print(f"OK 重跑 {stem} p{pi+1:03d} (300DPI, 渲染{w}x{h})", flush=True)
        except Exception as e:
            print(f"FAIL {stem} p{pi+1:03d}: {e}", flush=True)
    doc.close()
print("DONE", flush=True)
