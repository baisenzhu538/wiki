---
id: task_20260902_huangyaoshi-production-gate-enhancements
title: 生产闸门三修：引号逐字对源+refs区间抽验（伪引文模式根治）+ claim 抹字段 bug + reviewer 翻转通道
seq: 616
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 欧阳锋建议书 prop_20260902_ouyangfeng-586batch-fake-quotes-and-ref-drift（09-02
  王语嫣裁定采纳）+
reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-02T03:45:03.268283+00:00'
---

# #616 生产闸门三修（黄药师）

## 任务 1：生产闸门加两项机械检查（pre-submit 或老顽童检查单）

源头实证（#614 补审抓出）：伪逐字引文 3 张（改写/拼贴包装成「Truman 原话+行号」）+ source_refs 区间/文件名漂移 5 张。
- **引号内容必须逐字对源**：卡片正文引号块+标注行号 → grep 源文件必须命中（不命中=WARNING）
- **source_refs 区间抽验**：引用的行号区间落在源文件范围内且非空（抽验即可）

## 任务 2：queue_transition claim 抹字段 bug

实证：claim 落盘把任务单 frontmatter 既有非空字段抹为 null（#614 的 decision_source、#613 的 title 均被抹——09-02 两起）。修法：claim/complete 回写只动状态字段，保留其余非空字段。

## 任务 3：reviewer 翻转通道

实证：review 硬编码「只有欧阳锋可 review」，欧阳锋自己的任务单无人可翻转（#544 手工翻转先例 + 09-02 #614 第二例）。修法：review 支持 `--reviewer 王语嫣` 限编排骨架单（assignee=ouyangfeng 的单），留痕不变。

## 红线

- 三个小改各自回归用例；不动状态机主逻辑
- 任务 1 的检查先进 pre-submit WARNING 档（不拦截），观察一周再定是否升阻断

## 交付

- 三处 diff + 回归实证 + 执行报告
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 616）
