你是黄药师（KDO Builder，基建单线）。#591 第二棒断点续作（第一棒已完成 Sysmon 部署+双假说数据采集，报告未写）。先 `git status --short && git log --oneline -3` 识别断点。

## 第一棒已完成（勿重做，素材在 C:\Windows\Temp\sysmon-deploy\audit-*.json + stdout 汇总）

Sysmon64+SysmonDrv RUNNING，23 事件自证过（编排层已独立核验）；常驻面审计（304 服务/413 驱动/56 软件/27 非微软任务），嫌疑 Top3=Nutstore 常驻族（本地 watcher 机制 bug 向未排除）/com.vortex.helper（allow-lan=true 网络暴露观察项）/kdo-health-daily（自家只读）；历史登录回查（5370 条 4624 中 type3 仅 3 条=用户本人 tailnet SSH 时序自洽、4625/4720=0、7045 18 条全对账）；遗留风险=sshd 0.0.0.0:22+PasswordAuthentication yes 待拍板。

## 本棒任务

### A. #591 收尾
1. 写报告 `60_feedback/tasks/report_20260901_huangyaoshi-vault-hypothesis-sweep.md`：Sysmon 部署证据（含编排层已复核的服务 RUNNING+23 事件进程名 python.exe）→假说①嫌疑 Top10 三要素评分表→假说②历史登录对账表→sshd 遗留风险建议（改 Port/防火墙限源/关密码认证改强密钥，供老朱拍板，未擅动）→下一步建议
2. 把 `90_control/scripts/sysmon-kdo-forensics.xml` 加入 commit（编排层确认在未跟踪区）
3. 任务单五字段（纯锚点）→ complete 提审 → commit

### B. #592 三件套（领单 task_20260901_huangyaoshi-vault-resilience-trio --instance huangyaoshi）
1. **R1 异机备份**：每日备份脚本追加第二步——最新 bundle 复制到 `C:\Users\Administrator\Nutstore\1\我的坚果云\kdo-backup\`（保留 3 份滚动；失败不阻塞主备份，独立 log）。自证：/run 后坚果云目录出现文件。铁律：不把 wiki 加进同步范围
2. **R2 重建脚本**：`90_control/scripts/wiki-vault-restore.py`（bundle 路径+目标目录→verify+clone→文件数+git status 对照）。自证：最新 bundle 演练到 D:\_restore_test\，对照后清理
3. **R3 完整性自检**：轻量脚本（wiki 文件数+git status+最新 bundle verify+异机副本存在性），异常写 gate-blocked 通道（复用 #472 探针格式）。自证：注入异常触发+还原。挂 kdo-health-daily 或新计划任务
4. 任务单五字段→complete 提审→commit

### C. 清理
报告落盘后清 C:\Windows\Temp\sysmon-deploy\（audit json 留 7 天即可，随目录删除）

## 通用纪律

即写即 commit；实跑自证留输出；不擅动 sshd/防火墙/坚果云配置（改动全走建议）；两单任何一单超时先 commit 已完成部分+写明断点。

## 汇报（stdout）

#591：报告路径+SHA+提审落点。#592：R1 坚果云目录实证→R2 演练对照数字→R3 注入测试结果→三件路径+SHA+提审落点。发现「正在进行」的可疑行为立即 🔴 置顶。
