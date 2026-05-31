"""Debug LLM labeling prompt."""
import json, re, sys
sys.path.insert(0, r"C:\Users\Administrator\Knowledge Delivery OS 0.0.1")
from kdo.llm import LLMConfig, chat

cfg = LLMConfig.from_yaml()

# Simplified prompt — just 5 candidates
prompt = """You are a labeler. Given a text chunk and candidate labels, decide APPLY or REJECT for each. Return ONLY a JSON array.

Chunk: 偏差是系统性倾向，总是往同一方向偏。噪声是随机波动。

Candidates:
[
  {"dimension": "chunk_type", "value": "definition", "includes": "term definition, concept explanation", "excludes": "case studies"},
  {"dimension": "chunk_type", "value": "claim", "includes": "falsifiable knowledge claim", "excludes": "pure descriptive narrative"},
  {"dimension": "method_family", "value": "thinking-tool", "includes": "cognitive model, mental framework", "excludes": "concrete operational tools"},
  {"dimension": "audience", "value": "general", "includes": "general audience, all levels", "excludes": "specialized content"},
  {"dimension": "confidence", "value": "0.90", "includes": "multi-source verified, peer consensus", "excludes": "single-source claims"}
]

Output format: [{"dimension": "...", "value": "...", "decision": "APPLY|REJECT", "confidence": 0.XX, "reasoning": "..."}]"""

try:
    response = chat([{"role": "user", "content": prompt}], config=cfg, temperature=0.1)
    print(f"RAW RESPONSE ({len(response)} chars):")
    print(response)
    print()
    # Try to extract
    json_match = re.search(r"\[.*\]", response, re.DOTALL)
    if json_match:
        parsed = json.loads(json_match.group(0))
        print(f"PARSED: {len(parsed)} decisions")
        for d in parsed:
            print(f"  {d}")
    else:
        print("No JSON array found in response!")
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
