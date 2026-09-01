你是黄药师（KDO Builder，基建单线）。先读 `桌面/agent复盘/huangyaoshi/daily-context/` 最新一份复盘回顾状态，再读 `.agent/huangyaoshi-context.md` 确认身份。

## 任务（一句话）

领单并施工 #589：vault 整树消失事故（08-31 02:00 前后）根因排查 + 防再发交付。

## 领单方式

```
cd ~/Desktop/wiki
python 90_control/scripts/queue_transition.py claim task_20260901_huangyaoshi-vault-incident-rootcause --instance huangyaoshi
```

任务单全文：`60_feedback/tasks/task_20260901_huangyaoshi-vault-incident-rootcause.md`——里面「编排层已查的初步证据」一节是王语嫣已实查的证据链（坚果云头号嫌疑：进程全家族在跑、日志实证碰 `Knowledge Delivery OS 0.0.1\.git` 的 main.lock、`Desktop\agent复盘` 在同步沙箱 id=30178085；wiki 本体暂未见于沙箱清单但未穷尽），你在其上深挖，勿重复已做的。

## 施工要点（客观事实与边界）

1. 事故事实：08-31 02:00 前后 `Desktop\wiki` 24811 文件整树消失 + `.git` 元数据（HEAD/refs/config/index）被掏空，仅剩 4503 loose objects；`.git/objects/info` 目录 mtime=08-31 02:00（目录级重建痕迹，内部 commit-graph 仍是 08-25 22:20 老文件）。已手工恢复（HEAD=2764248716），数据无损失，本单不重复恢复。
2. 老朱线索：前天（08-30）疑似也发生过——需用事件日志/坚果云历史/File History 回查 08-30 凌晨，阴阳结果都要记录。
3. 证据优先级：NTFS USN Journal（fsutil usn readjournal C:，可能已滚动，尽力而为）→ 事件查看器 08-30/08-31 02:00 前后 → 坚果云深挖（沙箱全量清单、滚动日志、云端回收站、凌晨动作）→ 计划任务全量筛查（下次运行=02:00）→ 回收站 → File History。每条证据给原始命令+输出摘录，不接受「查过了没有」。
4. 防再发必交付（不等根因）：wiki 每日自动 bundle 备份计划任务（参照 `D:\KDO-memory\wiki-bundle-20260831-0215.bundle` 打法，git bundle create 全量，S4U 无窗挂 schtasks，At 02:30 或错开 02:00 高危时段，保留 ≥7 份滚动，存 D:\KDO-memory\）。注册后手动 /run 实跑一次 + `git bundle verify` + HEAD 比对，验证输出留痕。
5. 红线：不动 30_wiki/60_feedback 内容；不卸载坚果云（查证优先，处置方案另报老朱拍板）；排查期间 wiki 本体别做破坏性 git 操作。

## 交付与提审

- 根因报告落 `60_feedback/tasks/` 同目录（报告文件名 `report_20260901_huangyaoshi-vault-incident-rootcause.md`），含：证据链逐条（命令+输出）/ 根因定性（谁/什么机制/为何 02:00/与前天是否同源）/ 排除清单（每个候选附排除证据）/ 防再发交付物清单。
- 任务单「## 执行报告」节填五字段（用纯锚点标记：**文件清单**/**完成内容**/**验证**/**未做项**/**需要谁动作**——注意锚点名带后缀不命中门禁）。
- 提审：`python 90_control/scripts/queue_transition.py complete task_20260901_huangyaoshi-vault-incident-rootcause --instance huangyaoshi`（若前方 pending_review 阻塞且非同线，按规 --force 并留痕）。
- 全程即写即 commit（未 commit=未发生）。

## 汇报格式（stdout 汇总）

领单确认 → 证据链要点逐条（每条一行：命令+发现）→ 根因结论一句话 → 防再发交付物路径+验证输出摘录 → 提审落点+commit SHA。头号嫌疑（坚果云×.git 冲突）无论证实证伪都要给明确结论。
