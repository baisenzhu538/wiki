# kdo-seed bootstrap 开机手册（#532）

> 新机器五步起一座同构 KDO 工厂。**机制不走样由 seed-check.py 脚本保证，不靠人肉核对。**
> 本手册经王语嫣过可执行性；schtasks 注册命令照抄即可（#519 教训：一律 .cmd 包装，TR 不写嵌套引号）。

## 五步

### 1. 放种子
把 `seed/` 内容拷到目标目录（如 `D:\kdo-new\`）——九层空骨架+角色文件+制度层+工具层一次到位。

### 2. 设 KDO_ROOT
```
setx KDO_ROOT "D:\kdo-new"
```
（新开终端生效；临时窗口用 `set KDO_ROOT=...`）

### 3. 跑 seed-check
```
python kdo-tools\seed-check.py --skip-tasks
```
全过=目录/关键件/角色文件/脚本可编译齐活。**不过不往下走。**

### 4. 注册计划任务（照抄模板，逐条执行）
```
schtasks /create /tn "kdo-conveyor-probe" /tr "%KDO_ROOT%\kdo-tools\kdo-conveyor-probe.cmd" /sc minute /mo 10 /f
schtasks /create /tn "kdo-inbox-watch" /tr "\"C:\Program Files\Python312\python.exe\" %KDO_ROOT%\kdo-tools\watch_inbox.py" /sc minute /mo 10 /f
schtasks /create /tn "kdo-l1-capture" /tr "%KDO_ROOT%\kdo-tools\kdo-l1-capture.cmd" /sc minute /mo 30 /f
schtasks /create /tn "kdo-l1-archive" /tr "%KDO_ROOT%\kdo-tools\run-l1-archive.cmd" /sc daily /st 06:00 /f
schtasks /create /tn "kdo-quality-metrics" /tr "%KDO_ROOT%\kdo-tools\kdo-quality-metrics.cmd" /sc weekly /d MON /st 06:35 /f
```
注意：①python.exe 路径按新机实际调整；②.env 类凭证（飞书 webhook key 等）另行配置，种子不含密钥。

### 5. 五角色启动五连读验证
每个角色开首次会话，启动 SOP 四读（`.agent/startup.md` → 角色 context → `.agent/context.md` → `.agent/pitfalls.md`）+ 读 `90_control/todos/<role>.md` 收件箱。五角色各留下一条「我已上线」记录=装机完成。

## 复检验收

```
python kdo-tools\seed-check.py
```
（带 schtasks 核查的完整版；五项计划任务全注册+探针首轮回执后应全过）

## 不搬清单（C 层，新库从 #001 重新长）

30_wiki 卡片 / 70_product 队列行 / 60_feedback 历史 / agent复盘档案 / .kdo 状态文件——一律不搬。

## 故障排查

| 症状 | 先看 |
|:--|:--|
| 计划任务静默不跑 | TR 必须直指 .cmd（嵌套引号 cmd /c 会被剥壳，#519 事故） |
| 脚本找不到库 | KDO_ROOT 未设或拼错；脚本缺省回退=自身上两级目录 |
| 探针跑了没通知 | 90_control/gate-blocked.log + logs/conveyor-probe.log 双查 |
