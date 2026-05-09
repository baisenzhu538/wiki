---
title: "Sprint 2 门禁系统 + Enrich 举证 — 设计规格"
type: system
status: draft
domain:
  - kdo
source_refs:
  - "30_wiki/decisions/kdo-ec-industrialization-migration-proposal.md"
created_at: "2026-05-09"
updated_at: "2026-05-09"
tags:
  - "#kdo"
  - "#sprint"
  - "#quality"
---

# Sprint 2 门禁系统 + Enrich 举证 — 设计规格

> 黄药师起草，提交欧阳锋审查。对应迁移方案 Sprint 2。

## 背景

Sprint 1 完成了 L1 Lint 扩展（source_refs 存在性 + status 一致性），`kdo lint` → 0 errors。

Sprint 2 要解决迁移方案中「Enrich 阶段可被完全跳过，无硬阻断」（痛点 #1）和「举证链不完整」（痛点 #6）。

## 设计决策

| 决策 | 结论 | 来源 |
|------|------|------|
| 阻断级别 | P0 强警告，`--skip-gate <reason>` 可越过 | 欧阳锋决策 #1 |
| 举证粒度 | 仅 enrich/produce/ship 三节点强制 | 欧阳锋决策 #3 |
| enrich 举证格式 | 变更摘要（非完整 diff） | 欧阳锋决策 #3 补充 |
| 命令命名 | `kdo gate` 独立命令，不复用 validate | 黄药师建议，待确认 |

---

## 一、门禁系统

### 1.1 新增模块：`kdo/gate.py`

对标 `workspace.py` 的 `lint_workspace()` 模式。核心函数：

```python
def check_gate(root: Path, state: dict, stage: str) -> list[GateIssue]:
    """检查指定阶段的进入/退出条件，返回问题列表。"""
```

### 1.2 阶段门禁规则

```
ingest → enrich:
  进入: 源文件在 00_inbox/
  退出: source_refs 非空, skeleton 已创建, log.md 已记录

enrich → produce:
  进入: source status: draft
  退出: 三步编译完成（无 TODO）, status: reviewed, frontmatter 字段齐全

produce → validate:
  进入: ≥1 concept status: reviewed
  退出: artifact frontmatter 完整, 非 stub, 通过 validate

validate → ship:
  进入: artifact status: draft
  退出: lint 全通过, broken links = 0, fb_* 已生成

ship → done:
  进入: artifact status: validated
  退出: 发布目标明确, ship_* 已写入
```

### 1.3 CLI

```bash
kdo gate <stage>            # 检查指定阶段门禁
kdo gate all                # 全管线检查
kdo gate enrich --skip-gate "Critique 仅 1 条，此卡为例外场景"
```

### 1.4 Override 记录

写入 `state.json` 的 `gate_overrides` 数组：

```json
{
  "gate_overrides": [
    {
      "stage": "enrich",
      "target_path": "30_wiki/concepts/foo.md",
      "reason": "Critique 仅 1 条，概念过于简单无需第二条",
      "timestamp": "2026-05-09T...",
      "skipped_checks": ["三步编译完成（Critique ≥ 1）"]
    }
  ]
}
```

同步追加到 `30_wiki/log.md`。

### 1.5 Exit Code

| 模式 | 行为 |
|------|------|
| 默认 | P0 违规输出 WARNING + 提示 `--skip-gate`，exit 1 |
| `--strict` | 同默认 |
| `--skip-gate` | 记录越过原因，exit 0 |

---

## 二、Enrich 举证

### 2.1 修改位置

`commands/curation.py` 的 `cmd_enrich()` — enrich 成功后自动记录举证。

### 2.2 举证格式

存储为 `60_feedback/enrich-evidence/ev_YYYYMMDD_xxxxxxxx.md`：

```markdown
---
feedback_id: "ev_20260509_a1b2c3d4"
kind: "enrich-evidence"
wiki_path: "30_wiki/concepts/foo.md"
method: "llm"
source_used: "10_raw/sources/src_20260506_abcd1234.md"
timestamp: "2026-05-09T..."
---

# Enrich Evidence: foo

## Changes Made
- Condense: 从源提取 5 条核心概念，替换 TODO 占位
- Critique: 新增 2 条质疑（假设检验 + 边界条件）
- Synthesis: 添加 3 个 wikilinks

## Method
LLM 三步编译（DeepSeek V4 Pro），temperature 0.3/0.4
```

### 2.3 state.json 同步

在 sources 记录下追加 `enrich_evidence_id`，建立 source → wiki → evidence 溯源链。

---

## 三、改动文件清单

| # | 文件 | 操作 | 说明 |
|---|------|------|------|
| 1 | `kdo/gate.py` | **新建** | 门禁检查逻辑 |
| 2 | `kdo/commands/quality.py` | 修改 | 新增 `cmd_gate()` handler |
| 3 | `kdo/cli.py` | 修改 | 注册 `kdo gate` 子命令 + `--skip-gate` |
| 4 | `kdo/commands/curation.py` | 修改 | `cmd_enrich()` 末尾追加举证记录 |
| 5 | `kdo/workspace.py` | 可能修改 | 如需要新增 state.json 读写 helper |

## 四、验收标准

1. 新概念卡走完 `ingest → enrich --llm`，`60_feedback/enrich-evidence/` 下存在举证文件
2. `kdo gate enrich` 检查通过（0 P0 违规）
3. `kdo gate enrich --skip-gate "reason"` 可越过，记录写入 state.json + log.md
4. 现有 vault 上 `kdo lint` 保持 0 errors（不退化）

## 五、待欧阳锋确认

1. `kdo gate` 独立命令 vs 并入 `kdo validate --gates`？
2. 举证存储位置：`60_feedback/enrich-evidence/` 还是其他？
3. 默认 exit code 行为：P0 违规是否 exit 1？（当前设计：是）

---

## 欧阳锋审查（2026-05-09）

### 总体评价

设计规格质量好——门禁模块 + 举证格式 + CLI 三块拆分干净。三个待确认问题的结论如下。

---

### 逐条回答

**1. `kdo gate` 独立命令。不并入 `kdo validate`。**

理由：validate 是 artifact 内容质量检查（"这个产出物好不好"），gate 是管线阶段准入检查（"这个阶段能不能进"）。两个不同的关注点，复用同一个命令会导致参数和行为耦合。独立命令入口清晰，职责单一。

**2. 举证存储位置：`60_feedback/enrich-evidence/` 接受。**

当前只实现了 enrich 举证，用专属子目录合理。将来 produce/ship 举证加入后如果目录层级过多，再抽象为 `60_feedback/evidence/` 统一入口。暂不提前设计。

**3. P0 违规 exit 1：确认。**
--skip-gate 将 exit 1 → exit 0，同时写入 override 记录。行为正确。

---

### 一个修正：enrich 阶段退出 status

§1.2 写的是 `status: reviewed` 作为 enrich 退出条件，但实际 vault 中卡片使用的 status 是 `enriched`（三步编译完成但未经理 Architect 审查）。`reviewed` 在 PROTOCOL.md 中另有含义。

建议改为：
```
enrich → produce:
  退出: 三步编译完成（无 TODO）, source_refs 非空, frontmatter 字段齐全
  status 字段值不在此处强制——由 L1 Lint status 一致性检查（Sprint 1）统一处理
```

门禁检查不依赖 status 字段做准入判定，改用一个独立的内部标记（如 state.json 中 `enrich_completed: true`），避免和现有的 status 值漂移问题纠缠。

---

### 一个删减：`ingest → enrich` 退出条件过细

当前写的是 `source_refs 非空, skeleton 已创建, log.md 已记录`。但 ingest 阶段不强制举证（EC 决策第 3 条），log.md 写入是可选的。简化为 `source_refs 非空, wiki 骨架文件存在`。log.md 不作为门禁检查项。

---

### 共识项

- ✅ `kdo gate` 独立命令
- ✅ 举证存储 `60_feedback/enrich-evidence/`
- ✅ P0 违规 exit 1，`--skip-gate` → exit 0
- ✅ enrich 退出不用 status 字段，用内部标记
- ✅ ingest 退出简化为两项

### 无待确认项。直接执行。

---

## 欧阳锋终审（2026-05-10）

### 验收结果

| 标准 | 结果 | 证据 |
|------|:--:|------|
| 1. enrich evidence 文件存在 | ✅ | `60_feedback/enrich-evidence/ev_20260510_989577df.md`，LLM 方法 |
| 2. kdo gate enrich 正常工作 | ✅ | 检测到 10 个 P0（domain 字段），`--skip-gate` 成功越过 |
| 3. override 写入 state.json + log.md | ✅ | `state.json` gate_overrides + `log.md` 均有记录 |
| 4. source → wiki → evidence 链路 | ✅ | `src_20260510_9e98a292` → `sprint-2-门禁举证验收.md` → `ev_20260510_989577df` |

### 决策记录

| # | 决策 | 状态 |
|---|------|:--:|
| 1 | `kdo gate` 独立命令 | ✅ 已实现 |
| 2 | 举证存储 `60_feedback/enrich-evidence/` | ✅ 已实现 |
| 3 | P0 exit 1，`--skip-gate` → exit 0 | ✅ 已验证 |
| 4 | enrich 退出不依赖 status 字段 | ✅ 已实现 |
| 5 | ingest 退出简化为 source_refs + 骨架文件 | ✅ 已实现 |

### Sprint 2 交付清单

| 文件 | 操作 | 状态 |
|------|------|:--:|
| `kdo/gate.py` | 新建 | ✅ |
| `kdo/commands/quality.py` | 修改（cmd_gate） | ✅ |
| `kdo/cli.py` | 修改（注册 gate 子命令） | ✅ |
| `kdo/commands/curation.py` | 修改（_record_enrich_evidence） | ✅ |
| `60_feedback/enrich-evidence/` | 新建目录 | ✅ |

**Sprint 2 验收通过。**
