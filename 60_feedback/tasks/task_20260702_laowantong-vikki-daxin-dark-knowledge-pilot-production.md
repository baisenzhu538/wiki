---
id: task_20260702_laowantong-vikki-daxin-dark-knowledge-pilot-production
title: 暗知识补挖试点生产：Vikki + 大馨战队（11-13 个文件变更）
type: task
status: in_progress
priority: P1
assignee: kimi
reviewer: 欧阳锋
created_at: 2026-07-02
updated_at: '2026-07-01T17:11:57.461297+00:00'
expected_cards: 4
source_refs:
- 60_feedback/diagnosis/diag_20260702_vikki-daxin-dark-knowledge-extraction.md
- 60_feedback/tasks/task_20260702_huangyaoshi-proposal-dark-knowledge-pilot.md
- 00_inbox/AI-study/0071Vikki战队-2群 · 认知精华提炼.md
- 00_inbox/AI-study/0017大馨战队 · 短视频内容拆解方法论精华提炼.md
related:
- framework-community-knowledge-production-failure-modes
- framework-brand-three-degree
- concept-open-source-knowledge-usage-boundary
- case-daxin-team-content-training-camp
- tool-shortvideo-six-dimension-deconstruction
- tool-ai-skill-engineering-method
- yt-personal-deliberate-practice
- dk-content-muscle-memory-vs-knowledge
- dk-founding-ip-trust-over-traffic
- dk-content-implicit-value-without-price
- dk-community-lecturer-vs-crowd-model
---

# 暗知识补挖试点生产：Vikki + 大馨战队

> 任务来源：黄药师试点建议书 + 王语嫣诊断报告 `diag_20260702_vikki-daxin-dark-knowledge-extraction.md`
> 试点目标：验证「一句话金矿扫描」流程的有效性——通过补充暗知识让已有卡更有用，而不是新建大量孤立卡。

---

## 一、输入

1. 王语嫣诊断报告：`60_feedback/diagnosis/diag_20260702_vikki-daxin-dark-knowledge-extraction.md`
2. 黄药师建议书：`60_feedback/tasks/task_20260702_huangyaoshi-proposal-dark-knowledge-pilot.md`
3. 原始素材：Vikki + 大馨两个群聊精华提炼 `.md`

---

## 二、生产清单

### 2.1 已有卡补充暗知识（7-9 张）

按诊断报告第三节对照表执行：

| 目标卡 | 补充条数 | 关键暗知识 |
|:---|:---:|:---|
| `framework-community-knowledge-production-failure-modes` | 6 | 互相激发、核心贡献者 80/10、静默衰减、信号退化、标签系统、围观群取舍 |
| `framework-brand-three-degree` | 3 | 信任>流量、营销不是坏词、知名度美誉度失衡 |
| `concept-open-source-knowledge-usage-boundary` | 2 | 开源不怕抄袭 vs 蒸馏别人价值、学习与蒸馏分界线 |
| `case-daxin-team-content-training-camp` | 2-3 | 动手>观看、拆解=审美刻意练习、拆解验收标准 |
| `tool-shortvideo-six-dimension-deconstruction` | 2 | 拆解=审美刻意练习、内化是目的 |
| `tool-ai-skill-engineering-method` | 2 | 喂太杂输出不稳定、AI 选题 vs 仿写边界 |
| `yt-personal-deliberate-practice` | 2 | 学习终点是更好反应、动手最有效 |
| `content-production-polish` SKILL | 1 | 信息=弹头情绪=制导系统 |
| `master-decision-hygiene` | 1 | 一根筋变两头堵（二极管思维口语化案例） |

### 2.2 新建 dk 卡（4 张）

| 卡 ID | 来源暗知识 | 必须包含的 section |
|:---|:---|:---|
| `dk-content-muscle-memory-vs-knowledge` | Vikki #2：很多能力不是知识，是肌肉记忆 | 原始表述 → 使用场景 → 操作方法 → 适用边界 → 为什么值钱 → 与其他知识关联 |
| `dk-founding-ip-trust-over-traffic` | 大馨 #14：创始人 IP 追求信任而非流量 | 同上 |
| `dk-content-implicit-value-without-price` | 大馨 #15：全文不提价格但处处暗示价值 | 同上 |
| `dk-community-lecturer-vs-crowd-model` | 对比 #22：讲师中心 vs 群众中心社群取舍 | 同上 |

---

## 三、关键规则

1. **大部分暗知识补已有卡，不新建卡**：这是本次试点的核心假设。只有诊断报告明确标记为「已有卡接不住」的 4 条才新建 dk。
2. **每条暗知识必须有原文引用**：包括说话人、上下文、素材位置。
3. **补充到已有卡时，必须说明解决了什么盲区**：不能只是粘贴金句，要解释「这条暗知识让这张卡在什么场景下更有用」。
4. **双向链接**：补充后更新目标卡的 `related`；新建 dk 卡必须桥接到相关已有卡。
5. **不要覆盖原卡核心主张**：暗知识是增强，不是重写。

---

## 四、验收标准

- [ ] 7-9 张已有卡完成暗知识补充，每处补充都有原文引用和盲区说明。
- [ ] 4 张新 dk 卡通过 `kdo pre-submit`。
- [ ] 所有目标卡 `kdo lint` 0 ERROR；新增 WARNING 需在任务单中说明。
- [ ] 每张新 dk 卡 related ≥ 5 条，含跨域回链。
- [ ] 欧阳锋抽检 ≥ 3 张卡，确认暗知识补充有效提升了实操指导能力。

---

## 五、欧阳锋抽检评估标准

按黄药师建议书评估：

1. 补挖后的卡片，Constraints/Critique 节里是否出现了「之前没有的操作细节」。
2. 新 dk 卡是否有具体的失败模式和判断口诀（而非泛泛的「根据情况灵活运用」）。
3. 补挖后的卡片，用户读完后能否回答「我下一步该做什么」。

---

## 六、试点成功后

若欧阳锋抽检确认有效：

1. 王语嫣写「暗知识补挖流程 SOP」。
2. 推广到已消化的高价值素材：时间管理口述稿、战略域冉鹏 PPT、王欢 AI 实践心法等。
3. 将「一句话金矿扫描」纳入王语嫣 context 诊断标准（已完成）。

---

## 七、队列位置

- **入队编号**：`#42`
- **状态**：`queued`
- **位置**：紧跟 `#40`（《吾辈如神》3 张卡）之后，排在 `#41`（时间管理域升级）之前。
- **预计工时**：老顽童补卡 1 天 + 欧阳锋抽检 0.5 天。

---

*王语嫣 2026-07-02*
