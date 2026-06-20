#!/usr/bin/env python3
"""
域感知检索器（Phase 1：域路由 + 关键词混合检索）

不再全库盲目搜。先判断查询属于哪个域，加载域索引入口卡获取候选池，
然后在池内做关键词+wikilink 混合检索，最后按类型分组输出。

用法：
    python 90_control/scripts/query-domain.py "老百姓大药房 研报 调研 一堂方法论"
    python 90_control/scripts/query-domain.py "上市公司财报解读" --json
"""

import argparse
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = VAULT_ROOT / "30_wiki"

# 域关键词 → 域索引入口卡 映射
DOMAIN_ROUTES = {
    "调研": {
        "keywords": ["调研", "研报", "报告", "情报", "尽调", "行业分析", "市场研究", "财报", "招股书",
                     "上市公司", "对标", "benchmark", "research", "analysis"],
        "index_cards": ["yitang-research-domain-digest", "five-step-domain-digest"],
        "search_dirs": ["frameworks", "tools", "cases", "dark-knowledges", "concepts"],
    },
    "决策": {
        "keywords": ["决策", "判断", "选择", "评估", "风险", "ROI", "投资"],
        "index_cards": [],
        "search_dirs": ["concepts", "frameworks", "dark-knowledges"],
    },
    "五步法": {
        "keywords": ["五步法", "产品内核", "商业模式", "增长", "壁垒", "需求"],
        "index_cards": ["five-step-domain-digest"],
        "search_dirs": ["concepts", "frameworks", "tools", "cases"],
    },
    "生产": {
        "keywords": ["卡片", "编译", "wiki", "kdo", "source_refs", "质量"],
        "index_cards": [],
        "search_dirs": ["concepts", "tools"],
    },
}


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    try:
        import yaml
        fm = yaml.safe_load(text[4:end])
        return fm if isinstance(fm, dict) else {}
    except Exception:
        return {}


def extract_wikilinks(text):
    return re.findall(r"\[\[([^\]]+)\]\]", text)


def identify_domains(query):
    """关键词匹配识别域"""
    scores = defaultdict(int)
    for domain, config in DOMAIN_ROUTES.items():
        for kw in config["keywords"]:
            if kw.lower() in query.lower():
                scores[domain] += 1
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)


def load_index_cards(domains):
    """加载域索引入口卡，提取候选卡片 ID"""
    candidates = set()
    for domain_name, domain_config in DOMAIN_ROUTES.items():
        for index_id in domain_config.get("index_cards", []):
            for d in domain_config["search_dirs"]:
                fp = WIKI_DIR / d / f"{index_id}.md"
                if fp.exists():
                    text = fp.read_text(encoding="utf-8")
                    # 提取索引入口卡中所有 wikilink 指向的卡片 ID
                    for link in extract_wikilinks(text):
                        candidates.add(link)
                    # 也提取 bare card IDs
                    for cid in re.findall(r"`([a-z]+-[a-z]+-[a-z0-9-]+)`", text):
                        candidates.add(cid)
    return candidates


def find_card_files(card_ids, search_dirs):
    """在指定目录下找到卡片文件"""
    found = {}
    for cid in card_ids:
        for d in search_dirs:
            fp = WIKI_DIR / d / f"{cid}.md"
            if fp.exists():
                found[cid] = fp
                break
    return found


def score_keywords(text, query_terms):
    """简单 BM25 风格关键词评分"""
    text_lower = text.lower()
    score = 0
    for term in query_terms:
        count = text_lower.count(term.lower())
        if count > 0:
            score += 1 + min(count, 5)
    return score


# 方法论相关关键词 → 信号：用户要的是"怎么做"的方法卡，不是"做了什么"的报告卡
METHODOLOGY_SIGNALS = [
    "方法论", "方法", "框架", "framework", "步骤", "流程", "怎么", "如何",
    "工具", "tool", "手段", "技巧", "策略", "五步", "指南", "系统式",
    "OSCAR", "OSL", "降龙十八掌", "武器库", "雷达", "深挖", "交叉验证",
]

# 报告/输出相关关键词 → 下调权重，用户通常不需要这些
REPORT_SIGNALS = [
    "调研报告", "分析报告", "评估报告", "诊断报告", "可行性", "规划方案",
]


def score_keywords(text, query_terms):
    """简单 BM25 风格关键词评分"""
    text_lower = text.lower()
    score = 0
    for term in query_terms:
        count = text_lower.count(term.lower())
        if count > 0:
            score += 1 + min(count, 5)
    return score


def is_methodology_query(query):
    """判断用户是否在问方法论（怎么做），还是找具体报告（做了什么）"""
    for sig in METHODOLOGY_SIGNALS:
        if sig in query:
            return True
    return False


def type_boost(card_type):
    """方法类查询下，framework/tool 加权，report/case 降权"""
    boosts = {
        "framework": 5,
        "tool": 4,
        "dark-knowledge": 3,
        "dk": 3,
        "concept": 1,
        "case": -2,
        "report": -3,
        "analysis": -1,
    }
    return boosts.get(card_type, 0)


def search_card_body(fp, query_terms):
    """读卡片正文，关键词评分"""
    try:
        text = fp.read_text(encoding="utf-8")
    except Exception:
        return 0

    # 标题加权
    score = 0
    fm = parse_frontmatter(text)
    title = fm.get("title", "")
    score += score_keywords(title, query_terms) * 3

    # 正文匹配
    body_start = text.find("\n---\n", 4)
    if body_start != -1:
        body = text[body_start + 5:]
        score += score_keywords(body[:3000], query_terms)  # 读前 3000 字符

    return score


def query_domain(query, top_k=10):
    """域感知检索主函数"""
    query_terms = re.findall(r"[一-鿿]+|[a-zA-Z]+", query)

    # Step 1: 识别域
    domains = identify_domains(query)
    primary_domain = domains[0][0] if domains else None

    # Step 2: 获取候选池
    candidates = set()
    search_dirs = ["concepts", "frameworks", "tools", "cases", "dark-knowledges", "systems", "domains"]

    if primary_domain and primary_domain in DOMAIN_ROUTES:
        domain_config = DOMAIN_ROUTES[primary_domain]
        search_dirs = domain_config["search_dirs"]
        candidates = load_index_cards([primary_domain])

    # Step 3: 如果域索引卡不够，扩展搜索范围
    if len(candidates) < 20:
        # 全局关键词搜索补充
        for d in search_dirs:
            dir_path = WIKI_DIR / d
            if not dir_path.exists():
                continue
            for fp in dir_path.rglob("*.md"):
                if "_archive" in fp.parts or "raw" in fp.parts:
                    continue
                cid = fp.stem
                # 快速文件名匹配
                name_score = score_keywords(cid, query_terms)
                if name_score > 0:
                    candidates.add(cid)
                # 或者 type 匹配
                if d in search_dirs:
                    candidates.add(cid)

    if len(candidates) > 200:
        # 候选池太大不好，预过滤一下
        pre_filtered = set()
        for cid in candidates:
            if score_keywords(cid, query_terms) > 0:
                pre_filtered.add(cid)
        if pre_filtered:
            candidates = pre_filtered

    # Step 4: 在候选池内打分
    scored = []
    card_files = find_card_files(candidates, search_dirs)
    is_method = is_methodology_query(query)

    for cid, fp in card_files.items():
        score = search_card_body(fp, query_terms)
        fm = parse_frontmatter(fp.read_text(encoding="utf-8"))
        card_type = fm.get("type", "?")

        # 方法类查询：framework/tool 加权，report/case 降权
        if is_method:
            score += type_boost(card_type)

        # 标题匹配加权
        title = fm.get("title", "")
        title_score = score_keywords(title, query_terms) * 3
        score += title_score

        if score > 0:
            scored.append((cid, title, card_type, score))

    scored.sort(key=lambda x: x[3], reverse=True)
    return scored[:top_k], primary_domain


def generate_report(results, domain, query):
    """生成人类可读报告"""
    lines = [
        "# 域感知检索结果",
        f"**查询**: {query}",
        f"**识别域**: {domain or '未识别（全库搜索）'}",
        f"**命中**: {len(results)} 张",
        "",
        "| # | 卡片 ID | 类型 | 标题 | 评分 |",
        "|---|---|---|---|---|",
    ]
    for i, (cid, title, ctype, score) in enumerate(results, 1):
        title_short = title[:60] if title else cid
        lines.append(f"| {i} | `{cid}` | {ctype} | {title_short} | {score} |")

    # 按类型分组建议工作流
    by_type = defaultdict(list)
    for cid, title, ctype, score in results:
        by_type[ctype].append((cid, title))

    if len(by_type) > 1:
        lines.extend(["", "## 建议工作流路径"])
        order = ["framework", "tool", "case", "dark-knowledge", "concept"]
        for t in order:
            if t in by_type:
                cards = by_type[t][:3]
                lines.append(f"\n### {t}（{len(by_type[t])} 张）")
                for cid, title in cards:
                    lines.append(f"- 先读 `{cid}` — {title[:60]}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="域感知检索器")
    parser.add_argument("query", help="自然语言查询")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--top", type=int, default=10)
    args = parser.parse_args()

    results, domain = query_domain(args.query, top_k=args.top)

    if args.json:
        output = [{"id": cid, "title": t, "type": ct, "score": s} for cid, t, ct, s in results]
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        print(generate_report(results, domain, args.query))


if __name__ == "__main__":
    main()
