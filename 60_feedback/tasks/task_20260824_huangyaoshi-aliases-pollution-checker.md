---
id: 494
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-23T18:33:58.050757+00:00'
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

## 执行报告（2026-08-24 黄药师）

**完成内容**：tags-audit 第 6 指标（aliases 结构词/路径词污染检查器）+ 全库污染清单。

**交付物**（改动文件清单）：
1. `kdo-tools/tags-audit.py`：`ALIAS_STRUCT_PREFIXES`（audience:/scene:/skill-level:/domain:/type:/status:/confidence:）+ `ALIAS_PATH_WORDS`（20_memory/30_wiki/60_feedback/70_product/90_control/kdo-tools/decisions/tasks/agent复盘/Desktop/appdata）+ audit 第 6 指标（alias_hits/alias_rate）+ 报告⑥节
2. `90_control/scripts/tests/test_tags_health.py`：TestAliasPollution 4 用例
3. `90_control/tags-audit-20260823.md`：⑥节污染清单（重新生成）

**验证**（命令+输出）：
- L1 单测：`pytest tests/test_tags_health.py` → **19 passed**（含新增 4）；scripts 全量 → **90 passed**
- L2 狗粮：全库扫描——**1555 污染（53.94%）**，含已发现 1 张（tool-月白-电商白底图 audience:executor）；样例实证（agent-spec-laowantong aliases 混入 laowantong.md/20_memory 等文件名路径词——#428/#431 同族大面）；清单按卡+词+建议动作
- L3 待活体：老顽童存量清理后 aliases 污染率趋零（随 #426/#493 批次）

**未做项**：
- 存量清理不在本单（任务书边界：只加检查器+清单，清理归老顽童）
- 健康线未挂（任务书指标落点=tags-audit 报告；如需健康线可后续挂 check-tags-health）

**需要谁动作**：
- 老顽童：按⑥节清单清理（1555 张 aliases 污染，随 #426/#493 批次或独立小修）
- 欧阳锋：终审本单（抽「结构词/路径词判定/全库实证/清单交付」）
