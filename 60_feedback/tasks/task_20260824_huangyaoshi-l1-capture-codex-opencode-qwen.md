---
id: 489
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-23T18:03:11.995096+00:00'
version: v0.1
instance: huangyaoshi
---

# #489 L1 采集面补全（Codex / opencode / qwen 四会话源）

- **任务号**：#489
- **状态**：queued
- **assignee**：huangyaoshi（改脚本；王语嫣编排；欧阳锋终审；风清扬审计验收）
- **优先级**：P1（F-048 拍板落地——codex 定性=工厂共用工具，采集面补全）
- **立项**：2026-08-24 王语嫣（老朱 2026-08-24 直达拍板 F-048 → P1-①；原拍板 2026-08-23 23:16 记录于 `diag_20260823_fengqingyang-l1-periodic-audit.md` §拍板记录）

## 背景

F-048 拍板生效：codex 定性=**工厂角色工具**（纳 KDO 治理，非老朱个人工具）。L1 全量上下文采集面当前漏三个新会话源（`l1_capture.py` SOURCE_DIRS 仍只有 claude / kimi / hermes，无 codex / opencode / qwen）——codex 工具一旦开跑，其全量上下文断在 L1 外，风清扬审计侧无法覆盖。

风清扬第二期审计（`diag_20260824_fengqingyang-l1-audit-round2.md`）实测：`codex-homes` 7 角色目录 sessions 全空、共享 `.codex\history.jsonl` 仍在写（当前角色会话落在 L1 采集面之外）。

## 任务

`l1_capture.py` 增补四个会话源（SOURCE_DIRS）：

| # | 会话源 | 具体路径 |
|:--|:--|:--|
| 1 | Codex 主目录 | `.codex` 的 `history.jsonl` / `state_*.sqlite` / `logs_*.sqlite` |
| 2 | codex-homes 角色隔离目录 | `D:\KDO-memory\codex-homes\<角色拼音>\sessions`（未来主力） |
| 3 | opencode | `.config\opencode` |
| 4 | qwen | `.qwen` |

## 验证（验证分层）

- L1 单测：`l1_capture.py` 采集面配置增补后 pytest/自检通过
- L2 狗粮：改后实际采集一次，确认 codex/opencode/qwen 源有文件进入 L1 全量库
- L3 待活体：风清扬审计侧实测「codex 会话可被 L1 采集」（#490 切换试点后闭环验证）

## 边界

- **只改 `l1_capture.py` 采集面（SOURCE_DIRS 增补），不动 L1 采集其他逻辑**（调度/体积红线/镜像 #463/#464/#471 不动）
- 风清扬只审计不实施（脚本改动归黄药师）
- **先补后切**：本单只补采集面，不切 codex-homes——切换是 #490（依赖本单完成，杜绝「切了就断留痕」）
- 采集面增补不触发体积红线风险加速（见 round2 §3 体积线性增长，另裁定）

## 关联

- F-048（老朱 2026-08-24 拍板：codex 定性 + P1 两项）
- `diag_20260823_fengqingyang-l1-periodic-audit.md` §拍板记录（P1-① 原文）
- `diag_20260824_fengqingyang-l1-audit-round2.md`（采集面缺口实测 + 拍板转述悬空）
- `diag_20260823_fengqingyang-codex-instance-isolation.md`（CODEX_HOME 分家建议）
- #463（L1 全量采集基建）/ #471（常驻调度）/ #490（codex-homes 切换试点，依赖本单）

## 需要谁动作

- **黄药师**：`l1_capture.py` 采集面增补四会话源 + 实测
- **王语嫣**：编排（本单）+ 验收后启动 #490 切换试点
- **欧阳锋**：终审本单
- **风清扬**：审计侧验收采集面覆盖（不实施）

## 执行报告（F-034 五字段，complete 前必填）

（黄药师填写）
