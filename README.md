# Knowledge Delivery OS Workspace

This workspace is a local-first knowledge delivery system.

> **All AI agents and human operators must read `90_control/PROTOCOL.md` before any create, update, or delete operation.**

Core loop:

```text
Capture -> Register -> Compile -> Route -> Produce -> Validate -> Deliver -> Feedback -> Improve
```

Directory contract:

- `00_inbox/`: low-friction capture.
- `10_raw/`: source of truth.
- `20_memory/`: cross-session continuity.
- `30_wiki/`: reusable compiled knowledge.
- `40_outputs/`: deliverable assets: content, code, and capabilities.
- `50_delivery/`: shipped releases and channel records.
- `60_feedback/`: comments, issues, logs, corrections, eval failures.
- `70_product/`: project specs, task queue, connector specs, and roadmaps.
- `90_control/`: schemas, routing rules, quality gates, and agent instructions.

Run:

```bash
kdo status
kdo capture "A useful idea" --title "Useful idea"
kdo ingest
kdo produce content/article --topic "Useful idea"
kdo project "Knowledge Delivery Product" --goal "Turn knowledge into shipped assets"
kdo task "Ship first artifact" --project-id proj_YYYYMMDD_xxxxxxxx
kdo lint
```

## Local Tools

All agents can invoke these directly. Paths are relative to workspace root.

### Image OCR (Chinese text extraction)

Local PaddleOCR v5 pipeline. No network, no API key. Supports PNG and JPEG.

```bash
# Single image → outputs *_paddle_ocr.txt alongside the image
powershell 40_outputs/capabilities/skills/image-ocr/ocr-image.ps1 path/to/image.png

# Batch
powershell 40_outputs/capabilities/skills/image-ocr/ocr-image.ps1 "00_inbox/*.png" -Batch

# Direct Node.js (if PowerShell unavailable)
node C:\Users\Administrator\ocr-pipeline\ocr-paddle.cjs path/to/image.png
```

**Runtime** (outside wiki, to avoid git): `C:\Users\Administrator\ocr-pipeline\` — contains `ocr-paddle.cjs`, `models/` (~20MB), `node_modules/`. Set up with `npm install paddleocr onnxruntime-web fast-png jpeg-js`.

**Known pitfall**: The character dictionary (`dict.txt`) must NOT be filtered. If you `.filter(l => l.trim())` after `split('\n')`, the leading full-width space line is removed and all character indices shift by 1 — the output will be random Chinese gibberish.

**Capability doc**: `40_outputs/capabilities/skills/image-ocr/SKILL.md`
