# Multimodal Production Workflow

## Purpose

Unified entry point for all multimodal rendering. Don't make callers know which tool to use — they say what they need, this workflow routes to the right weapon.

## Design Principle

```
One ask → one route → one output.

Caller says:   "把这篇文章转成视频"
Workflow does: 判类型 → 选武器 → 执行渲染 → 质检 → 产出 → 通知段王爷

Caller doesn't need to know:
  - Wan vs Hyperframes vs T2V pipeline
  - CosyVoice vs commercial TTS
  - ComfyUI vs Draw.io for diagrams
```

---

## Trigger

When any agent or user requests multimodal output:
- "做成视频""转视频""video please"
- "画个架构图""做成图""visualize this"
- "做 PPT""转幻灯片""slides please"
- "配音""TTS""读出来""audio"
- "分析这张图""看看这个截图""VA this"

---

## Step 1 — Classify Input

Determine what the input IS and what the caller WANTS.

| Input Type | Examples | Default Route |
|------|------|------|
| Markdown 文章/卡片 | wiki card, article, report | 视频 / PPT / 架构图 |
| 图片/截图 | screenshot, diagram, photo | VLM + VA |
| 数据/流程 | process, pipeline, architecture | 架构图 / 信息图 |
| 纯文本 | script, narration | TTS 配音 |
| 网页文章 | URL, multi-page article | Multi-page Capture → 再路由 |

**Decision tree**:
```
输入是什么？
  ├── 图片/截图
  │   ├── 需提取文字？ → OCR Pipeline
  │   ├── 需理解内容？ → VLM Pipeline
  │   └── 需分析设计？ → VA 四维法
  │
  ├── 文章/卡片（文字为主）
  │   ├── 需做成视频？ → Video Pipeline
  │   ├── 需做成 PPT？ → Presentation Pipeline
  │   ├── 需做成无限画布？ → Infinite Canvas Pipeline（空间叙事，镜头飞行）
  │   ├── 需做成信息图？ → Infographic Pipeline
  │   ├── 需做成架构图？ → Diagram Pipeline (Draw.io)
  │   └── 需做成播客？ → Audio Pipeline
  │
  └── 网页文章 → Multi-page Capture → 回到文章路由
```

---

## Step 2 — Route to Pipeline

### Pipeline A: Video

```
输入文章 → Stage 1: 脚本精炼（老顽童）
          → Stage 2: 分镜设计（洪七公）
          → Stage 3: 画面生成（洪七公 — Wan/Hyperframes/T2V）
          → Stage 4: 音频生成（CosyVoice TTS）
          → Stage 5: 合成导出（ffmpeg）
          → Gate: 欧阳锋审查（script + storyboard + draft）
          → 产出: 40_outputs/content/videos/<slug>/
```

**Weapon selection**:
| 场景 | 武器 | 理由 |
|------|------|------|
| 通用文章→视频 | Hyperframes | 内置TTS+字幕+转场，一站式 |
| 长文章批量 | Text-to-Video Pipeline | 全自动流水线 |
| 需要 AI 生成 B-roll | Wan 2.2 | 文/图→5秒视频片段 |
| 需要精确分镜控制 | 手动分镜 + ComfyUI render | 每镜独立控制 |

### Pipeline B: Visual Analysis

```
输入图片 → OCR 提取文字（PaddleOCR/EasyOCR）
         → VLM 识图（MiniMax M3 / Qwen-VL）
         → VA 四维法（空间层级+分组逻辑+阅读路径+视觉强调）
         → visual-polish 去 AI 味（如果是 AI 生成图）
         → 产出: OCR文本 + VLM描述 + VA节 + 卡片更新
```

### Pipeline C: Diagram / Infographic

```
输入描述/数据 → 判类型
  ├── 架构图/流程图 → Draw.io MCP（自然语言→可编辑图）
  ├── 信息图/海报 → ComfyUI + AI Image Generation
  └── 数据图表 → 确定图表类型 → 生成 → 标注
  → visual-polish（去 AI 味→配色检查→构图检查）
  → 产出: 40_outputs/content/images/<type>/<slug>/
```

### Pipeline D: Presentation

```
输入文章/卡片 → 提取核心论点（≤5 个）
              → 选择演示风格
              ├── 标准 PPT → Presenton（Docker AI PPT）
              ├── 代码幻灯片 → Marp/Slidev（Markdown→Slide）
              └── 空间叙事 → Prezi 无限画布（段王爷
              → visual-polish（PPT AI 感检查）
              → 产出: 40_outputs/content/presentations/<slug>/
```

### Pipeline E: Audio

```
输入文字 → 判语言/方言 → 选 TTS 引擎
         ├── 中文普通话/方言 → CosyVoice TTS
         └── 多语种 → CosyVoice 9 语种
         → 后期（BGM/音效/降噪）
         → 产出: 40_outputs/content/audio/<slug>/
```

---

## Step 3 — Quality Gate

Each pipeline has its own gate before handoff:

| Pipeline | Gate | Gatekeeper |
|------|------|------|
| Video | Script + Storyboard + Draft 审查 | 欧阳锋 |
| Visual Analysis | 四维全+零颜色违规+≥100字/图 | 洪七公自检 + 欧阳锋抽检 |
| Diagram | 逻辑正确+可编辑+配色检查 | 洪七公自检 |
| Presentation | 页面节奏+品牌感+无 AI 模板感 | 洪七公自检 + visual-polish |
| Audio | 可懂度+自然度+无机械感 | 洪七公自检 |

---

## Step 4 — Output and Handoff

```
洪七公产出
  → 写入 40_outputs/content/<type>/<slug>/
  → visual-polish 最终检查（如果是 AI 生成）
  → 标记 ready-for-publish
  → 通知段王爷：有新资产可发布
```

**段王爷 handoff 格式**:
```
📦 新资产就绪
类型: [video/image/presentation/audio]
路径: 40_outputs/content/<type>/<slug>/
描述: [一句话]
建议渠道: [按 channel-distribution 矩阵]
质检: [通过/有待修复项]
```

---

## Integration with Channel Distribution

After multimodal production completes, handoff to `workflows/channel-distribution.md`:

```
Multimodal Production (洪七公)
  → Output: visual asset
    → Channel Distribution (段王爷)
      → Choose channel → Adapt format → Publish → Track
```

---

## Related

- `agent-spec-hongqigong-multimodal` — 洪七公角色规格（含武器决策树）
- `shared/visual-asset-analysis/SKILL.md` — VA 统一入口
- `shared/visual-polish/SKILL.md` — 视觉去 AI 味
- `shared/beikai-multimodal-pipeline/SKILL.md` — 多模态渲染总纲
- `workflows/video-production-flow.md` — 视频生产详细流程
- `workflows/channel-distribution.md` — 下游：渠道分发
- `agent-spec-duanwangye-publisher` — 下游：段王爷发布
