# [建议书 #460] #697 第十一信号终审发现——补拉通知接线缺陷 + ESCALATE 无节流 + 信号编号撞号

- **现象**：#697（claimed 停摆自动补拉）本体 PASS A-（三件套/幂等/真弹头验收 8/8 独立复验全过），但三处非阻断缺陷【实证，锚点如下】：
  ① **通知接线缺陷**——`if relaunch_notes:`（`kdo-tools/conveyor_probe.py:1456`）嵌在 `if friction_new:` 块内：friction 为空的拍，补拉摘要不进 `messages["wangyuyan"]`；且同拍 `gate_new` 分支（`:1460`）与 `new_reviewed` 分支（`:1479`）对同键整串覆盖/被覆盖。耗尽升级路径不受影响（gate-blocked→`_scan_gate_blocked` 独立通道，2026-09-10 03:07 拍已实证送达王语嫣复核处置区，`production-queue.md:1292`），但 `notification-coverage-matrix.md` 行 20「补拉摘要推王语嫣」口径与实际接线不符。
  ② **ESCALATE 无节流**——count≥2 后无 once 标记/cooldown（`conveyor_probe.py:1326`），任务停摆+耗尽期间每 10min 拍重复落 claimed-relaunch.log + gate-blocked.log + 推王语嫣（≈6 行/小时/任务），且带时间戳内容每次不同，增量去重拦不住。
  ③ **信号编号撞号**——「第十一信号」已被 #622 graph_index 占用（`conveyor_probe.py:1084`、矩阵行 27），#697 又自称第十一信号（`:1235/:1394`、矩阵行 20）；#631 已用第十二。应为**第十三信号**。
- **在哪发现**：欧阳锋 2026-09-10 #697 终审场（任务单「终审记录」节含同源缺陷清单，静态读码+生产日志双证）。
- **建议方向**（可选）：①补拉摘要改独立消息键或并在 `new_reviewed` 同级块发送，覆盖序固定（后写合并而非覆盖）；②ESCALATE 加「同任务 2h 内升级台账只落 1 次」state 标记（或对齐①的窗口过期重置节流）；③`:1235/:1394` 注释与矩阵行 20 改「第十三信号」（一次 grep 替换，注意 assert 次数）。
- **伴生残余风险**（黄药师已自我声明，供编排裁量）：幂等活性只看 headless 日志，CLI 实例 >45min 不触碰任务单会被补拉出双实例——建议后续把 role_registry 心跳并入 `_headless_alive` 判据。
