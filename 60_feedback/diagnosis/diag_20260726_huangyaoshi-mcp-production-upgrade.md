---
id: diag-20260726-huangyaoshi-mcp-production-upgrade
title: "KDO MCP + 生产管线升级：全网调研与建议"
type: diagnosis
status: draft
author: 黄药师
reviewed_by: 待王语嫣审
created_at: "2026-07-26"
updated_at: "2026-07-26"
source_refs:
  - "Glean MCP Best Practices (2025)"
  - "Kong MCP Server Pattern (2025)"
  - "EMNLP 2025: Tool Preferences in Agentic LLMs are Unreliable"
  - "Prompt-to-Paper: 8-dim Auto Quality Scorer (arXiv 2026)"
  - "Agent Book Factory: 5-dim Scoring + Multi-judge Panels (2026)"
  - "Single Grain/McKinsey: 97% Brand Compliance via Voice Libraries (2026)"
  - "Agentic Product Standard: Autonomy Ladder L0-L4 (2025)"
  - "RAG-MCP: Mitigating Prompt Bloat (2025)"
related:
  - framework-ouyangfeng-review-methodology
  - framework-kdo-mcp-server
  - framework-kdo-retrieval-architecture-v2
  - agent-spec-duanwangye-publisher
  - agent-spec-hongqigong-multimodal
---

# KDO MCP + 生产管线升级：全网调研与建议

> 审阅对象：王语嫣  
> 目的：基于 2025-2026 全网最佳实践调研，提出 KDO 外部访问 + 生产质量的三层升级方案。P0/P2 已执行，P1 待王语嫣确认方向。

---

## 1. 调研背景

WorkBuddy 通过 MCP 成功接入 KDO，4 个 Tool 全链路打通。但实测暴露了两个问题：
1. 外部 Agent 对 KDO 的理解效率取决于 Tool 描述质量（非功能正确性）
2. KDO 的知识生产质量依赖单人审查，缺乏结构化评分

为此对 2025-2026 年全网最佳实践做了系统调研。

---

## 2. 调研发现

### 2.1 外部 Agent 效率：Tool 描述是决定性因素

**核心数据**：Tool 描述质量导致 LLM 选择准确率差 2.6 倍（EMNLP 2025）。同功能工具，描述好的版本比差的版本多用 10 倍（GPT-4.1 实测）。RAG-MCP 证明：对工具做检索预过滤，token 省 50%+，选择准确率提升 3 倍。

**最佳实践**：
- Glean MCP：设计围绕"用户工作"而非"API 结构"，用具体场景替代技术术语
- Kong MCP：在 server instructions 中写 workflow 引导（"START HERE → then → then"）
- cortex-brain：知识新鲜度标记（current ≤60d → aging → stale），Agent 据此判断时效

### 2.2 知识生产质量：多法官评审 + 自动预评分 = 最优组合

**核心数据**：Prompt-to-Paper 的 8 维自动评分与 ICLR 人工评审高度相关。Agent Book Factory 的 5 维 0-100 评分使返工率降低 ~40%。Single Grain/McKinsey 报告：治理化 AI 管线 9-10x 吞吐量、97% 品牌语调合规。

**最佳实践**：
- 多法官评分（3 人 + 1 对抗者，取中位数）优于单人审查
- 自动化质量预评分（不替代人类，是帮人类预处理）
- 限定修订轮数（≤3 轮）+ 系统化追踪
- 品牌语调库标准化 → 跨渠道一致性

### 2.3 MCP 协议层：5 项可落地的改进

| 改进点 | 来源 | 效果 |
|:--|:--|:--|
| Server instructions 写入 workflow | Kong MCP pattern | Agent 首次调用不再乱序 |
| Tool 描述用"用户语言"替代"实现语言" | Glean MCP | 选择准确率 +2.6x |
| 返回相关建议而非"not found" | Awesome MCP Best Practices | 减少无效调用 |
| 结构化输出（JSON + Markdown） | MCP spec 2024-11-05 | 支持程序化消费 |
| SSE transport 支持远程 Agent | Streamable HTTP 替代 SSE | 飞书 Agent 远程调用 |

---

## 3. 已执行（P0 + P2）

### P0：MCP Tool 描述重写 + 新鲜度 ✅

| 改动 | 效果 |
|:--|:--|
| kdo_search 描述从"RRF fusion"→"Search KDO like Google" | 外部 Agent 不再看到内部术语 |
| Server instructions 加 workflow 引导 | "WORKFLOW: onboard → search → read" |
| Search/Onboard 结果加 `updated_at` | Agent 能判断卡片新鲜度 |

狗粮：WorkBuddy 实测通过。Tool 描述无内部术语，onboard 返回完整 MOC + reading_order。

### P2：pre-submit 自动化质量预评分 ✅

| 改动 | 效果 |
|:--|:--|
| `_check_quality_score` 函数 | 4 维 0-100 预评分（定位声明/暗知识密度/溯源完整/解压配套） |
| 每次 pre-submit 自动输出 | 诊断用，不阻断通过 |

狗粮：好卡 100/100，差卡 25/100。数字分让生产者知道哪里弱，不替代欧阳锋审查。

---

## 4. 待王语嫣确认（P1）

### P1：欧阳锋审查方法论升级 v2.0 → v2.1——多维数字评分

**改什么**：在现有字母等级（A/A-/B+/B/B-/C）基础上，增加 5 维 0-100 数字评分作为诊断层。

**5 维标准**（已写入 `framework-ouyangfeng-review-methodology.md` v2.1 草案）：

| 维度 | 权重 | 评估重点 |
|:--|:--:|:--|
| 溯源完整 | 25% | source_refs 是否完整、行号是否准确、Claims 是否可溯源到原文 |
| 逻辑骨架 | 25% | 依赖关系是否呈现、框架归属是否声明、related 双向链接 |
| 暗知识密度 | 20% | 失败模式是否具体（症状+修复）、是否有真实反例 |
| 可操作性 | 15% | Action Triggers 是否有触发条件、解压资产是否 ≥3 |
| 表达质量 | 15% | 无 AI 味、无模板话、正文 ≥100 行 |

**总分→等级映射**：≥90=A, 80-89=A-, 70-79=B+, 60-69=B, 50-59=B-, <50=C

**为什么不是替代而是补充**：字母等级仍是终审结论。数字分是诊断工具——让老顽童知道"这卡哪里弱、下次怎么改"。这和 P2 的 pre-submit 预评分形成互补：P2 是机械预检，P1 是人工精评。

**影响范围**：
- `framework-ouyangfeng-review-methodology.md` → v2.1（草案已写，待确认后改 status=reviewed）
- `.agent/ouyangfeng-context.md` → 审查标准引用 v2.1（已更新）
- 欧阳锋审查报告格式 → 新增 `scores` 字段
- 老顽童收到的审查结论 → 从"B+"变成"B+（溯源:85 骨架:72 暗知识:60 可操作:78 表达:80）"

**你的判断点**：
1. 5 维权重是否合理？特别是"表达质量 15%"——KDO 的知识卡片是否需要这么高权重？
2. 分数是否只对 framework 卡打？还是扩展到 concept/tool？
3. 是否需要加入"跨域同构"作为逻辑骨架的子维度？

---

## 5. 后续建议（P3，待排期）

| 项目 | 内容 | 优先级 | 负责 |
|:--|:--|:--|:--|
| MCP SSE transport | 支持飞书 Agent 远程调用 MCP | P1 | 黄药师 |
| 品牌语调库 | 扩展 content-production-polish 为全厂"品牌语调模型" | P2 | 老顽童+段王爷 |
| 多法官审查试点 | 选 1 个域，王语嫣+欧阳锋双审对比 | P2 | 王语嫣 |
| 审查修订追踪 | 系统化记录每张卡的 revision 轮数 | P2 | 黄药师 |

---

*黄药师 · 2026-07-26 · 基于 2025-2026 全网调研*
