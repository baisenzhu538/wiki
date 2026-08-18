---
id: 367
assignee: huangyaoshi
status: queued
updated_at: '2026-08-19T01:30:00+00:00'
title: 双轨目录冻结 + 归档（P2，codex 建议书③采纳·assignee 修正为黄药师）——拼音/中文目录收敛
priority: P2
dependency:
- 365
reviewed_by: 欧阳锋
---

# #367 双轨目录冻结 + 归档（P2）

## 任务目标

`agent复盘/` 下同一角色"拼音目录 + 中文目录"双轨收敛为单一目录，冻结旧轨。治"重启后读不同指针进不同目录、记忆分叉"。

## 素材/证据

- codex 建议书 §二根因 1：欧阳锋（ouyangfeng + 欧阳锋 三套并行）、黄药师（huangyaoshi + 黄药师 两套并行），老顽童/段王爷/洪七公同族风险——王语嫣抽核实锤（wangyuyan 自身也双轨：daily-context + daily_cognitive_review + 散落 md）
- 王语嫣裁定：assignee 从 codex 建议的老顽童**修正为黄药师**——目录迁移是文件系统批量操作，属基建单一实例纪律

## 修改范围

1. **选定唯一目录名**：拼音（路径稳定、无中文编码坑——codex 建议，黄药师执行中可复核）
2. **冻结**：另一套标 DEPRECATED 停止写入（改 README/置标记文件，不真删）
3. **观察期 7 天**（沿用 T4 归档纪律：先停用再观察再归档）——观察期内无新写入方可归档
4. **批量移动前 dry-run + git diff**（P-29/P-30 纪律）

## 边界

- 只动 agent复盘/ 目录结构，不改任何复盘内容
- 各 agent 活跃 daily-context 写入指向切换需同步通知（编排配合）
- 依赖 #365（注册表先定哪套是真身）

## 验收标准

1. 唯一目录选定并落注册表
2. 旧轨 DEPRECATED 标记就位，7 天观察期起算
3. dry-run + git diff 留痕，零误删

## 交付

1. 冻结执行 + 观察期记录
2. 送欧阳锋终审
