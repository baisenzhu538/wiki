---
id: task_20260711_wangyuyan-decision-coach-agent-supplement
title: 决策域补产：科学决策教练 agent-spec（orchestrator）+ 三角形卡脏数据清理
status: queued
priority: P1
assignee: 老顽童
reviewer: 欧阳锋
expected_cards: 1
expected_agent_specs: 1
source_refs:
- 30_wiki/frameworks/framework-科学决策三角形.md
- 30_wiki/domains/decision-science-domain-digest.md
- 30_wiki/concepts/concept-科学决策宽度.md
- 30_wiki/concepts/yt-decision-width-method.md
- 30_wiki/concepts/yt-decision-depth-ladder.md
- 30_wiki/concepts/yt-decision-height-toolkit.md
- 30_wiki/frameworks/yt-decision-abcd-model.md
- 30_wiki/concepts/yt-decision-canvas.md
- 30_wiki/concepts/yt-decision-full-process.md
- 30_wiki/concepts/yt-decision-review.md
- 30_wiki/dark-knowledges/dk-ai-judgment-human-responsibility.md
related:
- '[[framework-科学决策三角形]]'
- '[[decision-science-domain-digest]]'
- '[[agent-spec-yitang-Y-model-cross-domain-coach]]'
- '[[agent-spec-yitang-dual-triangle-cross-domain-diagnostician]]'
created_at: '2026-07-11'
updated_at: '2026-07-11'
---

# 决策域补产：科学决策教练 agent-spec + 三角形卡脏数据清理

> 王语嫣盘点结论（2026-07-11）：决策域是 KDO 最厚的大域之一，宽度/深度/高度三度齐全（科学决策三角形），域摘要 `decision-science-domain-digest` 已 reviewed，成熟度 **A-**——**不立大生产任务**。唯一缺口：决策域是**唯一没有专属 agent-spec 的大域**（`.agent/prompts/` 35 个 spec：五步法/机会预判/关键假设/表达力/学习方法/时间管理/需求分析/基本功全有 orchestrator，决策域没有）。故立本轻量任务补 agent-spec + 顺手清三角形卡脏数据。
>
> **领取节奏**：老朱指示"任务先编排好"——本任务 `queued` 入队，领取时间由老朱定（不抢 #150/#151/#152 产能，可与基本功三线任意先后）。

---

## 一、目标产出

### 产出 1：`.agent/prompts/agent-一堂-科学决策教练.md`（新，orchestrator）

**System Prompt 核心**：

1. **主线**：科学决策三角形（宽度×高度×深度）——任何决策先三维自查（宽度列全？高度四维？深度至少 L2？），短板维先补。
2. **调度资产**（按场景路由）：
   - 宽度：`concept-科学决策宽度` / `yt-decision-width-method`（列推建查四步法 + 三层盲区）
   - 深度：`yt-decision-depth-ladder` + `tool-决策深度-L1优先级定性` / `L2部分定量` / `L3定量公式` / `L4严格财务公式` + `tool-完整财务公式决策`；`dk-决策经验值` / `dk-你的业务是一次抽样实验`
   - 高度：`yt-decision-height-toolkit`（上帝视角四维提升 + 高水平共识曲线）+ `concept-两种典型思考习惯` / `concept-X型Y型决策习惯` / `yt-decision-habit-shift`
   - 假设与验证：`yt-decision-abcd-model`（关键假设 ABCD）+ `framework-lean-pivot-decision`（转向/坚持）
   - 画布与流程：`yt-decision-canvas` / `tool-ROI决策评估画布` / `yt-decision-full-process`（五阶段）/ `yt-decision-review`（L1-L4 复盘）
   - 质量与偏差：`framework-decision-quality-checklist` / `framework-decision-cognitive-bias-map` / `master-decision-hygiene`
   - 团队对齐：`framework-高水平共识曲线` / `yt-decision-consensus-iceberg`
   - 人机协作：`人机协作决策-双三角模型` / `yt-decision-ai-partner` / `tool-decision-outside-view` / `tool-decision-delay-intuition` / `dk-decision-when-to-defer`
3. **TCPR 完整**（教学/咨询/实践/研究四段）；默认身份 C（协作者），重大决策升 S（严格质询：宽度盲区三轮"还有吗"+ 深度诚实打分对照 L1-L4）。
4. **When NOT to Use**：应急决策可降深度（L1 足够）但宽度/高度不能省；纯执行无判断空间的事不启动决策流程。
5. **边界（铁律）**：
   - **不替代人做最终决策**——AI 是外骨骼、决策责任在人（引 `dk-ai-judgment-human-responsibility`）；教练只负责"让决策更科学"，拍板与担责归人。
   - **不做跨域总入口分诊**（归 #143 双三角诊断 agent）。
   - **Y模型/实事求是/解放思想跨域问题**转 `agent-spec-yitang-Y-model-cross-domain-coach`（#142）。
   - 终局/机会预判类转 `agent-一堂-机会预判教练`（#147）。
6. **协议**：按 #143 跨域双三角诊断协议注册；按 #144 cap_hub 协议调用共享能力（VLM/OCR/搜索）。
7. **自评**：五维 Judge Skill 自检（标准/边界/坑/约束/门控），参照 #128/#129。

### 产出 2：`framework-科学决策三角形.md` 脏数据清理（1 卡升级）

- related 里 3 个 `pending_unknown` 补齐真实卡：`yt-decision-width-method` / `yt-decision-depth-ladder` / `yt-decision-height-toolkit`。
- "与已有框架的关系 = src_unknown" 补内容：本卡=三维总纲；宽度/深度/高度各有工具卡落地；上挂 `decision-science-domain-digest`；与 ABCD 模型（假设检验）互补——ABCD 管"假设质量"，三角形管"三维完备"。
- `pending_unknown` 清零。

### 产出 3：回链（收尾）

- `decision-science-domain-digest.md` related 追加 `[[agent-一堂-科学决策教练]]`（域摘要挂上新 orchestrator）。
- 新 agent-spec related 双向回链三角形/digest/#143/#144。

---

## 二、边界（与在产任务零冲突）

- **只新增 1 agent-spec + 升级 1 张已 reviewed 卡（三角形）+ digest 1 行回链**；不碰 #150/#151/#152 任何文件。
- 不新增方法论卡（域已成熟，方法论卡全 reviewed）；不为决策域立新 digest（已有）。
- 承接人=老顽童（产内容性质：agent-spec 属域 orchestrator，非工厂改造——黄药师不碰）。

---

## 三、验收标准（欧阳锋终审）

- [ ] agent-spec 通过 pre-submit；System Prompt 含主线三维自查 + ≥15 个真实 wikilink 资产 + TCPR + When NOT to Use + 三条边界。
- [ ] 三角形卡 `pending_unknown` 清零、"与已有框架的关系" 有实质内容。
- [ ] digest 回链闭环（新 spec ↔ digest ↔ 三角形 双向可达）。
- [ ] 注册：按 #143 协议登记，#143 诊断 agent 的域注册表可检索到"决策域→科学决策教练"。
- [ ] 未改动任何在产任务文件。

---

## 四、依赖与阻塞

- **依赖**：无（决策域卡全部 reviewed，可直接产）。
- **阻塞**：不阻塞 #150/#151/#152；亦不被其阻塞。
- **领取**：老朱定节奏（建议基本功三线收口后，或 hermes 实例空档时顺手）。

---

## 五、最终判断

- 评级：**A-**（轻量补缺，半张工单量；补齐"大域都有 orchestrator"的最后一块拼图，让 agent 沿决策域干活时有教练调度）。
- 编号 **#153**；`status: queued`；assignee 老顽童；reviewer 欧阳锋。

*王语嫣编排 · 2026-07-11*
