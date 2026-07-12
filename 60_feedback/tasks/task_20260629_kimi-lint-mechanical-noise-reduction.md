---
id: task_20260629_kimi-lint-mechanical-noise-reduction
type: task
status: reviewed
assignee: 老顽童(Hermes)
priority: P1
created_at: 2026-06-29
updated_at: 2026-06-29
reviewer: 欧阳锋
source_refs:
- 60_feedback/tasks/task_20260629_kimi-full-frontmatter-compliance-cleanup.md
review_date: '2026-06-29'
---

# lint 机械类 WARNING 直接降噪

## 目标

在 #26 全库 frontmatter 合规修复的基础上，按用户要求对 lint WARNING 做“第一类”直接降噪：改 lint 阈值 + 批量处理机械可修项，不改卡的核心内容。

## 已完成的降噪动作

### 1. lint 阈值调整（黄药师建议）

修改 `kdo/workspace.py`：

- copy-paste 相似度阈值：`0.85` → `0.95`
- 标题数字 vs 正文数量容差：`actual >= expected * 3` → `abs(actual - expected) > 2`

### 2. source_refs 路径规范化

- 修复 435 个文件、511 个 source_refs 条目
- 将 `src_<id>-标题` 格式统一改为 `10_raw/sources/src_<id>-标题.md` 完整路径
- `src_unknown` 条目改为 `pending_archive: src_unknown`

### 3. index.md 批量补录

- 将 1637 个未列入 `30_wiki/index.md` 的 wiki 页面按子目录分组追加到索引末尾
- 修正 wikilink 路径中的反斜杠为正斜杠，确保 kdo 能正确解析

### 4. Tool card 标准 section 骨架补全

- 对 751 个 tool 卡批量补全缺失的标准 section 骨架：
  - `## 目的`
  - `## 操作步骤`
  - `## 不要用的场景`
  - `## 质疑`

## 降噪效果

| 检查项 | 调整前 | 阈值调整后 | source_refs 后 | index 后 | section 后 |
|:---|---:|---:|---:|---:|---:|
| `kdo lint` WARNING | 7507 | 6523 | 6012 | 4379 | **3286** |
| `kdo lint` ERROR | 0 | 0 | 0 | 0 | 0 |

累计减少 WARNING：**4221**（-56%）

## 剩余 WARNING 基线

- 日期：2026-06-29
- `kdo lint`：0 ERROR / 3286 WARNING
- 主要剩余类型：
  - L2 Critique 缺关键术语：846
  - Critique section 无外部攻击者姓名：717
  - Section 高度相似（copy-paste）：~720
  - L2 Condense 0 要点：215
  - L2 Synthesis 0 外部链接：187
  - body 过短 / 无来源 / artifact 未注册等：~100

这些属于内容债，需按 domain 分批改写，已拆分为独立任务 #27。

## 验收标准

- `kdo lint` 0 ERROR ✅
- 机械类 WARNING（index、source_refs、section 骨架）批量清零 ✅
- `kdo pre-submit` 不退化 ✅

---

> 本任务为 #26 的延续，承接用户“继续”指令，对 lint WARNING 做机械类降噪。剩余内容债进入 `task_20260629_kimi-lint-content-debt-by-domain.md` 按域分批处理。

## 欧阳锋终审记录

- **审查时间**：2026-06-29
- **实测验证**：
  - `kdo lint`：0 ERROR / 3286 WARNING，符合任务表预期 ✅
  - `kdo pre-submit`：Result PASS ✅
  - `kdo/workspace.py` 阈值调整已确认：`copy-paste` 0.85→0.95，标题数字容差改为 `abs(actual - expected) > 2` ✅
- **审查结论**：机械类降噪目标达成，状态置为 `reviewed`。
- **下一步**：剩余 3286 WARNING 为内容债，进入 `task_20260629_kimi-lint-content-debt-by-domain.md` 按域分批处理，不再做机械修复。
