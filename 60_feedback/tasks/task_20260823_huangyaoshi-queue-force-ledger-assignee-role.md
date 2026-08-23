---
id: 444
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-23T04:28:32.213484+00:00'
instance: huangyaoshi
reviewed_by: 欧阳锋
review_date: '2026-08-23'
grade: A-
---
# #444 queue_transition 交接语义加固：--force/--evidence 例外台账 + frontmatter assignee 角色名口径

- **任务号**：#444
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P1（#441 complete 实证 F-034 被 --force 绕过——门禁后门；老朱「想犯错也犯不了」机制偏好）
- **立项**：2026-08-23 王语嫣（风清扬建议书 1+3 裁定采纳合并，见 `diag_20260823_wangyuyan-441-rework-ruling.md` §二）

## 任务目标

堵住 F-034 交付五字段门禁的两条绕过路径，并统一任务单 frontmatter 的 assignee 口径（角色名），消除实例名污染文档署名。

## 缺陷定位（已核实）

1. **--force 后门**：`queue_transition.py` L533 `--force 可跳过，语义=已声明例外`——但例外无任何留痕要求，#441 无执行报告 force 过关（2026-08-23 10:48 complete by hermes，绕过路径穷举证明见裁定文书 §一 P1-2）。「声明例外」正被当常规通道用。
2. **--evidence 侧门**：五字段检查对 evidence 文件做锚点匹配——evidence 指向任务单外任意含锚点词的文件即可过关，五字段没落在任务单交接文档上（同次穷举验证发现）。
3. **assignee 口径**：frontmatter `assignee` 被流转脚本写入执行实例名（#441=hermes），正文是角色名（laowantong）——文档署名双口径（E020/E045 同病）。

## 范围

1. **例外台账（--force）**：force 时强制留痕——谁（instance）/何时/绕过哪条门禁/理由（`--reason` 必填）/事后何时补；台账落 `90_control/force-exceptions.log` 或任务单追加节，终审可见。无理由的 force 拒绝执行。
2. **evidence 留档（--evidence）**：evidence 文件路径必须写进任务单（执行报告节或 frontmatter 字段），git 可溯；evidence 不再作为五字段锚点的替代检查面——五字段必须最终落在任务单上（evidence 只是佐证附件）。
3. **assignee 口径**：新任务单 frontmatter `assignee` 只写角色名（laowantong/huangyaoshi/wangyuyan/fengqingyang/ouyangfeng）；实际执行实例另存字段（如 `instance: hermes`）；**存量兼容**——读到实例名照常流转不报错，存量不回改（历史既往不咎）。
4. **测试**：+force 无理由拒绝 / force 带理由入台账 / evidence 路径留档 / 新口径写入+存量实例名兼容 四组用例。

## 验证

- 正测：无执行报告 complete → FAIL；--force 无 --reason → FAIL；--force --reason → 过且台账有记录。
- 反测：五字段齐全 → 无需 force 直接过；存量 frontmatter（hermes）claim/complete 不受影响。
- 回归：`pytest 90_control/scripts/tests/test_queue_transition.py` 全过 + 新增。

## 边界

- 只动 queue_transition.py（+台账文件），不碰 #421 探针（路由归 #443）、不碰 #442 词表。
- 探针/conveyor 侧对新字段的适配（如未来读 assignee 路由）不在本单——#443 映射表已按「角色名+实例名都能认」设计。
- 交付五字段（F-034）+ 审查意见落盘（F-035）+ commit 入档。

## 关联

- 裁定：`diag_20260823_wangyuyan-441-rework-ruling.md` §二（建议 1+3 合并）
- 建议书：`diag_20260823_fengqingyang-441-review-and-proposal.md`
- 实证：#441 complete by hermes（71527b483）无执行报告过关
- 同族：F-034（#429 交付五字段）/ E020（实例/角色双口径）/ E045（编号三层）
---

## 追加说明（2026-08-23 王语嫣，黄药师验证分层建议书裁定并入）

- **执行报告「验证分层」字段**（F-034 演进同族）：五字段外增第六字段——验证分层四态声明（L1 单测 / L2 狗粮 / L3 活体 / 待活体）。**缺声明=审查时可追问，不硬拦**（只拦机械项原则）。禁止把「待活体」写成「已验证」。
- 底本：`60_feedback/diagnosis/diag_20260823_huangyaoshi-verification-tier-insight.md`（「跑了≠真了/模拟≠真实/文档类无狗粮」三条铁律；另两条铁律入黄药师 spec，F-028 场素材）。
- 测试相应 +1：执行报告含「待活体」声明 → 门禁放行但审查端可见。

---

## 执行报告（2026-08-23 王语嫣——老朱直令改派领取，claim --force 并行通道）

**完成内容**：queue_transition 交接语义加固——--force 例外台账（reason 必填）+ evidence 侧门封堵与留档 + frontmatter assignee 角色名口径，#441 后门根治。

**交付物**（改动文件清单）：
1. `90_control/scripts/queue_transition.py`：
   - `_check_delivery_fields` 重构：evidence 不再替代五字段检查面（检查面恒为任务单「## 执行报告」节；evidence 仅验证可读性=佐证附件）——#441 实证侧门封死
   - `_log_force_exception` + `FORCE_LEDGER`（`90_control/force-exceptions.log`）：force 例外留痕（时间/task/instance/绕过门禁/reason）
   - `action_complete`：force 无 `--reason` 直接拒绝；force 带理由过且台账可见；evidence 路径留档任务单 frontmatter
   - `INSTANCE_ROLE_MAP` + `_role_of`：claim 时 frontmatter `assignee`=角色名（hermes/kimi→laowantong），实际执行实例另存 `instance` 字段；存量实例名不回改（读侧兼容）
   - main() 参数解析 + `--reason`；usage 文档同步
2. `90_control/scripts/tests/test_queue_transition.py`：+6 用例（TestForceLedgerAndEvidenceGate）

**验证**：
- `pytest 90_control/scripts/tests/test_queue_transition.py` → **36 passed**（30 原有 + 6 新增）
- 正测：执行报告五字段齐全 complete 路径门禁 PASS；force+reason 过且台账落行
- 反测：force 无 reason → 拒绝（真实队列 #444 无副作用实测）；evidence 指向含全部锚点的外部文件+任务单无执行报告 → 仍 FAIL（侧门封死实证）
- 口径：_role_of 五实例映射断言全过；Windows mkstemp 句柄坑修复（E002 同族，os.close 后 unlink）

**验证分层**：L1 单测 36 passed ✅ / L2 狗粮=本单自身 complete 走新门禁（五字段真实验证）✅ / L3 待活体：下一单真实使用 --force --reason 与 hermes 实例 claim 后 frontmatter 双字段写入，欧阳锋复审时抽验

**边界**：claim --force（并行通道）未加 reason 要求——语义不同（跨 assignee 并行是设计用途），如需统一另立演进单；不动 #421 探针（归 #443）；不回改存量任务单 assignee。

**需要谁动作**：欧阳锋终审本单（抽验侧门封堵与 force 拒绝路径）；黄药师知悉口径变更（下次 claim 起 frontmatter 为 assignee+instance 双字段）。

---

## 终审记录（欧阳锋 · 2026-08-23 · FAIL 退回）

**结论：退回（FAIL）→ queued**——功能核心验证通过，验收项「回归全过」未达成（1 failed），测试脆弱性需修，复审只验测试

**P0/P1/P2 清单**：
- P1：`test_force_complete_without_reason_rejected` 用**真实队列 #444** 当测试对象（编写时 claimed-wangyuyan，现已 pending_review）——状态漂移导致断言失败（msg 是状态错误而非 --reason 提示）——**测试设计脆弱**：应隔离环境（KDO_QUEUE_PATH 隔离，同 #429 狗粮）或 mock
- P2：验收项「回归 pytest 全过」未达成（实测 1 failed, 35 passed——报告"36 passed"写于 #444 提审前状态，时间相关失效非故意造假）；force-exceptions.log 惰性创建正常

**字段级定位**：`90_control/scripts/tests/test_queue_transition.py` TestForceLedgerAndEvidenceGate::test_force_complete_without_reason_rejected（L420-427）——`qt.action_complete("task_20260823_huangyaoshi-queue-force-ledger-assignee-role", "wangyuyan", ...)` 直接操作真实队列任务

**证据**：
- 独立复现：`pytest test_queue_transition.py` → **1 failed, 35 passed**（失败断言 `'--reason' not found in '任务 … 状态为 pending_review，不是由 wangyuyan 领取的 claimed-wangyuyan'`）
- 功能核心独立验证全过：① force 无 reason → 拒绝（ok=False ✅ #441 后门根治行为成立）② evidence 指向含全锚点外部文件 + 任务单无执行报告 → 仍 FAIL（侧门封死 ✅）③ `_role_of` 八实例映射全对（hermes/kimi→laowantong，其余各自 ✅）

**期望形态**：测试改为隔离环境——monkeypatch KDO_QUEUE_PATH/KDO_TASK_DIR 指向 tmp 队列（#429 狗粮同款），构造 claimed-wangyuyan 状态任务再断言 force 无 reason 拒绝且 msg 含 --reason；或 mock find_task。修复后复审只验本测试 + 全量回归。

**说明**：本单功能交付质量高（侧门封堵/台账/角色口径三件全过），退回仅为不留红测试——复审一轮可闭环。

**存在性核查**（本意见书负向断言证据）：
- 「1 failed」→ 核查：pytest 独立复现输出 `1 failed, 35 passed`（失败断言原文附上）
- 「侧门封堵」→ 核查：构造 fake-evidence（含全锚点）+ 无执行报告任务单 → `_check_delivery_fields` 返回 FAIL（输出："任务单缺少执行报告节"）
- 「_role_of 映射」→ 核查：八实例逐一调用实测输出全对
- 「报告 36 passed 系时间相关」→ 核查：失败测试用真实队列 #444（状态 claimed→pending_review 漂移），编写时通过提审后必挂

*欧阳锋 · 2026-08-23 · FAIL 退回*

### FAIL 退回修复记录（2026-08-23 黄药师 · 欧阳锋复审只验本测试 + 全量回归）

**退回原因**：`test_force_complete_without_reason_rejected` 用真实队列 #444 当测试对象——状态漂移（claimed→pending_review）导致断言失败（msg 是状态错误而非 --reason 提示）。

**修复**：monkeypatch 函数级隔离（不碰真实队列）——
- `qt.parse_queue` → 构造 claimed-wangyuyan 状态 fake rows
- `qt.find_task` / `qt._find_task_file_dual` → 临时任务单
- 断言：force + reason=None → 拒绝且 msg 含 --reason ✅
- （首版尝试改 qt.QUEUE_PATH 隔离失败——parse_queue 默认参数在 queue_gate 模块定义时绑定，改属性不生效；函数级 monkeypatch 是正解，已记 friction）

**验证分层**：L1 单测 **36 passed**（30 原有 + 6 新增，脆弱用例修复后全绿）/ L2 本单复审 complete 走新门禁 / L3 待活体：下一单真实 --force --reason 与 hermes 实例 claim 双字段写入，欧阳锋复审抽验

**回归**：`pytest test_queue_transition.py` → 36 passed（修复前 1 failed）

---

## 终审记录（欧阳锋 · 2026-08-23 · 复审轮）

**结论：PASS / A-**

**复审对照法**：只验上次 FAIL 清单（测试脆弱性 1 项）。

**FAIL 项验证** ✅：`test_force_complete_without_reason_rejected` 已改函数级隔离（commit 38d155a80 12:26）——monkeypatch `parse_queue/find_task/_find_task_file_dual` 构造 claimed 状态 fake_rows + 临时任务单，**不碰真实队列**（注释明确"状态漂移断言脆弱根治"）；全量回归独立复现 **36 passed**（此前 1 failed 消除）

**其余不重复审**（首轮功能核心已验证：force 无 reason 拒绝/evidence 侧门封死/_role_of 八实例映射全过）

**结论**：FAIL 一项闭环，复审一轮达成。

**存在性核查**：- 「隔离化修复」→ 核查：sed 读测试源码——TemporaryDirectory + monkeypatch 三函数，无真实队列引用
- 「36 passed」→ 核查：pytest 全量独立复现输出 `36 passed in 0.89s`
- 「commit 入档」→ 核查：git log 38d155a80（12:26 test(gates) FAIL 退回修复）

*欧阳锋 · 2026-08-23 · 复审 PASS A-*
