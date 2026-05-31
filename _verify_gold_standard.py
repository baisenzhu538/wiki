"""Verify auto_label accuracy against Gold Standard (15 chunks)."""
import json
import sys
sys.path.insert(0, r'C:\Users\Administrator\Knowledge Delivery OS 0.0.1')

from pathlib import Path
from kdo.commands.label import auto_label_chunk, load_tag_registry, flatten_dimensions
from kdo.llm import LLMConfig

VAULT = Path(r'C:\Users\Administrator\Desktop\wiki')
GOLD_FILE = VAULT / '30_wiki/decisions/gold-standard-manual-labels.md'
registry = load_tag_registry(VAULT)
cfg = LLMConfig.from_yaml()
print(f'LLM configured: {cfg.is_configured()}', file=sys.stderr)

def parse_gold() -> list[dict]:
    """Parse Gold Standard file into list of {text, labels}."""
    text = GOLD_FILE.read_text('utf-8')
    chunks = []
    current = None
    in_labels = False
    for line in text.split('\n'):
        if line.startswith('| **来源卡片**'):
            if current:
                chunks.append(current)
            current = {'text': '', 'labels': {}}
            in_labels = False
        elif line.startswith('| **chunk 内容**'):
            current['text'] = line.split('| **chunk 内容** |')[1].strip().rstrip(' |')
            in_labels = False
        elif line.startswith('| **维度** | **标签值** | **理由**'):
            in_labels = True
            continue
        elif in_labels and line.startswith('|') and current:
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) >= 2:
                dim = parts[0].strip('`').strip()
                val = parts[1].strip('`').strip()
                if dim and val and dim != '维度':
                    current['labels'][dim] = val
        elif in_labels and not line.startswith('|'):
            in_labels = False
    if current:
        chunks.append(current)
    return chunks

gold = parse_gold()
print(f'Gold Standard: {len(gold)} chunks parsed', file=sys.stderr)

total_dims = 0
total_matches = 0
chunk_results = []

for i, g in enumerate(gold):
    text = g['text'][:2000]
    if not text:
        chunk_results.append({'id': i+1, 'error': 'empty text', 'accuracy': 0.0})
        continue

    result = auto_label_chunk(text, registry=registry, llm_config=cfg, top_k=10)
    auto_labels = {}
    for lbl in result.get('result', {}).get('labels', []):
        auto_labels[lbl['dimension']] = lbl['value']

    chunk_dims = 0
    chunk_matches = 0
    details = []
    for dim, gold_val in g['labels'].items():
        chunk_dims += 1
        auto_val = auto_labels.get(dim, '<missing>')
        if auto_val == gold_val:
            chunk_matches += 1
            details.append(f'  ✅ {dim}: {gold_val}')
        else:
            details.append(f'  ❌ {dim}: gold={gold_val} auto={auto_val}')

    acc = chunk_matches / chunk_dims if chunk_dims else 0
    total_dims += chunk_dims
    total_matches += chunk_matches
    chunk_results.append({
        'id': i+1,
        'dims': chunk_dims,
        'matches': chunk_matches,
        'accuracy': round(acc, 3),
        'details': details,
    })
    print(f'\n--- Chunk {i+1} (acc={acc:.1%}) ---')
    for d in details:
        print(d)

overall = total_matches / total_dims if total_dims else 0
print(f'\n{"="*50}')
print(f'Overall accuracy: {total_matches}/{total_dims} = {overall:.1%}')
print(f'{"="*50}')

summary_path = VAULT / '60_feedback/data-quality/label-results/gold-standard-verify.json'
summary_path.write_text(json.dumps({
    'total_chunks': len(gold),
    'total_dimensions': total_dims,
    'total_matches': total_matches,
    'accuracy': round(overall, 4),
    'chunks': chunk_results,
}, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'\nFull results -> {summary_path}')
