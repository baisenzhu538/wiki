---
id: diag_20260622_战略域PPT视觉层重标
type: diagnosis_record
created_at: 2026-06-22
status: completed
author: 王语嫣（CLI）
audience: 欧阳锋 → 老顽童 / 黄药师 / 洪七公
source: 00_inbox/战略专题/冉鹏PPT截图/ (299张VLM + OCR)
---

# 诊断记录：冉鹏 PPT 视觉层第二轮重标——飞书王语嫣的重大遗漏

## 用户问题

老朱（欧阳锋）发现飞书王语嫣对冉鹏 PPT 视觉层的判断有误：

> "PPT 视觉层暂不独立建卡——Agent 检索的是文字，视觉信息融入已有卡即可"

实际翻看 PPT 截图后发现：97 张截图里藏着一套完整的 **IBM BLM 业务设计七要素** 操作框架——客户选择、价值主张、盈利模式、活动范围、战略控制点、风险管理、业务设计总结，以及战略能力金字塔、核心能力评估矩阵、麦肯锡 7S 等。这些在文字版（逐字稿+知识点）中根本没有完整展开，冉鹏在 PPT 讲义里用 30+ 张幻灯片细致展开每一要素的步骤、模板、检查清单。

## 诊断追问

1. **Q: PPT 视觉层到底有多少张？parse error 占比多少？**
   A: 299 张 VLM 描述，其中 **113 张标记为 parse error / 未识别**。但 CLI 深读后发现，这 113 张多数是 P-33 模式——外层 JSON 解析失败 fallback 为低置信度，内层 JSON 实际包含高质量描述（如 _98 内层 confidence 0.92，内容完整）。

2. **Q: 飞书王语嫣已经产出了什么？**
   A: Waves 1-5（38 张）基于 103 条知识点；Waves 6-8（21 张）基于逐字稿。两张 v2 标杆卡已由黄药师完成：`framework-strategy-business-design`（_97/_99）、`tool-strategy-customer-selection`（_97/_101）。

3. **Q: 漏掉的内容主要是哪些类型？**
   A: 三类：
   - 操作框架/模板（工作坊空白模板、检查清单、矩阵图）
   - 步骤详解（六步循环、价值捕获六步倒漏斗、盈利模式八问）
   - 跨页整合框架（现有 vs 期望业务设计、业务单元概要模板）

## 命中框架

| 框架 | 匹配理由 | 提供的视角 |
|:-----|:---------|:----------|
| IBM BLM 业务设计六要素×三步骤 | PPT _97/_99 是核心操作框架，不是概念名罗列 | 战略层业务设计有标准工作坊模板 |
| 客户选择六步循环迭代法 | PPT _101 有完整步骤和图标 | 已有 tool-strategy-customer-selection v2，但缺 _102/_103/_104 辅助矩阵 |
| 价值主张 5P2Q / 战略画布 | PPT _111/_112 是结构化工具 | 应独立成卡或并入 tool-strategy-value-proposition v2 |
| 价值捕获六步倒漏斗 | PPT _116 有从发散到收敛的完整流程 | 应并入 tool-strategy-value-capture v2 |
| 麦肯锡 7S 组织诊断 | PPT _128 用于风险管理前的组织匹配度评估 | 应并入 tool-strategy-risk-management v2 |
| Grace LaConte 风险矩阵 | PPT _129 是概率-影响四象限 | 可独立成卡 |
| 战略能力四层级金字塔 | PPT _30 格局/行动/决断/洞察 | 应独立成卡 |
| 核心能力评估矩阵（影响力×急迫性） | PPT _145 是 2×2 优先级矩阵 | 应独立成卡 |

## 关键判断

### 判断 1：飞书王语嫣的错误根因是工具链，不是能力

飞书 Hermes 无法批量扫描 299 个文件、无法逐页深读 VLM/OCR、无法跑 `kdo query` 全库检索、无法在 vault 里直接写任务文件。这导致她只能以"知识点摘要"为索引，看不到 PPT 视觉层 30+ 张幻灯片的结构化细节。

### 判断 2：PPT 视觉层不是"边角料"，而是"主菜"

冉鹏 30 年经验的操作精华——步骤、模板、检查清单、失败模式——大量存在于 PPT 讲义中，而非口述稿。文字稿只提了框架名，PPT 才把框架变成可执行的 Agent 指令。

### 判断 3：113 张 parse error 是"伪低质量"

P-33 模式复现：MiniMax-M3 返回的 JSON 中字符串值内部含未转义双引号（如 `标题为"AI 业务档案"`），导致 `json.loads` 失败，脚本 fallback 成 confidence=0.3 / 未识别。但内层 JSON 实际上高质量可用。这部分内容需要洪七公修复脚本后重跑，或人工读取内层 JSON 使用。

## 盲区 / Gap

1. **飞书王语嫣未扫描 PPT 讲义全量目录**——如果她先列出"这个文件夹里 299 张图分别是什么"，就不会把 30+ 张业务设计幻灯片误判为"无需独立建卡"。
2. **parse error 文件未人工复核**——直接以 VLM 外层置信度排除 113 张图，丢掉大量有效框架。
3. **战略能力金字塔（_30）和核心能力评估矩阵（_144/_145）完全未进入第一轮任务清单**——这两块在 PPT 后期章节，不在 103 条知识点里。
4. **"凯纳创新框架"未在 PPT 中找到**——可能是用户记忆偏差，或该框架在另一份素材中，需进一步确认。

## 应独立成卡 / 重点补强的 PPT 幻灯片清单

### 一、业务设计模块（Slides 97-132）—— 已部分覆盖，需大补

| 幻灯片 | 内容 | 建议动作 | 目标卡片 |
|:--|:--|:--|:--|
| _97 | 业务设计六要素 BLM 框架图 | ✅ 已入 `framework-strategy-business-design` v2 | — |
| _98 | 业务设计是迈向执行的关键：现有 vs 期望 + 四维评估 | **独立成卡** | `framework-strategy-business-design-execution-gap` 或并入 framework v3 |
| _99 | 六要素×三步骤工作坊空白模板 | ✅ 已入 framework v2 | — |
| _101 | 客户选择六步循环 | ✅ 已入 `tool-strategy-customer-selection` v2 | — |
| _102 | 市场规模 vs 品牌契合度矩阵 | 并入 customer-selection v2 或独立成 tool | `tool-strategy-customer-selection` v2+ |
| _104 | 场景-客群-产品矩阵（核心场景） | **独立成卡** | `tool-scenario-customer-product-matrix` |
| _107 | 价值主张三问 + 六维度 | 并入 value-proposition v2 | `tool-strategy-value-proposition` |
| _108 | 顾客需求金字塔（马斯洛） | **独立成卡** | `framework-maslow-customer-needs-strategy` |
| _109 | 价值主张维度表 | 并入 value-proposition v2 | `tool-strategy-value-proposition` |
| _110 | 价值主张排序与描述示例 | 并入 value-proposition v2 | `tool-strategy-value-proposition` |
| _111 | 顾客最关注的价值点（5P2Q 矩阵） | **独立成卡** | `tool-value-proposition-5p2q` |
| _112 | 战略画布 / 价值曲线 | **独立成卡** | `tool-strategy-canvas` |
| _113 | 差异化核心价值主张（Fresh/Free/Focus） | **独立成卡** | `tool-differentiated-value-proposition` |
| _115 | 价值获取八问 | 并入 value-capture v2 | `tool-strategy-value-capture` |
| _116 | 价值捕获六步倒漏斗 | 并入 value-capture v2 | `tool-strategy-value-capture` |
| _117 | 盈利模式示例（直营/加盟对比） | **独立成卡** 或并入 value-capture v2 | `case-profit-model-comparison` / `tool-strategy-value-capture` |
| _118 | 真壁垒 vs 伪壁垒 | **独立成卡** | `concept-moat-real-vs-fake` 或并入 control-points v2 |
| _120 | 活动范围核心问题 | 并入 activity-scope v2 | `tool-strategy-activity-scope` |
| _121 | 活动范围对比矩阵（零售商 A/B/C） | 并入 activity-scope v2 | `tool-strategy-activity-scope` |
| _123 | 战略控制点思考问题 | 并入 control-points v2 | `tool-strategy-control-points` |
| _124 | 价值定位模型 + 战略控制点表 | 并入 control-points v2 | `tool-strategy-control-points` |
| _125 | 战略控制点示例 | 并入 control-points v2 | `tool-strategy-control-points` |
| _127 | 风险识别与评估四步闭环 | 并入 risk-management v2 | `tool-strategy-risk-management` |
| _128 | 麦肯锡 7S 模型 | 并入 risk-management v2 | `tool-strategy-risk-management` |
| _129 | Grace LaConte 风险矩阵 | **独立成卡** | `tool-risk-laconte-matrix` |
| _131 | 业务设计结果示例 | 作为 case | `case-business-design-example` |
| _132 | 业务单元业务设计概要模板 | **独立成卡** | `tool-business-unit-design-template` |

### 二、战略能力模块（Slides 30 + 144-145）—— 全新发现

| 幻灯片 | 内容 | 建议动作 | 目标卡片 |
|:--|:--|:--|:--|
| _30 | 战略能力四层级金字塔：格局/行动/决断/洞察 | **独立成卡** | `framework-strategic-capability-pyramid` |
| _144 | 支撑战略目标所需打造的全部核心能力（7 大模块） | **独立成卡** | `framework-core-capability-map` |
| _145 | 核心能力评估矩阵（影响力×急迫性） | **独立成卡** | `tool-core-capability-prioritization-matrix` |

### 三、其他高价值但需确认优先级的框架

- _71 市场定位框架（GE/McKinsey 矩阵简化版）
- _80 关键成功要素分析对比表
- _86 SWOT 本质逻辑图
- _93 产品矩阵（核心/获客/增利/补充 × 生鲜/非生鲜）
- _246 三个地平线模型（短中长期业务管理）
- _260 突破型布局 / 击破边界

## 反馈建议

### 给老顽童

1. **按 v2 标准补完 5 张 tool 卡**，每张必须含：
   - 核心问题
   - 操作步骤（分步、可执行）
   - Agent 执行指令（Python 伪代码）
   - 失败模式表（≥3 种）
   - 具体 PPT VLM source_refs（精确到幻灯片编号）

2. **新增 8-10 张独立卡片**：
   - `framework-strategy-business-design-execution-gap`（_98）
   - `tool-scenario-customer-product-matrix`（_104）
   - `framework-maslow-customer-needs-strategy`（_108）
   - `tool-value-proposition-5p2q`（_111）
   - `tool-strategy-canvas`（_112）
   - `tool-differentiated-value-proposition`（_113）
   - `tool-risk-laconte-matrix`（_129）
   - `tool-business-unit-design-template`（_132）
   - `framework-strategic-capability-pyramid`（_30）
   - `framework-core-capability-map`（_144）
   - `tool-core-capability-prioritization-matrix`（_145）

3. **优先顺序**：先补完 5 张已有 tool 卡 v2 → 再新增业务设计相关卡 → 最后补战略能力金字塔/核心能力矩阵。

### 给黄药师

1. 修复 `describe-images-minimax.py` 的 P-33 问题（JSON 内嵌引号未转义），对 113 张 parse error 文件重跑或修复外层解析逻辑。
2. 提供批量读取 VLM 内层 JSON 的辅助脚本，避免老顽童人工读 113 个文件。
3. 更新 `scan-ppt-gaps.py` 概念词典，加入"战略能力金字塔""核心能力评估矩阵""Grace LaConte 矩阵"等新概念。

### 给洪七公

1. 对 113 张 parse error 的 PPT 截图补跑 OCR（如尚未跑），因为 VLM 描述即使修复也无法 100% 替代逐字 OCR。
2. 修复 VLM 描述汇总文件 `README-VLM描述汇总.md`，避免第二批覆盖第一批（P-32 模式）。

### 给欧阳锋

1. 确认新增卡片的优先级：建议 5 张 tool v2 为 P0，新增业务设计卡为 P1，战略能力金字塔/核心能力矩阵为 P1/P2。
2. 确认"凯纳创新框架"是否确实在本次 PPT 素材中——CLI 王语嫣未找到匹配内容。

## 置信度评估

- 业务设计六要素框架已在 PPT _97/_99 中被黄药师标杆卡验证：🔵 高置信度
- 113 张 parse error 内层 JSON 可人工读取并可用：🟡 存疑（需脚本修复后确认）
- 战略能力金字塔（_30）和核心能力评估矩阵（_145）为单一来源、无外部交叉验证：🟡 建议入库但标注"待外部验证"
- "凯纳创新框架"未找到：🔴 不确认

---

*CLI 王语嫣 · 2026-06-22 · 基于 299 张 VLM + OCR 逐页扫描*
*关联：60_feedback/tasks/task_20260621_战略域PPT补强_黄药师标杆.md*
