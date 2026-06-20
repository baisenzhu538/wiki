#!/usr/bin/env python3
"""
域感知混合检索器 v2
架构：域索引入口卡（MOC 模式）绝对优先 → BM25 关键词融合 → RRF 排序

业界依据（2026 调研）：
- Obsidian MOC: 索引入口卡 = 人工策展的导航 hub，优于纯自动检索
- Hybrid Search: BM25 + Vector + RRF = 15-20% MRR 提升（Google Research 2025）
- Domain-Aware Routing: 先分域再检索（LlamaIndex RouterQueryEngine 模式）

用法：
    python 90_control/scripts/query-domain.py "老百姓大药房 研报 调研"
    python 90_control/scripts/query-domain.py "调研 爬虫" --json
"""

import argparse
import json
import math
import re
import sys
from pathlib import Path
from collections import defaultdict

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = VAULT_ROOT / "30_wiki"

# 域关键词 → 域索引入口卡
DOMAIN_ROUTES = {
    "调研": {
        "keywords": ["调研", "研报", "报告", "情报", "尽调", "行业分析", "市场研究",
                     "财报", "招股书", "上市公司", "对标", "benchmark", "research",
                     "爬虫", "数据采集", "OCR", "scraping"],
        "index_cards": ["yitang-research-domain-digest"],
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
}


def parse_frontmatter(text):
    if not text.startswith("---\n"): return {}
    end = text.find("\n---\n", 4)
    if end == -1: return {}
    try:
        import yaml
        fm = yaml.safe_load(text[4:end])
        return fm if isinstance(fm, dict) else {}
    except: return {}


def tokenize(text):
    """中文按字+词切分，英文按空格"""
    tokens = []
    # 英文词
    tokens.extend(re.findall(r"[a-zA-Z0-9]+", text.lower()))
    # 中文 bigram
    cn = re.findall(r"[一-鿿]+", text)
    for w in cn:
        tokens.append(w)  # 全词
        for i in range(len(w) - 1):
            tokens.append(w[i:i+2])  # bigram
    return tokens


def bm25_score(doc_tokens, query_tokens, doc_freqs, total_docs, avg_dl, k1=1.2, b=0.75):
    """简化 BM25"""
    dl = len(doc_tokens)
    score = 0.0
    for qt in query_tokens:
        df = doc_freqs.get(qt, 0)
        if df == 0: continue
        tf = doc_tokens.count(qt)
        idf = math.log(1 + (total_docs - df + 0.5) / (df + 0.5))
        numerator = tf * (k1 + 1)
        denominator = tf + k1 * (1 - b + b * dl / max(avg_dl, 1))
        score += idf * numerator / denominator
    return score


def extract_index_lookup(domain_config):
    """
    从域索引入口卡提取 场景→卡片 映射表（MOC 模式核心）。
    入口卡里显式列出的卡片 = 人工策展质量 = 绝对优先。
    """
    lookup = {}  # card_id -> {'scenario': str, 'boost': int}
    for index_id in domain_config.get("index_cards", []):
        for d in domain_config.get("search_dirs", ["domains", "frameworks", "tools", "concepts", "cases"]) + ["domains"]:
            fp = WIKI_DIR / d / f"{index_id}.md"
            if not fp.exists(): continue
            for line in fp.read_text(encoding="utf-8").split("\n"):
                if not line.startswith("|"): continue
                cells = [c.strip() for c in line.split("|") if c.strip()]
                if len(cells) < 2: continue
                # 提取行内所有卡片 ID
                card_ids = re.findall(r"`([a-z]+-[a-z]+-[a-z0-9-]+)`", line)
                scenario = re.sub(r"[^一-鿿 a-zA-Z0-9]", " ", cells[0]).strip()
                for cid in card_ids:
                    if cid not in lookup:
                        lookup[cid] = {"scenarios": [], "source": index_id}
                    lookup[cid]["scenarios"].append(scenario)
    return lookup


def query_domain(query, top_k=10):
    """
    三步检索：
    1. MOC 查表：域索引入口卡场景匹配 → 直接命中（100+ 分起）
    2. BM25 关键词：在候选池内打分
    3. RRF 融合排序
    """
    query_terms = tokenize(query)

    # Step 1: 识别域
    domain_scores = defaultdict(int)
    for domain, config in DOMAIN_ROUTES.items():
        for kw in config["keywords"]:
            if kw.lower() in query.lower():
                domain_scores[domain] += 1
    primary_domain = max(domain_scores, key=domain_scores.get) if domain_scores else None

    # Step 2: 加载域索引入口卡 → 获取 MOC 优先列表 + 候选池
    moc_priority = {}  # card_id -> boost
    candidates = set()
    search_dirs = ["frameworks", "tools", "cases", "dark-knowledges", "concepts", "domains", "dark-knowledges"]

    if primary_domain and primary_domain in DOMAIN_ROUTES:
        config = DOMAIN_ROUTES[primary_domain]
        search_dirs = config["search_dirs"]
        index_lookup = extract_index_lookup(config)

        # 场景→卡片直接匹配（MOC 最高优先级）
        for cid, info in index_lookup.items():
            candidates.add(cid)
            for scenario in info["scenarios"]:
                match = score_keywords_simple(scenario, query)
                if match > 0:
                    moc_priority[cid] = max(moc_priority.get(cid, 0), 100 + match * 10)

        # 候选池不够，全局补充
        if len(candidates) < 30:
            for d in search_dirs:
                dir_path = WIKI_DIR / d
                if not dir_path.exists(): continue
                for fp in dir_path.rglob("*.md"):
                    if "_archive" in fp.parts or "raw" in fp.parts: continue
                    candidates.add(fp.stem)

    # Step 3: BM25 在候选池内打分
    # 收集文档
    docs = {}
    all_tokens = []
    doc_freqs = defaultdict(int)

    for cid in list(candidates)[:500]:  # 上限 500 防爆炸
        for d in search_dirs:
            fp = WIKI_DIR / d / f"{cid}.md"
            if not fp.exists(): continue
            try:
                text = fp.read_text(encoding="utf-8")
            except: continue
            fm = parse_frontmatter(text)
            title = fm.get("title", "")
            card_type = fm.get("type", "?")

            # 索引标题 + 前 3000 字符正文
            body_start = text.find("\n---\n", 4)
            body = text[body_start+5:3000] if body_start > 0 else ""
            index_text = (title + " " + title + " " + body)  # 标题加权

            tokens = tokenize(index_text)
            docs[cid] = {"tokens": tokens, "type": card_type, "title": title, "path": str(fp.relative_to(VAULT_ROOT))}
            all_tokens.append(tokens)
            for t in set(tokens):
                doc_freqs[t] += 1
            break

    total_docs = len(docs)
    avg_dl = sum(len(d["tokens"]) for d in docs.values()) / max(total_docs, 1)

    # BM25 评分
    bm25_scores = {}
    for cid, doc in docs.items():
        bm25_scores[cid] = bm25_score(doc["tokens"], query_terms, doc_freqs, total_docs, avg_dl)

    # 归一化 BM25
    max_bm25 = max(bm25_scores.values()) if bm25_scores else 1
    if max_bm25 > 0:
        bm25_scores = {k: v / max_bm25 * 50 for k, v in bm25_scores.items()}

    # Step 4: RRF 融合
    # MOC 优先 + BM25 关键词 + 类型加权
    TYPE_BOOST = {"framework": 10, "tool": 8, "dk": 5, "dark-knowledge": 5, "case": 2, "concept": 0}
    final_scores = {}

    for cid in docs:
        score = 0.0
        # MOC 查表命中
        if cid in moc_priority:
            score += moc_priority[cid]
        # BM25
        score += bm25_scores.get(cid, 0)
        # 类型加权
        score += TYPE_BOOST.get(docs[cid]["type"], 0)
        final_scores[cid] = score

    # 排序
    ranked = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)

    results = []
    for cid, score in ranked[:top_k]:
        doc = docs[cid]
        results.append((cid, doc["title"], doc["type"], round(score, 1), doc["path"]))

    return results, primary_domain, len(index_lookup) if primary_domain else 0


def score_keywords_simple(text, query):
    """简单场景匹配"""
    s = 0
    for t in tokenize(query):
        if t in text.lower():
            s += 1
    return s


def generate_report(results, domain, moc_size, query):
    lines = [
        "# 域感知混合检索 v2",
        f"**查询**: {query}",
        f"**识别域**: {domain or '全库'} | **索引入口卡**: {moc_size} 条映射",
        f"**命中**: {len(results)} 张",
        "",
        "| # | 卡片 ID | 类型 | 标题 | 评分 |",
        "|---|---|---|---|---|",
    ]
    for i, (cid, title, ctype, score, path) in enumerate(results, 1):
        title_short = title[:60] if title else cid
        lines.append(f"| {i} | `{cid}` | {ctype} | {title_short} | {score} |")

    lines.extend(["", "## 建议阅读路径"])
    order = ["framework", "tool", "case", "dark-knowledge", "dk", "concept"]
    for t in order:
        cards = [(cid, title) for cid, title, ct, _, _ in results if ct == t]
        if cards:
            lines.append(f"**{t}**: " + " → ".join(f"`{cid}`" for cid, _ in cards[:4]))

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="域感知混合检索器 v2")
    parser.add_argument("query", help="自然语言查询")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--top", type=int, default=10)
    args = parser.parse_args()

    results, domain, moc_size = query_domain(args.query, top_k=args.top)

    if args.json:
        output = [{"id": cid, "title": t, "type": ct, "score": s, "path": p}
                  for cid, t, ct, s, p in results]
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        print(generate_report(results, domain, moc_size, args.query))


if __name__ == "__main__":
    main()
