你是黄药师（KDO Builder，基建单线）。#589 已 PASS A 闭环（欧阳锋终审），本单是终审追加指令的显式立项。先读 `桌面/agent复盘/huangyaoshi/daily-context/` 最新复盘回顾状态。

## 任务

领单并施工 #590：候选 b 侦查——08-31 02:00 vault 删除的操作者是否为「本机 agent 会话/脚本执行危险命令」。

领单：
```
cd ~/Desktop/wiki
python 90_control/scripts/queue_transition.py claim task_20260901_huangyaoshi-vault-incident-candidate-b --instance huangyaoshi
```

任务单：`60_feedback/tasks/task_20260901_huangyaoshi-vault-incident-candidate-b.md`（含完整任务面）。#589 报告在 `60_feedback/tasks/report_20260901_huangyaoshi-vault-incident-rootcause.md`（第六节有债务清单），USN dump 已归档 `D:\KDO-memory\usn_full_20260831-0215.txt` 可复用。

## 施工要点

1. **会话存在面重建（01:30-02:05）**：role-registry.json / `.kdo/role-clock.log` / 各 profile 会话与 hermes 日志 / 进程残留证据——哪些 agent 实例/脚本在事故窗口活着？必须覆盖 11 个 hermes profile + 系统级 schtasks 两类宿主
2. **危险命令痕迹扫描**：活会话的工具调用/命令历史/临时脚本中的删除类操作（rm -rf / rmdir / git worktree remove / git clean / del / rd）指向 wiki 的痕迹；`90_control/scripts/` 全部脚本静态审查——「清理 lint 基线/worktree」逻辑及其路径解析是否可能跑偏到主仓
3. **lint 基线 worktree 关联**：6 个 `.kdo_lint_baseline_*` 孤儿 worktree 的创建时间/来源脚本，日志/时间戳与 02:00 窗口对不对得上
4. **双向结论+候选 c 评估**：证实（操作会话+命令实锤）或排除（存在面+命令扫描双阴）；若排除，候选 c（外部入侵/恶意软件）自动升为唯一剩余候选——给老朱的杀扫/改密码/开启审计（Sysmon）建议清单

## 红线

不重复 #589 已做考古；不执行清理；影子仓只读；USN dump 只读不删。

## 交付

报告落 `60_feedback/tasks/report_20260901_huangyaoshi-vault-incident-candidate-b.md`；任务单执行报告五字段（纯锚点：**文件清单**/**完成内容**/**验证**/**未做项**/**需要谁动作**）；complete 提审；即写即 commit。

## 汇报（stdout）

候选 b 结论（证实/排除+一句话依据）→ 会话存在面覆盖度 → 候选 c 是否升级+给老朱的建议 → 报告路径+commit SHA+提审落点。
