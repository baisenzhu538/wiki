# Produce and Ship Flow

## Purpose

Structured pipeline for turning compiled wiki knowledge into a shipped,
feedback-ready artifact. Do not start this flow until the relevant topic
has at least one wiki page and one raw source.

## Trigger

When a topic has sufficient coverage in `30_wiki/concepts/` and you have
a clear target user and delivery channel in mind.

## Estimated Duration

1–4 hours depending on artifact complexity.

## Prerequisites

- Topic has ≥ 1 wiki page with non-empty Reusable Knowledge section
- Topic has ≥ 1 raw source in `10_raw/sources/`
- Delivery channel is known (website, github, newsletter, local, etc.)
- `kdo lint` passes

## Steps

### Step 1 — Verify knowledge coverage

```bash
kdo query "<topic>"
```

Expected: ≥ 2 results, at least one from `30_wiki/concepts/`.
If fewer results: run Daily Capture Flow first.

### Step 2 — Choose artifact type

| Intent | Type | Subtype |
| --- | --- | --- |
| Publish written content | content | article / tutorial / report |
| Ship working code | code | template / script / app |
| Package a repeatable task | capability | skill / workflow / playbook |
| Define an eval framework | capability | eval |

### Step 3 — Generate artifact skeleton

```bash
kdo produce <type>/<subtype>   --topic "<topic>"   --target-user "<target user description>"   --channel <channel>
```

Note the printed `artifact_id`.

### Step 4 — Get context brief

```bash
kdo brief --artifact-id <artifact_id>
```

Read the Local Context section fully before writing.

### Step 5 — Fill the artifact

Open the artifact file at the path printed by `kdo produce`:

| Artifact type | File path convention |
| --- | --- |
| content | `40_outputs/content/<subtype>/<artifact_id>-<slug>.md` |
| code | `40_outputs/code/<subtype>/<artifact_id>-<slug>/README.md` (wrapped directory) |
| capability | `40_outputs/capabilities/<subtype>/<artifact_id>-<slug>/SKILL.md` (wrapped directory) |

Replace all `TODO:` sections with actual content derived from the wiki and source context.
See the Delivery Producer Skill for type-specific guidance.

### Step 6 — Validate

```bash
kdo validate <artifact_id>
```

All checks must pass. Fix failures before proceeding.
Common failures and fixes:

| Check | Fix |
| --- | --- |
| `placeholders` | Replace remaining TODO sections |
| `source_refs` | Ensure artifact frontmatter has source_refs from ingest chain |
| `wiki_refs` | Ensure artifact frontmatter has wiki_refs pointing to concept pages |
| `feedback_path` | Ensure `## Feedback Path` section has specific `60_feedback/` sub-paths |

### Step 7 — Ship

```bash
kdo ship <artifact_id> --channel <channel> --url "<published url or release path>"
```

### Step 8 — Record initial feedback

```bash
kdo feedback "<observations from publishing>"   --kind comments   --artifact-id <artifact_id>
```

Minimum: one comment about the delivery experience or expected reception.

## Exit Criteria

- `kdo validate <artifact_id>` returns 0
- Delivery record exists in `50_delivery/published/`
- At least one feedback record linked to the artifact

## Related Skills

- `40_outputs/capabilities/skills/delivery-producer/SKILL.md`
- `40_outputs/capabilities/workflows/feedback-improve-flow.md`
