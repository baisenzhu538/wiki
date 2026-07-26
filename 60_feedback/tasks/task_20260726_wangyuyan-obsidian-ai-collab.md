---
id: task_20260726_wangyuyan-obsidian-ai-collab
task_id: 204
assignee: laowantong
status: queued
created_at: 2026-07-26
updated_at: 2026-07-26
domain: system
priority: P1
source: 00_inbox/一堂-obsidian加AI协作-内部实践分享/
diagnosis: 60_feedback/diagnosis/diag_20260726_wangyuyan-obsidian-ai-collab.md
---

# Obsidian+AI协作 · 卡片化生产任务

## 任务目标

从于陆Live83分享中提取"Obsidian+AI协作"方法论，产出2张新卡+升级1张已有卡。核心洞察：**命名即基础设施**、**YAI是长出来的不是设计出来的**。

## 素材

| 文件 | 路径 |
|:--|:--|
| Live83逐字稿 | `00_inbox/一堂-obsidian加AI协作-内部实践分享/AI落地Live83_探索AI协作新范式_逐字稿.md` |
| 口述 | `00_inbox/一堂-obsidian加AI协作-内部实践分享/一堂-obsidian加AI协作-内部实践分享-口述.txt` |
| 笔记 | `00_inbox/一堂-obsidian加AI协作-内部实践分享/一堂-obsidian加AI协作-内部实践分享-笔记.txt` |

## 卡片规格

### 新卡（2张）

| # | id | type | title | 核心内容 |
|:--|:--|:--|:--|:--|
| 1 | concept-structured-naming-as-infrastructure | concept | 结构化命名即基础设施：人机共识的文件系统设计 | 月白(设计域八要素法)+于陆(知识域00/1x/3x/5x/6x/9x)的独立共振。核心主张：命名不是为了整洁，是为了使人和AI都能"扫读文件夹、批量操作、无需逐文件打开"。含OKF范式验证。连接KDO自身命名体系并显式声明设计意图 |
| 2 | method-obsidian-ai-collaboration | method | Obsidian+AI协作最佳实践：从一次交付到持续资产 | 完整五要素：§1协作双目标哲学(当下交付+未来数据) §2文件夹命名规则 §3清单式笔记·AI协作场景 §4工具对比(Obsidian vs 飞书) §5三阶段案例(一堂内部) §6 YAI诞生拼图(链接闪电模型+龙虾+Obsidian+清单笔记+顶层文档)。暗知识嵌入："聊天不适合承担全部长期记忆""人不是把思维外包给AI是把低价值维护外包" |

### 升级已有卡（1张）

| # | 对象 | 动作 | 内容 |
|:--|:--|:--|:--|
| 3 | `tool-清单式笔记法` | 新增§节 | "AI协作数据资产场景"——"不是为了记得更多，而是为了让协作内容更容易被继续加工"。人+AI接力加工的标准化格式。引用于陆口述L698-704 |

**合计：2新卡 + 1升级**

## 验收标准

1. source_refs引用口述稿行号
2. concept卡必须含：月白命名哲学(摘引已有卡)+于陆命名规则+OKF外部验证+KDO自身命名体系声明
3. method卡必须含：完整五要素+三阶段时间线+YAI拼图(引用闪电模型+龙虾+YAI角色卡)
4. `tool-清单式笔记法` 升级后含"AI协作数据资产场景"独立§
5. related ≥5且≥2跨域
6. 提交前跑`kdo pre-submit`

## 已有卡关联

| 已有卡 | 关系 | 动作 |
|:--|:--|:--|
| `tool-月白-设计文件八要素命名法` +其余5张月白命名卡 | 同源共振：设计域↔知识域 | concept卡related引用全部6张，统一标注"命名=协作基础设施" |
| `tool-月白-设计师AI资产四类型沉淀` | 资产沉淀逻辑同构 | method卡related单向 |
| `framework-yitang-thought-liberation-lightning` (#201) | 闪电模型是YAI的方法论引擎 | method卡§YAI拼图引用 |
| `yai-counsel-role` / `yai-tcp-teacher-role` | YAI现在的角色形态 | method卡§YAI拼图引用"现在的YAI" |
| `concept-collaboration-philosophy-foundation` (#202) | 博弈环境面向未来=当下交付+未来数据 | method卡§协作哲学引用 |
| `framework-kdo-modeling-methodology` | YAI诞生链=真实过程≠事后框架 | method卡§YAI拼图引用 |
| `case-wenxiaobao-campus-bilateral-network` (#201) | 半肥猫→Truman推荐线 | method卡§YAI拼图提及 |

## 边界

- **不覆盖**：龙虾/Cherry Studio/Codex具体操作教程（已有于陆原文）
- **不覆盖**：Obsidian插件配置
- **域归属**：归入system域（KDO基础设施），桥接design域（月白命名卡）
