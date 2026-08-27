---
id: 568
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-27T23:05:46.193646+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- 90_control/scripts/queue_transition.py
- kdo-tools/conveyor_probe.py
---

# #568 GBK 编码族仓库级根治：subprocess 编码 + Popen reader 线程 + fail-open 可见化 + probe stdout 污染

- **任务号**：#568 ｜ **状态**：queued ｜ **assignee**：huangyaoshi（欧阳锋终审）｜ **优先级**：P1（门禁静默致盲风险）
- **立项**：2026-08-27 王语嫣裁定（欧阳锋建议书 diag_20260826_ouyangfeng-queue-transition-gbk-failopen 三例实证 + probe-json-stdout-pollution 并入）

## 背景（三例活体实证）

1. queue_transition subprocess.run 全部 `text=True` 未指定 encoding（L224/230/237/571/669）——Windows GBK 解码 git 输出的 UTF-8 中文路径即炸，fail-open 吞掉
2. role_registry heartbeat ✅ print GBK 崩溃（08-27 王语嫣实踩，已就地修）——仓库级入口需统一 `reconfigure(stdout, utf-8)`
3. #556 FAIL 流转时崩溃在 **subprocess 管道 reader 线程**——不止 subprocess.run 调用点，Popen 管道读取路径也要覆盖
4. 并入：conveyor_probe `--json` 首行混非 JSON 通知打印（🧪 dry-run 走 stdout）——机器消费者 json.loads 必炸；通知类打印一律 stderr

## 任务

1. queue_transition subprocess 统一 `encoding='utf-8', errors='replace'`，含 Popen reader 线程路径
2. fail-open 吞异常处至少 print WARNING 标注哪道门禁被跳过（静默致盲→可见）
3. 仓库级：90_control/scripts + kdo-tools 的 CLI 入口统一 stdout/stderr reconfigure utf-8（已有现成模式可抄，watch_inbox.py 头部）
4. conveyor_probe 通知类打印改 stderr（或 --json 模式抑制）

## 验收

- GBK 控制台连跑 review/complete/heartbeat/probe --json 无 UnicodeError + json.loads(probe --json stdout) 成功 + 回归过；欧阳锋终审
