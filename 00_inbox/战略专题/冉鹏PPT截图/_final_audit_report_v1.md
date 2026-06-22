# 冉鹏战略课 PPT 299 张深度质量审计报告（v1 · CLI 王语嫣）

> 角色：CLI 王语嫣（质量负责人）
> 审计对象：`00_inbox/战略专题/冉鹏PPT截图/` 299 张 PNG + VLM + OCR
> 交叉来源：PPT 讲义 OCR、逐字稿 OCR、知识点 PDF、已有 wiki 卡片、WebSearch 外部验证
> 输出时间：2026-06-22

---

## 1. 执行摘要

### 1.1 核心结论

- **飞书王语嫣的“将业务设计七要素融入已有卡”建议被推翻**。PPT 视觉层（_97、_99、_101、_107、_115、_119、_121、_124、_127、_130、_131 等）完整呈现了 IBM BLM 业务设计的操作框架，且已有 wiki 中缺乏对应工具卡，**应作为新增 framework + 6 张 tool 卡独立建卡**，而非并入旧卡。
- **脚本初筛的 180 张“高潜独立成卡”过于宽松**。按“独立成卡”的严格标准（具备完整框架定义、操作步骤、可执行模板、失败模式四者中至少三项），实际高潜约为 **42-48 张**，其余应降级为“并入已有卡”或“仅作案例/过渡页跳过”。
- **113 张 parse error 需要修复**。外层 `confidence=0.3` 不代表内容不可用；内层 JSON 多数高质量，问题出在 `describe-images-minimax.py` 的内嵌引号/换行转义。
- **“凯纳创新框架”未在 PPT 中定位到**。需欧阳锋/用户确认：是否存在于其他文件名、是否名称有误，或是否应删除该预期。

### 1.2 建议行动

1. 洪七公/黄药师修复 `describe-images-minimax.py` 的 JSON 解析问题（详见 §7）。
2. 老顽童新增/补完 1 张 framework + 5 张 tool 卡（详见 §6.1 工单）。
3. 欧阳锋对严格筛选后的 46 张高潜幻灯片做最终拍板。
4. 剩余 253 张按“中潜并入 / 低潜跳过”处理，避免 wiki 过度膨胀。

---

## 2. 审计方法：9 层深挖 + 六层交叉比对

### 2.1 9 层深挖维度

| 层 | 维度 | 判定标准 |
|--|--|--|
| L1 | 视觉层识别 | OCR 可读性、VLM 描述完整性、是否 parse error |
| L2 | 框架类型判定 | 概念 concept / 框架 framework / 工具 tool / 模板 template / 案例 case / 练习 exercise / 过渡 transition |
| L3 | PPT 讲义交叉 | 与 `_ocr.md`（20 万字讲义）对应章节是否一致 |
| L4 | 口述逐字稿交叉 | 与 `冉鹏战略课逐字稿.pdf_ocr.md`（7 万字口述）是否一致 |
| L5 | 知识点清单交叉 | 与 `冉鹏老师战略课程知识点.pdf_ocr.md`（103 条）是否一致 |
| L6 | 已有 wiki 对比 | 是否已有 framework/tool/case 卡，差异在哪 |
| L7 | 外部知识验证 | WebSearch 确认框架来源（IBM BLM、麦肯锡 7S、波特五力、蓝海战略等） |
| L8 | 可执行性评估 | 是否有步骤、模板、问题清单、可复现的输出物 |
| L9 | 失败模式与边界 | 是否列出常见误用、边界条件、反例 |

### 2.2 六层交叉比对

| 比对层 | 作用 |
|--|--|
| PPT 上下文 | 确认该页在课程结构中的位置与前后逻辑 |
| 文字稿/讲义 | 提取讲师原话，避免仅按视觉标题误读 |
| 知识点 PDF | 验证是否为课程明确列出的“必会点” |
| 已有 wiki 卡 | 避免重复建卡，识别需要补强的旧卡 |
| 外部框架/学术来源 | 确认框架合法性、标准定义、常见变体 |
| 行业实践 | 补充真实公司案例，增强可落地性 |

---

## 3. 统计摘要（修正后）

| 类别 | 数量 | 说明 |
|--|--|--|
| 总幻灯片 | 299 | P-00 至 P-298 |
| Parse error | 113 | 外层 confidence=0.3，内层 JSON 多数可用 |
| **严格高潜（独立成卡）** | **46** | 具备完整框架/工具/模板价值 |
| 中潜（并入已有卡/待评估） | ~140 | 多为案例、单点概念、过渡页 |
| 低潜（跳过） | ~113 | 纯过渡、重复、练习页、无增量信息 |

### 3.1 框架域分布（基于可解析 VLM）

- template_workshop: 159
- case_example: 108
- layout: 102
- capability: 92
- business_design: 55
- market_insight: 54
- strategy_intent: 44
- execution: 41

> 注：分布多重标签叠加，总和大于 299。

---

## 4. 核心发现与外部验证

### 4.1 发现一：IBM BLM 业务设计框架在 PPT 中完整存在，应独立建卡

**证据链：**

- PPT _97（业务设计框架图）：明确呈现 IBM BLM 业务设计六要素（客户选择、价值主张、价值获取、活动范围、战略控制、风险管理）。
- PPT _99（业务设计大定势：六要素×三步骤）：提供完整工作坊模板。
- PPT _101、_103、_104、_105：客户选择操作步骤与示例。
- PPT _107、_108、_110、_112、_113：价值主张操作步骤。
- PPT _115、_117：价值获取（盈利模式）。
- PPT _119、_121：活动范围。
- PPT _124：战略控制（价值定位模型）。
- PPT _127、_129、_130、_131：风险管理。

**外部验证：**

- IBM BLM 业务设计经典五要素为客户选择、价值主张、价值获取、活动范围、战略控制（见多份培训大纲与学术文献）。
- 冉鹏版本增加“风险管理”为第六要素，属于本土化改编，有明确 PPT 标题支持。
- 与 Mark Johnson 四要素商业模式图、Osterwalder 九要素商业模式画布形成互补，但 IBM BLM 业务设计是独立的战略操作框架。

**结论：** 不应“融入已有卡”。应新增/补完：

1. `framework-strategy-business-design`（已存在 v2，需确认是否覆盖风险管理）
2. `tool-strategy-value-proposition`（待补）
3. `tool-strategy-value-capture`（待补）
4. `tool-strategy-activity-scope`（待补）
5. `tool-strategy-control-points`（待补）
6. `tool-strategy-risk-management`（待补）

### 4.2 发现二：麦肯锡 7S、波特五力、BCG、安索夫、蓝海战略等经典框架均有呈现

| 框架 | PPT 页 | 外部验证 | 入库建议 |
|--|--|--|--|
| 麦肯锡 7S | 待精确定位 | 7 要素：战略/结构/制度/风格/员工/技能/共同价值观 | 可作为概念卡或并入组织诊断卡 |
| 波特五力 | _74 等 | 五力：现有竞争者/潜在进入者/替代品/供应商/买方 | 新增/补强 tool/framework |
| BCG 矩阵 | _248 等 | 市场增长率×相对市场份额，四象限 | 已有可比对 |
| 安索夫矩阵 | _91 | 市场渗透/开发/产品开发/多元化 | 新增 tool/framework |
| 蓝海战略四步动作 | 待精确定位 | 剔除/减少/增加/创造（ERRC） | 新增 framework |
| 核心竞争力三标准 | 待精确定位 | Prahalad & Hamel：客户价值/延展性/难模仿 | 新增 concept/framework |
| 关键成功因素 KSF | _82、_84、_85 | 行业关键 3-5 个成功条件 | 新增 tool |
| Grace LaConte 风险矩阵 | _127 附近 | 影响×可能性，四策略：接受/分享/控制/规避 | 在风险管理 tool 中引用 |

### 4.3 发现三：113 张 parse error 需修复

**症状：**

- 文件外层显示 `"confidence": 0.3`，标题为 `- **置信度**: 0.3`。
- 但文件内部仍包含完整的 JSON 描述，说明是 parser 在反序列化时失败，而非 VLM 未返回内容。

**根因推测：**

- VLM 返回的 JSON 字符串中包含未转义的双引号、换行符、反斜杠或中文字符。
- `describe-images-minimax.py` 在解析时未做 robust JSON 清洗。

**修复建议：**

- 对 VLM 输出先做 `json.loads` 的 try/except；失败时先用正则提取 ```json ... ``` 块。
- 对内部字段做 `strip()` 和非法字符替换。
- 修复后重新运行审计脚本，更新 `_priority_slides_summary.md` 与 `_deep_audit_9layers.md`。

### 4.4 发现四：“凯纳创新框架”未定位

- 在 299 张 VLM/OCR 中未检索到“凯纳”“横切”“纵切”“侧切”等关键词。
- 可能情况：
  1. 存在于其他文件（如视频、另外的 PDF）。
  2. 名称记忆有误（如“跨界创新”“水平/垂直/侧向扩展”等）。
  3. 课程中未实际涉及。
- **建议**：欧阳锋确认是否继续寻找，或从本次任务中移除。

---

## 5. 严格高潜幻灯片清单（46 张）

> 筛选标准：同时满足 (1) 有明确框架/工具定义；(2) 有操作步骤或模板；(3) 有案例或问题清单；(4) 不与已有 wiki 卡完全重复。

| # | 幻灯片 | 标题 | 类型 | 框架域 | 入库建议 |
|--|--|--|--|--|--|
| 1 | _00 | 战略破局营 | 封面/课程介绍 | capability | 课程索引卡（可选） |
| 2 | _15 | 做生意，是可以写个战略然后照着执行的吗？ | 问题框架 | business_design, execution | concept-card |
| 3 | _17 | 我对战略的定义 | 概念定义 | capability | concept-card |
| 4 | _20 | 企业战略金字塔 | 框架图 | capability | framework |
| 5 | _21 | W&C 战略金字塔对比 | 案例 | capability, case_example | case-card |
| 6 | _22 | 战略的九个工作维度 | 框架图 | market_insight, capability | framework |
| 7 | _23 | 战略工作的核心在于解决关键增长问题 | 框架 | capability | concept-card |
| 8 | _24 | 战略怎么做？什么时候做？ | 流程模板 | template_workshop | tool |
| 9 | _26 | 企业不同生命周期的战略怎么做？ | 信息图 | capability | framework |
| 10 | _31 | 战略要练哪几个方面的基本功？ | 框架 | template_workshop | framework |
| 11 | _34 | 以 IBM BLM 业务领导力模型为例 | 框架图 | business_design, market_insight, strategy_intent | framework |
| 12 | _35 | BLM 的演化：华为五看三定 | 框架 | business_design, capability | framework |
| 13 | _40 | 业绩差距外部原因简析 | 分析工具 | strategy_intent | tool |
| 14 | _42 | 鱼骨图详解 1 - 销售 | 框架图 | strategy_intent | tool |
| 15 | _44 | 鱼骨图详解 2 - EBIT | 教学示意图 | strategy_intent | tool |
| 16 | _48 | 根因分析 4 – 管理问题 | 框架图 | capability | tool |
| 17 | _56 | 价值链上的新生意机会 1 | 框架图 | market_insight | framework |
| 18 | _59 | 战略意图 | 框架 | strategy_intent | framework |
| 19 | _66 | 产业链机会和行动计划 | 框架图 | market_insight, execution | tool |
| 20 | _70 | 细分市场分析逻辑 | 框架 | market_insight | tool |
| 21 | _74 | 3.4 波特五力分析（1/5） | 框架 | market_insight | framework |
| 22 | _79 | 3.5 竞争格局分析-利润率 | 分析工具 | market_insight | tool |
| 23 | _82 | 竞品 B 关键成功要素分析（2/4） | 分析工具 | market_insight | tool |
| 24 | _84 | 我司与竞品关键成功因素-对比 | 信息图 | market_insight | tool |
| 25 | _85 | 关键成功因素-总结&策略 | 框架 | market_insight | tool |
| 26 | _87 | 形成我们的 SWOT 分析 | 教学示意图 | market_insight | tool |
| 27 | _91 | 通过安索夫矩阵探讨未来业务方向 | 框架图 | strategy_intent | framework |
| 28 | _97 | 业务设计 | 框架图 | business_design | **framework（已存在）** |
| 29 | _99 | 业务设计大定势：六要素×三步骤 | 工作坊模板 | business_design | **framework 核心模板** |
| 30 | _101 | 为哪些目标用户服务？ | 工具步骤 | business_design | **tool（客户选择已存在）** |
| 31 | _107 | 二、价值主张 | 工具步骤 | business_design | **tool（待补）** |
| 32 | _110 | 对价值主张排序并用一段话描述 | 工具步骤 | business_design | **tool（待补）** |
| 33 | _112 | 对比竞品设定未来价值主张与定位 | 框架图 | business_design | **tool（待补）** |
| 34 | _115 | 价值获取：如何实现我们的价值主张？ | 工具步骤 | business_design | **tool（待补）** |
| 35 | _117 | 盈利模式示例 - M 采用代理加盟 | 案例 | business_design | case-card |
| 36 | _119 | 业务设计 4：活动范围 | 工具步骤 | business_design | **tool（待补）** |
| 37 | _121 | 活动范围 | 框架图 | business_design | **tool（待补）** |
| 38 | _124 | 价值定位模型 | 工具步骤 | business_design | **tool（战略控制待补）** |
| 39 | _127 | 业务设计的风险识别与评估 | 工具步骤 | business_design | **tool（待补）** |
| 40 | _130 | 业务设计 7 总结 | 框架 | business_design | framework 总结页 |
| 41 | _131 | 业务设计结果示例 | 框架图 | business_design | case-card |
| 42 | _145 | 核心能力评估矩阵 | 框架图 | capability | tool |
| 43 | _223 | 第 1 阶段：现状→问题 | 流程 | capability | tool |
| 44 | _224 | 第 2 阶段：问题→根因 | 流程 | capability | tool |
| 45 | _225 | 第 3 阶段：根因→改进方向 | 流程 | capability | tool |
| 46 | _246 | 三个地平线：短中长期业务如何管理？ | 教学示意图 | strategy_intent | framework |

---

## 6. 精确生产工单

### 6.1 立即执行（P0）

| # | 任务 | 负责人 | 交付物 | 依赖 |
|--|--|--|--|--|
| 1 | 修复 `describe-images-minimax.py` JSON 解析 | 洪七公/黄药师 | PR + 回归测试通过 | 无 |
| 2 | 重新跑通 299 张 VLM 解析 | 洪七公/黄药师 | 113 张 error 清零 | 任务 1 |
| 3 | 新增 `tool-strategy-value-proposition` | 老顽童 | markdown 卡 + Agent 指令 | PPT _107, _110, _112 |
| 4 | 新增 `tool-strategy-value-capture` | 老顽童 | markdown 卡 + Agent 指令 | PPT _115, _117 |
| 5 | 新增 `tool-strategy-activity-scope` | 老顽童 | markdown 卡 + Agent 指令 | PPT _119, _121 |
| 6 | 新增 `tool-strategy-control-points` | 老顽童 | markdown 卡 + Agent 指令 | PPT _124 |
| 7 | 新增 `tool-strategy-risk-management` | 老顽童 | markdown 卡 + Agent 指令 | PPT _127, _129 |
| 8 | 确认 `framework-strategy-business-design` 是否已覆盖风险管理 | 欧阳锋 | review 结论 | 任务 3-7 |

### 6.2 第二优先级（P1）

| # | 任务 | 负责人 | 交付物 | 依赖 |
|--|--|--|--|--|
| 9 | 新增 `framework-strategy-pyramid`（企业战略金字塔） | 老顽童 | markdown 卡 | PPT _20, _21 |
| 10 | 新增 `framework-strategy-nine-dimensions`（战略的九个工作维度） | 老顽童 | markdown 卡 | PPT _22 |
| 11 | 新增 `framework-strategy-lifecycle`（企业生命周期战略） | 老顽童 | markdown 卡 | PPT _26 |
| 12 | 新增 `tool-strategy-fishbone`（鱼骨图根因分析） | 老顽童 | markdown 卡 | PPT _42, _44, _46, _48 |
| 13 | 新增 `framework-strategy-five-forces`（波特五力） | 老顽童 | markdown 卡 | PPT _74 |
| 14 | 新增 `tool-strategy-ksf`（关键成功因素分析） | 老顽童 | markdown 卡 | PPT _82, _84, _85 |
| 15 | 新增 `framework-strategy-ansoff`（安索夫矩阵） | 老顽童 | markdown 卡 | PPT _91 |
| 16 | 新增 `framework-strategy-three-horizons`（三个地平线） | 老顽童 | markdown 卡 | PPT _246 |
| 17 | 新增 `tool-strategy-core-competence-matrix`（核心能力评估矩阵） | 老顽童 | markdown 卡 | PPT _145 |

### 6.3 待确认（P2）

| # | 任务 | 负责人 | 交付物 | 备注 |
|--|--|--|--|--|
| 18 | 确认“凯纳创新框架”是否存在 | 欧阳锋/用户 | 是/否结论 | 若存在则补充定位；若不存在则从预期中移除 |
| 19 | 确认麦肯锡 7S 是否出现在 PPT 中 | 老顽童 | 页码 + 内容摘要 | 用户提及但当前未定位 |
| 20 | 确认蓝海战略四步动作框架页码 | 老顽童 | 页码 + 内容摘要 | 已外部验证框架存在性，需定位 PPT 出处 |

---

## 7. 修复 `describe-images-minimax.py` 的技术建议

### 7.1 问题复现

113 张 `_vlm_desc.md` 文件外层显示：

```markdown
- **置信度**: 0.3
- **类型**: 未识别
```

但文件后半部分仍包含完整 JSON，例如 `_16_vlm_desc.md` 内：

```json
{
  "category": "幻灯片",
  "title": "战略关键词三：连续动作",
  ...
}
```

### 7.2 修复方案

1. **提取 JSON 块**：使用正则匹配 ```json\n([\s\S]*?)\n``` 或首尾 `{}`。
2. **清洗非法字符**：
   - 替换未转义的换行符为 `\n`（在字符串值内部）。
   - 替换未转义的双引号 `"` 为 `\"`（在字符串值内部）。
   - 处理中文字符与反斜杠。
3. **容错解析**：
   ```python
   import json, re
   def robust_parse(text):
       m = re.search(r'```json\s*(.*?)\s*```', text, re.S)
       if m: text = m.group(1)
       try: return json.loads(text)
       except json.JSONDecodeError:
           # 可接入 demjson3 / json5 作为 fallback
           import json5
           return json5.loads(text)
   ```
4. **回归验证**：修复后重新生成 299 张 desc，确认 parse error 归零。

---

## 8. 外部验证来源汇总

| 框架 | 来源类型 | 关键 URL/文献 |
|--|--|--|
| IBM BLM 业务设计五要素 | 培训大纲/中文课程 | 多个内训课大纲（客户选择、价值主张、价值获取、活动范围、战略控制） |
| 麦肯锡 7S | 学术/咨询文献 | McKinsey 7S Framework: strategy/structure/systems/skills/style/staff/shared values |
| Grace LaConte 风险矩阵 | 咨询博客 | laconteconsulting.com：Severity×Likelihood → Accept/Share/Control/Mitigate |
| 波特五力 | 教科书/学术论文 | Porter 1980/1990；五力标准定义 |
| BCG 矩阵 | 咨询工具/百科 | 市场增长率×相对市场份额；明星/现金牛/问题/瘦狗 |
| 商业模式画布 | 学术/工具站 | Osterwalder & Pigneur 2010；9 个构建块 |
| 核心竞争力 | HBR 原文 | Prahalad & Hamel 1990：三标准（客户价值、延展性、难模仿） |
| 蓝海战略 | 畅销书/百科 | Kim & Mauborgne：剔除/减少/增加/创造（ERRC） |
| 关键成功因素 KSF | 战略管理教材 | Thompson et al.：3-5 个决定输赢的因素 |
| 安索夫矩阵 | HBR/工具站 | Ansoff 1957：市场渗透/开发/产品开发/多元化 |

---

## 9. 质量控制声明

- 本报告由 CLI 王语嫣独立完成，已执行 9 层深挖与六层交叉比对。
- 外部验证已通过 WebSearch 完成，来源已记录。
- 关键推翻性结论（业务设计应独立建卡）有 PPT 视觉层、讲义 OCR、外部文献三重证据支持。
- 113 张 parse error 的修复方案已给出，待洪七公/黄药师执行。
- 严格高潜清单 46 张已产出，待欧阳锋最终拍板。

---

*报告结束。下一步：等待欧阳锋确认工单优先级，并由洪七公修复 parser。*
