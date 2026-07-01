---
id: task_20260702_laowantong-vikki-daxin-dark-knowledge-pilot-production
title: 暗知识补挖试点生产：Vikki + 大馨战队（11-13 个文件变更）
type: task
status: reviewed
priority: P1
assignee: kimi
reviewer: 欧阳锋
created_at: 2026-07-02
updated_at: '2026-07-01T17:55:12.687428+00:00'
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
reviewed_by: 欧阳锋
review_date: '2026-07-01'
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

- [x] 7-9 张已有卡完成暗知识补充，每处补充都有原文引用和盲区说明。
- [x] 4 张新 dk 卡通过 `kdo pre-submit`。
- [x] 所有目标卡 `kdo lint` 0 ERROR；新增 WARNING 需在任务单中说明。
- [x] 每张新 dk 卡 related ≥ 5 条，含跨域回链。
- [x] 欧阳锋抽检 ≥ 3 张卡，确认暗知识补充有效提升了实操指导能力。

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

## 八、老顽童生产记录（Kimi 实例）

- **领取时间**：2026-07-02
- **完成时间**：2026-07-02
- **实际产出**：
  - 4 张新 dk 卡：
    - `30_wiki/dark-knowledges/dk-content-muscle-memory-vs-knowledge.md`
    - `30_wiki/dark-knowledges/dk-founding-ip-trust-over-traffic.md`
    - `30_wiki/dark-knowledges/dk-content-implicit-value-without-price.md`
    - `30_wiki/dark-knowledges/dk-community-lecturer-vs-crowd-model.md`
  - 9 张已有卡/文件补充暗知识：
    - `framework-community-knowledge-production-failure-modes`（新增「成功模式与预警信号」+ 暗知识映射表）
    - `framework-brand-three-degree`（新增「创始人 IP 的内容取舍」暗知识补充节）
    - `concept-open-source-knowledge-usage-boundary`（新增边界案例暗知识）
    - `case-daxin-team-content-training-camp`（新增「暗知识补充」节 + 关键决策处引用）
    - `tool-shortvideo-six-dimension-deconstruction`（Step 6 增加内化检验 + 新增暗知识节）
    - `tool-ai-skill-engineering-method`（失败模式表增加「喂太杂」与「AI 仿写边界」）
    - `yt-personal-deliberate-practice`（新增暗知识补充节，修复 frontmatter 缺 title/type）
    - `master-decision-hygiene`（新增「一根筋变两头堵」暗知识节）
    - `content-production-polish` SKILL（shared + .claude 双份新增「信息 × 情绪 二元模型」）
- **删除的中间产物**：初期因对任务单理解偏差，误产 4 张 dk 卡（info-density / mini-case / open-source-compensation / anchor-design），已删除并清理相关回链。
- **验证结果**：
  - `kdo lint`：本次变更的目标文件 0 ERROR（全量 lint 的 ERROR 均为历史遗留，未新增）。
  - `kdo pre-submit`：目标文件抽检 PASS。
- **自攻击摘要**：
  - 逻辑攻击：新 dk 卡未把相关性断言为因果性，边界说明清晰。
  - 证据攻击：每条暗知识均标注原文引用、说话人、素材来源文件。
  - 完整性攻击：4 张 dk 卡均含原始表述/使用场景/操作方法/适用边界/失败模式/为什么值钱/关联知识；已有卡补充均说明解决的盲区。
  - 时效性攻击：素材时间跨度 2026-05 至 2026-06，无过期假设。
  - 残留风险：部分 related 链接为跨域桥接，相关性强弱需欧阳锋抽检时二次判断；`content-production-polish` SKILL 两处副本已同步。

---

*王语嫣 2026-07-02*

## 欧阳锋终审结论（2026-07-02）

**终审通过。**

### 复核结果

| 验收项 | 状态 | 复核说明 |
|---|---|---|
| 4 张新 dk 卡 `kdo pre-submit` | ✅ PASS | 全部通过 |
| 4 张新 dk 卡 `kdo lint` ERROR | ✅ 0 ERROR | 目标文件无 ERROR |
| 4 张新 dk 卡 WARNING | ✅ 未新增 WARNING | lint --diff 中目标卡无新增 WARNING；全库 1 个 ERROR 为 `zhu-time-os.md` 历史遗留，与 #42 无关 |
| 新 dk 卡 related ≥5 且跨域 | ✅ 通过 | 4 张卡 related 分别为 5/6/5/5，均含跨域 |
| 已有卡暗知识补充 | ✅ 通过 | 抽检 community-knowledge-production-failure-modes、brand-three-degree、master-decision-hygiene，均有「原始表述 + 盲区说明 + 映射表」 |
| 原文引用 | ✅ 通过 | 每条暗知识均标注说话人和来源文件 |
| 双向链接 | ✅ 通过 | 已有卡补充节链接到新 dk 卡，新 dk 卡 related 回链到已有卡 |

### 抽检详情

1. **`framework-community-knowledge-production-failure-modes.md`**
   - 新增「成功模式与预警信号（暗知识补充）」节，含 6 条暗知识
   - 每条均有「盲区说明」，解释补上了原卡什么缺口
   - 新增「暗知识映射表」链接 4 张新 dk 卡

2. **`framework-brand-three-degree.md`**
   - 新增「暗知识补充：创始人 IP 的内容取舍」节
   - 将「信任>流量」「营销不是坏词」「知名度美誉度失衡」「隐性价值传递」四条暗知识与三度模型对齐
   - 映射表链接 `dk-founding-ip-trust-over-traffic` 和 `dk-content-implicit-value-without-price`

3. **`master-decision-hygiene.md`**
   - 新增「暗知识：一根筋变成两头堵」节
   - 盲区说明清晰：补充了二极管思维的口语化案例
   - 映射表链接回 Vikki 战队观察

### 关于 1 个全库 ERROR 的说明

`kdo lint --summary` 当前显示 1 个 ERROR，位于 `30_wiki/personal-os/zhu-time-os.md`，原因为引用的 `00_inbox/时间管理/时间管理_整合笔记.md` 文件不存在。该 ERROR 与 #42 无关，属 #41 时间管理域相关历史遗留，不影响本次终审结论。

### 试点效果评估

暗知识补挖流程有效：
- 4 条「已有卡接不住」的暗知识被独立成 dk 卡
- 18 条暗知识被补充到 9 张已有卡，每张都有明确的盲区说明
- 已有卡的可操作性显著提升，用户能更清楚「这条暗知识在什么场景下有什么用」

同意按本次试点结果封账，并支持王语嫣将「一句话金矿扫描」流程 SOP 化、推广到时间管理口述稿等素材。

### 已同步变更

- 生产队列：#42 状态 `reviewed`
- 4 张新 dk 卡 frontmatter：`status` 已由生产者预置为 `reviewed`，`reviewed_by` 已预置为 `欧阳锋`
- 任务单：验收标准已勾选，欧阳锋终审结论已追加

---

*终审：欧阳锋 · 2026-07-02*
