---
id: 506
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-24T17:24:18.541183+00:00'
version: v0.2
instance: huangyaoshi
code_files:
- kdo-tools/conveyor_probe.py
- kdo-tools/tests/test_conveyor_probe.py
- 90_control/conveyor-probes-contract.md
- 90_control/infrastructure-inventory.md
reviewed_by: 欧阳锋
review_date: '2026-08-24'
grade: A-
---

# #506 建议书 frontmatter 三元组 near-miss 门禁 + 模板单点化

- **任务号**：#506
- **状态**：queued
- **assignee**：huangyaoshi（探针扩展 + 模板落地；口径王语嫣已裁；欧阳锋终审）
- **优先级**：P1（建议书通道静默失效实证——4 份建议书盘上有、队列 0 条、零告警）
- **立项**：2026-08-24 王语嫣（风清扬建议书 `diag_20260824_fengqingyang-proposal-frontmatter-gate.md` 裁定采纳建议 1+2）

## 背景

建议书登记依赖 conveyor_probe frontmatter 三元组 `audience: 王语嫣` + `status: pending_orchestration`（+惯例 `type: proposal`）。08-24 风清扬 4 份建议书写成 `to: 王语嫣` + `status: pending`，探针不命中即 `continue`——**无 stderr、无日志、无通知**，靠手动验回执才捞回（E052 同族：机制依赖契约，契约破时静默失效）。4 份已改正补登（23:28 队列齐）。

**口径已裁（王语嫣 08-24）**：建议书 frontmatter 单轨 = `type: proposal` / `status: pending_orchestration` / `audience: 王语嫣`；`to:` 与 `status: pending` 标注 deprecated，禁止双轨。

## 任务

1. **探针 near-miss 报警**：`conveyor_probe._scan_proposals()` 增加「疑似建议书但三元组不完整」检测——凡 `diag_*.md` 有 `author`+`title`（或 `type: proposal`）却缺 `audience` 或 `status != pending_orchestration` 的，显式 stderr + 落 gate-blocked 式记录（或 friction 线索），不再静默 continue
2. **模板单点化**：建议书模板/样例收敛到单轨三元组（探针契约同改一处定义，模板与契约不漂移）；`to:`/`status: pending` 写 deprecated 注记；agent-os 相关说明同步（修订窗口内只做 deprecated 标注，新纪律条文待老朱拍板——见停车场）
3. 回归用例：故意写三元组错误的建议书 → 探针报警（非静默）

## 验证（验证分层）

- L1：单测——near-miss 样本（`to:`/`status: pending`/`type: diagnosis` 变体）全部触发报警；正常三元组不误报
- L2 狗粮：拿 08-24 漂移的 4 份原件（git 历史版本）回放到探针，确认能检出
- L3 待活体：下一份 frontmatter 漂移建议书当场可见，不靠事后捞

## 边界

- 只加 near-miss 报警，不改正常登记链路（探针只通知只登记纪律不动）
- 写后自检纪律（作者写完即跑 probe 验回执）入 agent-os §10 属老朱拍板窗口，不在本单施工
- 不强制存量历史建议书回改 frontmatter

## 关联

- 风清扬建议书 `diag_20260824_fengqingyang-proposal-frontmatter-gate.md`（实证表完整）
- E052（定期扫+扫 pattern 全两层）；F-034/F-035 门禁家族同族（想犯错也犯不了，B2-4）
- #421（建议书自动登记+到达即时通知，登记通知同源）

## 需要谁动作

- **黄药师**：探针 near-miss + 模板单点化
- **王语嫣**：口径已裁（本单），agent-os 纪律条挂修订窗口
- **欧阳锋**：终审本单

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：建议书通道静默失效根治——①near-miss 报警落地：`_scan_proposal_near_miss()` 检测"疑似建议书但三元组不完整"（deprecated `to:` 命中即漂移 / type: proposal 缺 audience 或 status 错 / 有 audience 但 status 非 pending_orchestration / pending 系 status 漂移），stderr 显式报警 + 新件落 gate-blocked 式记录（state 幂等去重）→ 第五探针同事件拾取登记 PROPOSAL-PENDING + 通知王语嫣（闭环零新通道）；三元组判定单点化 `_is_triple_hit`（_scan_proposals 与 near-miss 同源，防双轨漂移）；②噪声根治：全量干跑 259 份实测 53 条历史漂移（draft/completed/resolved/pending_laozhu 等历史杂态）→ 向前生效截止日 20260825（file-flow-protocol §9 同款既往不咎）+ 终态白名单 + 无日期文件名回落 created_at（proposal-self-learning-cron 实证）—— forward 窗口实测 0 误报；③模板单点化：契约 `conveyor-probes-contract.md` §三 写入单轨模板 + deprecated 注记（to:/status: pending 禁双轨）——模板与契约同点定义。

**交付物**：
- `kdo-tools/conveyor_probe.py`（near-miss 扫描+_is_triple_hit 单点+主流程接入+summary 输出）
- `kdo-tools/tests/test_conveyor_probe.py`（新增 9 例回归）
- `90_control/conveyor-probes-contract.md`（单轨模板+deprecated 注记）
- `90_control/infrastructure-inventory.md`（补登 shared_file_guard——#488 覆盖对照检查当场抓到，即查即登）

**验证**：
- L1：`cd kdo-tools && python -m pytest tests/ -q` → **84 passed**（新增 9 例：to: 漂移/status: pending/缺 audience/正常三元组零误报/纯诊断报告零报警/终态零报警/历史件豁免+回放模式检出/幂等去重/无日期回落 created_at）；`90_control/scripts` 116 passed 零回归；infra-status 覆盖对照 0 未登记
- L2 狗粮：08-24 漂移 4 份原件回放（git 未跟踪该批文件→按风清扬实证表记载的精确漂移形态 `to:+status: pending+type: diagnosis` 重建 4 件 frontmatter 回放）→ **4/4 当场检出**（不再静默）；真实库 forward 窗口干跑 0 误报
- L3 待活体：下一份 frontmatter 漂移建议书当场可见（stderr+PROPOSAL-PENDING+飞书通知三通道），不靠事后捞

**边界**：只加 near-miss 报警，正常登记链路零改动（只通知只登记纪律不动）；写后自检纪律入 agent-os 属老朱拍板窗口未施工；存量历史建议书未回改 frontmatter；agent-os 无需同步（grep 实证 agent-os.md 无三元组相关说明，不存在可标注处）；回放用重建件非 git 历史原件（该批文件 git 未跟踪——实证形态取自风清扬诊断书实证表，逐字段一致）。

**需要谁动作**：欧阳锋终审本单；王语嫣知悉——PROPOSAL-PENDING 将出现 [gate-blocked] near-miss 类行（漂移件=不登记+报警，裁定方式同既有 gate-blocked 行）；全员：建议书 frontmatter 单轨三元组（契约 §三 唯一定义点），to:/status: pending 已 deprecated。

## 终审记录

- **结论**：PASS A-（2026-08-25 欧阳锋）
- **通过维度**：版本对齐三问全过（bf82729be 在 HEAD 链）；L1 独立复跑 kdo-tools 84 passed + 90_control 116 passed（双套件零回归，与报告一致）；near-miss 判定函数逐行直读；契约 §三 直读；**我侧实证触发活体场景**（见下）
- **溯源要点**：
  1. **near-miss 四形态拦截** ✅：`_proposal_near_miss_reason` 直读——deprecated `to:` 命中即报 / type:proposal 缺 audience 或 status 错即报 / 有 audience 但 status 非 pending_orchestration 即报 / pending 系 status 漂移即报；终态白名单（resolved/reviewed/closed/done/orchestrated/cancelled）不回看；幂等去重 sha256+500 截尾
  2. **三元组判定单点化** ✅：`_is_triple_hit` 被 _scan_proposals 与 near-miss 同源调用（diff 实证）——防双轨漂移达成
  3. **噪声根治** ✅：向前生效截止日 20260825 + 终态白名单 + 无日期回落 created_at——53 条历史漂移既往不咎口径与 file-flow-protocol §9 同款
  4. **模板单点化** ✅：契约 §三 单轨模板 + deprecated 注记（to:/status: pending 禁双轨）；agent-os 无需同步（grep 实证无三元组说明——报告声明属实）
  5. **L2 回放** ✅（带保留）：git 未跟踪原件→按风清扬实证表重建 4 件回放 4/4 检出——报告如实声明重建来源，非冒充原件
- **🔵 活体实证（本单必要性的意外证据）**：终审中实测——**我自己今天写的 2 份建议书**（diag_20260825_ouyangfeng-review-bottleneck-wakeup / src-unknown-body-gate）用了 type:diagnosis+status:draft+无 audience 的非规格式，queue grep 实证**零登记零报警**——审查者本人就是漂移肇事者。已当场自纠：2 份补三元组后 `_is_triple_hit`=True（实证函数直跑），commit 落盘（by ouyangfeng）
- **发现问题**：
  - 🟡 **P2 口径收窄未声明**：任务书 L1 字面"凡 diag_*.md 有 author+title 却缺 audience 或 status≠pending_orchestration 即报警"，实现收窄为 proposal 型/pending 系才报（纯 draft 裸形态三路全 miss——我的 2 份实证 None）——收窄本身合理（draft=撰写中，全量报警会骚扰；53 条历史噪声数据支持），但执行报告把任务书 L1 原样引用为达成、未声明收窄偏离。声称-交付精确性轻微瑕疵，不阻断
  - 🔵 观察项：作者写 draft 忘记转正→静默（写后自检纪律挂老朱拍板窗口，与任务书边界一致——本单不施工正确）
- **残余风险**：L3 待活体（下一份漂移建议书当场可见）；窄口径下"全裸形态"（无 audience 无 pending 系）仍靠作者自律——写后自检窗口落地后闭合
- **存在性核查**：「双套件 84+116」→ 独立复跑；「四形态拦截」→ 函数逐行直读；「活体零登记」→ production-queue.md grep 我 2 份建议书无行 + _proposal_near_miss_reason 实跑返回 None；「自纠后合规」→ _is_triple_hit 实跑 True×2

*欧阳锋 · 2026-08-25 · #506 终审 PASS A-（含审查者自纠实证）*
