---
id: task_20260816_laowantong-ai-km-wave-b
assignee: hermes
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-16
priority: P1
wsjf: 3.5
created_at: 2026-08-16
updated_at: '2026-08-16T05:58:00.351967+00:00'
source: 王语嫣编排（2026-08-16）；AI 知识库全域启动
related: null
---

# AI×知识管理 Wave B：工具与案例 9 卡（#340）

## 背景

Wave A（#336）六卡入队后，本批 = 工具与案例 9 卡（锚点见生产任务清单 task_20260816_ai-knowledge-management-production.md Wave B 表）。

## 卡清单（9 张）

| ID | 类型 | 名称 | 锚点 |
|:--|:--|:--|:--|
| B1 | tool | 知识小抄 S/A/B 三级收录清单 | 015204 |
| B2 | tool | 顶层文档制度 | 批注 213157 + L648-706（四字开头/每年 100+/新人两天入门/离职补两篇） |
| B3 | tool | Skill 封装八步流水线 | 015300 + L960-1160（先萃取再合并、10 ToDo+10 NoToDo、交叉打分、配 YAI Partner） |
| B4 | concept | AI Style 新型知识文档 10-11 种 | 015515 + 批注 221751/221853 |
| B5 | case | VibeCoding 训战营一周交付 | 015547/015601 + L1990-2360（三种协作方式对比+五核心文档+一周 vs 两月） |
| B6 | case | 新年洞察一封信四棒接力 | L1810-1990（每次交接只说一句话） |
| B7 | framework | 偶遇自动采集五通道+120 万字机制 | 015814 + L2520-2870 |
| B8 | tool | 自动分类脚本 7 步+MUSE 目录 | 015732/015737（LongCat/T1 强制 S/frontmatter/审计日志） |
| B9 | framework | PatrolKit 知识资产雷达 | 015759（健康检查/记忆补全/资产回收/技能迁移→复利飞轮） |

## 验收标准

- 9 卡 frontmatter 规范（source_refs 口述行号主锚、related ≥5）
- 互链：B2（顶层文档）↔ #339 试点顶层文档；B9（PatrolKit）↔ #338 设计文档
- 2 处待核矛盾以逐字稿为准+标注
- `kdo pre-submit` PASS + `kdo lint` 零 FAIL

## 边界

- 单角色单任务（E026）：老顽童生产，欧阳锋终审
- 队列顺序：#336 → #340

## 执行报告（老顽童 hermes 实例，2026-08-16）

### 产出（Wave B 九卡全部完成）
| ID | 类型 | 文件 | 关键内容 |
|:--|:--|:--|:--|
| B1 | tool | `30_wiki/tools/tool-knowledge-cheatsheet-sab.md` | 小抄 S/A/B 三级（大量/偶尔/不再复用）；015204 图 |
| B2 | tool | `30_wiki/tools/tool-top-level-document.md` | 顶层文档制度（四字开头/有且只有一个/必知必会前置/新人两天入门/离职补两篇）；L648-706+批注 213157 |
| B3 | tool | `30_wiki/tools/tool-skill-packaging-eight-steps.md` | Skill 封装八步（下载标杆→翻译→建模→最贵模型→纠偏 10ToDo+10NoToDo→交叉打分→封装→现场学）；L998-1096+015300 |
| B4 | concept | `30_wiki/concepts/concept-ai-style-knowledge-docs.md` | AI Style 文档 10-11 种（能力/数据/设计/复盘四方向）；015515+批注 221751/221853 |
| B5 | case | `30_wiki/cases/case-vibecoding-one-week-delivery.md` | 训战营一周交付（900 页 PPT+100-120 AI 图）；三种协作方式对比（2-3 月/4-6 周/1 周）；五核心文档；015547/015601 |
| B6 | case | `30_wiki/cases/case-new-year-insight-relay.md` | 四棒接力（PM→Truman→编辑→志钊）；每次交接只说一句话；补三个关键文档；L1810-1990 |
| B7 | framework | `30_wiki/frameworks/framework-serendipity-five-channels.md` | 偶遇五通道自动采集（文章/视频/创作者/选题/开源项目）；120 万字机制；饱和话术；L2520-2870+015814 |
| B8 | tool | `30_wiki/tools/tool-autoclassify-seven-steps.md` | 自动分类 7 步（提取→关键词参考→LongCat→T1 强制 S→frontmatter→移动→日志）；015732/015737 |
| B9 | framework | `30_wiki/frameworks/framework-patrolkit-radar.md` | PatrolKit 四模块（健康检查/记忆补全/资产回收/技能迁移）；Before-Process-After；015759 已核验 |

### 素材精做
- 口述锚点区间逐字精读：L648-706（B2）/L998-1096（B3）/L1810-1990（B6）/L1990-2360（B5）/L2520-2870（B7）/L3290-3346（B8/B9）+ 相关 OCR（015204/015300/015515/015547/015601/015732/015737/015759+批注 213157/221751/221853）
- ASR 对照已核对（A镇=Obsidian/OPC=Obsidian/龙虾=OpenClaw）
- 精做笔记 `_tmp/ai-km-wave-b-精做笔记.md`

### pre-submit 门禁（9/9 PASS 零 warning）
- 全部 Passed 1/Failed 0 零 warning；related 8 条/卡、死链=0、跨域≥2

### 互链对照
- [x] B2↔#339 顶层文档试点（tool-top-level-document 与任务单互链——试点文档为 70_product/tasks/top-doc-爆炸式调研.md，制度卡已建）
- [x] B9↔#338 PatrolKit 设计（framework-patrolkit-radar 与 #338 设计文档互链）
- [x] C1↔爆炸式 W3-1（framework-serendipity-five-channels 内含饱和话术节，related 含 dk-research-important-things-must-do）

### 验收对照
- [x] 9 卡 frontmatter 规范（source_refs 行号/图锚点、related ≥5、domain 含 knowledge-management）
- [x] kdo pre-submit 9/9 PASS

### 边界遵守
- 单角色单任务（E026）；正文零虚构（全卡行号/图锚点）；数字以官方逐字稿/OCR 图为准
