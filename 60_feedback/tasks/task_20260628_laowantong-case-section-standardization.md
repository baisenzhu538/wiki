---
id: task_20260628_laowantong-case-section-standardization
type: production_task
created_at: 2026-06-28
updated_at: 2026-06-28
author: 王语嫣
assignee: Hermes 老顽童
priority: P1
scope: 渠道增长域 13 张 case 卡 section 标题标准化
related:
  - '[[task_20260628_wangyuyan-cleanup-channel-growth-residuals]]'
  - '[[review_20260628_ouyangfeng-channel-growth]]'
status: queued
---

# 老顽童生产任务：渠道增长域 13 张 case 卡 section 标准化

> **来源**：`task_20260628_wangyuyan-cleanup-channel-growth-residuals` 中的 P1 部分。
> 黄药师已完成 P2（dk 目录移动）+ P3（concept 目录移动），P1 部分归老顽童执行。

---

## 0. 任务元信息

| 项目 | 内容 |
|------|------|
| 任务类型 | 既有卡片修复 |
| 来源 | 渠道增长域终审遗留问题 P1 |
| 优先级 | P1 |
| 生产方 | Hermes 老顽童 |
| 卡数 | 13 张 |
| 目标 | 将 13 张 case 卡 section 标题统一为 lint 新标准 |
| 验收 | 每张卡 `kdo pre-submit` 通过；`kdo lint` case section 相关 WARNING 减少 |

---

## 1. 待修复 13 张 case 卡清单

| # | 文件路径 | 当前问题 |
|:---:|:---|:---|
| 1 | `30_wiki/cases/case-yitang-amazon-growth-flywheel.md` | section 标题未对齐 lint 新标准 |
| 2 | `30_wiki/cases/case-yitang-novel-app-flywheel.md` | 同上 |
| 3 | `30_wiki/cases/case-yitang-yitang-course-industrialization.md` | 同上 |
| 4 | `30_wiki/cases/case-yitang-solid-redbull-channel.md` | 同上 |
| 5 | `30_wiki/cases/case-yitang-maiyi-cloud-computer-channel.md` | 同上 |
| 6 | `30_wiki/cases/case-yitang-topcity-growth-flywheel.md` | 同上 |
| 7 | `30_wiki/cases/case-yitang-redburger-selection-industrialization.md` | 同上 |
| 8 | `30_wiki/cases/case-yitang-lianjia-site-selection-industrialization.md` | 同上 |
| 9 | `30_wiki/cases/case-yitang-yitu-lead-industrialization.md` | 同上 |
| 10 | `30_wiki/cases/case-yitang-xujian-invoice-saas-channel.md` | 同上 |
| 11 | `30_wiki/cases/case-yitang-yitang-shortvideo-industrialization.md` | 同上 |
| 12 | `30_wiki/cases/case-yitang-shuzu-channel-scan-test.md` | 同上 |
| 13 | `30_wiki/cases/case-yitang-yitang-self-growth-channel.md` | 同上 |

---

## 2. case 卡标准 section 结构

每张 case 卡必须包含以下 4 个顶层 section：

```markdown
## 关键证据
## 可迁移场景
## 教训
## 失败模式
```

卡片正文通常已有对应内容，只是标题不一致。例如：
- 原始标题可能是 `## 核心数据`、`## 数据与证据` → 统一改为 `## 关键证据`
- 原始标题可能是 `## 举一反三`、`## 应用场景` → 统一改为 `## 可迁移场景`
- 原始标题可能是 `## 避坑指南`、`## 常见错误` → 统一改为 `## 失败模式`
- 原始标题可能是 `## 启发`、`## 复盘` → 统一改为 `## 教训`

---

## 3. 修复规范

1. **只改标题，不动内容实质**
   - 先读卡片，识别现有段落对应哪个标准 section
   - 只把标题改成标准名称，不重新写内容

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

## 4. 验收标准

1. 13 张卡 `kdo pre-submit` 全部通过
2. `kdo lint 30_wiki/cases` 中，这 13 张卡无新增 ERROR
3. case section 相关 WARNING 明显减少
4. 欧阳锋抽检 3-5 张，确认 section 标题符合标准

---

## 5. 审查与入库流程

```
Hermes 老顽童修复 13 张卡
  → 每张跑 kdo pre-submit
  → 全量跑 kdo lint 30_wiki/cases
  → 改任务状态为 pending_review
  → 欧阳锋抽检
  → 通过后全部标记 reviewed
```

---

## 6. 给 Hermes 老顽童的口令

**短版：**
> 老顽童，切到 wiki 目录，读 startup 和队列，领 `task_20260628_laowantong-case-section-standardization`，按清单修复 13 张 case 卡 section 标题。

**完整版：**
> 你是老顽童。先进入工作目录 `C:\Users\Administrator\Desktop\wiki\`，读 `.agent/startup.md`，再读 `70_product/tasks/production-queue.md`，找到 `task_20260628_laowantong-case-section-standardization`，读 `60_feedback/tasks/task_20260628_laowantong-case-section-standardization.md`，按清单修复 13 张 case 卡 section 标题。每张改完跑 `kdo pre-submit`，更新队列前先加锁。

---

## 7. 状态记录

| 日期 | 事件 | 操作人 |
|:---|:---|:---|
| 2026-06-28 | 欧阳锋渠道增长域终审发现 13 张 case 卡 section 未对齐 | 欧阳锋 |
| 2026-06-28 | 黄药师完成 P2+P3 目录移动 | 黄药师 |
| 2026-06-28 | 王语嫣将 P1 拆分为本任务单 | 王语嫣 |
| 待填写 | Hermes 老顽童完成 13 张卡 section 标准化 | Hermes 老顽童 |

---

*维护人：王语嫣 | 最后更新：2026-06-28*
