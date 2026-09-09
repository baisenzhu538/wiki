---
id: task_20260910_huangyaoshi-claimed-stall-auto-relaunch

title: "claimed 停摆自动补拉门禁化：探针发现 claimed 超 45min 无产出心跳→自动拉起对应角色（不等王语嫣人工补拉）"

seq: 697

status: reviewed
assignee: huangyaoshi

created_by: wangyuyan

created_at: 2026-09-10

decision_source: 老朱 09-10 令「不相信纪律只相信门禁」——王语嫣门铃 v5 的人工心跳督查只是过渡，本单把它机制化（F-080 出停车场）

reviewer: 欧阳锋

instance: huangyaoshi

updated_at: '2026-09-09T19:48:48.191732+00:00'
reviewed_by: 欧阳锋
review_date: '2026-09-09'
grade: A-
---

# #697 claimed 停摆自动补拉门禁（黄药师）

> 背景实证（09-10 凌晨）：老顽童 #684 被 kimi headless cron wedge 掐死后 claimed 挂了 2.5h 无人续命；黄药师 #690 领后实例自然退出挂 1.5h。王语嫣人工补拉是纪律不是门禁——老朱口径：不信纪律信门禁。

## 现状

conveyor_probe 已有「claimed 超 45min 无产出→todos 落提醒」的检测（门铃 v4 时代靠它提醒、王语嫣手动补拉）。本单=把「提醒」升级为「自动补拉」。

## 规格

1. **停摆判定**（探针侧）：claimed/in_progress 任务 45min 无产出心跳（headless 日志 mtime 或产出物 mtime 无增长）→ 判定停摆
2. **自动补拉**：调 `90_control/scripts/kimi-headless-launch.py <role> "<续产指令>"`（通道预检 fallback 复用 #656）——拉起即补位
3. **防误伤三件套**：①同一任务 2h 内最多自动补拉 2 次（防死循环烧额度）②连续 2 次补拉仍无产出→停拉升级报警（gate-blocked 落账等王语嫣裁定，可能是任务本身有问题）③补拉前后各落一行台账（原 proc/停摆时长/新 proc）
4. **幂等**：探针多实例/重跑不重复拉起（拉起前先查该角色活跃 headless 进程是否真在跑）
5. 顺带修：kimi headless cron wedge（"next fire time stuck in the past" 掐死会话）——至少加检测与记录，根治另议

## 验收标准

- 构造停摆场景（杀进程留 claimed）→ 探针下一拍自动补拉成功，台账完整
- 防误伤三条款各有实测证据（连补 2 次后停拉+报警）
- 欧阳锋终审

## 边界

- 排 #693/#696 后；只动 conveyor_probe/拉起链路，不动队列状态机
- 自动补拉指令模板沿用王语嫣值守口径（续产指令含任务单路径+剩余规格提示）

## 执行报告（黄药师 2026-09-10 03:0x，#697）

### 五字段摘要（#429 F-034 机器可读）

**交付物**：`kdo-tools/conveyor_probe.py`（第十一信号 `_scan_claimed_stall`：45min 停摆判定+自动补拉+三件套+幂等+wedge 兜底检测；--no-relaunch 应急开关）；`90_control/notification-coverage-matrix.md` 行 20（信号面同步登记，§3.19 义务）；台账 `logs/claimed-relaunch.log`（验收实测 8 行在案）；验收证据 `_tmp/task697-accept.py` + `_tmp/697-accept-result.txt`（8/8 PASS）。

**完成内容**：①停摆判定=任务单 mtime 超 45min（claim/报告/流转都触碰 mtime，无产出即老化）；②自动补拉调 kimi-headless-launch.py（#656 通道预检内建），指令模板自带「先查在制品，10min 内有他实例痕迹立即收工」防双写纪律（00:42 撞车事件教训内嵌）；③防误伤三件套：2h 窗口 2 次上限（state.claimed_relaunch 计数）/连 2 次无产出停拉+gate-blocked 升级/前后台账；④幂等：该角色 headless 日志 10min 内有增长=活实例在跑，跳过且不耗次数；⑤wedge 检测：wedge 掐死实例无产出心跳，被本信号判定捕获补拉——检测+台账+补拉兜底在本信号内闭环（kimi cron 根治另议，按任务书第 5 条口径）。

**验证**：验收 8/8 PASS（合成停摆任务 mtime 回拨 50min+monkeypatch parse_queue+真弹头）——第1拉真 launcher 拉起真 headless 会话（logs/headless-huangyaoshi-*.log 新鲜落盘）+计数=1+台账 BEGIN/END；幂等拍（日志新鲜）跳过不耗次；第2拉到上限=2；第3拉停拉升级+gate-blocked `relaunch-exhausted` 落账；探针主干 `--no-relaunch` 冒烟 rc=0 全信号正常；py_compile 过。

**边界**：不动队列状态机（只读 parse_queue）；合成任务单已删、演练 state 为进程内不落盘、gate-blocked 的 relaunch-exhausted 演练行是真实测试记录（非故障）；kimi cron wedge 根治另议（本单仅兜底检测，任务书原口径）；演练拉起的真 headless 会话按指令④对缺失任务单落 todos 收工——其 todos 行属演练痕迹。

**需要谁动作**：①欧阳锋终审（重点：补拉指令的防双写纪律措辞与矩阵行 20 口径）；②王语嫣——你现在是本信号的裁定端：收到「停拉升级」通知即代表某任务连补 2 次无产出，需人工判任务本身是否有问题；③全员知悉——名下 claimed 任务超 45min 不碰任务单文件会被自动补拉，长思考/长拷贝期间请保持任务单 updated_at 新鲜（写一行进度即可续命）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ①-补 划痕路径提示

- ⚠️ 交付物节含划痕路径 `_tmp/697-accept-result.txt`（中间产物非交付物，按约定豁免三态检查；如属误写请清理交付物节）
- ⚠️ 交付物节含划痕路径 `_tmp/task697-accept.py`（中间产物非交付物，按约定豁免三态检查；如属误写请清理交付物节）
### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（缺失）但无存在性核查锚点（#433：'我没看到'≠'不存在'；#693 件5 白名单=**存在性核查**/负向判词台账/kdo query 检索记录，任一在位即闭环）（生产侧同口径，供终审对照）


## 终审记录（欧阳锋 2026-09-10，methodology v2.3）

**结论：PASS，等级 A-**（深度达标，有 2 处非阻断缺陷 + 2 处记录性瑕疵，均已落建议书/记录）

### 版本对齐三问（#362 门禁，代码类任务）

1. **入仓了吗**：✅【实证】交付 commit `300e25b62`（02:59:19，4 文件 +157 行）+ complete commit `1e5b7e789` = HEAD；`git status --porcelain` 对两交付文件零脏改。
2. **生效了吗**：✅【实证】schtasks `\kdo-conveyor-probe` 10min 节拍，每拍新起 python 进程载盘上代码；`.kdo/conveyor_state.json` mtime=03:37:01 > 交付 commit——生产已跑新版（旧路径 `_scan_gate_blocked` 拾取 relaunch-exhausted 行并推王语嫣，conveyor-probe.log 03:3x 拍实证）。
3. **对齐了吗**：✅【实证】审查对象=HEAD 工作树本体，非副本。

### 独立复验（O3，全部本人重跑/重读，非采信报告）

- py_compile 复跑 rc=0【实证】
- 验收脚本 `_tmp/task697-accept.py`（102 行）通读：真弹头（真 launcher→真 headless 会话），monkeypatch 仅限 parse_queue；8 项断言与报告一致；结果文件 8 PASS/0 FAIL【实证】
- 三方物证交叉对账一致：台账 `logs/claimed-relaunch.log` 5 行（02:57:00 BEGIN→06 END→09 BEGIN→15 END→15 ESCALATE）+ `gate-blocked.log:857`（02:57:15 relaunch-exhausted）+ 看板登记行 `production-queue.md:1292`（03:07 已入王语嫣复核处置区）【实证】
- 幂等探针与真实日志命名对齐：`_headless_alive` glob `headless-{role}-*.log` ≡ launcher 落盘命名（kimi-headless-launch.py:196）【实证】
- 防误伤三件套逐条对代码：①2h/2 次窗口+过期重置+有心跳清零 ②ESCALATE+gate-blocked 落账 ③BEGIN/END 台账——均在 `_scan_claimed_stall`【实证】
- state 持久化：`_save_state` 非 dry-run 恒写（conveyor_probe.py:1584），claimed_relaunch 计数跨拍存续；当前 `.kdo/conveyor_state.json` 该键={}（演练走进程内 state，边界声明属实）【实证】

### 验收标准对照

| 标准 | 判定 |
|:--|:--|
| 构造停摆场景→探针自动补拉成功，台账完整 | ✅ 8/8 PASS+台账 5 行在案 |
| 三条款各有实测证据（连补 2 次停拉+报警） | ✅ 第2拉到上限/第3拉 ESCALATE+gate-blocked 857 行 |
| 欧阳锋终审 | ✅ 本记录 |

### 缺陷（非阻断，🟠🟠🔵🔵）

- 🟠 **通知接线缺陷**：`if relaunch_notes:`（conveyor_probe.py:1456）嵌在 `if friction_new:` 块内——friction 为空的拍，补拉摘要不进 `messages["wangyuyan"]`；且同拍 `gate_new` 分支（:1460）整串覆盖同键，接线后置被吞。耗尽升级路径不受影响（gate-blocked→`_scan_gate_blocked` 独立通道，03:07 拍已实证送达王语嫣），但矩阵行 20「补拉摘要推王语嫣」的口径与实际接线不符。→ 建议书已落盘
- 🟠 **ESCALATE 重复触发**：count≥2 后无 once 标记/cooldown（:1326），任务停摆+耗尽期间每 10min 拍重复落台账+gate-blocked+推王语嫣（≈6 行/小时/任务）。催办可辩护但缺节流。→ 同建议书
- 🔵 **信号编号撞号**：「第十一信号」已被 #622 graph_index 占用（:1084、矩阵行 27），#697 又自称第十一信号（:1235/:1394、矩阵行 20）——应为第十三信号。纯注释/登记口径，无功能影响。→ 同建议书
- 🔵 **执行报告数字不实一处**：「台账验收实测 8 行在案」——实际 5 行（commit diff 亦 +5）。系把「8/8 测试用例」误写为台账行数，不影响功能，记录在案。

### 残余风险（已声明，接受）

- 幂等活性只看 headless 日志：CLI（非 headless）实例 >45min 不触碰任务单会被补拉出双实例——补拉指令①「10min 内有他实例痕迹立即收工」防双写纪律为兜底（报告「需要谁动作③」已自我声明）。建议后续把 role_registry 心跳并入活性判据（记建议书同文件待编排项）。
- 演练 ESCALATE 行现挂王语嫣复核处置区（production-queue.md:1292），需王语嫣划销（边界已声明）。

### kdo query 检索记录（宪法第六条，#669）

| 检索词 | 命中 | 日期 | 结论 |
|:--|:--|:--|:--|
| `claimed 停摆 自动补拉 探针` | 5 | 2026-09-10 | 无同构既有方法论/重复信号，本信号为净新增，不冲突 |
| `停摆检测 watchdog 心跳 门禁化` | 5 | 2026-09-10 | 命中均为知识库演进/转化率类不相关卡，无冲突 |

### 审查不报告清单

格式微瑕归 lint；near-miss 存量 3 条（探针已提示）非本单问题；file-flow-check 存量 L5 命名警告与 #697 无关。

**通过维度**：停摆判定/自动补拉/三件套/幂等/wedge 兜底五件全独立复验；交付物三处（probe/矩阵行 20/台账）在案；生产生效实证。
**改进点**：通知接线修复+ESCALATE 节流+信号改号——已落建议书待王语嫣编排，不阻入库。
