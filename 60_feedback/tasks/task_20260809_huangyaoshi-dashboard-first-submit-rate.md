---
id: task_20260809_huangyaoshi-dashboard-first-submit-rate
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-09
updated_at: 2026-08-09
priority: P2
claimed_at: 2026-08-09
---

## 执行报告（2026-08-09 黄药师）

### 交付物
1. **`kdo-tools/generate-dashboard.py`** 新增首交率区块：
   - `parse_rework_rounds()`：扫描 60_feedback/tasks/ 任务单 frontmatter，提取 `rework: N` 字段 + `review_date`/`updated_at`（月份）
   - `first_submit_rate_html()`：本月首交率（一次通过 ÷ 总任务数）+ 近 3 月趋势（条形图）+ 阈值颜色分级（≥80 绿 / ≥50 黄 / <50 红，<50 标注"规格质量问题"）
   - 无数据优雅降级："记录中 — 任务单补 rework: 0/N 字段后自动统计（#267+ 起）"
2. dashboard.html 已重新生成（263 任务统计不变）

### 数据约定（对齐 task-orchestration 硬规则 3）
- 任务单 frontmatter 加 `rework: 0`（一次通过）/ `rework: N`（返工 N 次）
- **无 rework 字段不计入分母**（不拉低首交率，显示"记录中"）
- 字段规范由王语嫣编排侧定，展示层已就位

### 狗粮测试
| 场景 | 结果 |
|:---|:---|
| 真实任务单（无 rework） | ✅ 空 → 降级"记录中"正确 |
| 模拟 rework: 0 + rework: 2 | ✅ {'2026-08': {'pass': 1, 'total': 2}} = 50% 正确 |
| 有数据渲染 | ✅ 86% 正确 + 趋势条 + 颜色分级 |
| 完整生成 | ✅ dashboard.html 无报错，263 任务统计不变 |

# dashboard 首交通过率指标（B3）

## 任务目标

dashboard.html 增加 first-submission pass rate（首交通过率）指标——内容运营最重要指标（content ops playbook 2026 共识）。

## 背景

- 调研结论（diag_20260809_wangyuyan-orchestrator-evolution.md）：KDO 无首交率跟踪，E019 状态流转违反依赖人提醒
- task-orchestration skill 硬规则 3：编排侧记录"pre-submit 一次通过/返工 N 次"，月度汇入 dashboard
- 数据源：任务单验收记录（返工轮次字段，从 #267+ 起）+ queue 状态流转记录

## 规格

1. dashboard.html 新增"首交率"区块：本月首交率 = 一次通过任务数 ÷ 总任务数 + 近 3 月趋势
2. 数据来源：任务单 frontmatter/验收字段（返工轮次），无数据时显示"记录中"占位
3. 与飞轮日志联动：月度回顾可引用该指标

## 验收标准

- dashboard 生成脚本（generate-dashboard.py）无报错，数字与实际队列一致
- 无历史数据时优雅降级（显示占位不报错）

## 边界

- 不改变队列状态机（queue_transition.py 不动）
- 任务单字段规范由王语嫣定（编排侧），黄药师只做展示层

## 终审记录（2026-08-09 欧阳锋）

**verdict: PASS A- · blocking: 无 · methodology v2.2**

O3 独立验证：
1. 函数存在：parse_rework_rounds（L163）+ first_submit_rate_html（L210）
2. 重跑生成：UTF-8 口径 `PYTHONIOENCODING=utf-8 python kdo-tools/generate-dashboard.py` → "✅ dashboard.html 已生成 (263 个任务) / 待领取 10 | 审查中 2 | 进行中 1 | 已完成 250"——263 任务统计不变，与报告一致
3. dashboard.html 首交率区块实测存在："记录中 — 任务单补 rework: 0/N 字段后自动统计（#267+ 起）"降级显示正确
4. 逻辑读码确认：无 rework 不计分母（L189 continue）/ 非数字容忍 / rework==0 计 pass / 月份 review_date→updated_at→mtime 兜底 / 阈值分级 ≥80 绿 ≥50 黄 <50 红 + 归因标注（规格质量 vs 执行质量）/ 近 3 月趋势条形图——全部与报告约定一致
5. 狗粮数字验证：模拟 {'2026-08': {pass 1, total 2}} → 50% 逻辑成立

🟢 TODO：脚本结尾 print ✅ emoji 在 Windows GBK 终端崩溃（UnicodeEncodeError，exit 1）——HTML 已生成不影响功能，但默认终端复现会报错。建议并入停车场 GBK 编码修复项一次清（同 #272 语境识别的问题族）。

五维：溯源 90/逻辑 90/暗知识 80/可操作 90/表达 85 → 总分 88（A-）
