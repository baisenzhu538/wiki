---
id: "ocr-一堂-科学决策-深度-l4-案例01"
created_at: 2026-05-21
domain:
  - "yitang"
source_refs:
  - "src_20260522_5323822f"
status: "enriched"
title: "OCR: 一堂-科学决策-深度-L4-案例01"
type: "concept"
updated_at: 2026-05-22
tags:
  - #scene/ai-collaboration
  - #scene/business-analysis/conversion-rate
  - #scene/business-analysis/customer-acquisition
  - #scene/learning-methodology
  - #scene/skill-engineering
pipeline:
  - #boundary/requires-human-judgment
  - confidence-source-cited
  - confidence-verified-by-case
---

# OCR: 一堂-科学决策-深度-L4-案例01



## Summary

原图: `00_inbox/科学决策/一堂-科学决策-深度-L4-案例01.

png` 1万个投放线索的ROI分析(乐观) 成本 收益 投放成本：200万元 转化金额：240万元 履约成本：60万元 退费成本：12万元 总成本：272万元 总收益：240万元 - 本文件由 PaddleOCR ONNX pipeline 自动提取 - 可能存在连字/误识，需要人工校对 - 视觉结构信息（标题/正文/表格分块）未在 OCR 中体现，需要结合原图理解



## Source Refs

- `src_20260522_5323822f` -> `10_raw/sources/src_20260522_5323822f-ocr-一堂-科学决策-深度-l4-案例01.md`



## Reusable Knowledge

- 投放获客需核算全链路成本，包括投放成本、履约成本及退费成本，而非仅计算直接投放支出。
- 本案例"乐观"口径下，1万条线索总成本272万元，总收益240万元，实际ROI为负。
- 科学决策要求区分乐观/悲观等多情景测算，避免单一预期误导投入判断。
- 线索量级（1万条）需与转化效率联动分析，大规模投放可能放大亏损基数。



## Open Questions

- 该案例标注为"乐观"口径，但悲观情景的具体参数（如转化率假设、退费率假设）未披露，无法验证乐观/悲观的边界是否合理
- "1万个投放线索"的转化金额240万元对应的客单价、转化率、转化周期等关键中间指标缺失，无法评估模型可复用性
- 履约成本60万元的具体构成（人力、物料、服务周期）未说明，无法判断该成本属于固定成本还是可变成本，影响规模效应分析
- 退费成本12万元的退费触发条件、退费时间窗口、是否含资金占用成本未明确，乐观口径下是否已充分计提存在疑问
- 投放成本200万元对应的渠道结构（单一渠道/组合渠道）、线索单价（200元/条）与行业基准对比缺失，无法评估投放效率
- 总收益240万元是否含续费/复购等LTV延伸收益，或仅为首单收入，直接影响ROI计算口径的科学性
- 视觉结构信息未在OCR中体现，"乐观"标注位置及是否有其他情景表格并列原图，需人工校对确认是否存在关键信息遗漏



## Critique

#### Dennett - 意向立场陷阱
Dennett 论证多情景分析的形式化限制。案例中乐观/悲观两种情景虽然比单一预期好，但实际世界可能有无数个情景。你确定悲观情景真的够悲观吗？

#### Klein - 全链路成本认知负荷
Klein 论证专家直觉有限。案例中提醒需核算全链路成本，但履约和退费成本往往是事后才出现的。你是否在用理论上完整的框架分析实际上缺乏数据的业务？



## Synthesis

### 与本库其他概念的关联

- [[yt-decision-depth-ladder]] - 深度梯子，L4 是其第四级走进阶
- [[yt-decision-canvas]] - 同域决策画布，L4 是其在投放场景的应用
- [[master-decision-hygiene]] - 通用决策卫生

### 可迁移场景

- 投放获客投资决策：用全链路成本核算警惕乐观假设
- 销售渠道收益评估：强制包含退费、履约等隐性成本



### 不要用的场景

- 不要将多情景分析当作考虑全面的保证
- 不要在缺乏全链路数据时做理论上完整的核算
- 不要将案例中的乐观口径下也是负当作所有投放的定律



## Action Triggers

- 従你在评估投放/获客投资时，用全链路成本核算
- 従你只做了乐观+悲观两种情景时，用 Dennett 视角检查
- 従你在用案例中的也是负来否决项目时，检查可比性



## Output Opportunities

Content: <article/tutorial/report/analysis>
Code: <script/tool/template>
Capability: <workflow/playbook/skill/agent>
