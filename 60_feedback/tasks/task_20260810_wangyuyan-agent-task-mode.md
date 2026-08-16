---
id: task_20260810_wangyuyan-agent-task-mode
assignee: claude
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-10
updated_at: '2026-08-09T17:36:11.933611+00:00'
priority: P1
wsjf: 3.0
---

# Agent 任务模式编排（#310 · spec 任务上下文模板化 + 素材收集协议）

## 任务目标

借鉴 WorkBuddy"任务式生成"（对话上下文→交付物）——飞书 agent 从"对话式应答"升级为"任务式生成"：**spec 升级为运行时生效的任务上下文模板，每次任务 phase 按五节组织**。

## 背景（用户对齐确认 2026-08-10）

- WorkBuddy 模式拆解（00_inbox/老朱的个人域/如何认识一个人-用户维度-对话上下文.md + 附件.md）：任务背景封装/素材结构化/跨域桥接/第一人称交付/待确认闭环
- 用户确立：①素材收集器 = **多轮对话出口式咨询**（疑点必问，挖到不能深不能再挖——Truman 出口式咨询：找出口→换视角→探究解法）②spec 必须有作用（运行时生效，不是评审完放着）
- 试点 agent：教练式领导力助理（老朱个人域任务：拆书/复盘/文章最贴合）

## 规格（核心产出 3 项）

1. **spec 任务上下文模板化**（教练助理 spec 升级版——E025 另开）：
   - 五节任务模板：①任务背景封装（来源/交付物/输出路径）②素材收集协议（出口式咨询多轮深挖）③知识库检索（已读卡清单+引用卡名）④交付物（形态+第一人称）⑤待确认闭环（2-4 个待确认问题）
2. **素材收集协议**（出口式咨询协议化）：复用 tool-leadership-exit-consulting + tool-leadership-questioning-cards——疑点必问、每轮追问（"为什么觉得是认知问题不是执行问题？"）、直到挖到不能再深
3. **交付物第一人称化**：调用 content-production-polish（去 AI 味）+ 真实素材嵌入（用户经历结构化）

## 验收标准

- spec 含五节任务模板 + 基线用例（用户给"拆书任务"→ agent 按五节组织）
- 素材收集协议含出口式咨询三步 + 疑点必问规则
- 欧阳锋终审通过
- 冒烟：老朱给"如何认识一个人拆书作业"任务 → agent 多轮问出真实经历 → 交付第一人称成稿 + 待确认清单

## 依赖

- #306（飞书文档 MCP——交付物写入路径）+ #307（输出物升级）+ #308（检索引用）——任务模式是其上的组装层，spec 设计可先行

## 边界

- 不修改已终审 spec（#300/#287）——本任务产出升级版
- SOUL 实现/部署拆给黄药师（#310 审后另开——E026 单角色）


## 黄药师对比分析并入（WorkBuddy vs basic-skills-coach——spec 设计核心输入）

**核心工作流差异**：小昭 = "检索→理解→映射用户场景→交付物"；飞书 agent = "SOUL 内嵌→直接回答"。四个深层原因（按重要性）：
①知识调用：MCP 语义检索（查了理解重组）vs SOUL 内嵌抄写（写啥给啥）
②上下文运用：全量业务场景映射 vs 孤立问题泛答
③分层认知：先定意图（L0）再选 Feature 组合 vs 平面点菜
④交付物意识：可复制提示词 vs Feature 名称列表

**spec 设计必须体现的"咨询模式引导"（并入五节模板第④节知识组合）**：
- 回答前先确认用户最终意图（L0 定意图）→ 再选知识/工具组合 → 最后给可复制交付物
- "意图一定，组合自己跳出来"——框架的完整方法论（意图→拆解→组合→落地），不只执行工具调用（点菜）

**试点扩展**：basic-skills-coach（AI 基本功教练）差距最明显（点菜不组合）——模式通用化后作为第二个试点候选（Feature 组合落地：从"给你 5 个 Feature 名"到"意图→组合→可复制提示词"）

## C2 SOUL 实现（2026-08-10 黄药师，E026 拆分）

### 交付物
**`agents/coaching-leadership-assistant/SOUL.md` 新增"任务模式"节**（运行时生效，未改已终审 spec #300）：

| 子节 | 内容 |
|:--|:--|
| 触发条件 | 任务感输入（写作业/拆书/复盘/整理）→ 自动切换；普通问答保持对话式 |
| 五节任务模板 | ①任务背景封装（复述任务等确认）②素材收集协议（出口式咨询多轮深挖）③知识库检索（已读卡清单+引用卡名）④知识组合与交付（第一人称+素材嵌入+金句收尾+已知边界节）⑤待确认闭环（2-4 个待确认问题） |
| 出口式咨询协议化 | 疑点必问 + 追问模板 + 直到"挖到不能再深"；引用 tool-leadership-exit-consulting + tool-leadership-questioning-cards |
| 案例沉淀回路 | 用户硬仗 → personal case 回写知识库 → 双向激活 |
| 对话 vs 任务对比表 | 触发/流程/输出三差异 |

### 逻辑冒烟（10 项全过）
触发条件 / 五节完整 / 出口式三步 / 疑点必问 / 第一人称 / 待确认 2-4 / 已知边界 / 案例沉淀 / 意图先于组合 / 对比表

### 引用卡存在性
3/3 存在（exit-consulting / questioning-cards / human-insights-digest）——防死链

### Hermes profile
已同步（~/.hermes/profiles/coaching-leadership-assistant/SOUL.md）

### 待办（真机验证，需 WSL 侧重启 gateway）
`systemctl --user restart hermes-gateway-coaching-leadership-assistant` → 老朱发"如何认识一个人拆书作业"→ 验证：多轮出口式问出真实经历 → 第一人称成稿 → 待确认清单

### C1 完成
L28 引用卡名已修正（tool-coaching-questioning-cards → tool-leadership-questioning-cards，全库错误引用清零）

## 终审记录（2026-08-10 欧阳锋）

**verdict: PASS（条件）A- · blocking: 🟠1 · methodology v2.2**

O0 溯源验证：
1. 五节任务模板完整（任务背景封装/素材收集协议/知识库检索/知识组合与交付/待确认闭环）+ 交付物规范（第一人称/素材嵌入/引用不堆卡/金句收尾）+ 案例沉淀回路（用户硬仗→personal case 回写）+ 基线用例（老朱拆书任务全流程示范）+ 适用边界（任务感输入自动触发）
2. 借鉴来源真实：出口式咨询（tool-leadership-exit-consulting #281 ✅）+ content-production-polish（第一人称去 AI 味 ✅）+ WorkBuddy 模式
3. 基线用例引用卡名 6/7 真实（framework-how-to-know-a-person / human-insights-domain-digest / tool-narrative-thinking-user-insight / dk-emotional-value-premium / case-shuishui-business-insight 全已终审）
4. 与 #300 spec/#306 MCP/#308 检索/#307 输出物关联清晰——任务模式是 spec 的运行时扩展
5. 队列健康：parse 289 全表 + #310 可见（"表格内注释移出区"说明行 break 已删——防 break 的注释自己造成 break，已记 queue_audit 白名单纪律）

条件项：
- **C1 引用卡名修正**：L49 `tool-coaching-questioning-cards` → **tool-leadership-questioning-cards**（#280 卡 5 实际卡名——错前缀）
- **C2** SOUL 实现拆分（黄药师 E026）+ 真机验证（老朱拆书任务跑一遍）

亮点：设计质量高——素材收集硬规则（"疑点必问，挖到不能深"）+ 边界诚实（交付物必含"已知边界"节）+ 案例沉淀回路（知识库与用户世界双向激活）。任务模式从设计进入实现阶段。

五维：溯源 88/逻辑 92/暗知识 90/可操作 90/表达 90 → 总分 90（A- 上限——引用错名 1 处）

## 条件项跟踪（2026-08-10 欧阳锋复核）

- **C1 ✅ 已闭环**：引用卡名修正（tool-coaching-questioning-cards → tool-leadership-questioning-cards）——实测全库实际错误引用清零（残留 2 处均为任务单修正记录文本，非实际引用）
- **C2 ✅ 已闭环（SOUL 实现）**：SOUL.md L73 新增"任务模式"节——触发（任务感输入自动切换）/五节模板/出口式咨询协议化（疑点必问+追问模板）/交付物规范（第一人称+真实素材+已知边界+金句+polish）/案例沉淀回路。引用卡 3/3 真实（exit-consulting/questioning-cards/digest）；10 项逻辑冒烟全过；Hermes profile 已同步。**未改已终审 spec #300（运行时扩展，正确姿势）**

待办（WSL 侧真机验证）：重启 gateway → 老朱发"如何认识一个人拆书作业"→ 验证多轮出口式问出真实经历 → 第一人称成稿 + 待确认清单
