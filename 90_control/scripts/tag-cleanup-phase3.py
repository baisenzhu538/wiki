# -*- coding: utf-8 -*-
"""Phase 3: conservative mapping of flat tags to dimension tags."""
import os, yaml
from pathlib import Path
from collections import Counter

base = '30_wiki'

mapping = {
    '#ai': ['#domain/ai'],
    '#saas': ['#domain/saas'],
    '#healthcare': ['#industry/healthcare'],
    '#consulting': ['#industry/consulting'],
    '#e-commerce': ['#industry/ecommerce'],
    '#dental': ['#industry/dental'],
    '#gym': ['#industry/fitness'],
    '#business-strategy': ['#method/decision-framework'],
    '#product-strategy': ['#method/decision-framework'],
    '#product-development': ['#method/product-design'],
    '#course-design': ['#method/course-design'],
    '#skill-engineering': ['#domain/skill-engineering'],
    '#skill-training': ['#method/learning-method'],
    '#reverse-engineering': ['#method/research-method'],
    '#formula': ['#content-format/formula'],
    '#critique': ['#chunk-type/critique'],
    '#concept': ['#chunk-type/definition'],
    '#insight': ['#chunk-type/synthesis'],
    '#logic': ['#method/thinking-tool'],
    '#statistics': ['#method/research-method'],
    '#system': ['#domain/master'],
    '#organization': ['#method/management-tool'],
    '#evaluation': ['#method/evaluation-method'],
    '#sales-analysis': ['#method/research-method'],
    '#vendor-assessment': ['#method/evaluation-method'],
    '#self-assessment': ['#method/evaluation-method'],
    '#decision-quality': ['#method/decision-framework'],
    '#cognitive-tool': ['#method/thinking-tool'],
    '#methodology': ['#method/thinking-tool'],
    '#meta-method': ['#method/thinking-tool'],
    '#lean-validation': ['#method/evaluation-method'],
    '#demand-validation': ['#method/evaluation-method'],
    '#offline-retail': ['#industry/local-service'],
    '#pitch': ['#method/communication-method'],
    '#selector': ['#method/decision-framework'],
    '#selection': ['#method/decision-framework'],
    '#priority': ['#method/decision-framework'],
    '#quadrant': ['#content-format/framework'],
    '#triangle': ['#content-format/framework'],
    '#binary': ['#method/thinking-tool'],
    '#n-factor': ['#method/evaluation-method'],
    '#parameters': ['#method/evaluation-method'],
    '#predictive': ['#method/thinking-tool'],
    '#signal-processing': ['#domain/ai-saas'],
    '#personal-map': ['#content-format/canvas'],
    '#tool-stack': ['#domain/ai-saas'],
    '#abstract-modeling': ['#method/modeling'],
    '#minimal-model': ['#method/modeling'],
    '#action-driven': ['#method/execution-method'],
    '#agent-standard': ['#domain/ai-saas'],
    '#ai-application': ['#domain/ai-saas'],
    '#ai-hackathon': ['#domain/ai-saas'],
    '#ai-methodology': ['#method/thinking-tool'],
    '#ai-skill': ['#domain/skill-engineering'],
    '#ai-skills': ['#domain/skill-engineering'],
    '#beverage': ['#industry/local-service'],
    '#catering': ['#industry/local-service'],
    '#catering-channel': ['#industry/local-service'],
    '#card-quality': ['#method/evaluation-method'],
    '#boundary/single-use-only': ['#chunk-type/boundary'],
    '#conflict': ['#chunk-type/question'],
    '#decision-support': ['#method/decision-framework'],
    '#knowledge-collision': ['#chunk-type/synthesis'],
    '#learning-methodology': ['#method/learning-method'],
    '#live-field': ['#scene/note-taking/live-field'],
    '#misjudgment': ['#chunk-type/error-data'],
    '#paradigms': ['#method/thinking-tool'],
    '#pipeline': ['#method/execution-method'],
    '#quantification': ['#method/evaluation-method'],
    '#sabc': ['#method/evaluation-method'],
    '#expert-consensus': ['#confidence/verified-by-case'],
    '#bias-detection': ['#method/evaluation-method'],
    '#complex-systems': ['#domain/master'],
    '#judgment': ['#method/decision-framework'],
}

changed = 0
mapped = 0
remaining = Counter()

for root, dirs, files in os.walk(base):
    for f in files:
        if not f.endswith('.md'):
            continue
        path = os.path.join(root, f)
        p = Path(path)
        with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
            text = fh.read()
        if not text.startswith('---\n'):
            continue
        end = text.find('\n---\n', 4)
        if end == -1:
            continue
        try:
            fm = yaml.safe_load(text[4:end])
            if not isinstance(fm, dict):
                continue
            old_tags = fm.get('tags', []) or []
            new_tags = []
            modified = False
            for t in old_tags:
                if t is None or str(t).strip() == '':
                    modified = True
                    continue
                s = str(t).strip()
                if s in mapping:
                    new_tags.extend(mapping[s])
                    mapped += 1
                    modified = True
                elif not s.startswith('#'):
                    modified = True
                else:
                    new_tags.append(s)
            if modified:
                seen = set()
                final = []
                for t in new_tags:
                    if t not in seen:
                        seen.add(t)
                        final.append(t)
                fm['tags'] = final
                new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False).strip()
                p.write_text('---\n' + new_fm + '\n---\n' + text[end+5:], encoding='utf-8')
                changed += 1
        except Exception as e:
            pass

# Re-scan remaining unmapped flat tags
with open('90_control/tag-registry.yaml', 'r', encoding='utf-8') as fh:
    registry = yaml.safe_load(fh)
allowed = set()
for dim, spec in registry.get('dimensions', {}).items():
    for v in spec.get('values', []):
        allowed.add(f'#{dim}/{v["value"]}')

for root, dirs, files in os.walk(base):
    for f in files:
        if not f.endswith('.md'):
            continue
        path = os.path.join(root, f)
        with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
            text = fh.read()
        if not text.startswith('---\n'):
            continue
        end = text.find('\n---\n', 4)
        if end == -1:
            continue
        try:
            fm = yaml.safe_load(text[4:end])
            if isinstance(fm, dict):
                for t in fm.get('tags', []) or []:
                    if t and str(t).startswith('#') and str(t) not in allowed and '/' not in str(t):
                        remaining[str(t)] += 1
        except:
            pass

print(f'Mapped flat tags in {changed} files, total mappings: {mapped}')
print(f'Remaining unmapped flat tags: {len(remaining)}')
for t, c in remaining.most_common():
    print(f'  {t}: {c}')
