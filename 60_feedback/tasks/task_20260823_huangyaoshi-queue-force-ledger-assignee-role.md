---
id: 444
assignee: wangyuyan
status: in_progress
updated_at: '2026-08-23T04:00:42.661156+00:00'
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
