---
title: KDO Protocol — AI-Agent Operating Contract
type: system
status: draft
aliases:
- src_unknown
id: kdo-protocol
created_at: '2026-05-02'
updated_at: '2026-06-16'
related:
- "[[case-半肥猫-course-to-skill]]"
- "[[dk-modeling-ai-without-judgment]]"
- "[[kdo_product_design_agent_final]]"
- "[[kdo-priority-checklist]]"
- "[[case-ban-fei-mao-conversion-hacker-skill]]"
- "[[kdo-protocol]]"
- "[[index]]"
- "[[business-research-skill-oscar-13-weapon-system]]"
tags: []
trust_level: medium
reviewed_by: Claude
review_date: '2026-05-03'
domain:
- master
author: unknown
source_context: KDO internal record （原 legacy，已从 title/context/filename 推断为 src_20260503_52ae08ba）
source_refs:
- 'pending_archive: src_unknown'
confidence: 0.6# KDO Protocol — AI-Agent Operating Contract
---
## Core Points

1. **KDO Protocol 是为 AI Agent 设计的仓库操作契约**，目的是让 AI 在操作 Obsidian/KDO 知识库时，不再依赖隐性的文本约定，而是遵循显式的机器可读规则。
2. **它解决的核心矛盾**：Obsidian 给了人类极致的自由（本地文件、双向链接、无限定制），但这种自由对 AI 来说是"无接口的混沌"——AI 不知道怎么操作这个仓库。
3. **协议包含四个层面**：目录拓扑与访问权限（哪里能读写）、实体类型与 Schema（知识产物该长什么样）、流水线规则（状态怎么流转）、禁止清单（红线）。
4. **它的设计灵感来源于一堂课程中提到的 `cloud.md` 协议假设**——即笔记系统需要一个类似 API 契约的标准化协作协议，让 AI Agent 能够掌握操作方法，将人类从"胶水工作"中解放出来。
5. **当前版本 v0.1 是骨架级实现**，核心结构已经落地，但距离"AI 完全自主执行"还差一层：严格的 Schema 校验自动化、知识图谱索引层、以及上下文感知机制。

### [Critique]

- src_unknown
- src_unknown
- src_unknown
- src_unknown

### [Synthesis]

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown



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

## External Intake Routing: Skill vs Raw Material

外部知识/Skill 进入 KDO 时，走哪条路线取决于**内容结构化程度**：

| 路线 | 入口 | 适用素材 | 产出 |
|------|------|---------|------|
| **Inbox Pipeline** | `00_inbox/` → `kdo capture` → `kdo ingest` → `kdo enrich` | 原始课程笔记、网页抓取、录音转写、未整理的碎片 | `concepts/` 三步骤编译卡 |
| **Direct Compile** | `30_wiki/concepts/` 直接创建 | 已结构化的 Skill 包（含 SKILL.md + references/）、明确要求"研究并内化"的技术栈 | 三步骤编译概念卡 + 可执行 Skill 安装 |

**决策树**：

```
外部输入
├── 已结构化 Skill 包（.zip / 完整 SKILL.md）？
│   ├── 是 → 安装到 ~/.claude/skills/（可执行层）
│   │      → concepts/ 直接出概念卡（知识层）✅
│   └── 否 → 是否需要人工先确认再加工？
│       ├── 是 → 00_inbox/ → KDO pipeline ✅
│       └── 否（如技术能力研究）→ concepts/ 直接编译 ✅
```

**核心判断标准**：目标是"整理已有知识"走 inbox pipeline；目标是"编译新能力/技能"直接出概念卡。

**两层分离**：
- src_unknown
- src_unknown

> 此规则来自 business-research skill 安装过程中的实践总结。参见 [[business-research-skill-oscar-13-weapon-system]]。

---

## Known Limitations

1. **No automated validation yet**: `schemas/concept.yaml` 是声明式 Schema，但还没有钩子（hook）在 AI 写入前自动执行校验。目前依赖 AI 自检。
2. **Context loading is expensive**: AI 每次会话需要重新读取 PROTOCOL.md + AGENTS.md + routing-rules.md，大型 vault 的上下文加载成本高。
3. **Graph RAG not integrated**: 双向链接 `...` 对人类是知识网络，对当前 AI 是文本符号。缺乏显式图谱索引。
4. **Cross-device sync edge cases**: Protocol 假设 Git 是同步层，但没有处理 Obsidian Git 插件的自动备份冲突（`.obsidian/` 等机器配置的多设备打架问题）。
