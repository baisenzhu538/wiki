---
id: framework-openclaw-vs-harness-selection
title: OpenClaw vs Harness 选型决策树——70% 论 × 三分法（养员工/造工具/打短工）
type: framework
status: draft
domain:
- ai-basic
- ai-collaboration
author: 老顽童
reviewed_by: 待审
confidence: 0.85
trust_level: medium
source_person: Truman（老朱转述）
source_context: 战略笃定篇口述（L1376-1392 三分法；L1716-1718 70%论；L1688-1774 Harness 详述；L1318-1346 OpenClaw 灵魂赋能/10角色），老朱一手体感
source_refs:
- 00_inbox/我用一堂做一堂/战略笃定-一堂AI转型复盘-口述.txt
- 30_wiki/tools/tool-ai-agent-feature-comparison.md
confidence_notes: 70% 论与三分法为 Truman 口述一手表述；DeepSeek Harness 为 2026-08 新工具、老朱手操验证中，实跑定论待补充
aliases:
- OpenClaw vs Harness 选型决策树
- 70%论
- 三分法
- 养员工造工具打短工
- 战略笃定-一堂AI转型复盘-口述
- 我用一堂做一堂
- tool-ai-agent-feature-comparison
- tool-ai-agent-feature-comparison.md
- 工具选型决策树
- OpenClaw还是Harness
- 什么情况用OpenClaw
- 什么情况用Harness
discoverable_by:
- OpenClaw选型
- Harness选型
- 70%论
- 三分法
- 养员工
- 造工具
- 打短工
- OpenClaw
- Harness
- 选型决策树
- 工具选型
related:
- tool-ai-agent-feature-comparison
- framework-truman-feature-thinking-core
- agent-spec-basic-skills-coach
- case-truman-ai-native-research-flow
- case-openclaw-selfbuilt-agent-platform
- framework-wanghuan-harness-seven-stages
- dk-decision-value-overrides-roi
tags:
- audience:manager
- audience:executor
- scene:tool-selection
- scene:planning
- skill-level:intermediate
- method:tool-selection
created_at: 2026-08-30
updated_at: 2026-08-30
quality_labels:
- actionable
- insight
diagnostic_signals:
- signal: 用户问'到底什么情况用 OpenClaw、什么情况用 Harness'
  severity: medium
  implication: 先过三分法决策树定位（养员工/造工具/打短工），再看差异化 Feature——不是比"哪个工具好"
- signal: 团队在 Agent 工具选型上反复纠结、换了又换
  severity: medium
  implication: 70% Feature 重叠说明纠结重叠部分无意义——用决策树锁任务类型，差异部分才是选型依据
---

> **定位**：属于 [[framework-truman-feature-thinking-core]] 的应用层选型卡——用 Feature 思维回答"什么情况用 OpenClaw / 什么情况用 Harness"。逐工具 Feature 明细见 [[tool-ai-agent-feature-comparison]]，本卡专注**选型决策树**（先问任务类型，再选工具）。

# OpenClaw vs Harness 选型决策树

> 一句话：**所有 Agent 工具 70% Feature 重叠，选型不看重叠部分——先过三分法（养员工/造工具/打短工）锁任务类型，再看差异化 Feature。**

---

## 一、70% 论（Truman 原话）

> 「CodeX WorkBody 龙虾 Hermes 啊，什么什么什么 Harness，反正这一套……它的70%是一样的。他在完成70%的任务，就是 A 阵的那些那个 Feature，他是一样的。」（口述 L1716）
> 「CodeX 有额外的一些 Feature，然后那个 WorkBody 也有啊，然后龙虾也有，每个都有额外的那么一批 10~30 个 Feature。」（口述 L1718）

**含义拆解：**

| 层 | 内容 | 对选型的意义 |
|:--|:--|:--|
| **70% 公共 Feature** | 写调研、写脚本、改文档、常规对话——所有 Agent 都会 | 不值得纠结——"随便用个最糙的 Agent，区别也不大"（L1748） |
| **10-30 个差异化 Feature** | 各工具专属：长期记忆 / 角色身份 / 组件化 / 云端长跑等 | 选型依据——你的任务需要哪几个专属 Feature |
| **你的资产** | 数据、工作流、审美、判断 | Truman 原话：「你的数据，你的工作流，你的审美，你的判断对这事影响会更大」（L1730） |

> ⚠️ 数字标注：70% / 10-30 个为 Truman 口述估计（口述待独立核实），非实测基准测试结果。

---

## 二、三分法决策树（核心）

```
你要用 Agent 做什么？
│
├─ Q1：任务是一次性的，做完就关？
│   ├─ 是 ────────────────→ 【打短工】Codex / Claude Code
│   │                        （一次性 Session，无长期记忆/角色/进化）
│   │
│   └─ 否：要长期协作、跨会话积累
│       │
│       ├─ Q2：你要"养"它，还是"造"它？
│       │   ├─ 养（当人用：记忆+角色+主动+陪伴进化）
│       │   │   └─ Q3：OpenClaw 还是 Hermes？
│       │   │       ├─ 要角色化养成、灵魂赋能、岗位边界 → OpenClaw
│       │   │       └─ 要多 bot 常驻值守、7×24、密钥池并行 → Hermes
│       │   │
│       │   └─ 造（当工具台：组件化+插件可改+多机部署）
│       │       └─ 【造工具】DeepSeek Harness
│       │           （"把个人定制 Harness 工作台门槛打掉"，L1764）
│       │
│       └─ Q4：现有工具跑不满，需要定制/多机？
│           └─ 是 → 升级到 Harness 层（组件化/跨平台/内网穿透多机）
```

**判断口诀**：任务做完就结束、下次从零开始 → 打短工；要长期记住你、当人养、主动找你 → 养员工；要定制一套自己的 Agent 工作台、多机部署 → 造工具。

**三分法三层的本质区别（Truman 口述 L1376-1378）：**

| 层 | 隐喻 | 记忆/角色 | 典型工具 | 一句话 |
|:--|:--|:--|:--|:--|
| **项目制** | 打短工 | 无（Session 结束就关，最多落到文档） | Codex / Claude Code | 干完即走，不养不造 |
| **Agent 级** | 养员工 | 有（长期记忆+角色身份+主动汇报+陪伴进化） | OpenClaw / Hermes | 当"一个封装过的人"养 |
| **工作台** | 造工具 | 按需（Data Pack / 插件暴露） | DeepSeek Harness | 自己造一个用着顺手的 Agent 工作台 |

> 「项目制的工作我会用 Codex Cloud Code 来做，因为他们就是一个 Session 嘛，Session 结束就关了……Agent 的层呢，就是我把它当人，一个封装过的人这一层，我会用龙虾和 Hermes 啊，然后统一调度。」（口述 L1376-1378）

---

## 三、触发场景表（每类 2-3 场景 + 1 反例）

### 3.1 打短工（Codex / Claude Code）

| 触发场景 | 为什么选 | 口述/体感依据 |
|:--|:--|:--|
| 一次性长代码任务、跑一夜 | Codex 云端长跑不占本地 | 「开始用 Codex 了，Codex 一定程度上吃了我很多龙虾的场景」（L1374） |
| 项目制交付，做完落文档即可 | Session 模式够用，无需长期记忆 | 「项目制的工作我会用 Codex Cloud Code 来做」（L1376） |
| 快速原型 / Vibe Coding 实验 | 起手快、不配置、干完就扔 | 老朱 Vibe Coding 10+ 实验项目（逐字稿 L495） |

**反例**：想配置一个"每周主动汇报、记得你偏好"的长期员工 → 不要用 Codex/Claude Code（无长期记忆/角色/主动），应升级到养员工层。

### 3.2 养员工（OpenClaw / Hermes）

| 触发场景 | 为什么选 | 口述/体感依据 |
|:--|:--|:--|
| 长期角色化协作：给 Agent 起真人名、写岗位 JD、划权限边界 | 灵魂赋能后表现质变 | 「给 Agent 起了一个跟 100% 真人一样的同事的名字……像写 JD 样……两三千字的灵魂赋能文档」（L1318-1326） |
| 多角色团队分工：不同 Agent 不同身份/思维方式/权限隔离 | 硅基组织行为学、10 角色团队 | 「我把我的 AI 团队分成了 10 个角色……每一个岗位我都认真的写了它的负责它的任务清单以及它的边界」（L1334-1336） |
| 需要主动汇报/写任务书/分发调度 | Agent 层"当人"才有主动性 | 「一个龙虾钓几个 Hermes」（L1372）；「他会写一个任务书……然后分发过去」（L1370） |
| 7×24 常驻值守、多 bot 并行 | Hermes 唯一常驻 bot 形态 | 六角色全跑在 Hermes（KDO 映射，见 §四） |

**反例**：只想快速做一个一次性调研任务 → 不要配置 OpenClaw/Hermes 员工（养员工有配置成本，杀鸡用牛刀），回到打短工层。

### 3.3 造工具（DeepSeek Harness）

| 触发场景 | 为什么选 | 口述/体感依据 |
|:--|:--|:--|
| 想要一套完全定制、自己顺手的工作台 | 组件化到官方都组件化，插件可改 | 「它把一切组件化了……连他官方那些都是组件化的，所以一定程度上，当插件之后你都能改」（L1770-1772） |
| 多机部署、内网穿透、随处办公 | 分布式工作台，4-5 台电脑 × 6-10 Session | 「我有几个不同的电脑，然后我分别给每个电脑配了一个 Harness，然后用内网穿透的方式穿到任何一台电脑里」（L1688-1692） |
| 想造"给孩子定制学习工作台"这类个性化产品 | 把个人定制工作台门槛打掉 | 「你可以给你孩子定制一个属于他的 Harness 的工作台……你这一套就比那些通用的 Agent 其实要好」（L1756） |
| 需要改 Agent 行为细节（如消息提醒插件） | 可定制性强，Codex 难实现 | 「这个玩意儿就是在 Harness 就非常快乐，你可以随便往里加东西」（L1746） |

**反例**：你的需求只是"长期养一个懂我的助理" → 不要先上 Harness（Harness 是工作台/造工具层，灵魂赋能/陪伴进化是 OpenClaw/Hermes 层的差异化 Feature）。

---

## 四、KDO 映射（本框架在 KDO 工厂的落地）

| KDO 资产 | 对应层 | 说明 |
|:--|:--|:--|
| **六角色 Agent（老顽童/黄药师/欧阳锋/王语嫣/洪七公/段王爷）** | 养员工（Hermes ≈ OpenClaw 层） | 长期记忆+角色身份+主动汇报，跑在 Hermes 上 |
| **KDO 知识库（30_wiki 卡片）** | 养员工的长期记忆 | Feature 卡片 = Agent 的可迁移 Feature 库 |
| **pipeline / 门禁 / 脚本（queue_transition.py、pre-submit、kdo lint）** | 造工具（可 Harness 化） | 组件化、可定制、多角色调用的工作台候选 |
| **一次性生产任务（单卡/单批）** | 打短工 | 用 Codex/Claude Code 类一次性会话执行，不占用长期员工 |

> KDO 的现状：六角色=养员工层（Hermes），基建脚本=可 Harness 化的工作台组件。选型决策树对 KDO 的直接应用：**生产任务走打短工，角色协作走养员工，基建定制走造工具**。

---

## 五、When NOT to Use

| 场景 | 后果 | 正确做法 |
|:--|:--|:--|
| 工具还没上手就想做精细选型 | 纸上谈兵——Harness 的定制优势要实跑才体会得到 | 先各跑一个真实任务再选（老朱"手操验证中"同款姿势） |
| 想靠换工具解决流程/资产问题 | 换工具不解决"数据/工作流/审美"问题——这些才是影响更大的变量（L1730） | 先梳理任务类型 + 资产，再选工具 |
| 团队规模大、管理能力强 | 一号位不一定必须下场（Truman 特别说明"特指我们一堂"） | 按公司形态判断是否走养员工层 |
| 纠结 70% 重叠部分 | 越比越晕，重叠部分选谁都一样 | 直接跳到差异化 Feature 比较（§二决策树 Q2-Q4） |
| 任务是一次性的却配置了员工 | 配置成本 > 收益，养了不用 | 回到打短工层 |

---

## 六、常见失败模式

| 失败模式 | 症状 | 修复动作 |
|:--|:--|:--|
| **工具思维选型** | 问"哪个工具最好"，不问"我的任务属于哪层" | 先跑三分法决策树（§二），锁任务类型再看差异化 Feature |
| **单一工具押注** | 把所有任务压在一个工具上，任务类型不匹配时抱怨"工具不行" | 按任务类型分层：短工/员工/工作台可并存（Truman 同时用 Codex+龙虾+Hermes+Harness） |
| **忽略资产层** | 反复换工具，数据/工作流/审美没沉淀 | 先建资产（Feature 库/数据包/工作流），工具抓来就用（L1392"都是一堆干活的"） |
| **养员工当短工使** | 配置了灵魂赋能文档但只做一次性任务 | 员工只用于长期协作；一次性任务走 Codex/Claude Code |
| **把 Harness 当员工养** | 在 Harness 上期待"陪伴进化/主动汇报" | 陪伴进化是 OpenClaw/Hermes 层 Feature；Harness 是工作台（L1206 三层边界） |
| **不验证就定论** | 凭文档定位选型，忽略实际体感 | 以实战体感为准——Harness 尚在入门期，老朱"还在入门期"（L1420） |

---

## 七、Action Triggers

| 触发场景 | 第一个动作 |
|:--|:--|
| 要选工具跑新任务 | 跑三分法决策树（§二）→ 一次性=打短工；长期协作=养员工；定制工作台=造工具 |
| 用户问"OpenClaw 还是 Harness" | 反问任务类型：要养员工→OpenClaw；要定制工作台/多机→Harness（先三分法再比 Feature） |
| 团队在工具间反复横跳 | 检查是不是在纠结 70% 重叠部分——重叠部分不值得纠结，锁差异化 Feature |
| KDO 要新建 Agent/脚本 | 映射 §四：角色→养员工层；pipeline/门禁→造工具候选；一次性生产→打短工 |

---

## 八、Critique

### 内部局限

1. **三分法基于 Truman 一手体感**（2025.8-2026.8 一年实践），样本是创业者/研究型公司场景——大公司组织化 AI 落地可能不完全适用（Truman 自己在第二轮强调"特指我们一堂，你们很多公司不一定的"，L600）。
2. **70% 论是口述估计**，无公开基准测试数据支撑——工具迭代快（月月变），今日的差异化 Feature 三个月后可能被吸收为公共 Feature。
3. **DeepSeek Harness 尚在入门期**（老朱 2026-08 刚上手，L1420"我现在还在入门期"），"造工具"层的完整 Feature 边界待实跑补充。

### 外部攻击者

**[工具中立派（效率视角）]**
> "与其花时间选型，不如随便用一个工具把活干了——选型本身在浪费时间。"

**回应**：对 70% 重叠的任务成立（随便用哪个区别不大，L1748）。但 10-30 个差异化 Feature 在长期任务上放大——养员工层的灵魂赋能、造工具层的定制化，是"随便用一个"拿不到的。选型成本应只花在差异化 Feature 上，重叠部分不纠结（这正是 70% 论的使用方式）。

**[组织行为学者]**
> "把 Agent 当人养、给岗位起名字，可能是拟人化幻觉——流程/工具导向的组织会更高效。"

**回应**：这是市场真实分歧（Truman 在闲聊中承认："市场上有一派分工是不按人类分，别用人类的习惯……你就用工作流去串联他们"，L1560-1562）。拟人化养员工适合"调教出可用水平"的早期阶段；Truman 自己也说"如果有一天它遇到门就上不去了，我可能会用一套新的东西把它们重构一遍"（L1562）。选型决策树应被看作**阶段适配**而非永恒结论。

**[Feature 周期论者]**
> "工具会互相吞噬——Harness 组件化可能抹平工作台类商业价值，选型树很快就过时。"

**回应**：同意——Truman 自己判断"Harness 是未来一个定制化的一套基础框架，它会把一部分通用的工作台级别的商业价值给抹平"（L1750-1752）。所以决策树的**判断逻辑**（先任务类型→再差异化 Feature→资产比工具重要）比**具体工具名**更耐久；工具列应随周期律更新（见 feature 周期律 V0.8）。

---

## 九、与其他知识的关联（Synthesis）

| 关联卡 | 关系 |
|:--|:--|
| [[tool-ai-agent-feature-comparison]] | 本卡的明细底座——本卡出决策树视角，该卡出逐工具 Feature 表（互补不重复） |
| [[framework-truman-feature-thinking-core]] | 本卡是 Feature 思维的应用层——"先问 Feature 需求，再选工具" |
| [[agent-spec-basic-skills-coach]] | 养员工层的 KDO 实例——Agent 规格=岗位 JD 的 KDO 化 |
| [[case-truman-ai-native-research-flow]] | 养员工层实战案例（MUSE 模型+3 Agent 协作） |
| [[case-openclaw-selfbuilt-agent-platform]] | OpenClaw 层实战案例——排飞书微信→A2A 直连→项目空间隔离 |
| [[framework-wanghuan-harness-seven-stages]] | 造工具层的方法论参考——Harness 七阶段工作流 |
| [[dk-decision-value-overrides-roi]] | 选型背后的决策本质——决策不是只看收益，是愿意承受多大代价 |

*Truman 战略笃定篇口述 + 老朱一手体感 · 2026-08-30 · #575*
