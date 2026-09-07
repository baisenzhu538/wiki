---
id: task_20260907_laowantong-force-exception-labeling
title: "force 放行率标注：35 例人工标注（真误判 vs 合法逃生门）产出基线（小昭审计路由 1）"
seq: 678
status: in_progress
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-07
decision_source: 小昭三天审计建议 1（diag_20260907_xiaozhao-three-day-audit，王语嫣裁定立项 P1）
reviewer: 欧阳锋
instance: laowantong
updated_at: '2026-09-07T01:50:52.573626+00:00'
---

# #678 force 放行率标注（老顽童）

## 任务
force-exceptions.log 35 例逐例人工标注：**真误判**（不该放行）vs **合法逃生门**（force 设计意图内），产出真误判率基线报告——门禁收口方案以基线为据（现 20.8% 放行率是代理值，直接收口有误伤风险）。

## 验收
35/35 标注表（每例判定+理由）+ 基线报告 + 抽验（王语嫣抽 5 例复核）。
