---
id: 371
assignee: huangyaoshi
status: queued
updated_at: '2026-08-19T02:30:00+00:00'
title: 正库元数据规范清洗（P1，小昭体检修正版）——真 domain 空值 307 + trust_level/status/type 枚举收敛
priority: P1
dependency: []
reviewed_by: 欧阳锋
---

# #371 正库元数据规范清洗（P1）

## 任务目标

清洗正库元数据真实缺陷（王语嫣复核修正小昭口径后的版本）：domain 真空值 307 张 + 枚举污染。**注意：小昭报告的"1967 空值+拼接污染 193 张"是她扫描器不解析 list 式 domain 的测量伪影，真实规模以本任务单为准。**

## 素材/证据（王语嫣全库扫描 2026-08-19，2800 卡）

- domain 真空值：307 张（10%）
- trust_level 非标：235 张（`observed` 65 / `medium-high` 99 / `medium-low` 90 / 带 `#` 尾巴等）
- type 双轨：dk 316 vs dark-knowledge 8
- status 14 种取值无终态枚举规范（reviewed 1120 / draft 646 / enriched 523 / pending_review 88 / needs-review 45 / 其他零散）
- 缺 title 14 / 缺 type 59 / 重复键 95（OSCAR 卡 3 个 aliases 键通病）/ `_test_pa.md` 测试文件混正库

## 修改范围

1. **枚举定标**（王语嫣已裁定，黄药师执行）：trust_level ∈ {high, medium, low}——observed→medium、medium-high→high、medium-low→low；type 统一 `dk`；status 终态枚举 {reviewed, deprecated}，中间态 {draft, pending_review, enriched} 规范化
2. **脚本批量清洗**：dry-run 先行 + 非空值不覆盖 + git 留痕（批量三问）
3. **domain 307 张补全**：脚本按目录/related 推断 + 人工抽查（老顽童协助抽查 10%）
4. **重复键/缺字段修复**：95+14+59 张逐批修；`_test_pa.md` 移出正库
5. **非终态 785 张不在本任务**（处置决策另议，见队列备注）

## 边界

- 只改 frontmatter 不动正文
- 每批 dry-run + 抽查留痕
- lint 全库回归：ERROR 不新增

## 验收标准

1. trust_level/type/status 枚举 100% 合规
2. domain 空值 307→个位数（无法推断的标 unknown 并备案）
3. 重复键/缺 title/缺 type 清零；_test_pa.md 移出
4. kdo lint ERROR 不增

## 交付

1. 清洗脚本 + dry-run 记录 + 抽查证据
2. 送欧阳锋终审
