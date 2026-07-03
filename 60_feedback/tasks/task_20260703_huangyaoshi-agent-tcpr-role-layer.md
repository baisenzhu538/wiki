---
id: task_20260703_huangyaoshi-agent-tcpr-role-layer
title: Agent 能力分层引入 TCPR 角色模型：所有 Agent 协作前必须选定 T/C/P/R 身份
type: task
status: reviewed
priority: P1
assignee: kimi
co_architect: 黄药师
reviewer: 欧阳锋
reviewed_by: 欧阳锋
review_date: "2026-06-29"
created_at: 2026-07-01
updated_at: '2026-06-29'
source_context: 用户提出 TCPR 应作为 Agent 身份协议，防止 Agent 军团协作混乱
estimated_cards: 1 system + 2 framework更新 + 7-8 agent-spec retrofit + 设计规范更新
dependencies:
- task_20260702_laowantong-opc-sales-agent-testing-wave1 (reviewed)
- task_20260703_laowantong-yitang-Y-model-os (queued，可并行设计，最终需与其对齐)
---

# Agent 能力分层引入 TCPR 角色模型：所有 Agent 协作前必须选定 T/C/P/R 身份

## 背景

用户指出：**每次 Agent 与用户协作时，都应先选定一个 TCPR 身份（T/C/P/R），并在一开始就明确目标。** 这样 Agent 军团才不会乱。

TCP-R（教学 Teach / 咨询 Consult / 实践 Practice / 研究 Research）原本是人类知识工作者的能力模型（见 `framework-TCPR底层网络协议.md`、`framework-TCPR皇冠模型.md`），但当前两张卡存在明显问题：

1. **没有被接入 Agent 架构**：`agent-native-card-design.md` 中没有 TCPR 的任何字段或协议要求。
2. **卡本身建设不完整**：底层网络协议卡充斥 `src_unknown` 占位；皇冠模型卡是 stub，训练层级细节缺失。
3. **没有与现有 agent-spec 产生关联**：7 张 OPC 销售 agent-spec 卡和 Y模型 Coach agent-spec 均未声明自己的 TCPR 身份。
4. **没有会话启动协议**：Agent 不知道在开场时该以什么身份、什么目标出现。

这正是黄药师「不记得」这张卡的原因——它不是被设计成「可被 Agent 调用的运行时协议」，而是一张静态的能力分类框架卡。

## 目标

把 TCP-R 从「人类能力模型」升级为 **Agent 协作的身份协议（Role Protocol）**：

- 每个 agent-spec 卡在 frontmatter 中显式声明 `tcp_role`、`tcp_default_mode`、`tcp_switch_trigger`。
- 每次会话启动时，Agent 先声明身份、确认目标，再进入具体任务。
- 设计规范、Y模型 OS、现有 agent-spec 卡全部对齐。

## 交付物

### 1. 架构/规范层

- [ ] 更新 `30_wiki/systems/agent-native-card-design.md`
  - 新增「Agent 规格卡的 TCPR 身份协议」强制章节
  - 要求所有 `agent-spec` 类型卡片必须包含 `tcp_role` / `tcp_default_mode` / `tcp_switch_trigger` / `tcp_session_opening`
  - 给出 System Prompt 开场模板
  - **切换协议本身不写在设计规范里，而是引用 `agents/agent-os.md`**

- [ ] 更新/确认 `agents/agent-os.md`
  - 作为所有 Agent 启动时必读的底层 OS 文件
  - 包含 TCPR 身份定义、默认 C 身份、切换触发语
  - 包含同一会话内切换的五条硬边界协议
  - 可被任何 agent-spec 通过文件路径或 related 链接引用

### 2. TCPR 框架卡升级

- [ ] 更新 `30_wiki/frameworks/framework-TCPR底层网络协议.md`
  - 补齐 `src_unknown` 占位
  - 新增「TCPR 作为 Agent 身份协议」章节
  - 补充 `query_triggers`："让 Agent 以什么身份帮我"、"切换到研究模式" 等
  - related 回链到所有现有 agent-spec 和 `agents/agent-os.md`

- [ ] 更新 `30_wiki/frameworks/framework-TCPR皇冠模型.md`
  - 补齐训练层级与 6 项核心训练的详细内容
  - 新增「从训练体系到 Agent 角色切换」映射
  - 补充 related 链接

### 3. 现有 agent-spec 卡 retrofit

- [ ] 为以下 7 张 OPC 销售 agent-spec 卡补全 TCPR 字段与 System Prompt 开场：
  - `tool-agent-spec-yitang-customer-segmentation`
  - `tool-agent-spec-yitang-value-proposition`
  - `tool-agent-spec-yitang-sales-process-tracker`
  - `tool-agent-spec-yitang-sales-performance-monitor`
  - `tool-agent-spec-yitang-opening-3min`
  - `tool-agent-spec-yitang-objection-handler`
  - `tool-agent-spec-yitang-self-motivation`

- [ ] 与 `#55 Y模型 OS` 对齐：把 TCPR 身份选择作为 Y模型 OS 共享 prompt 的第一步

### 4. 工具链/门禁

- [ ] `kdo lint` 增加对 `agent-spec` 类型卡片的 TCPR 字段校验（可先做 WARNING，不做阻塞）
- [ ] 产出一份 retrofit 指南，便于未来新增 agent-spec 时直接套用

### 5. 中途切换身份支持（用户明确要求）

- [ ] `agents/agent-os.md` 必须包含同一会话内从 C→P、C→R、P→C 等常见切换协议（已写入，需确认并补 frontmatter/引用）。
- [ ] 所有 agent-spec 卡的 System Prompt 必须支持用户说"切换到教学/咨询/实践/研究"，切换时 Agent 要：
  - 明确声明新身份和新目标；
  - 复述继承的事实/分析；
  - 检查新身份所需事实输入是否完整，缺失时返回 `INPUT_MISSING`；
  - 高风险动作仍标注 `需人工确认`。

## 验收标准

1. `agent-native-card-design.md` 新增 TCPR 身份协议章节，并通过 `kdo pre-submit`。
2. `framework-TCPR*` 两张卡 `src_unknown` 清零，新增 Agent 身份视角，lint 无新增 ERROR。
3. 7 张 OPC agent-spec 卡均包含完整的 TCPR 字段与开场模板，`kdo pre-submit` 全部 PASS。
4. Y模型 OS 卡（#55）与 TCPR 角色选择逻辑一致，无冲突。
5. 产出 retrofit 指南 `40_outputs/agent-tcpr-role-retrofit-guide.md` 或等价文档。

## 依赖与阻塞

- `#50` OPC 销售智能体实测 Wave 1（reviewed）：已有 7 张 agent-spec 卡，是 retrofit 的对象。
- `#55` Y模型 OS（queued）：本任务可与 #55 并行设计，最终需与其对齐，避免 OS 层与 TCPR 层冲突。

## 负责人调整

- **主执行人**：老顽童(Kimi)
- **架构对齐**：黄药师（co_architect）
- 黄药师专注 #59 Agent Prompt 编译器，#58 的具体卡片改造由老顽童执行；涉及 `agents/agent-os.md` 和 `agent-native-card-design.md` 的架构变更需黄药师评审。

## 用户决策

- **单列执行**：本任务不与 #55 Y模型 OS 合并，保持独立任务单，避免执行中回退和任务混乱。
- **入队方式**：以后新任务按顺序追加到队列末尾，不随意插队或合并。
- **队列顺序**：#59 按队列规则等待 #55 终审及前面 queued 任务清空后，再由黄药师领取。

## 备注

- 用户特别强调：**Agent 不要死板流程，要协作式。** 因此 TCPR 身份选择不应变成强制填表，而是「先声明、再协商、随时可切」的轻协议。
- 身份选择不是人格设定：同一个 Agent 在不同会话中可以是 C 或 P，身份字段写入 frontmatter，开场 prompt 动态加载。

---

## 欧阳锋终审报告

### 审查结果：通过 ✅

| 项目 | 数据 |
|:---|:---|
| 审查时间 | 2026-06-29 |
| 审查人 | 欧阳锋 |
| 改动文件数 | 13 个核心文件 + 1 个 lint 脚本 |
| pre-submit | 13/13 PASS ✅ |
| lint 新增 ERROR | 0 |

### 交付物核查

| 类型 | 文件 | 状态 |
|:---|:---|:---|
| 运行时 OS | `agents/agent-os.md` | ✅ 已升级为完整 TCPR 身份协议与启动规范，默认 C 身份、切换触发语、五条硬边界清晰 |
| 设计规范 | `30_wiki/systems/agent-native-card-design.md` | ✅ 新增 TCPR 身份协议章节，定义 `tcp_role` / `tcp_default_mode` / `tcp_switch_trigger` / `tcp_session_opening` |
| Y模型 OS 对齐 | `30_wiki/systems/system-yitang-Y-model-os.md` | ✅ 共享 prompt 第 0 步为 TCPR 身份选择，引用 `agents/agent-os.md` |
| TCPR 框架升级 | `30_wiki/frameworks/framework-TCPR底层网络协议.md` | ✅ 补齐 src_unknown，新增 Agent 身份协议章节与 query_triggers |
| TCPR 皇冠模型 | `30_wiki/frameworks/framework-TCPR皇冠模型.md` | ✅ 补齐 T/C/P/R 各 6 项核心训练，新增训练层级到 Agent 角色切换映射 |
| 7 OPC agent-spec retrofit | `30_wiki/tools/tool-agent-spec-yitang-*.md` | ✅ 全部 7 张卡 frontmatter 含 4 个 TCPR 字段，System Prompt 含 TCPR 身份声明 |
| Retrofit 指南 | `40_outputs/agent-tcpr-role-retrofit-guide.md` | ✅ 覆盖判断是否需要 retrofit、选身份、加字段、插声明、更新 related、验证清单 |
| lint 增强 | `90_control/scripts/kdo_lint.py` | ✅ 对 `agent-spec` 类型增加 TCPR 字段与 System Prompt 声明的 WARNING 级检查 |

### 7 张 OPC agent-spec 默认身份分配

| 卡片 | tcp_role | 身份 |
|:---|:---:|:---|
| customer-segmentation | C | 咨询诊断 |
| value-proposition | C | 咨询共创 |
| sales-process-tracker | C | 咨询诊断 |
| sales-performance-monitor | R | 研究复盘 |
| opening-3min | T | 教学共创 |
| objection-handler | C | 咨询诊断 |
| self-motivation | P | 实践驱动 |

身份分配与卡片核心动作匹配，无异议。

### 质量评估

- **架构清晰**：Agent OS / Y模型 OS / 域 Agent 三层结构保持完整；TCPR 只解决「以什么身份协作」，不替代 Y模型「怎么思考」。
- **协议轻量**：身份声明、切换触发、五条硬边界完整，但未变成强制填表，符合用户「Agent 不要死板流程，要协作式」的要求。
- ** retrofit 完整**：7 张 OPC agent-spec 全部接入，且产出可复用指南，未来新增 agent-spec 有标准模板。
- **工具链闭环**：lint 脚本增加 WARNING 级校验，可逐步把 TCPR 字段变成软规范。
- **无新增 ERROR**：13 个改动文件 pre-submit 全部 PASS；全库 lint 中仅 `agent-native-card-design.md` 有 2 条 `source_refs contaminated` 历史 ERROR，与本次 TCPR 改动无关。

### 审查中发现的小问题（不阻塞通过）

1. **`agent-native-card-design.md` 存在两个「Agent 规格卡的 TCPR 身份协议」章节**：分别位于约第 207 行和第 581 行，内容有重叠。建议下次清理时合并为一个权威章节，避免维护两份。
2. **部分 `related` 仍为 bracket wikilink 格式**：虽然不影响 pre-submit，但与 #52 GraphRAG bare id 规范不一致，可在后续 link-repair 批次中统一。
3. **`tcp_role` 在 lint 脚本中允许为空字符串**：当前逻辑 `tcp_role not in ("", "T", "C", "P", "R")` 把空字符串视为合法，建议后续改为空字符串也报 WARNING。
4. **Agent OS 文件位于 `agents/agent-os.md`**：路径在 30_wiki 之外，需确认 GraphRAG 索引时是否包含该路径。如未包含，建议通过 `related` 或显式索引确保 Agent 启动时能加载。

### 结论

同意 `#58` Agent TCPR 角色模型任务终审通过。TCPR 已从人类能力模型升级为 Agent 运行时身份协议，与 Y模型 OS、OPC 销售 agent-spec、设计规范、lint 门禁形成完整闭环。

*终审：欧阳锋 · 2026-06-29*
