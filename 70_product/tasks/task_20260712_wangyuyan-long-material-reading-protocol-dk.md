---
id: task_20260712_wangyuyan-long-material-reading-protocol-dk
title: dk 卡：长素材分层读取协议（子代理外存 + 行号锚点 + 三道防线）
status: queued
priority: P2
assignee: 老顽童
reviewer: 欧阳锋
expected_cards: 1
expected_agent_specs: 0
source_refs:
- 30_wiki/personal-os/wangyuyan-working-protocols.md（一等原文，王语嫣工作协议）
- 70_product/tasks/task_20260711_wangyuyan-fundamentals-domain-production.md（#150 实例：行号锚点 source_refs）
- 60_feedback/diagnosis/diag_20260711_yitang-fundamentals-deep-dive.md（证据三等与裁定实例）
related:
- '[[wangyuyan-working-protocols]]'
- '[[dk-research-decision-first-mapping]]'
- '[[dk-yihang-non-expert-judgment]]'
created_at: '2026-07-12'
updated_at: '2026-07-12'
---

# dk 卡：长素材分层读取协议

> 来源：老朱 2026-07-12 提问「口述稿密度大但长，全读爆上下文、只读笔记漏暗知识，你怎么解决？」→ 王语嫣作答的三件套机制。已写入 `30_wiki/personal-os/wangyuyan-working-protocols.md`（王语嫣自用一等原文），本任务将其军团共享化为 dk 卡。
>
> **时机**：明天 C/D 域（业务公式 101 图 VLM + YAI 素材）生产即用到此协议——老顽童/洪七公/未来 agent 都会遇到长素材。**建议 hermes 实例空档优先领**（半小时量级）。

---

## 一、目标产出

### `30_wiki/dark-knowledges/dk-long-material-layered-reading-protocol.md`（新，1 张 dk）

**核心内容**（以 `wangyuyan-working-protocols.md` 协议 1 为一等原文，不得缩水）：

1. **问题**：长素材（口述逐字/百图 VLM）密度大但长——全读爆上下文，只读笔记漏暗知识。
2. **三件套机制**：
   - ① 密度×长度选策略：短而密→亲自全读；长而稀→子代理精读回传行号索引；冲突点→定点复核下场。
   - ② 子代理外存 + 行号锚点：子代理独立窗口扛全量，回传可回溯指针（source_refs 带行号）；核实按行号定点读。
   - ③ 三道防线：提取清单防漏 / 定点复核防错 / 终审兜底。
3. **暗知识捕捞清单**：反复强调 / 临场案例 / 与笔记冲突 / 数字比例 / 语气词。
4. **证据三等**：实物图 VLM = 口述逐字（一等）> 笔记（二等）；冲突一等压二等。实例：「拆建推练」裁定、40 卡数量 6/7/7/20。
5. **Failure Modes（边界，重点）**：
   - 短而密素材（prompt/关键图/整合笔记）委托子代理 = 犯罪，必须亲自全读。
   - 子代理回传只能建索引，不能下判决；判决必回一等证据。
   - 行号区间粗是设计不是缺陷（粗索引+定点精读=最低成本的准确）。
6. **实例**：#150 基本功域全流程（4 口述上万行→2 explore agent→行号回传→定点裁定→零返工）。
7. **frontmatter**：`type: dark-knowledge`，`reviewed_by: 欧阳锋`，`status: draft`（待终审）；related 回链 `[[wangyuyan-working-protocols]]`。

---

## 二、验收标准（欧阳锋终审）

- [ ] 通过 pre-submit（YAML/WIKILINK/DK_SECTION，`reviewed_by: 欧阳锋`）。
- [ ] 三件套机制完整无缩水；含暗知识捕捞清单与证据三等。
- [ ] 含 #150 实例与 Failure Modes 三条。
- [ ] related 双向回链 personal-os 原文。

---

## 三、依赖与阻塞

- **依赖**：无（一等原文已就绪）。
- **阻塞**：不阻塞任何在产任务；hermes 空档可立即领。
- **边界**：只新增 1 张 dk；不碰在产任务文件。

---

## 四、最终判断

- 评级：**B+**（轻量但高复用——agent 军团每个成员都会遇到长素材；明天 C/D 域即验证）。
- 编号 **#154**；`status: queued`；assignee 老顽童；reviewer 欧阳锋。

*王语嫣编排 · 2026-07-12*
