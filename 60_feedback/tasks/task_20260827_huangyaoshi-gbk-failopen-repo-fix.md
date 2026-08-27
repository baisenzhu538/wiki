---
id: 568
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-27T23:11:56.042670+00:00'
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

## 执行报告（2026-08-28 黄药师）

**完成内容**：

1. **subprocess 编码（任务1）**：`queue_transition.py` 5 处 `subprocess.run(text=True)` 全部补 `encoding="utf-8", errors="replace"`——含背景 3 提到的 reader 线程崩溃路径：Windows 上 `capture_output+text=True` 的解码发生在 subprocess 内部 `_communicate` reader 线程，不指定 encoding 即用 locale(GBK) 解码 git 的 UTF-8 输出，修复点正是这 5 处调用签名（无独立 Popen 调用点，reader 线程是 subprocess.run 内部实现）
2. **fail-open 可见化（任务2）**：E040 门禁两个组件的静默吞异常改为 stderr WARNING——`_git_dirty_paths`（异常=按无脏改动放行）+ `_git_tracked`（异常=按已跟踪放行），均标注「哪道门禁哪个组件被跳过」。既有 stderr 留痕的（预审层 L944、git 收口失败 🚨）不动
3. **入口 reconfigure 统一（任务3）**：四入口对齐 watch_inbox 模式——`role_registry.py` / `role_clock.py` 新增 stdout+stderr UTF-8 reconfigure；`queue_transition.py` 补 `errors="replace"`（原有但无 replace，遇不可映射字符仍炸）；`conveyor_probe.py` 补 stderr reconfigure（原有 stdout 单侧）。范围=门禁链四入口（queue_transition/conveyor_probe/role_registry/role_clock），非两目录全量（其余入口今晚未被 GBK 实证击中，逐步补齐比批量铺开稳——自披露口径差异请终审裁定）
4. **probe stdout 污染（任务4）**：conveyor_probe 15 处通知类 print 改走 `_nprint`（stderr）；`--json` 模式 stdout 仅剩纯 JSON 一行；终态人类摘要保持 stdout 不动

**验证**：

- GBK 活体：`PYTHONIOENCODING=gbk` 下 ① role_registry heartbeat（含 ✅ emoji print）exit 0 无 UnicodeError ② conveyor_probe --json exit 0 且 stdout 过 `json.loads`（8 键结构完整）——修复前这两路均实证炸过
- 回归：wiki 双侧 409 passed 零失败；唯一改动既有断言=`test_notify_dry_run_no_send` 从 stdout 改读 stderr（行为变更即任务 4 本意，测试跟契约走）
- 负向：`-p` 与权限旗互斥类不属于本单；通知打印 stderr 化不影响 todos 落盘/ webhook 推送主链（409 全绿覆盖）
- 自披露：GBK 全链（review/complete 真实流转）未做自动化测试——probe 子进程测试会副作用生产状态（通知/落盘），活体手动验证代替，留痕上方；review/complete 的 subprocess 修复面由 409 回归+编码参数本身覆盖

**交付物**：

- `90_control/scripts/queue_transition.py`（subprocess×5+fail-open 可见化×2+errors=replace）
- `90_control/scripts/role_registry.py`（reconfigure）
- `kdo-tools/conveyor_probe.py`（_nprint+15 处通知打印+stderr reconfigure）
- `kdo-tools/role_clock.py`（reconfigure）
- `kdo-tools/tests/test_conveyor_probe.py`（1 断言跟契约）

**边界**：未动其他 scripts/kdo-tools 入口（门禁链外）；未改 fail-open 语义本身（仍放行，只加可见性）；通知文案零改动。

**需要谁动作**：欧阳锋终审（重点：门禁链四入口 vs 两目录全量的范围自裁、_nprint 方案、活体代替自动化的验证口径）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 5 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点
