---
id: task_20260708_wangyuyan-claude-retrospective-p1-supplement
type: task
status: reviewed
review_verdict: pass
review_grade: A
review_notes: 17/17 pre-submit PASS。四项补全（source_refs行号精确化、外部URL附录、诊断深度补充、交叉比对表）全部到位。
owner: 王语嫣
assignee: kimi-code
reviewer: 欧阳锋
reviewed_by: 欧阳锋
priority: P1
created_at: 2026-07-08
updated_at: '2026-07-08T02:50:00+00:00'
estimated_files: 16
dependencies:
- task_20260708_wangyuyan-claude-retrospective-p0-fix
source_audit: 60_feedback/diagnosis/audit_20260708_wangyuyan-claude-retrospective.md
---

# Claude 王语嫣回溯审计 P1 补全：source_refs 行号、外部验证与诊断深度

> 来源审计：`60_feedback/diagnosis/audit_20260708_wangyuyan-claude-retrospective.md`
> 前置：#134 P0 修复完成后启动
> 目标：为 2026-07-01 ~ 2026-07-05 期间的诊断报告和任务单补充 source_refs 精确行号、外部 URL、自攻击/失败模式，并补齐与已有 KDO 卡的交叉比对。
> 原则：只追加/修正诊断与任务单，不改已有卡片的正文内容；不改 reviewed 任务的终审结论。

---

## 一、任务目标

1. 为 7 份诊断报告和对应任务单补充带行号范围的 `source_refs`。
2. 为声称做了「全网调研」的任务补充外部 URL/文献引用（YAI 蒸馏）。
3. 为试点/草稿类诊断补充九层深挖、自攻击/失败模式或边界说明。
4. 补充诊断与已有 KDO 卡的交叉比对表。
5. 所有修改通过 `kdo lint`。

---

## 二、待补全文件清单

### 2.1 source_refs 精确化（必须精确到文件 + 行号）

| 诊断/任务单 | 关键素材 | 备注 |
|---|---|---|
| `diag_20260701_time-management-nine-layer-isomorphism.md` | `00_inbox/时间管理/时间管理-*-口述.txt`、笔记、VLM 描述 | 补充关键引语行号 |
| `diag_20260701_time-management-validation.md` | 同上 | 补充关键引语行号 |
| `70_product/tasks/task_20260701_wangyuyan-time-management-domain-orchestration.md` | 同上 | 移除已有卡片 `yt-personal-time-management` 作为 source_refs |
| `diag_20260702_vikki-daxin-dark-knowledge-extraction.md` | `0071Vikki战队...md`、`0017大馨战队...md` | 为 22 条暗知识补充行号 |
| `60_feedback/tasks/task_20260702_laowantong-vikki-daxin-dark-knowledge-pilot-production.md` | 同上 | 同步 source_refs |
| `diag_20260702_live81-ai-trademark-design.md` | `00_inbox/yitang-AI club/live81/*` | 补充关键案例/法律边界行号 |
| `60_feedback/tasks/task_20260702_laowantong-live81-ai-trademark-design-production.md` | 同上 | 同步 source_refs |
| `diag_20260702_yitang-scientific-sales-methodology.md` | `00_inbox/销售专题/*` | 补充 SABC、六维激励等关键段落的行号 |
| `60_feedback/tasks/task_20260702_laowantong-yitang-scientific-sales-methodology-production.md` | 同上 | 同步 source_refs |
| `diag_20260703_yitang-Y-model-foundation.md` | `00_inbox/底层逻辑之一-Y模型/*` | 补充四层结构、引擎层等关键行号 |
| `diag_20260704_dual-triangle-vlm-gap-analysis.md` | `00_inbox/人机协作双三角/_processed/*.md` | 列出关键 VLM 文件和六要素映射位置 |
| `60_feedback/tasks/task_20260704_laowantong-dual-triangle-vlm-case-enrichment.md` | 同上 | 补全 frontmatter：estimated_cards、source_refs、related |
| `diag_20260705_dual-triangle-domain-orchestration.md` | 双三角口述稿、课后闲聊记录 | 列出源文件和关键行号 |
| `60_feedback/tasks/task_20260705_wangyuyan-agent-distillation-method.md` | `一堂双三角-人机协作模型-口述.txt`、`一堂双三角partner的对话记录20260705.md` | 同时列出两个源文件及行号 |
| `60_feedback/tasks/task_20260705_wangyuyan-kdo-agent-design-meta-method.md` | 双三角相关口述稿、Truman 对话记录 | 补充 source_refs 和 estimated_cards |

### 2.2 外部验证 URL 补充

| 任务/诊断 | 声称的调研 | 需补充的 URL/引用 |
|---|---|---|
| `60_feedback/tasks/task_20260705_wangyuyan-agent-distillation-method.md` | 8 篇论文/框架（SePO/MASS/Anthropic 三原则/HuggingFace 提示词消亡等） | 在 `diag_20260705_yai-agent-distillation.md` / `diag_20260705_yai-agent-distillation-v2.md` 中列出 8 个来源 URL |
| `60_feedback/tasks/task_20260705_wangyuyan-kdo-agent-design-meta-method.md` | 6 个独立框架（MongoDB Canvas/Abundly/Anthropic/Gulli21/MASS 等） | 在诊断或任务单中列出 6 个来源 URL |
| `diag_20260701_time-management-nine-layer-isomorphism.md` | Eisenhower/Covey、Cal Newport、GTD、番茄工作法 | 为成熟概念补充公开 URL 或经典文献 |
| `diag_20260702_yitang-scientific-sales-methodology.md` | SABC、六维激励、销售工具箱 | 补充外部销售/组织行为学研究或标注为一堂课程主张 |
| `diag_20260703_yitang-Y-model-foundation.md` | 《实践论》《矛盾论》、王阳明心学 | 补充公开版本链接或引用 |

### 2.3 诊断深度补充

| 诊断 | 需补充内容 |
|---|---|
| `diag_20260702_vikki-daxin-dark-knowledge-extraction.md` | 增加「试点方法边界与风险」小节；为 4 张新 dk 增加 When NOT to Use / 自攻击 |
| `diag_20260704_retroactive-case-scan-pilot.md` | 为 Top A 级候选补做九层深挖与自攻击；补充 case 卡骨架 |
| `diag_20260704_dual-triangle-vlm-gap-analysis.md` | 补充 VLM→case 的边界条件、失败模式、When NOT to Use |
| `diag_20260705_dual-triangle-domain-orchestration.md` | 若保留为诊断，需补齐：素材读取、九层深挖/假设审计、外部验证、失败模式、source_refs；或重命名为「编排日志」 |
| `diag_20260705_yai-agent-distillation.md` 及 `v2.md` | 补充九层深挖结构、失败模式/When NOT to Use、与已有 KDO 卡的交叉比对表 |

### 2.4 交叉比对表补充

| 诊断 | 需补充 |
|---|---|
| `diag_20260705_yai-agent-distillation.md` / `v2.md` | 列出已有 KDO method/tool/agent-spec 卡与新洞察的对应关系 |
| `diag_20260705_dual-triangle-domain-orchestration.md` | 列出 30 个新增任务的统筹表：队列号 ↔ 任务文件 ↔ 优先级 ↔ 预计卡数 ↔ 状态 |
| `diag_20260704_dual-triangle-vlm-gap-analysis.md` | 列出 7 张拟建 case ID 与已有双三角卡片的桥接关系 |

---

## 三、验收标准

1. 所有待补全文件的 frontmatter `source_refs` 精确到「文件路径 + 行号范围」或「URL」。
2. YAI 蒸馏任务单中的「全网调研」声明在诊断中有对应 URL 列表。
3. 5 份试点/草稿类诊断至少补充了边界说明、失败模式或 When NOT to Use 之一。
4. 双三角编排诊断要么补齐诊断维度，要么明确重命名为「编排日志」。
5. 不产生新的死链或 frontmatter parse 错误。
6. 全量修改通过欧阳锋终审。

---

## 四、风险与阻塞

| 风险 | 影响 | 应对 |
|------|------|------|
| 部分源文件（如 Vikki/大馨群聊 md）行号定位困难 | 无法精确 source_refs | 至少定位到段落或小标题；无法精确时标注为「约第 X 段」 |
| 外部 URL 无法全部找回 | 任务单声明的 8/6 框架部分不可考 | 能找到几个补几个；找不到的删除声明或标注为「待验证」 |
| 补充诊断深度可能扩大任务范围 | 任务膨胀 | 只补充附录/小节，不新建卡片；如必须新建，另开任务 |

---

## 五、产出后动作

1. 老顽童完成补全并跑 `kdo lint`。
2. 将本任务状态改为 `pending_review`。
3. 欧阳锋按队列终审。
4. 终审通过后，王语嫣更新 `.agent/kb-evolution-direction.md`，增加纪律：所有诊断报告的 `source_refs` 必须精确到行号或 URL；试点/扫描类诊断必须显式标注边界与失败模式。
