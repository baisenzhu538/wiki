---
id: 462
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-23T07:27:37.715696+00:00'
version: v0.1
instance: huangyaoshi
reviewed_by: 欧阳锋
review_date: '2026-08-23'
grade: A-
---
# #462 探针「流转完成」信号——终审结果通知编排者（治编排者盲区）

- **任务号**：#462
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P1（老朱 2026-08-23 提问触发：「欧阳锋终审结束你是收不到探针通知吗？」——#447 PASS A 靠老朱询问编排者才知，部署卡点完全盲区）
- **立项**：2026-08-23 王语嫣（编排者盲区与 #454 沉没问题同族；与 #460 机器自报层互补——#460 治拦截事件，本单治流转完成事件）

## 缺口

探针现有三类信号：新提审→通知欧阳锋 / 新可领取→通知对应角色 / 新建议书→通知王语嫣。**流转完成（review pass/fail）无任何通知**——终审 PASS 后「待部署」卡点、终审 FAIL 后「待返工」卡点，编排者与生产者都靠自己去翻队列才发现。

## 设计

1. **new_reviewed 信号**：探针状态对比（last_reviewed 集合），本轮新增 reviewed 任务 → 通知 **wangyuyan**：「⚖️ #xxx 已终审 PASS（grade），待部署/已闭环」——编排者的部署/入宪动作从此有到达通知（「登记≠通知」原则补全到流转侧）
2. **new_failback 信号**：pending_review → queued 的退回（终审 FAIL）→ 通知**对应 assignee 角色**：「↩️ #xxx 被退回，见任务单终审记录」——生产者返工不再靠自觉发现
3. 通知文案含任务号/结论（PASS/FAIL+等级）/下一步（部署→王语嫣；返工→assignee）——信息自足，接收方不用翻文件即可行动
4. 单扫描器纪律：与既有探针同一扫描事件，state 文件扩两个集合字段

## 验证（验证分层声明）

- L1：单测（状态对比/两信号/幂等）
- L2 狗粮：模拟 review 流转 → 通知到达 wangyuyan 通道
- L3 待活体：下一次真实终审 PASS，我在无老朱提醒下主动报「#xxx 可部署」

## 边界

- 只加通知信号，不改状态机、不自动部署（判断留人——F-033 边界：探针只推送流转，部署/编排动作王语嫣自己做）
- 与 #460（gate-blocked 信号）同文件面 conveyor_probe.py，实施顺序自定（两单独立验收）

## 执行报告（2026-08-23 黄药师）

**完成内容**：探针「流转完成」信号——终审 PASS 通知编排者（⚖️）、终审退回通知 assignee（↩️），治编排者盲区。

**交付物**（改动文件清单）：
1. `kdo-tools/conveyor_probe.py`：`_queue_signal` 扩展两信号——`new_reviewed`（上次快照后新增 reviewed → 王语嫣「⚖️ #x 已终审，待部署/已闭环」）；`new_failback`（上次 pending_review 现在回 queued = 退回 → **按 assignee 路由**（#443 ASSIGNEE_ROLE 复用）「↩️ #x 被退回，见任务单终审记录」）；state 扩 `last_reviewed` 集合（幂等）
2. `kdo-tools/tests/test_conveyor_probe.py`：+1（三阶段状态对比：新 reviewed 检出 / pending→queued 退回检出 / 幂等）

**验证**（命令+输出）：
- L1：pytest **17 passed**（16 原有 + 1 新增：状态对比/两信号/幂等）
- L2 狗粮：真实探针重置 state 首扫——王语嫣收到「⚖️ KDO 已终审 45 单…」（首扫建档全量）；二次扫**零信号**（幂等 ✅）；新提审路由未破坏（欧阳锋收 #458/#461）
- L3 待活体：下一次真实终审 PASS，编排者在无老朱提醒下主动知道「#x 可部署」

**未做项**：
- 不改状态机、不自动部署（F-033 边界：探针只推送，部署/编排王语嫣自己做）
- 与 #460（gate-blocked 拦截信号）同文件面互补——本单治流转完成事件

**需要谁动作**：
- 王语嫣：收到 ⚖️ 后执行部署/入宪动作
- 各角色：收到 ↩️ 后按任务单终审记录返工
- 欧阳锋：终审本单（抽「两信号/幂等/路由正确」）

---

## 终审记录（欧阳锋 · 2026-08-23）

**结论：PASS / A-**

**版本对齐三问**（代码类，全绿）：① 入仓：f66acee17（15:22）在 HEAD ② 生效：CLI 即时加载 ③ 对齐：审查对象=HEAD

**O0 逐条溯源**：
1. **new_reviewed 信号** ✅（L110-114/121）：reviewed 快照对比 + `last_reviewed` 集合幂等——终审 PASS → 王语嫣「⚖️ KDO 已终审 N 单（待部署/已闭环）」——编排者部署/入宪动作有到达通知（"登记≠通知"补全到流转侧）
2. **new_failback 信号** ✅（L116-119）：failback_candidates = 上次 pending_review 现在既不在 pending 也不在 reviewed（=退回 queued）——**按 assignee 路由**（L450-452 复用 #443 ASSIGNEE_ROLE，未命中回落 laowantong）「↩️ KDO 退回 1 单：#{seq}（{tid}），见任务单终审记录」——生产者返工不再靠自觉
3. **单扫描器纪律** ✅：同一 `_queue_signal` 扫描事件 + state 扩 `last_reviewed` 集合——无第二套扫描器
4. **测试独立复现**（O3）✅：pytest **17 passed**（16 原有 + 1 新增：三阶段状态对比/两信号/幂等）
5. **L2 狗粮报告** ✅（真实探针重置 state：首扫建档 45 单到王语嫣 + 二次零信号幂等 + 新提审路由未破坏）
6. **边界** ✅：不改状态机、不自动部署（F-033 判断留人——探针只推送，部署/编排王语嫣自己做）

**发现问题**：
- 🔵 L117 死代码占位行（`new_failback = [(t, s) for t, s in review if False]`——恒空列表被 L119 覆盖）——无害但应清理（下个接触该文件的单顺手删）
- 🔵 新提审/新可领取通知在首扫建档时未受影响（L2 报告确认路由未破坏）——观察项无实质影响

**魔鬼代言人**：3 个月后最可能出问题——last_reviewed 快照长期不刷新（探针停跑）导致幂等集合过时，恢复后首次扫描全量补发通知（噪音一次）；或 failback 判定在"queued→pending_review→queued"的正常返工循环中误报（failback 语义=退回，与批次任务手动恢复 queued 同路径——批次验收场景可能误通知"被退回"，friction 观察）

**存在性核查**（本意见书负向断言证据）：
- 「两信号实现」→ 核查：L100-124 源码逐行（new_reviewed/failback_candidates/new_failback）
- 「路由复用」→ 核查：L450-452 ASSIGNEE_ROLE.get 实测
- 「17 passed」→ 核查：pytest 独立复现输出
- 「幂等」→ 核查：L121 last_reviewed 快照更新 + L2 报告二次扫零信号

**残余风险**：批次任务手动恢复 queued 可能触发 failback 误通知（friction 观察期）；死代码行待清理。

*欧阳锋 · 2026-08-23 · A-*
