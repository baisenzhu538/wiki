"""
批量补全 related 字段 —— TF-IDF 余弦相似度推荐 top-5 最相关卡片。

使用方式：
    python auto-related.py --dry-run   # 预览影响范围
    python auto-related.py             # 实际写入
"""

import re, json, sys
from collections import defaultdict
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

WIKI = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")
MIN_SIMILARITY = 0.15   # 相似度低于此值不推荐
TOP_K = 5


def extract_text(fpath: Path) -> str:
    """提取卡片正文（跳过 YAML frontmatter）用于 TF-IDF。"""
    try:
        raw = fpath.read_text(encoding="utf-8")
    except Exception:
        return ""
    if raw.startswith("---"):
        end = raw.find("---", 3)
        if end != -1:
            raw = raw[end + 3:]
    # 取前 3000 字符，去掉 wikilinks 语法
    raw = re.sub(r'\[\[([^\]]+)\]\]', r'\1', raw[:3000])
    return raw


def parse_frontmatter(text: str) -> dict | None:
    if not text.startswith("---"):
        return None
    end = text.find("---", 3)
    if end == -1:
        return None
    fm = {}
    for line in text[3:end].split("\n"):
        if ":" in line:
            k, _, v = line.partition(":")
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if v.startswith("[") and v.endswith("]"):
                fm[k] = [it.strip().strip('"').strip("'") for it in v[1:-1].split(",") if it.strip()]
            else:
                fm[k] = v
    # Multi-line YAML lists
    for lk in ["related", "domain", "source_refs", "tags"]:
        if lk in fm and (fm[lk] == [] or fm[lk] == ""):
            pat = re.compile(rf"^{lk}:\n((?:\s+-.+\n?)*)", re.MULTILINE)
            m = pat.search(text[3:end])
            if m:
                items = re.findall(r"^\s*-\s+(.+)$", m.group(1), re.MULTILINE)
                fm[lk] = [it.strip().strip('"').strip("'") for it in items]
    return fm


def get_related(fm: dict) -> set:
    rel = fm.get("related", [])
    if isinstance(rel, str):
        rel = [rel]
    ids = set()
    for r in rel:
        r = r.strip()
        if not r:
            continue
        m = re.search(r'\[\[([^\]|]+)', r)
        if m:
            ids.add(m.group(1).strip())
        else:
            ids.add(r)
    return ids


def write_related(fpath: Path, new_related_ids: list[str], dry_run: bool):
    text = fpath.read_text(encoding="utf-8")
    end = text.find("---", 3)
    fm_block = text[3:end]
    rest = text[end + 3:]

    # Build YAML related block
    rel_lines = ["related:"]
    for rid in new_related_ids:
        rel_lines.append(f"  - '[[{rid}]]'")

    # Replace or insert related field
    if "\nrelated:" in fm_block:
        # Replace existing
        new_fm = re.sub(
            r'^related:.*$(\n(?:  -.*\n?)*)?',
            '\n'.join(rel_lines) + '\n',
            fm_block,
            flags=re.MULTILINE
        )
    else:
        # Insert before the closing ---
        new_fm = fm_block.rstrip() + "\n" + "\n".join(rel_lines) + "\n"

    new_text = "---\n" + new_fm + "---" + rest
    if not dry_run:
        fpath.write_text(new_text, encoding="utf-8")


def main(dry_run=False):
    # 1. 扫描所有卡片
    all_cards = []
    for f in sorted(WIKI.rglob("*.md")):
        if any(p in str(f) for p in ["_archive", "raw/", ".git", "index.md", "log.md"]):
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except Exception:
            continue
        fm = parse_frontmatter(text)
        if not fm or "id" not in fm:
            continue
        body = extract_text(f)
        all_cards.append({
            "id": fm["id"],
            "title": fm.get("title", ""),
            "type": fm.get("type", "?"),
            "status": fm.get("status", "?"),
            "domain": fm.get("domain", ""),
            "text": body[:3000],
            "path": str(f.relative_to(WIKI)).replace("\\", "/"),
            "fpath": f,
            "fm": fm,
        })

    print(f"卡片总数: {len(all_cards)}")

    # 2. 识别无出链卡（无 related 或 related 为空）
    no_outgoing = []
    id_to_idx = {}
    for i, c in enumerate(all_cards):
        id_to_idx[c["id"]] = i
        rel = get_related(c["fm"])
        if not rel:
            no_outgoing.append(c)

    print(f"无出链卡: {len(no_outgoing)}")

    # 3. TF-IDF + 余弦相似度
    texts = [c["text"] for c in all_cards]
    vectorizer = TfidfVectorizer(max_features=5000, stop_words=None, lowercase=False)
    tfidf = vectorizer.fit_transform(texts)
    print(f"TF-IDF 矩阵: {tfidf.shape}")

    # 4. 为每张无出链卡找 top-K
    skipped = 0
    written = 0
    for nc in no_outgoing:
        idx = id_to_idx[nc["id"]]
        query_vec = tfidf[idx]
        sims = cosine_similarity(query_vec, tfidf).flatten()
        # 排除自身 + 相似度低于阈值
        candidates = []
        for j in np.argsort(-sims):
            if j == idx:
                continue
            if sims[j] < MIN_SIMILARITY:
                break
            # 优先同域
            candidates.append((all_cards[j]["id"], sims[j]))
            if len(candidates) >= TOP_K * 2:  # collect extra, then filter
                break

        # 取 top-K，至少 1 个（如果找得到）
        best = candidates[:TOP_K]
        if not best:
            skipped += 1
            continue

        new_related = [bid for bid, _ in best]
        # 合并已有 related（如果有）
        existing = get_related(nc["fm"])
        combined = list(dict.fromkeys(existing | set(new_related)))  # dedup, keep order

        if dry_run:
            print(f"  [DRY-RUN] {nc['id']} ({nc['type']}) [{nc.get('title','')[:40]}] -> {new_related[:3]}")
        else:
            write_related(nc["fpath"], combined, dry_run=False)
        written += 1

    mode = "[DRY-RUN] " if dry_run else ""
    print(f"\n{mode}写入: {written} | 跳过（无相似卡）: {skipped}")


def verify():
    """Spot-check recommendation quality by sampling 5 cards with related fields.

    For each sampled card, prints: the card body snippet, each recommended related
    card with its TF-IDF similarity score and body snippet.  No files are written.
    A human reviews the output to judge whether the recommendations make sense.
    """
    import random
    random.seed(42)  # reproducible

    all_cards, no_outgoing, id_to_idx = _scan_cards()
    print(f"卡片总数: {len(all_cards)} | 无出链: {len(no_outgoing)}")

    # Only verify cards that already have related fields (written by a prior run)
    with_related = [c for c in all_cards if get_related(c["fm"])]
    if not with_related:
        print("没有已写入 related 的卡片。先运行 auto-related.py 再 --verify。")
        return

    sample = random.sample(with_related, min(5, len(with_related)))
    print(f"有 related 的卡片: {len(with_related)} | 抽检: {len(sample)}\n")

    texts = [c["text"] for c in all_cards]
    vectorizer = TfidfVectorizer(max_features=5000, stop_words=None, lowercase=False)
    tfidf = vectorizer.fit_transform(texts)

    for i, card in enumerate(sample, 1):
        related_ids = get_related(card["fm"])
        body_preview = card["text"][:200].replace("\n", " ").strip()
        print(f"{'='*72}")
        print(f"#{i}  {card['id']}  [{card['type']}]  {card.get('title','')[:60]}")
        print(f"  正文预览: {body_preview}...".encode(sys.stdout.encoding, errors="replace").decode(sys.stdout.encoding))
        print(f"  推荐 {len(related_ids)} 张关联卡:")

        c_idx = id_to_idx[card["id"]]
        query_vec = tfidf[c_idx]
        sims = cosine_similarity(query_vec, tfidf).flatten()

        for rid in related_ids:
            if rid not in id_to_idx:
                print(f"    [[{rid}]]  (卡片不在索引中)")
                continue
            r_idx = id_to_idx[rid]
            r_card = all_cards[r_idx]
            r_body = r_card["text"][:150].replace("\n", " ").strip()
            score = sims[r_idx]
            bar = "█" * max(1, int(score * 40))
            line1 = f"    [[{rid}]]  [{r_card['type']}]  sim={score:.3f} {bar}"
            line2 = f"      {r_card.get('title','')[:60]}"
            line3 = f"      {r_body}..."
            for line in [line1, line2, line3]:
                print(line.encode(sys.stdout.encoding, errors="replace").decode(sys.stdout.encoding))
            print()

    print(f"{'='*72}")
    print("抽检完毕。人工判断标准：")
    print("  sim ≥ 0.30 → 通常合理")
    print("  0.15 ≤ sim < 0.30 → 需要人工确认")
    print("  sim < 0.15 → 大概率噪音（已过滤）")


def _scan_cards():
    """Shared card scanning logic used by both main() and verify()."""
    all_cards = []
    for f in sorted(WIKI.rglob("*.md")):
        if any(p in str(f) for p in ["_archive", "raw/", ".git", "index.md", "log.md"]):
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except Exception:
            continue
        fm = parse_frontmatter(text)
        if not fm or "id" not in fm:
            continue
        body = extract_text(f)
        all_cards.append({
            "id": fm["id"],
            "title": fm.get("title", ""),
            "type": fm.get("type", "?"),
            "status": fm.get("status", "?"),
            "domain": fm.get("domain", ""),
            "text": body[:3000],
            "path": str(f.relative_to(WIKI)).replace("\\", "/"),
            "fpath": f,
            "fm": fm,
        })

    id_to_idx = {c["id"]: i for i, c in enumerate(all_cards)}
    no_outgoing = [c for c in all_cards if not get_related(c["fm"])]
    return all_cards, no_outgoing, id_to_idx


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true", help="预览影响范围，不写入")
    p.add_argument("--verify", action="store_true", help="随机抽检5张已有related的卡片，人工判断推荐质量")
    args = p.parse_args()

    if args.verify:
        verify()
    else:
        main(dry_run=args.dry_run)
