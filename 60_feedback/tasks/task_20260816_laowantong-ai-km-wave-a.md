---
id: task_20260816_laowantong-ai-km-wave-a
assignee: hermes
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-16
priority: P0
wsjf: 4.0
created_at: 2026-08-16
updated_at: '2026-08-16T05:26:05.913315+00:00'
source: 王语嫣编排（2026-08-16 综合 codex/黄药师裁决）；diag_20260816_ai-knowledge-management.md
related: null
---

# AI×知识管理 Wave A：P0 框架主线 6 卡（#336）

## 背景

楚门公开拆解 vault 体系——**KDO 理论源头+照镜子**。诊断完成（diag_20260816_ai-knowledge-management.md）。本批 = P0 框架 6 卡（老顽童按队列顺序执行，#333/334 交付后领取）。

## 卡清单（6 张，锚点见生产任务清单 task_20260816_ai-knowledge-management-production.md Wave A 表）

| ID | 类型 | 名称 | 要点（口述锚点） |
|:--|:--|:--|:--|
| A1 | framework | 知识复利火箭六要素 | 超长周期/数量/质量/自动化/协作化/可掌控底线（L340-392 + 批注 211608） |
| A2 | framework | 五次知识管理飞跃 | 2013→2026 编年+触发点；AI 周期变短（015236/015814+全场） |
| A3 | framework | 多 Agent 协作链六环节 | 管理读写关系，上下文一轮轮变厚（批注 215606+L960-1160） |
| A4 | concept | Session<<AI记忆<<文档 | 降 Session 依赖；开会脑记/自觉小本本/文档会议三类比（批注 221150+L1360-1530） |
| A5 | framework | 双中心原则 | 飞书给人/Obsidian 给 AI；不迁移各用 Feature（015649+L2366-2400） |
| A6 | framework | Truman Agent 团队系统架构 | 缓冲站→Library→四库；三团队 10 Agent+负责人制（015649+L3080-3250） |

## 验收标准

- 6 卡 frontmatter 规范（source_refs 口述行号主锚、related ≥5）
- **互链**：A2↔master-knowledge-compound；A1↔yt-personal-knowledge-management；**模型祛魅 dk↔framework-kdo-context-design**（黄药师建议：#277/309 独立佐证）
- 2 处待核矛盾（莫非/半肥猫、元旦年份）：以官方逐字稿为准+卡内标注待核
- `kdo pre-submit` PASS + `kdo lint` 零 FAIL

## 边界

- 单角色单任务（E026）：老顽童生产，欧阳锋终审
- **队列顺序执行**（#333/334 在产，本批不插队）
- Wave B/C 另批（Wave A 交付后）

## 执行报告（老顽童 hermes 实例，2026-08-16）

### 产出（Wave A 六卡全部完成）
| ID | 类型 | 文件 | 关键内容 |
|:--|:--|:--|:--|
| A1 | framework | `30_wiki/frameworks/framework-knowledge-compound-rocket-six.md` | 火箭六要素（超长周期顶/数量×质量主体/自动化+协作化引擎/可掌控底线）；评价体系（L340-392+批注 211608） |
| A2 | framework | `30_wiki/frameworks/framework-knowledge-five-leaps.md` | 五次飞跃编年 2013→2026（个人→团队→AI×个人→多 Agent→自动化）；AI 周期变短规律（八年→四个月）；图 015236/015814 |
| A3 | framework | `30_wiki/frameworks/framework-multi-agent-collab-chain-six.md` | 协作链六环节（搜学→翻译→建模→封装→学习→沉淀）；管理读写关系让上下文变厚；批注 215606 已核验 |
| A4 | concept | `30_wiki/concepts/concept-session-vs-memory-vs-document.md` | Session<<AI 记忆<<文档三类比（开会脑记/小本本/文档会议）；降 Session 依赖纪律 |
| A5 | framework | `30_wiki/frameworks/framework-dual-center-feishu-obsidian.md` | 双中心（飞书给人/Obsidian 给 AI）；不迁移各用 Feature |
| A6 | framework | `30_wiki/frameworks/framework-truman-agent-team-architecture.md` | 缓冲站→Library→三团队（业务/研究/产品×10 Agent 负责人制）→四库；岗位画像；015649 已核验 |

### 素材精做
- 口述锚点区间逐字精读：L340-392（A1）/L1132-1144+Skill 实战 L998-1096（A3）/L1360-1530（A4）/L2366-2400（A5）/L3080-3250（A6）；A2 五次飞跃读理解消化件交叉（王语嫣通读锚点）
- ASR 对照已核对（三婶=Session/奥森=Obsidian/四店=四库/荷尔米斯=Hermes）
- **待核矛盾处理**：莫非老师 vs 半肥猫——卡内用"莫非老师"（逐字稿口径）；"23 年元旦"为 2026 元旦（逐字稿口径）——均已按官方逐字稿为准
- 精做笔记 `_tmp/ai-km-wave-a-精做笔记.md`

### pre-submit 门禁（6/6 PASS 零 warning）
- 全部 Passed 1/Failed 0 零 warning（aliases 补 AI知识库/源名带后缀变体）
- related 7-8 条/卡、死链=0、跨域≥2（A6 补 case-cross-xingangwan-pharma）

### 互链对照
- [x] A2↔master-knowledge-compound（已链）
- [x] A1↔yt-personal-knowledge-management（已链）
- [ ] 模型祛魅 dk↔framework-kdo-context-design——**framework-kdo-context-design 尚不存在**（Wave C C5 互链项，已从 related 移除并在正文标注"待建"；Wave C 生产时若卡仍不存在需先建或改纯文本引用）

### 验收对照
- [x] 6 卡 frontmatter 规范（source_refs 口述行号主锚、related ≥5、domain 含 knowledge-management）
- [x] kdo pre-submit 6/6 PASS

### 边界遵守
- 单角色单任务（E026）；队列顺序执行（#333/334 收官后领取）；正文零虚构（全卡行号/图锚点）
