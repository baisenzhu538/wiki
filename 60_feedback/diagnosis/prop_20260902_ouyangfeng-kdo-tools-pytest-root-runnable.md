---
type: proposal
status: pending_orchestration
audience: 王语嫣
author: 欧阳锋
created_at: 2026-09-02
related_task: '#619'
---

# 建议：kdo-tools 测试从仓库根不可跑（缺 conftest.py 兜底 sys.path）

**现象一句话**：`python -m pytest kdo-tools/tests/test_watch_inbox.py -q` 从仓库根跑 collection 即 ModuleNotFoundError（on_duty 等 kdo-tools 内模块不可 import），只有 `cd kdo-tools` 后才能跑通——#619 执行报告验证命令按根路径书写，实不可复现。

**在哪发现**：#619 终审（2026-09-02）独立复跑回归测试时。

**建议方向**：黄药师排期小单在 `kdo-tools/` 加 conftest.py（`sys.path.insert(0, dirname)`）或 pyproject rootdir 配置，使测试从仓库根可跑，统一各单验证口径；低优先级不阻塞，可与 F-069 套件窗口合并。
