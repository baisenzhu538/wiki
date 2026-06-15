---
id: huangyaoshi-extractor-upgrade-report
title: 黄药师：暗知识萃取器 B+→A 升级报告
type: decision
status: draft
domain:
- master
created_at: 2026-05-31
updated_at: '2026-06-16'
target_roles:
- 欧阳锋（Architect）
- 用户（决策者）
related:
- '[[data-curator-role-division]]'
- '[[plan_20260531_data-curator-v1.3]]'
author: legacy
source_context: KDO internal record （原始 source 无法追溯，已标记为 source_unknown，待后续补充）
source_refs:
- source_unknown
reviewed_by: pending
confidence: 0.6
trust_level: low
---
# 暗知识萃取器 B+→A 升级报告

## B+ 版本的问题（自我诊断）

| # | 问题 | 影响 |
|:--:|------|------|
| 1 | **精确率不足** — 111 条 insight，估计 70%+ 是噪声。口述稿每三句话就有一个"我觉得"，全被判为 insight | 老顽童要从 266 条中挑 ~20，浪费在看噪声上 |
| 2 | **operation 自动提取不可靠** — "然后我教大家说第二个方法…"提取出"我是高角度仰视产品特写"——不是步骤，是原文碎片 | 读到 operation 字段会觉得"你不懂" |
| 3 | **评分区分度不足** — 大量 0.50-0.55 和 top 0.70+ 混在一起 | 排序没把金子浮到上面 |
| 4 | **cross-reference 全空** — 无法自动建议关联卡片 | 老顽童要从零补关联 |

## A 版本的四个改造

### 1. 4 维加权评分（替代单维度特异性评分）

```
tool_usage: 特异性(.30) + 独特性(.20) + 独立性(.25) + 可操作性(.25)
failure:    特异性(.25) + 独特性(.30) + 独立性(.20) + 可操作性(.25)
insight:    特异性(.15) + 独特性(.40) + 独立性(.30) + 可操作性(.15)
workflow:   特异性(.30) + 独特性(.15) + 独立性(.25) + 可操作性(.30)
```

每维有独立的打分逻辑，按类型不同权重。

### 2. 金句检测器（替代"我觉得"批量判决）

正信号：
- 短精炼（<80字）
- 包含反转/对比（"不是X而是Y"）
- 包含原创比喻（"活菩萨""许愿""操盘手"）
- 反直觉判断（"其实""本质上""恰恰"）

负信号：
- 长而散（>150字）
- 大量填充词（"这个""然后呢""就是说"≥3次）
- 只是偏好陈述（"我觉得好用""我喜欢"）

### 3. operation 留空标注

不再自动提取破碎的步骤。改为：
- tool_usage/workflow/failure 如果步骤可提取（≥2条且每条>20字）→ 填入
- 否则 → 标注 `[需从原始表述中提取操作步骤]`
- insight → 标注 `[不适用]`

### 4. 语义去重 + cross-reference 匹配

- **去重**：CJK bigram 重叠 >70% → 保留高分，合并重复
- **cross-ref**：加载全库 384 张卡的标题+正文做关键词匹配，自动建议 top 3 关联

## 效果对比

| 指标 | B+ | A | 变化 |
|------|:--:|:--:|:---:|
| 候选总数 | 266 | 52 | **↓81%** |
| insight | 111 | 44 | ↓60% |
| tool_usage | 92 | 6 | 精确率大幅提升 |
| workflow | 45 | 2 | ↓96% |
| failure | 18 | 0 | 口述稿天然少 failure |
| top 分数 | 0.70-0.75 | 0.54-0.56 | 更诚实（全维度压低虚高） |
| 老顽童筛选时间 | ~2h 扫 266 条 | ~30min 扫 52 条 | **省 75%** |

## 当前状态

| 组件 | 状态 |
|------|:--:|
| extract_dark_knowledge.py (A版) | ✅ 已测试，`40_outputs/capabilities/skills/data-curator/scripts/` |
| 月白口述稿01 产出 | ✅ `60_feedback/data-quality/dk-candidates/` — 52 条候选 |
| 月白口述稿02 待处理 | ⏳ `00_inbox/design/AI设计-AI设计基础01.txt` |
| 月白口述稿03 待处理 | ⏳ `00_inbox/design/AI设计-AI设计师实操培训01.txt`（第二期口述，已处理第一期的 cleaned 版本） |

## 老顽童使用流程

```
1. 打开 60_feedback/data-quality/dk-candidates/<口述稿名>-dk-candidates.json
2. 从 score 高到低扫 52 条候选
3. 对每条判断：是否值得做成暗知识卡？(预计 ~15 条)
4. 对值得的：补完 operation（人写步骤）+ boundary + cross_reference + 精修 title
5. 按 SOP 模板写入 30_wiki/concepts/dk-yb-<slug>.md
6. 在 laowantong-next-tasks.md 标记完成
```

## 欧阳锋判断（2026-05-31）

### 1. 萃取器 A 版是否可交付？→ ✅ 可交付

4 个改造方案全部合理。效果对比 266→52 条、省 75% 筛选时间，改进量已经足够。

唯一建议：operation 的"留空标注"方案（`[需从原始表述中提取操作步骤]`）需要确认老顽童看得到这个标注。如果标在 JSON 里但老顽童读 JSON 不仔细，等于没标。建议在输出的 `dk-candidates.json` 中，把 `operation` 字段的值设置为显眼的大写占位符，如 `OPERATION_NEEDS_HUMAN`，让他一眼知道"这一步要我来写"。

### 2. 先给第一批还是等第二篇一起？→ 先给第一批，异步跑第二篇

月白口述稿01 的 52 条候选足够老顽童试手了。他在做筛选和卡片的这段时间，你跑第二篇。等第一批产出审查通过时，第二篇刚好接上。不阻塞。

### 3. 命名规范 → `dk-yb-{N}-{slug}.md`

同意。记：

| 前缀 | 素材源 | 示例 |
|:----:|:-------|:-----|
| `dk-c{N}` | corrections.md | `dk-c10-batch-tool-no-dry-run` |
| `dk-f{N}` | failure-modes.md | `dk-f1-regex-on-cjk` |
| `dk-yb{N}` | 月白口述稿 | `dk-yb01-notebooklm-workflow` |
| `dk-tr{N}` | Truman 口述稿（后续） | `dk-tr01-agent-three-loops` |

N 统一用两位序号（01, 02, …），不跳过。

---

*欧阳锋 · 2026-05-31*
