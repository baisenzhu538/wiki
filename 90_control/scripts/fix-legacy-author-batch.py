#!/usr/bin/env python3
"""
批量修复 enriched/reviewed/stable/active 状态下 author=legacy 的卡片
按文件名/内容推断真实作者，无法推断的设为 unknown
"""

import re
import yaml
from pathlib import Path
from collections import defaultdict

WIKI_DIR = Path("C:/Users/Administrator/Desktop/wiki/30_wiki")
REPORT_DIR = Path("C:/Users/Administrator/Desktop/wiki/60_feedback/audit")


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text, None
    end_idx = text.find("\n---\n", 4)
    if end_idx == -1:
        return None, text, None
    fm_text = text[4:end_idx]
    try:
        fm = yaml.safe_load(fm_text)
        if not isinstance(fm, dict):
            fm = {}
        return fm, text[end_idx + 5:], fm_text
    except Exception as e:
        return None, text, str(e)


def infer_author(file_path, fm, body):
    """根据文件名、frontmatter、正文推断作者"""
    name = file_path.stem
    title = str(fm.get("title", "") or "").lower()
    
    # 1. 文件名前缀规则
    if name.startswith("yt-"):
        return "老顽童"
    if name.startswith("skill-月白-") or name.startswith("dk-yb"):
        return "月白"
    if name.startswith("skill-纪浩-") or name.startswith("case-纪浩-") or "纪浩" in name:
        return "纪浩"
    if name.startswith("case-半肥猫-") or "半肥猫" in name:
        return "半肥猫"
    if name.startswith("case-truman-") or "truman" in name:
        return "老顽童"
    if name.startswith("dk-c") or name.startswith("dk-f") or name.startswith("dk-p"):
        return "欧阳锋"
    if name.startswith("case-广冷电子-"):
        return "欧阳锋"
    if name.startswith("skill-mece") or name.startswith("skill-一堂-"):
        return "老顽童"
    
    # 2. title 或正文中的作者线索
    if "月白" in title or "月白" in body[:500]:
        return "月白"
    if "纪浩" in title or "纪浩" in body[:500]:
        return "纪浩"
    if "半肥猫" in title or "半肥猫" in body[:500]:
        return "半肥猫"
    if "truman" in title:
        return "老顽童"
    if "黄药师" in body[:1000] or "黄药师" in title:
        return "黄药师"
    if "欧阳锋" in body[:500] and "老顽童" not in body[:500]:
        return "欧阳锋"
    
    # 3. type 和 domain 线索
    card_type = str(fm.get("type", "") or "").lower()
    domain = fm.get("domain") or []
    if isinstance(domain, str):
        domain = [domain]
    domain_str = ",".join(str(d) for d in domain).lower()
    
    if "design" in domain_str:
        return "月白"
    if "ai-collaboration" in domain_str and ("纪浩" in name or "jh" in name):
        return "纪浩"
    if "yitang" in domain_str and card_type in ("concept", "framework", "tool", "case"):
        return "老顽童"
    if "master" in domain_str and card_type == "dark-knowledge":
        return "欧阳锋"
    if "kdo" in domain_str or "agent-infrastructure" in domain_str:
        return "黄药师"
    
    # 4. 无法推断
    return "unknown"


def format_scalar(val):
    if isinstance(val, str):
        if re.search(r'[\u4e00-\u9fff\s\[\]:,]', val) or val in ("true", "false", "null", "yes", "no", "on", "off"):
            escaped = val.replace('\\', '\\\\').replace('"', '\\"')
            return f'"{escaped}"'
        return val
    return str(val)


def rebuild_frontmatter(fm, original_keys):
    lines = []
    for key in original_keys:
        if key not in fm:
            continue
        val = fm[key]
        if val is None:
            continue
        if isinstance(val, list):
            lines.append(f"{key}:")
            for item in val:
                if item is None or str(item).strip() == "None":
                    continue
                lines.append(f"  - {format_scalar(item)}")
        elif isinstance(val, dict):
            lines.append(f"{key}:")
            for k, v in val.items():
                lines.append(f"  {k}: {format_scalar(v)}")
        else:
            lines.append(f"{key}: {format_scalar(val)}")
    return "\n".join(lines)


def main():
    files = list(WIKI_DIR.rglob("*.md"))
    fixed = []
    stats = defaultdict(int)
    
    for file_path in files:
        text = file_path.read_text(encoding="utf-8")
        result = parse_frontmatter(text)
        if result[0] is None:
            continue
        
        fm, body, fm_text = result
        status = str(fm.get("status", "") or "").strip().lower()
        author = str(fm.get("author", "") or "").strip()
        
        if author != "legacy":
            continue
        
        if status not in ("enriched", "reviewed", "stable", "active"):
            continue
        
        inferred = infer_author(file_path, fm, body)
        fm["author"] = inferred
        stats[inferred] += 1
        
        # 保持原始键顺序
        original_keys = list(fm.keys())
        new_fm_text = rebuild_frontmatter(fm, original_keys)
        new_text = f"---\n{new_fm_text}\n---\n{body}"
        file_path.write_text(new_text, encoding="utf-8")
        
        fixed.append({
            "file": str(file_path.relative_to(WIKI_DIR)),
            "status": status,
            "inferred_author": inferred,
        })
    
    # 生成报告
    lines = [
        "# author=legacy 批量修复报告",
        "",
        f"**修复时间**：2026-06-15  ",
        f"**修复文件数**：{len(fixed)}  ",
        "",
        "## 作者推断统计",
        "",
    ]
    for author, count in sorted(stats.items(), key=lambda x: -x[1]):
        lines.append(f"- {author}: {count} 张")
    
    lines.extend(["", "## 修复文件清单", ""])
    for item in fixed:
        lines.append(f"- `{item['file']}` (status={item['status']}) → {item['inferred_author']}")
    
    report_path = REPORT_DIR / "kcard-legacy-author-fix-report-2026-06-15.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    
    print(f"修复文件数：{len(fixed)}")
    print(f"作者统计：{dict(stats)}")
    print(f"报告：{report_path}")


if __name__ == "__main__":
    main()
