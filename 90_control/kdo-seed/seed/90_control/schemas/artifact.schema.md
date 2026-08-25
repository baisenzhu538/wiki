# Artifact Schema

Machine-readable artifact records are mirrored in `.kdo/state.json`. This human-readable YAML file is append-only.

Required fields:

```yaml
- artifact_id: art_YYYYMMDD_xxxxxx
  type: content | code | capability
  subtype: article | video | audio | tutorial | report | template | script | skill | agent | workflow | eval | playbook
  title: string
  target_user: string
  source_refs: []
  wiki_refs: []
  definition_of_done: []
  status: draft | review | shipped | deprecated
  delivery_channel: string
  feedback_source: string
  path: string
```
