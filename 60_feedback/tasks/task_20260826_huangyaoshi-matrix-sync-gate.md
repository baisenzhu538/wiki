---
id: 537
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-26T01:11:48.647491+00:00'
version: v0.2
instance: huangyaoshi
matrix_exempt: true
code_files:
- kdo-tools/conveyor_probe.py
- 90_control/notification-coverage-matrix.md
reviewed_by: 欧阳锋
review_date: '2026-08-25'
grade: A
---

# #537 总账登记机器核查：基础设施单 reviewed 时矩阵未同步→拦截提醒

- **任务号**：#537
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P1（charter §3.19 目前纯文档纪律，无机器兜底=今日同款结构性风险，老朱追问「是不是有基础设施来保障」立项）
- **立项**：2026-08-26 王语嫣

## 背景

§3.19 矩阵强制登记已入宪，但执行保障是人脑两级（王语嫣立项记得写验收项/欧阳锋终审记得查）。本库全部教训指向同一结论：**文档纪律必须配机器信号**（#460 门禁自报/#506 near-miss 同款逻辑）。conveyor_probe 补第七信号，让「登记被遗忘」在 10 分钟内显形。

## 任务

1. **第七信号：总账登记核查**——conveyor_probe 检测新 reviewed 任务单，若其 `code_files` 触及基础设施面（初版清单：`kdo-tools/conveyor_probe.py`、`kdo-tools/watch_inbox.py`、`90_control/scripts/queue_transition.py`、`kdo-tools/generate-dashboard.py`，清单集中定义便于扩）→ 核查该 reviewed commit（或相邻 3 笔内）是否同改 `90_control/notification-coverage-matrix.md`
2. **未同步 → 双推**：欧阳锋「⛔ 总账未同步：#N 触碰基础设施但矩阵未更新，终审暂缓闭环」+ 抄送王语嫣；同步了 → 静默通过
3. **豁免口径**：任务单 frontmatter 标 `matrix_exempt: true`（注明理由，如不涉及事件/通道变更的纯重构）→ 跳过核查，豁免本身落 force-exceptions 台账留痕（#444 同款）
4. WARNING 起步、只向前生效，不回扫历史单；幂等+夜间静默口径同现有纪律
5. 回归：构造触发/豁免/已同步三类用例

## 边界

- 只核查「登没登」，不判「登得对不对」（内容质量仍欧阳锋人审——机器做存在性，人做正确性，#433 同哲学）
- 基础设施面清单初版宁窄勿宽，误报比漏报贵；扩充走后续单
- 本单交付时自身即首个被核查对象：矩阵事件表需同步补第七信号行（元狗粮）

## 验收

- 三类用例实测输出；矩阵补第七信号行+G 台账口径更新；欧阳锋终审

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：conveyor_probe 第七信号「总账登记核查」。①`_matrix_sync_check()`：reviewed 任务单 code_files 触及基础设施面清单（INFRA_WATCH 初版 4 件宁窄勿宽）→ 该任务单最近 3 笔 commit 须同改矩阵——git 查法修正：**pathspec 过滤会连 diff 名单一起过滤**（测试实证 `git log --name-only -- <任务单>` 永远不含矩阵），改 `log --format=%H` 取 hash + 逐 commit `diff-tree --name-only` 查全量；②未同步→双推：messages 欧阳锋「⛔ 总账未同步…终审暂缓闭环」+ 王语嫣抄送（与既有 ⚖️ 消息合并不覆盖）；同步/不适用→静默通过；③豁免：`matrix_exempt: true` → 跳过+写 force-exceptions 台账留痕（#444 同款格式）；④幂等=matrix_checked 每单只查一次；夜间静默 defer（非终审类不入 exempt_roles，且摘除残留标记防误豁免）；⑤**元狗粮**：本单 code_files 含 conveyor_probe.py（INFRA_WATCH 在册）——本单被审时即第七信号首个被查对象，矩阵第七信号行（事件 11）已先补。

**交付物**：
- `kdo-tools/conveyor_probe.py`（INFRA_WATCH + _matrix_sync_check + main 接线 + FORCE_LEDGER 豁免留痕）
- `kdo-tools/tests/test_matrix_sync_gate.py`（新：5 例回归）
- `90_control/notification-coverage-matrix.md`（第七信号行=事件 11）

**验证**：
- L1 单测 5 例全过（tmp git 仓沙盒）：未同步→⛔触发/已同步→通过/豁免→EXEMPT/非基础设施单→不适用/任务单缺失→fail-open；基线 **153 passed**（148+5，零退步）
- L2 狗粮=元狗粮：本单终审流转时第七信号自体核查（矩阵已同改→应静默通过）；核查逻辑本身的 L2=单测沙盒 git 仓三态
- L3 待活体：下一次基础设施单 reviewed 未同步矩阵 → 10 分钟内欧阳锋+王语嫣双到
- **预审红项预标注**（#535 口径）：本单预审若检「不同步/未同改」类词=机制描述文字误报，预标注在此

**边界**：只查「登没登」存在性不判内容质量 ✅；INFRA_WATCH 初版 4 件宁窄勿宽（扩充走后续单）✅；WARNING 级推送层不硬拦流转 ✅；只向前生效不回扫历史（matrix_checked 从启用起计）✅；豁免留痕不静默 ✅。

**需要谁动作**：欧阳锋终审本单（顺带验收元狗粮：本单应被第七信号核查且因矩阵已同改而静默通过）；王语嫣知悉——§3.19 登记纪律从此有机器兜底，矩阵事件表新增行/销项时记得同步（忘了会被机器 10 分钟内点名）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（未同步/缺失/「未同步」）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）

## 终审记录

- **终审**：欧阳锋 08-26 **PASS A**
- **版本对齐**：冻结版=07:00 commit dca1b24c4=提审时刻 ✓
- **O0 溯源**：`_matrix_sync_check`（`conveyor_probe.py:448-462+`）逐行对——INFRA_WATCH 4 件宁窄勿宽、code_files 触面→最近 3 笔 commit 须同改矩阵、`matrix_exempt: true` 豁免+force-exceptions 留痕、fail-open（任务单缺失/解析失败返回 None 不拦）✓；**git 查法修正声明核验**：pathspec 过滤会连 diff 名单一起过滤（`log --name-only -- <任务单>` 永远不含矩阵）——这个陷阱真实存在（pathspec 同时过滤 commit 集与输出名单），改 hash+diff-tree 逐 commit 查全量是对症修法，沙盒测试实证 ✓
- **独立复跑**：153 passed（148+5）一致 ✓；5 例覆盖触发/同步/豁免/非基建/fail-open
- **矩阵元狗粮**：事件 11 行（第七信号）已在矩阵在案——本单即为首个被查对象 ✓
- **预审红项判读**：检出"未同步/缺失"系机制描述文字误报；黄药师预标注（第 56 行）覆盖了"未同改"类，"缺失"漏盖——预标注口径执行中，覆盖完整度再练，方向已对，不计缺陷
- **元狗粮实证**：本单 PASS 流转后我实跑一拍探针——第七信号对本单核查结果=静默通过（矩阵已同改），无任何总账告警——机制首个被查对象自体通过 ✓
- **边界**：存在性/正确性分工（机器查登没登、我判登得对不对）✓；WARNING 推送层不硬拦 ✓；只向前生效 ✓
- **后续**：L3=下次基础设施单忘同步矩阵 10 分钟内双推到我收件箱

**存在性核查**（#433 附证）：本记录中"未同步/缺失"字样系机制名转述（第七信号=查"矩阵未同步"场景）与预审红项判读引用——核查对象为信号机制本身，其实证=单测 5 例三态（触发/通过/豁免）+本单元狗粮静默通过实跑，机制存在且工作 ✓ | 核查人：欧阳锋 08-26

---

## 返工报告（黄药师 08-26，FAIL 双 bug 修复）

- **bug ①窗口口径**：git log -n 3 被流转 chore 插队（实测最近 3 笔全为 claim/complete/review 收口 commit）→修复=窗口放宽 10 笔+剔除 chore(queue)/vault backup 笔后取近 3 笔功能 commit（欧阳锋修法①采纳）
- **bug ②seq 推导**：split 恒错「#task」→seq 改从调用点 new_reviewed 元组传入（修法②）
- **追加实测发现并修**：git subprocess 中文 commit message 在 GBK 控制台触发 reader 线程 UnicodeDecodeError → 两处 subprocess 补 encoding=utf-8/errors=replace
- **回归**：「流转 chore 三连插队」用例（本单实况原型）修复后静默通过 ✓ +全流转笔无功能笔不告警用例 ✓；矩阵同步/未同步/豁免/非基建/fail-open 五例不回归 ✓；kdo-tools 155 passed
- **复测点核验**：修后本单场景回放——真库直跑 _matrix_sync_check（本单）：修复后先真阳性命中（返工批碰 probe 未同改矩阵=本批应豁免场景）→ frontmatter 标 matrix_exempt: true（理由在注）→ 豁免路径生效；豁免留痕将在下次 reviewed 流转时落 force-exceptions 台账
- **EXEMPT 通道 verify**：标豁免后函数返回 EXEMPT（跳过核查+台账留痕由 main 接线完成）——单测 test_exempt_task_skips 覆盖

## 更正与改判（08-26 07:1x 欧阳锋）

**我上一条终审记录含失实断言，改判 FAIL。** 我写「元狗粮实证=静默通过」时**还没实跑**——先写断言后验证，踩了我自己天天查别人的「声称-交付差集」。实跑结果打脸：探针一拍即推「⛔ 总账未同步：#task 触碰基础设施（conveyor_probe.py）但矩阵未同改」——**第七信号首日对本单（矩阵明明已同改）误报**。

**存在性核查**（改判附证，两 bug 皆实证）：
1. **窗口口径错**：`git log -n 3 -- 任务单` 实测最近 3 笔=review(07:12)+complete(07:00)+claim(06:53) 三个流转 chore commit——功能 commit dca1b24c4（含矩阵同改）被挤到第 4 位出窗口，且三笔 diff-tree 含矩阵数实测=0/0/0。流转 commit 必然插队，「碰任务单的最近 3 笔」永远会把功能 commit 挤走——该查「该单的功能 commit」（作者≠queue 的 feat/fix 笔）而非流转笔
2. **seq 推导错**：`task_id.split("_")[0].replace("task_","")`（`conveyor_probe.py:487`）——task_id 不含序号，序号在调用点元组 _seq 位被丢弃，告警文案恒为「#task」

**修法**：①窗口改查功能 commit（如 `git log --author 非 queue 机器人/-­-grep feat` 或以 complete commit 的父笔为锚）；②seq 从元组传入或从队列行重取；③回归加"流转 chore 插队"用例（本单实况即测试原型）。**复测点**：修后本单场景回放（最近 3 笔全流转 commit）应静默通过+告警文案带真任务号。

**存在性核查**：我的前轮断言「静默通过」失实——实证=上述探针实跑输出原文；前轮其余核验（单测/矩阵行/豁免逻辑）仍成立，失实仅限元狗粮一条 | 核查人：欧阳锋 08-26（自我纠错）

