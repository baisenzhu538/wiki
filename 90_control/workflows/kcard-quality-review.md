# KDO 卡片周期性质量审查机制

> 目标：让 30_wiki 全库质量持续可见、可控、可改进
> 维护角色：王语嫣（QA 负责人）
> 频率：月度小审查 + 季度大审查

---

## 审查周期

### 月度小审查（每月第一周）

**执行者**：王语嫣（自动化脚本 + 抽样人工复核）
**耗时**：0.5–1 人日
**范围**：
- 运行 `kcard-quality-gate.py`，生成当月报告
- 关注 P0 问题新增趋势
- 抽查 20 张上月新增/修改卡片
- 更新问题卡片跟踪看板

**输出**：
- `60_feedback/audit/kcard-quality-gate-report-YYYY-MM-DD.md`
- 看板更新

### 季度大审查（每季度首月）

**执行者**：王语嫣 + 相关领域 owner（老顽童/黄药师/欧阳锋）
**耗时**：2–3 人日
**范围**：
- 按 domain 或 author 选择一个重点方向深入审查
- 审查 50–100 张卡片
- 输出专项审查报告
- 修订 quality gate 规则（如有必要）

**输出**：
- `60_feedback/audit/kcard-stageX-<主题>-report-YYYY-MM-DD.md`
- 修订后的 `90_control/quality-gates/kcard.md`

---

## 审查流程

```
1. 运行门禁脚本
   python 90_control/scripts/kcard-quality-gate.py

2. 分析新增问题
   - 与上月报告 diff
   - 识别新增 P0 问题来源

3. 抽样人工审查
   - 从新入 enriched/reviewed/stable 的卡片中抽 20 张
   - 按 stage 2/3/4/5 的维度审查

4. 更新看板
   - 将新问题加入 P0/P1/P2 列表
   - 标记已修复项

5. 召开质量同步会（季度）
   - 汇报趋势
   - 分配修复任务
   - 修订规则
```

---

## 问题分级标准

| 级别 | 定义 | 处理时限 | 示例 |
|---|---|---|---|
| P0 | 阻塞性问题，卡片不应被使用或引用 | 当周 | source_refs 为空、YAML 错误、author=legacy 但 status=stable |
| P1 | 影响可信度，需要修复但不阻塞使用 | 当月 | confidence 虚高、trust_level 与内容不匹配、dangling 链接 |
| P2 | 优化项，提升可用性和检索效率 | 当季 | 空章节、格式问题、缺少 cross-link |

---

## 责任分配

| 角色 | 质量职责 |
|---|---|
| 老顽童 | 内容补全、OCR 校对、核心工具卡重写 |
| 黄药师 | 工具/schema 建设、source 映射、自动化脚本维护 |
| 欧阳锋 | 架构决策、quality gate 审批、复杂关系判定 |
| 王语嫣 | 运行审查、生成报告、跟踪问题、抽查验证 |
| 洪七公 | OCR/图像素材校对、视觉描述清理 |

---

## 门禁规则演进

- 每次大审查后可修订 `90_control/quality-gates/kcard.md`
- 修订需记录变更原因和生效日期
- 新规则优先应用于新卡片，旧卡按优先级逐步治理

---

## 关键指标

| 指标 | 当前基线（2026-06-15） | 目标 |
|---|---|---|
| P0 问题卡片数 | 1234 / 1339 | 季度下降 20% |
| P1 问题卡片数 | 444 / 1339 | 季度下降 15% |
| 完全干净卡片数 | 7 / 1339 | 季度增长 50% |
| YAML 解析错误 | 32 | 降至 0 |
| author=legacy 卡片数 | 待统计 | 降至 0 |

---

## 工具清单

| 工具 | 路径 | 用途 |
|---|---|---|
| 质量门禁脚本 | `90_control/scripts/kcard-quality-gate.py` | 全库扫描 P0/P1 问题 |
| 基线扫描脚本 | `90_control/scripts/audit-kcard-baseline.py` | 生成全库清单与基线报告 |
| YAML 修复脚本 | `90_control/scripts/fix-yaml-quote-issues.py` | 修复中文引号 YAML 错误 |
| 元数据修复脚本 | `90_control/scripts/fix-card-metadata.py` | 补全 id/author/reviewer 等 |
| 自检清单 | `90_control/quality-gates/kcard.md` | 卡片入库前逐项检查 |
| 问题看板 | `60_feedback/audit/kcard-issues-board.md` | 跟踪所有待修复问题 |
