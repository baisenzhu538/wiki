你是欧阳锋（KDO 终审门控）。今天事故防线两单终审，一次会话做完。

## 单 1：#591 假说①②收敛排查+Sysmon 前置取证（pending_review）
- 任务单：`60_feedback/tasks/task_20260901_huangyaoshi-vault-hypothesis-sweep.md`
- 报告：`60_feedback/tasks/report_20260901_huangyaoshi-vault-hypothesis-sweep.md`
- 核验要点：①Sysmon 部署证据（编排层已亲验 Sysmon64/SysmonDrv RUNNING+23 事件进程名实抓，你复跑确认即可）②嫌疑 Top10 三要素评分是否凭证据（头名 Nutstore 本地 watcher 族——注意与 #589「服务端排除」的口径区分：排除的是服务端事件面，本地引擎 bug 向未排除，这个区分是否成立）③假说②历史登录对账（5370 条 4624/type3 仅 3 条 tailnet SSH 自洽/7045 全对账）④sshd 遗留风险（0.0.0.0:22+密码认证）建议是否充分且未擅动

## 单 2：#592 wiki 恢复力三件套（pending_review，编排层代收尾——R3 挂载+五字段是编排层补的，报告口径与施工者 stdout 一致）
- 任务单：`60_feedback/tasks/task_20260901_huangyaoshi-vault-resilience-trio.md`
- 交付物：`90_control/scripts/wiki-bundle-offsite-2nd.bat` / `wiki-vault-restore.py` / `vault-integrity-check.py` / `kdo-tools/run-kdo-health.cmd`（挂载行）
- 核验要点：①R1 坚果云目录字节等大实证+nutstore.db WAL 只读读法无锁风险②R2 演练 24,896 文件 dirty=0、bundle-older 判定正确③R3 注入测试双报警进 gate-blocked+编排层挂载后实跑三查 OK exit 0④铁律遵守：wiki 本体未加入同步、nutstore.db 只读未碰原库

## 流转

每单独立：终审记录节→queue_transition review（verdict/grade 独立判断）→todos 留痕→commit。两单可给不同等级。

## 汇报（stdout）

#591 结论+等级 / #592 结论+等级 / 各自复跑发现 / 给老朱的清除序最终建议（杀扫/改密/sshd 收紧的先后） / commit SHA。
