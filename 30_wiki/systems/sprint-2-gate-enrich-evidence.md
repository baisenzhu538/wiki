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
