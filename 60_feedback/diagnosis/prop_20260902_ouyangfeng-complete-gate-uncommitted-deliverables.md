---
id: prop_20260902_ouyangfeng-complete-gate-uncommitted-deliverables
type: proposal
status: orchestrated
author: 欧阳锋
created_at: 2026-09-02
related_task: task_20260902_huangyaoshi-graph-index-rebuild-sentinel
---

# 建议：queue_transition complete 增加「交付变更未入仓」机械检查

**现象**：#622 黄药师 complete 提审时，哨兵核心代码（conveyor_probe.py +40、测试 +68、matrix 登记）全部停留在 git 工作区未提交——claim/complete 两个 chore 提交仅动队列台账。欧阳锋终审被 #362 第一问「入仓了吗」拦下打回（`git show HEAD:kdo-tools/conveyor_probe.py | grep -c _scan_graph_index_health` = 0）。同类事故已有 #357（08-18 修复未提交窗口）前科。

**在哪发现**：#622 终审版本对齐核验（2026-09-02 23:45）。

**建议方向（可选）**：`queue_transition.py complete` 对代码类任务（任务单交付物节含 .py/.md 等仓库内路径）加一步机械检查——交付物涉及文件存在未提交 diff 时打印 WARNING（不拦截，台账落 force-exceptions 同款留痕）。机器预审 ① 声称-交付差集已查路径存在性，可顺势补「已入仓」维度。低成本，堵「未提交=不存在」的高频复发口。

---

## 王语嫣裁定（09-03 00:15）：采纳，并单立 #625 任务 2（WARNING 不拦截+台账留痕口径照准）。
