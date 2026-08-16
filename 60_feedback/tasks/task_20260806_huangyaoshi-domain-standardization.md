---
reviewed_by: 欧阳锋
review_date: 2026-08-09
id: task_20260806_huangyaoshi-domain-standardization
task_id: 237
assignee: huangyaoshi
status: reviewed
updated_at: 2026-08-06
domain: system
priority: P0
---

# #237 域名标准化迁移（6 个脏域 294 张）

## 背景

欧阳锋发现 + 王语嫣全库扫描验证：frontmatter `domain` 字段存在脏值，会让 MOC/domain digest 按 domain 聚合时分裂成伪域，检索域路由、图分析、质量门禁全部受影响。**王语嫣裁定标准化方案**（2026-08-06，裁定全文见 `.agent/decisions.md`）。

## 王语嫣裁定（执行标准）

**规范**：统一 kebab-case 英文小写（与存量主流 `yitang` 1022 / `ai-collaboration` 262 一致）。

| 脏域（现） | 标准化为 | 卡数 |
|:--|:--|:--|
| `design- design` | `design` | 187 |
| `yitang- yitang` | `yitang` | 34 |
| `ai_collaboration` | `ai-collaboration` | 20 |
| `learning-methodology- product` | `learning-methodology` | 14 |
| `critical_thinking` | `critical-thinking` | 20 |
| `business_judgment` | `business-judgment` | 19 |
| **合计** | | **294** |

**范围边界（裁定明确）**：
1. **只统一"值"，不统一"格式"**——43 张旧卡内联标量 `domain: strategy` 与列表格式并存是历史遗留，本次不动（格式统一风险大收益低，另议）
2. 不处理空 domain 值（极少数，随元数据回填长线）
3. 不处理 `src_unknown`（733 张，占位未填≠命名脏，单列跟踪，不纳入本次）

## 执行纪律（硬约束，违反=返工）

1. 复用 `90_control/scripts/bulk-fix-frontmatter.py` 模式（dry-run/fix/stats 三模式、不覆盖已有值）：`--dry-run` 预览 → `git diff` 逐卡验证 → `yaml.safe_load` 全库通过率 ≥99% 才 apply（#222 事故教训：统计达标≠结构健康）
2. 串行 + 目录划分（8 高价值目录/普通目录分批）
3. `#228` 重复键检测已上线——新 frontmatter 不得引入重复键
4. 无法解析的文件（若存在）跳过并单独移交，不强行修改
5. 迁移基于 7/27 基线（commit 16b64db39）全量比对审计（#222-224 已验证不涉及 domain 字段，零冲突）
6. 每批写入前：dry-run 预览 + git diff 验证 + yaml.safe_load 确认（#223 任务单同款规范）

## 验证 / 验收标准

1. 重跑全库 domain 扫描：6 个脏域归零、无新脏域、全库 domain 值数 257 → 预期 <100
2. `kdo lint` 0 新增 ERROR；`yaml.safe_load` 全库 ≥99%
3. git diff 显示：只改 domain 值行，正文零改动
4. 复测：复盘 MOC（#236）聚合正常

## 依赖 / 边界

- #228 重复键 lint 已上线 ✅（防复发护栏）
- #40 已 reviewed：design 域 196 文件全部 healthy（0 编码损坏）——无需跳过损坏文件
- 与 #236 并行（MOC 手工关系图聚合，不依赖 domain 字段）；与 #233/#234/#235 无冲突（相关卡 domain 值干净）
- 完成后登记到 dashboard + kb-evolution-direction

## 🆕 验收记录（2026-08-06）

- ✅ **王语嫣独立验证通过**（E004 教训：申报≠事实，重跑全库 domain 扫描）：6 脏域全部归零（design- design 0 / yitang- yitang 0 / ai_collaboration 0 / critical_thinking 0 / business_judgment 0 / learning-methodology- product 0）
- 黄药师报告 254 张迁移（王语嫣口径 294 值为按"值"计数，差异为一张卡含多个 domain 值的去重，不冲突）
- ⚠️ 发现第二批非标准域名（粘连/重复/大小写/测试值）→ 已编排 #239 补充清理（#238 前置）
- ⚠️ 王语嫣扫描脚本存在跨字段误读（~250 个假"脏值"）——#239 要求 yaml.safe_load 级权威清单
- 状态：待欧阳锋终审（队列流转）
