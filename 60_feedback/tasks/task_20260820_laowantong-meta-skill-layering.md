---
id: 381
assignee: hermes
status: reviewed
updated_at: '2026-08-19T19:23:17.988975+00:00'
title: 元技能分层卡（P1，老朱 08-20 对齐"这个很重要"）——先封装"封装能力"再量产
priority: P1
dependency: []
reviewed_by: 欧阳锋
review_date: '2026-08-19'
grade: A
---

# #381 元技能分层卡（P1）

## 任务目标

AI 知识库域三刷补挖第一张（老朱 08-20 边听课边对齐时点名"很重要"）：把楚门"Skill 创业专家"的**元技能分层结构**提炼成卡——八步卡（tool-skill-packaging-eight-steps）覆盖了"怎么封装一个 skill"的战术层，本卡补战略层：**先封装"生产 skill 的能力"（元 Partner），再用元能力量产具体 skill**。

## 素材（行号已锚定，双源对照）

> **口径修正（老朱 2026-08-20 权威裁定）**：YAI = 一堂知识库之上的一系列 Agent 体系（知识库/数据包/Partner 等），**不是单一工具**——任务单和卡文中"封装进 YAI"一律按此理解："Skill 创业专家"是 YAI 体系中的一个 Partner。老朱仍在听课，后续可能补充该主题新内容（含 "Dee…" 系列），到时由王语嫣对齐后追加进本任务或另立项。

- 口述 `00_inbox/AI知识库/楚门-AI知识管理探索营-口述.txt`：
  - L1056-1074：封装"Skill 创业专家" Partner → 对它说"我想做一个调研的专家" → Partner 自己去知识库搜调研方法论、讨论、产出调研 Skill 文档
  - L1075-1110：龙虾自学调用、知识三落点（项目库/技能库/个人库）、"我也看不懂没关系，AI 能看懂就行"
  - L2454-2458：Partner 生态演化苗头（数据访谈分身、Partner Office 多人协作）
- 逐字稿 `AI×知识管理 探索课（逐字稿）.md` L335-400：阶段还原对照（快速认识→翻译解读→自建教程→逐步打磨→封装）
- 已有卡（L7 基线）：`tool-skill-packaging-eight-steps`（战术层，不动它，互链）、`framework-multi-agent-collab-chain-six`、`dk-extract-then-merge`

## 卡内容与结构建议

- 卡型：**concept**（战略结构洞察，非单点操作）
- 核心命题：能力复用的三级演化——①单 Skill（解决一个问题）②元 Partner（生产 Skill 的 Skill，"Skill 创业专家"）③Partner 生态（分身+Office 协作）
- 关键判别：什么时候值得先做元层？——同类需求会反复出现（调研/写作/设计），且单次封装成本高（最贵模型+十几轮打磨），元层把成本摊薄
- KDO 照镜子：五绝 spec 是"人封装 Agent"，楚门是"Agent 封装 Agent"——元层是角色产能从手工作坊到生产线的跃迁
- Critique 必写：元层不是银弹——需求不够高频时元层是过度设计（楚门自己也是先做出单个 Skill 再长元层）；元 Partner 的质量上限=它的知识库喂养质量

## 纪律与边界

- 行号溯源到口述原文；引用前查 ASR 对照表；"YI"=YAI、"奥森"=Obsidian
- 结构门禁按 concept 卡标准；related ≥5 且 ≥2 跨域；与八步卡/六环节卡互链（旧卡回链需求列清单，不动正文）
- `kdo pre-submit` 0 ERROR；O0 零编造
- 本任务只产 1 张卡；若生产过程中发现同源其他漏挖点，列清单报告，不顺手扩产

## 内容价值判断（PROTOCOL §7 合规声明）

- 只读素材+产 1 张新卡，不删/不移/不改任何已有文件

## 验收标准

1. 三级演化结构完整（单 Skill→元 Partner→生态）+ 每级行号溯源
2. Critique 含"什么时候不做元层"的边界
3. pre-submit 0 ERROR；与八步卡互链无死链
4. KDO 照镜子小节（五绝 vs 元 Partner 对照）

## 交付

1. 新卡 1 张 + 旧卡回链需求清单
2. 送欧阳锋终审

---

## 执行报告（2026-08-20 老顽童 hermes 实例）

### 完成概要
1 张 concept 卡（concept-meta-skill-layering 元技能分层）完成，pre-submit ✅ PASS。

### 卡内容
- **卡型**：concept（战略结构洞察）
- **核心命题**：能力复用三级演化——①单 Skill（解决一个问题）②元 Partner（生产 Skill 的 Skill，"Skill 创业专家"）③Partner 生态（分身+Office 协作）
- **关键判别**：同类需求反复出现 + 单次封装成本高（最贵模型+十几轮打磨）→ 元层摊薄成本；两条件缺一=过度设计
- **KDO 照镜子**：五绝="人封装 Agent"（spec 驱动）vs 楚门="Agent 封装 Agent"——元层是角色产能从手工作坊到生产线的跃迁
- **Critique**：元层非银弹（楚门自己先做单 Skill 再长元层）；元 Partner 质量上限=知识库喂养质量；三级演化渐进不跳级

### 溯源
- 口述 L1056-1110（Skill 创业专家全流程：L1060-1062 提需求/L1062-1064 搜方法论/L1074-1080 龙虾自学/L1088-1096 质量震撼）+ L2454-2458（Partner 生态苗头）
- 逐字稿 L335-400（高阶技能封装案例：快速认识→翻译解读→自建教程→逐步打磨→封装）
- 口径修正已遵循：YAI=一堂知识库之上的 Agent 体系（非单一工具）；"Skill 创业专家"是 YAI 体系中的一个 Partner（老朱 08-20 权威裁定）
- 两处待核矛盾规避：未引莫非老师/半肥猫人名、未引元旦年份

### 验证
- kdo pre-submit ✅ PASS（发现并修复隐性门禁：检索索引新鲜度——新卡比 .kdo/search_index.json 新，跑 `kdo index` 后通过；该门禁在报告输出不可见但计 failed）
- WIKILINK 0 死链；related 7 项 ≥5 且 ≥2 跨域（dk-ai-builder-illusion / framework-yitang-y-model-cross-domain-fusion）

### 旧卡回链需求清单（列清单，不动旧卡正文，交编排裁决）
| 旧卡 | 建议回链 | 理由 |
|:--|:--|:--|
| tool-skill-packaging-eight-steps | → concept-meta-skill-layering | 战术层↔战略层互链 |
| framework-multi-agent-collab-chain-six | → concept-meta-skill-layering | 元层=协作链的"技能生产环节" |

---

## 欧阳锋终审（2026-08-20 · O0 溯源抽查）

**裁定：PASS A。** 验收标准 4 项全过。

**O0 溯源抽查（concept-meta-skill-layering）**：
- 口述稿 L1060-1062「Skill 创业专家…调研的专家…搜调研方法论」**逐字命中** ✓（YI=YAI 口径修正已标注）
- L1088「顾问公司、咨询公司估计都达不到这个水平」→ 卡"顾问公司都达不到" ✓
- L1096「至少…1000块钱以上」✓ / L1074-1080「挑了两三个龙虾…现场给我学会干活…全程不做粘贴」✓
- 逐字稿 L355-367「先快速认识…一步步推动实现」→ Critique 反驳 1 锚点对应 ✓

**验收标准**：① 三级演化表（单 Skill→元 Partner→生态）+ 每级行号锚点 ✓ ② Critique 含"什么时候不做元层"（§3 两条件判别+反驳：低频=过度设计）✓ ③ pre-submit PASS（顺带发现并修索引新鲜度隐性门禁）+ WIKILOCK 0 死链 + related 7 ≥2 跨域 ✓ ④ KDO 照镜子节（五绝"人封装 Agent" vs 楚门"Agent 封装 Agent"——角色产能手工作坊→生产线跃迁）✓

**纪律加分**：reviewed_by: pending（E018）+ PROTOCOL §7 内容价值判断节 + 矛盾规避（莫非老师/元旦年份）+ 边界执行（只产 1 张，漏挖点列清单不顺手扩产）。

**回链清单 2 项**（tool-skill-packaging-eight-steps / framework-multi-agent-collab-chain-six → 本卡）记 TODO 交编排裁决，不阻断。
