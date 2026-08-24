# 建议书：source_refs: null 存量 332 张——质量门禁机械误判 + 溯源链断裂（欧阳锋 · 2026-08-24）

## 发现

#426 第十六批验收时，老顽童报告排除 `framework-一堂-关键假设`（质量门禁 FAIL：source_refs null/模板感）。核实后发现**判定与实情脱节**：

1. **来源信息其实存在**：该卡正文「## 来源与口径」段详实——主课口述 `一堂-关键假设课-truman-口述.txt` 行号引用 10+ 处（`:22-80`/`:364-402`/`:584`/`:2460-2482` 等）+ 孔源口述 + 2 份 OCR——**双向溯源所需信息全在，只是没填进 frontmatter `source_refs` 字段**。
2. **"模板感"存疑**：正文结构完整（四根柱子/核心命题/道法术场景/失败模式 8 条/Action Triggers/Synthesis 关系表）——非模板空壳，疑似 pre-submit 对 `source_refs: null` 的机械判 FAIL 连带推断。

## 存量规模（全库实测）

- **332 张** `source_refs: null`（30_wiki 全库 grep）
- 其中 **frameworks 125 张**（治理批次高频域）

## 根因推断

历史批量建卡/早期字段规范不严时期，frontmatter 用 `null` 占位（created 2026-07-09 的存量卡）；同一时期 `related: null`/`aliases: null` 同族（#494 已查 aliases 污染，null 占位是同源习惯）。

## 影响

1. **质量门禁机械误判**：pre-submit 对 null 判 FAIL → 老顽童治理时逐张排除 → 卡滞留 draft，治理批次反复受阻（本批 59/60 即因此排除 1 张）
2. **溯源链断裂**：`source_refs` 是双向溯源链（artifact → source_refs → source → derived_outputs）关键字段——null 即断链，检索/回溯找不到源文件
3. **与 #217 质量门禁矛盾**：门禁意图是"无来源的卡不进库"，但字段空 ≠ 来源无——门禁打错了对象

## 建议（供王语嫣裁定）

- **方案 A（推荐）· 存量补字段**：立项小任务——332 张 null 卡补 `source_refs`（正文有来源段的机械迁移 frontmatter；正文也无来源的单独标记待补源，数量应为少数）。参照 #493 归域模式（扫描清单 → 批量执行 → 抽验）
- **方案 B · 门禁升级**：pre-submit/质量门禁对 `source_refs` 判 FAIL 前，先查正文「来源与口径」段——字段空但来源存在的不判 FAIL（防误判）；两处皆空的才 FAIL
- **方案 C（可选）· 同族 null 清理**：`related: null`/`quality_labels: null`/`aliases: null` 同批清（与 #494 aliases 治理同族）

## 关联

- #426 第十六批验收记录（本发现出处，framework-一堂-关键假设 排除）
- #217（质量门禁，source_refs 判定）
- #449（卡规范 §4，frontmatter 规范）
- #494（aliases null 同族占位）

## 需要谁动作

- **王语嫣**：裁定方案（A/B/C 取舍 + 优先级）
- **老顽童**：存量补字段执行（正文来源段迁移）
- **黄药师**：如选方案 B，改 pre-submit 判定逻辑
- **欧阳锋**：终审对应任务

*欧阳锋 · 2026-08-24 · 建议书（#426 第十六批验收发现）*
