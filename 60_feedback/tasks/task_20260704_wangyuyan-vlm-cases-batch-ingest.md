---
id: task_20260704_wangyuyan-vlm-cases-batch-ingest
type: task
status: queued
assignee: 老顽童
reviewer: 欧阳锋
priority: P0
created_at: 2026-07-04
updated_at: 2026-07-04
related:
- '[[concept-yihang-dual-triangle-core]]'
- '[[case-yihang-dual-triangle-beike-ai-outbound]]'
---

# 任务 #92：VLM 已处理案例批量入库（~35 张卡，分三批）

## 问题

洪七公已跑完 VLM 提取的 ~35 个独立案例/方法论图，六要素标注齐全，全部停在 `_processed/` 未入库。Agent 调用 `kdo query` 搜不到任何一个。

## 素材路径

`00_inbox/人机协作双三角/_processed/` 下所有非 page 分页的独立 VLM 文件。

## 分批生产

### 第一批：Agent 直接可用的 case 卡（P0，7 张）

立即入库，让 Agent 能回答"某某案例怎么做双三角"类查询。

| VLM 文件 | 拟建 case ID | 案例主体 |
|:---|:---|:---|
| 一堂双三角-数字化营销提效十倍_vlm.md | case-yihang-dual-triangle-moufeimao-digital-marketing | 牟肥猫 |
| 一堂双三角-IP选题智能体挑战交付上限_vlm.md | case-yihang-dual-triangle-vikki-ip-topic-selection | Vikki |
| 一堂双三角-教育新官网制作_vlm.md | case-yihang-dual-triangle-yitang-edu-website | 一堂 |
| 一堂双三角-图书分析AI工具_vlm.md | case-yihang-dual-triangle-liukai-book-analysis | 刘凯 |
| 一堂双三角-人生红点教练parther探索_vlm.md | case-yihang-dual-triangle-life-reddot-coach | 人生红点 |
| 一堂双三角-跨行业速解工业级难题_vlm.md | case-yihang-dual-triangle-cross-industry-industrial | 跨行业 |
| 一堂双三角-龙虾训练实验_vlm.md | case-yihang-dual-triangle-lobster-training | 龙虾训练 |

### 第二批：方法论/工具/框架卡（P1，~15 张）

| VLM 文件 | 拟建类型 |
|:---|:---|
| 一堂双三角-AI落地五部曲_vlm.md | framework |
| 一堂双三角-一个引擎-三阶六变_vlm.md | framework |
| 一堂双三角-AI时代的竞争力武器库_vlm.md | framework/tool |
| 一堂双三角-双三角预判画布_vlm.md | tool |
| 一堂双三角-清单版画布_vlm.md | tool |
| 一堂双三角-解释版画布_vlm.md | tool |
| 一堂双三角-AI企业经营数据分析_vlm.md | tool/framework |
| 一堂双三角-十年爬山地图_vlm.md | framework |
| 一堂双三角-作业洞察和特别表白_vlm.md | concept |
| 人创造力_vlm.md / 人审美_vlm.md / 人练体系_vlm.md | concept（合并到已有卡或新建） |
| 人类三角-创造力/审美/练体系_vlm.md | concept |
| AI三角-场景/基本功/数据_vlm.md | concept |
| AI场景/AI基本功/AI数据_vlm.md | concept |
| AI可以落地的场景假设_vlm.md | concept |
| 双三角-竞争力武器库_vlm.md | framework |

### 第三批：已有 wiki 卡的 VLM 可作为补充素材（P2）

以下案例已有 wiki 卡，VLM 提取可作为卡片的补充图文素材：

- 硬件公司-AI专利落地案例_vlm.md → 已有 case-yihang-dual-triangle-hardware-patent-rule-explicit
- 酒店行业-AI标签审核案例_vlm.md → 已有 case-yihang-dual-triangle-hotel-tag-sandbox
- 天末的双三角模型_vlm.md → 已有 case-yihang-dual-triangle-tianmo-design-delivery
- 阿豪的双三角模型_vlm.md → 已有 case-yihang-dual-triangle-ahao-product-selection

## 生产要求

- 每张卡从 VLM 文件的 `【基础结构】` 节直接提取六要素映射
- status=draft 先入库，让 `kdo query` 能搜到
- 六要素映射完整即可提交，精修后续再做
- 必须收录 index.md

## 验收标准

- 第一批 7 张 case 卡 `kdo pre-submit` PASS
- `kdo query "Vikki 怎么做选题"` 能返回结果
- index.md 收录
- 欧阳锋终审通过（可分批）
