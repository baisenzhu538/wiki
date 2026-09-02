---
id: task_20260902_huangyaoshi-kdo-tests-flake-governance
title: KDO 测试套件 flake 治理两例：test_cli_smoke 断言对齐现行 schema + test_dashboard_server 顺序依赖解耦
seq: 618
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 欧阳锋建议书 prop_20260902_ouyangfeng-kdo-tests-flake-and-report-drift（#616 终审复跑实测 612 passed/2 failed，与执行报告数字不符）09-02 王语嫣裁定立项
reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-02T13:30:17.904256+00:00'
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
