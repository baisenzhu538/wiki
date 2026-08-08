---
id: task_20260808_laowantong-feature-thinking-w1
task_id: 249
assignee: laowantong
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-08
updated_at: 2026-08-08
domain: ai-basic
priority: P0
---

# #249 Feature 思维 W1 框架层（4 张 + 已有 5 张卡处置）

## 背景

W0（#248）完成后启动。框架层 4 张新卡 + **已有 5 张同主题卡的升级/合并/补链**（欧阳锋洞察 2 + 王语嫣独立扫描验证）。

## ⚠️ 硬约束：先处置已有卡，再写新卡（禁止直接新建导致重复）

**Feature 定义以 `10_raw/sources/feature-periodic-table-v0.8.json` 为准，禁止另起炉灶**（欧阳锋 #248 终审建议 + 王语嫣采纳）——卡内 Feature 术语、层级、维度全部引用 JSON，与 #248 保持一致。周期表收尾（#255 C1-C4）并行处理，不阻塞本任务。

| 已有卡 | 状态 | 处置 |
|:--|:--|:--|
| `tool-Truman-Feature特性层训练法` | draft | **升级**：补 source_refs（口述行号）+ 充实（四要素/五学派/T-F 分界）→ 与新 framework 互链 |
| `concept-yihang-ai-feature-thinking` | draft | **升级**：比对内容，作为新 framework 的入口卡或 related 合并 |
| `dk-demand-feature-stacking` | draft | **补链**：related 到新卡（Feature 组合的失败模式互补） |
| `tool-ai-feature-inventory` | draft | 不动正文——W3（#251）对账 merge |
| `concept-kdo-feature-registry` | draft（黄药师建） | 不动——W3（#251）双轨 bridge 卡处理 |

## 新卡规格（4 张，source_refs 全部带口述行号）

### 1. framework-truman-feature-thinking-core
- 四要素定义（AI/解题水平/实践单位/最小——口述上 L534-590）
- T 型 vs F 型思维分界（工具思维 vs Feature 思维，口述上 L462-510）
- 五大学派蛋黄图（原理/工程/工具/教程/模板 → Feature 派取中间，口述上 L1084-1218）
- related ≥5 跨域：[[tool-Truman-Feature特性层训练法]]、[[framework-一堂-关键假设]]、[[framework-一堂-刻意练习]]、[[concept-一堂-Agent基本功修炼]]、[[yt-decision-y-model]]

### 2. framework-truman-feature-layered-system
- L0-L5 六层（模型/提示词/技能/Agent/Opencl/组织架构）+ 分层自洽（"如无必要勿增实体""下层能解决不上上层"）
- bridge 到 ai-collaboration skills 族（L2 技能层 ↔ skill 封装；L3 Agent 层 ↔ agent-spec）
- related ≥5：[[ai-collaboration-harness]]、[[ai-collaboration-ooda]]、[[concept-一堂-Agent基本功修炼]]、[[framework-一堂-关键假设]]、[[agent-spec-复盘教练]]

### 3. concept-truman-feature-four-scenarios
- 四场景矩阵：事×短期=解题地图（假设实验）/ 事×长期=无限调优 / 人×短期=刻意练习 / 人×长期=共同坐标系
- 每场景：KDO 工作流映射（解题地图↔诊断三方法 / 无限调优↔编排迭代 / 刻意练习↔技能进化日志 / 共同坐标↔跨角色翻译——"向所有人兼容"口述下 L980-1034）
- related ≥4

### 4. concept-truman-feature-six-stages
- 六阶段：偶遇(听)→理解(想)→尝试(做)→内核(成)→边界(败)→肌肉记忆(练)
- "feature 不是学会的，是用会的"（口述下 L816-858）——五/六阶段是卡片生命周期的同构
- related ≥3

## 验收标准

1. 已有 5 张卡处置完成（升级/补链有 git diff 证据，无重复新建）

---

## 补审记录（欧阳锋 2026-08-08）

**结论：FAIL（退回修正）**——4 张新卡内容质量 B+（溯源扎实/定位声明 5/5/JSON 一致性遵守），但验收 1 未完成（1 张已有卡未处置）+ 死链 1 处 + 结构/溯源问题 4 处。framework 卡是最高优先级审查对象，退回修复（修复量小，非重做）。

### 通过项（O0 溯源核实）

| 卡 | 定位声明 | related | 溯源核验 |
|:--|:--|:--|:--|
| framework-core | ✅ L62 | 8 | 四要素 L534-590 ✅、T/F 分界 L462-510 ✅、五学派 L1084-1218 ✅ |
| framework-layered | ✅ L58 | 6 | 层数分布 3/14/34/14/18/13 与 #248 JSON 完全一致 ✅（硬约束遵守）|
| concept-four-scenarios | ✅ L53 | 5 | 四场景 L80-110 ✅、引用 L130-132/L816-858 ✅ |
| concept-six-stages | ✅ L52 | 4 | 六阶段 L816-858 ✅、KDO 生命周期同构 ✅ |

- **已有卡处置（git diff 证据）**：tool-Truman-Feature 升级 ✅（src_unknown→3 真实源+related 补链）；dk-demand-feature-stacking 补链 ✅（+5 行）
- Critique/When NOT to Use：framework×2 质量高（真实攻击）；concept×2 **缺**

### 修复清单（6 项，退回老顽童）

1. **🔴 concept-yihang-ai-feature-thinking 未处置**：任务单明确要求"比对内容，升级为入口卡或 related 合并"——实测 0 改动（updated_at 仍 7/4）。处置后给 git 证据
2. **🔴 死链 `framework-一堂-刻意练习`**：core/four-scenarios/six-stages 三张卡 related 引用不存在。实际存在：`concept-一堂-基本功-刻意练习四要素` / `deliberate-practice-four-elements`——改为真实 id
3. **🟡 framework-layered L81 引号行号错位**："能在下一层实现的功能，优先选择下一层实现"标 L334——L334 仅"分层自洽很好使"；定义句实际在口述上 L1300-1302 或笔记。改行号
4. **🟡 concept×2 缺 Constraints/边界节**（分级审查矩阵 concept 硬检查项）：four-scenarios 仅 1 个 section（无边界/无 When NOT to Use）；six-stages 无 Constraints/Critique——参照 framework 卡 When NOT to Use 格式补齐
5. **🟡 four-scenarios L110 演绎例子未标**："说的是同一个Feature：上下文增强"是演绎（口述原文是技术/运营/老板"各说各话"）——标注"演绎示例"或改为口述原意
6. **🟡 framework-core 外部攻击者仅 1**（P1 检查 ≥2）：补 1 个攻击者（如原理派："不学原理，Feature 拆解是空中楼阁"）

**🟢 观察（不阻塞）**：framework-layered L58 "96 Feature"写死（#248 补齐后 100）。

---

## 复审记录（欧阳锋 2026-08-08 R2）

**结论：PASS，等级 A-**。6 项修复清单全部独立核验通过（O3 实测，非采信报告），新增节内容质量高（非凑数）。

| # | 修复项 | 状态 | 实测证据 |
|:--|:--|:--:|:--|
| 1 | concept-yihang-ai-feature-thinking 处置 | ✅ | related +3（feature-thinking-core/layered/four-scenarios）实测命中 |
| 2 | 死链 framework-一堂-刻意练习 ×3 | ✅ | core/four-scenarios/six-stages 全部改为 `concept-一堂-基本功-刻意练习四要素`（目标存在）|
| 3 | layered L81 行号 | ✅ | 改 L330-334 + 标注"Skill分层自洽概念"——L332-334 确有"Skill…分层自洽很好使"，诚实标注 |
| 4 | concept×2 Constraints | ✅ | 各 +When NOT to Use + Critique；内容真实（four-scenarios：翻译者依赖；six-stages：纯学习者无项目可练）|
| 5 | four-scenarios L110 标注 | ✅ | "⚠️ 演绎示例，非口述原文" |
| 6 | framework-core 第二攻击者 | ✅ | L133 教程/模板派攻击者 + 回应，与第一攻击者（工具派）异质 |

**#250 L54 同步确认**：dk-key-hypothesis L54 已改 L388-392，与 source_context L14/L60 三处统一 ✅

**解锁确认**：依赖链 #248 ✅ → #249 ✅ → #250 ✅ —— **#251 补链部分依赖全满足**（剩部署层次 2/3 待黄药师）。
2. 新卡 pre-submit PASS；lint 0 新增；定位声明有
3. source_refs 带口述行号（一等证据，禁止只引笔记/图）
4. 卡内 Feature 术语与周期表 JSON（#248）一致

## 依赖

- #248 reviewed（周期表结构化完成，术语统一依据）
