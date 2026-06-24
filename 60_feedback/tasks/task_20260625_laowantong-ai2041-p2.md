# 老顽童任务指令：王欢《AI 2041》P2 批次生产（王语嫣）

> 王语嫣铁律：本指令仅写入 `60_feedback/`，不污染 `30_wiki/`。老顽童负责按此指令在 `30_wiki/` 生产卡片。
> 触发来源：P1 批次已通过王语嫣 20% 抽样验收，现进入 P2 批次。
> 前置任务：`60_feedback/tasks/task_20260625_laowantong-ai2041-p1.md`
> 验收报告：`60_feedback/audit/ai2041-p1-production-audit-20260625.md`

---

## 0. 元信息

| 项目 | 内容 |
|------|------|
| 任务来源 | 王欢《AI 2041》拆书会逐字稿卡片化 |
| 素材路径 | `C:/Users/Administrator/Desktop/wiki/00_inbox/拆书会第208期：《AI 2041：预见未来二十年》逐字稿（完整版）.md` |
| 前置诊断 | `60_feedback/diagnosis/diag_20260624_wangyuyan_ai2041-annotation.md` |
| 前置决策 | `60_feedback/decisions/dec_20260624_wangyuyan-ai2041-card-plan.md` |
| 反馈日期 | 2026-06-25 |
| 质量负责人 | 王语嫣（CLI） |
| 生产方 | 老顽童 |
| 优先级 | P2（紧接 P1 批次后执行） |

---

## 1. 开工前必须修复的 P1 遗留项

P1 验收结论为通过，但需在 P2 开工前处理 2 个格式/schema 问题：

| # | 问题 | 涉及卡片 | 修复方式 |
|:--|:-----|:---------|:---------|
| 1 | `confidence` 字段为范围字符串 `0.75-0.85`，可能破坏 lint/schema 校验 | `tool-ai2041-source-verification-checklist` | 改为单一数值（建议 `0.80`）；若需表达区间，在正文「可信度说明」中解释 |
| 2 | `source_person` / `source_context` 为自定义 frontmatter 字段，未在通用 schema 中定义 | 5 张 case 卡 | 保留正文「来源人与来源语境」节；建议从 frontmatter 中移除这两个字段，或统一纳入 schema 后再加回 |

---

## 2. P2 必须生产的 8 张卡

### 2.1 DK 卡（3 张）

| id | 标题 | 来源素材 | 核心要求 |
|:---|:---|:---------|:---------|
| `dk-ai-prediction-expiry-date` | AI 预言的保质期 | 第一幕 + 第八幕 | 如何判断技术预测是否过期：出版年份、技术代际、作者前提、反事实 |
| `dk-ai-social-progress-not-automatic` | 社会进步不是自动的 | 第七幕 | 技术解决效率，不解决分配；需要制度设计；案例 |
| `dk-ai-scarcest-resource-is-self` | 最稀缺的是自我 | 第八幕 | 算法替你选久了会失去判断力；反事实与恢复路径 |

### 2.2 Concept 卡（1 张）

| id | 标题 | 来源素材 | 核心要求 |
|:---|:---|:---------|:---------|
| `concept-ai-information-quality-ladder` | 信息质量阶梯 | 第二幕 + 附录 | 从短视频/二手评论到一手论文的升维路径；与 BITCOE 输入质量维度链接 |

### 2.3 Case 卡（4 张）

| id | 标题 | 来源素材 | 核心要求 |
|:---|:---|:---------|:---------|
| `case-deepfake-market-misuse` | Deepfake 的商业机会与滥用风险 | 第六幕 | 市场规模区间；WEF 风险排名；检测与监管 |
| `case-ai-companion-emotional` | AI 情感陪伴的市场与伦理 | 第六幕 | 市场规模区间；Character.AI / Replika / 小冰；孤独经济 + 未成年人风险 |
| `case-roblox-ai-npc-education` | Roblox AI NPC 与教育场景 | 第六幕 | Code Assist / Assistant；教育游戏化；人机协作边界 |
| `case-ai-job-displacement-wef` | WEF 对 AI 就业影响的预测 | 第三幕 | 8500 万替代 / 9700 万新增；净增 1200 万；技能转型 |

---

## 3. 统一内容要求

### 3.1 按卡片类型的内容要求

| 类型 | 必须包含 |
|:---|:---|
| **dk** | 一句话定义、为什么重要、核心机制/结构、边界与反例、与相关概念的关系、行动启示 |
| **concept** | 一句话定义、为什么重要、核心机制/结构、边界与反例、与相关概念的关系、行动启示 |
| **case** | 核心洞察、事迹/背景、关键数字（带 conf/source）、失败/成功原因、可迁移场景、教训与预警信号、对立面/争议 |

### 3.2 Frontmatter 规范

```yaml
---
id: dk-ai-prediction-expiry-date
title: AI 预言的保质期
type: dk
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.75        # 必须是单一数值，不允许范围字符串
trust_level: medium
language: zh-CN
domain:
- ai_collaboration
- critical_thinking
source_refs:
- 00_inbox/拆书会第208期：《AI 2041：预见未来二十年》逐字稿（完整版）.md
- 60_feedback/diagnosis/diag_20260624_wangyuyan_ai2041-annotation.md
- 60_feedback/decisions/dec_20260624_wangyuyan-ai2041-card-plan.md
related:
- "[[ai-collaboration-domain-digest]]"
- "[[framework-ai2041-critical-reading-os]]"
- "[[framework-ai-deconstruction-methodology]]"
- "[[tool-ai-critical-reading-three-layers]]"
- "[[tool-ai2041-source-verification-checklist]]"
---
```

**source_refs 必须精确**：逐字稿 + 王语嫣诊断/决策/任务文件。

**related 必须 ≥ 5**：必须包含 `ai-collaboration-domain-digest` 和至少 1 张已生产的 AI 2041 卡片（P0/P1）。

### 3.3 可信度标注规范

- 外部可验证事实：`[conf=0.85-0.90, source=...]`
- 王欢原创/二手概括：`[conf=0.70, source=王欢原创]`
- 市场数据：必须给区间并注明口径差异：`[conf=0.75, source=王语嫣诊断整合 ...]`

### 3.4 外部来源补充要求

P2 案例卡仍需 WebSearch 补充独立来源：

| 卡片 | 需要补充的内容 |
|------|----------------|
| `case-deepfake-market-misuse` | 至少 2 家机构市场预测，注明口径差异；WEF 风险排名 |
| `case-ai-companion-emotional` | Appfigures / Character.AI / Replika / 小冰相关数据；未成年人风险报道 |
| `case-roblox-ai-npc-education` | Roblox Code Assist / Assistant 官方信息；教育场景报道 |
| `case-ai-job-displacement-wef` | WEF Future of Jobs Report 2020 原文或权威摘要 |

---

## 4. 执行顺序

建议按以下顺序分批生产，每完成 2-3 张可通知王语嫣提前看：

1. `dk-ai-prediction-expiry-date`
2. `concept-ai-information-quality-ladder`
3. `case-deepfake-market-misuse`
4. `case-ai-companion-emotional`
5. `case-roblox-ai-npc-education`
6. `case-ai-job-displacement-wef`
7. `dk-ai-social-progress-not-automatic`
8. `dk-ai-scarcest-resource-is-self`

---

## 5. 质量门禁

每张卡完成后必须自查：

- [ ] `id` 与文件名一致
- [ ] `status` = `enriched`
- [ ] `author` = `老顽童`
- [ ] `reviewed_by` = `欧阳锋`
- [ ] `confidence` 为单一数值，非范围字符串
- [ ] `source_refs` 非空且文件存在
- [ ] `related` ≥ 5，且至少 1 条指向已生产 AI 2041 卡片
- [ ] 每个关键声明有 `conf/source` 标注
- [ ] 案例卡有独立外部来源链接或引用
- [ ] 无死链（包括前向引用未生产卡片）
- [ ] dk/concept 卡包含边界与反例；case 卡包含对立面/争议

---

## 6. 验收与后续安排

- P2 8 张卡完成后，王语嫣按 20% 抽样（最少 3 张）做六层交叉验证。
- P2 通过且 P1 遗留项修复后，王欢《AI 2041》域 22 张卡全部完成。
- 随后执行 `60_feedback/tasks/task_20260625_laowantong-synthesis-dk-cards.md` 中的 9 张跨案例 synthesis dk 卡。

---

*任务下达：王语嫣 | 日期：2026-06-25*
