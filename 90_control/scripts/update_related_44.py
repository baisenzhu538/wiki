import re
from pathlib import Path

VAULT = Path('30_wiki')
UPDATED_AT = '2026-07-02'

NEW_CARDS = {
    'framework-yitang-scientific-sales-five-step': {
        'path': VAULT/'frameworks'/'framework-yitang-scientific-sales-five-step.md',
        'add': ['tool-yitang-customer-segmentation-4step','tool-yitang-value-proposition-4step','tool-yitang-sales-process-decomposition','tool-yitang-sales-performance-management','framework-yitang-sales-incentive-6d','tool-yitang-sales-toolkit-radar','dk-yitang-sales-common-pitfalls','case-yitang-sales-transformation-jubensha-saas','case-yitang-sales-transformation-meirongyuan','case-yitang-sales-transformation-tuliaogongsi','tool-opc-sales-dialogue-assistant'],
    },
    'tool-yitang-customer-segmentation-4step': {
        'path': VAULT/'tools'/'tool-yitang-customer-segmentation-4step.md',
        'add': ['framework-yitang-scientific-sales-five-step','tool-yitang-value-proposition-4step','tool-yitang-sales-process-decomposition','tool-yitang-sales-performance-management','framework-yitang-sales-incentive-6d','tool-yitang-sales-toolkit-radar','dk-yitang-sales-common-pitfalls','case-yitang-sales-transformation-tuliaogongsi','tool-opc-sales-dialogue-assistant'],
    },
    'tool-yitang-value-proposition-4step': {
        'path': VAULT/'tools'/'tool-yitang-value-proposition-4step.md',
        'add': ['framework-yitang-scientific-sales-five-step','tool-yitang-customer-segmentation-4step','tool-yitang-sales-process-decomposition','tool-yitang-sales-performance-management','framework-yitang-sales-incentive-6d','tool-yitang-sales-toolkit-radar','dk-yitang-sales-common-pitfalls','case-yitang-sales-transformation-jubensha-saas','tool-opc-sales-dialogue-assistant'],
    },
    'tool-yitang-sales-process-decomposition': {
        'path': VAULT/'tools'/'tool-yitang-sales-process-decomposition.md',
        'add': ['framework-yitang-scientific-sales-five-step','tool-yitang-customer-segmentation-4step','tool-yitang-value-proposition-4step','tool-yitang-sales-performance-management','framework-yitang-sales-incentive-6d','tool-yitang-sales-toolkit-radar','dk-yitang-sales-common-pitfalls','case-yitang-sales-transformation-jubensha-saas','case-yitang-sales-transformation-meirongyuan','tool-opc-sales-dialogue-assistant'],
    },
    'tool-yitang-sales-performance-management': {
        'path': VAULT/'tools'/'tool-yitang-sales-performance-management.md',
        'add': ['framework-yitang-scientific-sales-five-step','tool-yitang-customer-segmentation-4step','tool-yitang-value-proposition-4step','tool-yitang-sales-process-decomposition','framework-yitang-sales-incentive-6d','tool-yitang-sales-toolkit-radar','dk-yitang-sales-common-pitfalls','case-yitang-sales-transformation-meirongyuan','case-yitang-sales-transformation-tuliaogongsi','tool-opc-sales-dialogue-assistant'],
    },
    'framework-yitang-sales-incentive-6d': {
        'path': VAULT/'frameworks'/'framework-yitang-sales-incentive-6d.md',
        'add': ['framework-yitang-scientific-sales-five-step','tool-yitang-customer-segmentation-4step','tool-yitang-value-proposition-4step','tool-yitang-sales-process-decomposition','tool-yitang-sales-performance-management','tool-yitang-sales-toolkit-radar','dk-yitang-sales-common-pitfalls','case-yitang-sales-transformation-meirongyuan','tool-opc-sales-dialogue-assistant'],
    },
    'tool-yitang-sales-toolkit-radar': {
        'path': VAULT/'tools'/'tool-yitang-sales-toolkit-radar.md',
        'add': ['framework-yitang-scientific-sales-five-step','tool-yitang-customer-segmentation-4step','tool-yitang-value-proposition-4step','tool-yitang-sales-process-decomposition','tool-yitang-sales-performance-management','framework-yitang-sales-incentive-6d','dk-yitang-sales-common-pitfalls','case-yitang-sales-transformation-jubensha-saas','tool-opc-sales-dialogue-assistant'],
    },
    'dk-yitang-sales-common-pitfalls': {
        'path': VAULT/'dark-knowledges'/'dk-yitang-sales-common-pitfalls.md',
        'add': ['framework-yitang-scientific-sales-five-step','tool-yitang-customer-segmentation-4step','tool-yitang-value-proposition-4step','tool-yitang-sales-process-decomposition','tool-yitang-sales-performance-management','framework-yitang-sales-incentive-6d','tool-yitang-sales-toolkit-radar','case-yitang-sales-transformation-jubensha-saas','case-yitang-sales-transformation-meirongyuan','case-yitang-sales-transformation-tuliaogongsi','tool-opc-sales-dialogue-assistant','master-decision-hygiene'],
    },
    'case-yitang-sales-transformation-jubensha-saas': {
        'path': VAULT/'cases'/'case-yitang-sales-transformation-jubensha-saas.md',
        'add': ['framework-yitang-scientific-sales-five-step','tool-yitang-customer-segmentation-4step','tool-yitang-value-proposition-4step','tool-yitang-sales-process-decomposition','tool-yitang-sales-performance-management','framework-yitang-sales-incentive-6d','tool-yitang-sales-toolkit-radar','dk-yitang-sales-common-pitfalls','tool-opc-sales-dialogue-assistant'],
    },
    'case-yitang-sales-transformation-meirongyuan': {
        'path': VAULT/'cases'/'case-yitang-sales-transformation-meirongyuan.md',
        'add': ['framework-yitang-scientific-sales-five-step','tool-yitang-sales-process-decomposition','tool-yitang-sales-performance-management','framework-yitang-sales-incentive-6d','tool-yitang-sales-toolkit-radar','dk-yitang-sales-common-pitfalls','tool-opc-sales-dialogue-assistant'],
    },
    'case-yitang-sales-transformation-tuliaogongsi': {
        'path': VAULT/'cases'/'case-yitang-sales-transformation-tuliaogongsi.md',
        'add': ['framework-yitang-scientific-sales-five-step','tool-yitang-customer-segmentation-4step','tool-yitang-sales-performance-management','dk-yitang-sales-common-pitfalls','tool-opc-sales-dialogue-assistant'],
    },
    'tool-opc-sales-dialogue-assistant': {
        'path': VAULT/'tools'/'tool-opc-sales-dialogue-assistant.md',
        'add': ['case-yitang-sales-transformation-jubensha-saas','case-yitang-sales-transformation-meirongyuan','case-yitang-sales-transformation-tuliaogongsi'],
    },
}

EXISTING_MAPPING = {
    'yt-five-step-method-complete.md': ['framework-yitang-scientific-sales-five-step'],
    'yitang-methodology-system.md': ['framework-yitang-scientific-sales-five-step'],
    'framework-一堂五步法-泛产品设计.md': ['framework-yitang-scientific-sales-five-step','tool-yitang-customer-segmentation-4step','tool-yitang-value-proposition-4step','tool-yitang-sales-process-decomposition','case-yitang-sales-transformation-jubensha-saas','case-yitang-sales-transformation-meirongyuan','case-yitang-sales-transformation-tuliaogongsi'],
    'framework-yitang-channel-exploration-4step.md': ['framework-yitang-scientific-sales-five-step','tool-yitang-sales-process-decomposition','case-yitang-sales-transformation-jubensha-saas'],
    'tool-strategy-value-proposition.md': ['tool-yitang-value-proposition-4step','framework-yitang-scientific-sales-five-step'],
    'framework-demand-validation-pipeline.md': ['tool-yitang-customer-segmentation-4step','tool-yitang-value-proposition-4step'],
    'concept-一堂-hypothesis-driven-business-methodology.md': ['tool-yitang-customer-segmentation-4step','tool-yitang-value-proposition-4step','framework-yitang-scientific-sales-five-step'],
    'yt-panproduct-aesthetic-pool.md': ['tool-yitang-value-proposition-4step','tool-yitang-sales-toolkit-radar'],
    'yt-panproduct-aesthetic-modeling.md': ['tool-yitang-value-proposition-4step','tool-yitang-sales-toolkit-radar'],
    'framework-brand-three-degree.md': ['tool-yitang-value-proposition-4step'],
    'yt-business-formula-parameter-iceberg.md': ['tool-yitang-sales-process-decomposition','tool-yitang-sales-performance-management'],
    'tool-iceberg-triangle-modeling.md': ['tool-yitang-sales-process-decomposition','tool-yitang-sales-performance-management'],
    'yt-unit-model-overview.md': ['framework-yitang-scientific-sales-five-step','tool-yitang-sales-performance-management'],
    'yt-management-goal-management.md': ['tool-yitang-sales-performance-management','framework-yitang-sales-incentive-6d'],
    'yt-business-formula-six-level-logic.md': ['tool-yitang-sales-performance-management'],
    'framework-yitang-nine-layer-deep-dig.md': ['tool-yitang-sales-performance-management','case-yitang-sales-transformation-tuliaogongsi'],
    'framework-yitang-deliberate-practice-1plus4.md': ['framework-yitang-sales-incentive-6d','tool-yitang-sales-toolkit-radar'],
    'yt-personal-deliberate-practice.md': ['framework-yitang-sales-incentive-6d'],
    'tool-yitang-best-practice-as-golden-finger.md': ['tool-yitang-sales-toolkit-radar'],
    'tool-agent-research-swarm.md': ['tool-yitang-sales-toolkit-radar'],
    'case-yitang-sales-routine-deconstruction.md': ['framework-yitang-scientific-sales-five-step','tool-yitang-sales-process-decomposition'],
    'case-yitang-ai-painting-commercialization.md': ['framework-yitang-scientific-sales-five-step','tool-yitang-value-proposition-4step'],
    'opc-ai-sales-agent-architecture.md': ['tool-opc-sales-dialogue-assistant','framework-yitang-scientific-sales-five-step','tool-yitang-customer-segmentation-4step','tool-yitang-value-proposition-4step','tool-yitang-sales-process-decomposition','tool-yitang-sales-performance-management','framework-yitang-sales-incentive-6d','tool-yitang-sales-toolkit-radar','dk-yitang-sales-common-pitfalls'],
    'human-ai-collaboration-double-triangle.md': ['tool-opc-sales-dialogue-assistant'],
    'framework-lean-pivot-decision.md': ['case-yitang-sales-transformation-jubensha-saas'],
    'dk-yitang-channel-exploration-traps.md': ['framework-yitang-scientific-sales-five-step','tool-yitang-sales-process-decomposition','case-yitang-sales-transformation-meirongyuan'],
}

FM_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)

def find_file(name: str) -> Path:
    for sub in VAULT.rglob('*.md'):
        if sub.name == name:
            return sub
    raise FileNotFoundError(name)

def rewrite_related(fp: Path, to_add: list):
    text = fp.read_text(encoding='utf-8')
    m = FM_RE.match(text)
    if not m:
        print(f'SKIP no frontmatter: {fp}')
        return
    fm = m.group(1)
    rest = text[m.end():]

    fm = re.sub(r'^(updated_at:\s*).*$', rf'\g<1>{UPDATED_AT}', fm, flags=re.MULTILINE)
    if 'updated_at:' not in fm:
        fm += f'\nupdated_at: {UPDATED_AT}'

    existing = set()
    related_match = re.search(r'^related:\s*(.*?)(?=\n\w|\n---|\Z)', fm, re.DOTALL | re.MULTILINE)
    if related_match and related_match.group(1).strip() not in ('null', '~', ''):
        existing = set(re.findall(r'\[\[([^\]]+)\]\]', related_match.group(1)))

    combined = list(existing) + [cid for cid in to_add if cid not in existing]
    new_related = 'related:\n' + '\n'.join([f'  - "[[{cid}]]"' for cid in combined])
    if related_match:
        fm = fm[:related_match.start()] + new_related + fm[related_match.end():]
    else:
        fm += '\n' + new_related

    new_text = '---\n' + fm.rstrip() + '\n---\n' + rest
    fp.write_text(new_text, encoding='utf-8')
    print(f'UPDATED: {fp} related={len(combined)}')

for cid, info in NEW_CARDS.items():
    rewrite_related(info['path'], info['add'])

for fname, to_add in EXISTING_MAPPING.items():
    fp = find_file(fname)
    rewrite_related(fp, to_add)
