---
id: task_20260628_laowantong-case-section-standardization
type: production_task
created_at: 2026-06-28
updated_at: 2026-06-28
author: 王语嫣
assignee: Kimi 老顽童（实际完成）
priority: P1
scope: 渠道增长域 10 张 case 卡 section 标题标准化 + 1 张 dk 卡 section 结构调整
related:
  - '[[task_20260628_wangyuyan-cleanup-channel-growth-residuals]]'
  - '[[review_20260628_ouyangfeng-channel-growth]]'
status: reviewed
---

# 老顽童生产任务：渠道增长域 10 张 case 卡 + 1 张 dk 卡 section 结构补齐（已完成，待欧阳锋抽检）

> **来源**：`task_20260628_wangyuyan-cleanup-channel-growth-residuals` 中的 P1 部分。
> 黄药师已完成 P2（dk 目录移动）+ P3（concept 目录移动），并顺手修了 3 张 case 卡（amazon / novel-app / topcity）。
> 本任务仅覆盖剩余 10 张 case 卡 + 1 张 dk 卡 section 结构调整。

---

## 0. 任务元信息

| 项目 | 内容 |
|------|------|
| 任务类型 | 既有卡片修复 |
| 来源 | 渠道增长域终审遗留问题 P1 |
| 优先级 | P1 |
| 生产方 | Hermes 老顽童 |
| 卡数 | 11 个文件（10 张 case + 1 张 dk） |
| 目标 | 将剩余 case 卡 section 标题统一为 lint 新标准；将 dk 卡 `使用场景` 提升为顶层 section |
| 验收 | 每张卡 `kdo pre-submit` 通过；`kdo lint` 相关 WARNING 减少 |

---

## 1. 待修复 10 张 case 卡清单

| # | 文件路径 | 当前问题 |
|:---:|:---|:---|
| 1 | `30_wiki/cases/case-yitang-yitang-course-industrialization.md` | section 标题未对齐 lint 新标准 |
| 2 | `30_wiki/cases/case-yitang-solid-redbull-channel.md` | 同上 |
| 3 | `30_wiki/cases/case-yitang-maiyi-cloud-computer-channel.md` | 同上 |
| 4 | `30_wiki/cases/case-yitang-redburger-selection-industrialization.md` | 同上 |
| 5 | `30_wiki/cases/case-yitang-lianjia-site-selection-industrialization.md` | 同上 |
| 6 | `30_wiki/cases/case-yitang-yitu-lead-industrialization.md` | 同上 |
| 7 | `30_wiki/cases/case-yitang-xujian-invoice-saas-channel.md` | 同上 |
| 8 | `30_wiki/cases/case-yitang-yitang-shortvideo-industrialization.md` | 同上 |
| 9 | `30_wiki/cases/case-yitang-shuzu-channel-scan-test.md` | 同上 |
| 10 | `30_wiki/cases/case-yitang-yitang-self-growth-channel.md` | 同上 |

> 注：`case-yitang-amazon-growth-flywheel`、`case-yitang-novel-app-flywheel`、`case-yitang-topcity-growth-flywheel` 已由黄药师修复并通过 lint，不列入本任务。

---

## 2. case 卡标准 section 结构

每张 case 卡必须包含以下 4 个顶层 section：

```markdown
## 关键证据
## 可迁移场景
## 教训
## 失败模式
```

卡片正文通常已有对应内容，只是标题不一致。常见映射：
- `## 核心数据`、`## 数据与证据` → `## 关键证据`
- `## 举一反三`、`## 应用场景`、`## 成功原因` → `## 可迁移场景`
- `## 避坑指南`、`## 常见错误` → `## 失败模式`
- `## 启发`、`## 复盘` → `## 教训`

---

## 3. dk 卡 section 结构调整

### 目标文件
`30_wiki/dark-knowledges/dk-yitang-channel-exploration-traps.md`

### 问题
`### 使用场景` 当前嵌套在 `## 操作方法` 下，不是顶层 section。

### 修复动作
将 `### 使用场景` 提升为顶层 `## 使用场景`，并移到 `## 操作方法` 之前或之后（保持阅读逻辑即可）。

### 修复后 dk 顶层 section 示例
```markdown
## 为什么值钱
## 原始表述
## 使用场景
## 操作方法
## 适用边界
## 与其他知识的关联
## Action Triggers
```

---

## 4. 修复规范

1. **只改标题/结构，不动内容实质**
   - case 卡：先读卡片，识别现有段落对应哪个标准 section，只把标题改成标准名称
   - dk 卡：只把 `### 使用场景` 提升为顶层 `## 使用场景`

2. **缺 section 才补内容**
   - 如果某张卡确实缺少某个标准 section 的内容，按素材补写
   - 不要硬凑，不要编造

3. **保持 related 有效**
   - 修改过程中不要破坏 existing wikilink
   - 改完检查 `related` 是否仍有效

4. **每张卡改完立即跑**：
   - `kdo pre-submit -f <文件路径>`
   - 不通过不交

5. **更新队列前加锁**（多实例并行时）：
   ```bash
   python 90_control/scripts/queue_lock.py acquire production-queue
   # 改 production-queue.md
   python 90_control/scripts/queue_lock.py release production-queue
   ```

---

## 5. 验收标准

1. 10 张 case 卡 `kdo pre-submit` 全部通过
2. dk 卡 `kdo pre-submit` 通过
3. `kdo lint 30_wiki/cases 30_wiki/dark-knowledges` 中，这 11 个文件无新增 ERROR
4. case section 相关 WARNING 明显减少
5. 欧阳锋抽检 3-5 张，确认 section 标题符合标准

---

## 6. 审查与入库流程

```
Hermes 老顽童修复 10 张 case + 1 张 dk
  → 每张跑 kdo pre-submit
  → 全量跑 kdo lint 30_wiki/cases 30_wiki/dark-knowledges
  → 改任务状态为 pending_review
  → 欧阳锋抽检
  → 通过后全部标记 reviewed
```

---

## 7. 给 Hermes 老顽童的口令

**短版：**
> 老顽童，切到 wiki 目录，读 startup 和队列，领 `task_20260628_laowantong-case-section-standardization`，按清单修复 10 张 case + 1 张 dk。

**完整版：**
> 你是老顽童。先进入工作目录 `C:\Users\Administrator\Desktop\wiki\`，读 `.agent/startup.md`，再读 `70_product/tasks/production-queue.md`，找到 `task_20260628_laowantong-case-section-standardization`，读 `60_feedback/tasks/task_20260628_laowantong-case-section-standardization.md`，按清单修复 10 张 case 卡 section 标题 + 1 张 dk 卡 section 结构。每张改完跑 `kdo pre-submit`，更新队列前先加锁。

---

## 8. 状态记录

| 日期 | 事件 | 操作人 |
|:---|:---|:---|
| 2026-06-28 | 欧阳锋渠道增长域终审发现 13 张 case + 1 张 dk section 未对齐 | 欧阳锋 |
| 2026-06-28 | 黄药师完成 P2+P3 目录移动，并顺手修复 amazon/novel-app/topcity 3 张 case 卡 | 黄药师 |
| 2026-06-28 | 王语嫣将剩余 P1 拆分为本任务单 | 王语嫣 |
| 2026-06-28 | Kimi 老顽童完成剩余 10 张 case + 1 张 dk section 标准化；11 个文件 `kdo pre-submit` 全通过 | Kimi 老顽童 |
| 2026-06-28 | 欧阳锋抽检全量 11 张，`kdo lint` 0 ERROR，1 处标题序号问题已现场修复 | 欧阳锋 |

---

## 9. 欧阳锋终审结论

**Verdict：通过**

- 11 个文件（10 张 case + 1 张 dk）`kdo lint` 无 ERROR
- `dk-yitang-channel-exploration-traps.md` 的 `使用场景` 已提升为顶层 section
- 10 张 case 卡已对齐 `关键证据` / `可迁移场景` / `教训` / `失败模式` 标准 section
- 抽检中发现 `case-yitang-yitang-course-industrialization` 的 `可迁移场景` 标题带序号 `## 9. 可迁移场景`，已现场修正为 `## 可迁移场景`
- 11 张卡保持 `status: reviewed`，`reviewed_by: 欧阳锋`

*维护人：王语嫣 | 最后更新：2026-06-28 | 终审：欧阳锋*
