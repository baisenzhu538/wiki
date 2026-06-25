---
id: diag_20260625_wangyuyan_vlm-missed-knowledge
type: diagnosis
created_at: 2026-06-25
author: 王语嫣
scope: 00_inbox/_vlm_reprocess 结构化 VLM 描述 vs 成品卡所需深度
---

# VLM 重提取深度诊断：被遗漏的重要知识点

> 王语嫣铁律：本报告只写入 `60_feedback/`，不污染 `30_wiki/`。
> 目的：用洪七公已产出的结构化 VLM 描述反查上一轮 prompt 漏掉了哪些关键知识要素，并标注给老顽童补挖。

## 1. 诊断方法

- 扫描范围：`vlm_framework_value_triage.md` 中标注为 `new-* / case / dk / enrich / new_or_enrich / review` 的卡片。
- 漏挖判定：对每条 VLM 描述检查是否包含以下要素：
  - 失败模式/反例/边界（`失败模式/反例/坑/陷阱/误区`等）
  - 操作步骤/SOP/检查单（`步骤/流程/SOP/检查单/清单`等）
  - 关键数字/比例/量化证据（数字、`%`、倍数、金额等）
  - 暗知识/教训/心法标记（`暗知识/口诀/心法/教训/盲区`等）
  - 案例叙事段落长度（≥200 字连续叙事）
- `enrich` 类额外对比已有 wiki 卡片标题，若 VLM 描述中出现明显新主题而目标卡片未覆盖，也列为漏挖。

## 2. 总体发现

- 检查卡片总数：**146**
- 存在明显漏挖的卡片：**127**
- 缺少失败/边界/反例：**104**
- 缺少操作步骤/SOP：**22**
- 缺少关键数字：**0**
- 缺少暗知识/教训标记：**79**
- 案例卡缺少≥200字叙事：**0**
- enrich 目标卡片未覆盖新主题：**21**

## 3. 需老顽童重点补挖的卡片清单

| 域 | 文件名 | 建议动作 | 目标卡片 | 漏挖要素 | VLM 文件 |
|:---|:---|:---:|:---|:---|:---|
| 单元模型 | 一堂-单元模型-TCPR底层网络协议 | new-framework | framework-TCPR底层网络协议 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-TCPR底层网络协议_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-动态预测 | enrich | yt-tool-unit-model-dynamic | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-动态预测_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-单sku模型 | enrich | yt-unit-model-overview | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-单sku模型_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-单商圈模型 | new-tool | tool-单元模型-单商圈 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-单商圈模型_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-单城市模型 | new-tool | tool-单元模型-单城市 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-单城市模型_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-单客户模型 | enrich | yt-unit-model-overview | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-单客户模型_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-单履约模型 | enrich | yt-unit-model-overview | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-单履约模型_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-单柜子模型 | enrich | yt-unit-model-overview | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-单柜子模型_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-单用户模型 | enrich | yt-unit-model-overview | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-单用户模型_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-单订单模型 | enrich | yt-unit-model-overview | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-单订单模型_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-单销售模型 | enrich | yt-unit-model-overview | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-单销售模型_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-单门店模型 | enrich | yt-unit-model-overview | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-单门店模型_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-基准值 | enrich | yt-tool-unit-model-benchmark | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-基准值_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-壁垒预判 | new-tool | tool-单元模型-壁垒预判 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-壁垒预判_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-外部对抗地图 | new-framework | framework-单元模型-外部对抗地图 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-外部对抗地图_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-多模型情况 | enrich | yt-tool-unit-model-selection | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-多模型情况_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-学练用 | new-concept | concept-单元模型-学练用 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-学练用_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-对抗小抄01 | dk | dk-单元模型-对抗小抄 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-对抗小抄01_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-对抗小抄02 | dk | dk-单元模型-对抗小抄 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-对抗小抄02_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-对抗小抄 | dk | dk-单元模型-对抗小抄 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-对抗小抄_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-扭蛋机案例 | enrich-case | case-unit-model-gashapon | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-扭蛋机案例_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-找全成本实操难点 | dk | dk-单元模型-找全成本实操难点 | 缺少失败模式/边界/反例 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-找全成本实操难点_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-找单元模型实操难点 | dk | dk-单元模型-找单元模型实操难点 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-找单元模型实操难点_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-找基准值实操难点 | dk | dk-单元模型-找基准值实操难点 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-找基准值实操难点_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-斧子、尺子、梯子 | enrich | yt-unit-model-three-tools | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-斧子、尺子、梯子_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-斧子尺子梯子详解 | enrich | yt-unit-model-three-tools | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-斧子尺子梯子详解_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-最简单元模型 | new-concept | concept-最简单元模型 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-最简单元模型_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-段位专家 | enrich | yt-unit-model-ladder | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-段位专家_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-示例01 | case | case-单元模型-示例01 | 缺少失败/成功原因或反例 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-示例01_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-规模对抗实操难点 | dk | dk-单元模型-规模对抗实操难点 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-规模对抗实操难点_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-规模经济对抗武器库 | enrich | yt-scale-economy-weapon-library | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-规模经济对抗武器库_vlm_desc.md` |
| 单元模型 | 一堂-单元模型-象限分析法 | new-tool | tool-单元模型-象限分析法 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\单元模型\一堂-单元模型-象限分析法_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-ROI决策评估画布-案例01 | case | 待命名 | 缺少失败/成功原因或反例 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-ROI决策评估画布-案例01_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-ROI决策评估画布-案例02 | case | 待命名 | 缺少失败/成功原因或反例 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-ROI决策评估画布-案例02_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-ROI决策评估画布-案例03 | case | 待命名 | 缺少失败/成功原因或反例 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-ROI决策评估画布-案例03_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-ROI决策评估画布-案例04 | case | 待命名 | 缺少失败/成功原因或反例 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-ROI决策评估画布-案例04_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-ROI决策评估画布 | new-tool | tool-ROI决策评估画布 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-ROI决策评估画布_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-X型Y型决策习惯对比 | new-concept | concept-X型Y型决策习惯 | 缺少失败模式/边界/反例 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-X型Y型决策习惯对比_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-人机协作决策 | new-concept | concept-AI时代双三角竞争力 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-人机协作决策_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-关键训练清单（重要）） | new-tool | tool-科学决策关键训练清单 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-关键训练清单（重要））_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-决策三角形 | new-framework | framework-科学决策三角形 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-决策三角形_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-发现决策 | new-concept | concept-发现决策 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-发现决策_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-商业模式-完整财务公式决策 | new-tool | tool-完整财务公式决策 | 缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-商业模式-完整财务公式决策_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-宽度-个人 | new-concept | concept-科学决策宽度-个人 | 缺少失败模式/边界/反例 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-宽度-个人_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-宽度-企业 | new-concept | concept-科学决策宽度-企业 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-宽度-企业_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-宽度-团队 | new-concept | concept-科学决策宽度-团队 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-宽度-团队_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-深度-L1优先级定性 | new-tool | tool-决策深度-L1优先级定性 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-深度-L1优先级定性_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-深度-L2部分定量 | new-tool | tool-决策深度-L2部分定量 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-深度-L2部分定量_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-深度-L3定量公式 | new-tool | tool-决策深度-L3定量公式 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-深度-L3定量公式_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-深度-L4-案例01 | case | case-决策深度-L4-案例01 | 缺少失败/成功原因或反例 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-深度-L4-案例01_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-深度-L4严格财务公式 | new-tool | tool-决策深度-L4严格财务公式 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-深度-L4严格财务公式_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-深度-你的业务是一次抽样实验 | dk | dk-你的业务是一次抽样实验 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-深度-你的业务是一次抽样实验_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-深度-决策经验值 | dk | dk-决策经验值 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-深度-决策经验值_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-深度-案例01 | case | case-科学决策-全员涨薪20% | 缺少失败/成功原因或反例 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-深度-案例01_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-深度-案例02 | case | case-科学决策-上班开车还是打车 | 缺少失败/成功原因或反例 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-深度-案例02_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-深度-案例03 | case | case-科学决策-自研IM_CRM | 缺少失败/成功原因或反例 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-深度-案例03_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-深度-案例04 | case | case-科学决策-管员工中午饭 | 缺少失败/成功原因或反例 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-深度-案例04_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-深度-案例05 | case | case-科学决策-租办公室ROI | 缺少失败/成功原因或反例 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-深度-案例05_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-深度-案例06 | case | case-科学决策-电话外呼ROI | 缺少失败/成功原因或反例 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-深度-案例06_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-稀缺机会窗口 | new-concept | concept-稀缺机会窗口 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-稀缺机会窗口_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-稀缺资源清单 | new-tool | tool-稀缺资源清单 | 缺少失败模式/边界/反例 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-稀缺资源清单_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-项目方案评估三角形 | new-tool | tool-项目方案评估三角形 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-项目方案评估三角形_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-高度-两种典型的思考习惯 | new-concept | concept-两种典型思考习惯 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-高度-两种典型的思考习惯_vlm_desc.md` |
| 科学决策 | 一堂-科学决策-高水平共识曲线（重要） | new-framework | framework-高水平共识曲线 | 缺少失败模式/边界/反例 | `00_inbox/_vlm_reprocess\科学决策\一堂-科学决策-高水平共识曲线（重要）_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-审美卡片-最佳实践建模 | new-tool | tool-审美-最佳实践建模 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-审美卡片-最佳实践建模_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-审美卡片-最佳实践收集 | new-tool | tool-审美-最佳实践收集 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-审美卡片-最佳实践收集_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-审美卡片-最佳实践池子 | new-tool | tool-审美-最佳实践池子 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-审美卡片-最佳实践池子_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-审美卡片-美好作品想象 | new-concept | concept-美好作品想象 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-审美卡片-美好作品想象_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-审美工具箱指南 | new-tool | tool-审美工具箱指南 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-审美工具箱指南_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-用户卡片-动力阻力 | new-concept | concept-动力阻力 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-用户卡片-动力阻力_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-用户卡片-场景推演 | new-tool | tool-场景推演 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-用户卡片-场景推演_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-用户卡片-多视角思考 | new-tool | tool-多视角思考 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-用户卡片-多视角思考_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-用户卡片-峰终定律 | new-concept | concept-峰终定律 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-用户卡片-峰终定律_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-用户卡片-惊喜公式 | new-concept | concept-惊喜公式 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-用户卡片-惊喜公式_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-用户卡片-用户分层 | new-tool | tool-用户分层 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-用户卡片-用户分层_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-用户卡片-用户视角 | new-concept | concept-用户视角 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-用户卡片-用户视角_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-用户卡片-行业分析画布 | new-tool | tool-行业分析画布 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-用户卡片-行业分析画布_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-用户卡片-需求挖掘 | new-tool | tool-需求挖掘 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-用户卡片-需求挖掘_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-用户卡片-项目背景分析 | new-tool | tool-项目背景分析 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-用户卡片-项目背景分析_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-落地卡片-ROI分析 | new-tool | tool-泛产品-ROI分析 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-落地卡片-ROI分析_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-落地卡片-业务建模 | new-tool | tool-泛产品-业务建模 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-落地卡片-业务建模_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-落地卡片-假设拆解 | new-tool | tool-假设拆解 | 缺少失败模式/边界/反例 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-落地卡片-假设拆解_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-落地卡片-内核和边界 | new-concept | concept-内核和边界 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-落地卡片-内核和边界_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-落地卡片-努力仿真 | new-tool | tool-努力仿真 | 缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-落地卡片-努力仿真_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-落地卡片-十倍速验证 | new-tool | tool-十倍速验证 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-落地卡片-十倍速验证_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-落地卡片-善用佳软 | new-tool | tool-善用佳软 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-落地卡片-善用佳软_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-落地卡片-复盘迭代 | new-tool | tool-复盘迭代 | 缺少失败模式/边界/反例 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-落地卡片-复盘迭代_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-落地卡片-攻坚会 | new-tool | tool-攻坚会 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-落地卡片-攻坚会_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-落地卡片-灵感闪现 | dk | dk-灵感闪现 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-落地卡片-灵感闪现_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-落地卡片-管理三段论 | new-framework | framework-管理三段论 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-落地卡片-管理三段论_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-落地卡片-设计原则 | new-concept | concept-设计原则 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-落地卡片-设计原则_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-落地卡片-逻辑MECE | new-tool | tool-逻辑MECE | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-落地卡片-逻辑MECE_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-落地卡片-酝酿式打磨 | new-tool | tool-酝酿式打磨 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-落地卡片-酝酿式打磨_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-落地卡片-里程碑拆解 | new-tool | tool-里程碑拆解 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-落地卡片-里程碑拆解_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-落地卡片-风险管理 | new-tool | tool-风险管理 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-落地卡片-风险管理_vlm_desc.md` |
| 泛产品设计 | 泛产品设计-需求工具箱指南 | new-tool | tool-需求工具箱指南 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\泛产品设计\泛产品设计-需求工具箱指南_vlm_desc.md` |
| 个人修炼 | 一堂-个人修炼-Y模型 | enrich | yt-decision-y-model | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\个人修炼\一堂-个人修炼-Y模型_vlm_desc.md` |
| 个人修炼 | 一堂-个人修炼-双三角模型 | new-concept | concept-AI时代双三角竞争力 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\个人修炼\一堂-个人修炼-双三角模型_vlm_desc.md` |
| 个人修炼 | 一堂-个人修炼-提问刻意练习画布 | new-tool | tool-提问刻意练习画布 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\个人修炼\一堂-个人修炼-提问刻意练习画布_vlm_desc.md` |
| 个人修炼 | 一堂-个人修炼-科学学习IPO完整清单 | new-tool | tool-科学学习IPO完整清单 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\个人修炼\一堂-个人修炼-科学学习IPO完整清单_vlm_desc.md` |
| 个人修炼 | 一堂-个人修炼-科学提问刻意练习 | new-tool | tool-科学提问刻意练习 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\个人修炼\一堂-个人修炼-科学提问刻意练习_vlm_desc.md` |
| 个人修炼 | 一堂-个人修炼-解放思想 | new-concept | concept-思考深度分级 | 缺少失败模式/边界/反例 | `00_inbox/_vlm_reprocess\个人修炼\一堂-个人修炼-解放思想_vlm_desc.md` |
| 个人修炼 | 一堂-个人修炼-讲香十指模型-超级武器库 | new-tool | tool-讲香十指模型-超级武器库 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\个人修炼\一堂-个人修炼-讲香十指模型-超级武器库_vlm_desc.md` |
| 个人修炼 | 一堂-个人修炼-讲香基本功 | new-tool | tool-讲香基本功-十指模型 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\个人修炼\一堂-个人修炼-讲香基本功_vlm_desc.md` |
| 其他 | AI俱乐部-人和AI协作-纪浩-五层结构-图片01 | new-framework | framework-问题边界与Problem澄清五层结构 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\其他\AI俱乐部-人和AI协作-纪浩-五层结构-图片01_vlm_desc.md` |
| 其他 | Truman的个人成长五步法 | new-framework | framework-个人成长五步法 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\其他\Truman的个人成长五步法_vlm_desc.md` |
| 其他 | truman的选择：两条职业成长路线 | new-concept | concept-两条职业成长路线 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\其他\truman的选择：两条职业成长路线_vlm_desc.md` |
| 其他 | 一堂-AI学习-truman自用的AI FeatureSet | new-tool | tool-Truman自用AI FeatureSet | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\其他\一堂-AI学习-truman自用的AI FeatureSet_vlm_desc.md` |
| 其他 | 一堂-AI学习-提问工程化 | new-tool | tool-提问工程化 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\其他\一堂-AI学习-提问工程化_vlm_desc.md` |
| 其他 | 一堂-TCPR模型-皇冠模型 | new-framework | framework-TCPR皇冠模型 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\其他\一堂-TCPR模型-皇冠模型_vlm_desc.md` |
| 其他 | 一堂-人机协作-双三角模型 | new-concept | concept-AI时代双三角竞争力 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\其他\一堂-人机协作-双三角模型_vlm_desc.md` |
| 其他 | 一堂Y模型-科学成事道理 | enrich | yt-decision-y-model | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\其他\一堂Y模型-科学成事道理_vlm_desc.md` |
| 其他 | 一堂Y模型实操工作流 | new-tool | tool-Y模型实操工作流 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\其他\一堂Y模型实操工作流_vlm_desc.md` |
| 其他 | 一堂五步法-产品内核画布 | enrich | yt-product-kernel-canvas | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\其他\一堂五步法-产品内核画布_vlm_desc.md` |
| 其他 | 一堂五步法画布 | enrich | yt-five-step-method | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\其他\一堂五步法画布_vlm_desc.md` |
| 其他 | 一堂产品内核-十大典型指标 | enrich | yt-product-ten-metrics | VLM标题含目标卡片未覆盖的新主题 | `00_inbox/_vlm_reprocess\其他\一堂产品内核-十大典型指标_vlm_desc.md` |
| 其他 | 一堂刻意练习十年成长指数 | new-tool | tool-刻意练习十年成长指数 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\其他\一堂刻意练习十年成长指数_vlm_desc.md` |
| 其他 | 一堂提炼过的因果模型 | new-framework | framework-一堂因果模型 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\其他\一堂提炼过的因果模型_vlm_desc.md` |
| 其他 | 一堂最佳转化率动力曲线图 | new-framework | framework-最佳转化率动力三曲线 | 缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\其他\一堂最佳转化率动力曲线图_vlm_desc.md` |
| 其他 | 一堂泛产品设计-多出牌多练习 | dk | dk-多出牌多练习 | 缺少失败模式/边界/反例 | `00_inbox/_vlm_reprocess\其他\一堂泛产品设计-多出牌多练习_vlm_desc.md` |
| 其他 | 一堂深度复盘冰山图 | new-tool | tool-深度复盘冰山图 | 缺少失败模式/边界/反例 | `00_inbox/_vlm_reprocess\其他\一堂深度复盘冰山图_vlm_desc.md` |
| 其他 | 一堂转化率-10大容易浪费的触点 | new-tool | tool-转化率10大浪费触点 | 缺少失败模式/边界/反例 | `00_inbox/_vlm_reprocess\其他\一堂转化率-10大容易浪费的触点_vlm_desc.md` |
| 其他 | 优秀泛产品设计者的自我修养 | new-concept | concept-优秀泛产品设计者的自我修养 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\其他\优秀泛产品设计者的自我修养_vlm_desc.md` |
| 其他 | 婚礼操盘-用户和场景 | case | case-婚礼操盘-用户和场景 | 缺少失败/成功原因或反例 | `00_inbox/_vlm_reprocess\其他\婚礼操盘-用户和场景_vlm_desc.md` |
| 其他 | 婚礼规划 | case | case-婚礼规划 | 缺少失败/成功原因或反例 | `00_inbox/_vlm_reprocess\其他\婚礼规划_vlm_desc.md` |
| 其他 | 审美提升的层级 | new-concept | concept-审美提升的层级 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\其他\审美提升的层级_vlm_desc.md` |
| 其他 | 预判模型 | new_or_enrich | 需二轮提取后判断 | 缺少失败模式/边界/反例；缺少暗知识/教训/心法标记 | `00_inbox/_vlm_reprocess\其他\预判模型_vlm_desc.md` |

## 4. 按域重点说明

### 单元模型

**一堂-单元模型-TCPR底层网络协议** → `framework-TCPR底层网络协议`
- 建议动作：new-framework
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 单元模型 TCPR底层网络协议    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_单元模型\一堂 单元模型 TCPR……

**一堂-单元模型-动态预测** → `yt-tool-unit-model-dynamic`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂 单元模型 动态预测    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_单元模型\一堂 单元模型 动态预测.png   ……

**一堂-单元模型-单sku模型** → `yt-unit-model-overview`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂 单元模型 单sku模型    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_单元模型\一堂 单元模型 单sku模型.p……

**一堂-单元模型-单商圈模型** → `tool-单元模型-单商圈`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 单元模型 单商圈模型    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_单元模型\一堂 单元模型 单商圈模型.png……

**一堂-单元模型-单城市模型** → `tool-单元模型-单城市`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 单元模型 单城市模型    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_单元模型\一堂 单元模型 单城市模型.png……

**一堂-单元模型-单客户模型** → `yt-unit-model-overview`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂 单元模型 单客户模型    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_单元模型\一堂 单元模型 单客户模型.png……

**一堂-单元模型-单履约模型** → `yt-unit-model-overview`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂 单元模型 单履约模型    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_单元模型\一堂 单元模型 单履约模型.png……

**一堂-单元模型-单柜子模型** → `yt-unit-model-overview`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂 单元模型 单柜子模型    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_单元模型\一堂 单元模型 单柜子模型.png……

**一堂-单元模型-单用户模型** → `yt-unit-model-overview`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂 单元模型 单用户模型    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_单元模型\一堂 单元模型 单用户模型.png……

**一堂-单元模型-单订单模型** → `yt-unit-model-overview`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂 单元模型 单订单模型    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_单元模型\一堂 单元模型 单订单模型.png……

**一堂-单元模型-单销售模型** → `yt-unit-model-overview`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂 单元模型 单销售模型    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_单元模型\一堂 单元模型 单销售模型.png……

**一堂-单元模型-单门店模型** → `yt-unit-model-overview`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂 单元模型 单门店模型    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_单元模型\一堂 单元模型 单门店模型.png……

**一堂-单元模型-基准值** → `yt-tool-unit-model-benchmark`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂 单元模型 基准值    原图  :  00_inbox\_vlm_reprocess\_temp_单元模型\一堂 单元模型 基准值.png     模型  :  MiniMax M3      结构化描述      类型……

**一堂-单元模型-壁垒预判** → `tool-单元模型-壁垒预判`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 单元模型 壁垒预判    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_单元模型\一堂 单元模型 壁垒预判.png  ……

**一堂-单元模型-外部对抗地图** → `framework-单元模型-外部对抗地图`
- 建议动作：new-framework
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 单元模型 外部对抗地图    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_单元模型\一堂 单元模型 外部对抗地图.p……

**一堂-单元模型-多模型情况** → `yt-tool-unit-model-selection`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂 单元模型 多模型情况    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_单元模型\一堂 单元模型 多模型情况.png……

**一堂-单元模型-学练用** → `concept-单元模型-学练用`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 单元模型 学练用    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_单元模型\一堂 单元模型 学练用.png    ……

**一堂-单元模型-对抗小抄01** → `dk-单元模型-对抗小抄`
- 建议动作：dk
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 单元模型 对抗小抄01    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_单元模型\一堂 单元模型 对抗小抄01.p……

**一堂-单元模型-对抗小抄02** → `dk-单元模型-对抗小抄`
- 建议动作：dk
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 单元模型 对抗小抄02    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_单元模型\一堂 单元模型 对抗小抄02.p……

**一堂-单元模型-对抗小抄** → `dk-单元模型-对抗小抄`
- 建议动作：dk
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 单元模型 对抗小抄    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_单元模型\一堂 单元模型 对抗小抄.png  ……

**一堂-单元模型-扭蛋机案例** → `case-unit-model-gashapon`
- 建议动作：enrich-case
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂 单元模型 扭蛋机案例    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_单元模型\一堂 单元模型 扭蛋机案例.png……

**一堂-单元模型-找全成本实操难点** → `dk-单元模型-找全成本实操难点`
- 建议动作：dk
- 漏挖：缺少失败模式/边界/反例
- VLM 片段：VLM 描述：一堂 单元模型 找全成本实操难点    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_单元模型\一堂 单元模型 找全成本实操难……

**一堂-单元模型-找单元模型实操难点** → `dk-单元模型-找单元模型实操难点`
- 建议动作：dk
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 单元模型 找单元模型实操难点    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_单元模型\一堂 单元模型 找单元模型实……

**一堂-单元模型-找基准值实操难点** → `dk-单元模型-找基准值实操难点`
- 建议动作：dk
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 单元模型 找基准值实操难点    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_单元模型\一堂 单元模型 找基准值实操难……

**一堂-单元模型-斧子、尺子、梯子** → `yt-unit-model-three-tools`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂 单元模型 斧子、尺子、梯子    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_单元模型\一堂 单元模型 斧子、尺子、梯……

**一堂-单元模型-斧子尺子梯子详解** → `yt-unit-model-three-tools`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂 单元模型 斧子尺子梯子详解    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_单元模型\一堂 单元模型 斧子尺子梯子详……

**一堂-单元模型-最简单元模型** → `concept-最简单元模型`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 单元模型 最简单元模型    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_单元模型\一堂 单元模型 最简单元模型.pn……

**一堂-单元模型-段位专家** → `yt-unit-model-ladder`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂 单元模型 段位专家    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_单元模型\一堂 单元模型 段位专家.png   ……

**一堂-单元模型-示例01** → `case-单元模型-示例01`
- 建议动作：case
- 漏挖：缺少失败/成功原因或反例
- VLM 片段：VLM 描述：一堂 单元模型 示例01    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_单元模型\一堂 单元模型 示例01.png   ……

**一堂-单元模型-规模对抗实操难点** → `dk-单元模型-规模对抗实操难点`
- 建议动作：dk
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 单元模型 规模对抗实操难点    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_单元模型\一堂 单元模型 规模对抗实操难……

**一堂-单元模型-规模经济对抗武器库** → `yt-scale-economy-weapon-library`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂 单元模型 规模经济对抗武器库    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_单元模型\一堂 单元模型 规模经济对抗……

**一堂-单元模型-象限分析法** → `tool-单元模型-象限分析法`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 单元模型 象限分析法    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_单元模型\一堂 单元模型 象限分析法.png ……

### 科学决策

**一堂-科学决策-ROI决策评估画布-案例01** → `待命名`
- 建议动作：case
- 漏挖：缺少失败/成功原因或反例
- VLM 片段：VLM 描述：一堂 科学决策 ROI决策评估画布 案例01    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_科学决策\一堂 科学决策 ……

**一堂-科学决策-ROI决策评估画布-案例02** → `待命名`
- 建议动作：case
- 漏挖：缺少失败/成功原因或反例
- VLM 片段：VLM 描述：一堂 科学决策 ROI决策评估画布 案例02    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_科学决策\一堂 科学决策 ……

**一堂-科学决策-ROI决策评估画布-案例03** → `待命名`
- 建议动作：case
- 漏挖：缺少失败/成功原因或反例
- VLM 片段：VLM 描述：一堂 科学决策 ROI决策评估画布 案例03    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_科学决策\一堂 科学决策 ……

**一堂-科学决策-ROI决策评估画布-案例04** → `待命名`
- 建议动作：case
- 漏挖：缺少失败/成功原因或反例
- VLM 片段：VLM 描述：一堂 科学决策 ROI决策评估画布 案例04    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_科学决策\一堂 科学决策 ……

**一堂-科学决策-ROI决策评估画布** → `tool-ROI决策评估画布`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 科学决策 ROI决策评估画布    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_科学决策\一堂 科学决策 ROI决策……

**一堂-科学决策-X型Y型决策习惯对比** → `concept-X型Y型决策习惯`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例
- VLM 片段：VLM 描述：一堂 科学决策 X型Y型决策习惯对比    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_科学决策\一堂 科学决策 X型Y型……

**一堂-科学决策-人机协作决策** → `concept-AI时代双三角竞争力`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 科学决策 人机协作决策    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_科学决策\一堂 科学决策 人机协作决策.p……

**一堂-科学决策-关键训练清单（重要））** → `tool-科学决策关键训练清单`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 科学决策 关键训练清单（重要））    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_科学决策\一堂 科学决策 关键训……

**一堂-科学决策-决策三角形** → `framework-科学决策三角形`
- 建议动作：new-framework
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 科学决策 决策三角形    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_科学决策\一堂 科学决策 决策三角形.png……

**一堂-科学决策-发现决策** → `concept-发现决策`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 科学决策 发现决策    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_科学决策\一堂 科学决策 发现决策.png  ……

**一堂-科学决策-商业模式-完整财务公式决策** → `tool-完整财务公式决策`
- 建议动作：new-tool
- 漏挖：缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 科学决策 商业模式 完整财务公式决策    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_科学决策\一堂 科学决策 商……

**一堂-科学决策-宽度-个人** → `concept-科学决策宽度-个人`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例
- VLM 片段：VLM 描述：一堂 科学决策 宽度 个人    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_科学决策\一堂 科学决策 宽度 个人.png……

**一堂-科学决策-宽度-企业** → `concept-科学决策宽度-企业`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单
- VLM 片段：VLM 描述：一堂 科学决策 宽度 企业    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_科学决策\一堂 科学决策 宽度 企业.png……

**一堂-科学决策-宽度-团队** → `concept-科学决策宽度-团队`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单
- VLM 片段：VLM 描述：一堂 科学决策 宽度 团队    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_科学决策\一堂 科学决策 宽度 团队.png……

**一堂-科学决策-深度-L1优先级定性** → `tool-决策深度-L1优先级定性`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 科学决策 深度 L1优先级定性    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_科学决策\一堂 科学决策 深度 L1……

**一堂-科学决策-深度-L2部分定量** → `tool-决策深度-L2部分定量`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 科学决策 深度 L2部分定量    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_科学决策\一堂 科学决策 深度 L2部……

**一堂-科学决策-深度-L3定量公式** → `tool-决策深度-L3定量公式`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 科学决策 深度 L3定量公式    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_科学决策\一堂 科学决策 深度 L3定……

**一堂-科学决策-深度-L4-案例01** → `case-决策深度-L4-案例01`
- 建议动作：case
- 漏挖：缺少失败/成功原因或反例
- VLM 片段：VLM 描述：一堂 科学决策 深度 L4 案例01    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_科学决策\一堂 科学决策 深度 L4……

**一堂-科学决策-深度-L4严格财务公式** → `tool-决策深度-L4严格财务公式`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 科学决策 深度 L4严格财务公式    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_科学决策\一堂 科学决策 深度 L……

**一堂-科学决策-深度-你的业务是一次抽样实验** → `dk-你的业务是一次抽样实验`
- 建议动作：dk
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 科学决策 深度 你的业务是一次抽样实验    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_科学决策\一堂 科学决策 深……

**一堂-科学决策-深度-决策经验值** → `dk-决策经验值`
- 建议动作：dk
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 科学决策 深度 决策经验值    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_科学决策\一堂 科学决策 深度 决策经验……

**一堂-科学决策-深度-案例01** → `case-科学决策-全员涨薪20%`
- 建议动作：case
- 漏挖：缺少失败/成功原因或反例
- VLM 片段：VLM 描述：一堂 科学决策 深度 案例01    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_科学决策\一堂 科学决策 深度 案例01.……

**一堂-科学决策-深度-案例02** → `case-科学决策-上班开车还是打车`
- 建议动作：case
- 漏挖：缺少失败/成功原因或反例
- VLM 片段：VLM 描述：一堂 科学决策 深度 案例02    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_科学决策\一堂 科学决策 深度 案例02.……

**一堂-科学决策-深度-案例03** → `case-科学决策-自研IM_CRM`
- 建议动作：case
- 漏挖：缺少失败/成功原因或反例
- VLM 片段：VLM 描述：一堂 科学决策 深度 案例03    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_科学决策\一堂 科学决策 深度 案例03.……

**一堂-科学决策-深度-案例04** → `case-科学决策-管员工中午饭`
- 建议动作：case
- 漏挖：缺少失败/成功原因或反例
- VLM 片段：VLM 描述：一堂 科学决策 深度 案例04    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_科学决策\一堂 科学决策 深度 案例04.……

**一堂-科学决策-深度-案例05** → `case-科学决策-租办公室ROI`
- 建议动作：case
- 漏挖：缺少失败/成功原因或反例
- VLM 片段：VLM 描述：一堂 科学决策 深度 案例05    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_科学决策\一堂 科学决策 深度 案例05.……

**一堂-科学决策-深度-案例06** → `case-科学决策-电话外呼ROI`
- 建议动作：case
- 漏挖：缺少失败/成功原因或反例
- VLM 片段：VLM 描述：一堂 科学决策 深度 案例06    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_科学决策\一堂 科学决策 深度 案例06.……

**一堂-科学决策-稀缺机会窗口** → `concept-稀缺机会窗口`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 科学决策 稀缺机会窗口    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_科学决策\一堂 科学决策 稀缺机会窗口.pn……

**一堂-科学决策-稀缺资源清单** → `tool-稀缺资源清单`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例
- VLM 片段：VLM 描述：一堂 科学决策 稀缺资源清单    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_科学决策\一堂 科学决策 稀缺资源清单.pn……

**一堂-科学决策-项目方案评估三角形** → `tool-项目方案评估三角形`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 科学决策 项目方案评估三角形    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_科学决策\一堂 科学决策 项目方案评估……

**一堂-科学决策-高度-两种典型的思考习惯** → `concept-两种典型思考习惯`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 科学决策 高度 两种典型的思考习惯    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_科学决策\一堂 科学决策 高度 ……

**一堂-科学决策-高水平共识曲线（重要）** → `framework-高水平共识曲线`
- 建议动作：new-framework
- 漏挖：缺少失败模式/边界/反例
- VLM 片段：VLM 描述：一堂 科学决策 高水平共识曲线（重要）    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_temp_科学决策\一堂 科学决策 高水平共……

### 泛产品设计

**泛产品设计-审美卡片-最佳实践建模** → `tool-审美-最佳实践建模`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 审美卡片 最佳实践建模    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 审美卡片 最……

**泛产品设计-审美卡片-最佳实践收集** → `tool-审美-最佳实践收集`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 审美卡片 最佳实践收集    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 审美卡片 最……

**泛产品设计-审美卡片-最佳实践池子** → `tool-审美-最佳实践池子`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 审美卡片 最佳实践池子    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 审美卡片 最……

**泛产品设计-审美卡片-美好作品想象** → `concept-美好作品想象`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 审美卡片 美好作品想象    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 审美卡片 美……

**泛产品设计-审美工具箱指南** → `tool-审美工具箱指南`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 审美工具箱指南    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 审美工具箱指南.pn……

**泛产品设计-用户卡片-动力阻力** → `concept-动力阻力`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 用户卡片 动力阻力    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 用户卡片 动力阻……

**泛产品设计-用户卡片-场景推演** → `tool-场景推演`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 用户卡片 场景推演    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 用户卡片 场景推……

**泛产品设计-用户卡片-多视角思考** → `tool-多视角思考`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 用户卡片 多视角思考    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 用户卡片 多视……

**泛产品设计-用户卡片-峰终定律** → `concept-峰终定律`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 用户卡片 峰终定律    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 用户卡片 峰终定……

**泛产品设计-用户卡片-惊喜公式** → `concept-惊喜公式`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 用户卡片 惊喜公式    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 用户卡片 惊喜公……

**泛产品设计-用户卡片-用户分层** → `tool-用户分层`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 用户卡片 用户分层    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 用户卡片 用户分……

**泛产品设计-用户卡片-用户视角** → `concept-用户视角`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 用户卡片 用户视角    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 用户卡片 用户视……

**泛产品设计-用户卡片-行业分析画布** → `tool-行业分析画布`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 用户卡片 行业分析画布    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 用户卡片 行……

**泛产品设计-用户卡片-需求挖掘** → `tool-需求挖掘`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 用户卡片 需求挖掘    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 用户卡片 需求挖……

**泛产品设计-用户卡片-项目背景分析** → `tool-项目背景分析`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 用户卡片 项目背景分析    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 用户卡片 项……

**泛产品设计-落地卡片-ROI分析** → `tool-泛产品-ROI分析`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 落地卡片 ROI分析    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 落地卡片 RO……

**泛产品设计-落地卡片-业务建模** → `tool-泛产品-业务建模`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 落地卡片 业务建模    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 落地卡片 业务建……

**泛产品设计-落地卡片-假设拆解** → `tool-假设拆解`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例
- VLM 片段：VLM 描述：泛产品设计 落地卡片 假设拆解    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 落地卡片 假设拆……

**泛产品设计-落地卡片-内核和边界** → `concept-内核和边界`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 落地卡片 内核和边界    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 落地卡片 内核……

**泛产品设计-落地卡片-努力仿真** → `tool-努力仿真`
- 建议动作：new-tool
- 漏挖：缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 落地卡片 努力仿真    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 落地卡片 努力仿……

**泛产品设计-落地卡片-十倍速验证** → `tool-十倍速验证`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 落地卡片 十倍速验证    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 落地卡片 十倍……

**泛产品设计-落地卡片-善用佳软** → `tool-善用佳软`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 落地卡片 善用佳软    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 落地卡片 善用佳……

**泛产品设计-落地卡片-复盘迭代** → `tool-复盘迭代`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例
- VLM 片段：VLM 描述：泛产品设计 落地卡片 复盘迭代    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 落地卡片 复盘迭……

**泛产品设计-落地卡片-攻坚会** → `tool-攻坚会`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 落地卡片 攻坚会    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 落地卡片 攻坚会.……

**泛产品设计-落地卡片-灵感闪现** → `dk-灵感闪现`
- 建议动作：dk
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 落地卡片 灵感闪现    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 落地卡片 灵感闪……

**泛产品设计-落地卡片-管理三段论** → `framework-管理三段论`
- 建议动作：new-framework
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 落地卡片 管理三段论    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 落地卡片 管理……

**泛产品设计-落地卡片-设计原则** → `concept-设计原则`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 落地卡片 设计原则    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 落地卡片 设计原……

**泛产品设计-落地卡片-逻辑MECE** → `tool-逻辑MECE`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 落地卡片 逻辑MECE    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 落地卡片 逻……

**泛产品设计-落地卡片-酝酿式打磨** → `tool-酝酿式打磨`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 落地卡片 酝酿式打磨    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 落地卡片 酝酿……

**泛产品设计-落地卡片-里程碑拆解** → `tool-里程碑拆解`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 落地卡片 里程碑拆解    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 落地卡片 里程……

**泛产品设计-落地卡片-风险管理** → `tool-风险管理`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 落地卡片 风险管理    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 落地卡片 风险管……

**泛产品设计-需求工具箱指南** → `tool-需求工具箱指南`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：泛产品设计 需求工具箱指南    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_泛产品设计\泛产品设计 需求工具箱指南.pn……

### 个人修炼

**一堂-个人修炼-Y模型** → `yt-decision-y-model`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂 个人修炼 Y模型    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_个人修炼\一堂 个人修炼 Y模型.jpg    ……

**一堂-个人修炼-双三角模型** → `concept-AI时代双三角竞争力`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 个人修炼 双三角模型    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_个人修炼\一堂 个人修炼 双三角模型.jpg……

**一堂-个人修炼-提问刻意练习画布** → `tool-提问刻意练习画布`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 个人修炼 提问刻意练习画布    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_个人修炼\一堂 个人修炼 提问刻意练习……

**一堂-个人修炼-科学学习IPO完整清单** → `tool-科学学习IPO完整清单`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 个人修炼 科学学习IPO完整清单    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_个人修炼\一堂 个人修炼 科学学……

**一堂-个人修炼-科学提问刻意练习** → `tool-科学提问刻意练习`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 个人修炼 科学提问刻意练习    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_个人修炼\一堂 个人修炼 科学提问刻意……

**一堂-个人修炼-解放思想** → `concept-思考深度分级`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例
- VLM 片段：VLM 描述：一堂 个人修炼 解放思想    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_个人修炼\一堂 个人修炼 解放思想.png  ……

**一堂-个人修炼-讲香十指模型-超级武器库** → `tool-讲香十指模型-超级武器库`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 个人修炼 讲香十指模型 超级武器库    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_个人修炼\一堂 个人修炼 讲香……

**一堂-个人修炼-讲香基本功** → `tool-讲香基本功-十指模型`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 个人修炼 讲香基本功    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_个人修炼\一堂 个人修炼 讲香基本功.web……

### 其他

**AI俱乐部-人和AI协作-纪浩-五层结构-图片01** → `framework-问题边界与Problem澄清五层结构`
- 建议动作：new-framework
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：AI俱乐部 人和AI协作 纪浩 五层结构 图片01    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\AI俱乐部 人……

**Truman的个人成长五步法** → `framework-个人成长五步法`
- 建议动作：new-framework
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：Truman的个人成长五步法    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\Truman的个人成长五步法.png……

**truman的选择：两条职业成长路线** → `concept-两条职业成长路线`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：truman的选择：两条职业成长路线    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\truman的选择：两条职业……

**一堂-AI学习-truman自用的AI FeatureSet** → `tool-Truman自用AI FeatureSet`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 AI学习 truman自用的AI FeatureSet    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\一堂……

**一堂-AI学习-提问工程化** → `tool-提问工程化`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 AI学习 提问工程化    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\一堂 AI学习 提问工程化.png  ……

**一堂-TCPR模型-皇冠模型** → `framework-TCPR皇冠模型`
- 建议动作：new-framework
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 TCPR模型 皇冠模型    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\一堂 TCPR模型 皇冠模型.png……

**一堂-人机协作-双三角模型** → `concept-AI时代双三角竞争力`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂 人机协作 双三角模型    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\一堂 人机协作 双三角模型.png  ……

**一堂Y模型-科学成事道理** → `yt-decision-y-model`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂Y模型 科学成事道理    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\一堂Y模型 科学成事道理.png    ……

**一堂Y模型实操工作流** → `tool-Y模型实操工作流`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂Y模型实操工作流    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\一堂Y模型实操工作流.png     模型 ……

**一堂五步法-产品内核画布** → `yt-product-kernel-canvas`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂五步法 产品内核画布    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\一堂五步法 产品内核画布.png    ……

**一堂五步法画布** → `yt-five-step-method`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂五步法画布    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\一堂五步法画布.png     模型  :  Mi……

**一堂产品内核-十大典型指标** → `yt-product-ten-metrics`
- 建议动作：enrich
- 漏挖：VLM标题含目标卡片未覆盖的新主题
- VLM 片段：VLM 描述：一堂产品内核 十大典型指标    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\一堂产品内核 十大典型指标.png  ……

**一堂刻意练习十年成长指数** → `tool-刻意练习十年成长指数`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂刻意练习十年成长指数    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\一堂刻意练习十年成长指数.png    ……

**一堂提炼过的因果模型** → `framework-一堂因果模型`
- 建议动作：new-framework
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂提炼过的因果模型    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\一堂提炼过的因果模型.png     模型 ……

**一堂最佳转化率动力曲线图** → `framework-最佳转化率动力三曲线`
- 建议动作：new-framework
- 漏挖：缺少失败模式/边界/反例；缺少操作步骤/SOP/检查单；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：一堂最佳转化率动力曲线图    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\一堂最佳转化率动力曲线图.png    ……

**一堂泛产品设计-多出牌多练习** → `dk-多出牌多练习`
- 建议动作：dk
- 漏挖：缺少失败模式/边界/反例
- VLM 片段：VLM 描述：一堂泛产品设计 多出牌多练习    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\一堂泛产品设计 多出牌多练习.png……

**一堂深度复盘冰山图** → `tool-深度复盘冰山图`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例
- VLM 片段：VLM 描述：一堂深度复盘冰山图    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\一堂深度复盘冰山图.png     模型  :……

**一堂转化率-10大容易浪费的触点** → `tool-转化率10大浪费触点`
- 建议动作：new-tool
- 漏挖：缺少失败模式/边界/反例
- VLM 片段：VLM 描述：一堂转化率 10大容易浪费的触点    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\一堂转化率 10大容易浪费的触点……

**优秀泛产品设计者的自我修养** → `concept-优秀泛产品设计者的自我修养`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：优秀泛产品设计者的自我修养    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\优秀泛产品设计者的自我修养.png  ……

**婚礼操盘-用户和场景** → `case-婚礼操盘-用户和场景`
- 建议动作：case
- 漏挖：缺少失败/成功原因或反例
- VLM 片段：VLM 描述：婚礼操盘 用户和场景    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\婚礼操盘 用户和场景.png     模型 ……

**婚礼规划** → `case-婚礼规划`
- 建议动作：case
- 漏挖：缺少失败/成功原因或反例
- VLM 片段：VLM 描述：婚礼规划    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\婚礼规划.png     模型  :  MiniMax ……

**审美提升的层级** → `concept-审美提升的层级`
- 建议动作：new-concept
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：审美提升的层级    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\审美提升的层级.png     模型  :  Mi……

**预判模型** → `需二轮提取后判断`
- 建议动作：new_or_enrich
- 漏挖：缺少失败模式/边界/反例；缺少暗知识/教训/心法标记
- VLM 片段：VLM 描述：预判模型    原图  :  C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\预判模型.png     模型  :  MiniMax ……

## 5. 给老顽童的补挖指令

对上述清单中的卡片，老顽童在生产成品卡时必须：**不能仅依赖 VLM 描述**，必须回看原图 + OCR 文本，重点补挖以下要素：

1. **失败模式/边界/反例**：每个 framework/tool/concept/dk 卡至少补 3 条失败模式或边界条件。
2. **操作步骤/SOP/检查单**：把图中隐含的“怎么做”显式化为可执行的步骤或清单。
3. **关键数字与证据**：案例卡必须提取具体数字、比例、金额、时间；非案例卡提取图中给出的量化指标或阈值。
4. **暗知识/心法/口诀**：把讲师随口提到的判断口诀、失败教训、避坑经验单独标注为 `dk` 候选。
5. **叙事段落扫描**：案例卡必须定位 ≥200 字连续叙事段落，完整度评分 ≥4 分方可立项。

补挖结果应在成品卡 `source_refs` 中同时注明 VLM 描述文件 + 原图路径，并在正文中对补挖内容标注 `[conf=0.80, source=原图/OCR]`。

---
*诊断人：王语嫣 | 日期：2026-06-25*