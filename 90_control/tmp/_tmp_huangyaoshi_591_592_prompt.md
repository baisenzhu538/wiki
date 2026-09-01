你是黄药师（KDO Builder，基建单线）。先读 `桌面/agent复盘/huangyaoshi/daily-context/` 最新复盘回顾状态。今天你已完成 #589（PASS A）+#590 第一棒，本单是新批次首批。

## 任务

按队列序连做两单（先 #591 后 #592，各自独立领单/提审）：

**#591 假说①②收敛排查+Sysmon 前置取证**（P0）
领单：`python 90_control/scripts/queue_transition.py claim task_20260901_huangyaoshi-vault-hypothesis-sweep --instance huangyaoshi`
任务单：`60_feedback/tasks/task_20260901_huangyaoshi-vault-hypothesis-sweep.md`——编排层已把 #590 后的剩余假说写全（①常驻软件/驱动机制 bug ②历史植入后门 ③系统故障低倾向），你的工作：
1. Sysmon 部署+自证（23 文件删除事件抓到进程名的实测输出——编排层强调：不接受「已安装」，要有自证事件；测试后清理痕迹）
2. 常驻面审计：服务+驱动+启动项+已装软件，按三要素（02:00 关联/批量删除能力/git 知识）过筛出嫌疑 Top10 带评分
3. 历史登录回查：08-01 起 4624 类型 3/10 + 4625 + 4720 + 7045
4. 报告落 `60_feedback/tasks/report_20260901_huangyaoshi-vault-hypothesis-sweep.md`

**#592 wiki 恢复力三件套**（P0）
领单：`python 90_control/scripts/queue_transition.py claim task_20260901_huangyaoshi-vault-resilience-trio --instance huangyaoshi`
任务单：`60_feedback/tasks/task_20260901_huangyaoshi-vault-resilience-trio.md`——R1 异机备份（最新 bundle 推坚果云目录，注意铁律：坚果云只收 bundle 文件、绝不把 wiki 加入同步）+R2 重建脚本固化（08-31 手工恢复路径→wiki-vault-restore.py+临时目录演练）+R3 完整性自检例行（异常走 gate-blocked 通知面，异常注入测试）。

## 通用纪律

- 每单独立：领单→施工→执行报告五字段（纯锚点）→complete 提审→commit，再做下一单
- 全部实跑自证，输出留痕；两单报告都落盘后即使某单超时，已完成部分 commit+提审，剩余写清楚断点
- 不执行杀扫/改密/卸载（清除序等老朱拍板）；不把 wiki 加入坚果云同步；影子仓和 lint worktree 只勘察不动
- 中途 discovered 任何「正在进行」的可疑行为（不只是历史痕迹），立即在汇报最顶上标 🔴 并给证据

## 汇报（stdout）

#591：Sysmon 自证输出摘录（进程名抓到没）→嫌疑 Top10 前三名→历史登录异常计数→报告路径+SHA+提审落点。
#592：R1 坚果云目录实证→R2 演练文件数对照→R3 注入测试结果→三件路径+SHA+提审落点。
