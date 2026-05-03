---
title: "KDO Protocol — AI-Agent Operating Contract"
type: system
status: draft
source_refs:
  - "src_20260502_7d7c1b7c"
created_at: "2026-05-02"
updated_at: "2026-05-03"
related:
  - "[[Obsidian + KDO 内容产出工作流 — 产品设计大纲]]"
  - "[[KDO Protocol]]"
  - "[[Wiki Index — Knowledge Graph Entrypoint]]"
tags:
  - #kdo
  - #protocol
  - #ai-workflow
trust_level: medium
reviewed_by: "Claude"
review_date: "2026-05-03"
---

# KDO Protocol — AI-Agent Operating Contract

## Core Points

1. **KDO Protocol 是为 AI Agent 设计的仓库操作契约**，目的是让 AI 在操作 Obsidian/KDO 知识库时，不再依赖隐性的文本约定，而是遵循显式的机器可读规则。
2. **它解决的核心矛盾**：Obsidian 给了人类极致的自由（本地文件、双向链接、无限定制），但这种自由对 AI 来说是"无接口的混沌"——AI 不知道怎么操作这个仓库。
3. **协议包含四个层面**：目录拓扑与访问权限（哪里能读写）、实体类型与 Schema（知识产物该长什么样）、流水线规则（状态怎么流转）、禁止清单（红线）。
4. **它的设计灵感来源于一堂课程中提到的 `cloud.md` 协议假设**——即笔记系统需要一个类似 API 契约的标准化协作协议，让 AI Agent 能够掌握操作方法，将人类从"胶水工作"中解放出来。
5. **当前版本 v0.1 是骨架级实现**，核心结构已经落地，但距离"AI 完全自主执行"还差一层：严格的 Schema 校验自动化、知识图谱索引层、以及上下文感知机制。

### [Critique]

- **Assumption**: 假设所有 AI Agent 在进入仓库时都会先读取 `90_control/PROTOCOL.md`。实际上 LLM 的上下文窗口和行为不可控，如果没有显式的路由机制（如 `routing-rules.md` 强制执行），AI 可能跳过协议直接操作。
- **Boundary**: 协议只能约束"这个仓库内"的操作。跨仓库、跨工具的协作（比如从飞书文档拉取内容再写入 KDO）仍然需要额外的桥接协议。
- **Reliability: Medium** — 理由：协议本身是文本约定，不是编译器级别的强制约束。AI 可能读错、遗漏、或产生幻觉。需要配合 JSON Schema（`schemas/concept.yaml`）和自动化校验工具才能提升可靠性到 High。
- **Anti-pattern risk**: 过度协议化可能增加操作摩擦。如果 AI 每次创建笔记都要经过 10 项 frontmatter 校验，反而降低了"低摩擦捕获"的原始设计目标。需要在"严格"与"流畅"之间找到平衡点。

### [Synthesis]

- **Links to**: [[Obsidian + KDO 内容产出工作流 — 产品设计大纲]] — Protocol 是 Workflow 的底层基础设施；Workflow 定义"做什么"，Protocol 定义"怎么做"。
- **Links to**: [[Wiki Index — Knowledge Graph Entrypoint]] — Protocol 定义了 Index 的结构规则（概念类型、链接格式、状态枚举）。
- **Complements**: 一堂课程中提出的 `cloud.md` 协议假设 — KDO Protocol 是对这一假设的具体工程实现，但一堂更关注"产品内核级机会"，KDO Protocol 更关注"单仓库操作契约"。
- **Conflicts with**: 无直接冲突，但需警惕与 Obsidian 的"自由哲学"之间的张力。Obsidian 推崇无结构、无约束；KDO Protocol 是有结构、有约束的。两者需要在"人类自由度"和"AI 可执行性"之间取得平衡。
- **Transferable to**: 任何基于 Markdown + Git 的知识管理系统，尤其是多端协作、AI 参与的场景（如 Second Brain、Zettelkasten + LLM）。
- **Gap**: 缺少一个 `CONTEXT.md` 或动态快照机制，让 AI 能在每次会话开始时快速加载"当前仓库状态"，而不是每次都重新扫描全部文件。

---

## Protocol Structure

| Layer | File | Purpose |
|-------|------|---------|
| **Identity** | `PROTOCOL.md` Section 1 | Vault 定义与角色 |
| **Topology** | `PROTOCOL.md` Section 2 | 目录结构 + 访问矩阵 |
| **Schema** | `schemas/concept.yaml` | 知识卡片数据校验 |
| **Pipeline** | `PROTOCOL.md` Section 5 | KDO 流水线状态流转 |
| **Quality Gates** | `PROTOCOL.md` Section 6 | 写入前检查清单 |
| **Prohibitions** | `PROTOCOL.md` Section 7 | AI 绝对禁止的操作 |

---

## Known Limitations

1. **No automated validation yet**: `schemas/concept.yaml` 是声明式 Schema，但还没有钩子（hook）在 AI 写入前自动执行校验。目前依赖 AI 自检。
2. **Context loading is expensive**: AI 每次会话需要重新读取 PROTOCOL.md + AGENTS.md + routing-rules.md，大型 vault 的上下文加载成本高。
3. **Graph RAG not integrated**: 双向链接 `[[...]]` 对人类是知识网络，对当前 AI 是文本符号。缺乏显式图谱索引。
4. **Cross-device sync edge cases**: Protocol 假设 Git 是同步层，但没有处理 Obsidian Git 插件的自动备份冲突（`.obsidian/` 等机器配置的多设备打架问题）。
