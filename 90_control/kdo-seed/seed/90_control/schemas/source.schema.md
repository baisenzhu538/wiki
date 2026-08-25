# Source Schema

Machine-readable source records are mirrored in `.kdo/state.json`. This human-readable YAML file is append-only.

Required fields:

```yaml
- id: src_YYYYMMDD_xxxxxx
  title: string
  type: text | url | file | ai-chat | meeting | transcript | other
  location: path-or-url
  captured_at: ISO-8601 timestamp
  trust_level: low | medium | high | unknown
  freshness: volatile | current | stable | unknown
  rights: private | public | licensed | unknown
  related_wiki: []
  derived_outputs: []
```
