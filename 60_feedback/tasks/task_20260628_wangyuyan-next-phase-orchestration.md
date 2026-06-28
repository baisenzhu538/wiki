---
id: task_20260628_wangyuyan-next-phase-orchestration
type: task
status: queued
assignee: 王语嫣
priority: P1
created_at: 2026-06-28
updated_at: 2026-06-28
reviewer: 欧阳锋
source_refs:
- 70_product/tasks/production-queue.md
- 60_feedback/tasks/task_20260628_huangyaoshi-lint-batch2-source-refs.md
---

# 下一阶段任务编排建议（王语嫣）

## 当前状态（2026-06-28）

| 任务 | 状态 | 结果 |
|:---|:---|:---|
| Batch 2-A case section 标准化 | ✅ reviewed | 130/130 文件完成，Case section ERROR 清零 |
| Batch 2-B dk section 标准化 | ✅ reviewed | 57/57 文件完成，DK section ERROR 清零 |
| Batch 2-C source_refs 清理 | 🔄 in_progress | 黄药师修复中；当前 lint source_refs ERROR 175 待清零 |
| Wave 6 新盲区诊断 | queued | #16，王语嫣负责 |

当前 `kdo lint`：**175 ERROR / 5545 WARNING**。全部 ERROR 为 source_refs `file not found on disk`，待 Batch 2-C 收口。

---

## 下一阶段核心问题

用户提出："下一阶段是不是需要补链了？"

**判断：是，但要有节奏。**

Batch 2-C 完成后，全库 lint ERROR 将接近 0，机械性质量闸门基本清完。下一阶段应转向**内容连接度**和**知识网络密度**，即"补链"工作。但 Wave 6 新盲区探索是既定队列 #16，不应被搁置。

建议：**并行两条线**
- **A 线（内容方向）**：王语嫣主导 Wave 6 新盲区诊断
- **B 线（连接度方向）**：老顽童主导 Related/Synthesis 补链

---

## 建议编排

### A 线：Wave 6 新盲区诊断（继续 #16）

**负责人**：王语嫣  
**触发条件**：Batch 2-C 进入收尾阶段即可并行启动，不需要等完全结束  
**交付物**：
1. 基于周报、对话记录、已 reviewed 卡片分布，识别 1-2 个新盲区
2. 每个盲区产出：
   - 盲区定义（为什么重要、为什么当前覆盖不足）
   - 候选卡片清单（新卡/旧卡升级/跨域桥接）
   - 优先级建议（P0/P1/P2）
3. 拆分为独立任务单，入队到 production-queue #17 及以后

### B 线：Related/Synthesis 补链（新建 #17）

**负责人**：老顽童（WorkBuddy/Hermes 均可）  
**触发条件**：Batch 2-C 完成后启动  
**目标**：
- 把 frontmatter/正文中 `[[src_unknown]]`、`related: [src_unknown, ...]` 等占位替换为真实 wikilink
- 确保每张非 draft 卡片的 Synthesis section 出链 ≥ 2
- 减少"孤岛卡片"（related 为空或全 src_unknown）

**建议拆分子任务**：

| 子任务 | 范围 | 预计文件数 | 技术依赖 |
|:---|:---|---:|:---|
| B1 frontmatter related 占位清理 | `related` 字段含 `src_unknown` 的卡片 | 约 200-400 | `kdo lint` 可识别 |
| B2 Synthesis 死链/占位清理 | Synthesis section 含 `[[src_unknown]]` 或纯文本 src_unknown | 约 100-200 | 需读正文 |
| B3 孤岛卡片 link-suggest | related 为空且 status 为 enriched/reviewed 的卡片 | 约 50-100 | `kdo link-suggest` 批量模式 |
| B4 跨域桥接卡 production | 王语嫣诊断中识别出的跨域桥接需求 | 待定 | 九层深挖/六层交叉验证 |

**执行顺序建议**：
1. B1 → B2（机械占位清理，前置）
2. B3（link-suggest 批量推荐，人工/规则审核后写入）
3. B4（与王语嫣 Wave 6 输出对接）

---

## 需要王语嫣决策

1. **是否启动 B 线？**  
   - 选项 A：等 Batch 2-C 完全结束后启动（保守）
   - 选项 B：Batch 2-C 收尾阶段即启动 B1/B2 准备（推荐，可并行）

2. **B 线优先级是否高于 Wave 6？**  
   - 建议 Wave 6 保持 #16，补链作为 #17 入队；两者并行

3. **补链质量标准？**  
   - 是否允许 link-suggest 自动写入，还是仅生成推荐清单由人工审核？
   - `related` 最低数量要求是否维持 ≥ 8？是否按卡片类型区分？

4. **是否把"补链"拆分为独立任务单并入队？**  
   - 建议拆分为 `task_20260628_laowantong-link-repair-b1`、`b2`、`b3` 三个子任务

---

## 欧阳锋备注

- 我已复核 Batch 2-A/B，申诉成立，已通过
- Batch 2-C 当前 175 source_refs ERROR 待黄药师清零
- 补链工作建议用 `kdo link-suggest` 批量模式，但写入前必须经过 `kdo pre-submit` 和欧阳锋抽查
- 不要把"补链"做成第二个 Batch 2-C——先小批量试点 10-20 张卡，验证流程后再扩量

---

## 下一步动作

待王语嫣确认后：
1. 更新 `production-queue.md`，把 B1/B2/B3 作为 #17/#18/#19 入队
2. 创建对应任务单
3. 老顽童领取并开始小批量试点
