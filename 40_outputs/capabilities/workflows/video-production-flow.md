# Video Production Flow

## Purpose

Structured multi-role pipeline for turning a written article into a ≤10 minute
video. Each stage runs in an independent session (`/new`), reads only its
designated input file, and writes exactly one output file. No stage depends on
"remembering" what happened before.

## Design Principle

```
Session memory = volatile.  Files = durable.

  /new → read input.md → write output.md → exit
  /new → read output.md → write next.md → exit
  ...

Each session's context: 1 input file + stage spec.  Never the whole pipeline.
```

## Role Assignment

| Stage | Role | Why |
|:-----:|------|-----|
| 1. Script | **老顽童** (Producer) | Article→spoken script is content compression — his core skill |
| 2. Storyboard | **洪七公** (Multimodal) | Visual imagination + scene timing — his core skill |
| 3. Frames | **洪七公** (Multimodal) | Tool operation for visual asset generation |
| 4. Audio | **Toolchain** (kdo video render) | TTS + BGM is mechanical — no cognitive load, no agent needed |
| 5. Compose | **Toolchain** (kdo video render) | ffmpeg assembly is a script — deterministic, zero ambiguity |
| Gate | **欧阳锋** (Architect) | Review at script + storyboard + draft stages |

## Pipeline Stages

### Stage 0 — Project Init (Toolchain)

```
$ kdo video init <article_path> [--title "Video Title"]
```

Creates:
```
40_outputs/content/videos/<project-slug>/
├── _spec.md              # Project manifest (source article, title, specs)
├── 01-script.md          # Template for Stage 1 output
├── 02-storyboard.md      # Template for Stage 2 output
├── frames/               # Stage 3 output directory
├── audio/                # Stage 4 output directory
└── draft/                # Stage 5 output directory
```

### Stage 1 — Script Refinement（老顽童，/new session）

```
入参：源文章 .md
出参：01-script.md
审查：欧阳锋（≤3 个修改点直接批，>3 个返工）
```

**Instructions for 老顽童**:
```
Read the source article. Write a spoken-word script (口播稿) at:

  40_outputs/content/videos/<project-slug>/01-script.md

Rules:
- Target duration: 8-10 minutes spoken
- Chinese spoken pace: ~250 chars/min → script = 2000-2500 chars
- Every sentence must be speakable — read it aloud in your head before writing
- Break into exactly 5 segments, each with a clear hook:
  1. Hook (30-45s): The "然后呢？" moment — information overload is not the problem
  2. What is KDO (2min): Pipeline, not folder. 9-step closed loop.
  3. How it works (3-4min): Feishu doc → deliverable, 8 concrete steps
  4. Who it's for (1.5min): 4 fit signals + 3 misfit signals
  5. Closing (1min): Garden vs factory metaphor, CTA
- Each segment header: ## Segment N: [Title]  [est. duration]
- For each segment, include 3-5 speaking points (not paragraphs — bullet points
  the speaker will expand)
- At the end of each segment, note: [Visual hint: what should be on screen]
- AVOID: nested clauses, parentheticals, jargon that needs explaining
- PREFER: short sentences, concrete examples, pauses marked with --

Output format:
  ## Segment 1: Hook — 信息过载不是问题     [~45s]
  - Speaking point 1
  - Speaking point 2
  ...
  [Visual hint: ...]
```

**Acceptance criteria (欧阳锋 review)**:
- [ ] Speakable — every sentence works when read aloud
- [ ] 5 segments, each with hook + visual hint
- [ ] Total estimated duration 8-10 min
- [ ] No nested clauses longer than one breath
- [ ] Key terms explained in context (not assuming prior knowledge)

### Stage 2 — Storyboard（洪七公，/new session）

```
入参：01-script.md
出参：02-storyboard.md
审查：欧阳锋（重点关注画面与台词的匹配逻辑）
```

**Instructions for 洪七公**:
```
Read 01-script.md. Design the visual storyboard at:

  40_outputs/content/videos/<project-slug>/02-storyboard.md

Rules:
- For each speaking point in the script, define ONE visual frame
- Frame format:
  | Frame # | Segment | Speaking Point | Visual Type | Description | Duration |
  |---------|---------|---------------|-------------|-------------|----------|
  | 1       | 1       | "信息过载不是问题" | Title Card | Dark bg, glowing text reveal | 5s |
- Visual types: Title Card / Text Reveal / Flow Diagram / Terminal Demo / 
  Comparison Split / Metaphor Illustration / CTA Card
- Include a style guide section at the top:
  ## Style Guide
  - Color palette: [primary, accent, bg, text] with hex codes
  - Font: [name, weights used]
  - Animation language: [describe the motion feel — e.g. "clean reveals, 
    no bounce, 0.3s ease transitions"]
  - Aspect ratio: 1920x1080
  - Brand elements: [logo position, recurring motifs]
- At the bottom, include a timing summary:
  ## Timing Summary
  | Segment | Frames | Total Duration |
  |---------|--------|---------------|
  | 1       | N      | Xs            |
  | Total   | N      | Xmin Xs      |
- AVOID: generic "tech" aesthetic (blue/purple gradients on dark bg)
- PREFER: KDO brand language — Bauhaus simplicity, black/white/amber, 
  terminal aesthetics, structured whitespace
```

**Acceptance criteria (欧阳锋 review)**:
- [ ] Style guide defined (colors, font, animation, brand)
- [ ] Every speaking point mapped to a frame with visual type
- [ ] Timing summary matches 8-10 min target
- [ ] Visual types vary (not all Title Cards)
- [ ] Style is recognizably KDO, not generic tech

### Stage 3 — Frame Rendering（洪七公，/new session per segment）

```
入参：02-storyboard.md
出参：frames/segment_*.png（or .mp4 clips）
审查：欧阳锋抽查 2 个 segment（≥1 early + ≥1 late）
```

**Instructions for 洪七公**:
```
Read 02-storyboard.md. Render each segment's frames to:

  40_outputs/content/videos/<project-slug>/frames/

Rules:
- Work ONE SEGMENT PER SESSION. Do not attempt all 5 in one go.
- For each segment session:
  /new
  Read: 02-storyboard.md (only the segment you're working on)
  Output: frames/segment_N_frame_*.png (or segment_N.mp4 for animated segments)
- Use the tool that matches each visual type:
  - Flow Diagram → Excalidraw or SVG
  - Terminal Demo → styled HTML→screenshot or ASCII art
  - Text Reveal → keyframe PNGs
  - Metaphor Illustration → Excalidraw or p5js
  - Comparison Split → styled HTML→screenshot
- Each frame must match the style guide defined in 02-storyboard.md exactly
- Name convention: segment_N_frame_FFF.png (N=segment, FFF=frame number, 
  3-digit zero-padded)
- After all frames for a segment are rendered, run:
  kdo video validate --stage frames --segment N
```

**Acceptance criteria (欧阳锋 spot-check)**:
- [ ] Spot-check ≥2 segments: frames match storyboard descriptions
- [ ] Color/font matches style guide
- [ ] All frames 1920x1080

### Stage 4 — Audio Generation（Toolchain: `kdo video render --audio`）

```
入参：01-script.md + 02-storyboard.md（timing data）
出参：audio/segment_*.mp3
无审查门禁（纯机械操作，TTS 参数在 storyboard style guide 中已定义）
```

The `kdo video render --audio` command:
1. Reads `01-script.md` → extracts speaking text per segment
2. Reads `02-storyboard.md` → extracts per-frame durations for timing
3. Calls TTS for each segment, respecting the durations
4. Generates BGM at low volume (-18dB relative to voice)
5. Outputs `audio/segment_N.mp3` per segment

### Stage 5 — Compose（Toolchain: `kdo video render --compose`）

```
入参：frames/* + audio/* + 02-storyboard.md
出参：draft/draft.mp4
审查：欧阳锋（终审，关注整体节奏 + 音画同步）
```

The `kdo video render --compose` command:
1. Reads `02-storyboard.md` → extracts frame→duration mapping
2. Assembles frames + audio per the storyboard timing
3. Outputs `draft/draft.mp4`

### Stage 6 — Validate（Toolchain: `kdo video validate`）

```
入参：draft.mp4 + 01-script.md + 02-storyboard.md
出参：validation report (terminal output)
```

Three-layer quality gate:

| Layer | Checks | Gate |
|:-----:|--------|------|
| L1 Structure | 4 files present (script/storyboard/frames/audio), manifest complete | BLOCK |
| L2 Content | A/V sync ±0.3s, subtitle match, scene transition rhythm, no missing frames | BLOCK |
| L3 Pipeline | source article traceable, storyboard→script consistency, asset copyright noted | WARN |

### Stage 7 — Ship（Toolchain: `kdo video ship`）

```
入参：draft/draft.mp4（validate passed）
出参：final/final.mp4 + delivery record
```

Copies draft → final, records delivery event, initializes feedback path.

## Stage Gates Summary

```
Source Article
    │
    ▼
[Gate 0] kdo video init ─── Project skeleton created
    │
    ▼
[Stage 1] 老顽童 → 01-script.md
    │
    ▼
[Gate 1] 欧阳锋审查脚本 ─── BLOCK if not speakable
    │
    ▼
[Stage 2] 洪七公 → 02-storyboard.md
    │
    ▼
[Gate 2] 欧阳锋审查分镜 ─── BLOCK if style undefined or visual types monotonous
    │
    ▼
[Stage 3] 洪七公 → frames/*.png（5 sessions, 1 per segment）
    │
    ▼
[Gate 3] 欧阳锋抽查 2 segments ─── WARN if style drift
    │
    ▼
[Stage 4] Toolchain → audio/*.mp3
    │
    ▼
[Stage 5] Toolchain → draft/draft.mp4
    │
    ▼
[Gate 4] kdo video validate ─── L1/L2 BLOCK, L3 WARN
    │
    ▼
[Gate 5] 欧阳锋终审 ─── 节奏+音画同步+整体观感
    │
    ▼
[Stage 7] kdo video ship → final.mp4
```

## Exit Criteria

- [ ] `kdo video validate` returns 0 (L1+L2 pass, L3 warnings documented)
- [ ] `final/final.mp4` exists, duration 8-10 min
- [ ] Source article traceable from video manifest
- [ ] Script, storyboard, style guide all archived alongside video
- [ ] Delivery record exists in `50_delivery/`

## Related

- Source pattern: `40_outputs/capabilities/workflows/produce-and-ship-flow.md`
- Builder spec: `kdo video` CLI (see 黄药师 task)
- Quality reference: `90_control/kdo-industrialization-manual.md`
