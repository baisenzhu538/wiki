#!/usr/bin/env python3
"""
VLM 描述质量扫描器
扫描指定目录下的 _vlm_desc.md 文件，检测：
- _parse_error 标记
- 低置信度（≤0.3）
- "未识别"类型
- 外层置信度与内层 JSON 不一致（P-33 模式）

用法：
    python 90_control/scripts/scan-vlm-parse-errors.py                           # 扫默认目录
    python 90_control/scripts/scan-vlm-parse-errors.py --dir 00_inbox/调研专题    # 指定目录
    python 90_control/scripts/scan-vlm-parse-errors.py --json                    # JSON 输出
"""

import argparse
import json
import re
import sys
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_SCAN_DIR = VAULT_ROOT / "00_inbox" / "调研专题"

# 需要人工复核的信号
FLAG_PATTERNS = {
    "parse_error": re.compile(r"_parse_error['\"]?\s*[:=]\s*true", re.IGNORECASE),
    "low_confidence": re.compile(r"置信度[：:]\s*0\.[0-3]\d*"),
    "unrecognized_type": re.compile(r"类型[：:]\s*未识别"),
}


def extract_confidence_from_json_block(text):
    """从 markdown 中的 JSON 代码块提取内层置信度"""
    json_blocks = re.findall(r"```(?:json)?\s*\n(.*?)\n```", text, re.DOTALL)
    inner_confidences = []
    for block in json_blocks:
        try:
            data = json.loads(block)
            if isinstance(data, dict):
                conf = data.get("confidence") or data.get("置信度")
                if conf is not None:
                    try:
                        inner_confidences.append(float(conf))
                    except (ValueError, TypeError):
                        pass
        except json.JSONDecodeError:
            pass
    return inner_confidences


def scan_file(file_path, vault_root):
    """扫描单个 VLM 描述文件"""
    rel = file_path.relative_to(vault_root).as_posix()
    try:
        text = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return {"file": rel, "error": f"read error: {e}"}

    flags = []

    # 检查 _parse_error
    if FLAG_PATTERNS["parse_error"].search(text):
        flags.append("parse_error")

    # 检查外层置信度
    outer_conf_match = re.search(r"\*\*置信度\*\*[：:]\s*([\d.]+)", text)
    outer_confidence = float(outer_conf_match.group(1)) if outer_conf_match else None

    if outer_confidence is not None and outer_confidence <= 0.3:
        flags.append(f"low_outer_confidence({outer_confidence})")

    # 检查类型未识别
    if FLAG_PATTERNS["unrecognized_type"].search(text):
        flags.append("unrecognized_type")

    # P-33 模式：外层置信度低但内层 JSON 有高置信度
    inner_confs = extract_confidence_from_json_block(text)
    has_confidence_mismatch = False
    if (outer_confidence is not None and outer_confidence <= 0.3
            and any(c >= 0.9 for c in inner_confs)):
        flags.append("confidence_mismatch(outer_low_inner_high)")
        has_confidence_mismatch = True

    result = {
        "file": rel,
        "image": file_path.stem.replace("_vlm_desc", ""),
        "flags": flags,
        "outer_confidence": outer_confidence,
        "inner_confidences": inner_confs,
        "needs_review": len(flags) > 0,
    }

    return result


def scan_directory(scan_dir, vault_root):
    """扫描目录下所有 _vlm_desc.md 文件"""
    if not scan_dir.exists():
        return []
    files = sorted(scan_dir.rglob("*_vlm_desc.md"))
    return [scan_file(fp, vault_root) for fp in files]


def generate_report(results, scan_dir):
    """生成 Markdown 报告"""
    total = len(results)
    needs_review = [r for r in results if r.get("needs_review")]
    clean = total - len(needs_review)

    lines = [
        "# VLM 描述质量扫描报告",
        "",
        f"**扫描目录**：`{scan_dir.as_posix()}`",
        f"**扫描文件**：{total} 个 VLM 描述文件",
        f"**✅ 正常**：{clean} 个",
        f"**⚠️ 需复核**：{len(needs_review)} 个",
        "",
        "---",
        "",
    ]

    if needs_review:
        lines.append("## ⚠️ 需人工复核")
        lines.append("")
        lines.append("| 图片 | 问题 | 外层置信度 | JSON 内置信度 |")
        lines.append("|---|---|---|---|")
        for r in needs_review:
            flags_str = "; ".join(r.get("flags", []))
            outer = r.get("outer_confidence", "?")
            inner = ", ".join(str(c) for c in r.get("inner_confidences", [])) or "-"
            lines.append(f"| `{r['image']}` | {flags_str} | {outer} | {inner} |")
        lines.append("")
    else:
        lines.append("✅ 所有 VLM 描述文件正常，无需复核。")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## 复核指南",
        "",
        "1. **parse_error**：JSON 解析失败（通常是内嵌引号未转义，见 P-33）。读原始 VLM 输出，确认内容完整性。",
        "2. **low_outer_confidence**：外层标记置信度 ≤0.3。检查内层 JSON 的 confidence 字段——如果内层高外层低，是 P-33 的已知 bug（JSON 解析失败 fallback）。",
        '3. **unrecognized_type**：类型被标为"未识别"。人工确认图片属于哪个类别（框架图/手段卡/概念图等）。',
        '4. **confidence_mismatch**：P-33 标准模式——外层 0.3 但内层 JSON ≥0.9。通常是脚本解析失败而非模型看不懂。修复方式：重跑 VLM 描述或手动修正外层标记。',
        "",
        f"*生成：scan-vlm-parse-errors.py · {Path(__file__).name}*",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="VLM 描述质量扫描器")
    parser.add_argument("--dir", default=str(DEFAULT_SCAN_DIR), help="扫描目录（默认 00_inbox/调研专题）")
    parser.add_argument("--json", action="store_true", help="JSON 输出")
    args = parser.parse_args()

    scan_dir = Path(args.dir)
    if not scan_dir.is_absolute():
        scan_dir = VAULT_ROOT / scan_dir

    results = scan_directory(scan_dir, VAULT_ROOT)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        report = generate_report(results, scan_dir)
        print(report)

    needs_review = sum(1 for r in results if r.get("needs_review"))
    if needs_review > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
