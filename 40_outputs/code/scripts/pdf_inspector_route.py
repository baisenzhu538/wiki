# pdf-inspector classify-then-route 进料脚本（KDO PDF 进料默认快速通道）
# 用法：
#   python pdf_inspector_route.py <pdf路径>            # 分类 + 文本型输出 markdown 到同目录 <名>.md
#   python pdf_inspector_route.py <pdf路径> --stdout   # 只输出分类结论 + markdown 到 stdout
#   python pdf_inspector_route.py <pdf路径> --json     # JSON 输出（detect 字段 + markdown）
#   python pdf_inspector_route.py <dir>                # 批量处理目录下所有 *.pdf
# 路由语义：text_based → 本地直提（0 OCR 成本）；scanned/image_based → 提示走 MinerU/OCR；
#          mixed → 本地直提 + pages_needing_ocr 标出页送 OCR。
import sys, os, subprocess, glob, json, argparse

# pdf-inspector 装在独立受管 venv；任意 python 调起本脚本时自动用 venv 重新执行（self-reinvoke）
VENV_PY = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "..", "..", "..", "_tmp", "pdf-inspector", "Scripts", "python.exe")

try:
    import pdf_inspector
except ImportError:
    venv_py = os.path.normpath(VENV_PY)
    if os.path.exists(venv_py):
        sys.exit(subprocess.call([venv_py, __file__] + sys.argv[1:]))
    sys.exit("错误: pdf_inspector 未安装，且受管 venv 不存在（预期位置: %s）" % venv_py)

def route_one(pdf_path, out_dir=None):
    r = pdf_inspector.process_pdf(pdf_path)
    pdf_type = r.pdf_type
    pages_ocr = list(getattr(r, "pages_needing_ocr", []) or [])
    md = r.markdown or ""
    result = {
        "file": os.path.basename(pdf_path),
        "pdf_type": pdf_type,
        "confidence": getattr(r, "confidence", None),
        "pages_needing_ocr": pages_ocr,
        "markdown_len": len(md),
        "route": (
            "local-extract" if (pdf_type == "text_based" and not pages_ocr)
            else "local+mixed-ocr" if (pdf_type in ("text_based", "mixed") and pages_ocr)
            else "mineru-ocr"
        ),
    }
    if pdf_type == "text_based" and md:
        if out_dir:
            md_path = os.path.join(out_dir, os.path.splitext(os.path.basename(pdf_path))[0] + ".md")
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(md)
            result["markdown_path"] = md_path
        else:
            # 默认不把全文塞进 JSON（会爆输出）；要全文用 --stdout
            result["markdown"] = md[:200] + ("…" if len(md) > 200 else "")
    return result

def main():
    parser = argparse.ArgumentParser(description="pdf-inspector classify-then-route 进料")
    parser.add_argument("target", help="PDF 文件或目录（目录=批量）")
    parser.add_argument("--json", action="store_true", help="JSON 输出")
    parser.add_argument("--stdout", action="store_true", help="文本型 markdown 输出到 stdout")
    parser.add_argument("--out", help="markdown 输出目录（默认同源目录）")
    args = parser.parse_args()

    if os.path.isdir(args.target):
        files = sorted(glob.glob(os.path.join(args.target, "*.pdf")))
        if not files:
            sys.exit("目录下无 PDF 文件: %s" % args.target)
        results = [route_one(f, args.out) for f in files]
        text_based = sum(1 for r in results if r["route"] == "local-extract")
        if args.json:
            print(json.dumps({"total": len(results), "text_based": text_based, "results": results},
                             ensure_ascii=False, indent=1))
        else:
            for r in results:
                print(f"{r['file']}: {r['pdf_type']} → {r['route']}"
                      + (f" (markdown {r['markdown_len']} 字符)" if r['markdown_len'] else ""))
            print(f"共 {len(results)} 份，文本型直提 {text_based} 份")
        return

    result = route_one(args.target, args.out)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=1))
    elif args.stdout and result.get("markdown"):
        print(result["markdown"])
    else:
        route_hint = {
            "local-extract": "本地直提完成（0 OCR 成本）",
            "local+mixed-ocr": f"本地直提 + 第 {result['pages_needing_ocr']} 页需送 OCR",
            "mineru-ocr": "扫描/图片型 → 送 MinerU / magic-pdf 处理",
        }[result["route"]]
        print(f"{result['file']}: {result['pdf_type']} (conf {result['confidence']}) → {route_hint}")
        if result.get("markdown_path"):
            print(f"markdown 已写入: {result['markdown_path']} ({result['markdown_len']} 字符)")

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
