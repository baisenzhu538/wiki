---
id: sprint-6-agent-native-upgrade-all-cards
title: "Sprint 6：全量卡片 Agent-Native 格式升级"
status: in_progress
priority: P0
assigned_to: 黄药师
reviewer: 欧阳锋
domain: all
created: 2026-05-12
target: 2026-05-12
---

## 背景

Sprint 5 完成了 7 张 composite+framework 卡的 agent-native 升级，质量门禁全部通过。
Sprint 6 的目标：将剩余 ~67 张卡片全部升级到 agent-native 格式。

## 范围盘点

| 前缀 | 数量 | 当前状态 | 当前 type |
|------|------|---------|-----------|
| `yt-model-*` (非 pan-product) | ~21 | 旧格式，source_refs 多为 `[]` | concept |
| `yt-entrepreneur-*` | ~23 | 旧格式，source_refs 含 `00_inbox/` | concept |
| `yt-personal-*` | ~22 | 旧格式，source_refs 为空或 `00_inbox/` | concept |
| **合计** | **~66** | | |

## 升级标准（来自 agent-native-card-design.md）

### Frontmatter 必填字段

```yaml
id: "yt-{prefix}-{slug}"          # 统一 id，与文件名一致
title: "..."                       # 保留原 title
type: "tool" | "framework" | "case"  # 按内容复杂度判定
status: "enriched"
domain: "yitang"
language: "zh-CN"
version: 1
difficulty: "foundational" | "intermediate" | "advanced"
confidence: 0.80                   # 估计值

prerequisites: []                  # 前置卡片 id 列表
component_of: []                   # 所属上层卡片
related: []                        # 相关卡片
contradicts: []                    # 矛盾卡片

query_triggers: ["..."]            # 5-10 个中文搜索触发词
tags: ["..."]                      # 3-6 个标签

source_refs:                       # 必须指向 10_raw/
  - "10_raw/sources/xxx.md"
  - "10_raw/assets/yitang/xxx.png"

estimated_tokens: 800              # 估计 token 数
reviewed_by: "黄药师"
```

### 卡片类型判定

| type | 适用场景 | Claims 上限 | 体量上限 |
|------|---------|------------|---------|
| `framework` | 跨多张卡片的整合框架（如五步法、IPO模型、个人地图） | 15 | 300行 |
| `tool` | 单节课/单张卡牌的方法工具 | 10 | 150行 |
| `case` | 案例、探索营、启发式内容 | 8 | 120行 |

### Body 格式

```
## Claims

### {分组标题}
- claim:01 [conf=0.XX][src: 来源] 核心主张
- claim:02 [conf=0.XX][src: 来源] 核心主张

## Framework Gallery
### 关联框架卡
- [[关联卡片]] — 说明
### 关键原图
- ![[原图名.png]]

## Constraints & Boundaries
- claim:boundary-01 [conf=0.XX] 边界约束

## Synthesis
| 关系 | 目标节点 | 说明 |
|------|---------|------|
```

## 执行策略：三阶段分步

### Phase 1：P0 紧急 — 修复 source_refs（先做，影响最大）

**目标**：所有 `source_refs: ["00_inbox/..."]` 和 `source_refs: []` → 补全为 `10_raw/` 路径

**规则**：
- 文本源 → `10_raw/sources/`（文件名保持一致）
- 图片源 → `10_raw/assets/yitang/`
- 如果源文件确实不存在于 10_raw/，标注 `# TODO: verify source` 并保持原路径
- KF-020 铁律：source_refs 绝不能指向 00_inbox/

**验证**：`grep -r "00_inbox" 30_wiki/concepts/` 返回空

### Phase 2：P1 重要 — 升级 frontmatter（批量）

**目标**：为每张卡添加 agent-native frontmatter 字段

**操作**：
1. 添加 `id:` 字段（与文件名一致）
2. 修改 `type:` → `tool` / `framework` / `case`（按判定标准）
3. 添加 `query_triggers:`（从 title + 内容核心概念提取 5-10 个中文词）
4. 添加 `prerequisites:` / `component_of:` / `related:` / `contradicts:` 图边字段
5. 添加 `estimated_tokens:`（粗略估计）
6. 保留原有 `yitang:` 子字段（向后兼容，agent 不使用但人类可读）
7. 统一 `tags:` 格式为 `["tag1", "tag2"]`

**不删除**原有旧字段（domain, yitang.*），只新增 agent-native 字段。

### Phase 3：P2 改进 — 升级 body 格式（渐进）

**目标**：将 body 从 `## [Condense]` / `## [Critique]` / `## [Synthesis]` 映射为 agent-native 格式

**映射规则**（来自 agent-native-card-design.md）：
- `## Summary` + `## [Condense]` → `## Claims`（每条核心观点拆成 `claim:NN [conf=X][src:Y]`）
- `## [Critique]` → `## Constraints & Boundaries`（边界条件格式化为 `claim:boundary-NN`）
- `## [Synthesis]` → `## Synthesis`（关系表格式，保留双向链接）
- 原有 `## Framework Gallery` 保留（补全维基链接）

**体量控制**：
- tool 卡：3-10 claims，≤150 行
- framework 卡：5-15 claims，≤300 行

**注意**：Phase 3 不需要一次完成。优先完成 Phase 1+2，Phase 3 可按 domain 分批推进。

## 执行顺序：先高价值域

| 批次 | 域 | 卡片 | 理由 |
|------|-----|------|------|
| Batch 1 | pan-product 工具卡 | yt-personal-pan-product-* (6张) | 与已完成的 7 张 framework 卡形成完整闭环 |
| Batch 2 | model 框架卡 | yt-model-* (21张) | 框架卡是知识库骨架，query 命中率高 |
| Batch 3 | entrepreneur 工具卡 | yt-entrepreneur-* (23张) | 体量大但格式统一，可高效批处理 |
| Batch 4 | personal 工具卡 | yt-personal-* (16张) | 收尾 |

### ✅ Batch 1 完成 (2026-05-12 黄药师)

33 yt-panproduct-* + 6 yt-personal-pan-product-* = **39 张卡全部升级完成**。

**Phase 1**: source_refs 迁移 00_inbox/ → 10_raw/（29 PNG 归档到 assets/yitang/，1 MD 归档到 sources/）
**Phase 2**: frontmatter 注入 agent-native 字段（Python PyYAML 批处理）
**Phase 3**: body 格式升级：
- `[Condense]` → `Claims`，`[Critique]` → `Constraints & Boundaries`，`[Synthesis]` → `Synthesis` 表格式
- `## Synthesis` 表格式转换（39/39）
- `claim:boundary-NN` 格式转换（6/6 有 Constraints 的卡）
- `## Framework Gallery` 新增（39/39）

**质量门禁**:
- [x] `grep '"00_inbox'` → 0 hits
- [x] kdo lint: 0 errors, 305 warnings（全部存量）
- [x] 39/39 卡有 `id:`、`query_triggers:`、`estimated_tokens:`
- [x] 体量合规：全部 ≤150 行
- [x] 旧格式 headers 0 残留

### ✅ Batch 2 完成 (2026-05-13 黄药师)

22 张 yt-model-* 非 pan-product 框架卡全部升级完成。

**Phase 1**: 12 张 PNG 从 00_inbox/ 归档到 10_raw/assets/yitang/，source_refs 全部迁移（10 张卡片，0 残留 00_inbox/）
**Phase 2**: frontmatter 注入 agent-native 字段（type: framework, component_of: [], prerequisites: []）
**Phase 3**: body 格式升级：
- `[Condense]` → `Claims`（22/22）
- `## Framework Gallery` 新增（22/22）
- `## Synthesis` 表格式转换（22/22）
- `claim:boundary-NN` 格式转换（1/1 有 Critique 的卡）
- 旧格式 headers 0 残留

**质量门禁**:
- [x] `grep '"00_inbox' yt-model-*.md` → 0 hits
- [x] kdo lint: 0 errors, 305 warnings（全部存量）
- [x] 22/22 卡有 `id:`、`query_triggers:`、`estimated_tokens:`
- [x] 22/22 `type: framework`

### ✅ Batch 3 完成 (2026-05-13 黄药师)

23 张 yt-entrepreneur-* 工具卡全部升级完成。

**Phase 1**: 3 个 MD 口述稿从 00_inbox/ 归档到 10_raw/sources/，source_refs 路径迁移（sed 简单字符串替换，5 张卡片，0 残留 00_inbox/）
**Phase 2**: frontmatter 注入 agent-native 字段（type: tool, status: enriched 升级了 3 张 draft 卡）
**Phase 3**: body 格式升级：
- `[Condense]` → `Claims`（23/23）
- `## Framework Gallery` 新增（23/23）
- `## Synthesis` 表格式转换（23/23）
- `claim:boundary-NN` 格式转换（有 Critique 的卡）
- 旧格式 headers 0 残留

**质量门禁**:
- [x] `grep '"00_inbox' yt-entrepreneur-*.md` → 0 hits
- [x] kdo lint: 0 errors, 309 warnings（全部存量）
- [x] 23/23 卡有 `id:`、`query_triggers:`、`estimated_tokens:`
- [x] 23/23 `type: tool`

## 质量门禁

完成每个 Batch 后自查：
- [ ] `grep -r '"00_inbox' 30_wiki/concepts/` 返回空（指向该 batch 的卡片）
- [ ] 每张卡有 `id:` 字段
- [ ] 每张卡有 `query_triggers:` 且非空
- [ ] 每张卡有 `estimated_tokens:`
- [ ] `type:` 符合卡片类型判定标准
- [ ] 不删除任何原有有价值内容（向后兼容）

## 完成信号

全部 4 个 Batch 完成后，通知 欧阳锋 做 Sprint 6 终审。
