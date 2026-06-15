---
id: kimi-lean-startup-deep-review-2026-06-16
title: 精益创业域卡片深度复核报告
type: report
status: draft
domain:
- kdo-quality
author: kimi
reviewed_by: pending
confidence: 0.85
trust_level: medium-high
source_refs:
- src_20260616_b1e25c49
- src_20260616_7dc80216
- src_20260616_6c8b240b
created_at: '2026-06-16'
updated_at: '2026-06-16'
---

# 精益创业域卡片深度复核报告

## 复核背景

用户质疑老顽童产出的精益创业域卡片"深度不够"、"质量是否认真复核"、"是否真正理解精益创业"。此前第一次验收主要依赖 `kcard-quality-gate.py` 的形式化指标（P0=0, P1=0）和 frontmatter 完整性，**深度内容复核不足**。本报告为补救性深度复核。

## 复核方法

1. 重新读取源材料 `00_inbox/精益创业/` 下 5 份文件。
2. 深度抽查 4 张关键卡片：`yt-lean-essence`、`yt-lean-assumption-verification-3means`、`yt-lean-false-model-ai`、`yt-lean-daily-chemical-mvp`。
3. 将卡片内容与源材料逐段对照，检查概念准确性、边界清晰度、概念归属。
4. 检查卡片与通用精益创业（Lean Startup）知识的关系。

## 主要发现

### 1. 概念归属不清：把"一堂张磊版精益测试"写成了通用"精益创业"

**问题**：`yt-lean-essence.md` 标题为"精益创业的本质"，正文大量引用"一堂五步法"、"FALSE 模型"、"产品内核四要素"等一堂内部框架，但没有说明这是**一堂教练对精益测试的特定阐释**，而非 Eric Ries《精益创业》的通识。

**风险**：知识库用户搜索"精益创业"时，会拿到一个特定讲师、特定课程的方法论，误以为这是通用定义。

**修正**：已将标题改为"一堂张磊版精益测试的本质"，并在正文增加"定位说明"段落。

### 2. FALSE 模型英文全称是老顽童自己脑补的

**问题**：`yt-lean-false-model-ai.md` 中表格写明：

| 字母 | 英文关键词 |
|---|---|
| F | Face |
| A | Artificial |
| L | Leverage |
| S | Substitute |
| E | Earliest |

但源材料 Q2 原文仅说："F（直接测试）、A（人工服务）、L（借用工具）、S（人工替代）、E（最小版本）"，**并未给出每个字母的英文全称**。老顽童把推断出的英文当作事实写入卡片。

**风险**：容易让读者误以为英文来自本次 AMA。

**修正**：已恢复英文全称，但增加说明——英文关键词来自一堂课程内容，而非本次 AMA 口述。未来如补充一堂课程原文，可进一步把 source_refs 指向课程来源。

### 3. 缺少与经典精益创业的对话

**问题**：12 张卡片中没有任何一张提到 Eric Ries、《精益创业》、Build-Measure-Learn、Validated Learning、Pivot 等经典概念，也没有说明张磊方法与之的异同。

**风险**：知识库变成"一堂课程笔记库"，而不是与已有知识对话的"知识网络"。

**建议**：
- 在 `yt-lean-essence.md` 中增加"与经典精益创业的关系"小节；
- 在 `yt-lean-assumption-verification-3means.md` 中说明"三种验证手段"与 Steve Blank  customer discovery、Eric Ries validated learning 的对应关系；
- 未来老顽童写卡时，必须先用 `kdo query` 查 vault 中是否已有相关经典概念，再做关联或对比。

### 4. AI 降本"1/10"被过度确定化

**问题**：源材料中"成本降到 1/10"是张磊的定性经验表述，无数据支撑。卡片中多次将其作为核心结论呈现，虽然 confidence 0.75，但语气接近事实陈述。

**建议**：在每张涉及 AI 降本的卡片中，明确标注"1/10 为讲师经验性比例，非定量数据"，或改用"数量级下降"等更弱表述。

### 5. case 卡 diagnostic_signals 未填充

**问题**：3 张精益 case 卡（日化沐浴露、宝妈团长、美业门店）frontmatter 中 `diagnostic_signals` 为空。按 ingestion-pipeline 规则，case 卡建议有 diagnostic_signals。

**风险**：case 卡的使用价值降低，无法作为诊断工具被调用。

**建议**：老顽童为 3 张 case 卡补充 diagnostic_signals（可参考 `yt-lean-daily-chemical-mvp.md` 已填充的 3 条，另外两张也需补充）。

### 6. 两张非精益域 case 卡混入本次产出

**问题**：`case-hr-saas-feature-usage-trap.md` 和 `case-toc-content-platform-correlation-trap.md` 与精益创业域无关，但出现在本次 git 新增中，且 diagnostic_signals 为空。

**建议**：确认这两张卡是否属于其他任务；如属于本次老顽童工作，补充 diagnostic_signals。

## 对"老顽童是否理解精益创业"的判断

| 维度 | 评估 |
|---|---|
| 张磊 AMA 核心方法论 | ✅ 理解准确：关键假设、三种验证手段、FALSE 模型、五步法、AI 加速 |
| 精益创业通用知识 | ⚠️ 边界不清：未区分一堂版本与经典精益创业 |
| 知识卡片写作规范 | ⚠️ 形式合规但深度不足：有 frontmatter、有案例、有 checklist，但概念归属和学术边界处理不够严谨 |
| 源材料忠实度 | ⚠️ 基本忠实，但存在来源边界不清（FALSE 英文）和过度确定化（1/10） |
| 与已有知识库对话 | ❌ 不足：未关联 Eric Ries、Steve Blank 等经典，未查询 vault 已有覆盖 |

**总体判断**：老顽童理解了**张磊所讲的精益测试**，但还没有把这份理解放到更广阔的"精益创业"知识谱系中去定位。产出的卡片更像是"高质量的课程笔记"，而不是"可与通用知识对话的独立知识卡"。

## 已完成的修正

1. `30_wiki/concepts/yt-lean-essence.md`
   - 标题改为"一堂张磊版精益测试的本质"
   - 增加"定位说明"段落
2. `30_wiki/frameworks/yt-lean-false-model-ai.md`
   - 标题改为"一堂精益小抄 FALSE 模型..."
   - 增加"说明"段落，注明英文全称来自一堂课程内容，非本次 AMA 口述
   - 恢复英文全称表格

## 仍需老顽童返工的任务

### 高优先级

1. **为 3 张精益 case 卡补充 diagnostic_signals**
   - `cases/yt-lean-daily-chemical-mvp.md`（已有，检查是否需要优化）
   - `cases/yt-lean-flower-mom-group-leader.md`
   - `cases/yt-lean-beauty-store-conversion.md`

2. **在 `yt-lean-essence.md` 增加"与经典精益创业的关系"小节**
   - 提及 Eric Ries《The Lean Startup》、Build-Measure-Learn、Validated Learning
   - 说明张磊版本与经典版本的 2-3 个关键异同

3. **在 `yt-lean-assumption-verification-3means.md` 增加知识谱系定位**
   - 说明"访谈调研"与 Steve Blank customer discovery 的关系
   - 说明"实验验证"与 Eric Ries validated learning / MVP 的关系

### 中优先级

4. **检查所有英文缩写/模型名称**
   - 确认源材料是否明确给出全称
   - 没有明确依据的，必须标注"辅助记忆"或"非官方命名"

5. **弱化"1/10"表述**
   - 在 `yt-lean-false-model-ai.md` 等处增加"经验性比例，非定量数据"标注

6. **查询 vault 已有覆盖**
   - 用 `kdo query "精益创业"`、`kdo query "MVP"`、`kdo query "假设验证"` 查已有卡片
   - 在相关字段中补充 `related` 链接

## 验收标准

返工完成后，本报告中的 6 项"主要发现"至少解决 1-5 项（第 6 项视任务归属而定），方可宣布精益创业域卡片进入稳定状态。

## 关联文件

- `60_feedback/quality-gate/精益创业-入口质量门-2026-06-16.md`
- `70_product/tasks/laowantong-next-tasks.md` §十五
- `30_wiki/concepts/yt-lean-essence.md`
- `30_wiki/frameworks/yt-lean-false-model-ai.md`
