---


title: KDO Agent 体系建设方案（草案）
type: proposal
status: draft
domain:
- agent-infrastructure
created_at: '2026-06-10'
updated_at: '2026-06-16'
author: 黄药师
source_context: KDO infrastructure decision — internal design record （原 legacy，已从
  title/context/filename 推断为 src_20260503_52ae08ba）
source_refs: []
id: agent-ecosystem-design
reviewed_by: pending
confidence: 0.6
trust_level: low
related:
- [[graph-rag-retrieval-layer]]
- [[case-truman-ai-partner]]
- [[proposal-prompt-injection-infrastructure]]
- [[case-ji-hao-skills-market]]
- [[ai-native-im-multi-agent]]
# KDO Agent 体系建设方案

> 状态：**待欧阳锋裁决**。三个核心问题未定：agent 数量、分发机制、颗粒度。

---

## 一、为什么要建 Agent 体系

当前 KDO 的输出形式以"文章"为主（`kdo produce content/article`）。但用户提出了两个更直接的需求：

1. **C 角色咨询**：不是读一篇文章，而是让 AI 基于知识库框架直接分析我的实际案例，生成诊断报告。
2. **P 角色工具**：让 AI 直接用特定方法论帮我干活——整理清单体笔记、做商业预判、拆解关键假设。

**核心理念**：Agent = Role（谁） + Knowledge（知道什么） + Task（做什么）

每个 Agent 是一个"角色"——它有明确的身份（P 实践者 / C 顾问），注入了特定的知识卡片，能执行一组定义好的能力。

---

## 二、现有基础设施

```
40_outputs/capabilities/
├── skills/                    ← Agent 定义（manifest.yaml）
│   ├── note-coach/            ← 已有 ✅ P角色：清单体笔记教练
│   ├── knowledge-curator/     ← 已有 ✅
│   ├── delivery-producer/     ← 已有 ✅
│   └── system-linter/         ← 已有 ✅
├── prompts/                   ← 可复用 prompt 片段
└── templates/                 ← 产出模板
```

**已有能力**：
- src_unknown
- src_unknown
- src_unknown

---

## 三、候选 Agent 清单（未定稿）

按"角色类型 × 知识域"组合：

| Agent | 角色 | 注入的知识卡 | 输出类型 |
|-------|:--:|------|------|
| `business-consultant` | C | 产品内核5卡 + 商业预判 + 关键假设 + 假设驱动方法论 | 商业分析报告 |
| `research-investigator` | C | 全库检索（按话题动态加载） | 调研报告 |
| `checklist-coach` | P | 清单体笔记 + 知识萃取三流派 + Truman PRD案例 | 结构化清单 |
| `kernel-validator` | C | 产品内核验证 + 六策略阶梯 | 验证方案 |
| `prediction-analyst` | C | 商业预判 + 光谱模型 + 三类硬伤 | 方向评估报告 |
| `assumption-deconstructor` | P | 关键假设思维 + 259工具 | 假设拆解清单 |
| `note-coach` | P | 已有 ✅ | 清单体笔记 |

**P 角色 vs C 角色的核心差异**：

| | P 角色 | C 角色 |
|:--|:---|:---|
| 身份 | 实践者——直接干活 | 顾问——帮你分析 |
| 回答方式 | "这是你要的产物" | "这是诊断 + 2-3个选项，你选" |
| 决策权 | 不替你判断 | 永远把决策权留给人 |
| 典型 prompt | "你不探讨、不说教、不解释原因。直接干活。" | "你分析问题、给出选项、说明利弊——最终决策由人来做。" |

---

## 四、待裁决问题（欧阳锋）

### Q1：建多少个 Agent？

- src_unknown
- src_unknown
- src_unknown

### Q2：如何封装发布给团队？

- src_unknown
- src_unknown
- src_unknown
- src_unknown

### Q3：颗粒度多细？

- src_unknown
- src_unknown
- src_unknown

---

## 五、技术实现路径（已具备）

实现一个 Agent 的技术栈：

```
Agent 定义层：
  40_outputs/capabilities/skills/<name>/
  ├── manifest.yaml          ← 身份 + 知识卡列表 + 能力清单 + 约束
  ├── system-prompt.md       ← C/P-role prompt 模板
  └── SKILL.md               ← 人类可读说明

编译层（已有）：
  kdo encapsulate <name>     ← manifest + 知识卡 → system prompt

检索层（已有）：
  kdo query "<问题>"          ← 语义 + 图检索，动态加载知识

用户接口层（待建）：
  kdo consult "<问题>"       ← query → encapsulate → LLM → 报告
```

**新增代码量**：`kdo consult` ~50 行 + C-role 编译模板 ~30 行 + manifest.yaml 模板 ~30 行 = ~110 行。

---

## 六、不做什么

- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

## 七、建议的下一步

1. **MVP**：建 `business-consultant` Agent → 跑通"输入商业问题 → 检索框架 → C 角色分析 → 输出报告"闭环
2. **验证**：用真实案例（如青岛奶茶店、声音变现课程）测试报告质量
3. **裁决**：欧阳锋拍板 Q1/Q2/Q3 → 定稿 Agent 体系设计 → 分批建设

---

## 相关

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
