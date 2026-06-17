---

id: labeling-final-consolidation
title: 数据标注方案最终汇总 — 三方调研 + 独立判断
type: decision
status: draft
domain:
- master
created_at: 2026-05-31
updated_at: '2026-06-16'
target_roles:
- 用户（决策者）
- 欧阳锋（Architect）
reviewer: 用户 + 欧阳锋
related:
- '[[data-labeling-best-practices-report]]'
- '[[kdo-15-dimension-label-spec]]'
- '[[labeling-research-alignment]]'
- '[[ouyangfeng-labeling-research-review]]'
author: unknown
source_context: KDO internal decision record （原 legacy，已从 title/context/filename 推断为
  src_20260503_52ae08ba）
source_refs:
  - src_20260503_52ae08ba-kdo_product_design_agent_final
reviewed_by: pending
confidence: 0.6
trust_level: low
---
# 数据标注方案最终汇总 — 三方调研 + 黄药师独立判断

> 汇总人：黄药师
> 审查人：用户（决策者）、欧阳锋（Architect）
> 前置阅读：本文件是三份调研 + 一份独立判断的最终合并。阅读本文件即可，不需要回溯其余四份。

---

## 一、三份调研定位

| | 老顽童 | 黄药师 | 欧阳锋 |
|------|---------|--------|--------|
| **路线** | 传统 ML 标注标准（COCO/CoNLL/Pascal VOC） | AI 时代 RAG 标注实践（HILTS/混合管线） | 2025-2026 生产级验证（NVIDIA/Amazon KDD/ATLAN） |
| **回答的问题** | "行业标准是什么" | "KDO 应该怎么做" | "行业最新实践是否支持黄药师" |
| **KDO 映射** | 无 | 完整（15维度方案） | 逐条核对 → 方向正确 |
| **AI 时代适用性** | ~40% 直接适用，~30% 需翻译，**~30% 不适用** | 100% 为 AI 时代设计 | 100% 为 AI 时代设计 |

---

## 二、黄药师独立判断：老顽童报告的取舍

### 保留的部分

| 内容 | 原因 |
|------|------|
| 四层维度架构（语义→属性→质量） | 通用框架，映射到 KDO 四组 |
| MECE 原则 | 任何标签体系的基础 |
| MVA 最小可用原则 | 等价于"从下游决策倒推" |
| 渐进精细化 | 等价于版本迭代 |
| 质量四维矩阵（一致性×准确性×完整性×可追溯性） | QC 通用语言 |
| 边界情况显式定义 | 每个标签的 included/excluded 描述 |

### 需要翻译的部分

| 内容 | 传统含义 | AI 时代翻译 |
|------|---------|-----------|
| IAA（标注者间一致性） | 多人标注同一样本的一致性 | **AI 标注 vs Gold Standard 一致性** |
| 金标准样本集（5-10%） | COCO 有 20 万张图，5% = 1 万张 | **绝对值 10-20 条 chunk**（384 张卡不需要按比例） |
| 标注指南 | 人读的 PDF | **标签描述（YAML 的 includes/excludes）**——AI 靠这段文本做 Embedding 匹配 |
| 标注者培训 | 多文化标注者校准 | **不适用**——KDO 标注者是 AI 脚本，不存在文化偏差 |

### 丢弃的部分

| 内容 | 丢弃理由 |
|------|---------|
| NLP 标注维度（POS/NER/依存句法/共指消解） | 训练 NLP 模型的标注方案。KDO 不做模型训练 |
| CV/语音/视频标注（边界框/语义分割/关键点/ASR） | KDO 不处理图像/视频/音频的逐像素/逐帧标注 |
| 标注工具对比（Label Studio/BRAT/Doccano/CVAT） | 人工标注 UI 工具。KDO 标注是脚本自动跑的 |
| CoNLL/COCO/Pascal VOC 标准 | 模型训练数据集的格式标准，不是知识库标签标准 |
| 多标注者偏差控制 | KDO 只有一个标注者（AI 脚本） |

### 最关键的范式差异

老顽童报告的隐含假设：
```
人在 UI 里手动标注 → 训练数据 → 模型训练 → 模型产出
```

KDO 的现实：
```
AI 脚本自动标注 → RAG 检索 → LLM 上下文 → AI 回答
```

这带来三个根本性差异：
1. **精度要求不同**：训练数据错标会毒化模型。RAG 标签错只影响检索精度——LLM 还有一次机会自己判断。KDO 容错率更高。IAA ≥ 0.8 对 KDO 过度。
2. **标签描述 > 标签名**：传统场景人看标签名选。AI 场景 Embedding 靠描述做语义匹配。描述文本质量直接决定标注准确率。
3. **成本结构完全颠倒**：传统场景人工标注贵。KDO 场景 AI 标注几乎零成本，瓶颈在人工抽检。应该追求"**在可接受准确率下最小化抽检工作量**"，不是"降低标注成本"。

---

## 三、最终方案：15 维度 v1.1

合并三份调研 + 欧阳锋三个补充建议后的最终形态。

### 维度总表（15 维，4 组）

| # | 组 | 维度 | 层级 | 激活 | 标注方式 | 值数 |
|:--:|:--:|------|:--:|------|---------|:--:|
| 1 | 检索 | domain | 卡 | 必标 | 人工 | 5 |
| 2 | 检索 | chunk_type | 块 | 必标 | 自动 | 19 |
| 3 | 检索 | method_family | 块 | 必标 | 自动 | 11 |
| 4 | 视角 | audience | 块 | 有信号 | 自动 | 8 |
| 5 | 视角 | perspective | 块 | 有信号 | 自动 | 6 |
| 6 | 视角 | platform | 块 | 有信号 | 自动 | 6 |
| 7 | 视角 | source_person | 卡 | 暗知识卡必标 | 人工 | 12 |
| 8 | 视角 | source_context_type | 卡 | 暗知识卡必标 | 人工 | 9 |
| 9 | 质量 | confidence | 块 | 有证据 | 自动 | 4+null |
| 10 | 质量 | data_generation | 卡 | **必标** ↑ | 人工 | 5 |
| 11 | 质量 | error_root | 块 | error_data | 自动 | 9 |
| 12 | 质量 | expiry | 卡 | 条件必标† | 人工 | 5 |
| 13 | 价值 | value_tier | 卡 | 必标 | 人工 | 3 |
| 14 | 价值 | usage_depth | 卡 | 必标 | 自动+人工 | 5 |
| 15 | 价值 | prerequisite_knowledge | 卡 | 有前置 | 人工 | 4+ |

\* `label_confidence`（LLM 标注置信度）路由规则：LLM 推理时给出置信度 score → 高(>0.85)直接入库，中(0.70-0.85)进抽检池，低(<0.70)必须人工确认。注意与维度 #9 `confidence`（标签值：高/中/低/null，描述 chunk 主张本身的置信水平）区分——`label_confidence` 是标注过程的元数据，`confidence` 是标签内容。  
† expiry 条件必标：value_tier = macro 的卡必须填 expiry。其余可选。

### v1.1 新增字段（欧阳锋三个建议）

| # | 字段 | 层级 | 说明 | 来源 |
|:--:|------|:--:|------|:--:|
| 1* | `label_confidence` | 块 | LLM 标注时给出的置信度 (0-1)。用于路由决策 | 欧阳锋建议 1 |
| 2 | `last_reviewed_at` | 卡/块 | 自动时间戳。配合 `kdo lint --stale N` | 欧阳锋建议 2 |
| 3 | `label_version` | 块 | 标注时使用的 tag-registry 版本号。registry 升级后触发重标注 | 欧阳锋建议 3 |
| 4 | `labeled_by` | 块 | 标注者：ai / human / ai+human | 老顽童质量矩阵→黄药师翻译 |
| 5 | `labeled_at` | 块 | 标注时间戳 | 老顽童质量矩阵→黄药师翻译 |

### 标注管线架构（三段式升级版）

```
[Embedding 预筛] → [LLM 推理+评分] → [规则验证] → [路由]
    Top-10候选       每块给 confidence   格式/合法性    高(>0.85)→入库
    <100ms           score (0-1)         值合规检查     中(0.70-0.85)→抽检池
                                                      低(<0.70)→人工确认
```

### 质量控制体系（合并老顽童四维 + 欧阳锋时效性）

| 维度 | 指标 | KDO 做法 | 目标 |
|------|------|---------|:--:|
| **一致性** | AI 标注 vs Gold Standard | 欧阳锋手工标 10-20 条 chunk 做基准 | ≥ 85% |
| **准确性** | 金标准准确率 | 每批自动标注后对比 gold standard | ≥ 85% |
| **完整性** | 必标字段填充率 | frontmatter 校验（已有）+ 块属性校验（新增） | ≥ 99% |
| **可追溯性** | 标注来源 + 标注者 + 标注时间 | `labeled_by` + `labeled_at` + `label_version` | 全覆盖 |
| **时效性** | 数据新鲜度 | `last_reviewed_at` + `kdo lint --stale` | 月度自动检查 |

### 标签值总数

| 维度 | 值数 |
|------|:--:|
| domain | 5 |
| chunk_type | 19 |
| method_family | 11 |
| audience | 8 |
| perspective | 6 |
| platform | 6 |
| source_person | 12 |
| source_context_type | 9 |
| confidence | 4 |
| data_generation | 5 |
| error_root | 9 |
| expiry | 5 |
| value_tier | 3 |
| usage_depth | 5 |
| prerequisite_knowledge | 4 |
| **合计** | **111** |

每块实际激活 5-10 个标签（分层激活，不是全量）。在行业建议范围（3-8 个）的上限，但维度多是因为分层——同一 chunk 不会同时触发所有维度。

---

## 四、与三方共识的对照

| 共识点 | 状态 |
|--------|:--:|
| 数据是给 AI 吃的，评估标准是"AI 用了后产出变好" | ✅ 用户+欧阳锋+黄药师 |
| 湖仓架构：inbox=湖，wiki=仓 | ✅ |
| 暗知识独立管线：六字段模板替代三步编译法 | ✅ |
| 真原子粒度：30-200 字/块，主张/事实/规则级 | ✅ |
| 标签重心在块（80%）> 卡（20%） | ✅ 欧阳锋已转向 |
| 15 维度 110 标签值 | ⏳ **待用户+欧阳锋审查通过** |
| AI 自动标注 + 人工 20% 抽检（三段式路由） | ⏳ **待审查** |
| 老顽童报告的传统部分不适用于 KDO | ⏳ **待欧阳锋确认** |

---

## 五、下一步

| 步骤 | 谁 | 内容 |
|:--:|----|------|
| 1 | 用户 + 欧阳锋 | **审查本文件**。确认 15 维度方案和三段式管线 |
| 2 | 欧阳锋 | 手工标注 10-20 条 chunk 作为 Gold Standard |
| 3 | 黄药师 | 实现 `auto_label_chunk()` 三段式管线 |
| 4 | 黄药师 | 更新 `tag-registry.yaml` 到 v1.1（加入 includes/excludes 描述） |
| 5 | 三人 | Pilot 20 张卡 → 测标注准确率 → 达标后全量 |

---

## 六、相关文件索引

| 文件 | 作者 | 内容 |
|------|------|------|
| `30_wiki/concepts/data-labeling-best-practices-report.md` | 黄药师 | AI 时代标注最佳实践调研 |
| `kdo-15-dimension-label-spec.md` | 黄药师 | 15 维度方案 v1.0 |
| `labeling-research-alignment.md` | 黄药师 | 黄药师×老顽童 报告对齐 |
| `ouyangfeng-labeling-research-review.md` | 欧阳锋 | 2025-2026 行业验证 + 三个补充建议 |
| `数据标注维度最佳实践调研报告.md` | 老顽童 | 传统标注标准调研（inbox） |
| **本文件** | 黄药师 | **最终汇总** |

---

*黄药师 · 2026-05-31*
