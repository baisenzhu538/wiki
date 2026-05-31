"""Quick test of new few-shot prompt on 3 chunks."""
import json, re, sys
from pathlib import Path

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
sys.path.insert(0, r"C:\Users\Administrator\Knowledge Delivery OS 0.0.1")
from kdo.commands.label import load_tag_registry, flatten_dimensions, llm_label_chunk
from kdo.llm import LLMConfig

all_dims = flatten_dimensions(load_tag_registry(VAULT))
CORE = ["chunk_type", "method_family", "audience", "perspective"]
core_dims = {k: v for k, v in all_dims.items() if k in CORE}

cfg = LLMConfig.from_yaml()

tests = [
    ("偏差定义", "偏差（Bias）是系统性倾向，总是往同一方向偏。噪声（Noise）是随机波动，不同人/不同时刻往不同方向偏。偏差类比：枪靶总是偏右上方。噪声类比：枪靶散布很大但中心是对的。"),
    ("Klein攻击", "Gary Klein（Sources of Power作者，自然决策理论创始人）基于数十年对消防员、急救医生、军事指挥官的田野观察，对决策卫生提出根本性质疑。消防指挥官在秒级决策窗口中的直觉判断，事后分析往往优于耗时做效用计算的结果。"),
    ("五步法procedure", "核心操作：把这个项目能成吗拆成市场规模→竞争强度→团队能力→资金需求→执行风险五个子判断。具体做法：1. 列出决策涉及的所有维度（≥3个）2. 每个维度给一个独立评分（1-10）3. 禁止在分解前就给出整体判断。"),
]

for name, text in tests:
    print("--- {} ---".format(name))
    print("  text: {}...".format(text[:60]))
    decisions = llm_label_chunk(text, core_dims, config=cfg)
    if decisions:
        for d in decisions:
            print("  {}={} (conf={:.2f})".format(d["dimension"], d.get("value","?"), d.get("confidence",0)))
    else:
        print("  EMPTY")
    print()
