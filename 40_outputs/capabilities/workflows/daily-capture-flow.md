# Daily Capture Flow

## Purpose

Low-friction daily session for turning new inputs into durable knowledge.
Run at the start of each work session or whenever new inputs accumulate.

## Trigger

Manual start, or scheduled at the beginning of each work session.

## Estimated Duration

15–30 minutes for a typical day's inputs.

## Prerequisites

- KDO workspace initialized (`kdo init`)
- At least one new input to capture (URL, idea, chat, document)

## Steps

### Step 1 — Capture new inputs (5–15 min)

For each new input from the session:

```bash
# Text idea or insight
kdo capture "<your idea or note>" --title "<title>"

# URL to save and extract
kdo fetch-url "<url>" --trust-level medium --freshness current

# AI conversation export
kdo import-chat ./chat-export.json --title "<conversation topic>"

# Local file (PDF, document, notes)
kdo capture ./path/to/file.md --title "<file title>"
```

**Routing intent:** everything goes into `00_inbox/` — do not classify yet.

### Step 2 — Ingest (1–2 min)

```bash
kdo ingest
```

Review the output: note which source IDs and wiki pages were created.

### Step 3 — Review new wiki skeletons (5–10 min)

```bash
kdo status
```

For each new wiki page in `30_wiki/concepts/`:
- Is the Summary accurate?
- What are the most reusable claims?
- Are there output opportunities (content/code/capability)?

Optional: enrich with the Knowledge Curator Skill if high-value source.

### Step 4 — Health check (1 min)

```bash
kdo lint
```

Resolve any errors before ending the session.

### Step 5 — Record session snapshot

```bash
kdo status
```

Write down the printed source/artifact/inbox counts in `20_memory/project-continuity.md`
so the next session starts with accurate context.

## Exit Criteria

- All new inputs are captured and ingested
- `kdo lint` returns 0
- Wiki pages reviewed for immediate output opportunities

## Common Variations

- **Batch day (10+ inputs):** use `kdo ingest --limit 5` to process in batches
  and review incrementally
- **URL-heavy day:** use `kdo fetch-url` for each URL immediately as you encounter it;
  batch ingest at session end
- **Chat-heavy day:** export conversations to JSON first, then `kdo import-chat`
  for each high-value exchange

## Related Skills

- `40_outputs/capabilities/skills/knowledge-curator/SKILL.md`
- `40_outputs/capabilities/workflows/produce-and-ship-flow.md`
