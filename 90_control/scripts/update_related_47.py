import re
from pathlib import Path

VAULT = Path('30_wiki')
UPDATED_AT = '2026-07-02'

AGENT_SPECS = [
    'tool-agent-spec-yitang-customer-segmentation',
    'tool-agent-spec-yitang-value-proposition',
    'tool-agent-spec-yitang-sales-process-tracker',
    'tool-agent-spec-yitang-sales-performance-monitor',
]

# Each agent-spec should link to the other three
NEW_CARD_LINKS = {cid: [other for other in AGENT_SPECS if other != cid] for cid in AGENT_SPECS}

# Existing cards that must link to all 4
EXISTING_LINKS = {
    VAULT/'personal-os'/'opc-ai-sales-agent-architecture.md': AGENT_SPECS,
    VAULT/'tools'/'tool-opc-sales-dialogue-assistant.md': AGENT_SPECS,
}

NEW_CARD_PATHS = {cid: VAULT/'tools'/f'{cid}.md' for cid in AGENT_SPECS}

FM_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)

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

for cid, links in NEW_CARD_LINKS.items():
    rewrite_related(NEW_CARD_PATHS[cid], links)

for fp, links in EXISTING_LINKS.items():
    rewrite_related(fp, links)
