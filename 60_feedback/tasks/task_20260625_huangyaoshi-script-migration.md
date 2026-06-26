---
id: task_20260625_huangyaoshi-script-migration
type: infrastructure_task
created_at: 2026-06-25
author: 王语嫣
assignee: 黄药师
priority: P2
scope: vault 根目录 Python 脚本整理与 kdo 工厂基础设施
---

# 黄药师基础设施任务：根目录脚本迁移与规范化

> 王语嫣铁律：本指令仅写入 `60_feedback/`，不污染 `30_wiki/`。黄药师负责按此指令在仓库基础设施层执行迁移与配置调整。

---

## 0. 元信息

| 项目 | 内容 |
|------|------|
| 任务类型 | 基础设施整理 |
| 来源 | vault 根目录堆积 15+ 个临时 Python 脚本，影响 glob/grep 扫描效率与 git 管理 |
| 优先级 | P2（不影响当前卡片生产，可在 kdo 工厂基础设施排期中处理） |
| 质量负责人 | 王语嫣（CLI） |
| 执行方 | 黄药师 |

---

## 1. 现状

vault 根目录目前散落以下脚本：

- `_check_dk_output.py`
- `_check_extractor_output.py`
- `_check_score_dist.py`
- `_debug_label_llm.py`
- `_review_laowantong.py`
- `_tmp_batch_fix.py`
- `_tmp_check_at.py`
- `_tmp_check_batch_a.py`
- `_tmp_fix_order.py`
- `_tmp_v15_debug.py`
- `_tmp_v15_fix.py`
- `_tmp_v15_fix2.py`
- `_verify_gold_standard.py`
- `_verify_sprint4.py`
- `.temp_v15_check.py`

其中部分脚本被 wiki 引用（如 `_verify_gold_standard.py` 出现在 `dk-f14-accuracy-measurement-mismatch.md` 等卡片中），不能简单删除或忽略。

---

## 2. 迁移目标

把根目录脚本统一归集到 `40_outputs/code/scripts/`，并按用途分层：

| 目标目录 | 用途 | 当前候选脚本 |
|:---|:---|:---|
| `40_outputs/code/scripts/` | 可复用的检查/验证/调试工具 | `_verify_gold_standard.py`、`_verify_sprint4.py`、`_review_laowantong.py`、`_check_*.py`、`_debug_label_llm.py`、`.temp_v15_check.py` |
| `40_outputs/code/scripts/archive/` | 已完成历史使命的一次性修复脚本 | `_tmp_batch_fix.py`、`_tmp_check_at.py`、`_tmp_check_batch_a.py`、`_tmp_fix_order.py`、`_tmp_v15_debug.py`、`_tmp_v15_fix.py`、`_tmp_v15_fix2.py` |

---

## 3. 迁移要求

### 3.1 路径修复

迁移后，所有脚本必须能正确解析 vault 根路径。建议统一使用基于脚本位置的定位：

```python
from pathlib import Path
VAULT = Path(__file__).resolve().parents[3]  # scripts/ -> code/ -> 40_outputs/ -> wiki/
```

原脚本中使用的相对路径如 `dir = pathlib.Path("30_wiki/concepts")` 需要改为：

```python
dir = VAULT / "30_wiki" / "concepts"
```

绝对 Windows 路径（如 `C:\Users\Administrator\Desktop\wiki`）可保留，但建议统一为相对定位，便于跨环境运行。

### 3.2 引用同步

`_verify_gold_standard.py` 在以下文件中被引用，迁移后需同步更新路径：

- `30_wiki/dark-knowledges/dk-f14-accuracy-measurement-mismatch.md`
- `.agent/pitfalls.md`
- `10_raw/sources/src_20260619_1545a6ee_.agent_pitfalls.md`
- `10_raw/sources/src_20260619_d967c8f5_90_control_failure_modes.md`

### 3.3 命名规范化

- `.temp_v15_check.py` 建议重命名为 `validate_v15.py`
- archive 目录中的脚本可保留原命名作为历史记录

### 3.4 git 与 .gitignore

- 迁移完成后，根目录不应再遗留 `.py` 脚本（除用户明确保留的）。
- 不需要把 `40_outputs/code/scripts/` 加入 `.gitignore`，这些脚本应继续被 git 跟踪备份。

---

## 4. 影响评估

| 影响 | 说明 |
|:---|:---|
| 正面 | 根目录整洁；glob/grep/kdo index 扫描范围缩小；脚本版本控制更清晰 |
| 风险 | 脚本运行时的当前工作目录变化，需统一改为基于脚本位置定位 vault root |
| 风险 | wiki 中对 `_verify_gold_standard.py` 的引用路径会变，需要同步更新 |

---

## 5. 验收标准

- [ ] 根目录下不再散放 `_*.py`、`_verify_*.py`、`_check_*.py`、`_debug_*.py`、`.temp_*.py`
- [ ] 可复用脚本全部位于 `40_outputs/code/scripts/`
- [ ] 一次性历史脚本全部位于 `40_outputs/code/scripts/archive/`
- [ ] 迁移后的脚本在 vault root 作为 cwd 时能正常运行
- [ ] `_verify_gold_standard.py` 的 wiki 引用已同步更新
- [ ] `git status` 能正确反映移动/重命名，无意外未跟踪文件
- [ ] `kdo lint` / `kdo validate` 未因脚本迁移报错

---

## 6. 提交方式

- 黄药师完成后，在当前会话或 `.agent/context.md` 中通知王语嫣复核。
- 王语嫣只抽查 3-5 个迁移后脚本的运行结果和引用更新情况。

---

*任务下达：王语嫣 | 日期：2026-06-25*
