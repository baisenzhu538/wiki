---
id: kdo-scaffold-v15
title: "kdo scaffold — 为缺失 v1.5 信号的卡片自动生成升级骨架"
status: todo
priority: P0
assigned_to: 黄药师
reviewer: 欧阳锋
created: 2026-05-19
depends_on: validate-v15-upgrade-plan
---

## 背景

`kdo validate --v15 --upgrade-plan` 已经能精确诊断每张卡缺什么（89 FAIL + 71 WARN）。但老顽童开工修卡时，每张都要从空白页开始写 Critique/不要用场景/Action Triggers——重复劳动是定格式、查学者、写占位。

`kdo scaffold` 在 plan 之上加一层：**读卡 → 诊断缺失 → 生成带 TODO 占位符的骨架**。老顽童拿到的不再是"这张卡缺 Critique"，而是"这张卡的 Critique 节已经搭好框架，学者方向已建议，你填内容即可"。

## 目标

`kdo scaffold --card <id>` 在目标卡片末尾追加缺失节的 TODO 骨架。不覆盖已有内容。不改已有内容。

## 核心逻辑

### Step 1 — 读取卡现状

复用 `_parse_card_sections()` + `classify_card_structure()` + `_read_frontmatter()`，确定：
- 结构类型（standard-concept / pan-product / research / ...）
- 已有哪些节（Critique？不要用场景？Action Triggers？）
- 每节的当前信号数（攻击者数 × 不要用行数 × AT 行数）

### Step 2 — 计算缺失

对照 v1.5 校验矩阵，列出缺口：

| 缺口 | 触发条件 |
|------|---------|
| `missing_critique` | 结构需要 Critique 但不存在 |
| `missing_attacks` | Critique 存在但攻击者 <2（**只追加攻击段落，不重建整节**） |
| `missing_no_use` | 需要不要用场景但不存在或 <2 |
| `missing_triggers` | 需要 Action Triggers 但不存在或 <3 |

### Step 3 — 生成骨架

三类骨架模板：

#### 缺 [Critique] 整节时：

```markdown
## Critique

### 外部攻击

#### [ATTACKER_1]：[ONE_LINE_SUMMARY]

> [TODO: 选择一位与「{card_title}」核心假设冲突的跨范式学者。参考方向：{suggested_direction_1}]

[TODO: 写 3-4 段攻击论述——学者的核心论点是？与本卡核心主张的冲突点？具体攻击角度？]

> **{attacker_1} 让读者睡不着觉的问题**：[TODO: 一个直击要害的拷问]

#### [ATTACKER_2]：[ONE_LINE_SUMMARY]

> [TODO: 选择第二位攻击者，从与前一位不同的角度攻击。参考方向：{suggested_direction_2}]

[TODO: 写 3-4 段攻击论述]

> **{attacker_2} 让读者睡不着觉的问题**：[TODO]

### 内部局限

- [TODO: 工具/框架本身的内部局限，非外部攻击。至少 3 条。常见角度：前提假设脆弱、执行门槛、跨场景迁移失效、依赖上下游配合]
```

#### 缺攻击者（Critique 存在但 <2）时：

在现有 `### 外部攻击` 节末尾追加：

```markdown
#### [ATTACKER_NAME]：[ONE_LINE_SUMMARY]

> [TODO: 选择一位跨范式学者。已有攻击者：{existing_attackers}。建议从 {suggested_angle} 角度攻击。参考方向：{suggested_direction}]

[TODO: 写 3-4 段攻击论述]

> **{attacker_name} 让读者睡不着觉的问题**：[TODO]
```

#### 缺 不要用场景：

```markdown
### 不要用的场景

| 场景 | 为什么失效 | 替代方案 |
|------|-----------|---------|
| [TODO: 场景1 — 什么情况下本工具/概念反而不适用？] | [TODO: 失效原因] | [TODO: 替代做法] |
| [TODO: 场景2] | [TODO] | [TODO] |
```

（已有部分行时只追加缺失行，不重建表头）

#### 缺 Action Triggers：

```markdown
## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---------|-----------|---------|
| [TODO: 场景1 — 什么情况下应该使用本工具？] | [TODO: 立即可执行的第一步] | [TODO: 可量化的完成标准] |
| [TODO: 场景2] | [TODO] | [TODO] |
| [TODO: 场景3] | [TODO] | [TODO] |
```

### Step 4 — 智能建议（核心差异化价值）

骨架不是空白 TODO——**每个 TODO 带上下文提示**。提示来源：

#### 4a. 攻击者建议

按 domain + 关键词做三层匹配：

1. **同域攻击者池**：扫描同 domain 下已有 Critique 的卡，收集所有攻击者名 → 去重 → 排除该卡已用过的 → 按出现频次排序 → 取 top 3
2. **跨域经典配对**：硬编码已知高频有效配对（如 Kahneman+Klein, Taleb+Popper, Mintzberg+Pfeffer），匹配卡主题关键词
3. **fallback**：如果上述都没命中，留 "[TODO: 选择合适的跨范式学者]" 不编造

#### 4b. 不要用场景提示

从卡的 Summary/Claims 提取核心假设，反写为边界条件：

```
假设：本工具预设"管理者有管理意愿"
→ 不要用场景提示：[TODO: 管理者抗拒管理/认为管理是官僚主义时？]
```

用 LLM 做这一步（`kdo query` 或直接调 DeepSeek API，~200 tokens/card）。**如果 LLM 不可用，fallback 到通用提示。**

#### 4c. Action Triggers 提示

从卡的 query_triggers 和 Summary 提取高频触发词，反写为具体场景。

### Step 5 — 写入

- **默认 dry-run**：只输出 diff，不修改文件
- `--write`：实际写入。不覆盖已有节，只追加缺失节/段落
- 写入后不自动运行 validate（留给用户验证）

## CLI 接口

```bash
kdo scaffold --card <id>              # 单卡骨架（dry-run）
kdo scaffold --card <id> --write      # 单卡骨架（写入）
kdo scaffold --batch A                # 整批 dry-run（A=全信号缺失高引, B=缺攻击, C=缺AT, D=研究降级, E=warnings）
kdo scaffold --batch A --write        # 整批写入
kdo scaffold --from-plan              # 读取最近一次 validate --v15 --upgrade-plan 的输出，按优先级分批
kdo scaffold --card <id> --no-hints   # 纯骨架不带智能提示（快速模式）
```

## 技术实现

- 位置：`kdo/commands/quality.py`（新增 `cmd_scaffold` 函数，注册到 `cli.py`）
- 复用：`_parse_card_sections`、`classify_card_structure`、`_read_frontmatter`、`_count_*`、`_card_citation_count`
- 新增：
  - `_detect_missing(checks, structure)` → dict of gaps
  - `_generate_critique_skeleton(card_id, fm, existing_attackers, domain_pool)` → str
  - `_generate_no_use_skeleton(existing_count, needed)` → str
  - `_generate_triggers_skeleton(existing_count, needed)` → str
  - `_get_attacker_suggestions(domain, keywords, existing_attackers, concepts_dir)` → list[str]
  - `_get_context_hints(card_id, section_type)` → list[str]（LLM 或 fallback）
  - `_apply_scaffold(card_path, sections_to_add)` → writes file
- ~200-250 行代码
- ~8 个新 test cases

## 验收标准

- [ ] `kdo scaffold --card <id>` 对已有 Critique 的卡不追加重复节
- [ ] `kdo scaffold --card <id>` 对缺 Critique 的卡正确生成完整骨架（含攻击者提示）
- [ ] `kdo scaffold --card <id>` 对缺 Action Triggers 的卡正确追加 AT 表（不覆盖已有的 2 行只补 1 行）
- [ ] `--batch A/B/C/D/E` 分组正确
- [ ] `--write` 实际写入，`dry-run`（默认）只输出 diff
- [ ] 攻击者建议不推荐该卡已有的攻击者
- [ ] 同域攻击者池从实际卡片数据中提取，非硬编码
- [ ] 对 205 张真实卡运行 `--from-plan`，无崩溃
- [ ] 写入后原卡的已有内容完整保留（逐字节验证 ≥3 张卡）
- [ ] pytest ≥8 新 test cases，全绿

## 不做

| 候选项 | 理由 |
|--------|------|
| 自动生成攻击内容 | 攻击段落的论证质量需要人的判断，自动生成 = 稻草人风险 |
| 自动选择攻击者（不做建议只做推荐） | 跨范式配对是创作决策，不是工程决策 |
| 自动修改已有节的内容 | 只追加，不编辑。已有内容神圣不可侵犯 |
| 自动运行 validate 验证骨架 | scaffold 不保证通过 validate——骨架填完内容后才应该跑 validate |
| 建立全库学者→主题映射数据库 | 太重。同域扫描 + 高频配对表足够 |
| 用 PageRank/外部图数据库排攻击者优先级 | 零依赖原则。同域频次排序够用 |

## 使用流程（老顽童视角）

```bash
# 1. 看升级计划
kdo validate --v15 --upgrade-plan

# 2. 从 Batch A 开始（全信号缺失高引卡）
kdo scaffold --batch A --write

# 3. 打开被 scaffold 的卡，填 TODO
#    - 攻击者提示给了方向，去 Wikipedia/Google Scholar 验证学者论点
#    - 不要用场景提示给了假设反写，补真实案例
#    - AT 提示给了触发词，补具体动作和指标

# 4. 填完后验证
kdo validate --v15 --card <id>

# 5. 通过 → 下一张
```

## 相关

- [[70_product/tasks/validate-v15-upgrade-plan.md]] — 前置工单（plan 是 scaffold 的数据源）
- [[70_product/tasks/quality-gate-automation-v15.md]] — 前置工单（validate 是 scaffold 的检测源）
- [[70_product/tasks/laowantong-next-tasks.md]] — 老顽童任务队列（包含 89 卡修复任务）
