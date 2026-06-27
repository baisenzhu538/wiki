---
id: task_20260628_laowantong-dark-knowledges-batch8
type: production_task
created_at: 2026-06-28
updated_at: 2026-06-28
author: 王语嫣
assignee: WorkBuddy 老顽童
priority: P0
scope: dark-knowledges 目录第八批清零：补齐 10 张问题 dk 卡的标准 section
related:
  - '[[laowantong-batch-2026-06-20-wave3]]'
status: queued
---

# 老顽童生产任务：dark-knowledges 第八批清零（10 张 dk 卡）

> **来源**：欧阳锋 2026-06-28 wave3 第七批审查结论。
> 第七批 7 张卡单卡验证通过，但全库 `dark-knowledges/` 目录仍有 10 张卡未清零，需要第八批修复。

---

## 0. 任务元信息

| 项目 | 内容 |
|------|------|
| 任务类型 | 既有卡片修复 |
| 来源 | 欧阳锋 wave3 第七批审查后遗漏清单 |
| 优先级 | P0（阻塞 dark-knowledges 目录清零目标） |
| 生产方 | WorkBuddy 老顽童（已在跑 wave3，第八批作为 wave3 收尾） |
| 卡数 | 10 张 |
| 目标 | 补齐 10 张 dk 卡缺失的标准 section，使 `dark-knowledges/` 目录 lint ERROR 归零 |
| 验收 | 每张卡 `kdo pre-submit` 通过；`kdo lint 30_wiki/dark-knowledges` 无新增 ERROR |

---

## 1. 待修复 10 张 dk 卡清单

### 1.1 缺 1 个 section（3 张）

| # | 文件路径 | 缺 section | 修复动作 |
|:---:|:---|:---|:---|
| 1 | `30_wiki/dark-knowledges/dk-f1-regex-on-cjk.md` | `## 适用边界` | 根据卡片内容补写适用边界：明确正则匹配 CJK 的适用场景和失效场景 |
| 2 | `30_wiki/dark-knowledges/dk-f2-txt-ingest-skip.md` | `## 适用边界` | 根据卡片内容补写适用边界：明确 txt 跳读策略的适用与失效场景 |
| 3 | `30_wiki/dark-knowledges/dk-yitang-business-formula-plus-times-trap.md` | `## 原始表述` | 根据素材补写原始表述：找到业务公式中「加法变乘法」陷阱的原始出处 |

### 1.2 6 个标准 section 全缺（7 张）

| # | 文件路径 | 主题 | 修复动作 |
|:---:|:---|:---|:---|
| 4 | `30_wiki/dark-knowledges/dk-modeling-ai-cross-validation.md` | AI 建模交叉验证 | 按 dk 卡标准结构重写：原始表述/使用场景/操作方法/适用边界/为什么值钱/与其他知识的关联 |
| 5 | `30_wiki/dark-knowledges/dk-modeling-ai-iterative-prompting.md` | AI 迭代提示 | 同上 |
| 6 | `30_wiki/dark-knowledges/dk-modeling-ai-judgment-limit.md` | AI 判断边界 | 同上 |
| 7 | `30_wiki/dark-knowledges/dk-modeling-case-explosion-confidence.md` | 案例爆炸置信度 | 同上 |
| 8 | `30_wiki/dark-knowledges/dk-modeling-expert-consensus-five-percent.md` | 专家共识 5% | 同上 |
| 9 | `30_wiki/dark-knowledges/dk-strategy-longzhong-four-failures.md` | 隆中四败 | 同上 |
| 10 | `30_wiki/dark-knowledges/dk-strategy-three-must-do-moments.md` | 三个必做时刻 | 同上 |

---

## 2. dk 卡标准 section 结构

每张 dk 卡必须包含以下 6 个顶层 section：

```markdown
## 原始表述
## 使用场景
## 操作方法
## 适用边界
## 为什么值钱
## 与其他知识的关联
```

对于缺 1 个 section 的卡，只补缺失的 section，不动其他内容。
对于 6 个 section 全缺的卡，需要按素材重写整个正文结构。

---

## 3. 修复规范

1. **不要编造素材**：
   - 补 `## 原始表述` 时必须引用 source_refs 中的具体素材
   - 找不到原始素材时，用 `[conf=0.6, source=推断]` 标注，不能硬编

2. **适用边界必须具体**：
   - 不能写"需要灵活运用"
   - 必须写：什么场景下失效、为什么会失效、替代方案是什么

3. **为什么值钱要有用户视角**：
   - 不写"这个知识很重要"
   - 写：用户在什么情况下会因为这个知识少踩什么坑、省多少时间、避免多少损失

4. **与其他知识的关联 ≥3 条**：
   - 链回同域相关卡
   - 至少 1 条跨域链接

5. **每张卡改完立即跑**：
   - `kdo pre-submit -f <文件路径>`
   - 不通过不交

---

## 4. 验收标准

1. 10 张卡 `kdo pre-submit` 全部通过
2. `kdo lint 30_wiki/dark-knowledges` 中，这 10 张卡无新增 ERROR
3. `dark-knowledges/` 目录 lint ERROR 从 45 个降至 0 个（或降至基线容忍范围内）
4. 欧阳锋抽检 3-5 张，确认 section 结构符合 dk 卡标准

---

## 5. 审查与入库流程

```
WorkBuddy 老顽童修复 10 张卡
  → 每张跑 kdo pre-submit
  → 全量跑 kdo lint 30_wiki/dark-knowledges
  → 改任务状态为 pending_review
  → 欧阳锋抽检
  → 通过后全部标记 reviewed
```

---

## 6. 给 WorkBuddy 老顽童的口令

**完整版**：
> 你是老顽童。先进入工作目录 `C:\Users\Administrator\Desktop\wiki\`，读 `.agent/startup.md`、`70_product/tasks/production-queue.md`，领取 `task_20260628_laowantong-dark-knowledges-batch8`，读 `60_feedback/tasks/task_20260628_laowantong-dark-knowledges-batch8.md`，按清单修复 10 张 dk 卡，补齐缺失 section，每张跑 `kdo pre-submit`。

**短版**：
> 老顽童，切到 wiki 目录，读 startup 和队列，领第八批 dk 清零任务，修 10 张卡。

---

## 7. 状态记录

| 日期 | 事件 | 操作人 |
|:---|:---|:---|
| 2026-06-28 | 欧阳锋 wave3 第七批审查发现 10 张 dk 卡未清零 | 欧阳锋 |
| 2026-06-28 | 王语嫣写第八批清零任务单 | 王语嫣 |
| 待填写 | WorkBuddy 老顽童修复完成 | WorkBuddy 老顽童 |
| 待填写 | 欧阳锋抽检 | 欧阳锋 |

---

*维护人：王语嫣 | 最后更新：2026-06-28*
