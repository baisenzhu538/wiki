# Frames Production Brief

## Project
- **Title:** Knowledge Delivery OS 快速上手指南：把散落知识变成可交付资产
- **Stage:** 3/6 — Frames
- **Input:** `../01-script.md` + `../02-storyboard.md`
- **Output:** `frames/` — 38 static key frames (1920×1080)

## Style Guide (Strict)
- **Palette:** `#0A0A0A` (bg) / `#F5F5F5` (text) / `#E5A028` (amber primary) / `#888888` (muted) / `#EF4444` (red/danger) / `#4ADE80` (green/success)
- **Fonts:** JetBrains Mono (terminal/code) / Inter (body) / Noto Sans SC (Chinese)
- **Aesthetic:** Bauhaus simplicity. Terminal aesthetics. Structured whitespace.
- **NEVER:** Blue/purple gradients on dark bg. Generic "tech" look. Bouncy animations.
- **Aspect Ratio:** 1920×1080

## Frame List (38 frames)

### Segment 1: Hook (~50s) — Frames 1–10
| # | Type | Key Visual | Priority |
|---|------|-----------|----------|
| 1 | Title Card | KDO logo 居中淡入 + 副标题 | P0 |
| 2 | Text Reveal | 大问号放大出现移左上 | P0 |
| 3–5 | Text Reveal | 数据通讯式跳动: 200+/50+/10+ | P0 |
| 6 | Text Reveal | 713块/1200+小时 数字跳动变暗 | P0 |
| 7 | Text Reveal | "然后呢？"闪烁 | P0 |
| 8 | Metaphor | 日历+钟表+收藏夹 快闪场景 | P1 |
| 9 | Text Reveal | 金句: "信息变不成资产才是问题" | P0 |
| 10 | Logo Reveal | KDO 从噪点中显现 | P0 |

### Segment 2: 知识流水线 (~115s) — Frames 11–17
| # | Type | Key Visual | Priority |
|---|------|-----------|----------|
| 11 | Text Reveal | "你不是不努力..." amber 高亮 | P0 |
| 12 | Text Reveal | "收集+分类=死胡同" 红线划掉 | P0 |
| 13 | Comparison | 三大应用失败现状列表 | P1 |
| 14 | Text Reveal | 消费行为(红) vs 生产行为(琥珀) | P0 |
| 15 | Flow Diagram | 闭环图: 输入→加工→交付→反馈→改进 | P0 |
| 16 | Flow Diagram | 9 个方块横向排列依次高亮 | P0 |
| 17 | Text Reveal | "不是做得更多。是做得更清晰。" | P0 |

### Segment 3: KDO 是什么 (~195s) — Frames 18–29
| # | Type | Key Visual | Priority |
|---|------|-----------|----------|
| 18 | Text Reveal | KDO 不是什么 列表+红叉 | P1 |
| 19 | Flow Diagram | 漏斗动画: 顶部文件倒入→节点闪烁→底部三产出 | P0 |
| 20 | Flow Diagram | 三产出方块 + 溯源虚线 | P0 |
| 21 | Terminal Demo | `kdo trace` 返回结果 | P1 |
| 22 | Text Reveal | 金句: "不是存得更多，是产得更清晰" | P0 |
| 23–25 | Terminal Demo | `capture` / `ingest` / `enrich` CLI 截图 | P0 |
| 26 | Metaphor | 生肉→粥→菜 三帧快闪 | P1 |
| 27–28 | Terminal Demo | `route`/`produce`/`validate` / `ship`/`feedback`/`improve` | P0 |
| 29 | Text Reveal | "可以只用 3 步。也可以用满 9 步。" | P1 |

### Segment 4: 典型工作流 (~85s) — Frames 30–32
| # | Type | Key Visual | Priority |
|---|------|-----------|----------|
| 30 | Comparison | 左右分屏: 墓碑(传统) vs 流水线(KDO) | P0 |
| 31 | Comparison | 墓碑长青草，流水线输出文竩+checkmark | P0 |
| 32 | Text Reveal | "文档写完就是墓碑 / 文档写完才是开始" | P0 |

### Segment 5: Closing (~60s) — Frames 33–38
| # | Type | Key Visual | Priority |
|---|------|-----------|----------|
| 33 | Comparison | 花园(Obsidian) vs 厨房(KDO) 分屏+传送带 | P0 |
| 34 | Metaphor | 花园插画→果实流动→厨房插画 | P1 |
| 35 | Text Reveal | 适合/不适合 两栏对比 | P1 |
| 36 | Text Reveal | 金句: "信息变不成资产才是问题" | P0 |
| 37 | CTA Card | KDO logo + "让你的知识值得被交付" | P0 |
| 38 | End Screen | 淡出至黑 + 底部信息 | P0 |

## Asset Checklist (for production)
- [ ] KDO logo 横版+竖版 (SVG, 白/琥珀双色)
- [ ] 简约墓碑图标 (用于 Frame 30–31)
- [ ] 生肉/粥/菜插画 (用于 Frame 26, 极简几何风格)
- [ ] 花园/厨房插画 (用于 Frame 34, 极简几何风格)
- [ ] 飞书文档图标简化版 (用于 Frame 30)
- [ ] 终端背景纹理 (可选，纯黑可替代)

## Priority Definition
- **P0:** 必需。没有这帧，视频完整性受损。
- **P1:** 重要。能显著提升质感和理解度，但缺失不致命。
