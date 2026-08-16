---
id: framework-truman-agent-team-architecture
title: Truman Agent 团队系统架构：缓冲站→Library→三团队→四库
type: framework
status: pending_review
author: 老顽童
reviewed_by: 待审
confidence: 0.85
trust_level: medium
language: zh-CN
created_at: 2026-08-16
updated_at: 2026-08-16
domain:
- knowledge-management
- ai-collaboration
aliases:
- TrumanAgent团队架构
- 硅基组织行为学
- 缓冲站Library四库
- 30个AI员工
- 楚门-AI知识管理探索营-口述
- 楚门-AI知识管理探索营-口述.txt
- OCR_一堂DOC-20260816015649
- OCR_一堂DOC-20260816015649.md
- AI知识库
tags:
- audience:manager
- scene:planning
- skill-level:advanced
source_person: 楚门
source_context: AI×知识管理探索营（2026-08-15 晚直播）——组建跨职能 AI 团队（015649 已人工核验 2 处纠偏，L3080-3250）
source_refs:
- 00_inbox/AI知识库/楚门-AI知识管理探索营-口述.txt
- 00_inbox/AI知识库/OCR_一堂DOC-20260816015649.md
related:
- '[[framework-multi-agent-collab-chain-six]]'
- '[[framework-knowledge-five-leaps]]'
- '[[framework-dual-center-feishu-obsidian]]'
- '[[concept-session-vs-memory-vs-document]]'
- '[[framework-knowledge-compound-rocket-six]]'
- '[[agent-spec-zhu-ai-coach]]'
- '[[dk-ai-builder-illusion]]'
- case-cross-xingangwan-pharma
---

# Truman Agent 团队系统架构：缓冲站→Library→三团队→四库

> 本卡属于「AI×知识管理」体系（楚门探索营第五次飞跃·组建跨职能 AI 团队，015649 图已人工核验，L3080-3250）：硅基组织行为学——像做岗位画像一样定义每个 Agent（内核/边界/职能/画像文档），组建三个 10 人 Agent 团队（业务/研究/产品）共 30 个"AI 员工"，负责人制，人只给负责人分活。数据流：偶遇→缓冲站→Library→素材库→反思自查中心→四库。

## 1. 核心洞察

组建 AI 团队不是堆工具，是**像公司一样组织 Agent**（L3112-3122）：
- **岗位画像**：每个 Agent 定义内核/边界/职能/画像版文档（像做岗位画像一样，L3120）
- **负责人制**：人只给负责人分活，负责人从团队挑 3-4 个研究员并合并（L3148-3150）——人不直接给 30 个 Agent 分配
- **特性最大化**：Claude=统筹通信（记性差但擅长统筹）/Abacc=专家型（L3196-3200）
- **不依赖 Session**：所有沉淀靠文档知识库（L3212-3214）

## 2. 系统架构（015649 已核验）

```
偶遇（文章/视频/灵感/假设/聊天）
  → 缓冲站：Cubox（内容）/ FloMo（灵感）/ YAI（AI 对话）
  → Library 阅读库（尽量自动收纳）
  → 素材库（爬虫自动采集）
  → 反思自查中心（代码/程序库，捞市场最佳实践）
  → 三团队（各 10 Agent，负责人制）
  → 四库：阅读库 / 产品库 / 项目库 / 作品库
```

## 3. 三团队×10 Agent

| 团队 | 负责人 | 职能 | 示例成员 |
|:--|:--|:--|:--|
| 业务团队 | JM | 管理/执行 | 分身/美女助理/CEO/教练负责人/设计/营销/产品/研发/运维负责人（L3122-3124） |
| 研究团队 | 伊森 | 调研/研究 | 个人方向/业务方向/组织方向/AIGC 方向研究员（L3144） |
| 产品团队 | Summer | 内容/作品 | 写作/营销/作图/摄影/PPT/视频（L3134-3136，已转 Hermes） |

（L3190-3194：负责人分管；"我相当于分了一层管理者"）

## 4. 应用方法

1. **定义岗位画像**：给每个 Agent 写内核/边界/职能/画像文档（像招人一样）
2. **设负责人**：人只跟负责人对话（3 个负责人 vs 30 个 Agent）
3. **配齐资源**：独立库/案例库全配齐（L3144-3146）
4. **按任务分活**：课题甩给负责人，负责人挑研究员+合并（L3202-3206）
5. **沉淀靠文档**：不依赖 Session，所有产出写进四库（L3212-3214）

## 5. When NOT to Use

1. **单任务/单 Agent 够用**——不需要 30 个 Agent 的组织。
2. **团队协作未验证**——先单 Agent 跑通，再组队（楚门也是分批实验：第一批 AIGC→第二批内容→第三批研究）。
3. **管理成本失控**——负责人制前提是能定义清楚岗位画像；定义不清=30 个乱跑的 Agent。

## 6. 失败模式

| 失败模式 | 真实信号 | 修复动作 |
|:--|:--|:--|
| 无岗位画像 | Agent 边界不清/重复干活 | 像岗位画像一样定义内核边界职能 |
| 无负责人 | 人直接指挥 30 个 Agent | 分层管理者（负责人制） |
| 依赖 Session | Agent 忘事/上下文丢失 | 全沉淀到文档（四库） |
| 工具堆砌 | 买了工具没用起来 | 先定义"要解决什么问题"再配 Agent |
| 特性错配 | Claude 做专家活/Abacc 做统筹 | 统筹用 Claude，专家用 Abacc（特性最大化） |

## 7. Action Triggers

- 多 Agent 场景变多 → 考虑组织化（岗位画像+负责人制）
- 任务重复分配 → 设负责人（人只对负责人分活）
- Agent 经常忘上下文 → 检查沉淀是否靠文档（不是 Session）

## 8. 与其他知识的关联

- `framework-multi-agent-collab-chain-six`：六环节=单次任务的流水线；团队=组织化形态
- `framework-knowledge-five-leaps`：团队架构=飞跃④⑤的成果（多 Agent+自动化）
- `framework-dual-center-feishu-obsidian`：Obsidian=团队共享的知识库中心
- `concept-session-vs-memory-vs-document`：文档=团队沉淀载体（不依赖 Session）
- `framework-knowledge-compound-rocket-six`：协作化引擎的极致=30 Agent 团队
- `agent-spec-zhu-ai-coach`：岗位画像文档的 Agent 化模板（KDO 已有实践）
- `framework-kdo-context-design`：上下文设计——团队知识库组织（待建卡，互链预留）
- `dk-ai-builder-illusion`：AI 建造者幻觉——团队化不等于能力自动涌现（跨域）
