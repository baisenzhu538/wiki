---
id: 461
assignee: huangyaoshi
status: queued
updated_at: '2026-08-23T07:30:00+00:00'
version: v0.1
---
# #461 queue_transition cancel 命令（queued 单取消/被取代状态）

- **任务号**：#461
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P1（老朱 2026-08-23 拍板立项；#460 场景暴露：queued 单被取代后只能挂账冻结，探针仍通知可领取）
- **立项**：2026-08-23 王语嫣（老朱指令「立项 cancel 命令，另下任务编排书」）

## 设计

1. **命令**：`python queue_transition.py cancel <task-id> --instance <name> --reason '<取消理由>'`
   - `--reason` **必填**（与 #444 force 台账同款留痕精神：谁/为何取消）
   - 取消记录追加到 `90_control/force-exceptions.log` 同款台账或独立 `cancel-ledger.log`（时间/任务/instance/理由）
2. **状态**：`cancelled` 新终态——**不是删除**：队列行保留原内容不动，状态列改 `cancelled`（状态列归脚本=上板冻结唯一例外既有口径），任务单 frontmatter `status: cancelled`
3. **适用范围**：仅 queued 状态可 cancel；claimed/pending_review 需先 release/review 退回；reviewed 不可取消（已闭环）
4. **下游适配**：
   - `parse_queue`/`can_claim`：cancelled 不可领取（报「已取消」非「不存在」）
   - 探针：cancelled 不触发可领取通知（new_queued 扫描排除）
   - dashboard：cancelled 不计待领/活跃；统计口径与 reviewed 同类（终态），可领/审查数字不受污染
   - 归档：与 reviewed 同规则（14 天后瘦身归档，#453）
5. **首批执行**：实施验收后王语嫣立即 cancel **#458/#459**（reason=被 #460 取代）——挂账问题当场清账

## 验证（验证分层声明）

- L1：单测（queued 可 cancel/claimed 拒/cancel 后 claim 拒/统计正确/reason 必填）
- L2 狗粮：cancel 一个测试单 → status 数字正确 + 探针不再通知 + dashboard 正确
- L3 待活体：cancel #458/#459 后探针运行零误通知

## 边界

- 只加取消状态机，不改既有状态流转（claim/complete/review/release 零改动）
- cancelled 单的任务单文件保留原样（冻结留档），不删除不归档移动
- 取消后反悔=不可逆（重新做=新单）——与「修订走新任务书」纪律一致

## 关联

- #460（取代场景暴露者）；#444（reason 必填+台账先例）；#453（归档规则）；charter §3.15（上板冻结与取消的边界：内容冻结+状态机出口）

## 执行报告（F-034 五字段+验证分层声明，complete 前必填）

（生产者填写）
