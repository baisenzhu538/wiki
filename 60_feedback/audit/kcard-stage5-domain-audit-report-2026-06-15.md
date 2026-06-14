# 30_wiki 阶段 5 按 Domain 专项审查报告

**报告日期**：2026-06-15  
**审查角色**：王语嫣  
**覆盖范围**：30_wiki 全库 1,339 张卡片  
**本阶段目标**：按 Domain 维度识别系统性质量问题，重点覆盖 yitang、design、master 三个核心 domain。

---

## 一、本阶段前置修复

在进入 Domain 审查前，发现阶段 1 元数据治理遗留的 YAML 列表字段格式问题：

- `domain` 字段被错误保存为 `"['xxx']"` 字符串
- `tags` / `pipeline` / `related` 字段中包含 `None` 值

已执行批量修复：

- **修复文件数**：952 张
- **修复内容**：将字符串化列表恢复为正确列表、清理 `None` 值
- **修复脚本**：`90_control/scripts/fix-yaml-list-issues.py`
- **修复报告**：`60_feedback/audit/kcard-yaml-list-fix-report-2026-06-15.md`

修复后重新统计 Domain 分布：

| Domain | 卡片数 |
|---|---|
| yitang | 513 |
| design | 230 |
| master | 106 |
| ai-collaboration | 96 |
| ai-saas | 54 |
| healthcare | 53 |
| business-strategy | 49 |
| product | 46 |

---

## 二、审查样本

| Domain | 总卡片数 | 抽样数 | 审查方式 |
|---|---|---|---|
| yitang | 513 | 50 | 随机抽样 |
| design | 230 | 40 | 随机抽样 |
| master | 106 | 30 | 随机抽样 |

---

## 三、各 Domain 关键发现

### 3.1 yitang（一堂课程域，50 张抽样）

**整体印象**：两极分化严重。精修卡质量高，OCR 卡质量差却被统一标为 medium trust。

| 问题类型 | 涉及卡片数 | 严重程度 |
|---|---|---|
| OCR 质量缺陷 | 13 | 高 |
| Confidence/Trust 高估 | 15 | 高 |
| 内容空泛/缺乏定义 | 16 | 高 |
| Source 笼统/不可读 | 11 | 中 |
| 卡片间重复/未合并 | 8 | 中 |
| 文件内容损坏 | 1 | 高 |

**最大风险点**：
1. OCR 卡片统一标注 `confidence: 0.8` / `trust_level: medium`，会误导下游引用
2. 核心工具卡空心化：`yt-entrepreneur-five-step-method`、`yt-entrepreneur-unit-model`、`yt-entrepreneur-259-milestone` 内容单薄
3. `yt-decision-depth-ladder.md` 被异常行号前缀污染

### 3.2 design（设计域，40 张抽样）

**整体印象**：头轻脚重。3 张 dk/concept 卡质量较高，37 张 skill 卡大量源自同一套模板，source 几乎全空。

| 问题类型 | 涉及卡片数 | 严重程度 |
|---|---|---|
| Source 可验证性不足 | 37 | 高 |
| 内容完整性不足 | 约 30 | 高 |
| Skill 类型检查缺陷 | 36 | 高 |
| 卡片间重复/冲突 | 8 组 | 中 |
| Confidence/Trust 不一致 | 3 | 中 |
| 事实/合规风险 | 3 | 高 |

**最大风险点**：
1. **92.5% 的 skill 卡片 source_refs 为空**，无法审计和更新
2. `skill-月白-印刷DPI标准设置` 数值疑似与行业常识相反
3. `skill-月白-AI电商图人工过审处理` 和 `skill-月白-薅AIGC羊毛资源法` 存在合规风险
4. 8 组重复主题卡片（提示词、PPT、参考图等）造成检索噪音

### 3.3 master（通用能力域，30 张抽样）

**整体印象**：中等质量。暗知识卡结构较好，但 `contradicts` 字段被系统性误用，decision/proposal 卡 source 缺失。

| 问题类型 | 涉及卡片数 | 严重程度 |
|---|---|---|
| Source 可验证性不足 | 8 | 中 |
| 内容完整性不足 | 7 | 中 |
| Frontmatter/格式问题 | 6 | 中 |
| 卡片间关系标注错误 | 12+ | **高** |
| Domain 一致性 | 3 | 中 |
| Confidence/Trust 校准 | 3 | 中 |

**最大风险点**：
1. **`contradicts` 字段系统性误用**：大量暗知识卡把“相关/纠正”关系标为“矛盾”，污染知识图谱
2. `dk-yb20-ai-eye-high-principle` 内容严重不足
3. `ocr-婚礼规划` OCR 质量差且被错误标记为 enriched
4. 单元模型工具 domain 标注缺少 `yitang`

---

## 四、跨 Domain 共性问题

| 共性问题 | 表现 | 影响 |
|---|---|---|
| OCR 卡质量问题 | 乱码、断行、视觉结构丢失、内容空泛 | 污染检索结果，误导引用 |
| source_refs 缺失 | design 92.5% skill 卡、master 多 decision/proposal 卡无 source | 无法审计、无法更新 |
| 卡片间重复 | 同一主题 OCR 版与精修版并存、design 多组重复 skill | 检索噪音、版本混乱 |
| 关系字段误用 | `contradicts` 被用于非矛盾关系 | 知识图谱污染 |
| 类型与内容不匹配 | 课程清单标为 concept、单元模型标为 tool 但缺步骤 | 用户找不到合适卡片 |
| Confidence/Trust 虚高 | OCR 卡、内容单薄卡被标 medium/high | 降低知识库可信度 |
| 事实/合规风险 | DPI 标准错误、规避检测、薅羊毛 | 实际损失和法律风险 |

---

## 五、批量处理建议

### 5.1 可脚本化批量处理

| 批量任务 | 处理策略 | 预期效果 |
|---|---|---|
| OCR 卡统一降级 | 对 `id` 以 `ocr-` 开头、source 薄弱、reviewed_by=pending 的卡片，confidence 降至 ≤0.6，trust_level 降至 low | 消除 OCR 卡误导信号 |
| `contradicts` 字段审计 | 输出所有 `contradicts` 指向 `master-*` / `yt-*` 概念卡的清单 | 定位关系误用 |
| source_refs 缺失扫描 | 按 type 分组列出空 source 卡片 | 定位补源优先级 |
| 重复章节检测 | 检测同一文件中重复出现的“不要用的场景”“外部攻击”“Critique”等 | 清理模板残留 |
| Markdown 语法检查 | 检测未闭合 `**`、异常行号前缀 `"|"`、转义引号 `"` | 修复渲染异常 |
| 重复主题聚类 | 基于标题关键词做相似度聚类 | 发现疑似重复卡片 |
| Domain 标注规范化 | 统一 `yitang` / `entrepreneur` / `business-strategy` 的归属规则 | 提升检索准确性 |

### 5.2 必须人工判断处理

| 任务 | 原因 | 建议执行者 |
|---|---|---|
| OCR 文本与原图校对 | 需要对照原图确认 OCR 误识 | 洪七公 / 老顽童 |
| 核心工具卡重写 | 五步法、单元模型、259 里程碑需要领域知识补全 | 老顽童 / 黄药师 |
| 重复卡片合并 | 涉及知识架构设计 | 欧阳锋 / 内容负责人 |
| 事实/合规核查 | DPI 标准、规避检测、薅羊毛等需专业判断 | 行业专家 / 法务 |
| Source 溯源到原始课程 | 需要人工追踪具体课程材料 | 黄药师 / 老顽童 |
| `contradicts` 语义修正 | 需要理解卡片实际逻辑关系 | 欧阳锋 / 审查员 |

---

## 六、优先处理建议（P0–P2）

| 优先级 | 行动项 | 责任方 | 预计工作量 |
|---|---|---|---|
| P0 | 对所有 `ocr-*` 卡片统一复核或降级 | 领域 owner + OCR 校对员 | 2-3 人日 |
| P0 | 重写/补全 yitang 三张核心工具卡 | 老顽童 / 黄药师 | 3-5 人日 |
| P0 | 审计并修正 `contradicts` 字段误用 | 欧阳锋 / 审查员 | 1-2 人日 |
| P0 | 核查 design 三张高风险卡片（DPI、过审、薅羊毛） | 行业专家 / 法务 | 0.5-1 人日 |
| P1 | 为 design 37 张空 source skill 卡补 source | 月白 / 老顽童 | 3-5 人日 |
| P1 | 清理 `yt-decision-depth-ladder.md` 行号污染 | 技术编辑 | 0.5 人日 |
| P1 | 合并/互链 design 8 组重复主题卡片 | 内容负责人 | 2-3 人日 |
| P2 | 建立各 domain confidence/trust 评分 rubric | QA + 领域 owner | 1 人日 |
| P2 | 运行死链扫描并修复 | 技术编辑 | 0.5 人日 |

---

## 七、下阶段计划（阶段 6）

**目标**：建立持续质量控制机制，防止问题复发。

**执行方式**：
1. 制定《KDO 卡片入库自检清单》
2. 建立自动化门禁脚本：
   - 新增卡片必须包含 source_refs
   - pipeline 含 `verified-by-case` 必须正文有 case/outcome
   - `contradicts` 字段必须人工复核
   - OCR 卡默认 trust_level=low
3. 建立周期性审查机制（每月/每季度）
4. 建立问题卡片跟踪看板

---

## 附录：相关文件

- yitang 审查：`stage5-domain-reviews/domain-yitang-sample-review.md`
- design 审查：`stage5-domain-reviews/domain-design-sample-review.md`
- master 审查：`stage5-domain-reviews/domain-master-sample-review.md`
- YAML 列表字段修复报告：`kcard-yaml-list-fix-report-2026-06-15.md`
- 阶段 4 报告：`kcard-stage4-trust-layer-report-2026-06-15.md`
