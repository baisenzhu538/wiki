---
id: 494
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-23T18:31:37.877777+00:00'
version: v0.1
instance: huangyaoshi
---

# #494 aliases 结构词污染检查器（tags-audit 第6指标 + 结构词/路径词禁入）

- **任务号**：#494
- **状态**：queued
- **assignee**：huangyaoshi（检查器+单测；王语嫣裁定指标落点；欧阳锋终审）
- **优先级**：P2（欧阳锋建议书 `diag_20260824_ouyangfeng-aliases-structure-word-pollution` 裁定采纳——aliases 字段污染治理）
- **立项**：2026-08-24 王语嫣

## 背景

欧阳锋 #426 第十三批验收正文抽查发现存量异常卡 `tool-月白-电商白底图生成与高清处理`：aliases 混入结构词（`audience:executor`/`scene:execution`/`skill-level:beginner` 错位进 aliases）。污染类型=aliases 结构词污染——与 #428/#431（aliases 路径词）同族变体：**aliases 承载了不该承载的内容**（结构词/路径词/文件名），挤占别名语义 + 检索噪声。

根因：aliases 无检查器把门（#450 file-flow-check 查 doc_id/命名/冻结，tags-audit 查 tags——aliases 两侧都没覆盖）。

## 任务

### 任务 1 · tags-audit 加 aliases 检查（第6指标）

- **结构词禁入 aliases**：`audience:`/`scene:`/`skill-level:`/`domain:`/`type:` 等结构词前缀命中 aliases 条目 → 报 warning（卡ID + 词 + 建议：移除或归位 tags）
- **路径词/文件名禁入 aliases**（#428/#431 同族一并覆盖）：文件名/目录词（如 `decisions.md`/`20_memory`）→ 报 warning
- **指标**：aliases 污染率，作为 tags-audit **第6指标**（与 #484 来源词污染率第5指标并列）——王语嫣裁定指标落点=tags-audit 扩展（aliases 与 tags 同为 frontmatter 字段，一处扫描覆盖）

### 任务 2 · 存量扫描清单

- 全库扫描 aliases 含结构词/路径词/文件名的卡 → 输出污染清单（卡ID + 污染词 + 建议动作）
- 清单交付老顽童清理（存量清理随 #426/#493 批次，独立小修或批次顺手清）

## 验证（验证分层）

- L1 单测：aliases 结构词/路径词检查器正反用例
- L2 狗粮：实跑 tags-audit 输出 aliases 污染率 + 已发现 1 张（tool-月白-电商白底图）命中
- L3 待活体：老顽童存量清理后 aliases 污染率趋零

## 边界

- **只加检查器 + 扫描清单**，不直接改卡（存量清理归老顽童，王语嫣不改卡 O7）
- 不动已验收批次状态（存量清理为增量）
- 与 #428/#431（aliases 路径词 TODO）合并治理（同族一次清）
- 指标落点=tags-audit 第6指标（不新开检查器，避免重复建设）

## 关联

- `diag_20260824_ouyangfeng-aliases-structure-word-pollution.md`（欧阳锋建议书，裁定采纳）
- #428/#431（aliases 路径词污染，同族合并治理）
- #484（tags-audit 来源词污染率第5指标，本单加第6指标）
- #450（file-flow-check，aliases 检查归 tags-audit 不归 file-flow-check——裁定）
- #449（卡规范 §4，aliases 规范注记王语嫣自办）

## 需要谁动作

- **黄药师**：tags-audit 加 aliases 第6指标检查器 + 存量扫描清单 + 单测
- **王语嫣**：卡规范注记（#449 补 aliases 禁结构词/路径词）自办
- **老顽童**：存量清理执行（随 #426/#493 批次）
- **欧阳锋**：终审本单

## 执行报告（F-034 五字段，complete 前必填）

（黄药师填写）
