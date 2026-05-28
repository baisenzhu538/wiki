---
title: "黄药师：Sprint 5 — Validate→Ship 闭环"
assigned_to: "黄药师 (Builder)"
priority: "P1"
created_at: "2026-05-28"
reviewer: "欧阳锋"
status: "completed"
depends_on: []
blocks: []
---

# 黄药师：Sprint 5 — Validate→Ship 闭环

## 背景

Sprint 4（数据卫生）✅ 已完成并通过审查。A 类断链 83→0、frontmatter 245→0、双格式 134→0。

**Sprint 5 的目标**：把 Validate→Ship 之间的缝隙焊死。当前：

- `kdo validate` 和 `kdo ship` 各自独立运行——ship 虽然调用了 validate 结果，但 validate 的故障信息没有自动反馈到改进流程
- Ship 的三道质量门检查粒度可提升（目前只拦最明显的缺失）
- Feedback 收集后的闭环（→自动生成改进项 → 验证修复 → 重新 ship）尚未建立

Sprint 5 不做大重构，而是在现有架构上"焊死"三个断点。

---

## 全局测量

| 指标 | Sprint 5 目标 | 测量方式 |
|:----|:-------------|:---------|
| Ship 拦截率 | 所有 validate failed 的 artifact 在 ship 时被 100% 拦截 | `kdo ship --skip-validation` vs 不带 skip 的对比 |
| 闭环延迟 | 从 feedback 录入到 improvement task 生成 ≤1 次 `kdo improve` 调用 | 人工测试 |
| 测试覆盖 | ship gate + feedback loop 的 pytest 覆盖率 ≥80% | `pytest --cov` |
| pytest | 不降级 | `pytest` 全量运行 |

---

## 执行顺序（严格，不跳步）

### S5-1：Ship Gate 硬化（~2h）

**目标**：ship 前的验证门禁从"建议性"升级为"审计性"——每次 ship 必须记录当时的 validate 快照。

**当前代码位置**：`commands/delivery.py:283-292`，`cmd_ship` 中的 validation gate。

**做法**：

1. **Ship 时自动嵌入 validate 报告快照**
   - 在 `cmd_ship` 中，当 `--skip-validation` 未设置时：运行 validate → 将 validate 结果（passed/failed/warning 计数 + 关键失败条目）嵌入 delivery record 的 `validation_snapshot` 字段
   - `50_delivery/published/<delivery_id>-<slug>.md` 的 frontmatter 新增 `validation_snapshot` 字段，内容格式：
     ```yaml
     validation_snapshot:
       passed: 12
       failed: 0
       warnings: 3
       v15_failed: 0
     ```
   - 不改变 ship 的退出行为（有 failed 仍然拒绝 ship），只是追加审计记录

2. **Ship delivery record 增设 `validation_report` 文件链接**
   - 每次 ship 时，如果 `kdo validate --write-report` 有输出，自动将 report 路径记入 delivery record
   - 这样每次 ship 都有可追溯的 validate 快照

3. **Ship 日志增强**
   - 当前 ship 只打印一句话。改为输出结构化摘要：
     ```
     kdo ship yt-pitch-storytelling --channel feishu
     → Validation: 20 passed, 0 failed, 3 warnings
     → Gate check: 3/3 passed
     → Delivery recorded: del_abc123 → 50_delivery/published/del_abc123-yt-pitch-storytelling-feishu.md
     ```

**验收**：
- 每次 `kdo ship`（不带 `--skip-validation`）后，delivery record 中必有 `validation_snapshot`
- 验证 failed 时 ship 拒绝，且快照记录包含失败条目
- pytest ship gate tests 覆盖硬化后的行为

---

### S5-2：Feedback→Improve 自动闭环（~2h）

**目标**：`kdo feedback` 录入 eval 结果后，能一键生成 improvement task。

**当前代码位置**：
- `commands/feedback.py`：`cmd_eval`（写入 eval 结果）、`cmd_feedback`（录入反馈）、`cmd_improve`（生成改进计划）
- `improvement.py`：`render_improvement_plan`、`apply_improvements`

**做法**：

1. **`kdo feedback --kind eval-results` 增强**
   - 当前 `cmd_eval` 写入 eval 结果到 `50_delivery/eval/`，但 eval 结果与 improvement 之间没有自动关联
   - 新增：eval 结果写入后，自动扫描 validate 报告，输出"建议改进项"到 stdout（不自动写入，只预览）
   - 命令行为：
     ```
     kdo feedback --kind eval-results --title "Batch 1 Review" --source "欧阳锋" <<< "PASS with notes"
     → Eval recorded at 50_delivery/eval/eval_xxx.md
     → Suggested improvements (3): [1] yt-pitch-storytelling: attacker argument too brief  [2] ...
     → Run `kdo improve --from-eval eval_xxx` to generate improvement plan
     ```

2. **`kdo improve --from-eval <eval_id>`**
   - 当前 `cmd_improve` 从 `feedback.yaml` 读数据生成改进计划
   - 新增 `--from-eval` 参数：读取指定 eval 文件，生成对应的 improvement task 文件到 `70_product/tasks/`
   - output 格式：`70_product/tasks/improve-<slug>-<timestamp>.md`
   - 不自动 apply，只生成 task 文件（让欧阳锋审查后再执行）

3. **Validate failed → 建议 feedback 录入**
   - 当 `kdo validate` 检测到 Failed 项时，在末尾追加一行：
     ```
     → 建议：`kdo feedback --kind eval-results --title "Validate Failed: <card_id>" --source "kdo validate"`
     ```
   - 降低"知道有错但不记录"的心理摩擦

**验收**：
- `kdo feedback --kind eval-results` 输出含建议改进项
- `kdo improve --from-eval eval_xxx` 生成 task 文件到 `70_product/tasks/`
- `kdo validate` 有 Failed 时输出 feedback 建议
- pytest 覆盖闭环流程

---

### S5-3：Ship Gate 测试套件（~1h）

**目标**：为 S5-1 和 S5-2 的新行为补测试，确保不破坏现有逻辑。

**当前测试文件**：
- `tests/test_validate.py`
- `tests/test_validate_deep.py`
- `tests/test_validate_v15.py`

**新增测试文件**：

```
tests/test_ship_gate.py    — Ship 硬化行为测试
tests/test_feedback_loop.py — Feedback→Improve 闭环测试
```

**测试覆盖场景**：

| # | 场景 | 所在文件 |
|:-:|:-----|:---------|
| 1 | `kdo ship` 正常流程：validate pass → ship 成功 | `test_ship_gate.py` |
| 2 | `kdo ship` validate fail → ship 拒绝 + snapshot 含失败条目 | `test_ship_gate.py` |
| 3 | `kdo ship --skip-validation` → 跳过 gate + snapshot 含 skip 标记 | `test_ship_gate.py` |
| 4 | `kdo ship` re-ship duplicate detection | `test_ship_gate.py` |
| 5 | `kdo feedback --kind eval-results` → 输出建议改进项 | `test_feedback_loop.py` |
| 6 | `kdo improve --from-eval` → 生成 task 文件 | `test_feedback_loop.py` |
| 7 | `kdo validate` 有 Failed → 输出 feedback 建议行 | `test_feedback_loop.py` |

**验收**：
- 7 个测试场景全部 PASS
- `pytest` 全量运行不降级（当前 354/354 passing）

---

## 总体验收

| # | 验收项 | 判定方式 |
|:-:|:------|:--------|
| 1 | S5-1：每次 ship 记录含 validation_snapshot | 查看 delivery record |
| 2 | S5-1：validate fail 时 ship 拒绝 | pytest test_ship_gate.py |
| 3 | S5-2：eval 录入后输出建议改进项 | pytest test_feedback_loop.py |
| 4 | S5-2：`kdo improve --from-eval` 生成 task 文件 | pytest + 文件存在检查 |
| 5 | S5-2：validate fail 时输出 feedback 建议 | pytest test_feedback_loop.py |
| 6 | S5-3：7 个测试场景全部 PASS | pytest tests/test_ship_gate.py tests/test_feedback_loop.py |
| 7 | `pytest` 全量不降级 | 354/354 passing（不含 flaky dashboard 网络测试） |

## 不做

- **不做** 重构 quality.py（1415 行不动，只在 delivery.py/feedback.py 增量改）
- **不做** 新增渠道适配器（飞书/企微/webhook 等放到 Sprint 6）
- **不做** CLI 输出颜色/格式化美化
- **不做** `kdo ship` 的自动多渠道发布
- **不做** Graph RAG 的 feedback integration

---

## 测量脚本

执行验收时运行：

```bash
# S5-1 验证
kdo validate --v15 --card <some-card>  # 制造一个通过场景
kdo ship <card> --channel test         # 验证通过后 ship 成功
# 检查 delivery record 有 validation_snapshot

# S5-2 验证
kdo feedback --kind eval-results --title "Test" --source "test" <<< "OK"
kdo improve --from-eval eval_xxx     # 验证生成 task 文件

# S5-3 验证
pytest tests/test_ship_gate.py tests/test_feedback_loop.py -v
pytest  # 全量不降级
```

---

*欧阳锋 · 2026-05-28*
