# Cross-Tool Bridge Protocol

> **Input contract**: How external content (Feishu, Web, Notion, WeChat) flows into KDO.
> **Goal**: Zero-friction capture from any tool into `00_inbox/`, then `kdo ingest` handles the rest.

---

## Supported Input Channels

| Channel | Source Format | KDO Target | Transformer |
|---------|--------------|------------|-------------|
| **Feishu Docs** | `.docx` export or API markdown | `00_inbox/` → `10_raw/sources/` | `bridge/feishu.py` |
| **Web Articles** | HTML / Readability extraction | `00_inbox/links/` → `10_raw/web/` | `bridge/web.py` |
| **WeChat MP** | HTML / copy-paste markdown | `00_inbox/` → `10_raw/web/` | `bridge/wechat.py` |
| **Notion** | Markdown export | `00_inbox/` → `10_raw/sources/` | `bridge/notion.py` |
| **AI Chats** | Markdown transcript | `00_inbox/ai-chats/` → `10_raw/sources/` | `bridge/ai_chat.py` |
| **Screenshots** | PNG/JPG + OCR text | `00_inbox/screenshots/` → `10_raw/assets/` | `bridge/ocr.py` |
| **Voice Notes** | Audio + transcript | `00_inbox/voice-notes/` → `10_raw/transcripts/` | `bridge/transcribe.py` |

---

## Ingest Pipeline

```
External Tool
     │
     ▼
[Bridge Transformer]  ──→  Normalized Markdown + Metadata JSON
     │
     ▼
00_inbox/{<channel>}/
     │
     ▼
kdo ingest  ──→  10_raw/sources/ + source metadata
     │
     ▼
kdo enrich  ──→  30_wiki/concepts/ skeleton
```

---

## Normalized Markdown Format

All bridge transformers MUST output files in this structure:

```markdown
---
bridge_source: feishu | web | notion | wechat | ai-chat | voice | screenshot
bridge_id: <unique-id-from-source>
bridge_url: <original-url-if-applicable>
captured_at: "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ"
captured_by: <human-or-agent-name>
title: "Original Title"
author: "Original Author"
tags:
  - #auto-imported
---

# Original Title

<Clean Markdown Body>

---

## Bridge Metadata

- **Extraction method**: readability-api / docx-parser / ocr / whisper
- **Confidence**: high | medium | low
- **Raw storage**: `00_inbox/<channel>/<file-id>`
```

### Field Rules

| Field | Required | Notes |
|-------|----------|-------|
| `bridge_source` | ✅ | Must match enum above |
| `bridge_id` | ✅ | Unique within source system |
| `bridge_url` | ⚠️ | Required for web/WeChat/Notion; optional for voice/screenshots |
| `captured_at` | ✅ | ISO-8601 timestamp |
| `captured_by` | ✅ | Who initiated the capture |
| `title` | ✅ | Human-readable title |
| `author` | ❌ | Original content author |
| `tags` | ✅ | Always include `#auto-imported` |

---

## Per-Channel Specifications

### Feishu → KDO

```python
# bridge/feishu.py (pseudocode)
def transform(docx_path: Path) -> tuple[Path, Path]:
    """
    1. Unzip .docx
    2. Extract word/document.xml text
    3. Convert to Markdown (headings, lists, tables)
    4. Generate metadata JSON
    5. Output: 00_inbox/feishu/<slug>.md + .meta.json
    """
```

**Known Limitations**:
- Feishu tables → Markdown tables (lossy formatting)
- Images extracted to `00_inbox/feishu/assets/` with relative links
- Comments/annotations dropped (or stored in `.meta.json`)

### Web → KDO

```python
# bridge/web.py (pseudocode)
def transform(url: str, html: str) -> Path:
    """
    1. Readability extraction (article text only)
    2. Remove ads, nav, footer
    3. Convert to Markdown
    4. Archive raw HTML to 10_raw/web/<url-hash>.html
    5. Output: 00_inbox/links/<slug>.md
    """
```

**Anti-patterns**:
- ❌ Do NOT import entire webpage with navigation chrome
- ❌ Do NOT import paywalled content without rights check
- ✅ DO extract main article content only
- ✅ DO save raw HTML as archive (source of truth)

### AI Chat → KDO

```python
# bridge/ai_chat.py (pseudocode)
def transform(transcript_path: Path) -> Path:
    """
    1. Parse transcript format (Claude / ChatGPT / Kimi)
    2. Identify Q/A turns
    3. Summarize key insights in header
    4. Output: 00_inbox/ai-chats/<date-slug>.md
    """
```

**Required Header**:
```markdown
## Chat Summary

- **Platform**: Claude / ChatGPT / Kimi / etc.
- **Topic**: One-line summary
- **Key Insights**: 3-5 bullets
- **Action Items**: Any TODOs generated
```

---

## Quality Gates for Bridge Output

Before `kdo ingest` processes a bridged file:

- [ ] Title is meaningful (not "Untitled" or auto-generated hash)
- [ ] Body is not empty or whitespace-only
- [ ] `bridge_source` and `bridge_id` are present
- [ ] If `bridge_url` is present, URL is valid format
- [ ] No obvious garbled text (OCR confidence > medium)
- [ ] File size is reasonable (< 10MB for text)

If any gate fails → move to `00_inbox/.quarantine/` for human review.

---

## Conflict Resolution

| Scenario | Rule |
|----------|------|
| Same `bridge_id` re-imported | Overwrite if `captured_at` newer; otherwise skip |
| Same title, different `bridge_id` | Allow both; disambiguate with `(v2)` suffix |
| Content modified in KDO after ingest | Do NOT overwrite on re-import; flag for human |
| Bridge output missing required fields | Quarantine + notify |

---

## Implementation Status

| Bridge | Status | Owner |
|--------|--------|-------|
| Feishu | 🔴 Not started | — |
| Web | 🟡 Manual (kdo fetch-url) | — |
| WeChat | 🔴 Not started | — |
| Notion | 🔴 Not started | — |
| AI Chat | 🟡 Manual (kdo import-chat) | — |
| Screenshots | 🔴 Not started | — |
| Voice | 🔴 Not started | — |

**Next Step**: Implement `bridge/web.py` auto-extraction as PoC (Proof of Concept).

---

## Version

v0.1 — 2026-05-03 — Initial bridge protocol draft.
