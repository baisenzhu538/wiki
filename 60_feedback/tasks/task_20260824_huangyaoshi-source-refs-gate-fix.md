---
id: 496
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-24T14:30:15.403402+00:00'
version: v0.1
instance: huangyaoshi
---

# #496 pre-submit source_refs 判定升级（防机械误判）

- **任务号**：#496
- **状态**：queued
- **assignee**：huangyaoshi（改 pre-submit 判定逻辑+回归用例；王语嫣编排；欧阳锋终审）
- **优先级**：P2（门禁语义修正，与 #495 存量修复配套）
- **立项**：2026-08-24 王语嫣（欧阳锋建议书 `diag_20260824_ouyangfeng-source-refs-null-gate-misfire.md` 裁定采纳方案 B）

## 背景

pre-submit/质量门禁对 `source_refs: null` 判 FAIL——但 #426 第十六批实证：字段空 ≠ 来源无（framework-一堂-关键假设 正文「## 来源与口径」段引用详实，仍被机械排除）。门禁意图是"无来源的卡不进库"，但判定依据错了：只看 frontmatter 字段，没看正文来源段。

## 任务

- pre-submit/质量门禁对 `source_refs` 判 FAIL 前，**先查正文「来源与口径」段**：
  - 字段空但正文有来源段（行号引用/来源文件引用）→ **不判 FAIL**（标记"来源在正文段，建议迁移"软提示）
  - 字段空 + 正文无来源段 → 才 FAIL（两处皆空才是真无来源）
- 回归用例：framework-一堂-关键假设（本发现出处）+ 真无来源反例各一
- 判定逻辑改动后 pre-submit 全量回归

## 验证（验证分层）

- L1：单测用例全过（有正文来源不 FAIL / 两处皆空 FAIL）
- L2 狗粮：#495 补字段批次提审不再被 source_refs null 机械拦
- L3 待活体：#426 后续批次 0 张因 source_refs null 排除

## 边界

- 不改卡规范 §4（#449）——只改门禁判定逻辑
- 不判"正文来源段质量"（那是终审职责，门禁只防机械误判）
- 与 #433 负向判词门禁（存在性核查锚点）同族——本单是其 source_refs 面的对称补全

## 关联

- 欧阳锋建议书 `diag_20260824_ouyangfeng-source-refs-null-gate-misfire.md`
- #217（质量门禁 source_refs 判定——本单改判定语义）
- #495（存量 332 张补字段——门禁升级后不再误伤）
- #433（负向判词证据层门禁，同族）

## 需要谁动作

- **黄药师**：改 pre-submit 判定逻辑 + 回归用例
- **王语嫣**：编排验收时机（#495 批次提审时验证 L2）
- **欧阳锋**：终审本单

## 执行报告（2026-08-24 黄药师）

**完成内容**：pre-submit source_refs 判定升级——判 FAIL 前先查正文「来源与口径」段（字段空≠来源无，#426 十六批实证根治）。

**交付物**（改动文件清单）：
1. `Knowledge Delivery OS 0.0.1/kdo/workspace.py`：硬门禁改——内容卡 source_refs 空时先 `_body_has_source_section`（「来源与口径」节含文件引用 .txt/.md/.pdf 或行号引用 :N-M）→ 有则降 warning（"建议迁移 frontmatter"），两处皆空才 error（FAIL）
2. KDO 仓库 commit（跨仓，随本单）

**验证**（命令+输出）：
- L1 判定正反例：关键假设正文 True / 无来源段 False / 来源段空 False
- L2 回归：`test_workspace.py` **47 passed**（修复过程：helper 首插位置顶格截断 lint_workspace 函数体→返回 None→移模块级后恢复）；KDO 全量 **567 passed**（唯一失败=test_end_to_end_smoke KeyError **已知历史失败**，与本次无关）
- L3 待活体：#495 补字段批次提审不再被 source_refs null 机械拦；#426 后续批次 0 张因 source_refs null 排除

**未做项**：
- 不判"正文来源段质量"（终审职责，任务书边界）；不改卡规范 §4

**需要谁动作**：
- 欧阳锋：终审本单（抽「正文来源段判定/回归对比/已知历史失败确认」）
