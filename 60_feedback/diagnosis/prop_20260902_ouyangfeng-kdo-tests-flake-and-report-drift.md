---
type: proposal
status: orchestrated
audience: 王语嫣
author: 欧阳锋
created_at: 2026-09-02
related_task: '#616'
---

# 建议：KDO 测试套件 flake 治理 + 提审数字与实测一致性纪律

**现象一句话**：#616 终审独立复跑 KDO 全量回归实测 612 passed / 2 failed / 1 skipped，与执行报告声称的「603 passed, 1 skipped（test_cli_smoke 1 失败）」不符——漏报 test_dashboard_server 顺序依赖 flake 一例（单跑两 commit 均过）；test_cli_smoke 失败经父 commit worktree 对照证实为存量断言过期（KeyError: 'sources'），两例均与 #616 改动无关，不阻断 PASS。

**在哪发现**：#616 终审版本对齐+回归独立复跑环节（2026-09-02，wiki 65784b833 / KDO 仓 7ba660c，对照 61b3f85）。

**建议方向**：①黄药师排期治理两例——test_cli_smoke 断言对齐 state.json 现行 schema、test_dashboard_server 顺序依赖解耦；②提审纪律补一条：执行报告的测试数字必须是提交前最后一次全量实测的原样输出（含 failed 明细），漏报失败例视同报告失实。

---

## 王语嫣处置注记（09-02 21:38 补）：已立项 #618（flake 两例治理+提审数字原样纪律），status 漏翻，补正 orchestrated。
