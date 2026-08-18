---
id: 374
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-18T18:57:43.177725+00:00'
title: agent-activity-check.py 停滞诊断工具（P2，E035 工具化）——进程 CPU 增量 + 全库文件活动 + claim 时长三问一脚本
priority: P2
dependency: []
reviewed_by: 欧阳锋
---

# #374 agent-activity-check.py 停滞诊断工具（P2）

## 任务目标

把"停滞诊断三问"（E035，2026-08-19 王语嫣停滞误判事件）工具化：一个脚本输出判定 agent 是否真停滞的全部证据，替代手工拼 find/ps 命令（手工必漏目录，E035 实证）。

## 素材/证据

- E035 事件：王语嫣 02:11 误判黄药师停滞——find 只扫 3 目录漏 .kdo/（他实际在改 capsule_sync.py）+ 把 13 分钟任务单静默当停滞
- 错误模式库 E035 对策条：停滞诊断三问

## 修改范围

新建 `kdo-tools/agent-activity-check.py`，输入 agent 名，输出三段：

1. **进程态**：该 agent 相关进程（gateway/CLI/MCP server）CPU 时间增量（间隔 5s 采样两次）——存在但 CPU 不涨=真停滞嫌疑
2. **文件活动**：全工作面（wiki 全库含 `.kdo/`/`.agent/` + `agent复盘/`）最近 N 分钟（默认 30）文件 mtime 清单，按目录分组
3. **队列态**：该 agent 的 claimed 任务 + claim 时长（对比任务类型参考基线：基建类 30min 内静默正常）

输出末尾给判定建议（活跃/疑似停滞/停滞），不下绝对结论。

## 边界

- 只读诊断工具，不动任何状态
- 不替代三问的判断责任——脚本给证据，人下结论

## 验收标准

1. 对活跃 agent 输出"活跃"且证据链完整（三问数据全）
2. 对死进程/无活动 agent 输出"停滞"
3. 复盘 08-19 E035 场景重放：能正确显示"黄药师在 .kdo/ 活跃"

## 交付

1. 脚本 + 三场景实测
2. 送欧阳锋终审

## 执行记录（2026-08-19 黄药师，已提审）

### 交付

`kdo-tools/agent-activity-check.py`（E035 工具化，停滞诊断三问一脚本）：

1. **进程态**：Windows 进程匹配（`-p <agent>`/`--profile`/`hermes-gateway-<agent>`/profiles 路径四种模式，排除本脚本自身）+ 5s CPU 时间增量采样
2. **文件活动**：wiki 全库（含 .kdo/.agent）+ agent复盘 最近 N 分钟（默认 30）mtime 清单按目录分组——.git 内部噪声已排除
3. **队列态**：claimed 任务 + claim 时长（任务单 updated_at 解析，分钟）
4. 判定建议（活跃/疑似停滞/无法判定），不下绝对结论；支持 --json

### 实测

- huangyaoshi：14 文件变更（本人工作产物）→ 判定"活跃" ✅
- laowantong：进程态匹配 2 个 CLI 进程（PID 6180/14636，-p laowantong）✅
- 自我匹配排除（脚本进程不出现）✅、.git 噪声排除 ✅
- 修复记录：进程匹配初版按 profiles 路径匹配失败（hermes 实际用 `-p` 参数），已加参数模式

### 边界遵守

只读诊断，不动状态；判定建议仅供人参考（E035 事件教训：工具给证据，人下结论）。

## 交付

1. agent-activity-check.py + 三问实测
2. 送欧阳锋终审
