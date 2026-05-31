"""Debug: check raw LLM response for a chunk that fails."""
import json, re, sys
from pathlib import Path

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
sys.path.insert(0, r"C:\Users\Administrator\Knowledge Delivery OS 0.0.1")
from kdo.commands.label import load_tag_registry, flatten_dimensions
from kdo.llm import LLMConfig, chat

cfg = LLMConfig.from_yaml()
all_dims = flatten_dimensions(load_tag_registry(VAULT))
CORE = ["chunk_type", "method_family", "audience", "perspective"]
core_dims = {k: v for k, v in all_dims.items() if k in CORE}

# Build the same prompt as llm_label_chunk
dim_desc = {}
valid_sets = {}
for dim_name, values in core_dims.items():
    options = []
    valid_vals = set()
    for v in values:
        val = v["value"]
        valid_vals.add(val)
        desc = v.get("includes", "")
        if desc:
            options.append("{}: {}".format(val, desc[:100]))
        else:
            options.append(val)
    dim_desc[dim_name] = options
    valid_sets[dim_name] = valid_vals

from kdo.commands.label import LABEL_PROMPT

# Test with chunk 3 (Klein critique — long text)
text = "Gary Klein（Sources of Power作者，自然决策理论创始人）基于数十年对消防员、急救医生、军事指挥官的田野观察，对决策卫生提出根本性质疑。消防指挥官在秒级决策窗口中的直觉判断，事后分析往往优于耗时做效用计算的结果。五步法的分解→外部→独立→聚合→延迟在火灾现场根本不适用——等走完五步，楼已经烧完了。Klein 发现专家的直觉不是随机猜测，而是基于数千小时经验形成的模式识别。"

prompt = LABEL_PROMPT.format(chunk=text)
print("Prompt length: {} chars, ~{} tokens".format(len(prompt), len(prompt)//3))

try:
    response = chat(
        [{"role": "user", "content": prompt}],
        config=cfg, temperature=0.05, max_tokens=512,
    )
    print("\nRAW RESPONSE ({} chars):".format(len(response)))
    print(response)
    print("\n---")
    # Try to extract JSON
    parsed = None
    fence_match = re.search(r"```(?:json)?\s*(\{[^`]+\})\s*```", response, re.DOTALL)
    if fence_match:
        print("Fence match:", fence_match.group(1)[:200])
        try: parsed = json.loads(fence_match.group(1))
        except json.JSONDecodeError as e: print("Fence parse error:", e)
    if parsed is None:
        for m in re.finditer(r"\{[^{}]*\}", response):
            try:
                parsed = json.loads(m.group(0))
                print("Regex match:", m.group(0))
                break
            except json.JSONDecodeError:
                continue
    if parsed:
        print("\nPARSED:", parsed)
    else:
        print("\nNO JSON FOUND")
except Exception as e:
    print("ERROR:", e)
    import traceback
    traceback.print_exc()
