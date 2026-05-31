"""Verify auto_label accuracy against Gold Standard (15 chunks)."""
import json
import sys
sys.path.insert(0, r'C:\Users\Administrator\Knowledge Delivery OS 0.0.1')

from pathlib import Path
from kdo.commands.label import auto_label_chunk, load_tag_registry, flatten_dimensions
from kdo.llm import LLMConfig

VAULT = Path(r'C:\Users\Administrator\Desktop\wiki')
registry = load_tag_registry(VAULT)
cfg = LLMConfig.from_yaml()

# Gold Standard: 15 chunks hard-coded from 30_wiki/decisions/gold-standard-manual-labels.md
GOLD = [
    # Chunk 1: master-decision-hygiene — bias vs noise definition
    {"text": "偏差（Bias）是系统性倾向，总是往同一方向偏。噪声（Noise）是随机波动，不同人/不同时刻往不同方向偏。偏差类比：枪靶总是偏右上方。噪声类比：枪靶散布很大但中心是对的。金句：偏差是'枪总打偏'，噪声是'枪到处乱飞'。框架修的是'偏'，卫生修的是'散'。",
     "labels": {"domain": "master", "chunk_type": "definition", "method_family": "thinking-tool",
                "audience": "general", "perspective": "general", "platform": "general",
                "confidence": "0.90", "data_generation": "original", "value_tier": "micro",
                "prerequisite_knowledge": "basic-domain", "expiry": "stable", "usage_depth": "feed"}},
    # Chunk 2: master-decision-hygiene — Step 1 procedure
    {"text": "核心操作：把'这个项目能成吗？'拆成'市场规模→竞争强度→团队能力→资金需求→执行风险'五个子判断。为什么有效：复杂判断的噪声 > 简单判断的噪声之和。具体做法：1. 列出决策涉及的所有维度（≥3 个）2. 每个维度给一个独立评分（1-10 或具体数值）3. 禁止在分解前就给出整体判断。陷阱：分解维度本身也可能有噪声——不同的人拆出不同的维度。",
     "labels": {"domain": "master", "chunk_type": "procedure", "method_family": "thinking-tool",
                "audience": "manager", "perspective": "general", "platform": "general",
                "confidence": "0.90", "data_generation": "original", "value_tier": "micro",
                "prerequisite_knowledge": "basic-domain", "expiry": "stable", "usage_depth": "feed"}},
    # Chunk 3: master-decision-hygiene — Gary Klein critique
    {"text": "Gary Klein（'Sources of Power'作者，自然决策理论创始人）基于数十年对消防员、急救医生、军事指挥官的田野观察，对'决策卫生'提出根本性质疑。消防指挥官在秒级决策窗口中的直觉判断，事后分析往往优于耗时做效用计算的结果。五步法的'分解→外部→独立→聚合→延迟'在火灾现场根本不适用——等走完五步，楼已经烧完了。",
     "labels": {"domain": "master", "chunk_type": "critique", "method_family": "thinking-tool",
                "audience": "general", "perspective": "professional", "platform": "general",
                "confidence": "0.70", "data_generation": "original", "value_tier": "micro",
                "prerequisite_knowledge": "intermediate-method", "expiry": "stable", "usage_depth": "feed"}},
    # Chunk 4: master-decision-hygiene — time constraint
    {"text": "时间成本高：完整五步法需要1-3天（含延迟直觉的等待时间），不适合日常小决策。建议只在'高影响+不可逆'决策前使用。依赖团队独立性：Step 3的'独立评估'最难执行——团队成员可能已经通过各种渠道知道了彼此的倾向。必须在物理/数字上隔离。",
     "labels": {"domain": "master", "chunk_type": "constraint", "method_family": "thinking-tool",
                "audience": "manager", "perspective": "general", "platform": "general",
                "confidence": "0.90", "data_generation": "original", "value_tier": "micro",
                "prerequisite_knowledge": "basic-domain", "expiry": "stable", "usage_depth": "feed"}},
    # Chunk 5: yt-decision-y-model — core claim
    {"text": "Y 模型在一堂知识体系中的坐标：科学决策模块的底层框架，贯穿预判、起盘、增长三阶段，与关键假设、单元模型、科学管理等课程形成方法论网络。",
     "labels": {"domain": "yitang", "chunk_type": "claim", "method_family": "decision-framework",
                "audience": "general", "perspective": "general", "platform": "general",
                "confidence": "0.85", "data_generation": "original", "value_tier": "micro",
                "prerequisite_knowledge": "basic-domain", "expiry": "stable", "usage_depth": "feed"}},
    # Chunk 6: yt-decision-y-model — width definition
    {"text": "宽度：这件事涉及多少收益项和成本项？操作要点：列清单→推演业务过程→查盲区（列推查）。目标不是越多越好，而是'找全'以确保关键项不遗漏，再从中识别真正关键的几项。",
     "labels": {"domain": "yitang", "chunk_type": "definition", "method_family": "decision-framework",
                "audience": "manager", "perspective": "general", "platform": "general",
                "confidence": "0.85", "data_generation": "original", "value_tier": "micro",
                "prerequisite_knowledge": "basic-domain", "expiry": "stable", "usage_depth": "feed"}},
    # Chunk 7: yt-decision-y-model — Klein critique
    {"text": "Gary Klein（宏观认知/自然决策理论创始人）对结构化决策框架提出了根本性挑战。Klein通过对消防员、急救医护、军事指挥官等专家决策者的实地研究提出RPD模型：专家决策的核心是模式识别而非比较分析。在真实的高风险、时间压力、信息不完备场景中，专家并非列出多个方案比较利弊，而是在看到情境的瞬间就识别出'这像什么'，并直接生成一个可行方案。结构化分析会打断专家的直觉过程。",
     "labels": {"domain": "yitang", "chunk_type": "critique", "method_family": "decision-framework",
                "audience": "general", "perspective": "professional", "platform": "general",
                "confidence": "0.70", "data_generation": "original", "value_tier": "micro",
                "prerequisite_knowledge": "intermediate-method", "expiry": "stable", "usage_depth": "feed"}},
    # Chunk 8: yt-decision-y-model — crisis constraint
    {"text": "时间窗口极短的危机决策（如突发公关危机需在2小时内回应、生产安全事故需立即处置）：Y模型的'列推查→逐层深入'流程耗时过长，危机场景需要的是基于预案的快速反应而非重新分析。此时'停下来做分析'本身就是最大的成本——时间窗口会关闭。框架的结构性在此成为负担。",
     "labels": {"domain": "yitang", "chunk_type": "constraint", "method_family": "decision-framework",
                "audience": "manager", "perspective": "general", "platform": "general",
                "confidence": "0.85", "data_generation": "original", "value_tier": "micro",
                "prerequisite_knowledge": "basic-domain", "expiry": "stable", "usage_depth": "feed"}},
    # Chunk 9: yt-decision-y-model — action trigger
    {"text": "触发场景：即将投入 ≥10 万元或影响 ≥3 人的资源，且内心有犹豫。第一个动作：打开Y模型画布，强制列出 ≥5 条收益项和 ≥5 条成本项（用'列推查'），标注其中最关键的前3项。成功指标：画布上至少出现1条'之前完全没想到'的收益或成本项。",
     "labels": {"domain": "yitang", "chunk_type": "action_trigger", "method_family": "decision-framework",
                "audience": "manager", "perspective": "roi", "platform": "general",
                "confidence": "0.85", "data_generation": "original", "value_tier": "micro",
                "prerequisite_knowledge": "basic-domain", "expiry": "current", "usage_depth": "feed"}},
    # Chunk 10: master-cognitive-bias-checklist — 12 biases procedure
    {"text": "决策前花3-5分钟，逐条问自己这12个问题。任何一个问题的答案是'是'，就执行对应的'快速修复'。01 锚定效应：我做判断时，第一个看到的数字/信息是否还在影响我？→主动重新锚定。02 确认偏误：我是否只找了支持我已有观点的证据？→强制找反例。",
     "labels": {"domain": "master", "chunk_type": "procedure", "method_family": "evaluation-method",
                "audience": "general", "perspective": "general", "platform": "general",
                "confidence": "0.85", "data_generation": "original", "value_tier": "micro",
                "prerequisite_knowledge": "none", "expiry": "stable", "usage_depth": "feed"}},
    # Chunk 11: master-cognitive-bias-checklist — Kahneman attack
    {"text": "Daniel Kahneman（诺贝尔经济学奖获得者）对'用清单对抗偏差'本身提出了根本性质疑。认知偏差是系统1（直觉）的自动化产物，清单是系统2（理性）的工具——但系统2太慢、太累、太懒，无法在所有决策中持续监控系统1。当你跑完这12个问题后，你会产生'我已经检查过了，所以我很客观'的错觉——但'检查过'不等于'消除了'。清单给你的不是'客观'，是'客观感'。",
     "labels": {"domain": "master", "chunk_type": "critique", "method_family": "evaluation-method",
                "audience": "general", "perspective": "professional", "platform": "general",
                "confidence": "0.90", "data_generation": "original", "value_tier": "micro",
                "prerequisite_knowledge": "basic-domain", "expiry": "stable", "usage_depth": "feed"}},
    # Chunk 12: master-cognitive-bias-checklist — cannot eliminate constraint
    {"text": "不能消除偏差：清单只能降低偏差被忽略的概率，不能消除偏差本身。目标是'发现自己可能有偏差'，不是'证明自己已经没有偏差'。清单本身也是框架：使用清单会产生'清单偏差'——觉得'检查过了就不会犯了'。必须在每次使用后明确写下'但我可能还是错了'。",
     "labels": {"domain": "master", "chunk_type": "constraint", "method_family": "evaluation-method",
                "audience": "general", "perspective": "general", "platform": "general",
                "confidence": "0.90", "data_generation": "original", "value_tier": "micro",
                "prerequisite_knowledge": "none", "expiry": "stable", "usage_depth": "feed"}},
    # Chunk 13: ai时代判断力口述-3 — IPO displacement (dark knowledge)
    {"text": "IPO 位移：AI 接管了 P（Process），且 P 变得极快极便宜。过去 P 是最难最稀缺的环节，现在 P 同质化了。结果：I（问题定义、需求深挖）和 O（结果判断、审美把关、责任承担）成为新的瓶颈和竞争力所在。关键金句：'加速一切，除了思考'。",
     "labels": {"domain": "yitang", "chunk_type": "claim", "method_family": "knowledge-engineering",
                "audience": "developer", "perspective": "professional", "platform": "general",
                "confidence": "0.75", "data_generation": "original", "value_tier": "micro",
                "prerequisite_knowledge": "basic-domain", "expiry": "current", "usage_depth": "feed"}},
    # Chunk 14: ai时代判断力口述-3 — judgment pyramid (dark knowledge)
    {"text": "判断力的三层金字塔：底层—能判断什么AI做不了（核心算价逻辑、涉及钱的代码、关键安全逻辑——这些必须人写，AI只做Review）。中层—一致性判断（代码风格、Tab vs空格、文档规范）。顶层—审美判断：'审美不是天赋，是伤疤的组合'——AI见过百万倍于人的失败案例但不懂疼。",
     "labels": {"domain": "yitang", "chunk_type": "definition", "method_family": "thinking-tool",
                "audience": "developer", "perspective": "professional", "platform": "general",
                "confidence": "0.75", "data_generation": "original", "value_tier": "micro",
                "prerequisite_knowledge": "basic-domain", "expiry": "current", "usage_depth": "feed"}},
    # Chunk 15: ai时代判断力口述-3 — training ground crisis (dark knowledge)
    {"text": "人类训练场的消失（代际危机）：初级工程师/岗位被AI取代后，新人不再有机会通过亲手做Process积累判断力和审美。成长链条断裂：写代码→炸了→复盘（一层）→能用但难维护（二层）→逐步改→练出审美（三层）。不写代码长不出代码审美。10年经验的程序员能练就判断力，新大学生练什么？",
     "labels": {"domain": "yitang", "chunk_type": "question", "method_family": "knowledge-engineering",
                "audience": "developer", "perspective": "professional", "platform": "general",
                "confidence": "0.70", "data_generation": "original", "value_tier": "micro",
                "prerequisite_knowledge": "basic-domain", "expiry": "current", "usage_depth": "feed"}},
]

total_dims = 0
total_matches = 0
chunk_results = []

# Dimensions the auto_label pipeline currently outputs
# (card-level dims like domain/data_generation/value_tier are not auto-labeled)
COMPARISON_DIMS = {"chunk_type", "method_family", "audience", "perspective", "platform",
                   "confidence", "prerequisite_knowledge", "expiry", "usage_depth"}

for i, g in enumerate(GOLD):
    result = auto_label_chunk(g["text"][:2000], registry=registry, llm_config=cfg, top_k=10)
    auto_labels = {}
    for lbl in result.get("result", {}).get("labels", []):
        auto_labels[lbl["dimension"]] = lbl["value"]

    chunk_dims = 0
    chunk_matches = 0
    details = []
    for dim, gold_val in g["labels"].items():
        if dim not in COMPARISON_DIMS:
            continue  # skip card-level dims the auto pipeline doesn't label
        chunk_dims += 1
        auto_val = auto_labels.get(dim, "<missing>")
        if auto_val == gold_val:
            chunk_matches += 1
            details.append(f"  PASS {dim}: {gold_val}")
        else:
            details.append(f"  FAIL {dim}: gold={gold_val} auto={auto_val}")

    acc = chunk_matches / chunk_dims if chunk_dims else 0
    total_dims += chunk_dims
    total_matches += chunk_matches
    chunk_results.append({
        "id": i+1,
        "dims": chunk_dims,
        "matches": chunk_matches,
        "accuracy": round(acc, 3),
        "details": details,
    })
    print(f"\n--- Chunk {i+1} (acc={acc:.1%}) ---")
    for d in details:
        print(d)

overall = total_matches / total_dims if total_dims else 0
auto_total = sum(1 for c in chunk_results if c["accuracy"] > 0)
print(f"\n{'='*50}")
print(f"Overall accuracy: {total_matches}/{total_dims} = {overall:.1%}")
print(f"Chunks with any match: {auto_total}/{len(GOLD)}")
print(f"{'='*50}")

summary_path = VAULT / "60_feedback/data-quality/label-results/gold-standard-verify.json"
summary_path.write_text(json.dumps({
    "total_chunks": len(GOLD),
    "total_dimensions": total_dims,
    "total_matches": total_matches,
    "accuracy": round(overall, 4),
    "chunks": chunk_results,
}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nFull results -> {summary_path}")

