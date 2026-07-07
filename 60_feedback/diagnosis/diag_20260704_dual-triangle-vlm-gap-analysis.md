---
id: diag_20260704_dual-triangle-vlm-gap-analysis
title: 双三角 VLM 素材交叉验证与入库缺口诊断
type: diagnosis
status: draft
created_at: 2026-07-04
source: 00_inbox/人机协作双三角/_processed/ 全部 VLM 文件
method: 6层交叉验证
source_refs:
  - 00_inbox/人机协作双三角/_processed/vlm_summary.json
  - 00_inbox/人机协作双三角/_processed/一堂双三角-数字化营销提效十倍_vlm.md
  - 00_inbox/人机协作双三角/_processed/一堂双三角-IP选题智能体挑战交付上限_vlm.md
  - 00_inbox/人机协作双三角/_processed/一堂双三角-图书分析AI工具_vlm.md
  - 00_inbox/人机协作双三角/_processed/一堂双三角-AI企业经营数据分析_vlm.md
  - 00_inbox/人机协作双三角/_processed/一堂双三角-人生红点教练parther探索_vlm.md
  - 00_inbox/人机协作双三角/_processed/一堂双三角-龙虾训练实验_vlm.md
  - 00_inbox/人机协作双三角/_processed/一堂双三角-教育新官网制作_vlm.md
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

---

## 六、VLM→case 边界条件

将 VLM 输出转化为正式 case 卡时，必须同时满足以下边界条件，否则应退回原始素材或降级为 draft：

1. **六要素可映射**：VLM 中的关键信息能明确对应到双三角六要素（AI 落地五部曲、三阶六变、竞争力武器库、十年爬山地图、双三角预判画布、跨行业迁移），不存在无法归类的游离信息。
2. **决策/迭代过程完整**：案例必须包含「问题 → 决策 → 行动 → 结果/复盘」的闭环，不能只是观点或口号。
3. **关键事实可核验**：人名、公司名、业务数据、时间线等关键事实能与原始口述/课堂记录交叉核对。
4. **无已有卡重叠**：在 `30_wiki/` 中已存在同主题 reviewed 卡时，优先合并到已有卡，不重复建卡。
5. **来源可追溯**：case 卡的 `source_refs` 必须指向本诊断列出的 8 个 VLM 文件之一或原始口述稿。

## 七、失败模式

1. **把 VLM 标签当正文**：仅复制六要素标签，缺少叙事逻辑与决策细节，导致 case 卡空洞。
2. **未核验 OCR/VLM 提取结果**：将 VLM 误读的数字、人名、业务结论直接写入 case，造成事实失真。
3. **方法论与 case 混淆**：把「人类三角/AI三角维度展开」等方法论素材误判为独立案例。
4. **重复建卡**：未先查已有 Wiki 卡，导致同一知识点产生多张低质量 draft。
5. **将课堂轶事当作确定结论**：对 VLM 中「待验证」的课堂故事未加标注，直接写成正式结论。

## 八、When NOT to Use

- **不要**用本诊断中的 VLM 文件替代原始素材进行终审；VLM 只是提取草稿，原始素材才是权威来源。
- **不要**仅凭 VLM 标题就新建 case；必须先核对六要素映射与正文内容是否一致。
- **不要**把只有标题和标签、缺乏过程与结果的 VLM 片段直接 enrichment 为正式 case。
- **不要**在已有同主题 reviewed 卡存在时另建新卡；应通过 `related` 桥接或补充已有卡内容。

## 九、7 张拟建 case 与已有卡片桥接表

| 拟建 case ID | 来源 VLM | 可桥接的已有卡片 | 桥接说明 |
|:---|:---|:---|:---|
| `case-yihang-moufeimao-digital-marketing` | 一堂双三角-数字化营销提效十倍_vlm.md | `framework-yihang-dual-triangle-ai-landing-five-steps`、`framework-yihang-dual-triangle-weapon-library` | 营销提效对应 AI 落地五部曲与武器库选型 |
| `case-yihang-vikki-ip-topic-selection` | 一堂双三角-IP选题智能体挑战交付上限_vlm.md | `framework-yihang-dual-triangle-three-stages-six-changes`、`concept-yihang-dual-triangle-core` | IP 选题是「三阶六变」在内容生产中的具体应用 |
| `case-yihang-liukai-book-analysis` | 一堂双三角-图书分析AI工具_vlm.md | `tool-yihang-dual-triangle-canvas`、`framework-yihang-dual-triangle-weapon-library` | 图书分析工具是画布+武器库的组合实践 |
| `case-yihang-xujian-enterprise-data` | 一堂双三角-AI企业经营数据分析_vlm.md | `framework-yihang-dual-triangle-ai-landing-five-steps`、`framework-yihang-dual-triangle-ten-year-map` | 企业经营数据分析对应 AI 落地与长期能力地图 |
| `case-yihang-life-reddot-coach` | 一堂双三角-人生红点教练parther探索_vlm.md | `framework-yihang-dual-triangle-ten-year-map`、`tool-yihang-dual-triangle-canvas` | 人生红点教练是十年地图在个人决策场景的延伸 |
| `case-yihang-lobster-training` | 一堂双三角-龙虾训练实验_vlm.md | `framework-yihang-dual-triangle-weapon-library`、`framework-yihang-dual-triangle-three-stages-six-changes` | 龙虾训练实验展示武器库与三阶六变的训练闭环 |
| `case-yihang-yitang-edu-website` | 一堂双三角-教育新官网制作_vlm.md | `framework-yihang-dual-triangle-ai-landing-five-steps`、`case-yihang-dual-triangle-huazao-synthetic-data` | 新官网制作与花总跨行业案例共同构成「AI 落地五部曲」的企业级证据 |

*注：桥接表中的已有卡片均来自本诊断「VLM → 已有 Wiki 卡」一节，拟建 case 上线后应反向更新这些已有卡的 `related`。*
