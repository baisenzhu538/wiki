# 30_wiki 阶段 3 按作者深度审查报告

**报告日期**：2026-06-15  
**审查角色**：王语嫣  
**覆盖范围**：30_wiki 全库 1,320 张卡片  
**本阶段目标**：按作者维度对老顽童、黄药师的真实 author 卡片及黄药师 review 的 legacy 卡片进行深度审查，识别系统性质量问题并给出批量处理建议。

---

## 一、审查范围与方法

| 作者/Review 角色 | 总卡片数 | 审查样本数 | 审查方式 |
|---|---|---|---|
| 老顽童（真实 author） | 54 | 54（全覆盖） | 按 domain/type 分 4 组并行审查 |
| 黄药师（真实 author） | 13 | 13（全覆盖） | 全量深度审查 |
| 黄药师 review 的 legacy | 163 | 40（抽样） | 随机抽样深度审查 |

分组方式：
- 老顽童 cases：16 张
- 老顽童 AI 短剧：7 张
- 老顽童建模能力域：24 张
- 老顽童 other（frameworks + concepts + tools）：7 张

---

## 二、老顽童卡片审查结果

### 2.1 总体印象

老顽童的 54 张卡片整体结构规范，多数具备清晰的 Protocol、Claims、Constraints、Critique、Sources 等模块，方法论体系感强。但存在以下系统性风险：

1. **自审痕迹明显**：所有卡片的 `author` 与 `reviewed_by` 均为老顽童，且 `review_date` 与 `created_at` 相同，缺乏独立 reviewer。
2. **同源集中风险**：大量卡片共享同一个 source `src_20260614_8269ccdb`（一堂建模能力培训 Truman 口述），若源材料存在偏差，将系统性影响多张卡片。
3. **术语与边界冲突**：同主题卡片之间存在重复定义、步骤数冲突、术语混用。

### 2.2 分组关键发现

#### cases（16 张）

| 问题类型 | 涉及卡片数 | 严重程度 |
|---|---|---|
| Case outcome 可验证性不足 | 8 | 中 |
| Source 路径格式不一致 | 6 | 低 |
| Confidence/Trust 与证据不匹配 | 3 | 中 |
| 卡片间冲突/重复 | 4 | **高** |
| 类型模板不匹配 | 1 | 中 |

**重点问题**：
- `case-course-milestone-model`（六步）与 `framework-course-milestone-model`（七步）步骤数冲突
- `case-thousand-people-square` 与 `concept-thousand-people-square` 内容高度重叠
- "千人广场"与"销冠广场"、"5% after"与"5% 专家"术语混用

#### AI 短剧（7 张）

| 问题类型 | 问题数 | 严重程度 |
|---|---|---|
| 内容完整性 | 2 | 中 |
| Source 可验证性 | 3 | 中 |
| Confidence/Trust | 2 | 低 |
| 卡片间关系 | 1 | 低 |
| 类型特定检查 | 2 | 中 |

**重点问题**：
- `ai-short-drama-platform-policy-comparison` 名为平台政策对比，但未在正文呈现具体对比数据（分成比例、投稿入口、结算周期等），必须补全数据表
- 拆本罗盘、框架三板斧、剧本策划三板斧的核心 claims 缺少精确 transcript 行号

#### 建模能力域（24 张）

| 问题类型 | 涉及卡片数 | 严重程度 |
|---|---|---|
| 跨卡片 dangling 链接 | 17 | **高** |
| 卡片间内容重叠/边界模糊 | 4 | **高** |
| Source 引用与 frontmatter 不一致 | 2 | **高** |
| 卡片内部重复内容 | 1 | 中 |
| 无明显问题 | 7 | — |

**重点问题**：
- 70.8% 的卡片引用了当前知识库中不存在的卡片
- `modeling-capability-system` 与 `modeling-three-stages` 内容高度重叠
- `modeling-capability-system` / `modeling-level-map` / `modeling-personal-practice-loop` 对 L1-L6 段位定义重复
- `tool-essence-nfactor-modeling` 和 `tool-sabc-tier-modeling` 引用了未在 frontmatter 注册的 source

#### other（7 张）

| 问题类型 | 涉及卡片数 | 严重程度 |
|---|---|---|
| Source 形式不一致 | 2 | 中 |
| Confidence/Trust 缺失或不一致 | 2 | 中 |
| 案例/数据支撑不足 | 2 | 中 |
| 卡片间概念重叠 | 2 | 中 |
| 元数据缺失/状态不一致 | 2 | 中 |
| 内容表述瑕疵 | 2 | 低 |

**重点问题**：
- `yt-unit-model-overview`：`status=reviewed` 但 `reviewed_by` 为空，且缺少 confidence/trust_level
- `yt-tool-ai-ppt-maker`：source_refs 使用文件路径而非 `src_` ID，存在错别字"一弖00字"，缺少 confidence
- `tool-iterative-recursive-deep-dig` 与 `tool-ai-skill-engineering-method` 核心概念"喷—撞—改"高度重叠，层级关系不清

---

## 三、黄药师卡片审查结果

### 3.1 真实 author 卡片（13 张）

| 问题类型 | 出现次数 | 涉及卡片数 |
|---|---|---|
| source_refs 缺失 | 6 | 7 |
| confidence/trust_level 缺失 | 7 | 7 |
| frontmatter 状态与正文不一致 | 3 | 3 |
| 数据/结果可验证性不足 | 3 | 3 |
| 阈值或映射关系缺乏依据 | 3 | 3 |
| 推测性内容未标注置信度 | 2 | 2 |

**重点问题**：
- `decisions/label-accuracy-standard-alignment`、`decisions/proposal-deep-synthesis-infrastructure`、`decisions/sprint-6-cli-gap-proposal` 正文中已有欧阳锋"批准/回应"，但 frontmatter 仍为 `reviewed_by: pending`
- `decisions/agent-ecosystem-design`、`decisions/proposal-kdo-flywheel-infrastructure`、`decisions/truman-ai-partner-design-analysis` 等 draft/proposal 卡无 source_refs 和 confidence
- `systems/kdo-batch-produce-req014` 创建于 2026-05-04，status 仍为 `proposed`，一个多月未更新执行状态

### 3.2 Review 的 legacy 卡片（40 张抽样）

| 问题类型 | 涉及卡片数 | 占比 |
|---|---|---|
| Source 溯源不足/不可验证 | 24 | 60% |
| YAML/元数据质量 | 12 | 30% |
| 内容课程介绍化/空泛 | 8 | 20% |
| 类型标注与内容不匹配 | 8 | 20% |
| 重复/冲突/过时 | 5 | 12.5% |
| Confidence/Trust 一致性 | 9 | 22.5% |
| 模板重复/冗余段落 | 7 | 17.5% |

**重点问题**：
- 大量课程衍生卡片只引用通用 `一堂-课程地图精华串讲.md`，未指向具体课程原文
- 多张卡片 YAML 存在重复键、`null` 字段、字段名拼写错误（如 `review_by` 应为 `review_date`）
- `entities/紫鲸AI.md` YAML 结构损坏
- `yt-model-prediction-model` 已被新版替代但未标记 `deprecated`
- `yt-research-weaponry-course` 与 `yt-entrepreneur-research-camp` 内容重叠

---

## 四、跨作者共性问题

| 共性问题 | 表现 | 影响 |
|---|---|---|
| Source 格式不统一 | `.md` / `.txt` / `src_ID` / 文件路径 混用 | 脚本化追溯困难 |
| Frontmatter 状态与正文不一致 | `reviewed_by: pending` 但正文已"批准" | 元数据不可信 |
| Confidence/Trust 缺失或不匹配 | 单来源口述标 0.90、draft 卡无 confidence | 读者无法判断可信度 |
| 卡片间重复/冲突 | 同主题多卡定义不同、步骤数冲突 | 知识体系混乱 |
| 术语不统一 | 千人广场/销冠广场、5% after/5% 专家 | 增加读者理解成本 |
| Dangling 链接 | 大量 related/[[...]] 指向不存在的卡片 | 知识网络断裂 |
| 模板重复 | "不要用的场景"、Taleb/Simon 批判段落重复 | 信息密度低 |

---

## 五、批量处理建议

### 5.1 可脚本化批量处理

| 批量任务 | 处理规则 | 预期效果 |
|---|---|---|
| Dangling 链接扫描 | 提取所有 `[[...]]` 与 frontmatter `related`，比对实际文件 | 定位断裂链接 |
| Source 格式统一 | 统一 Sources 区块路径格式为 `src_ID:line-line` 或可解析路径 | 消除格式混用 |
| Frontmatter 状态不一致检测 | 扫描 `reviewed_by: pending` 但正文含"采纳/批准/回应"的卡片 | 发现状态错误 |
| Date 字段不一致检测 | 扫描 `date` / `created_at` / `updated_at` / `review_date` 矛盾 | 发现元数据错误 |
| 高置信低来源检测 | `confidence ≥ 0.90` 但 `source_refs` 数量 < 2 | 发现 confidence 虚高 |
| YAML 重复键清理 | 检测重复 `updated_at`、`tags` 等键 | 修复 YAML 结构 |
| Null 字段清理 | 将 `tags`、`pipeline` 中的 `null` 清空 | 规范元数据 |
| 模板重复段落检测 | 检测同一文件中"不要用的场景"等重复段落 | 定位冗余内容 |

### 5.2 必须人工判断处理

| 任务 | 原因 |
|---|---|
| 重叠卡片边界重定义 | `modeling-capability-system` / `modeling-three-stages` / `modeling-level-map` 需要重新定义职责 |
| 术语统一 | 千人广场/销冠广场、5% 定义需要领域专家决策 |
| 六步/七步里程碑冲突确认 | 需要确认一堂当前官方流程 |
| 已批准提案状态更新 | 需确认欧阳锋的回应是否构成正式批准 |
| 案例数据补充 | 需要核对原始课程材料或公开资料 |
| 类型重分类 | 大量 `tool`/`concept`/`framework` 边界模糊 |

---

## 六、下阶段计划（阶段 4）

**目标**：按可信度分层审查，重点处理 confidence/trust_level 标注问题。

**理由**：
- 阶段 3 发现大量 confidence 虚高、trust_level 缺失、frontmatter 状态与正文不一致的问题
- 这些元数据问题直接影响用户对知识库的信任
- 规则清晰，适合批量脚本化处理

**执行方式**：
1. 批量修正 `reviewed_by: pending` 但正文已批准的卡片
2. 批量下调高置信低来源卡片的 confidence
3. 批量补充缺失的 confidence/trust_level
4. 对无法脚本化判断的卡片生成人工复核清单

---

## 附录：相关文件

- 老顽童 cases 审查：`stage3-author-reviews/laowantong-cases-review.md`
- 老顽童 AI 短剧审查：`stage3-author-reviews/laowantong-ai-short-drama-review.md`
- 老顽童建模审查：`stage3-author-reviews/laowantong-modeling-review.md`
- 老顽童 other 审查：`stage3-author-reviews/laowantong-other-combined-review.md`
- 黄药师真实 author 审查：`stage3-author-reviews/huangyaoshi-author-all-review.md`
- 黄药师 review legacy 抽样审查：`stage3-author-reviews/huangyaoshi-review-legacy-sample-review.md`
- 阶段 2 报告：`kcard-stage2-audit-report-2026-06-15.md`
