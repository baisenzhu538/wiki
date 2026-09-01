你是黄药师（KDO Builder，基建单线）。这是 #589 的第二棒续作（同一单，你第一棒实例已收工）。先做断点识别：`git status --short && git log --oneline -3`，读任务单 `60_feedback/tasks/task_20260901_huangyaoshi-vault-incident-rootcause.md` 全文+`C:\Windows\TEMP\usn_full.txt` 只抽查不动（1.15GB），从断点继续，已完成勿重做。

## 第一棒已完成（勿重做）

USN 考古（02:00-02:01 两阶段删除：先 .git 元数据后工作树顶层，单秒 264 项精确保留 objects）、计划任务全量排除（223 个 0 命中）、事件日志（0 事件）、08-30 凌晨零事件（双阴）、根因初判（高度疑似同步盘机制，差铁证）。

## 本棒三件事（按序）

1. **坚果云深挖三件套（铁证收口）**：
   a. 沙箱全量清单：`C:\Users\Administrator\AppData\Roaming\Nutstore\config\NsConfig.json` + `db1/` 全目录（确认 wiki 是否曾在/在同步范围）
   b. 滚动历史日志：`AppData\Roaming\Nutstore\logs\` 下 Nutstore.Client.Wpf.1-9.log（每个 5MB 滚动档）grep 08-31 01:30-02:15 窗口的 wiki/Desktop 删除与 UpstreamDeleteProcessor 记录——第一棒只看了当前档
   c. 本地能查的云端删除记录（本地 db/缓存里的服务端事件镜像）；若需登录云端回收站而无凭据，如实标注「待老朱提供坚果云账号登录查云端回收站」，给老朱留一行操作指引
2. **防再发必交付（不等根因）**：wiki 每日 bundle 备份计划任务——schtasks 注册（S4U 无窗，禁 Interactive，每日 02:30 错开高危时段），命令 `git -C C:\Users\Administrator\Desktop\wiki bundle create D:\KDO-memory\wiki-bundle-<date>.bundle --all`（包一层 .bat 放 90_control/scripts/），保留 ≥7 份滚动（脚本里做清理），注册后 `schtasks /run` 实跑+`git bundle verify`+HEAD 比对，输出留痕
3. **收尾闭环**：根因报告落 `60_feedback/tasks/report_20260901_huangyaoshi-vault-incident-rootcause.md`（两棒证据链合并：命令+输出逐条/根因定性/排除清单/防再发交付物/铁证差什么）；任务单「## 执行报告」填五字段（纯锚点：**文件清单**/**完成内容**/**验证**/**未做项**/**需要谁动作**）；`queue_transition.py complete` 提审（同 assignee 续作无阻塞则不用 force）；全程即写即 commit

## 债务登记（报告里带一节即可，不开新单）

第一棒发现：Desktop 6 个 `.kdo_lint_baseline_*` 残留工作树（git worktree 元数据已删实体还在）+ wiki 内嵌套 `wiki/` 影子仓——已在编排层留档待老朱拍板，报告里汇总路径清单即可，不执行清理。

## 红线（继承第一棒）

不动 30_wiki/60_feedback 内容；不卸载/不改坚果云配置（查证优先）；USN dump 留 C:\Windows\TEMP 不删（编排层后续归档）。

## 汇报格式（stdout）

铁证结论（拿到/没拿到+差什么）→ bundle 计划任务名+实跑验证输出摘录 → 报告路径+commit SHA → 提审落点。
