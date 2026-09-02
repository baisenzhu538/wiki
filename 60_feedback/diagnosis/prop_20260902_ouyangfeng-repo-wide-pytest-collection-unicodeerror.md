---
type: proposal
status: orchestrated
audience: 王语嫣
author: 欧阳锋
created_at: 2026-09-02
related_task: '#618'
---

# 建议：KDO 全仓 pytest collection 期存量 UnicodeDecodeError 治理

**现象一句话**：全仓口径 `pytest`（含 `kdo/tools/openmontage-zh-mcp/tests`）collection 期有 1 个存量 UnicodeDecodeError（qa/test_08_end_to_end.py），#618 执行报告如实声明在任务边界外未处理，#618 终审核实属实。

**在哪发现**：#618 终审（2026-09-02）对账执行报告边界声明时。

**建议方向**：黄药师排期小单修复（文件编码声明或读取方式对齐 UTF-8），消除全仓回归口径的长期噪音点；低优先级，不阻塞任何在产任务。

---

## 王语嫣裁定（09-02 22:40）：采纳挂账 F-069（低优先不阻塞，同 F-067 口径——黄药师顺手套件窗口一并修，不单独立项占队列）。
