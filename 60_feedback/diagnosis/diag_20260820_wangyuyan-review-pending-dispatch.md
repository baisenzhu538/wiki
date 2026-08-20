# 立项建议书：REVIEW-PENDING 待终审自动登记段

- 呈送：王语嫣（编排拍板）
- 作者：王语嫣（编排侧自查立项，#387 事件驱动）
- 日期：2026-08-20
- 建议执行：黄药师 ｜ 建议优先级：P2 ｜ 依赖：无

---

## 一、事件背景（证据链）

2026-08-20 #387 提审后欧阳锋"找不到任务"事件：

| 时间 | 事件 |
|:--|:--|
| 10:47 | 欧阳锋会话档案最后写入（#386 终审 PASS A，此后无活动） |
| 11:10:40 | #387 进 pending_review（queue_transition.py + 任务单 mtime 实锤） |
| 之后 | 老朱@欧阳锋审 #387，欧阳锋报"找不到" |

王语嫣排查结论（全链路实测）：队列行/状态脚本/任务单/交付卡/dashboard/双 wiki 路径**全部在位**——问题不在数据，在欧阳锋信了 10:47 之前的会话内旧快照（E034 家族：版本漂移，与 #383 王语嫣覆盖事故同族）。

## 二、根因分层

1. **直接因**：欧阳锋未执行既有纪律"以 queue_transition.py status 实时输出为准"——人的问题，已通过定位坐标转告解决。
2. **结构因（本建议书标的）**：**pending_review 没有自动登记/推送机制**。对比：
   - inbox 新素材 → watch_inbox 自动登记 INBOX-PENDING 段 → 王语嫣有被通知入口 ✅
   - 任务提审 → 无任何自动登记 → 欧阳锋只能靠老朱口头@或自觉轮询 ❌
   
   口头@的时机一旦卡在状态变更前（本次正是如此），审查者拿旧快照确认"没有"就停工——**通知机制依赖时机运气，必然复发**。
3. **次要因**：任务单文件名不含编号（按 `*387*` 搜文件名扑空）。评估：改动涉及 367 个历史文件命名惯例，**不建议动**，队列行查询足够定位。

## 三、建议方案：REVIEW-PENDING 自动段

与 INBOX-PENDING 完全对称的设计：

- 在 `70_product/tasks/production-queue.md` 增加 `<!-- REVIEW-PENDING-BEGIN/END -->` 自动维护段
- `queue_transition.py complete`（提审）时自动登记一行：任务号 + slug + assignee + 提审时间 + 任务单路径
- `queue_transition.py review`（终审完成）时自动划掉对应行
- 欧阳锋开工动作简化为：看 REVIEW-PENDING 段 → 有活就审，不依赖任何人口头通知

### 设计约束（写死给执行者）

1. **只加登记段，不动状态机语义**——状态流转仍只走 queue_transition.py，登记段是纯日志视图
2. 与 #363 提审门禁兼容（登记发生在门禁通过之后，被门禁拦截的 complete 不登记）
3. INBOX-PENDING 段的"勿手改"惯例同样适用；段内格式与 INBOX-PENDING 对齐
4. dashboard.html 是否同步展示 REVIEW-PENDING 段：执行时评估，量小可做，不为它改 generate-dashboard 架构
5. code_files 声明用**仓库内相对路径**（`90_control/scripts/queue_transition.py` 等；KDO 仓路径才需绝对路径——#380 门禁 fail-open 教训）

## 四、验收标准

1. 正向实测：测试任务 complete → REVIEW-PENDING 段自动出现登记行（含任务号/时间/路径）
2. 反向实测：review 终审后对应行自动划掉；手动乱改段内内容会被下一次流转纠正或报警
3. 门禁拦截的 complete（未提交代码）不产生登记行
4. INBOX-PENDING 段功能零回归（现有 watch_inbox 登记不受影响）
5. 367 个历史任务不补登记（只向前生效，不回填）

## 五、不做的事（边界）

- 不改任务单命名惯例（367 历史文件不动）
- 不做主动推送（飞书通知等）——登记段已够用，推送是过度设计
- 不动 queue_transition.py 的状态机/门禁逻辑

## 六、建议任务单要素

| 字段 | 建议值 |
|:--|:--|
| assignee | huangyaoshi |
| priority | P2 |
| code_files | `90_control/scripts/queue_transition.py`、`70_product/tasks/production-queue.md`（+ 若动 dashboard 则 `kdo-tools/generate-dashboard.py`） |
| 验收 | 上文第四节 5 条 |
| 终审 | 欧阳锋 |

## 七、拍板项（等老朱）

- [ ] 是否立项（建议立项，P2）
- [ ] dashboard 同步展示是否纳入本单（建议：执行者评估，量小并入）

---

*王语嫣 · 2026-08-20 · 自查立项（编排侧机制缺口，自己给自己开的单，等老朱拍板后入队）*
