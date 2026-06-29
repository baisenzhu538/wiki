---
id: task_20260629_wangyuyan-vikki-dk-extraction
type: task
status: proposed
assignee: 王语嫣→老顽童
priority: P1
created_at: 2026-06-29
author: 黄药师
---

# Vikki 方法库 → dk 卡萃取

## 来源

`00_inbox/vikki-human-speech(2).zip` — Vikki 讲人话检查 v1.0，含 4 标准 + 7 诊断 + 12 方法。

## 已完成

黄药师已将 SKILL.md + human-speech-rules.md 替换到：
- `.claude/skills/content-production-polish/SKILL.md`（Claude Code 版）
- `40_outputs/capabilities/skills/shared/content-production-polish/SKILL.md`（共享/Hermes 版）

## 建议王语嫣拆任务

`human-speech-rules.md` 含 12 个方法，每个方法结构为 Problem→Fix→Pattern→Example，天然适合做成 dk 卡：

| # | 方法 | dk 卡 id 建议 |
|:--|:---|:---|
| 1 | 抽象词落地法 | `dk-vikki-abstract-to-concrete` |
| 2 | 先场景后概念 | `dk-vikki-scene-before-concept` |
| 3 | 短句切分法 | `dk-vikki-short-sentence` |
| 4 | 排比控制法 | `dk-vikki-parallel-limit` |
| 5 | 边界标注法 | `dk-vikki-boundary-marker` |
| 6 | 例子密度法 | `dk-vikki-example-density` |
| 7 | 金句去重法 | `dk-vikki-gold-sentence-dedup` |
| 8 | 节奏控制法 | `dk-vikki-rhythm-control` |
| 9 | 视觉锚点法 | `dk-vikki-visual-anchor` |
| 10 | 转化钩子法 | `dk-vikki-conversion-hook` |
| 11 | 身份对齐法 | `dk-vikki-identity-alignment` |
| 12 | 信源显影法 | `dk-vikki-source-visibility` |

建议拆为 2-3 批，每批 4-6 张，老顽童逐张萃取入库到 `30_wiki/dark-knowledges/`。萃取标准：保留 Problem→Fix→Pattern→Example 四段，补 `## 原始表述` / `## 使用场景` 等 dk 标准 section。

## 优先级

P1——内容润色是老顽童产文章/口播稿的刚需，12 张 dk 卡入库后直接可用。
