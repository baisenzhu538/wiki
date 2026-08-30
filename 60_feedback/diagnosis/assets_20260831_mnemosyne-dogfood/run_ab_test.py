# -*- coding: utf-8 -*-
"""#583 狗粮测试 · A/B 对比 harness
A组 10 条自然语言 / B组 10 条精确术语，每组查询分别在：
  - Mnemosyne（50卡沙盒语料，project=kdo-dogfood-583，k=5）
  - kdo query（vault 全库生产索引，--limit 5）
上跑，采集：命中率(hit@1/@3/@5)、MRR、单次延迟、送入LLM上下文的token(cl100k)。
输出：ab_results.json（原始数据，可复现）
"""
import json, os, re, shutil, statistics, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
WS = r"C:\Users\Administrator\Desktop\wiki"
DB_DIR = os.path.join(HERE, "mnemo_store")
PROJECT = "kdo-dogfood-583"

import tiktoken
ENC = tiktoken.get_encoding("cl100k_base")

from mnemosyne import MnemosyneMemory
from mnemosyne.utils import compress_text

# ---------- 查询集（ground truth = 语料内目标卡 id）----------
A_SET = [
    ("A1", "哪些卡讲过怎么把日常刷到的文章视频自动收集进知识库？", "framework-serendipity-five-channels"),
    ("A2", "公司到了要变革的阶段，加外挂还是换路子怎么判断？", "framework-strategy-basics-05-change"),
    ("A3", "增长漏斗每个环节都在流失，怎么优化？", "yt-growth-funnel-optimization"),
    ("A4", "做专家访谈有没有系统的流程和方法？", "framework-yitang-expert-interview-10steps"),
    ("A5", "医药零售小程序加实体药店的模式，利润怎么算、多久回本？", "xingangwan-pharma-business-model-calc"),
    ("A6", "颠覆式创新和延续性创新怎么区分？", "framework-christensen-disruptive-innovation"),
    ("A7", "To B 业务怎么判断该做标品、服务还是定制项目？", "yt-tob-solution-model"),
    ("A8", "单元模型算账水平从差到好分几个阶段？", "yt-unit-model-ladder"),
    ("A9", "客户觉得AI生成的销售内容没人情味、胡说八道怎么办？", "dk-customers-hate-ai"),
    ("A10", "供应商合作失控了，复盘时责任怎么划分？", "case-千惠供应链复盘"),
]
B_SET = [
    ("B1", "framework-yitang-expert-interview-10steps", "framework-yitang-expert-interview-10steps"),
    ("B2", "yt-unit-model-ladder", "yt-unit-model-ladder"),
    ("B3", "case-yitang-single-course-199-failure", "case-yitang-single-course-199-failure"),
    ("B4", "xingangwan-pharma-business-model-calc", "xingangwan-pharma-business-model-calc"),
    ("B5", "dk-signal-cluster-illusion", "dk-signal-cluster-illusion"),
    ("B6", "千人广场模型", "concept-thousand-people-square"),
    ("B7", "口喷新人四难", "dk-oral-spray-newcomer-blockers"),
    ("B8", "PaddleOCR v5", "dk-p8-toolkit-forget"),
    ("B9", "TBox ABox", "case-wechat-article_4dd7be7cd82f7e80"),
    ("B10", "src_20260606_42e11f09", "structured-ai-workspace"),
]


def tok(text):
    return len(ENC.encode(text))


# ---------- Mnemosyne ----------
def mnemo_rank(memory, query, target):
    t0 = time.perf_counter()
    recs = memory.recall(query, k=5, project=PROJECT)
    dt = (time.perf_counter() - t0) * 1000
    ranks = []
    contents = []
    for item in recs:
        rec = item[1] if isinstance(item, tuple) and len(item) >= 2 else item
        content = rec.get("content", "")
        contents.append(content)
        m = re.search(r"^id:\s*(.+?)\s*$", content.split("---")[1] if content.startswith("---") else content, re.M)
        cid = m.group(1) if m else ""
        ranks.append(cid)
    rank = ranks.index(target) + 1 if target in ranks else 0
    full = "\n\n".join(contents)
    comp = "\n\n".join(compress_text(c, level=2) for c in contents)
    return {"rank": rank, "latency_ms": round(dt, 1), "tokens_full": tok(full),
            "tokens_compressed": tok(comp), "top_ids": ranks}


# ---------- kdo ----------
KDO = shutil.which("kdo")
KDO_NOISE = re.compile(r"^\[kdo\]|^Top \d+ result")
KDO_RESULT = re.compile(r"^\[(\d+\.?\d*)\]\s+(\S+)$", re.M)


def kdo_rank(query, target):
    t0 = time.perf_counter()
    proc = subprocess.run([KDO, "query", query, "--limit", "5"], cwd=WS,
                          capture_output=True, encoding="utf-8", errors="replace", timeout=120)
    dt = (time.perf_counter() - t0) * 1000
    out = proc.stdout or ""
    paths = [m.group(2) for m in KDO_RESULT.finditer(out)]
    rank = 0
    for i, p in enumerate(paths):
        if p.endswith(target + ".md"):
            rank = i + 1
            break
    # 送进LLM的上下文 = 结果块（去掉[kdo]噪声行与头行）
    blocks = "\n".join(l for l in out.splitlines() if not KDO_NOISE.match(l))
    return {"rank": rank, "latency_ms": round(dt, 1), "tokens_context": tok(blocks), "top_paths": paths}


def hit_stats(entries):
    n = len(entries)
    return {
        "hit@1": sum(1 for e in entries if e["rank"] == 1) / n,
        "hit@3": sum(1 for e in entries if 0 < e["rank"] <= 3) / n,
        "hit@5": sum(1 for e in entries if 0 < e["rank"] <= 5) / n,
        "mrr": sum(1 / e["rank"] for e in entries if e["rank"]) / n,
        "median_latency_ms": statistics.median(e["latency_ms"] for e in entries),
    }


def main():
    memory = MnemosyneMemory(base_dir=DB_DIR, k=5)
    memory.recall("预热查询", k=1, project=PROJECT)  # 索引加载暖场
    results = {"meta": {"engine": "mnemosyne-os 7.0.0 + kdo query(vault全库)", "k": 5,
                        "tokenizer": "tiktoken cl100k_base", "corpus": "50卡/222880字符",
                        "ts": time.strftime("%Y-%m-%d %H:%M:%S")}, "A": [], "B": []}
    for group, qset in (("A", A_SET), ("B", B_SET)):
        for qid, q, target in qset:
            row = {"id": qid, "query": q, "target": target,
                   "mnemo": mnemo_rank(memory, q, target),
                   "kdo": kdo_rank(q, target)}
            results[group].append(row)
            print(f"[{qid}] mnemo rank={row['mnemo']['rank']} kdo rank={row['kdo']['rank']} :: {q[:30]}")
    summary = {}
    for g in ("A", "B"):
        summary[g] = {
            "mnemo": hit_stats([r["mnemo"] for r in results[g]]),
            "kdo": hit_stats([r["kdo"] for r in results[g]]),
            "mnemo_tokens_full_avg": statistics.mean(r["mnemo"]["tokens_full"] for r in results[g]),
            "mnemo_tokens_compressed_avg": statistics.mean(r["mnemo"]["tokens_compressed"] for r in results[g]),
            "kdo_tokens_context_avg": statistics.mean(r["kdo"]["tokens_context"] for r in results[g]),
        }
    results["summary"] = summary
    out = os.path.join(HERE, "ab_results.json")
    json.dump(results, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved ->", out)
    print(json.dumps(summary, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
