---
id: task_20260708_wangyuyan-claude-retrospective-p0-fix
title: 'Claude 王语嫣回溯审计 P0 修复：元数据一致性与关键内容校准'
type: task
status: in_progress
owner: 王语嫣
assignee: kimi-code
reviewer: 欧阳锋
reviewed_by: 欧阳锋
priority: P0
created_at: 2026-07-08
updated_at: '2026-07-07T17:49:27.133950+00:00'
estimated_files: 10
dependencies: []
source_audit: 60_feedback/diagnosis/audit_20260708_wangyuyan-claude-retrospective.md
---

# Claude 王语嫣回溯审计 P0 修复：元数据一致性与关键内容校准

> 来源审计：`60_feedback/diagnosis/audit_20260708_wangyuyan-claude-retrospective.md`
> 目标：修正 2026-07-01 ~ 2026-07-05 期间 Claude 王语嫣编排的诊断报告与任务单中的 P0 级问题，避免卡片 ID 漂移、队列混乱和审计追溯断裂。
> 原则：只修正元数据和明确错误，不改已有卡片的正文内容；不改 reviewed 任务的终审结论。

---

## 一、任务目标

1. 修正时间管理域任务单重复问题。
2. 修正 4 个任务单的 frontmatter 日期/状态不一致问题。
3. 对齐 Y模型域卡片 ID（诊断 vs 任务单 vs 实际产出）。
4. 修正 retroactive case scan 的统计数字与 A/B/C 评级漂移。
5. 所有修改通过 `kdo lint` / `kdo pre-submit`（如适用），不产生新的死链或 frontmatter parse 错误。

---

## 二、待修复文件与具体动作

### 2.1 时间管理域任务单去重

**文件**：
- `60_feedback/tasks/task_20260701_wangyuyan-time-management-domain-orchestration.md`
- `70_product/tasks/task_20260701_wangyuyan-time-management-domain-orchestration.md`

**问题**：存在两份同名/同 ID 任务单，内容不同；60_feedback 版 YAML 格式错误（`related` 数组嵌套）。

**动作**：
1. 确认 `70_product` 版为唯一有效任务单（内容更完整、有 `estimated_cards`、与诊断报告一致）。
2. 将 `60_feedback` 版状态改为 `closed_merged`，并在正文顶部添加说明：「本任务单已合并至 `70_product/tasks/task_20260701_wangyuyan-time-management-domain-orchestration.md`，请勿以此版为准。」
3. 修复 60_feedback 版 YAML parse 错误，使其至少可被 `kdo lint` 解析。
4. 检查 production-queue.md / dashboard.md 中引用的路径是否指向 `70_product` 版；如有引用 60_feedback 版，统一修正。

---

### 2.2 Frontmatter 日期与状态不一致修复

**文件 1**：`60_feedback/tasks/task_20260702_laowantong-yitang-scientific-sales-methodology-production.md`

**问题**：
- `created_at: 2026-07-02`
- `updated_at: '2026-06-29T19:30:00+00:00'`
- `review_date: '2026-06-29'`（正文终审结论为 2026-07-02）
- 验收标准 checkbox 全未勾选，但 `status: reviewed`

**动作**：
1. 统一日期为 2026-07-02（created_at、updated_at、review_date）。
2. 将验收标准中已实际完成的 checkbox 改为 `- [x]`；未完成的项若已被覆盖，删除或说明。
3. 保持 `status: reviewed` 和 `reviewed_by: 欧阳锋` 不变。

**文件 2**：`60_feedback/tasks/task_20260703_laowantong-yitang-Y-model-foundation-production.md`

**问题**：
- `created_at: 2026-07-03`
- `updated_at: '2026-06-29T20:30:00+00:00'`
- `review_date: '2026-06-29'`（正文生产完成报告为 2026-07-03）

**动作**：统一日期为 2026-07-03。

**文件 3**：`60_feedback/tasks/task_20260702_laowantong-vikki-daxin-dark-knowledge-pilot-production.md`

**问题**：
- `created_at: 2026-07-02`
- `updated_at: 2026-07-01T17:55...`
- `review_date: 2026-07-01`（早于创建时间）

**动作**：统一日期为 2026-07-02。

**文件 4**：`60_feedback/tasks/task_20260702_laowantong-live81-ai-trademark-design-production.md`

**问题**：
- `created_at: 2026-07-02`
- `review_date: 2026-07-01`（早于创建时间）

**动作**：统一日期为 2026-07-02。

---

### 2.3 Y模型卡片 ID 对齐

**涉及文件**：
- `60_feedback/diagnosis/diag_20260703_yitang-Y-model-foundation.md`
- `60_feedback/tasks/task_20260703_laowantong-yitang-Y-model-foundation-production.md`
- `30_wiki/concepts/yt-decision-y-model.md`（已有产出卡片）

**问题**：诊断报告建议新建/重写为 `framework-yitang-Y-model`，任务单决定保留原 ID `yt-decision-y-model`，实际产出卡片也是 `yt-decision-y-model`。

**动作**：
1. 以实际产出为准，保留 `yt-decision-y-model` 作为最终卡片 ID。
2. 更新诊断报告 `diag_20260703_yitang-Y-model-foundation.md`：
   - 将「建议新建/重写为 `framework-yitang-Y-model`」改为「重写现有卡 `yt-decision-y-model`」。
   - 同步所有 `related` 建议中的卡片 ID。
3. 在诊断报告中增加说明：「任务单与终审采用原 ID `yt-decision-y-model`，本诊断此前的 `framework-yitang-Y-model` 为初稿建议，已对齐。」

---

### 2.4 Retroactive Case Scan 统计与评级校准

**涉及文件**：
- `60_feedback/diagnosis/diag_20260704_retroactive-case-scan-pilot.md`
- `60_feedback/tasks/task_20260703_wangyuyan-retroactive-case-scan-pilot.md`

**问题**：
1. 统计数字与实际列表不一致：诊断写「科学决策 551 / 泛产品设计 224 / 战略 205」，实际每域只列出 120 条。
2. A/B/C 评级跨域漂移：科学决策 A 级过宽，泛产品设计 A 级过严，战略域 A 级多取自 VLM 描述而非真实案例叙事。

**动作**：
1. 重新统计三个域的实际候选数量，修正诊断报告中的数字。
2. 按统一标准重新校准 A/B/C 评级：
   - A 级：有完整人物/动作/时间线/决策点/结果，可直接投产为 case 卡。
   - B 级：有案例骨架但缺 1-2 个要素，需补充素材。
   - C 级：只有观点/结论，缺少叙事细节，暂不入库。
3. 对战略域取自 `vlm_desc` 元描述的候选降级处理，优先从 OCR/口述稿中选取 A 级案例。
4. 在任务单中更新最终 A 级候选清单（如欧阳锋终审建议的 7 条），并补充 Top 5-7 条候选的 case 卡骨架。

---

## 三、验收标准

1. 所有待修复文件 `kdo lint` 0 ERROR（WARNING 可接受）。
2. 时间管理域只保留一个有效任务单；另一个已标记 `closed_merged` 且可解析。
3. 4 个任务单的 `created_at` / `updated_at` / `review_date` 时间顺序正确，无早于创建时间的 review_date。
4. 科学销售任务单 checkbox 状态与正文终审结论一致。
5. Y模型诊断报告中的卡片 ID 与实际产出 `yt-decision-y-model` 一致。
6. Retroactive case scan 统计数字与实际列表一致，A/B/C 评级按统一标准校准。
7. 不产生新的死链或 related 错误。
8. 全量修改通过欧阳锋终审。

---

## 四、风险与阻塞

| 风险 | 影响 | 应对 |
|------|------|------|
| 修改 reviewed 任务单的 frontmatter 被误认为改状态 | 触发审计争议 | 只改日期/source_refs/说明，不改 `status`、`reviewed_by`、`review_date` 代表的真实终审结论（仅修正录入错误） |
| 时间管理 60_feedback 版被其他文件引用 | 去重后路径失效 | 全局搜索 `task_20260701_wangyuyan-time-management-domain-orchestration.md`，统一改为 70_product 路径 |
| retroactive scan 评级重校引发争议 | 需要返工已投产 case 卡 | 本次只校准诊断与任务单中的评级，不追溯已 reviewed 的 case 卡；后续如要调整，另开 patch 任务 |

---

## 五、产出后动作

1. 老顽童完成修复并跑 `kdo lint`。
2. 将本任务状态改为 `pending_review`。
3. 欧阳锋按队列终审。
4. 终审通过后，王语嫣更新 `.agent/kb-evolution-direction.md`，增加一条纪律：任务单 frontmatter 日期需经一致性校验，诊断报告必须同步实际卡片 ID。
