---
id: task_20260904_laowantong-transcript-to-qingdanti-skill
title: 清单体生产 skill：口述稿→清单体笔记（分层编号/重点前置/提出-展开-回收）+ Live261 试跑交付老朱验收
seq: 638
status: pending_review
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-04
decision_source: 老朱 09-04 直令立项（知识卡未用清单体方法论的知行断裂修复）
reviewer: 欧阳锋
source_refs:
- 00_inbox/一堂-AI时代清单体笔记-Truman-口述-01.txt
- 30_wiki/concepts/concept-提升笔记阅读舒适度.md
- 30_wiki/concepts/concept-问题驱动式深度思考笔记.md
instance: laowantong
updated_at: '2026-09-04T13:40:06.514759+00:00'
evidence: 60_feedback/tasks/task_20260904_laowantong-transcript-to-qingdanti-skill.evidence.md
---

# #638 清单体生产 skill（老顽童）

## 建模方案（L1 出牌，2026-09-04 laowantong）

依赖链：`[素材牌] → [边界牌] → [结构牌] → [过程牌] → [质量牌]`

| 牌号 | 牌名 | 一句话理由 |
|:--|:--|:--|
| 素材 #3 | 先口述稿再笔记 | 标准源=122KB 清单体口述稿，已逐字全读（2374 行），不凭笔记摘要下结论 |
| 素材 #4 | 先扫信号词再读内容 | 口述稿中"划重点/举个例子/来感受一下"段落=审美示范高密度区，全部落进 skill 规则 |
| 边界 #6 | 先查已有卡再新建 | 已查：note-coach（教练 agent，非生产 SOP）、tool-清单式笔记法（概念卡）均不等价，无重复建设 |
| 边界 #7 | 先对标准则再命名 | "清单体/qingdanti"为一堂内部术语已在库（yt-note 卡族），不与国际术语冲突，沿用 |
| 结构 #10 | 先骨架再填肉 | skill 先写死六条产出标准（分层≤3/编号序列/重点前置/提出-展开-回收/一分钟扫完/全>简不漏），再展开流程 |
| 过程 #14 | 先跑脚本确认再声称完成 | 试跑笔记完成后逐条机械自检（层级数/编号/首句结论/数字保留），实测再报 |
| 质量 #15 | 先自攻击再提交 | 交付前自检四问：有没有创造原文没有的内容？有没有信息丢失？层级超标？首句非结论？ |

## 背景

清单体方法论在库（122KB 口述全稿+训练段位图+L1-L6 卡族）但生产线零引用（90_control/40_outputs grep 实证）——老朱点破的知行断裂。本单把「口述稿→清单体笔记」做成产线能力。

## 任务

1. **skill 落地**：`40_outputs/capabilities/skills/shared/transcript-to-qingdanti/`（SKILL.md+manifest）——标准源=清单体口述稿+段位图结构化件+yt-note 卡族；产出标准写死：分层≤3 层/编号序列/重点前置（每节第一句是结论）/提出-展开-回收闭环/一分钟扫完自检/全>简但不漏（口述一等全覆盖）
2. **试跑**：用 `00_inbox/Live261-一堂战略笃定作业candy-逐字稿.md` 主件（教育版论持久战）产一份清单体笔记，落 `40_outputs/content/`——老朱肉眼验收件
3. 红线：不改变原意不创造内容（清单体=结构重组非再创作）；长稿分段处理防截断

## 交付

- skill 目录 + 试跑笔记（40_outputs/content/）+ 执行报告
- claim/complete 走 queue_transition（complete 638）

## 执行报告（2026-09-04 laowantong）

**交付物**
- `40_outputs/capabilities/skills/shared/transcript-to-qingdanti/SKILL.md` + `manifest.yaml`（口述稿→清单体笔记生产 SOP v1.0.0）
- `40_outputs/content/live261-zhanshududing-qingdanti-note.md`（Live261 试跑清单体笔记，老朱肉眼验收件）

**完成内容**
- 素材全量消费：清单体口述稿 122KB/2374 行逐字全读；系统故事线+训练段位图结构化件全读；yt-note 卡族（five-levels-training/live-field-skill/fact-pattern-insight/l4-internalization/l6-extraction/dk×2/tool-清单式笔记法）+ 任务单指定两张概念卡全读；Live261 逐字稿 868 行全读
- skill 写死六条产出标准（分层≤3层/编号序列/重点前置/提出-展开-回收/一分钟扫完/全>简但不漏），含五步流程、信息删留对照表、六条判断标准、九条失败模式（全部来自口述稿实证，如串糖葫芦/手工编号/逐字誊抄）
- 试跑笔记：Live261 全量重组为 5 节（总览+主作业+路禹+Jacky+李秀慧+总回收），每节结论前置+回收句闭环；原文 58KB→笔记 23.5KB（约 40%，全>简：关键信息零丢失）

**验证**
- `kdo pre-submit -f 40_outputs/capabilities/skills/shared/transcript-to-qingdanti/SKILL.md` → ✅ PASS（0 issues，一次通过）
- `kdo pre-submit -f 40_outputs/content/live261-zhanshududing-qingdanti-note.md` → ✅ PASS（首轮 FAIL 无 frontmatter → 补齐后 PASS；aliases WARNING 已修 → 复跑全清）
- 机械自检（牌 #14，grep 实测）：①无 ≥3 级缩进列表行（分层≤3）②无手工字符编号（"一、""1)"零命中）③关键数字/事实 14 项抽查全命中（1015 分/80%/1 亿 vs 2000 万/50%-60%/三四家/2023 年 9 月/8 年/4 个 IP/5w/7 要素/15 个磨课例/战略防御等）④5 个 H2 节均有加粗结论前置句+回收句
- 结构对账：笔记四节与原文四大块（V1.0 作业/路禹/Jacky/李秀慧）一一对应，无新增观点、无原文外升华

**边界**
- 本 skill 只做"结构重组"，不做再创作；评论/分析类产出不在边界内（SKILL.md When NOT to Use 已写死）
- 试跑件是"老朱肉眼验收件"，非知识卡——未进 30_wiki，产线批量引用待终审后再议
- Live261 原文中 Jacky"两个关键认知""笃定三件事"等口述不完整处，按原文如实保留，未脑补
- #639（黄药师：生产规范补清单体标准）是后续衔接单，本单不动工业化手册

**需要谁动作**
- 欧阳锋：终审本单（skill 目录 + 试跑笔记）
- 老朱：肉眼验收试跑笔记 `40_outputs/content/live261-zhanshududing-qingdanti-note.md`
- 黄药师：skill 已落在 shared/ 桥接点，无需补桥；`kdo index --rebuild` 按需（新 skill 目录+新 content 文件）

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 2 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（丢失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）
