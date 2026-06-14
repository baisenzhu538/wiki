# 30_wiki P0/P1 问题协作修复计划

> 生成日期：2026-06-15  
> 当前问题池：P0 402 张 / P1 982 张 / 完全干净 237 张（总 1,339）  
> 协调人：王语嫣

---

## 一、当前问题分布

### 1.1 P0 阻塞问题（402 张）

| 问题类型 | 数量 | 说明 |
|---|---|---|
| enriched/reviewed/stable/active 卡 source_refs 为空 | 约 250 | 已通过阶段 4 填充 confidence/trust，但 source 仍需补充 |
| author=unknown（无法推断） | 146 | 阶段 6 批量修复 legacy author 时无法识别真实作者 |
| 少量其他 P0 | 约 10 | id 不一致、status/reviewed_by 冲突等 |

> 注：4 个"YAML 错误"实际是无 frontmatter 的索引文件（index.md / cases/index.md / links/index.md / concept-card-index-latest.md），非知识卡。

### 1.2 P1 修复问题（982 张）

| 问题类型 | 数量 | 说明 |
|---|---|---|
| draft/proposed 卡 source_refs 为空 | 大量 | 可在提升状态前补充 |
| author=legacy（draft 状态） | 约 700 | 需要逐步替换为真实作者 |
| dangling 链接 | 中量 | related/[[...]] 指向不存在卡片 |
| confidence/trust 不匹配 | 少量 | 需人工复核 |

---

## 二、协作原则

1. **谁产的卡谁负责补**：OCR/课程/案例卡由原始作者或内容 owner 补充
2. **能脚本化的不人工**：元数据、格式、链接问题由脚本批量处理
3. **P0 优先于 P1**：先让 enriched/reviewed/stable 卡合规，再治理 draft
4. **王语嫣每周跟进度**：运行门禁脚本、更新看板、标记阻塞

---

## 三、任务分配

### 3.1 黄药师（Builder / 工具 owner）

**适合他的**：需要 schema、脚本、系统思维、source 映射的工作

| 优先级 | 任务 | 目标卡片数 | 预计耗时 | 产出 |
|---|---|---|---|---|
| P0 | 为 enriched/reviewed/stable 的 decision / proposal / system / improvement-plan 卡补充 source_refs 或 source_context | 约 30 | 1 人日 | 这些卡片的 P0 清零 |
| P0 | 建立 `src_ID → 10_raw/sources/...` 映射索引 | 全局 | 0.5 人日 | `90_control/scripts/source-id-registry.py` |
| P0 | 修复 `contradicts` 字段系统性误用 | master 域 10+ | 0.5 人日 | related 关系修正 |
| P1 | 维护并增强 `kcard-quality-gate.py` | 全局 | 持续 | 每月报告更准确 |
| P1 | 为 design / ai-saas / agent-infrastructure 域卡片补充 source 和 metadata | 约 50 | 2 人日 | P1 降低 |

**具体文件示例**：
- `decisions/kdo-priority-checklist.md`
- `decisions/proposal-kdo-flywheel-infrastructure.md`
- `systems/kdo-protocol.md`
- `systems/graph-rag-retrieval-layer.md`
- master 域所有 `dk-f*` / `dk-p*` / `dk-c*` 卡的 `contradicts`

---

### 3.2 老顽童（Producer / 内容 owner）

**适合他的**：需要内容理解、案例补充、OCR 校对、工具卡重写的工作

| 优先级 | 任务 | 目标卡片数 | 预计耗时 | 产出 |
|---|---|---|---|---|
| P0 | OCR 卡片人工校对或确认删除 | yitang 域 13 + 其他 若干 | 3 人日 | OCR 卡 P0 清零 |
| P0 | 重写 yitang 三张核心工具卡 | 3 | 2–3 人日 | 五步法 / 单元模型 / 259 里程碑达到 tool 标准 |
| P0 | 为 enriched/reviewed/stable 的 yitang 概念/工具/案例卡补充具体 source | 约 200 | 5 人日 | yitang 域 P0 大幅下降 |
| P1 | 处理卡片间重复/合并 | 8 组 design + 5 组成建模/yitang | 2 人日 | 减少检索噪音 |
| P1 | 为 case 卡补充 outcome/数据或可验证标注 | 约 30 | 2 人日 | case 可信度提升 |

**具体文件示例**：
- `concepts/yt-entrepreneur-five-step-method.md`
- `concepts/yt-entrepreneur-unit-model.md`
- `concepts/yt-entrepreneur-259-milestone.md`
- `concepts/ocr-一堂-科学决策-深度-l4严格财务公式.md`
- `cases/case-一堂-无人餐厅-hypothesis-failure.md`
- `cases/case-dental-clinic-formula.md`

---

### 3.3 欧阳锋（Architect / 裁决者）

**适合他的**：需要架构判断和最终拍板的工作

| 优先级 | 任务 | 说明 |
|---|---|---|
| P0 | 裁决重复卡片合并 | 千人广场/销冠广场、六步/七步里程碑、design 重复主题 |
| P0 | 审定 domain 规范 | yitang / entrepreneur / business-strategy 边界 |
| P1 | 确认已批准提案状态 | 黄药师 decisions 中正文明说批准但 frontmatter pending 的卡片 |
| P1 | 审定 contradicts 关系修正结果 | 抽检黄药师的修正 |

---

### 3.4 洪七公（Visual / OCR）

**适合他的**：图像/视觉相关校对

| 优先级 | 任务 | 目标卡片 |
|---|---|---|
| P0 | OCR 图像校对 | `concepts/ocr-婚礼规划.md` 等含原图的 OCR 卡 |
| P1 | 清理 Visual Analysis 噪音 | `tools/yt-unit-model-selection.md` 等视觉描述过长的工具卡 |

---

### 3.5 王语嫣（QA / 协调）

| 频率 | 任务 |
|---|---|
| 每周 | 运行 `kcard-quality-gate.py`，更新看板 |
| 每周 | 检查黄药师/老顽童修复进度，标记阻塞 |
| 每月 | 抽样审查 20 张新增/修改卡片 |
| 每季度 | 输出质量趋势报告，修订 quality gate 规则 |

---

## 四、执行节奏

### 第 1 周：P0 止血

| 负责人 | 任务 | 目标 |
|---|---|---|
| 黄药师 | 补充 decision/proposal/system 卡 source | P0 减少 30 张 |
| 老顽童 | OCR 卡片统一降级/校对前 5 张 | OCR P0 风险可控 |
| 欧阳锋 | 裁决 3 组最高优先级重复卡片 | 减少冲突 |
| 王语嫣 | 更新看板，分配任务 | 看板状态清晰 |

### 第 2–3 周：核心内容补全

| 负责人 | 任务 | 目标 |
|---|---|---|
| 老顽童 | 重写 yitang 三张核心工具卡 | 核心工具卡达到可发布标准 |
| 老顽童 | OCR 卡片继续校对 | 完成 80% |
| 黄药师 | 建立 src ID 映射 + contradicts 修正 | 图谱关系清洁 |
| 洪七公 | 配合 OCR 校对 | 完成图像相关卡 |

### 第 4 周：验收与规则固化

| 负责人 | 任务 | 目标 |
|---|---|---|
| 王语嫣 | 运行门禁脚本，验收本周修复 | 生成周度报告 |
| 黄药师 | 根据修复经验修订 quality gate | 规则更贴合实际 |
| 欧阳锋 | 审定遗留架构问题 | 季度方向明确 |

---

## 五、检查点

| 检查点 | 时间 | 通过标准 |
|---|---|---|
| P0 < 200 | 1 周后 | source 为空、author=unknown 等快速修复完成 |
| P0 < 100 | 2 周后 | OCR 卡、核心工具卡、decision/proposal 卡基本修复 |
| P0 ≈ 0 | 1 个月后 | 仅剩需要深度内容重构的少数卡片 |
| 干净卡片 > 500 | 1 个月后 | 全库 1/3 卡片通过门禁 |

---

## 六、工具与看板

| 工具 | 路径 | 用途 |
|---|---|---|
| 质量门禁脚本 | `90_control/scripts/kcard-quality-gate.py` | 每周扫描 |
| 自检清单 | `90_control/quality-gates/kcard.md` | 新卡入库标准 |
| 问题看板 | `60_feedback/audit/kcard-issues-board-2026-06-15.md` | 跟踪所有问题 |
| 审查机制 | `90_control/workflows/kcard-quality-review.md` | 月度/季度流程 |
| 本次修复报告 | `60_feedback/audit/kcard-yaml-errors-fix-v3-report-2026-06-15.md` | YAML 修复记录 |
| 本次修复报告 | `60_feedback/audit/kcard-legacy-author-fix-report-2026-06-15.md` | author 修复记录 |
| 本次修复报告 | `60_feedback/audit/kcard-ocr-cards-downgrade-report-2026-06-15.md` | OCR 降级记录 |

---

## 七、风险与应对

| 风险 | 影响 | 应对 |
|---|---|---|
| 老顽童/黄药师时间有限 | 修复进度慢 | 优先 P0，P1 可延后；王语嫣每周提醒阻塞项 |
| author=unknown 的 146 张卡难以归属 | 可能长期滞留 | 按 domain 分组后请各 owner 认领；无人认领的保持 unknown + draft |
| source 原始材料缺失 | 无法补充 | 标记为 `source-lost`，降低 trust_level |
| 重复卡片合并引发争议 | 影响知识体系 | 欧阳锋裁决，必要时开会讨论 |

---

*本计划由王语嫣基于阶段 0–6 审查结果制定，待欧阳锋审定后执行。*
