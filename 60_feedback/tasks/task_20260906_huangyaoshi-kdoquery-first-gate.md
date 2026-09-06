---
id: task_20260906_huangyaoshi-kdoquery-first-gate
title: "kdo query 第一优先门禁：知识检索强制规则（宪法第六条+pre-submit 检索记录检查）——老朱「不信自律信门禁」"
seq: 669
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 老朱 09-06 直令「kdo query 是第一优先级，我不相信自律只相信门禁和强制规则，找不到再采用 grep」
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-06T22:20:00+08:00'
---

# #669 kdo query 第一优先门禁（黄药师）

## 背景
王语嫣标签治理调研时未用 kdo query（用 grep 沿自己足迹搜），漏掉库内已有方法卡两周——W11 写在锚点里照样违例。老朱裁定：**不信自律，信门禁**。规则=kdo query 第一优先，grep 是兜底不是首选。

## 任务
1. **宪法增补第六条**（90_control/agent-behavior-constitution.md，v1.0→v1.1）：「知识类问题第一动作=kdo query（检索词做同义/中英扩展）；0 命中或证据不足才降级 grep 兜底；诊断/调研类产出必须附 kdo query 检索记录节（查询词+命中数+日期），无检索记录=不闭环」
2. **pre-submit 检查项**：诊断/调研/报告类文件提交时，检查器校验存在「kdo query 检索记录」节——缺失=WARNING（先软一周）→ 升 HARD（门禁化，与 F-035 同级）
3. **grep 降级口径写进 constitution 与各角色 context 模板**：grep 只用于①kdo query 之后补充定位②非知识类检索（代码/配置/日志）
4. **回归**：模拟无检索记录的报告→检查器拦截；有记录→通过；现有测试不红

## 验收
- 检查器两态（WARNING→HARD）生效实证
- 宪法 v1.1 diff+三挂载点同步（startup/拉起器模板/公告）
- 回归不红
