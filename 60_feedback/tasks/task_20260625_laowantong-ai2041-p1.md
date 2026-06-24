# 老顽童任务指令：王欢《AI 2041》P1 批次生产（王语嫣）

> 王语嫣铁律：本指令仅写入 `60_feedback/`，不污染 `30_wiki/`。老顽童负责按此指令在 `30_wiki/` 生产卡片。
> 触发来源：P0 批次已通过王语嫣 20% 抽样验收，现进入 P1 批次。
> 前置任务：`60_feedback/tasks/task_20260624_laowantong-ai2041-cards.md`
> 验收报告：`60_feedback/audit/ai2041-p0-production-audit-20260625.md`

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
| 优先级 | P1（紧接 P0 批次后执行） |

---

## 1. 开工前必须修复的 P0 遗留项

P0 验收结论为通过，但需在 P1 开工前处理 1 个死链问题：

| # | 问题 | 涉及卡片 | 修复方式 |
|:--|:-----|:---------|:---------|
| 1 | 前向引用尚未生产的 P1 工具卡，形成死链 | `framework-ai2041-critical-reading-os` | 在 Critique 段落中，将 `[[tool-ai2041-source-verification-checklist]]` 改为纯文本 `tool-ai2041-source-verification-checklist（P1 待生产）`；待本批次该卡完成后，再替换为双向链接 |

---

## 2. P1 必须生产的 9 张卡

### 2.1 Concept 卡（2 张）

| id | 标题 | 来源素材 | 核心要求 |
|:---|:---|:---------|:---------|
| `concept-ai-chair-determines-view` | 椅子决定视角 | 第七幕 | 定义、五问清单、学术对照（standpoint theory）、与李开复/Crawford/Mollick 的具体映射 |
| `concept-ai-neutrality-bias` | 中立的暴政 | 第七幕 | 定义、识别信号、与 false neutrality / 算法审计的关系、反例 |

### 2.2 Tool 卡（2 张）

| id | 标题 | 来源素材 | 核心要求 |
|:---|:---|:---------|:---------|
| `tool-ai-cross-reading-method` | 交叉阅读法 | 附录一 + 第七幕 | 如何选择 2-3 本立场相反的书、对撞提问清单、输出格式、常见错误 |
| `tool-ai2041-source-verification-checklist` | AI 预测来源验证检查单 | 全文 + 附录 | 来源可信度五问、信息质量阶梯、市场数据口径提醒、每问附行动指令 |

### 2.3 Case 卡（5 张）

| id | 标题 | 来源素材 | 核心要求 |
|:---|:---|:---------|:---------|
| `case-compas-racial-bias` | COMPAS 再犯算法种族偏见 | 第四幕 | ProPublica 77.3% 数字；Northpointe 辩护；算法公平性启示；balanced 叙述 |
| `case-apple-card-gender-bias` | Apple Card 信用额度性别争议 | 第四幕 | DHH/Wozniak 投诉；NYDFS 最终结论；算法黑箱与监管回应；balanced 叙述 |
| `case-dutch-childcare-scandal` | 荷兰育儿补贴算法丑闻 | 第四幕 | 26,000 家庭；系统性伤害；政府辞职；算法问责教训 |
| `case-cambridge-novelists-survey` | 剑桥小说家对 AI 创作态度调查 | 第五幕 | 97% 反对整本书；样本范围（英国 258 位已出版小说家）；版权与 opt-in 偏好 |
| `case-chen-qiufan-ai-writing` | 陈楸帆对 AI 写作的态度转向 | 第五幕 | 2017 拥抱 → 2025 审慎；对抗式生成；中国作家网长文链接 |

---

## 3. 统一内容要求

### 3.1 Frontmatter 规范

```yaml
---
id: concept-ai-chair-determines-view
title: 椅子决定视角
type: concept
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.75
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
- "[[framework-wanghuan-ooda-loop]]"
- "[[framework-wanghuan-gan-three-roles]]"
---
```

**source_refs 必须精确**：逐字稿 + 王语嫣诊断/决策/任务文件。

**related 必须 ≥ 5**：必须包含 `ai-collaboration-domain-digest`、`framework-ai2041-critical-reading-os`，以及至少 1 张跨域卡片（如 strategy、research、yitang 域的 framework/case/tool）。

### 3.2 内容质量要求

1. **每个关键声明必须带 `[conf=X, source=...]` 标注**。王欢原创方法论统一 conf=0.70；外部可验证事实可至 0.85-0.90；市场数据口径差异大的必须降级并给区间。
2. **案例卡必须 WebSearch 补充独立来源**：COMPAS 需引用 ProPublica 原文；Apple Card 需引用 NYDFS 报告或权威媒体报道；荷兰育儿补贴需引用官方/学术报告；Cambridge 调查需引用 Minderoo Centre 官方报告；陈楸帆需引用中国作家网/新周刊原文。
3. **balanced 叙述**：COMPAS 和 Apple Card 必须并置反方观点（Northpointe 辩护、NYDFS 未违法结论），不能写成单向控诉。
4. **市场数据给区间**：deepfake / AI companion 等市场规模若引用，必须说明机构预测差异大，给出区间并注明口径。
5. **失败模式 ≥ 3 条**：每张 framework/tool/concept 卡必须包含失败模式表格。
6. **可迁移场景**：每张卡需说明在哪些其他情境下适用/不适用。

---

## 4. 执行顺序

建议按以下顺序分批生产，每完成一个类型可通知王语嫣提前看：

1. `concept-ai-chair-determines-view`
2. `concept-ai-neutrality-bias`
3. `tool-ai-cross-reading-method`
4. `tool-ai2041-source-verification-checklist`
5. `case-compas-racial-bias`
6. `case-apple-card-gender-bias`
7. `case-dutch-childcare-scandal`
8. `case-cambridge-novelists-survey`
9. `case-chen-qiufan-ai-writing`

---

## 5. 质量门禁

每张卡完成后必须自查：

- [ ] `id` 与文件名一致
- [ ] `status` = `enriched`
- [ ] `author` = `老顽童`
- [ ] `reviewed_by` = `欧阳锋`
- [ ] `source_refs` 非空且文件存在
- [ ] `related` ≥ 5，且至少 1 条跨域
- [ ] 每个关键声明有 `conf/source` 标注
- [ ] 案例卡有独立外部来源链接或引用
- [ ] 无死链（包括前向引用未生产卡片）
- [ ] 失败模式 ≥ 3 条

---

## 6. 验收与后续安排

- P1 9 张卡完成后，王语嫣按 20% 抽样（最少 3 张）做六层交叉验证。
- P1 通过后可继续执行 P2 批次 8 张卡：`dk-ai-prediction-expiry-date`、`dk-ai-social-progress-not-automatic`、`dk-ai-scarcest-resource-is-self`、`concept-ai-information-quality-ladder`、`case-deepfake-market-misuse`、`case-ai-companion-emotional`、`case-roblox-ai-npc-education`、`case-ai-job-displacement-wef`。
- P1/P2 全部完成后，再执行 `60_feedback/tasks/task_20260625_laowantong-synthesis-dk-cards.md` 中的 9 张跨案例 synthesis dk 卡。

---

*任务下达：王语嫣 | 日期：2026-06-25*
