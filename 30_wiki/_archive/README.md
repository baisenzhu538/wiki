# Card Archive

Deprecated and superseded cards moved here so they don't pollute quality gate metrics.

## Archive Process

1. Set `status: deprecated` or `status: superseded` in frontmatter
2. Set `superseded_by` field pointing to the replacement card ID(s)
3. Move the file to `30_wiki/_archive/`
4. Remove from `30_wiki/index.md` if present

## When NOT to archive

- Cards with `status: draft` that were never published → just delete
- Temporary/testing cards → just delete
- Cards that are still referenced by other cards → update references first
