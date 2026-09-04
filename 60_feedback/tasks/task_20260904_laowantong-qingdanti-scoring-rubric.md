---
id: task_20260904_laowantong-qingdanti-scoring-rubric
title: 清单体评分 rubric 化：训练段位图（L1-L6+六维）→ 可执行评分表 + transcript-to-qingdanti skill v1.1（两步法定位+自检门禁嵌入）
seq: 640
status: pending_review
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-04
decision_source: 老朱 09-04 设计定稿：两步法（深挖验收→清单体整理）+「清单体做得好不好要有评分规则」
reviewer: 欧阳锋
instance: laowantong
updated_at: '2026-09-04T17:15:39.633975+00:00'
evidence: 60_feedback/tasks/task_20260904_laowantong-qingdanti-scoring-rubric.md
---

# #640 清单体评分 rubric + skill v1.1（老顽童）

## 背景

老朱两步法定稿：第一步=接收→门禁验收（W6 三方法+暗知识全挖，用清单体枚举防漏）；第二步=清单体整理（结构层，锦上添花）。王语嫣实测背书：清单体改可达性不改增量。缺评分规则——原料在库：`00_inbox/一堂-AI清单体笔记（训练段位图）-truman-结构化.md`（L1-L6+六维）+ yt-note 卡族。

## 任务

1. **清单体评分 rubric**（落 `90_control/templates/` 或随 skill）：以段位图六维为骨架转成可打分表（每维 0-2 分锚点描述+总分档线），L4 清单笔记特征（重新整理/故事线/强逻辑）为合格线
2. **skill v1.1 升级**（`shared/transcript-to-qingdanti/`）：写入两步法定位（本 skill 管第二步结构层；第一步深挖走 W6 另轨）+ rubric 嵌入为交付前自检门禁（产出自评分数写进交付物头部）
3. 用 Live261 试跑件复评一次：按 rubric 打分，验证 rubric 可分辨好坏（自评+若分低修到达标再提）

## 交付

- rubric 文件 + skill v1.1 diff + Live261 复评分数实证 + 执行报告
- claim/complete 走 queue_transition（complete 640）

## 建模方案（L1 出牌）

`[素材牌] 段位图结构化件+yt-note 卡族（yt-note-five-levels-training / yt-note-l4-internalization）→ [边界牌] 两步法定位：skill 只管第二步结构层 → [结构牌] 六维 0-2 分锚点表 + 总分档线 → [过程牌] Step 5 自检门禁（打分→写入头部→低分修复循环）→ [质量牌] Live261 复评实证 + 单项否决红线（D4/D2=0 一票否决）`

理由：素材牌=段位图六维是指定原料；边界牌=老朱两步法定稿划清 skill 与深挖管线边界；结构牌=L11 清单类交付物三问（每维锚点可独立复跑证伪）；过程牌=嵌入门禁防"评了不用"；质量牌=L5 先实证再声称完成。

## 执行报告（2026-09-05 老顽童）

**交付物**：
1. `40_outputs/capabilities/skills/shared/transcript-to-qingdanti/rubric.md`（新建，清单体评分 rubric v1.0：六维 0-2 分锚点 + 档线 + 打分纪律 + 可分辨性基准）
2. `40_outputs/capabilities/skills/shared/transcript-to-qingdanti/SKILL.md`（v1.0.0→v1.1.0：新增「两步法定位」节 + Step 5 rubric 自检门禁 + 关联卡片补 2 条）
3. `40_outputs/capabilities/skills/shared/transcript-to-qingdanti/manifest.yaml`（version 1.1.0 + changelog）
4. `40_outputs/content/live261-zhanshududing-qingdanti-note.md`（头部写入 rubric 自评分数）

**完成内容**：
- rubric 以段位图六维（笔记数/完整度/舒适度/内化率/思考量/完成度）为骨架，每维 0-2 分锚点描述，满分 12；档线 11-12 优秀 / 9-10 合格（必要条件 D4/D5/D6 各≥1，即 L4 重新整理/故事线/强逻辑三特征）/ 6-8 待修 / ≤5 返工；D4=0 或 D2=0 单项否决
- skill v1.1 写入两步法定位（本 skill 管第二步清单体整理/结构层；第一步深挖验收走 W6 另轨，附王语嫣"改可达性不改增量"背书）+ rubric 嵌入为 Step 5 交付前自检门禁（分数写交付物头部、低分循环修复）
- Live261 试跑件复评：11/12 优秀（D1足量2/D2完整2/D3舒适1/D4内化2/D5思考2/D6完成2），≥9 合格线通过，无需修复即达标

**验证**：
- 复评 D2 完整度对账抽查：transcript 全文 grep 11 个关键数据点（1亿/2000万/1015学分/月入5万/星哥讲增长/杨医生/家庭医生/80%/50%/60%/行为经济学）11/11 命中
- rubric 可分辨性实证：Live261 的 D3 扣分项精确定位到「磨课小例子单行塞 15 例」；基准表反模式锚定（逐字稿直交 ≤4 分触发否决 / 只删语气词不重排 5-7 分）
- pre-submit 输出贴在任务单末尾
- 队列流转：claim → complete 均走 queue_transition.py，complete 后 status + 任务单双验证

**边界**：
- 只做任务单三件事（rubric + skill v1.1 + Live261 复评）；未改 Live261 正文（11 分已达标，任务单约定"分低才修"）
- rubric 落 skill 目录而非 90_control/templates/（任务单允许二选一；随 skill 便于 Step 5 同目录引用）
- 第一步深挖管线（W6）不在本单范围，仅在 skill 中定位声明

**需要谁动作**：
- 欧阳锋：终审本单（重点：rubric 锚点是否可机械复跑、两步法定位是否与设计定稿一致）
- 无其他角色依赖

## pre-submit 输出（2026-09-05）

```
kdo pre-submit -f 40_outputs/capabilities/skills/shared/transcript-to-qingdanti/SKILL.md
  Files checked: 1 | Passed: 1 | Failed: 0
  [YAML] 0 / [WIKILINK] 0 / [DOMAIN] 0 / [DK_SECTION] 0 / [OUTLINK] 0 / [ALIASES] 0
  [POSITION_DECLARATION] 0 / [SOURCE_REACHABILITY] 0 / [BODY_SRC_UNKNOWN] 0
  [VLM_TWO_SECTION] 0 / [CONCEPT_CROSSCHECK] 0 / [QINGDANTI_STRUCTURE] 0 / [QUOTE_VERBATIM] 0 / [SOURCE_RANGE] 0
  [QUALITY_SCORE] info: 40/100 | tacit:15 (4 signals)
  ✅ Result: PASS

kdo pre-submit -f 40_outputs/capabilities/skills/shared/transcript-to-qingdanti/rubric.md
  Files checked: 1 | Passed: 1 | Failed: 0
  同上 14 项检查 0 issue；[QUALITY_SCORE] info: 40/100 | src:15 (1)
  ✅ Result: PASS
```

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 4 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
