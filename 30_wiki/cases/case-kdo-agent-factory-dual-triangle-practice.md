---
id: case-kdo-agent-factory-dual-triangle-practice
title: KDO 多 Agent 工厂：人机协作双三角的组织化实践
type: case
status: reviewed
author: 王语嫣
reviewed_by: 欧阳锋
reviewed_at: 2026-07-04
confidence: 0.75
trust_level: medium-low
language: zh-CN
created_at: 2026-07-04
updated_at: 2026-07-04
domain:
- yitang
- ai-saas
- personal-os
source_refs:
- .agent/context.md
- 70_product/tasks/production-queue.md
- 70_product/tasks/dashboard.md
- 60_feedback/tasks/task_20260703_huangyaoshi-agent-tcpr-role-layer.md
- 60_feedback/tasks/task_20260703_laowantong-graphrag-orphan-reduction.md
related:
- "[[人机协作决策-双三角模型]]"
- "[[concept-AI时代双三角竞争力]]"
- "[[yt-decision-y-model]]"
- "[[system-yitang-Y-model-os]]"
- "[[agent-native-card-design]]"
- "[[tool-opc-sales-dialogue-assistant]]"
- '"[[case-yihang-dual-triangle-tianmo-design-delivery]]"'
- '"[[case-yihang-dual-triangle-ahao-product-selection]]"'
- '"[[case-yihang-dual-triangle-huazao-synthetic-data]]"'
- '"[[case-yihang-dual-triangle-chentian-knowledge-agent]]"'
---

# KDO 多 Agent 工厂：人机协作双三角的组织化实践

## 背景

2026-07-03 至 2026-07-04，用户（KDO 知识工厂所有者）在 Kimi Code CLI 中与「王语嫣」Agent 进行了一轮密集的队列与方向维护工作。期间涉及 #53-#61 多个任务的审阅、领取、状态同步，以及 #28 lint 内容债第七批/第八批的审查协调。

在对话中，用户提出一个战略判断：

> 「双三角模型域是未来一堂最重要的域，重要性不亚于一堂五步法。」

随后要求王语嫣把当前对话协作本身作为双三角模型的实例，写成 case 卡草案。

## 决策与行动

### 人的三角

| 角色 | 对应人的三角 | 具体行为 |
|:---|:---|:---|
| 用户 | 创造力 + 判断力 | 提出「双三角域 = 五步法级战略域」的判断；决定任务是否插队；批准 case 卡草案撰写 |
| 王语嫣（Content Consultant / Direction Gatekeeper） | 体系 | 维护 production-queue.md、dashboard.md、context.md；确保队列规则、角色分工、状态机被正确执行 |
| 欧阳锋子代理 | 判断力 | 对 #53、#54、#60、第七批、第八批进行质量终审，给出 pass/fail/pass with reservations |
| 老顽童 / 黄药师 | 执行力 | 领取并生产 #54、#57、#58、#59、#61 等任务 |

### AI 的三角

| 角 | 具体行为 |
|:---|:---|
| 场景适配 | Kimi 把通用能力适配到「队列维护」「子代理审查」「任务单编写」「dashboard 更新」等具体场景 |
| 数据包 | 实时 Read production-queue.md、context.md、任务单、source refs、概念卡；上下文即数据包 |
| 基本功 | Bash、Read/Edit/Write、Agent 工具、kdo query、queue_transition.py 等工具链 |

### 关键动作链

1. 用户汇报 #53 完成 → 王语嫣更新 context/dashboard，派欧阳锋子代理审查。
2. 用户通知 #58 完成 → 王语嫣同步 #57/#58 reviewed，释放 #59（黄药师）和 #61（老顽童）。
3. 第七批/第八批 lint 清理完成 → 王语嫣 spawn 欧阳锋子代理逐批审查，更新 #28 任务进度。
4. 用户要求把协作实例写成 case 卡 → 王语嫣直接产出本草案（用户 override）。

## 结果

- **队列状态清晰化**：#53-#58 全部 reviewed，#59/#61 明确可领取，#60 待正式状态变更。
- **审查带宽放大**：欧阳锋子代理在数分钟内完成多批次审查，人只在关键节点拍板。
- **战略洞察显性化**：对话协作本身验证了「双三角不是抽象框架，而是 KDO 工厂的底层运行结构」。

## 可迁移洞察

### 洞察 1：KDO 工厂是双三角的组织化实例

> 不是「AI 替代人审」，而是「AI 把审查带宽放大后，人只做最终价值判断」。

欧阳锋子代理可以并行审 10 张卡、跑 lint、读源码，但 verdict 的边界条件（pass with reservations 还是 fail）以及是否接受 reservations，必须由人决定。

### 洞察 2：人的三角中「体系」最容易被低估

用户/王语嫣维护的 queue_transition.py、production-queue.md、context.md 不是「软流程」，而是双三角能够运转的硬基础设施。没有状态机，AI 子代理会抢跑、重复审、漏审。

### 洞察 3：AI 的三角中「数据包」质量决定输出质量

当王语嫣 Read 了 `wangyuyan-context.md`、`context.md`、`production-queue.md` 后，后续判断明显更准确；当子代理没读到最新 context 时，容易给出与当前状态脱节的建议。

### 洞察 4：双三角之外还有「持续反馈循环」

KDO 的实际协作不是静态乘积，而是循环：

```
人给方向 → AI 执行 → AI/人审查 → 人拍板 → 状态更新 → 下一轮
```

这与王语嫣 context 中的「循环优先于深度」原则一致。

## 关键证据

| 证据点 | Before | After | 来源 / 可检验性 |
|:---|:---|:---|:---|
| 双三角从抽象框架落到角色分工 | 只有「人的三角 × AI 的三角」概念卡 | 用户=创造力+判断力、王语嫣=体系、欧阳锋子代理=判断力、老顽童/黄药师=执行力；Kimi=场景适配+数据包+基本功 | 本 case 文件「人的三角 / AI 的三角 / 关键动作链」表格 |
| TCPR 从人类能力模型升级为 Agent 身份协议 | `agent-native-card-design.md` 无 TCPR 字段；7 张 OPC agent-spec 未声明身份 | 13 个文件接入 `tcp_role` / `tcp_default_mode` / `tcp_switch_trigger` / `tcp_session_opening`；7 张 OPC agent-spec System Prompt 含身份声明；13/13 pre-submit PASS | `60_feedback/tasks/task_20260703_huangyaoshi-agent-tcpr-role-layer.md` 欧阳锋终审报告 |
| GraphRAG 健康度因跨域补链提升 | orphan 36%（1210/3394）、connected components 1235、health 65/100 | orphan 18%（621/3468）、components 669、health 90/100；578 张 orphan 卡新增 847 条 related | `60_feedback/tasks/task_20260703_laowantong-graphrag-orphan-reduction.md` 指标对比表；可复测 `kdo graph stats --health` |
| Agent Prompt 编译器解决模型无法 Read 文件问题 | Kimi/Hermes 不能读取本地文件，System Prompt 只能靠手动拼装 | 编译器代码通过，3 个试点编译产物 `kdo pre-submit` PASS，产出 2 项微债务并入 #62 | `70_product/tasks/production-queue.md` #59 备注；`70_product/tasks/dashboard.md` #59 行 |
| 状态机由手动编辑升级为脚本驱动 | 角色直接编辑 `status` / `reviewed_by`，曾出现抢跑、重复审、状态不一致 | `queue_transition.py` 内置 gate、锁、状态机校验；领取/完成/释放/终审全部走脚本 | `70_product/tasks/production-queue.md`「队列规则」第 8–9 条；可验证 `python 90_control/scripts/queue_transition.py --help` |
| queue_transition.py 按 frontmatter id 查找任务单修复 | #55 终审时 `review` 命令因 id 与文件名不一致而找不到任务单 | 黄药师修复查找逻辑 + 补 7 个回归测试，7/7 tests passed，#55 场景验证正确 | `.agent/context.md` blockers 与 next_session_hint；`70_product/tasks/production-queue.md` #60 备注 |

## 可迁移场景

- **多 Agent 知识工厂 / 内容管线**：用队列+状态机+子代理审查放大内容生产带宽，人只做方向与终审判断。
- **软件研发的代码审查流水线**：把 lint、单元测试、回归验证交给 AI 子代理批量跑，核心架构决策与合并审批保留给 Tech Lead。
- **销售 / 客服智能体军团**：把方法论卡编译为 agent-spec，按 TCPR 身份开场，Agent 给建议、销售代表做最终话术与合规判断。
- **教育 / 教练场景**：同一 Agent 在不同会话中切换 T（教学）/ C（咨询）/ P（实践）/ R（研究）身份，先声明目标再进入任务。
- **大型 GraphRAG / 知识图谱治理**：通过跨域 related 补链降低 orphan 比例，周期性监控图健康度，防止新卡持续孤岛化。

## 教训

- **先建硬结构，再放 Agent**：在让 AI 跑流程之前，先把队列规则、状态机、角色边界写成可执行文件（`production-queue.md`、`queue_transition.py`、角色 context），否则 AI 会抢跑、重复审、漏审。
- **Agent 做带宽，人做判断**：审查类工作可以交给子代理批量跑，但 verdict 的边界条件（pass / fail / pass with reservations）以及是否接受 reservations，必须由人拍板。
- **数据包完整度决定输出质量**：当 Agent 读了最新 `context.md`、`production-queue.md`、任务单和 source refs 后，判断会显著更准确；遗漏 context 时建议容易与当前状态脱节。
- **把抽象框架变成可执行字段**：双三角、TCPR 等框架只有落到具体字段（`tcp_role`、`tcp_default_mode`、agent-spec frontmatter）和 lint 规则里，才能避免停在概念层。
- **小步循环优于单点深度**：KDO 工厂的价值来自「人给方向 → AI 执行 → AI/人审查 → 人拍板 → 状态更新 → 下一轮」的持续循环，而非一次性的长链路推理。

## 失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| Agent 未读最新 context 就给出建议 | 子代理建议与当前队列状态脱节，例如推荐已 reviewed 的任务继续生产 | 会话启动协议强制先读 `.agent/context.md`、`production-queue.md`、任务单；将「数据包完整性」作为 pre-submit 前置检查 |
| 手动修改状态导致状态机紊乱 | 抢跑、重复审、同一任务被多个实例领取、`status` 与 `reviewed_by` 不一致 | 所有状态变更必须通过 `queue_transition.py`；脚本内置 gate、锁、状态机校验；禁止任何角色直接编辑 frontmatter 状态字段 |
| 子代理 verdict 噪声 | 同一批文件换实例/换模型后结论不同，例如 #60 欧阳锋子代理两次审查给出 fail，但其他实例可能直接 pass | 保留人工终审；对关键 verdict 引入多人/多实例校准；把 verdict 边界条件写进任务单验收标准 |
| 中央状态机单点故障 | `queue_transition.py` 出 bug（如按 id 找不到任务单）时全厂状态流转瘫痪 | 为脚本写回归测试（#60 修复后补 7 个 test）；关键路径定期跑 `pytest`；状态变更失败时回滚并报警 |
| 抽象框架停在概念层 | 团队能画双三角、谈 TCPR，但 agent-spec 卡里没有对应字段，System Prompt 不声明身份 | 把框架要求写入设计规范（`agent-native-card-design.md`）和 lint WARNING；新卡必须显式声明 `tcp_role` 与默认模式 |
| 用户对子代理给出模糊指令 | 说「你去审查一下」但没给任务 ID、文件路径、验收标准，子代理跑偏或漏审 | 任务单模板强制包含 ID、source_refs、验收标准；王语嫣在派生前先做「请求结构化」并把参数写进子代理 prompt |

## Critique

### 内部局限

1. **样本量为 1**：本 case 仅来自 KDO 这一个工厂的 2 天实践，不能推广到所有 AI 协作场景。
2. **基础设施已经成熟**：KDO 已有 queue_transition.py、角色 context、dashboard 等现成结构。从零开始搭建的团队不会立刻遇到这个级别的双三角。
3. **AI 仍依赖精确指令**：当用户说「你开子代理欧阳锋去审查」时，王语嫣需要明确知道任务 ID、文件路径、验收标准；模糊指令会导致子代理跑偏。

### 外部攻击

**Daniel Kahneman 的噪声批判**：即使人和 AI 都按同一套 KDO 流程工作，不同子代理实例对同一批文件的 verdict 可能差异巨大。本 case 中欧阳锋子代理两次审查 #60 给出 fail，但换一个人/实例可能直接 pass。框架减少偏差，不减少噪声。

**Henry Mintzberg 的管理教育批判**：把协作拆成「人的三角 × AI 的三角」六个维度，可能制造「知道框架 = 具备能力」的幻觉。真正的高手协作不依赖画三角，而是基于共同语境的快速适配。

**Nassim Taleb 的反脆弱性质疑**：KDO 工厂越是依赖 queue_transition.py 这类中央状态机，一旦该脚本出 bug（如 #60 修复前按 id 找不到任务单），整个工厂越容易瘫痪。强耦合带来脆弱性。

## Synthesis

### 关联已有卡

| 关系 | 目标节点 | 说明 |
|:---|:---|:---|
| 理论框架 | [[人机协作决策-双三角模型]] | 本 case 是该框架在 KDO 工厂中的实例化 |
| 能力结构 | [[concept-AI时代双三角竞争力]] | 人的三角（创造力/体系/判断力）+ AI 的三角（场景适配/数据包/基本功） |
| 决策基础 | [[yt-decision-y-model]] | KDO 队列优先级判断本质是 Y 模型在运营层面的应用 |
| 运行时 OS | [[system-yitang-Y-model-os]] | KDO 角色 context 与 TCPR 身份协议是双三角运转的「操作系统」 |
| 设计规范 | [[agent-native-card-design]] | Agent 卡片的结构设计直接影响 AI 能否正确填充「数据包」 |

### 不要用本 case 的场景

| 场景 | 为什么失效 | 替代方案 |
|:---|:---|:---|
| 团队没有现成 KDO/队列基础设施 | 双三角需要硬结构支撑，否则 AI 会乱跑 | 先建最小状态机，再谈 Agent 协作 |
| 单次性、非重复任务 | 本 case 的价值来自循环反馈，单次协作无法复利 | 使用简单提示词工程即可 |
| 高 stakes 决策且没有人工终审 | AI 子代理可能给出错误 verdict | 必须保留人工终审环节 |

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|:---|:---|:---|
| 团队想引入 AI Agent 协作 | 先定义角色、队列、状态机，再让 AI 跑流程 | 任何状态变更都可追溯、不依赖人工记 |
| AI 审查结果与人工判断频繁冲突 | 检查「数据包」是否完整：AI 是否读了最新 context、任务单、验收标准 | 冲突率下降 |
| 双三角模型讨论停留在概念层 | 找一个真实协作实例（如本 case）画出来：哪一步是人的三角，哪一步是 AI 的三角 | 团队能指出具体交互点 |
