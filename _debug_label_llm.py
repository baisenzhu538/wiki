"""Debug label pipeline with LLM."""
import sys
sys.path.insert(0, r'C:\Users\Administrator\Knowledge Delivery OS 0.0.1')

from kdo.commands.label import auto_label_chunk, load_tag_registry, flatten_dimensions
from kdo.llm import LLMConfig
from pathlib import Path

root = Path(r'C:\Users\Administrator\Desktop\wiki')
registry = load_tag_registry(root)
cfg = LLMConfig.from_yaml()
print(f'LLM configured: {cfg.is_configured()}')
print(f'Registry dims: {len(flatten_dimensions(registry))}')

result = auto_label_chunk(
    '偏差是系统性倾向，噪声是随机波动。金句：偏差是枪总打偏，噪声是枪到处乱飞。',
    registry=registry,
    llm_config=cfg,
    top_k=8
)
r = result.get('result', {})
print(f'Routing: {r.get("routing")}')
print(f'Labels ({r.get("label_count", 0)}):')
for lbl in r.get('labels', []):
    print(f'  {lbl["dimension"]}/{lbl["value"]} ({lbl.get("confidence", "?")})')
print(f'Summary: {r.get("summary")}')
decisions = result.get('decisions', [])
print(f'Decisions count: {len(decisions)}')
if decisions:
    for d in decisions[:3]:
        print(f'  {d.get("dimension")}/{d.get("value")}: {d.get("decision")} ({d.get("confidence")})')
