import os
import base64
import io
import sys
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from anthropic import Anthropic
from PIL import Image

# ============ 配置 ============
INPUT_DIR = Path(r"C:\Users\Administrator\Desktop\wiki\00_inbox\Handle the business\conversion rate")
OUTPUT_DIR = INPUT_DIR / "_vlm_output"
TMP_PDF_DIR = INPUT_DIR / "_vlm_tmp_pdf"   # PDF 渲染临时目录
IMG_OUT = OUTPUT_DIR / "images"            # 顶层图片
SUB_OUT = OUTPUT_DIR / "晓莉案例"          # 子文件夹图片
PDF_OUT = OUTPUT_DIR / "pdf"               # PDF 逐页
for d in (OUTPUT_DIR, TMP_PDF_DIR, IMG_OUT, SUB_OUT, PDF_OUT):
    d.mkdir(parents=True, exist_ok=True)

SUBFOLDER_NAME = "晓莉案例-转化率黑客"
MAX_WORKERS = 4
PDF_DPI = 150

# 高重要度关键词：更高分辨率
HIGH_PRIORITY_KEYWORDS = [
    "极其重要", "小抄", "冰山", "36计", "六步法", "组合6步法", "爬山地图",
    "动力三曲线", "触点质量", "FAB", "五维模型", "易浪费触点", "待破解阻力",
]

env_path = Path(r"C:\Users\Administrator\Desktop\wiki\.env")
api_key = None
with open(env_path, encoding="utf-8") as f:
    for line in f:
        if line.startswith("MINIMAX_API_KEY="):
            api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
            break
if not api_key:
    raise ValueError("MINIMAX_API_KEY not found in .env")

client = Anthropic(api_key=api_key, base_url="https://api.minimaxi.com/anthropic")

PROMPT = """你是一位专业的 OCR + 商业内容理解专家。这份素材是「一堂转化率黑客」课程的核心内容，极其重要，必须精确识别。

请对这张图片进行以下处理：

1. **完整 OCR（精确优先）**：尽可能准确地识别图片中的所有文字，保持原文的段落和结构。特别注意：
   - 表格类图片必须还原成 Markdown 表格，单元格内换行用 <br>
   - 框架图/流程图/冰山图/曲线图必须保留层级与坐标关系
   - 品牌名用"一堂"，不要写成"一莹/一望/一棠"
   - 英文用"Yitang"，不要写成"Yitanq"
   - 数学公式、业务公式、转化率公式、变量符号必须逐字准确
   - 专有名词、案例名、数据、百分比必须准确，不能编造
   - 动力/阻力/触点等专业术语保持原文，不要替换
2. **内容理解**：说明这张图片的核心主题或核心观点（2-3 句话）。
3. **结构化输出**：用 Markdown 还原图片的完整结构（标题、层级、表格、公式、清单）。
4. **关键概念提取**：列出图片中的 3-8 个关键概念、公式、术语或策略。
5. **一句话总结**：用一句话总结这张图片最有价值的信息。

【重要准确性要求】：
- 所有内容必须基于图片实际出现的信息，**严禁编造、推断、补充图片里没有的公式、数据、案例或内容**。
- 如果图片里只有一个词或概念而没有完整展开，就不要自行补全。
- 结构化内容和关键概念只能整理图片里已有的信息，不能额外添加。

请用中文输出，格式如下：

## 原文识别
[OCR 原文，含表格/公式/层级]

## 核心主题
[2-3 句话]

## 结构化内容
[Markdown 结构]

## 关键概念
- 

## 一句话总结
[一句话]
"""


def encode_image(image_path: Path, high_priority: bool) -> tuple[str, str]:
    max_size = 2200 if high_priority else 1600
    with Image.open(image_path) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        w, h = img.size
        if max(w, h) > max_size:
            ratio = max_size / max(w, h)
            img = img.resize((int(w * ratio), int(h * ratio)), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=90)
        return base64.b64encode(buf.getvalue()).decode("utf-8"), "image/jpeg"


def call_vlm(image_path: Path, high_priority: bool) -> str:
    b64, media_type = encode_image(image_path, high_priority)
    last_err = None
    for attempt in range(3):
        try:
            response = client.messages.create(
                model="MiniMax-M3",
                max_tokens=4096,
                messages=[{
                    "role": "user",
                    "content": [
                        {"type": "image", "source": {"type": "base64", "media_type": media_type, "data": b64}},
                        {"type": "text", "text": PROMPT},
                    ],
                }],
            )
            return response.content[0].text
        except Exception as e:
            last_err = e
            time.sleep(3 * (attempt + 1))
    raise last_err


def render_pdfs():
    """把所有 PDF 渲染成 PNG（断点续跑）。"""
    import fitz
    pdfs = sorted(INPUT_DIR.glob("*.pdf"))
    print(f"[PDF] 发现 {len(pdfs)} 个 PDF，开始预渲染...", flush=True)
    total_pages = 0
    for pdf in pdfs:
        stem = pdf.stem
        out_dir = TMP_PDF_DIR / stem
        out_dir.mkdir(parents=True, exist_ok=True)
        doc = fitz.open(pdf)
        n = doc.page_count
        for i in range(n):
            target = out_dir / f"p{i+1:03d}.png"
            if target.exists():
                total_pages += 1
                continue
            page = doc[i]
            pix = page.get_pixmap(dpi=PDF_DPI)
            pix.save(str(target))
            total_pages += 1
        doc.close()
        print(f"[PDF] {stem}: {n} 页已渲染", flush=True)
    print(f"[PDF] 预渲染完成，共 {total_pages} 页", flush=True)


def collect_tasks():
    """收集所有待处理任务：(image_path, output_path, high_priority, display)"""
    tasks = []
    image_exts = {".png", ".jpg", ".jpeg", ".jfif", ".webp", ".bmp", ".gif"}

    # 1) 顶层图片
    for f in sorted(INPUT_DIR.iterdir()):
        if f.is_file() and f.suffix.lower() in image_exts:
            hp = any(k in f.name for k in HIGH_PRIORITY_KEYWORDS)
            tasks.append((f, IMG_OUT / f"{f.stem}_vlm.md", hp, f.name))

    # 2) 子文件夹图片
    sub = INPUT_DIR / SUBFOLDER_NAME
    if sub.exists():
        for f in sorted(sub.iterdir()):
            if f.is_file() and f.suffix.lower() in image_exts:
                hp = any(k in f.name for k in HIGH_PRIORITY_KEYWORDS)
                tasks.append((f, SUB_OUT / f"{f.stem}_vlm.md", hp, f"{SUBFOLDER_NAME}/{f.name}"))

    # 3) PDF 渲染页
    for pdf_dir in sorted(TMP_PDF_DIR.iterdir()):
        if not pdf_dir.is_dir():
            continue
        stem = pdf_dir.name
        pdf_out_dir = PDF_OUT / stem
        pdf_out_dir.mkdir(parents=True, exist_ok=True)
        hp = any(k in stem for k in HIGH_PRIORITY_KEYWORDS)
        for png in sorted(pdf_dir.glob("p*.png")):
            page = png.stem  # p001
            tasks.append((png, pdf_out_dir / f"{stem}__{page}_vlm.md", hp, f"PDF:{stem}/{page}"))

    return tasks


def process_one(task):
    image_path, output_path, hp, display = task
    if output_path.exists():
        return ("skip", display)
    try:
        result = call_vlm(image_path, hp)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(f"# VLM 识别结果：{display}\n\n")
            f.write(f"> 来源文件：{image_path}\n\n")
            f.write(result)
        return ("ok", display)
    except Exception as e:
        return ("fail", f"{display} :: {e}")


def main():
    render_pdfs()
    tasks = collect_tasks()
    print(f"\n[VLM] 待处理任务总数: {len(tasks)}（图片+PDF页）", flush=True)

    ok = skip = fail = 0
    failed = []
    done_count = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(process_one, t): t for t in tasks}
        for fut in as_completed(futures):
            status, info = fut.result()
            done_count += 1
            if status == "ok":
                ok += 1
                print(f"[{done_count}/{len(tasks)}] OK  {info}", flush=True)
            elif status == "skip":
                skip += 1
                print(f"[{done_count}/{len(tasks)}] SKIP {info}", flush=True)
            else:
                fail += 1
                failed.append(info)
                print(f"[{done_count}/{len(tasks)}] FAIL {info}", flush=True)

    print(f"\n=== 完成 ===", flush=True)
    print(f"总数 {len(tasks)} | 成功 {ok} | 跳过 {skip} | 失败 {fail}", flush=True)
    if failed:
        print("失败清单：", flush=True)
        for x in failed:
            print(f"  - {x}", flush=True)


if __name__ == "__main__":
    main()
