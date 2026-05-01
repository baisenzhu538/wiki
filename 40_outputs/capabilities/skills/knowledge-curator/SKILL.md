---
title: Knowledge Curator Skill
type: capability
subtype: skill
status: ready
target_user: AI agent or human operating a KDO workspace
delivery_channel: local
source_refs: []
wiki_refs: []
definition_of_done:
  - task boundary explicit
  - inputs and outputs explicit
  - tool permissions declared
  - eval cases present
  - feedback path declared
artifact_id: kdo_builtin_knowledge_curator_v1
created_at: 2026-04-26T18:06:07+00:00
updated_at: 2026-04-26T18:06:07+00:00
origin: builtin
---

# Knowledge Curator Skill

## Capability Type

skill

## Mission

Systematically transform raw inputs into durable, source-traceable knowledge.
One invocation handles: capture → ingest → wiki skeleton enrichment → lint verification.

The curator's job is not to create opinions — it is to faithfully compile
what sources actually say, surface gaps, and flag conflicts rather than resolve them.

## Target User

AI agent or human collaborator operating a KDO workspace.

## Inputs

- `input`: text snippet, URL, local file path, or path to a chat export file
- `kind` (optional): `text | url | file | ai-chat | meeting | transcript | other` — defaults to auto-detection
- `title` (optional): human title for the captured item
- `trust_level` (optional): `low | medium | high | unknown` — default `unknown`
- `freshness` (optional): `volatile | current | stable | unknown` — default `unknown`
- `rights` (optional): `private | public | licensed | unknown` — default `unknown`
- `enrich_wiki` (optional, bool): if true, attempt to fill wiki placeholders after ingest

## Outputs

- Captured file in `00_inbox/<category>/`
- Raw source in `10_raw/sources/`
- Wiki skeleton in `30_wiki/concepts/<slug>.md` — Summary and Source Refs populated;
  Reusable Knowledge and Open Questions sections enriched when `enrich_wiki=true`
- Updated `.kdo/state.json` (source record, ingested_inbox_files)
- Updated `90_control/source-registry.yaml`
- Updated `30_wiki/index.md` and `30_wiki/log.md`

## Tool Permissions

| Tool | Allowed operations | Requires approval |
| --- | --- | --- |
| `kdo capture` | Capture any input kind | No |
| `kdo fetch-url` | Fetch http/https/data URLs (private-network IPs blocked) | No |
| `kdo import-chat` | Import text/JSON chat exports | No |
| `kdo ingest` | Process all new inbox items | No |
| `kdo lint` | Check workspace health | No |
| `kdo status` | Read workspace counters | No |
| Read `30_wiki/concepts/` | Inspect existing wiki pages | No |
| Write `30_wiki/concepts/*.md` | Enrich wiki skeleton sections | Yes — structural changes require approval |
| Write `30_wiki/contradictions.md` | Record source conflicts | Yes — append only, no deletes |

## Procedure

1. **Determine capture strategy.**
   - If input is a URL → use `kdo fetch-url <url> --trust-level <level>`.
   - If input is a chat export file → use `kdo import-chat <path> --title <title>`.
   - Otherwise → use `kdo capture "<input>" --title "<title>" --kind <kind>`.

2. **Run ingest.**
   ```
   kdo ingest
   ```
   Note the source id(s) and wiki page path(s) printed.

3. **Inspect the generated wiki skeleton** at `30_wiki/concepts/<slug>.md`.
   - Read the Summary section — verify it accurately reflects the source.
   - Check Source Refs — confirm the correct source_id is linked.

4. **Enrich wiki page** (if `enrich_wiki=true` or source is high-trust and non-trivial):
   - Fill `## Reusable Knowledge`: extract stable claims, concepts, and patterns that will
     outlast the source context. Keep each point falsifiable.
   - Fill `## Open Questions`: surface gaps, unknowns, and next-step hypotheses.
   - Fill `## Output Opportunities`: list concrete artifacts this knowledge could become.
   - **Do not remove or rewrite the Summary section** — it mirrors the source.
   - **Do not invent claims** — stay within what the source says.
   - If the source contradicts an existing wiki page, append to `30_wiki/contradictions.md`
     rather than silently merging.

5. **Run lint.**
   ```
   kdo lint
   ```
   Resolve any errors before reporting completion.

6. **Report outcome.**
   State: source_id created, wiki page path, enrichment status, any conflicts flagged.

## Failure Modes

| Condition | Response |
| --- | --- |
| Input is unreachable URL | Capture as reference with `trust_level=low`; note in wiki Open Questions |
| Source conflicts with existing wiki claim | Append to `30_wiki/contradictions.md`; do not merge |
| Source has very low signal density | Capture and ingest, mark wiki `status: stub`; skip enrichment |
| Lint fails after ingest | Stop, report the specific lint error; do not proceed to enrichment |
| Source rights are `private` | Set wiki `status: draft`, do not surface in public output paths |

## Eval Cases

### Case 1 — URL with clear factual content

Input:
```
kdo fetch-url "https://example.com/article" --trust-level medium
kdo ingest
```

Expected:
- Inbox file created in `00_inbox/links/`
- Raw source created in `10_raw/sources/`
- Wiki skeleton has non-empty Summary extracted from page text
- `kdo lint` returns 0

### Case 2 — AI chat import with strategic insight

Input:
```
kdo import-chat ./conversation.json --title "Strategy Discussion" --trust-level high
kdo ingest
```

Expected:
- Chat ingested to `00_inbox/ai-chats/`
- Wiki skeleton in `30_wiki/concepts/strategy-discussion.md`
- After enrichment: Reusable Knowledge has ≥ 2 bullet points extracted from the conversation
- `kdo lint` returns 0

### Case 3 — Source conflict

Input: capture of a claim that contradicts an existing wiki page.

Expected:
- New source ingested normally
- `30_wiki/contradictions.md` has a new row with both source IDs and a description of the conflict
- Existing wiki page is NOT modified

## Feedback Path

- `60_feedback/corrections/` — factual errors in wiki enrichment
- `60_feedback/issues/` — procedure failures or unexpected ingest behavior
- `60_feedback/eval-results/` — eval case failures recorded by `kdo eval`
