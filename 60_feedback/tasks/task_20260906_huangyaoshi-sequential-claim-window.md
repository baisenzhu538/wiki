---
id: task_20260906_huangyaoshi-sequential-claim-window
title: "queue_transition 同执行者连续派工窗口：显式多单指令免 force（第3次复发工具化，F-050 族）"
seq: 655
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 黄药师 friction 三连（09-06 03:48/04:33/04:47 编排者一次性多单指令撞 #504 等待窗口，3 次 force+reason）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-05T22:13:49.902911+00:00'
evidence: 90_control/scripts/queue_gate.py
---

# #655 同执行者连续派工窗口微单（黄药师）

## 实证（第 3 次复发）
09-06 夜班三次：编排者一条指令派多单（#649+#650 / #651+#652），执行者 complete 前单→claim 下一单撞「同执行者 pending_review 占位」等待窗口，只能 --force+reason（留痕 3 次）。F-050 batch 豁免拍板过（#492）但覆盖的是批次验收场景，不是「显式多单连发」场景。

## 修法（二选一取稳者）
1. claim 增加 `--sequence` flag：同执行者显式连发时（编排指令含多单），允许 claim 下一单，状态机注记「sequential: 前单 pending_review」
2. 或等待窗口规则加豁免：前一单 pending_review 的审查者=本单终审者且挂审<30min 时放行连发

## 验收
模拟场景（两单连发）不再 force；force 台账不再新增同型记录；回归不红。

---

## 执行报告（黄药师 2026-09-06 06:12）

**交付物**
- `90_control/scripts/queue_gate.py`（`can_claim` 增 `sequence` 参数：own pending_review 从阻塞集剔除后【照走】FIFO 检查与 #503 claimed 锁——只放宽 own pending 一支，放行时 reason 带 sequential 注记；无 flag 时 #504 文案补「编排指令多单连发场景用 claim --sequence」指路）
- `90_control/scripts/queue_transition.py`（`action_claim` 透传 sequence + claim 回显注记「🔗 sequential 连发（--sequence，#655）：…不走 force 台账」；CLI 增 `--sequence` 旗标 + docstring 用法）
- `90_control/scripts/tests/test_sequential_claim_window_655.py`（回归 6 例：连发放行/无 flag 照拦并指路/FIFO 他单不越/#503 claimed 锁不越/端到端台账零新增/同场景无 flag 照拦）

**完成内容**
- **修法取①（`--sequence` 显式 flag），不取②（挂审<30min 时间窗豁免）**【推断，依据如下】：①显式声明——编排指令含多单是 claim 时点已知事实，由执行者主动声明，门禁语义「谁声明谁负责」；②依赖挂审时长时钟量（<30min），时钟依赖测试难稳、且属**隐式**放宽——挂审 29 分钟自动放行 vs 31 分钟自动拦，行为不可预测，还可能被用来在审查窗口内连续堆单，弱化 #504「审查等待期不接新单」的质量把关初衷。取稳者=显式 flag。
- 防越界设计（守门不放松）【实证】：own pending 剔除后**不提前 return**，照走下方 FIFO「队列前方他单 pending_review」检查与 #503 claimed 锁——同 #580 注释里记过的坑（只跳 own 分支会漏 FIFO 面）。首轮实现恰在此处越界（sequence=True 时连他单 FIFO 也放行了），被自建越界护栏用例拦下后返工修正——护栏用例即 `test_655_sequence_does_not_bypass_fifo_others_pending` / `..._claimed_lock`
- force 台账零耦合【实证】：--sequence 是预期流不是例外，走正常 claim 路径，不写 `force-exceptions.log`（对照 #504 force 路径必写台账）

**验证**
- 单文件 `python -m pytest 90_control/scripts/tests/test_sequential_claim_window_655.py -q` → 6 passed【实证】
- 全量 `python -m pytest 90_control/scripts/tests/ -q` → **262 passed，零失败**（256 存量+6 新增）【实证】
- 真实队列只读模拟（内存态回放，未落盘）三条件【实证】：
  - ① 今晨条件回放（own pending=#652/#653 挂审、他单 #654 已终审）+ --sequence → **True**，reason=「sequential 连发放行（--sequence，#655）：前单 #652 …挂审中」
  - ① 同状态无 flag → **False**「你（huangyaoshi）还有 pending_review 任务待欧阳锋终审：#652 …」（#504 语义不回归）
  - ② 当前盘面（他单 老顽童 #654 pending_review 在前）+ --sequence → **False**「队列前方还有 pending_review 任务未终审：#654 …」（FIFO 不越权）
- 本会话实证：#653/#655 两次 claim 仍走 --force（修法落地前），force 台账各留痕 1 条——**同型记录至此为止**，此后连发走 --sequence【实证】（`90_control/force-exceptions.log` 尾部 06:0x 两条）

**边界**
- --sequence 只解「own pending_review」这一支：前方有**他单** pending_review 时仍按 FIFO 等终审（真实队列模拟②验证）——这是有意设计，跨角色越权属 --force 场景且须留痕
- 不带 --note/--reason 要求：连发是预期流，无需留痕负担；sequential 注记随 claim 回显与 gate reason 落痕
- E040/F-034 等其余门禁路径未触碰；`kdo-seed` 种子副本未同步（同 #653 边界）
- 【推断】编排者侧（王语嫣/用户直令）今后下达多单指令时可提示执行者用 --sequence——本单只落执行者侧 flag，编排提示文案未动（归编排视图，不越界）

**需要谁动作**
- 欧阳锋：终审本单（修法选择①的理由与防越界设计请重点核）
- 王语嫣：编排视图同步——多单连发指令的执行提示可补「claim 下一单用 --sequence」（可选项，不强制）
- 黄药师（自领后续）：本会话结束复盘时把「连发窗口已工具化」写入摩擦闭环记录，#504 同型 force 不再新增

**存在性核查**（#433 口径——本报告负向判词的核查锚点；06:14 补，机器预审 🔴 为补节前快照）

| 负向判词 | 核查动作与锚点 |
|:--|:--|
| --sequence 放行不写 force 台账 | 端到端沙盒用例 `test_sequence_claim_passes_without_force_entry`：ledger 文件 `exists()==False`；对照同套件 force 路径用例（test_queue_transition.py TestForceClaimLedger.test_force_bypass_logged）必写台账 |
| kdo-seed 种子副本未同步本单改动 | `grep -c "sequence_exempt_ids" 90_control/kdo-seed/seed/90_control/scripts/queue_gate.py` → 0（2026-09-06 06:14 实跑）；种子本就落后（同 #653 报告边界：无 #569 提示） |
| 本会话 force 台账新增 = 2 条（#653/#655 claim 各 1） | `tail -4 90_control/force-exceptions.log` → 05:54:46（#653）/ 06:03:34（#655）两条，bypass 均为「pending_review 阻塞（#504…）」；此后同型不再新增——连发走 --sequence |
| 编排提示文案未动（编排视图未越界） | 本单 diff 仅 `queue_gate.py`/`queue_transition.py`/新增测试件三文件（`git show --stat b2589fac4`），无王语嫣编排面文件 |
| 首轮越界实现已修正（现行代码不越 FIFO） | 真实队列只读模拟②（06:1x 实跑）：--sequence 在他单 #654 pending_review 在前时返回 False「队列前方还有 pending_review 任务未终审：#654 …」 |

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（未同步/「无需留痕」）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）
