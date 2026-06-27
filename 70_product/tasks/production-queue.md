---
id: production-queue
type: queue
updated: 2026-06-27
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
| 1 | `laowantong-batch-2026-06-20-wave1` | 老顽童批量工单第 1 波：门禁快速清理 | queued | - | 11 | 无 | `laowantong-batch-2026-06-20.md` | Hermes 负责；快速清理，让质量门禁归零 |
| 2 | `task_20260627_laowantong-deliberate-practice-cards` | 元能力-刻意练习域卡片化（含 AI 协作桥接卡） | queued | - | 12 | 无（可与 wave1 并行） | `task_20260627_laowantong-deliberate-practice-cards.md` | Kimi 负责；含 1 张跨域桥接 framework |
| 3 | `task_20260627_laowantong-channel-growth-cards` | 渠道增长域卡片化（含 2 张跨域桥接卡） | queued | - | 24-25 | 无（可与 wave1 并行） | `task_20260627_laowantong-channel-growth-cards.md` | Kimi 负责；含单元模型+精益创业桥接；案例审计后追加 8 张 case 卡 |
| 4 | `task_20260627_laowantong-lanyi-panproduct-organization` | 兰毅：用泛产品做组织（素材待定） | queued | - | 待定 | 无 | `task_20260627_laowantong-lanyi-panproduct-organization.md` | Kimi 负责；等素材进 00_inbox 后王语嫣补任务单 |
| 5 | `laowantong-batch-2026-06-20-wave2` | 老顽童批量工单第 2 波：P0 返工 | queued | - | 13 | 依赖 wave1 完成 | `laowantong-batch-2026-06-20.md` | Hermes 负责；业务公式域返工 |
| 6 | `laowantong-batch-2026-06-20-wave3` | 老顽童批量工单第 3 波：P1 深度补全 | queued | - | ~15 | 依赖 wave2 完成 | `laowantong-batch-2026-06-20.md` | Hermes 负责；具体卡数见源文件 |
| 7 | `laowantong-batch-2026-06-20-wave4` | 老顽童批量工单第 4 波：P2 清理 | queued | - | ~12 | 依赖 wave3 完成 | `laowantong-batch-2026-06-20.md` | Hermes 负责；具体卡数见源文件 |
| 8 | `laowantong-batch-2026-06-20-wave5` | 老顽童批量工单第 5 波：新域建设 | queued | - | ~11 | 依赖 wave4 完成 | `laowantong-batch-2026-06-20.md` | Hermes 负责；具体卡数见源文件 |
| 9 | `review_20260627_ouyangfeng-self-attack-framework` | 欧阳锋审核：自攻击方法论框架卡 | pending_review | 欧阳锋 | 1 | 无 | `30_wiki/frameworks/framework-kdo-self-attack.md` | review-only；pre-submit 已通过 |

> **当前总待生产卡数**：约 98-99 张（含历史批量工单 62 张 + 新任务 36-37 张）。
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
