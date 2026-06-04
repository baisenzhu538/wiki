---
title: "Spec: kdo stale --propagate — 增量传播机制"
status: approved
created_at: 2026-06-05
author: 黄药师
reviewer: 欧阳锋（待审查）
source_task: Task B — huangyaoshi-next-tasks.md
depends_on:
  - kdo stale --apply (Task A, committed 9f9b658)
---

# Spec: kdo stale --propagate — 增量传播机制

## 问题

卡片 A 被 `kdo stale --apply` 标记为 `status: needs-review` 后，所有通过 `[[wikilink]]` 引用 A 的卡片 B/C/D 无法感知——它们依赖的知识可能已经过期。

当前 wiki-link 是单向的（`[[A]]` 只记录 A 被引用，无法查"谁引用了 A"），没有反向引用能力。

## 目标

`kdo stale --propagate` 扫描所有卡片的 `[[wikilink]]`，找到引用了 stale 卡片的依赖者，在依赖者的 frontmatter 中写入 `stale_dependencies` 列表。

---

## 设计

### 数据流

```
kdo stale --apply                 kdo stale --propagate
      │                                  │
      ▼                                  ▼
┌──────────────────┐           ┌──────────────────────┐
│ 标记 stale 卡片    │           │ 1. 收集所有             │
│ status:           │           │    status: needs-review │
│ needs-review      │           │    的卡片 ID            │
└──────┬───────────┘           │                        │
       │                       │ 2. 全量扫描 30_wiki/*.md │
       ▼                       │    提取 [[wikilink]]     │
┌──────────────────┐           │    内存建反向索引         │
│ 30_wiki/*.md     │           │                        │
│ frontmatter 已更新 │           │ 3. 匹配：引用者 ∩ stale  │
└──────────────────┘           │                        │
                               │ 4. 写入 stale_           │
                               │    dependencies         │
                               │    到引用者 frontmatter   │
                               │                        │
                               │ 5. 清理：依赖已解除的      │
                               │    自动删除字段           │
                               └──────────────────────┘
```

### Frontmatter Schema

```yaml
# 被 propagate 后的卡片（引用了已 stale 的卡片）
stale_dependencies:
  - yt-scientific-decision
  - yt-model-y-organization
```

- 存卡片 wikilink 目标名（不含 `.md`、不含路径、不含锚点/别名）
- 去重排序
- 空列表时删除整个字段（不残留 `stale_dependencies: []`）
- 不影响 `status`——stale 是别人的事，依赖者只是被通知

### Wikilink 解析

正则：`\[\[([^\]|#]+)(?:[^\]]*)?\]\]`

| 格式 | 提取目标 |
|:------|:--------|
| `[[A]]` | A |
| `[[A\|显示文字]]` | A |
| `[[A#heading]]` | A |
| `[[self]]`（引用自己） | 忽略 |
| 目标卡片不存在 | 忽略（`kdo lint` 单独报断链） |

反向索引是内存字典：`{"card_id": ["引用者1", "引用者2", ...]}`，用完即弃。

### 匹配与写入逻辑

```
stale_set = {所有 needs-review 卡片的 id}
if stale_set 为空 → exit 0, "No stale cards to propagate"

for 每张卡片 B（排除 index/log/contradictions）:
    linked = B 正文中所有 [[目标]]
    hits = linked ∩ stale_set

    if hits:
        B.stale_dependencies = sorted(hits)           # 写入
    else:
        if B 已有 stale_dependencies:
            del B.stale_dependencies                  # 依赖已全部解除
```

幂等：重复跑不会累积重复条目。

### dk-* 卡片的处理

dk-* 卡片自己永不过期（Task A 跳过它们），但如果 dk-* 引用了 stale 卡片，**照常标记** `stale_dependencies`——别人过期了，dk 卡片作为引用者需要知道。

---

## CLI 接口

```bash
# 两步流程
kdo stale --apply              # Step 1: 标记 stale
kdo stale --propagate          # Step 2: 传播依赖

# 预览
kdo stale --propagate --dry-run

# JSON 输出
kdo stale --propagate --json

# 一步到位
kdo stale --apply --propagate
```

### Flag 组合

| Flag | 行为 |
|:------|:-----|
| `--apply` | 只标记 stale（已有行为） |
| `--propagate` | 只传播（基于已有 `needs-review`） |
| `--apply --propagate` | 先标记再传播，顺序执行 |

### 输出

```
$ kdo stale --propagate

Propagation:
  yt-management-basic-skills → +2 stale deps (yt-scientific-decision, yt-model-y)
  yt-pitch-metaphor → +1 stale dep (yt-pitch-cialdini)
  yt-entrepreneur-key-hypotheses → cleared (1 dependency resolved)

Summary: 3 cards updated, 1 cleared, 150 unaffected
```

`--json`：
```json
{
  "propagated": [
    {"card": "yt-management-basic-skills", "added": ["yt-scientific-decision", "yt-model-y"]}
  ],
  "cleared": ["yt-entrepreneur-key-hypotheses"],
  "unaffected": 150
}
```

### Exit Codes

| Code | 含义 |
|:----:|:-----|
| 0 | 成功（含 0 张受影响卡片） |
| 1 | 错误（workspace 不存在、文件写入失败等） |

---

## 边界情况

| 场景 | 行为 |
|:------|:-----|
| 没有 `needs-review` 卡片 | "No stale cards to propagate"，exit 0 |
| 引用不存在的 wikilink | 忽略 |
| 已有 `stale_dependencies`，本次无新匹配 | 不变 |
| 已有 `stale_dependencies`，依赖全部恢复 | 删除字段 |
| 一张卡引用多张 stale 卡 | 全部列出，去重排序 |
| `--propagate` 跑两次 | 幂等，第二次 0 变更 |
| `--apply --propagate` 但 --apply 无发现 | propagate 跳过 |
| 写入失败的单张卡 | warning 继续，不中断全量 |

---

## 实现

### 文件

单文件扩展：`commands/stale.py`（方案 A）

- 新增 `cmd_stale_propagate(args)` 函数
- `build_parser` 中 `--propagate` 路由到此函数
- `--apply --propagate` 时先调 `cmd_stale` 再调 `cmd_stale_propagate`

### 估时

~1.5h，~150 行代码。

---

## 测试（≥8 tests）

| 测试 | 验证点 |
|:------|:-----|
| `test_propagate_adds_deps` | 引用 stale 卡 → `stale_dependencies` 出现 |
| `test_propagate_multiple_deps` | 引用多张 stale 卡 → 全部列出 |
| `test_propagate_clears_resolved` | 依赖已解除 → 字段删除 |
| `test_propagate_no_stale_cards` | 无 needs-review → 0 变更 |
| `test_propagate_idempotent` | 跑两次 → 第二次无变更 |
| `test_propagate_dry_run_no_write` | `--dry-run` → frontmatter 不变 |
| `test_propagate_ignores_self_ref` | `[[self]]` → 不触发 |
| `test_propagate_ignores_broken_link` | 不存在的目标 → 忽略 |

回归：现有 25 stale tests + 全量 454 tests。

---

## 决策记录

| # | 决策 | 结论 |
|:--:|:-----|:-----|
| 1 | 传播信号级别 | `stale_dependencies` 列表，不改 status |
| 2 | 记录格式 | 直接写 frontmatter，自包含 |
| 3 | 生命周期 | `--propagate` 全量刷新，自动清理 |
| 4 | 索引策略 | 按需全量扫描，内存反向索引 |
| 5 | 文件结构 | 扩展 `commands/stale.py` |
| 6 | dk-* 是否传播 | 照常标记（dk 自己不 stale，但依赖可能过期） |
