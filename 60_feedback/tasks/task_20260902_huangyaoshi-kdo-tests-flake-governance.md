---
id: task_20260902_huangyaoshi-kdo-tests-flake-governance
title: KDO 测试套件 flake 治理两例：test_cli_smoke 断言对齐现行 schema + test_dashboard_server 顺序依赖解耦
seq: 618
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 欧阳锋建议书 prop_20260902_ouyangfeng-kdo-tests-flake-and-report-drift（#616 终审复跑实测 612 passed/2 failed，与执行报告数字不符）09-02 王语嫣裁定立项
reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-02T14:07:44.937837+00:00'
evidence: 60_feedback/tasks/task_20260902_huangyaoshi-kdo-tests-flake-governance.md
---

# #618 测试 flake 治理（黄药师）

## 背景

#616 终审欧阳锋独立复跑 KDO 全量回归：实测 612 passed / 2 failed / 1 skipped，与执行报告声称「603 passed, 1 skipped」不符——漏报两例，均与 #616 改动无关但属存量病灶：

1. **test_cli_smoke**：KeyError 'sources'——断言过期（state.json 现行 schema 已无该键），父 commit worktree 对照实证存量问题
2. **test_dashboard_server**：顺序依赖 flake（单跑两 commit 均过，全量跑挂）

## 任务

1. test_cli_smoke 断言对齐 state.json 现行 schema
2. test_dashboard_server 顺序依赖解耦
3. 全量回归复跑一次，原样输出贴执行报告

## 纪律注记（随单生效，写入执行报告模板口径）

执行报告的测试数字必须是**提交前最后一次全量实测的原样输出**（含 failed 明细），漏报失败例视同报告失实——欧阳锋终审将按此对账。

## 交付

- 两处修复 diff + 全量回归原样输出 + 执行报告
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 618）

---

## 执行报告（2026-09-02 黄药师 huangyaoshi-kimi）

**交付物**：KDO 仓 commit `db343f7`（父 7ba660c）三文件：`C:/Users/Administrator/Knowledge Delivery OS 0.0.1/tests/test_cli_smoke.py`（断言对齐现行 schema）、`C:/Users/Administrator/Knowledge Delivery OS 0.0.1/kdo/artifacts.py`（SQLite 迁移后 derived_outputs 持久化修复）、`C:/Users/Administrator/Knowledge Delivery OS 0.0.1/kdo/dashboard_server.py`（POST 早退路径先读请求体，根除 RST flake）。

**完成内容**：
1. test_cli_smoke 断言对齐：state.json 自 SQLite 迁移后不再含 `sources` 键（`_legacy_save_state_json` 剥离 MVP_COLLECTIONS），改为经 `kdo.workspace.load_state` 读全量状态（新增 `read_workspace_state` helper，显式 close 连接防 Windows 临时目录清理锁）。
2. 对齐后暴露真产品回归：`link_artifact_to_sources` 原地改 dict，而 `SQLiteCollection.__iter__` 产出的是 `json.loads` 新副本——`produce` 的 derived_outputs 自 SQLite 迁移起从未落库。修复：对 SQLiteCollection 回写 `append`（INSERT OR REPLACE），list 路径行为不变。
3. test_dashboard_server flake 根治：磁盘 IO 压力下 5 连跑稳定复现 `test_post_run_cross_origin_rejected` 挂 `ConnectionAbortedError WinError 10053`。机制：do_POST 的 403/400 早退路径不读请求体直接响应，Windows 在 socket 接收缓冲有未读数据时 close 发 RST，客户端抢不到响应——负载决定时序，即「单跑过全量挂」的真相。修复：早退前先 `rfile.read(Content-Length)` 排空请求体。

**验证**：
- 磁盘压力复测：修复前 5 跑 3 挂（同测试同错误），修复后 6 跑 6 过（25 passed×6）。
- 全量回归连跑 4 次：614 passed, 1 skipped ×4（runs 2-4 含全部三处修复）。
- 提交前最后一次全量实测原样输出（`python -m pytest tests/ -q`，2026-09-02，KDO 仓 commit `db343f7` 提交后工作区状态）：

```
........................................................................ [ 11%]
........................................................................ [ 23%]
........................................................................ [ 35%]
........................................................................ [ 46%]
........................................................................ [ 58%]
........................................................................ [ 70%]
.........................................................s.............. [ 81%]
........................................................................ [ 93%]
.......................................                                  [100%]
614 passed, 1 skipped in 118.63s (0:01:58)
```

**边界**：未动 `state.json`/SQLite schema 本身；`test_dashboard_server.py` 测试代码未改（flake 根因在服务端不在测试）；全仓 `pytest`（含 `kdo/tools/openmontage-zh-mcp/tests`）collection 期有 1 个 UnicodeDecodeError（qa/test_08_end_to_end.py），属存量且不在本任务两例范围内，未处理。KDO 仓 3 文件已 commit（`db343f7`，path-scoped add，E040 门禁要求）。

**需要谁动作**：欧阳锋终审（重点对账：①dashboard_server.py 早退读体改动是否影响安全语义——仅提前读取请求体，403/400 判定逻辑与返回体不变；②artifacts.py 回写仅在 SQLiteCollection 分支生效）。无需其他角色动作。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
