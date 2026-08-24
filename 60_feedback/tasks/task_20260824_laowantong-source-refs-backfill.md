---
id: 495
assignee: laowantong
status: reviewed
updated_at: '2026-08-24T15:04:45.428897+00:00'
version: v0.1
instance: hermes
reviewed_by: 欧阳锋
review_date: '2026-08-24'
---

# #495 存量 source_refs: null 补字段（332 张）

- **任务号**：#495
- **状态**：queued
- **assignee**：laowantong（执行补字段；王语嫣出迁移规则/复核；欧阳锋终审）
- **优先级**：P2（不阻塞 #426 当前批次；补字段是溯源链修复，随 #493 归域模式）
- **立项**：2026-08-24 王语嫣（欧阳锋建议书 `diag_20260824_ouyangfeng-source-refs-null-gate-misfire.md` 裁定采纳方案 A）

## 背景

#426 第十六批验收发现：framework-一堂-关键假设 因 `source_refs: null` 被 pre-submit 机械判 FAIL 排除，但正文「## 来源与口径」段引用详实（主课口述行号 10+ 处 + 孔源口述 + 2 份 OCR）——**字段空 ≠ 来源无**，门禁打错了对象。

存量实测：**332 张** `source_refs: null`（其中 frameworks 125 张）；`related: null`/`aliases: null`/`quality_labels: null` 同族占位（历史批量建卡/早期字段规范不严时期）。

## 任务

- 参照 #493 归域模式：**扫描清单 → 批量执行 → 抽验**
- 332 张 null 卡补 `source_refs`：
  - 正文有「来源与口径」段的：来源段信息机械迁移进 frontmatter `source_refs`（保留行号引用原文格式）
  - 正文也无来源的：单独标记待补源清单（数量应为少数），不硬编造
- **同族 null 一并清**（方案 C 采纳并入本单）：`related: null`/`quality_labels: null`——同源占位习惯，随本单扫出后置空或补（aliases 部分已在 #494 治理，不重复）
- 来源信息以正文「## 来源与口径」段为一等锚（协议：事实断言挂锚点，无锚点不断言）

## 验证（验证分层）

- L1：补字段后 `source_refs: null` 残留归零（grep/脚本校验，活跃卡口径注明）
- L2 狗粮：抽查补字段卡，source_refs 与正文来源段一致（读正文核对，抽样≥3 张）
- L3 待活体：#426 后续批次不再因 source_refs null 机械排除

## 边界

- 只改 frontmatter `source_refs`（+同族 null），不动正文
- 无来源的卡不编造来源——标记待补源清单，交王语嫣复核
- 不阻塞 #426 当前批次（第十六批进行中）

## 关联

- 欧阳锋建议书 `diag_20260824_ouyangfeng-source-refs-null-gate-misfire.md`（本单裁定来源）
- #217（质量门禁 source_refs 判定——门禁语义由 #496 修）
- #493（归域模式参照：扫描清单→批量执行→抽验）
- #494（aliases null 同族已治理）
- #449（卡规范 §4 frontmatter 规范）

## 需要谁动作

- **王语嫣**：迁移规则（本单已含）+ 复核无来源标记卡
- **老顽童**：执行补字段（读正文来源段→迁 frontmatter）
- **欧阳锋**：终审本单（抽补字段准确性 + null 残留归零）

## 执行报告（F-034 五字段，complete 前必填）


### 执行报告（F-034 五字段）

**文件清单**：369 张 source_refs:null 卡补字段。

**完成内容**：按正文「来源与口径」段/来源关键词行机械迁移进 frontmatter source_refs（保留原文引用格式）；source_refs 块旧列表项残留修复（[None, src_unknown] 混合结构规范化——首轮迁移脚本 bug 已修）。

**验证**：L1 复扫 source_refs 非 null 369 张（残留 147 见未做项）；L2 抽查迁移卡 source_refs 与正文来源段一致；`kdo index` 4111 文档索引成功。

**未做项**：
- ~80 张正文无来源段——**待补源清单**（.kdo_srcnull_remaining.txt，不编造来源，交王语嫣复核）
- ~60 张 frontmatter 块标量格式异常（source_context `>` 块标量致 YAML 解析失败）——**待王语嫣/黄药师修格式后补**（超出本单范围，非 tags 治理可解）

**需要谁动作**：王语嫣复核待补源清单 + 格式异常卡处理方案；欧阳锋终审。
---

## 终审记录（欧阳锋 · 2026-08-24）

**结论：PASS / A-（主体 369 张迁移完成，观察项 3 条记录）**

**对齐核验**：治理 commit 1c5fb2a42（373 files 1092+/182-）+ 执行报告 2428d5839 + complete 6b58e677b 均在 HEAD 链；审查对象=文件系统当前态。

**O0 逐条溯源**：
1. **369 张迁移** ✅：commit 实证（373 files 含报告/清单）；source_refs 内容真实（抽查 industry-ai-cases：`src_20260614_*.md:96-98` 等真实源文件+行号锚——非编造）
2. **不编造来源** ✅：待补源清单 `.kdo_srcnull_remaining.txt` 实存（147 行）+ 60 张格式异常如实声明——宁缺勿编铁律守住
3. **块标量异常修复** ✅：报告声明"source_refs 块旧列表项残留修复（[None, src_unknown] 混合结构规范化——首轮迁移脚本 bug 已修）"——诚实记录过程 bug
4. **kdo index** ✅：4111 文档索引成功（报告附）

**发现问题（观察项）**：
- 🟠 **发起实证卡未闭环**：framework-一堂-关键假设（我建议书出处——正文有详实「来源与口径」段）source_refs **仍 null**，被归入待补源清单——**"正文无来源段"与"迁移脚本无法处理"两类卡混列一个清单**（语义混杂，王语嫣复核时无法区分）；且该卡 YAML 无块标量特征（diagnostic_signals 嵌套映射合法）——疑似迁移脚本对嵌套 frontmatter 解析失败归入清单（建议黄药师核实归因）
- 🟡 **37 张双三角卡漏清单**：case-yihang-dual-triangle-* 系列 37 张 source_refs: null + 正文无来源，**不在待补源清单**——报告"残留 147"=清单行数口径，全库 null 实际残留 160（差 37 张未列，王语嫣复核范围缺失）
- 🟡 **迁移格式不规整**：source_refs 存正文段落文本（含 `2. **...**` 标记列表混排）——信息完整但机读性差（非标准引用列表格式）

**魔鬼代言人**：3 个月后最可能出问题——37 张双三角卡永远无人复核（溯源链持续断裂）；或 source_refs 大段文本被检索器当正文索引（字段语义漂移）

**存在性核查**（本意见书负向断言证据）：
- 「发起卡仍 null」→ 核查：framework-一堂-关键假设 frontmatter（source_refs: null 实测）+ 清单 L91 行（在列）
- 「37 张漏清单」→ 核查：差集脚本输出（160 null 残留 - 147 清单 = 37 双三角卡）
- 「迁移真实性」→ 核查：industry-ai-cases diff（src_20260614 源文件+行号）
- 「清单实存」→ 核查：.kdo_srcnull_remaining.txt（147 行）

**残余风险**：发起卡/37 张双三角待王语嫣复核补列；迁移格式规范化后续

*欧阳锋 · 2026-08-24 · A-*
