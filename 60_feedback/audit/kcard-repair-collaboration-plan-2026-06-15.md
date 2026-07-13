# 30_wiki P0/P1 问题三人协作修复计划

> 生成日期：2026-06-15  
> 当前问题池：P0 402 张 / P1 982 张 / 完全干净 237 张（总 1,339）  
> 协作方：王语嫣（QA/协调）、黄药师（Builder/工具）、老顽童（Producer/内容）  
> 注：本计划仅涉及王语嫣、黄药师、老顽童三人，避免跨角色沟通成本。

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
| dangling 链接 | 中量 | related/`[[...]]` 指向不存在卡片 |
| confidence/trust 不匹配 | 少量 | 需人工复核 |

---

## 二、协作原则

1. **谁产的卡谁负责补**：OCR/课程/案例卡由老顽童补充；系统/决策/工具卡由黄药师补充
2. **能脚本化的不人工**：元数据、格式、链接问题由王语嫣用脚本批量处理
3. **P0 优先于 P1**：先让 enriched/reviewed/stable 卡合规，再治理 draft
4. **王语嫣每周跟进度**：运行门禁脚本、更新看板、标记阻塞、协调两人优先级
5. **三人闭环**：遇到需要架构裁决的问题，由黄药师和老顽童先各自给出方案，王语嫣汇总后请用户拍板

---

## 三、任务分配

### 3.1 黄药师

**定位**：Builder / 工具 owner / source 治理  
**核心能力**：schema、脚本、系统思维、source 映射、decision/proposal

| 优先级 | 任务 | 目标卡片数 | 预计耗时 | 产出 |
|---|---|---|---|---|
| P0 | 为 enriched/reviewed/stable 的 decision / proposal / system / improvement-plan 卡补充 source_refs 或 source_context | 约 30 | 1 人日 | 系统/决策类卡片 P0 清零 |
| P0 | 建立 `src_ID → 10_raw/sources/...` 映射索引 | 全局 | 0.5 人日 | `90_control/scripts/source-id-registry.py` |
| P0 | 修复 master 域 `contradicts` 字段系统性误用 | 10+ | 0.5 人日 | 知识图谱关系清洁 |
| P0 | 处理 design 域事实/合规风险卡（DPI、过审、薅羊毛） | 3 | 0.5 人日 | 修正或加风险说明 |
| P1 | 维护并增强 `kcard-quality-gate.py` | 全局 | 持续 | 门禁更准确 |
| P1 | 为 design / ai-saas / agent-infrastructure 域卡片补充 source 和 metadata | 约 50 | 2 人日 | P1 降低 |
| P1 | 裁决或提出重复卡片合并方案 | 8 组 design | 0.5 人日 | 与王语嫣、老顽童对齐后执行 |

**具体文件示例**：
- `decisions/kdo-priority-checklist.md`
- `decisions/proposal-kdo-flywheel-infrastructure.md`
- `systems/kdo-protocol.md`
- `systems/graph-rag-retrieval-layer.md`
- `concepts/skill-月白-印刷DPI标准设置.md`
- `concepts/skill-月白-AI电商图人工过审处理.md`
- `concepts/skill-月白-薅AIGC羊毛资源法.md`
- master 域所有 `dk-f*` / `dk-p*` / `dk-c*` 卡的 `contradicts`

---

### 3.2 老顽童

**定位**：Producer / 内容 owner / 一堂课程专家  
**核心能力**：内容理解、案例补充、OCR 校对、工具卡重写

| 优先级 | 任务 | 目标卡片数 | 预计耗时 | 产出 |
|---|---|---|---|---|
| P0 | OCR 卡片人工校对或确认删除 | yitang 域 13 + 其他若干 | 3 人日 | OCR 卡 P0 清零 |
| P0 | 重写 yitang 三张核心工具卡 | 3 | 2–3 人日 | 五步法 / 单元模型 / 259 里程碑达到 tool 标准 |
| P0 | 为 enriched/reviewed/stable 的 yitang 概念/工具/案例卡补充具体 source | 约 200 | 5 人日 | yitang 域 P0 大幅下降 |
| P1 | 处理 yitang/建模域卡片间重复/合并 | 5 组 | 1.5 人日 | 减少检索噪音 |
| P1 | 为 case 卡补充 outcome/数据或可验证标注 | 约 30 | 2 人日 | case 可信度提升 |
| P1 | 承担原洪七公的 OCR 图像校对任务 | 配合 OCR 卡 | 1 人日 | 若原图可访问则由老顽童校对 |

**具体文件示例**：
- `concepts/yt-entrepreneur-five-step-method.md`
- `concepts/yt-entrepreneur-unit-model.md`
- `concepts/yt-entrepreneur-259-milestone.md`
- `concepts/ocr-一堂-科学决策-深度-l4严格财务公式.md`
- `concepts/ocr-婚礼规划.md`
- `cases/case-一堂-无人餐厅-hypothesis-failure.md`
- `cases/case-dental-clinic-formula.md`
- `cases/case-thousand-people-square.md` / `concept-thousand-people-square.md`

---

### 3.3 王语嫣

**定位**：QA / 协调 / 脚本化批量修复  
**核心能力**：规则化扫描、报告生成、进度跟踪、低人工判断任务

| 优先级 | 任务 | 目标卡片数 | 预计耗时 |
|---|---|---|---|
| P0 | 继续修复剩余 author=unknown 中可推断的部分 | 146 中可推断部分 | 0.5 人日 |
| P0/P1 | 用脚本修复 dangling 链接、重复 frontmatter 字段、格式问题 | 全局 | 1 人日 |
| P1 | 为 draft/proposed 卡批量推断 author=legacy → 真实作者 | 约 700 | 1 人日（分批） |
| 每周 | 运行 `kcard-quality-gate.py`，更新看板 | 全局 | 0.2 人日 |
| 每周 | 检查黄药师/老顽童修复进度，标记阻塞项 | — | 0.2 人日 |
| 每月 | 抽样审查 20 张新增/修改卡片 | — | 0.5 人日 |
| 协调 | 汇总黄药师/老顽童的重复卡片合并方案，提交用户裁决 | 必要时 | — |

**王语嫣不做**：
- 需要看原图的 OCR 精确校对（由老顽童执行）
- 需要行业知识的决策/架构判断（由黄药师提出方案，用户拍板）

---

## 四、执行节奏

### 第 1 周：P0 止血

| 负责人 | 任务 | 目标 |
|---|---|---|
| 黄药师 | 补充 decision/proposal/system 卡 source | P0 减少 30 张 |
| 黄药师 | 处理 design 域 3 张高风险卡 | P0 减少 3 张 |
| 老顽童 | OCR 卡片统一校对前 5 张 | OCR P0 风险可控 |
| 王语嫣 | 推断剩余 author=unknown，修复 dangling 链接 | P0 减少 50 张 |
| 王语嫣 | 更新看板，明确两人周目标 | 看板状态清晰 |

### 第 2–3 周：核心内容补全

| 负责人 | 任务 | 目标 |
|---|---|---|
| 老顽童 | 重写 yitang 三张核心工具卡 | 核心工具卡达到可发布标准 |
| 老顽童 | OCR 卡片继续校对 | 完成 80% |
| 黄药师 | 建立 src ID 映射 + contradicts 修正 | 图谱关系清洁 |
| 黄药师 | 为 design/ai 域卡片补充 source | P1 降低 |
| 王语嫣 | 每周运行门禁脚本，跟踪进度 | 生成周度报告 |

### 第 4 周：验收与规则固化

| 负责人 | 任务 | 目标 |
|---|---|---|
| 王语嫣 | 运行门禁脚本，验收本周修复 | 生成月度报告 |
| 黄药师 | 根据修复经验修订 quality gate | 规则更贴合实际 |
| 老顽童 | 确认 yitang 域遗留问题 | 下月计划明确 |

---

## 五、检查点

| 检查点 | 时间 | 通过标准 |
|---|---|---|
| P0 < 200 | 1 周后 | source 为空、design 高风险卡、部分 OCR 修复完成 |
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

## 七、三人沟通规则

1. **每周五下班前**：王语嫣更新看板，@ 黄药师和老顽童下周 top 3 任务
2. **遇到阻塞**：黄药师/老顽童在看板对应项下评论，王语嫣 24 小时内响应
3. **需要用户拍板**：王语嫣汇总两种方案，提交用户决策，不直接找欧阳锋/洪七公
4. **修复完成后**：由王语嫣运行门禁脚本验证，不自行关闭看板项

---

## 八、风险与应对

| 风险 | 影响 | 应对 |
|---|---|---|
| 老顽童/黄药师时间有限 | 修复进度慢 | 优先 P0，P1 可延后；王语嫣每周提醒阻塞项 |
| author=unknown 的 146 张卡难以归属 | 可能长期滞留 | 王语嫣按 domain 分组后请两人认领；无人认领的保持 unknown + draft |
| source 原始材料缺失 | 无法补充 | 标记为 `source-lost`，降低 trust_level |
| 重复卡片合并方案不一致 | 影响知识体系 | 黄药师和老顽童各提一版，王语嫣汇总请用户拍板 |
| OCR 原图无法访问 | 无法精确校对 | 老顽童能校则校，不能校的保持 low trust / draft |

---

*本计划由王语嫣制定，协作方为黄药师、老顽童三人。*
