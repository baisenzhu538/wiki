---
id: production-queue
type: queue
updated: 2026-06-28
owner: 王语嫣
audience: 老顽童 / 欧阳锋 / 黄药师 / 用户
---

# 生产队列：老顽童领取 / 欧阳锋审核

> 本文件是 KDO 知识工厂的**统一生产队列**。
> 老顽童按队列顺序领取任务，一次只做一件；欧阳锋按队列顺序审核。
> 任务来源：历史批量工单、新域诊断任务、跨域桥接任务。

---

## 队列规则

1. **单实例单线程领取**：每个老顽童实例每次只能领取一个 `queued` 任务，把状态改为 `claimed-<实例标识>`（如 `claimed-hermes`、`claimed-kimi`）。`pending_review` 状态的条目为审阅项，由欧阳锋直接审核，老顽童不领取。
2. **多实例并行**：当队列中存在 ≥2 个无依赖的 `queued` 任务时，可启动多个老顽童实例并行领取。同一任务默认由单实例完成；如需多实例协作同一任务，由用户或王语嫣在任务单中明确拆分。
3. **完成后提交**：老顽童完成生产并把 `kdo pre-submit` 输出贴到任务文件后，将状态改为 `pending_review`。
4. **按序审核**：欧阳锋按队列顺序审核 `pending_review` 任务，通过后改为 `reviewed`；王语嫣跟踪任务状态，必要时改为 `done`。
5. **阻塞处理**：若任务被阻塞，在「状态」列标注 `blocked` 并写明阻塞原因；阻塞解决后恢复为 `queued`。
6. **优先级调整**：用户可随时调整队列顺序；调整时由王语嫣更新本文件，并在 `.agent/context.md` 中同步。
7. **新任务入队**：王语嫣诊断完成后，新任务默认进入队列末尾；用户可指定插队。

---

## 当前队列

| 队列序号 | 任务 ID | 任务名称 | 状态 | 领取人 | 预计卡数 | 阻塞/依赖 | 来源文件 | 备注 |
|:---:|:---|:---|:---:|:---:|---:|:---|:---|:---|
| 1 | `laowantong-batch-2026-06-20-wave1` | 老顽童批量工单第 1 波：门禁快速清理 | reviewed | 老顽童(WorkBuddy) | 18 | 无 | `review_20260628_ouyangfeng-wave1.md` | 欧阳锋终审通过：18/18 张卡 status 更新为 reviewed，reviewed_by: 欧阳锋，review_date: 2026-06-28 |
| 2 | `task_20260627_laowantong-deliberate-practice-cards` | 元能力-刻意练习域卡片化（含 AI 协作桥接卡） | reviewed | - | 11 | 无（可与 wave1 并行） | `60_feedback/tasks/task_20260627_laowantong-deliberate-practice-cards.md` | 欧阳锋终审通过，11 张卡 status 更新为 reviewed，frontmatter 已补 review_date |
| 3 | `task_20260627_laowantong-channel-growth-cards` | 渠道增长域卡片化（含 2 张跨域桥接卡） | reviewed | - | 25 | 无（可与 wave1 并行） | `review_20260628_ouyangfeng-channel-growth.md` | 欧阳锋终审通过：25/25 张卡 status 更新为 reviewed，reviewed_by: 欧阳锋，review_date: 2026-06-28；已知遗留：13 张 case 卡缺 lint 标准 section（全局 case section 债务）、1 张 dk 目录未对齐、1 张 concept 目录未对齐，已记录为后续清理任务 |
| 4 | `task_20260627_laowantong-lanyi-panproduct-organization` | 兰毅泛产品组织化 + 泛产品设计域升级 | reviewed | - | 12 | 无 | `task_20260627_laowantong-lanyi-panproduct-organization.md` | 欧阳锋终审通过：12/12 张卡 status 更新为 reviewed，reviewed_by: 欧阳锋，review_date: 2026-06-28；审查中修复 3 张 case section + 5 个目录移动 |
| 5 | `laowantong-batch-2026-06-20-wave2` | 老顽童批量工单第 2 波：P0 返工 | reviewed | 老顽童(WorkBuddy) | 16 | 无 | `laowantong-batch-2026-06-20.md` | 欧阳锋子代理终审通过：16/16 张卡 `kdo pre-submit` 通过，status 更新为 reviewed，`reviewed_by: 欧阳锋`，`review_date: 2026-06-28`；仍有 frontmatter domain/related/tags/query_triggers `src_unknown` 占位及少量内容区占位，已记录为 wave2 残留项，建议由王语嫣/老顽童在后续清理任务中补齐 |
| 6 | `laowantong-batch-2026-06-20-wave3` | 老顽童批量工单第 3 波：P1 深度补全 | reviewed | 欧阳锋 | 14 | 依赖 wave2 完成（已 reviewed，解锁） | `review_20260628_ouyangfeng-wave3.md` | 欧阳锋终审通过：14/14 张卡 status 更新为 reviewed；审查中清理 14 张卡 frontmatter 中 domain/related/tags 的 src_unknown 占位；全库 lint ERROR 降至 533；已解锁 wave4 和第八批 dk 清零 |
| 7 | `task_20260628_laowantong-dark-knowledges-batch8` | dark-knowledges 第八批清零：补齐 10 张问题 dk 卡 | reviewed | 欧阳锋 | 10 | 依赖 wave3 完成（已 reviewed，解锁） | `task_20260628_laowantong-dark-knowledges-batch8.md` | 欧阳锋终审通过：10/10 张 dk 卡 status 更新为 reviewed；`dark-knowledges/` 目录 lint ERROR 归零；审查中修复 4 张卡格式问题；wave4 已完全解锁 |
| 8 | `laowantong-batch-2026-06-20-wave4` | 老顽童批量工单第 4 波：新域建设 | reviewed | Hermes 老顽童 | 15 | 已解锁（wave3 + 第八批均 reviewed） | `review_20260628_ouyangfeng-wave4.md` | 欧阳锋终审通过：15/15 张卡 status 更新为 reviewed，reviewed_by: 欧阳锋，review_date: 2026-06-28；审查中修复 4.1 source_refs 18 处、4.2 domain 占位 7 处及正文 src_unknown 占位 30+ 处；wave4 已解锁 wave5 |
| 9 | `laowantong-batch-2026-06-20-wave5` | 老顽童批量工单第 5 波：外部探索三个新盲区 | reviewed | WorkBuddy 老顽童 | 12 | 依赖 wave4 完成（已 reviewed，解锁） | `review_20260628_ouyangfeng-wave5.md` | 欧阳锋终审通过：12/12 张卡 `kdo pre-submit` 通过；审查中修复 12 张卡 frontmatter（补 `status: reviewed`、统一 `reviewed_by: 欧阳锋`、更新 `updated_at`）；wave5 已解锁 |
| 10 | `task_20260628_hermes-lint-baseline-cleanup-batch1` | Hermes lint 基线清理 Batch 1：机械性 frontmatter 修复 | pending_review | Hermes 老顽童 | 784（安全机械修复，含复查追加 125） | 无 | `60_feedback/tasks/task_20260628_hermes-lint-baseline-cleanup-batch1.md` | Hermes 已完成：frontmatter parse 类 ERROR 清零；`kdo lint` 从 690→890 是因为 frontmatter 修好后原被压制的卡片暴露更多 section/source_refs 错误；890 个内容级错误由 Batch 2-A/B/C 承接；Hermes 老顽童待命 |
| 11 | `review_20260627_ouyangfeng-self-attack-framework` | 欧阳锋审核：自攻击方法论框架卡 | reviewed | 欧阳锋 | 1 | 无 | `30_wiki/frameworks/framework-kdo-self-attack.md` | review-only；pre-submit 已通过；欧阳锋审查结论：deep 通过 |
| 11 | `task_20260628_wangyuyan-cleanup-channel-growth-residuals` | 渠道增长域终审遗留问题清理（P2+P3 已完成，P1 已拆分） | done | 黄药师 | 0（清理任务） | 无 | `task_20260628_wangyuyan-cleanup-channel-growth-residuals.md` | 黄药师已完成 dk/concept 目录移动 + 全库 related 链接更新 + 顺手修复 3 张 case 卡；P1 剩余 10 张 case + 1 张 dk section 调整已拆分为独立任务 #12 |
| 12 | `task_20260628_laowantong-case-section-standardization` | 渠道增长域 10 张 case + 1 张 dk section 标准化 | reviewed | 欧阳锋 | 11 | 无 | `task_20260628_laowantong-case-section-standardization.md` | 欧阳锋终审通过：11/11 文件 `kdo lint` 0 ERROR；1 处标题序号问题已现场修复 |
| 13 | `task_20260628_laowantong-lint-batch2-case-sections` | lint Batch 2-A：case section 标准化补全（130 文件） | reviewed | WorkBuddy 老顽童 | 130 | 无 | `60_feedback/tasks/task_20260628_laowantong-lint-batch2-case-sections.md` | 欧阳锋复核通过：申诉成立，130/130 case 文件已真实修改并 commit，`kdo lint` Case section ERROR 清零；之前 `git diff HEAD` 检查失效根因是 vault backup 自动 commit |
| 14 | `task_20260628_laowantong-lint-batch2-dk-sections` | lint Batch 2-B：dk section 标准化补全（43+14 文件） | reviewed | WorkBuddy 老顽童 | 57 | 无 | `60_feedback/tasks/task_20260628_laowantong-lint-batch2-dk-sections.md` | 欧阳锋复核通过：申诉成立，57/57 dk 文件已真实修改并 commit，`kdo lint` DK section ERROR 清零；原 43 清单 + 14 个 extra 文件均处理 |
| 15 | `task_20260628_huangyaoshi-lint-batch2-source-refs` | lint Batch 2-C：source_refs 真实存在性清理（175 ERROR / 90 文件） | pending_review | WorkBuddy 老顽童 | 90 | 无 | `60_feedback/tasks/task_20260628_huangyaoshi-lint-batch2-source-refs.md` | 用户复核发现规则层补丁已上线但数据层清理未完成；任务转交老顽童；已真实修改 90 个文件，为 175 个 bare source_refs 添加 `10_raw/sources/` 前缀，`kdo lint` source_refs ERROR 清零，`kdo pre-submit` 90/90 通过；待欧阳锋终审 |
| 16 | `task_20260628_wangyuyan-wave6-blindspot-diagnosis` | Wave 6 新盲区探索诊断 | queued | 王语嫣 | 0 | 无 | `60_feedback/tasks/task_20260628_wangyuyan-wave6-blindspot-diagnosis.md` | 王语嫣负责；基于周报和对话记录识别 1-2 个新盲区并拆任务入队；与补链 B 线并行 |
| 17 | `task_20260628_wangyuyan-next-phase-orchestration` | 下一阶段任务编排建议：Wave 6 + 补链并行 | confirmed | 王语嫣 | 0 | 无 | `60_feedback/tasks/task_20260628_wangyuyan-next-phase-orchestration.md` | 王语嫣已拍板：Wave 6 继续 #16，补链拆为 B1/B2/B3 作为 #18/#19/#20 入队；B1 自动写入+抽检，B2 必须人工审核，B3 半自动；related 分层标准不按 ≥8 一刀切 |
| 18 | `task_20260628_laowantong-link-repair-b1-frontmatter-related` | B1：frontmatter `related` 字段 src_unknown 占位清理 | queued | 老顽童 | 200-400 | 依赖 Batch 2-C reviewed | `60_feedback/tasks/task_20260628_laowantong-link-repair-b1-frontmatter-related.md` | 老顽童负责；自动写入 + 人工抽检 20 张；related 分层标准：concept/framework/dk/tool ≥5，case ≥3，draft ≥1 或 pending |
| 19 | `task_20260628_laowantong-link-repair-b2-synthesis-section` | B2：Synthesis section 死链/占位清理 | queued | 老顽童 | 100-200 | 依赖 Batch 2-C reviewed | `60_feedback/tasks/task_20260628_laowantong-link-repair-b2-synthesis-section.md` | 老顽童负责；必须人工审核逐张处理；Synthesis 出链 ≥2；批量提交前 `--expect-changes` 门禁 |
| 20 | `task_20260628_laowantong-link-repair-b3-island-cards` | B3：孤岛卡片 `kdo link-suggest` 批量推荐 | queued | 老顽童 | 50-100 | 依赖 B1/B2 完成后启动 | `60_feedback/tasks/task_20260628_laowantong-link-repair-b3-island-cards.md` | 老顽童负责；半自动：`kdo link-suggest` 生成 + 人工审核写入；孤岛卡片减少 ≥80% |

> **当前总待生产卡数**：约 98-99 张（含历史批量工单 62 张 + 新任务 36-37 张）+ lint Batch 2 约 280 文件修复 + 补链 350-700 文件。
> **当前 lint 基线**：`kdo lint` 剩余 890 ERROR（690 机械修复后基线 + 200 因 frontmatter 修复而暴露的内容错误），Batch 2-A/B/C 完成后预计降至 100 以下。
> **人员状态**：Hermes 老顽童 Batch1 完成后待命；WorkBuddy 老顽童已领取 Batch 2-A/B；黄药师负责 Batch 2-C；王语嫣负责 Wave 6 诊断。
> **执行顺序建议**：黄药师先投 0.5 天完成 Batch 2-C 的 URL lint 规则补丁（-16 ERROR），再与 WorkBuddy 的 A/B 并行推进；若 WorkBuddy 为单实例，建议先 A 后 B。欧阳锋按 pending_review 顺序终审。
> 历史批量工单卡数估算来自 `laowantong-batch-2026-06-20.md` 的 waves 1-5。
>
> **🆘 临时分流（2026-06-27）**：Hermes 老顽童历史任务重，启动 Kimi 老顽童临时协助生产 2026-06-27 新标注任务。历史批量工单 waves 1-5 仍由 Hermes 负责；刻意练习域、渠道增长域、兰毅泛产品组织内容及跨域桥接卡由 Kimi 负责。欧阳锋/黄药师无感知——他们只按 pending_review 顺序审卡。

---

## 状态流转图

```
queued
  ↓ 老顽童领取
claimed
  ↓ 老顽童生产完成 + pre-submit 通过
pending_review
  ↓ 欧阳锋审核
reviewed
  ↓ 王语嫣最终验收（如需）
done
```

**中间状态**：
- `blocked`：任务被阻塞，需用户/其他角色先解决
- `paused`：任务暂停，等待用户决策或外部输入

---

## 各角色启动时必读

- **老顽童**：启动后先读 `.agent/startup.md` → `.agent/kb-evolution-direction.md` → `70_product/tasks/production-queue.md`，领取队列最前面的 `queued` 任务。
- **欧阳锋**：启动后先读 `.agent/startup.md` → `.agent/kb-evolution-direction.md` → `70_product/tasks/production-queue.md`，按顺序审核 `pending_review` 任务。
- **黄药师**：关注队列中任务的 KDO 基建依赖（如 lint/index），按需支持。
- **用户**：可随时查看本队列，回复「调整顺序」「插队」「暂停某任务」。

---

## 变更日志

| 日期 | 变更 | 变更人 |
|:---|:---|:---|
| 2026-06-27 | 创建统一生产队列，整合历史批量工单与新域任务 | 王语嫣 |

---

*维护人：王语嫣 | 最后更新：2026-06-27*
