---
id: 579
assignee: laowantong
status: reviewed
updated_at: '2026-08-30T06:34:12.785569+00:00'
version: v0.1
instance: laowantong
reviewed_by: 欧阳锋
review_date: '2026-08-30'
grade: A-
---

# #579 战略笃定框架卡

- **任务号**：#579 ｜ **状态**：queued ｜ **assignee**：老顽童（欧阳锋终审）｜ **优先级**：P2
- **立项**：2026-08-30 王语嫣编排（诊断 `diag_20260830_战略笃定篇`，老朱拍板）

## 背景

这堂课的主线是"战略笃定"——战略（重大选择）+ 笃定（长期稳定）。知识库有 strategy 域存量（strategy-brm/诊断/生命周期等），但"战略笃定"这个概念本身无专门卡（散落 IPO 卡）。

## 任务

产出 `framework-战略笃定` 框架卡：

1. **定义**：战略=重大选择（做什么不做什么/靠什么赢舍什么/内核边界）；笃定=长期稳定（心态笃定/长期稳定/不断积累）
2. **七轮决策表**（决策题→调用框架→结论）
3. **攒牌心态/借假修真/5-10 年尺度**：用十年尺度的不变因素完成今天的决策
4. **"不要撒胡椒面"**：战略上不做五五开，敢于选、敢于押错
5. 与 strategy 域已有卡（strategy-brm/diagnose/lifecycle）桥接

## 素材锚点

- 逐字稿 + 口述稿全文（七轮决策完整推导）
- 已有卡：`framework-strategy-brm`（战略框架）、`concept-yitang-research-10-assumptions`（先博后渊）、`yt-model-ipo-learning-strategy`（IPO 学习策略含"战略笃定"提及）

## 验证

- 框架卡含七轮决策完整表 + 战略笃定定义 + 攒牌心态
- 与 strategy 域已有卡桥接不重复（本卡=Truman 战略笃定的七轮决策实证，非通用战略理论）

## 边界

- 不重写 strategy 域通用框架，只做"战略笃定"这个特定概念 + 七轮决策实证
- 传播限制：Truman 明确"不要外传、阅后即焚"，老朱是学员学习无碍，但卡上标注 source_person=Truman + 传播限制注记

## 建模方案（老顽童出牌，2026-08-30）

出牌链：`[素材牌#3 先口述稿再笔记] → [边界牌#6 先查已有卡再新建] → [边界牌#7 先对标准则再命名] → [结构牌#8 先定总纲再子卡] → [结构牌#10 先骨架再填肉] → [质量牌#16 先lint再pre-submit] → [质量牌#15 先自攻击再提交]`

- 素材牌#3：口述稿 1870 行全文已逐字读完（含末尾闲聊 L1536-1870），七轮决策完整推导已提取
- 边界牌#6：strategy 域已有 `framework-strategy-brm`/`tool-strategy-nine-problems`（diagnose）/`framework-strategy-six-stages`（lifecycle）/`concept-yitang-research-10-assumptions`/`yt-model-ipo-learning-strategy`——本卡只做"战略笃定"特定概念 + 七轮决策实证，不重写通用战略理论
- 边界牌#7："战略笃定"一词源于《论持久战》官方拆书题（口述 L74），非国际通行术语冲突
- 结构牌#8：本卡属于 strategy 域 Truman 战略笃定实证卡（定位声明 O8）
- 结构牌#10：framework 四节完整性——When NOT to Use / 失败模式 / Action Triggers / Critique
- 质量牌#16/#15：kdo pre-submit 门禁 + 四路自攻击
- 传播限制：Truman 明确"不要外传、阅后即焚"（口述 L48-50），卡上标注 source_person=Truman + 传播限制注记

## 需要谁动作

- **老顽童**：生产 `framework-战略笃定`
- **欧阳锋**：终审

## 执行报告

**交付物**：
- `30_wiki/frameworks/framework-strategy-conviction.md`（新建 framework 卡，战略笃定框架卡）
- `60_feedback/adversarial/atk_framework-strategy-conviction_20260830.md`（自攻击报告）

**完成内容**：战略笃定框架卡——战略定义（重大选择：做什么不做什么/靠什么赢舍什么/内核边界）+ 笃定定义（心态笃定/长期稳定/不断积累）+ 七轮决策表（决策题→调用框架→结论→选错后果，含 Truman 一年 7 次重大选择实证）+ 攒牌心态/借假修真/5-10 年尺度 + 不要撒胡椒面 + strategy 域桥接表（BRM/diagnose/lifecycle 全覆盖）+ When NOT to Use×5 + 失败模式×7 + Action Triggers×6 + Critique（内部局限×3 + 外部攻击者×3）。已标注 source_person=Truman + 传播限制注记（Truman 阅后即焚，仅供老朱学员学习）。

**验证**：`kdo pre-submit -f 30_wiki/frameworks/framework-strategy-conviction.md` → ✅ PASS 1/1（WARNING×1：CONCEPT_CROSSCHECK 提示制不拦截，人工核对一致）；`kdo index --incremental` → +1（4286 总数）；自攻击四路 0🔴 0🟡 4🟢。

**边界**：七轮决策为 Truman 事后复盘（有幸存者偏差风险，Critique 已注明）；"5-10 年尺度"无客观判断标准依赖判断力；样本为研究型公司 CEO 单人决策（Truman 注明"特指我们一堂"）；传播限制——本卡内容来自内部课，不得外传。

**需要谁动作**：欧阳锋终审 #579。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 2 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

## 终审记录

**审查结论：PASS A-**

- 七轮决策表 / 战略·笃定定义 / 攒牌心态 / 不要撒胡椒面 锚点全部命中（L62-66/L68-70/L74-76/L1442-1448/L1496-1502）。
- 传播限制注记合规（source_person=Truman + 阅后即焚），strategy 域桥接表完整不重复。
- 🟡 一处 ±1 行偏差：Critique 引「目前看决策质量还不错，L1449」，实际 L1449 为空行，原文在 L1450「目前看这些决策，目前看质量还不错」→ TODO：老顽童下次顺手修正 L1449→L1450（不阻断，观察项）。
- 写审分离：author=老顽童，reviewed_by=待审，合规。

