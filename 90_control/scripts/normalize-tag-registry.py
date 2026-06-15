# -*- coding: utf-8 -*-
"""Normalize tag-registry.yaml dimension keys to match actual tag usage (#dimension/value)."""
import yaml
from pathlib import Path

REGISTRY = Path('90_control/tag-registry.yaml')

with open(REGISTRY, 'r', encoding='utf-8') as fh:
    registry = yaml.safe_load(fh)

# Rename dimension keys to kebab-case to match actual tags like #chunk-type/claim
rename_map = {
    'chunk_type': 'chunk-type',
    'method_family': 'method',
    'content_format': 'content-format',
    'source_context_type': 'source-context-type',
    'data_generation': 'data-generation',
    'error_root': 'error-root',
    'value_tier': 'value-tier',
    'usage_depth': 'usage-depth',
    'prerequisite_knowledge': 'prerequisite-knowledge',
}

new_dimensions = {}
for old_key, spec in registry['dimensions'].items():
    new_key = rename_map.get(old_key, old_key)
    new_dimensions[new_key] = spec

# Add dimensions observed in actual usage but missing from registry
new_dimensions['confidence'] = {
    'group': 'quality',
    'layer': 'chunk',
    'activation': 'conditional',
    'labeling': 'auto_plus_manual',
    'description': 'Confidence level or verification state of the claim.',
    'values': [
        {'value': '0.90', 'includes': 'multi-source verified, strong empirical evidence'},
        {'value': '0.70', 'includes': 'single strong source, expert personal experience'},
        {'value': '0.50', 'includes': 'single source with partial counterexamples, plausible but unverified'},
        {'value': '0.30', 'includes': 'hypothesis, speculation, untested conjecture'},
        {'value': 'null', 'includes': 'pure factual statement without judgment'},
        {'value': 'draft', 'includes': 'preliminary claim, not yet verified'},
        {'value': 'source-cited', 'includes': 'claim backed by explicit source citation'},
        {'value': 'verified-by-case', 'includes': 'claim confirmed by real-world case'},
        {'value': 'verified-by-test', 'includes': 'claim confirmed by test or experiment'},
    ],
}

new_dimensions['scene'] = {
    'group': 'retrieval',
    'layer': 'card',
    'activation': 'conditional',
    'labeling': 'manual',
    'description': 'Usage scene or workflow context where this card is most relevant.',
    'values': [
        {'value': 'agent-infrastructure', 'includes': 'AI agent infrastructure, skill registry, tool use'},
        {'value': 'agent-infrastructure/discovery-chain', 'includes': 'agent discovery chain workflow'},
        {'value': 'agent-infrastructure/skill-registry', 'includes': 'skill registry design and management'},
        {'value': 'ai-collaboration', 'includes': 'human-AI collaboration workflows'},
        {'value': 'ai-collaboration/pdca-execution', 'includes': 'PDCA execution with AI assistance'},
        {'value': 'ai-collaboration/problem-validation', 'includes': 'problem validation using AI'},
        {'value': 'ai-collaboration/prompt-engineering', 'includes': 'prompt engineering workflows'},
        {'value': 'ai-collaboration/skill-market', 'includes': 'AI skill marketplace'},
        {'value': 'ai-collaboration/workspace-design', 'includes': 'AI collaboration workspace design'},
        {'value': 'business-analysis', 'includes': 'business analysis and metrics'},
        {'value': 'business-analysis/conversion-rate', 'includes': 'conversion rate analysis'},
        {'value': 'communication', 'includes': 'communication and messaging'},
        {'value': 'consulting', 'includes': 'consulting and advisory'},
        {'value': 'diagnosis', 'includes': 'diagnostic assessment'},
        {'value': 'entrepreneurship', 'includes': 'startup and entrepreneurship'},
        {'value': 'hardware-debugging', 'includes': 'hardware debugging and prototyping'},
        {'value': 'hardware-debugging/prototyping', 'includes': 'hardware prototyping'},
        {'value': 'knowledge-management', 'includes': 'knowledge management and PKM'},
        {'value': 'knowledge-management/case-library', 'includes': 'case library management'},
        {'value': 'knowledge-management/tagging', 'includes': 'tagging and taxonomy'},
        {'value': 'learning-methodology', 'includes': 'learning methods and deliberate practice'},
        {'value': 'learning-methodology/deliberate-practice', 'includes': 'deliberate practice'},
        {'value': 'learning-methodology/mental-models', 'includes': 'mental model building'},
        {'value': 'note-taking', 'includes': 'note taking and capture'},
        {'value': 'note-taking/live-field', 'includes': 'live field notes'},
        {'value': 'note-taking/training-plan', 'includes': 'training plan notes'},
        {'value': 'presentation', 'includes': 'presentation and pitching'},
        {'value': 'product-design/design-freeze', 'includes': 'design freeze process'},
        {'value': 'product-design/focus-workbench', 'includes': 'focus workbench design'},
        {'value': 'relationship-management', 'includes': 'relationship and stakeholder management'},
        {'value': 'skill-engineering', 'includes': 'skill engineering and course conversion'},
        {'value': 'skill-engineering/course-to-skill', 'includes': 'course to skill conversion'},
        {'value': 'skill-engineering/eval-testing', 'includes': 'skill evaluation testing'},
        {'value': 'skill-engineering/manifest-design', 'includes': 'skill manifest design'},
        {'value': 'skill-engineering/publish-deploy', 'includes': 'skill publish and deploy'},
        {'value': 'team-management', 'includes': 'team and people management'},
    ],
}

new_dimensions['problem'] = {
    'group': 'retrieval',
    'layer': 'card',
    'activation': 'conditional',
    'labeling': 'manual',
    'description': 'Problem domain this card addresses.',
    'values': [
        {'value': 'ai-workflow', 'includes': 'AI workflow integration problems'},
        {'value': 'knowledge-management', 'includes': 'knowledge management problems'},
        {'value': 'org-incentives', 'includes': 'organizational incentive problems'},
        {'value': 'org-learning', 'includes': 'organizational learning problems'},
        {'value': 'reporting', 'includes': 'reporting and status update problems'},
    ],
}

new_dimensions['source_type'] = {
    'group': 'perspective',
    'layer': 'card',
    'activation': 'conditional',
    'labeling': 'manual',
    'description': 'Source diversity or type for this card.',
    'values': [
        {'value': 'diverse', 'includes': 'multiple diverse sources'},
    ],
}

# Update domain dimension to include observed values
domain_values = new_dimensions['domain']['values']
domain_value_names = {v['value'] for v in domain_values}
extra_domains = [
    ('agent-infrastructure', 'AI agent infrastructure and tooling', 'general software'),
    ('ai', 'general artificial intelligence', 'specific AI products'),
    ('electronics', 'electronics and hardware', 'general engineering'),
    ('knowledge-management', 'knowledge management as a domain', 'general productivity'),
    ('prompt-engineering', 'prompt engineering as a domain', 'general AI usage'),
    ('skill-engineering', 'skill engineering and course conversion', 'general education'),
]
for value, includes, excludes in extra_domains:
    if value not in domain_value_names:
        domain_values.append({'value': value, 'includes': includes, 'excludes': excludes})

# Update method dimension values to include observed values
method_values = new_dimensions['method']['values']
method_value_names = {v['value'] for v in method_values}
extra_methods = [
    ('ai-collaboration', 'human-AI collaboration workflow, AI pairing', 'pure prompt technique'),
    ('checklist', 'checklist method and verification list', 'free-form prose'),
    ('course-design', 'curriculum and course design methodology', 'learning method itself'),
    ('critical-thinking', 'critical thinking and skepticism techniques', 'general thinking'),
    ('decision-quality', 'decision quality assessment', 'general decision making'),
    ('execution-management', 'execution and delivery management', 'strategic planning'),
    ('essence-modeling', 'essence and abstract modeling', 'concrete modeling'),
    ('logical-rigor', 'logical rigor and formal reasoning', 'casual reasoning'),
    ('model-validation', 'model validation methodology', 'general evaluation'),
    ('project-management', 'project management methods', 'execution methods'),
    ('retrospective', 'retrospective and review methods', 'general meeting'),
    ('sop', 'standard operating procedure creation', 'general execution'),
    ('structure', 'structural thinking and organization', 'content format'),
    ('visual-design', 'visual design methodology', 'UI development'),
]
for value, includes, excludes in extra_methods:
    if value not in method_value_names:
        method_values.append({'value': value, 'includes': includes, 'excludes': excludes})

# Update activation_rules references
for rule_name, rule in registry['activation_rules'].items():
    rule['dimensions'] = [rename_map.get(d, d) for d in rule['dimensions']]

# Update chunk_type_triggers references (key rename)
old_triggers = registry.pop('chunk_type_triggers', {})
new_triggers = {}
for key, val in old_triggers.items():
    new_key = rename_map.get(key, key)
    new_triggers[new_key] = {k: [rename_map.get(d, d) for d in v] for k, v in val.items()}
registry['chunk-type-triggers'] = new_triggers

# Also rename inference_map tag references (method_family -> method)
inference_map = registry.get('inference_map', {})
new_inference_map = {}
for key, tags in inference_map.items():
    new_tags = [t.replace('#method_family/', '#method/').replace('#quality/ocr-card', '#data-generation/ocr-card') for t in tags]
    new_inference_map[key] = new_tags
registry['inference_map'] = new_inference_map

registry['dimensions'] = new_dimensions
registry['version'] = '1.3'
registry['updated_at'] = '2026-06-16'

with open(REGISTRY, 'w', encoding='utf-8') as fh:
    yaml.dump(registry, fh, default_flow_style=False, allow_unicode=True, sort_keys=False)

print(f'Updated {REGISTRY} to version {registry["version"]}')
print(f'Dimensions: {len(registry["dimensions"])}')
