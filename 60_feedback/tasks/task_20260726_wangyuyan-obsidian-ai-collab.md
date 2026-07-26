---
id: task_20260726_wangyuyan-obsidian-ai-collab
task_id: 204
assignee: hermes
status: pending_review
created_at: 2026-07-26
updated_at: '2026-07-26T12:18:01.913393+00:00'
iterations: 3 (Claude初版→飞书王语嫣深度迭代→洪七公OCR+最终融合)
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
| 2 | method-obsidian-ai-collaboration | method | Obsidian+AI协作最佳实践：从一次交付到持续资产 | 完整五要素：§1协作双目标哲学 §2文件夹命名规则 §3清单式笔记·AI协作场景 §4工具对比 §5三阶段案例 §6 YAI诞生拼图。§7 LLM Wiki对标(Karpathy: Raw→Wiki→Schema ↔ KDO: 10_raw→30_wiki→framework)。暗知识：聊天≠记忆工具、人外包的是维护不是判断。解压资产：tool-ai-collab-folder-template(四大起步文件模板) |

### 升级已有卡（1张）

| # | 对象 | 动作 | 内容 |
|:--|:--|:--|:--|
| 3 | `tool-清单式笔记法` | 新增§节 | "AI协作数据资产场景"——"不是为了记得更多，而是为了让协作内容更容易被继续加工"。人+AI接力加工的标准化格式。引用于陆口述L698-704 |

**合计：2新卡 + 1升级**

## 🔴 Patch升级（2026-07-26 飞书王语嫣+Claude最终融合）

### Patch 1：暗知识补充

method卡§暗知识节注入两组新增暗知识：

| 暗知识 | 来源 | 锚点 |
|:--|:--|:--|
| PDF丢60-70%信息量——AI要过OCR识别层 | Claude深挖 | 口述L672-674 |
| 学员三困惑：不用Obsidian有替代方案？/清单体和普通笔记差别？/怎么从零开始？ | 洪七公提取 | 建议书§五 |

### Patch 2：解压资产升级

四大起步文件模板从一行描述升级为独立规格行：

| 文件 | 编号 | 放什么 | 作用 |
|:--|:--|:--|:--|
| 顶层文档 | 00 | 项目内核（做什么）+边界（不做什么） | AI和人理解项目scope的第一入口 |
| 背景信息 | 1x | 原始素材、参考资料、相关课程笔记 | AI全量读取后形成项目上下文 |
| 过程文档 | 3x | 提示词版本、数据包迭代、人工校准记录 | 过程不丢——每次修改都有迹可循 |
| 交付产物 | 5x | 最终产出的卡片/文档/模板 | 人和AI都能直接取用的成品 |
| 测试验证 | 6x | 案例测试、lint/pre-submit结果 | 质量证据链 |
| 复盘沉淀 | 9x | 本次协作的复盘、踩坑记录 | 下一次协作的起点 |

### Patch 3：口述稿扫描

新增验收标准——老顽童开工前扫描63KB口述稿全文，确认：
- method卡所有关键claims能在口述稿找到行号锚点
- 洪七公+Claude捕捞的暗知识无遗漏
- 笔记中未覆盖但口述中出现的案例（如马拉松100个AI最佳实践数据包）已被纳入

---

## 验收标准

1. source_refs引用口述稿行号
2. concept卡必须含：月白命名哲学(摘引已有卡)+于陆命名规则+OKF外部验证+KDO自身命名体系声明
3. method卡必须含：完整七要素（含§7 LLM Wiki对标）+三阶段时间线+YAI拼图+Patch 1暗知识+Patch 2四大模板独立规格
4. `tool-清单式笔记法` 升级后含"AI协作数据资产场景"独立§
5. related ≥5且≥2跨域
6. 提交前跑`kdo pre-submit`
7. 🔴 Patch 3：老顽童开工前扫描63KB口述稿全文，确认暗知识无遗漏+关键claims有行号锚点

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
