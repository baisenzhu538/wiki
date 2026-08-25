---
id: 519
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-25T03:42:01.094421+00:00'
version: v0.1
instance: huangyaoshi
---

# #519 conveyor_probe 计划任务态空转：运行但 state 不落盘（疑似 GBK 控制台 emoji 崩溃）

- **任务号**：#519
- **状态**：queued
- **assignee**：huangyaoshi（探针运行环境修复+失败可见；欧阳锋终审）
- **优先级**：P1（通知链静默断流实证——#498 终审 01:12 无任何收件箱收到，编排者凭通知缺失误报任务状态）
- **立项**：2026-08-25 王语嫣（自办诊断：老朱追问「#498 早审过了你为什么说在审」触发）

## 背景（实测证据链，非转述）

- 2026-08-25 00:43 后，探针 state（`.kdo/conveyor_state.json` `last_run_ts`）停在 00:43:24，**44 分钟未更新**；
- 但计划任务 `kdo-conveyor-probe` 正常执行（schtasks 实测：上次运行 1:21:36，下次 1:31:36）——**任务在跑，状态不落盘**=空转；
- 漏过的信号：#498 终审（01:12 commit eef134aa9）、#514-#518 五个新 queued 行、1 条新登记——全部未通知未登记；
- 手动实跑（Git Bash，01:27）正常：exit=0、state 落盘、增量补扫全部找回——**代码逻辑没问题，问题在计划任务运行环境**；
- 疑似元凶：Task Scheduler 默认 GBK 控制台，探针输出的 emoji（🔕⚠️）/中文在 GBK 下 `UnicodeEncodeError` → 崩在 state 保存（源码 L652）之前；手动环境 UTF-8 所以正常。（待黄药师证实或证伪，不断言）
- 同族病：#501 的「故障窗口补偿提示」在崩溃路径下无效——提示在跑成功的运行里打印，崩溃的运行打不出来（循环依赖）。

## 任务

1. 定位空转根因（GBK emoji 崩溃假设优先验证：任务环境跑 `python -c "print('🔕')"` 复现）
2. 修复二选一或组合：①计划任务环境补 `PYTHONIOENCODING=utf-8`/`PYTHONUTF8=1`（nssm/hermes 同款先例）②探针输出层加编码兜底（errors=replace）
3. **失败可见**：探针崩溃必须落 stderr 日志文件（`90_control/` 或 .kdo/ 下），且连续 N 次空转（state 年龄 >2×周期）由健康检查报警——不能依赖「下一次成功的运行」来报告「之前的运行崩了」
4. 回归：计划任务跑一次真实周期后 state `last_run_ts` 更新、通知落盘

## 验证（验证分层）

- L1：任务环境复现崩溃→修复后同环境跑通
- L2 狗粮：schtasks 触发一次实跑，state 落盘 + 通知入收件箱
- L3 待活体：下一次真实终审/建议书事件，通知 10 分钟内到达（不再靠老朱转达）

## 边界

- 只修运行环境/输出编码/失败可见，不动探针扫描逻辑与通知内容
- 不扩大范围到其他计划任务（如发现同族（kdo-l1-capture 等 6 个任务）同病，登记另立单，不在本单顺手改）

## 关联

- #501（角色收件箱+故障窗口补偿——补偿机制的崩溃盲区本单根治）
- charter §3.16 A8（凡机制必写读对账）/ §3.17 红线 5（熔断自动化：静默失效不会自曝）
- 触发事件：#498 终审通知丢失 → 王语嫣误报「#498 在审」（W9/E051 回源核验纪律违例的间接诱因）

## 需要谁动作

- **黄药师**：环境修复 + 失败可见
- **欧阳锋**：终审本单

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：根因定位 + 环境修复 + 失败可见三件套。①根因（GBK emoji 假设**证伪**——`conveyor_probe.py:29-30` stdout 早有 utf-8/errors=replace 兜底）：真凶=schtasks TR 的 cmd /c 嵌套引号 `cmd /c ""...python.exe" "script" >> log 2>&1"` 被 cmd 剥壳 → `'C:\Program' 不是内部或外部命令` → 静默零日志零 state（08-24 20:58 TR 变更后即失效，期间 00:43/01:27 两次 state 落盘均为手动跑）；叠加第二病灶：任务假运行实例卡死（模式=正在运行）→ 新触发被拒 `0x800710E0`（net helpmsg 4320=操作员或管理员拒绝），/end 终止后解除。②修复：新建 `kdo-tools/kdo-conveyor-probe.cmd` 包装（同族先例 kdo-l1-capture.cmd：cd /d+重定向+errorlevel→pending-git-commits.log，纯 ASCII），schtasks /create /f 重建任务 TR 直指 .cmd（每 10 分钟周期不变）；输出编码兜底既有（reconfigure）无需改。③失败可见三层：每轮必打摘要行进 `logs/conveyor-probe.log`（探针既有，通路修复后恢复留痕）；非零退出 → `90_control/pending-git-commits.log`（#434 口径，.cmd errorlevel 分支）；新增 `90_control/scripts/check-conveyor-state.py`——state 年龄 >2×周期（20min）→ exit 1，挂入 health-check 每日 02:07（不依赖「下一次成功运行」报告「之前崩了」，#501 补偿盲区闭环）。

**交付物**：
- `kdo-tools/kdo-conveyor-probe.cmd`（新：计划任务包装，根治嵌套引号失败类）
- `90_control/scripts/check-conveyor-state.py`（新：空转报警）+ `90_control/scripts/tests/test_check_conveyor_state.py`（5 例回归）
- `90_control/scripts/health-check.py`（checks 列表挂新检查项）
- 计划任务 kdo-conveyor-probe 重建（TR→.cmd；假运行实例已 /end 终止）
- `90_control/infrastructure-inventory.md`（conveyor_probe/check-conveyor-state/kdo-conveyor-probe 三行更新）

**验证**：
- L1：复现——原 TR 字符串实跑复现 `'C:\Program' 不是内部或外部命令` exit=1（零日志产出）；修复后计划任务实跑 `上次结果=0`
- L2 狗粮：schtasks 计划触发 11:37:00 实跑——state `last_run_ts`=11:37:00 ✅、`logs/conveyor-probe.log` 新增摘要行+near-miss 检出 ✅、通知落盘（11:18 手动验证跑已补发 huangyaoshi/wangyuyan todos 含 #517 reviewed）✅；`check-conveyor-state.py` 直跑「正常（2.3 分钟前落盘）」exit 0 ✅
- 回归：90_control/scripts 全量 **121 passed**（116 基线+新增 5，零退步）
- L3 待活体：下次真实终审/建议书事件 10 分钟内通知到达

**边界**：探针扫描逻辑/通知内容零改动 ✅；其他计划任务未顺手改 ✅——**同族登记**：kdo-l1-capture 今晨 09:37 起每轮被 Ctrl+C 杀死（上次结果 0xC000013A，log 尾 `^C^C`，l1-size.log 停更于 09:07；kdo-inbox-watch 直连 python TR 同期结果=0 正常），疑似环境级 console 杀手（09:07→09:37 窗口出现），超本单边界，建议王语嫣另立单排查；安慰语/通知文案未动。

**需要谁动作**：欧阳锋终审本单；王语嫣——①知悉通知链已恢复（11:18 起积压信号已补落 todos）；②l1-capture 今晨被杀新病灶建议立项排查（证据见上）；各角色知悉——探针通知链已复活，待办收件箱恢复更新。
