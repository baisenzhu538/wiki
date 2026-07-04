---
id: diag_20260704_dual-triangle-vlm-gap-analysis
title: 双三角 VLM 素材交叉验证与入库缺口诊断
type: diagnosis
status: draft
created_at: 2026-07-04
source: 00_inbox/人机协作双三角/_processed/ 全部 VLM 文件
method: 6层交叉验证
---

# 双三角 VLM 素材交叉验证与入库缺口诊断

## 一、素材全景

洪七公已完成 VLM 提取：`_processed/` 目录 129 个文件，其中独立 VLM 文件 ~37 个，多页口述 VLM ~50 个。

## 二、交叉验证结果

### VLM → 已有 Wiki 卡（已覆盖，不需新建）

| VLM | 已有 Wiki 卡 | 状态 |
|:---|:---|:---:|
| AI落地五部曲 | framework-yihang-dual-triangle-ai-landing-five-steps | ✅ |
| 一个引擎-三阶六变 | framework-yihang-dual-triangle-three-stages-six-changes | ✅ |
| 竞争力武器库 | framework-yihang-dual-triangle-weapon-library | ✅ |
| 十年爬山地图 | framework-yihang-dual-triangle-ten-year-map | ✅ |
| 双三角预判画布 | tool-yihang-dual-triangle-canvas | ✅ |
| 花总：跨行业 | case-yihang-dual-triangle-huazao-synthetic-data | ✅ |

### VLM → 无 Wiki 卡（缺口，需入库）

| # | VLM | 拟建 ID | 类型 | 六要素完整性 | 优先级 |
|:---:|:---|:---|:---:|:---:|:---:|
| 1 | 牟肥猫：数字化营销 | case-yihang-moufeimao-digital-marketing | case | 完整 | P0 |
| 2 | Vikki：IP选题 | case-yihang-vikki-ip-topic-selection | case | 完整 | P0 |
| 3 | 刘凯：图书分析AI工具 | case-yihang-liukai-book-analysis | case | 完整 | P0 |
| 4 | 徐剑：AI企业经营数据分析 | case-yihang-xujian-enterprise-data | case | 完整 | P0 |
| 5 | 人生红点教练 | case-yihang-life-reddot-coach | case | 完整 | P1 |
| 6 | 龙虾训练 | case-yihang-lobster-training | case | 完整 | P1 |
| 7 | 一堂：教育新官网 | case-yihang-yitang-edu-website | case | 完整 | P1 |

### VLM 方法论补充素材（可合并到已有框架卡，不需新建）

| VLM | 建议合并到 | 原因 |
|:---|:---|:---|
| 清单版画布 | tool-yihang-dual-triangle-canvas | 画布的变体版本 |
| 解释版画布 | tool-yihang-dual-triangle-canvas | 同上 |
| 人类三角各维度 VLM | concept-yihang-dual-triangle-core 或独立 concept | 已有核心卡覆盖六要素定义，VLM 是分维度展开 |
| AI三角各维度 VLM | concept-yihang-dual-triangle-core | 同上 |
| AI可以落地的场景假设 | concept-yihang-dual-triangle-core | 场景假设=场景角的展开 |
| 作业洞察和特别表白 | concept 类（可选） | 教学反馈维度，非核心 |
| 画布案例1/2 | 已有 case 卡或 tool 卡 | 案例填充 |

## 三、优先级判断

**P0：让 Agent 能回答案例查询。** 7 张 case 卡立即入库（已在 #92 任务单覆盖）。

**P1：组件 VLM 合并判断。** 人类三角/AI三角各维度 VLM 是否需要独立建卡？判断：已有 `concept-yihang-dual-triangle-core` 覆盖六要素定义，VLM 是同一概念的分维度展开。**不新建卡**——作为核心卡的补充素材，后续迭代时合并进去。

**P2：画布变体。** 清单版/解释版画布是 `tool-yihang-dual-triangle-canvas` 的 UI 变体，不独立建卡。

## 四、结论

- **需新建**：7 张 case 卡（已在 #92）
- **不需新建**：6 张已覆盖，其余方法论素材合并到已有卡
- **本次不丢知识点**：所有 VLM 六要素映射均有落处——要么新建 case，要么标注为已有卡的补充素材

## 五、任务标注

已建任务 #92 覆盖 7 张 case 卡 + 其余素材分类归档。不需额外新建任务。
