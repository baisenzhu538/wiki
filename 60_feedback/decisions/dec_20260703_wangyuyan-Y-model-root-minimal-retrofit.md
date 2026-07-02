---
id: dec_20260703_wangyuyan-Y-model-root-minimal-retrofit
title: "王语嫣裁定：Y模型根节点化走轻量 retrofit，三条线并行"
type: decision
status: confirmed
author: 王语嫣
reviewer: 欧阳锋
created_at: 2026-07-03
updated_at: 2026-07-03
domain:
  - kdo
  - epistemic-foundations
  - yitang
source_refs:
  - "60_feedback/tasks/task_20260703_huangyaoshi-proposal-kdo-next-phase-orchestration.md"
  - "60_feedback/tasks/task_20260703_laowantong-yitang-Y-model-foundation-production.md"
  - "60_feedback/tasks/task_20260703_huangyaoshi-yitang-Y-model-root-infrastructure.md"
related:
  - yt-decision-y-model
  - framework-yitang-shishi-qiushi
  - framework-yitang-jiefang-sixiang
  - yt-entrepreneur-scientific-method
  - yt-entrepreneur-truth-seeking
  - yt-model-liberate-thinking-layers
  - tool-yitang-Y-model-application
  - dk-yitang-Y-model-pitfalls
  - case-yitang-Y-model-seven-applications
  - case-yitang-Y-model-advertising-turnaround
  - agent-native-card-design
  - opc-ai-sales-agent-architecture
  - tool-opc-sales-dialogue-assistant
---

# 王语嫣裁定：Y模型根节点化走轻量 retrofit，三条线并行

> 针对黄药师建议书 `task_20260703_huangyaoshi-proposal-kdo-next-phase-orchestration.md` 的独立判断。

---

## 一、总体判断：采纳，但做减法

黄药师的 **Phase shift** 判断成立：KDO 已从「理论臂建体系」进入「事实臂验证」阶段。三条线并行的大框架采纳。

但我对 **线 A 的执行粒度** 做减法：
- ✅ 采纳：不重造 schema、不新增 card type、不建新目录。
- ✅ 采纳：把现有 `yt-decision-y-model` 重写升级为 KDO 根节点卡。
- ✅ 采纳：黄药师本周只做 GraphRAG rebuild + pipeline 监控，不新增工具。
- ❌ 不采纳原 `#52` 中的 schema 层改造（`is_root_node` / `replaces` / `deprecated_by`、lint 新规则、deprecation 文档化）。这些推迟到 Agent 闭环跑通后再评估。
- ❌ 不采纳原 `#51` 中「新建 `framework-yitang-Y-model`」的做法；改为就地重写 `yt-decision-y-model`，避免 ID 漂移和 deprecation 债务。

---

## 二、线 A 具体方案

| 动作 | 负责人 | 产出 | 备注 |
|:---|:---|:---|:---|
| 重写 `yt-decision-y-model` | 老顽童 | 从「科学决策域 framework」升级为「KDO 根节点 framework」 | 保留原 ID，标题可改为「Y模型：一堂科学做事系统」；正文加入四层结构、理论臂/事实臂/知行合一轴、与 KDO 工厂的映射 |
| 所有 framework/concept/tool 卡 related 补 `[[yt-decision-y-model]]` | 老顽童（批量） | 理论臂归属清晰 | 只补 related，不改目录/类型 |
| 所有 case/dk 卡 related 补 `[[yt-decision-y-model]]` | 老顽童（批量） | 事实臂归属清晰 | 同上 |
| GraphRAG rebuild | 黄药师 | Y模型成为查询入口节点 | 等线 A 前两步完成后执行 |
| `yt-entrepreneur-scientific-method` 加迁移提示 | 老顽童 | 旧卡顶部加「本卡已被 `yt-decision-y-model` 重写升级」 | 不引入 `deprecated_by` schema 字段；可用现有 `status: deprecated` 标记 |

---

## 三、#51 调整

原 `#51` 目标 7 张卡不变，但 **Card 1 从新建 `framework-yitang-Y-model` 改为重写 `yt-decision-y-model`**。

调整后的 7 张卡：
1. `yt-decision-y-model`（重写升级，根节点）
2. `framework-yitang-shishi-qiushi`（新建）
3. `framework-yitang-jiefang-sixiang`（新建）
4. `tool-yitang-Y-model-application`（新建）
5. `dk-yitang-Y-model-pitfalls`（新建）
6. `case-yitang-Y-model-seven-applications`（新建）
7. `case-yitang-Y-model-advertising-turnaround`（新建）

旧卡处理：
- `yt-entrepreneur-scientific-method` → 顶部加迁移提示指向 `yt-decision-y-model`，可标记 `status: deprecated`。
- `yt-entrepreneur-truth-seeking` → 顶部加迁移提示指向 `framework-yitang-shishi-qiushi`，可标记 `status: deprecated`。
- `yt-model-liberate-thinking-layers` → 顶部加迁移提示指向 `framework-yitang-jiefang-sixiang`，可标记 `status: deprecated`。

> 说明：实事求是/解放思想仍新建 framework 卡，因为原旧卡是 concept 层 stubs，内容无法直接承载新课素材；但旧卡保留并加迁移提示，避免链接断裂。

---

## 四、#52 调整

原 `#52`（schema + GraphRAG + deprecation 基础设施）范围过大，与「黄药师本周只做维护」冲突。

调整后 `#52`：
- **标题**：Y模型根节点化：GraphRAG rebuild + 批量 related 后的索引维护
- **负责人**：黄药师
- **内容**：
  1. 等线 A 完成后执行 `kdo index --rebuild`。
  2. 验证 `yt-decision-y-model` 成为查询扩散的默认中心节点。
  3. `kdo pipeline` 持续监控，观察 Agent 反馈是否产生新的 lint/链接信号。
  4. 不新增 schema 字段、不新增 lint 规则、不新增工具。
- **依赖**：线 A 完成（`yt-decision-y-model` 重写 + 批量 related）。

原 schema/deprecation 字段设计进入 `#52-backlog` 或黄药师停车场，待 Agent 闭环跑通后再评估。

---

## 五、线 B 与 #50 的关系

- 线 B（Agent 闭环）与 #51 可并行。
- 老顽童**现在就可以领取 #51**，不必等欧阳锋审完 #50。
- 欧阳锋审 #50 若提出修订，相关反馈直接进线 B 的回流清单，不阻塞 #51 的理论臂建设。
- 线 B 的产出（实测日志、case 归档）由王语嫣判断是否回流到 `tool-opc-sales-dialogue-assistant` 及相关方法论卡。

---

## 六、线 C 安排

- `#44` 销售域卡片生产：保持队列不变，继续推进。
- `#42` 暗知识补挖：保持队列不变，王语嫣用一句话金矿扫描产出清单后，老顽童执行建卡/补链。

---

## 七、不要做的事（强化版）

- ❌ 不要为 Y模型新建卡片或新 ID。
- ❌ 不要新增 schema 字段（`is_root_node` / `replaces` / `deprecated_by`）。
- ❌ 不要新增 card type 或目录。
- ❌ 黄药师不要新增 `--agent-trace` 工具；先用手工迭代日志。
- ❌ 不要把「跨域模式层」目录化；继续留在停车场。

---

## 八、下一步动作

1. 老顽童立即领取 `#51`，先执行线 A 的 `yt-decision-y-model` 重写 + 批量 related。
2. 黄药师待命，线 A 完成后执行 `#52` GraphRAG rebuild。
3. 欧阳锋继续审 `#50`，审完直接进线 B 回流。
4. 王语嫣监控三条线并行，必要时做再平衡。

---

*王语嫣 2026-07-03*
