---
id: task_20260628_wangyuyan-cleanup-channel-growth-residuals
type: cleanup_task
created_at: 2026-06-28
updated_at: 2026-06-28
author: 王语嫣
assignee: 黄药师
priority: P2
scope: 渠道增长域终审遗留问题清理
related:
  - '[[review_20260628_ouyangfeng-channel-growth]]'
status: queued
---

# 清理任务：渠道增长域终审遗留问题

> **来源**：欧阳锋 2026-06-28 渠道增长域 25 张卡终审结论（conditional pass）。
> 这些问题不阻塞卡片入库，但属于结构性债务，需要专项清理。

---

## 0. 任务元信息

| 项目 | 内容 |
|------|------|
| 任务类型 | 清理/标准化 |
| 来源 | 渠道增长域终审遗留问题 |
| 优先级 | P2 |
| 建议执行者 | 黄药师（目录/taxonomy 移动）或 老顽童（case section 标准化） |
| 预计工作量 | 0.5-1 小时 |
| 阻塞 | 无 |

---

## 1. 遗留问题清单

### 问题 1：13 张渠道增长域 case 卡 section 标题未对齐 lint 新标准

**影响范围**：
- `case-yitang-amazon-growth-flywheel`
- `case-yitang-novel-app-flywheel`
- `case-yitang-yitang-course-industrialization`
- `case-yitang-solid-redbull-channel`
- `case-yitang-maiyi-cloud-computer-channel`
- `case-yitang-topcity-growth-flywheel`
- `case-yitang-redburger-selection-industrialization`
- `case-yitang-lianjia-site-selection-industrialization`
- `case-yitang-yitu-lead-industrialization`
- `case-yitang-xujian-invoice-saas-channel`
- `case-yitang-yitang-shortvideo-industrialization`
- `case-yitang-shuzu-channel-scan-test`
- `case-yitang-yitang-self-growth-channel`

**问题描述**：
- 卡片正文已包含关键证据、可迁移场景、教训、失败模式等内容
- 但 section 标题未统一为 lint 新标准：
  - `## 关键证据`
  - `## 可迁移场景`
  - `## 教训`
  - `## 失败模式`
- 这是**全库 case 卡 section 系统性债务**，渠道增长域 13 张是其中一部分

**清理动作**：
1. 批量读取 13 张卡，识别现有对应内容段落
2. 将标题统一为 lint 标准 section 名称
3. 若某张卡确实缺少某 section 内容，则按素材补写，不硬凑
4. 每张改完单独跑 `kdo pre-submit -f <文件>`

**验收标准**：
- 13 张卡 `kdo pre-submit` 全部通过
- `kdo lint` 中 case section 相关 WARNING 减少或消失

---

### 问题 2：1 张 dk 卡目录未对齐 taxonomy

**影响范围**：
- `dk-yitang-channel-exploration-traps`

**问题描述**：
- 文件位于 `30_wiki/dk/`，但 KDO taxonomy 要求 dk 卡统一在 `30_wiki/dark-knowledges/`
- 卡片 `## 使用场景` 不是顶层 section（应在 `## 使用场景` 前加 `## 原始表述` 等标准结构）

**清理动作**：
1. 将文件从 `dk-yitang-channel-exploration-traps` 移动到 `30_wiki/dark-knowledges/dk-yitang-channel-exploration-traps.md`
2. 更新所有引用该卡的 `related` 链接（包括渠道增长域其他卡和跨域桥接卡）
3. 调整 section 结构：补充 `## 原始表述` / `## 使用场景` / `## 操作方法` / `## 适用边界` / `## 为什么值钱` / `## 与其他知识的关联`
4. 跑 `kdo pre-submit -f <文件>` 和 `kdo lint`

**验收标准**：
- 旧路径文件不存在，新路径文件存在
- 全库无 broken link 指向旧路径
- `kdo lint` 无新增 ERROR

---

### 问题 3：1 张 concept 卡目录未对齐 type

**影响范围**：
- `concept-yitang-channel-lean-validation-bridge`

**问题描述**：
- 文件位于 `30_wiki/frameworks/`，但 type 是 `concept`，应位于 `30_wiki/concepts/`

**清理动作**：
1. 将文件从 `concept-yitang-channel-lean-validation-bridge` 移动到 `30_wiki/concepts/concept-yitang-channel-lean-validation-bridge.md`
2. 更新所有引用该卡的 `related` 链接
3. 跑 `kdo pre-submit -f <文件>` 和 `kdo lint`

**验收标准**：
- 旧路径文件不存在，新路径文件存在
- 全库无 broken link 指向旧路径
- `kdo lint` 无新增 ERROR

---

## 2. 执行建议

### 方案 A：一次性清理（推荐）

由黄药师执行：
1. 先移动 2 个文件（dk + concept），更新全库 related 链接
2. 再由老顽童批量修复 13 张 case section 标题
3. 最后统一跑 `kdo lint` 验收

### 方案 B：拆分清理

- 问题 2/3 作为黄药师的 taxonomy 清理任务
- 问题 1 作为老顽童的 case section 标准化任务（可扩展为全库 case 卡，不仅渠道增长域 13 张）

---

## 3. 禁止事项

- 不要直接删除旧路径文件而不更新 related 链接
- 不要批量用正则替换 section 标题而不检查内容实质
- 不要在未跑 `kdo lint` 前宣称完成

---

## 4. 状态记录

| 日期 | 事件 | 操作人 |
|:---|:---|:---|
| 2026-06-28 | 欧阳锋渠道增长域终审发现遗留问题 | 欧阳锋 |
| 2026-06-28 | 王语嫣写本清理任务单 | 王语嫣 |
| 待填写 | 分配执行者并完成清理 | 待定 |

---

*维护人：王语嫣 | 最后更新：2026-06-28*
