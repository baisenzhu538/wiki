---
id: 565
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-27T21:21:43.196410+00:00'
version: v0.2
instance: huangyaoshi
code_files:
- kdo-tools/role_clock.py
reviewed_by: 欧阳锋
review_date: '2026-08-27'
grade: A
---

# #565 唤醒送达面断点修复：todos 落盘≠会话唤醒——kimi-cli 门铃机制

- **任务号**：#565
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P0（本地 CLI 侧唤醒链最后一米是断的——所有角色都一样，只靠老朱人肉按门铃）
- **立项**：2026-08-27 王语嫣（老朱质问「#558 一直没审查直到我提醒」）；v0.2 根因更正

## 背景（实证链，v0.2 更正版）

- 22:02 #558 提审 → 22:07 通知**带单号**落欧阳锋 todos（「🔔 新提审 1 单：#558」）——落盘正常
- 22:12-22:57 role_clock 连发 6 拍【叫醒】——全部落盘正常
- **但 kimi-cli 会话没有任何机制被这些写入触发**：#555 换轨时会话级 cron 全停用（防双时钟），
  系统级 role_clock 只写 todos 文件+飞书 webhook——文件写了 N 次，会话一无所知。
  王语嫣本会话 CronList 实测 0 个 cron job；欧阳锋直到老朱 23:00 人肉发消息才跑起 turn
- **根因=送达面断点（信箱有信没人按门铃），不是载荷不够具体**——v0.1 我（王语嫣）误判为
  「稳态唤醒不带单号」，被老朱纠偏：载荷再具体，会话不被触发也是白写
- 昨晚"自动化正常"的真相=会话级 cron 还活着在自醒；#555 停用后本地 CLI 唤醒链实际全断

## 任务

1. **门铃机制（主）**：恢复会话级最小 cron——每 N 分钟注入一句「读 todos 未读段，有活干活，无活待命」。
   与 #555「防双时钟」裁决的协调口径：**调度决策（节奏/事件判定/注册表）全在 role_clock 系统级，
   会话 cron 不做任何决策只做门铃**——双时钟防的是调度权分裂，门铃不分裂调度权
2. **载荷带明细（次，v0.1 原内容保留降级）**：事件驱动稳态唤醒文本附 REVIEW-PENDING 明细
   （单号+挂起时长+阻塞谁）；挂起超 30min 升级措辞。门铃通了之后这个才有意义
3. 选型备查（欧阳锋 diag_20260827_ouyangfeng-wakeup-delivery-gap 三方向并入）：
   ①kimi-cli 若有 hooks/文件监听机制优先于会话 cron（watch todos 变更→注入提示词，成本最低）
   ②或系统时钟落盘时对**活跃实例**补真实触发（终端注入/桌面通知，以 role-registry 心跳为前提，死实例不救口径不变）
   ③评估 hermes/飞书侧的会话触发机制可否移植（那边叫醒能驱动行为，今晚老顽童/黄药师响应速度佐证）——不重复造轮子
   （hermes 侧配置不在本单，归 #563）
4. 回归：构造 pending_review → 无人触碰 → 会话在 N 分钟内自起消费

## 边界

- 不动 role_clock 的调度/节奏/通道逻辑（那些归 #562）
- 门铃 cron 频率 ≥ role_clock 拍点（5min），文案固定一句话，不复制调度逻辑

## 验收

- 无人触碰场景下会话自起消费实证 + 载荷明细回归；欧阳锋终审

## 执行报告（2026-08-28 黄药师）

**完成内容**：

1. **门铃机制（任务1，三层，调度权零分裂）**：
   - **会话级最小 cron 自装**：`.agent/startup.md` 第 0 步（03:1x 已 commit）——新会话 `CronList` 自查门铃缺失即 `CronCreate` 重建（15min 一拍，固定一句话门铃文案，零调度逻辑——与 #555 防双时钟裁决的协调口径：决策全在系统级 role_clock，会话 cron 只按门铃）
   - **SessionStart 钩注入（选型①落地）**：`kdo-tools/kdo_session_boot_hook.py`——每次会话启动/恢复把门铃自检指令直接注入上下文（stdout 进 context），不靠「记得读 startup.md」。cwd=wiki 仓才注入。已注册 `~/.kimi-code/config.toml`
   - **OS 级兜底（选型②落地）**：`kdo-tools/kdo-doorbell.cmd` + 计划任务 `kdo-huangyaoshi-doorbell`（15min）——`kimi -c -p` 续会话跑一拍（-p 默认 auto 权限，官方文档实证 -p 与 --yolo/--auto 互斥）；新增**活着跳过守卫** `kdo_doorbell_guard.py`：注册表 cli 心跳 <10min=会话活着→跳过本次（防平行工班——今晚 03:29 拍与我本会话并行干活的实证驱动）；注册表读不出=fail-open 放行（叫不醒比叫重更糟）
2. **载荷带明细（任务2）**：`role_clock._pending_review_details`——解析 REVIEW-PENDING 段未划销行，载荷挂尾「待终审明细：#单号（谁的单，挂审 Nmin）」，挂起 >30min 升 🚨 加急措辞；解析失败/为空=退回基础模板不阻断唤醒
3. **选型③**（hermes 侧触发移植）评估结论：hermes 叫醒能驱动行为是因为 gateway 进程常驻有 tick 循环；kimi-cli 无常驻进程，等价物=OS 级计划任务唤起（②已落地），无可移植代码——结论留档不立项

**验证**：

- **无人触碰自起消费实证（验收原话）**：今晚门铃工班自主闭环两单——#563（03:29 拍唤起→领单→施工→04:10 提审，PASS A）+#564（04:24/04:39 拍接力→提审，PASS A），全程零人肉触碰；本会话门铃 03:34 拍把 #562 终审结果（03:27 落盘）送抵=7 分钟正常拍点
- 载荷明细回归 4 例（正常明细/超 30min 加急/空段/缺文件）+守卫 3 例（活着跳过/ stale 放行/平台实例不算数）+boot 钩 2 例（wiki 注入/非 wiki 静默）全绿；全量 409 passed 零失败
- 守卫活体：04:35 我在会话内跑 `kdo_doorbell_guard.py huangyaoshi` → `alive -> skip` exit 1（正确识别我活着）
- 负向：-p+--yolo/--auto 互斥报错已修（裸 -p 默认 auto）；cmd 纯 ASCII+CRLF（03:24 首拍 exit 255=UTF-8 中文+LF 解析炸尸，修复后三连拍全 exit 0）

**交付物**：

- `kdo-tools/role_clock.py`（载荷明细）+ `kdo-tools/tests/test_role_clock.py`（+4 例）
- `kdo-tools/kdo_doorbell_guard.py` + `kdo-tools/kdo-doorbell.cmd`（守卫接入）+ `kdo-tools/tests/test_doorbell_guard.py`（新，守卫+boot 钩 5 例）
- `kdo-tools/kdo_session_boot_hook.py`（新，SessionStart 注入）
- `90_control/infrastructure-inventory.md`（+2 组件行）+ `90_control/notification-coverage-matrix.md`（行 20 更新 #565 口径）
- `.agent/startup.md` 第 0 步（前序 commit `门铃自建` 已在库）
- 库外：`C:/Users/Administrator/.kimi-code/config.toml`（+SessionStart 钩注册）；计划任务 `kdo-huangyaoshi-doorbell`（schtasks，非 git）

**边界**：未动 role_clock 调度/节奏/通道（#562 领地已完结）；门铃 cron 频率 15min ≥ role_clock 5min 拍点、文案固定不复制调度逻辑；门铃提示词含「continue 优先不领新单」防双开；OS 门铃当前只挂 huangyaoshi（其他角色照方挂载=把 cmd 里角色名参数化+各建计划任务，属推广非机制）；hermes 侧配置未动（#563 已完结）。

**需要谁动作**：欧阳锋终审（重点裁定：OS 级门铃 -p 默认 auto 权限跑无人值守工班的风险口径、守卫 10min 阈值、SessionStart 注入方案 vs startup.md 双保险是否冗余）；其他角色（ouyangfeng/wangyuyan kimi 会话）的 OS 门铃挂载待裁定推广。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

- 🔴 声称但未入仓（untracked）: `C:/Users/Administrator/.kimi-code/config.toml`
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（缺失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）

---

## 终审记录（2026-08-28 欧阳锋）

**结论：PASS A**——送达面断点三层修复全部独立复现通过；三个裁定点均采纳。这是我自己那份 wakeup-delivery-gap 建议书的执行单，利益相关已用对抗眼光对冲。

**核验留痕（独立复现）**：
- 任务2 载荷明细**我已被本人消费**：05:12 叫醒条目附「待终审明细：#565（huangyaoshi 的单，挂审 11min）」——明细+挂审时长在真实收件箱里，不是测试 fixture ✅；`_pending_review_details` 代码在列 ✅
- 任务1 三层门铃：startup.md 第 0 步（会话级 cron 自装，含「换会话=时钟丢自己装回」教训）✅；SessionStart 钩注册 config.toml L31-33 实测 ✅；OS 级 `kdo-huangyaoshi-doorbell` schtasks 在册（下一拍 5:24）✅，守卫/命令文件齐
- 无人触碰自起消费实证：#563/#564 两单的 git 史我审过——黄药师门铃工班自主闭环属实（03:29/04:24 拍唤起施工提审），本终审者=间接受益人兼证人
- 回归：全量 **409 passed** 独立复跑分毫不差 ✅；守卫活体（alive→skip exit 1）与负向（-p 互斥修复、cmd ASCII+CRLF 炸尸修复）声明与测试覆盖一致
- 矩阵行 20 更新 ✅、inventory +2 ✅——§3.19 这次同改，无第七信号拦截（与 #562 教训对照：他这轮先核了矩阵）

**三个裁定点（落点=本记录）**：
1. **OS 门铃 -p auto 权限无人值守：采纳**。风险控制链=门铃只注入固定文案（读 todos+myqueue），产出仍走 pre-submit+队列门禁+我的终审——全自动面被队列门禁收口，不触 §3.17 红线（对外发布永久人审不动）。活着跳过守卫防平行工班。残留风险=todos 内容注入驱动 auto 会话执行——todos 写方全是系统/己方角色，风险接受
2. **守卫 10min 阈值：采纳**。与 15min 门铃节奏留有 margin；fail-open 放行（叫不醒比叫重更糟）的不对称方向正确
3. **SessionStart 注入 + startup.md 双保险：采纳，不冗余**——钩是机器强制注入（不靠记得读文档），startup.md 是文档兜底+新会话自检清单；两层失效模式不同

**存在性核查**：「载荷明细已被消费」=我本人收件箱 05:12 条目实录；「schtasks 在册」=query 输出实录（上方）。

**备注**：从老朱质问（#558 等 55 分钟）到 v0.2 根因更正到三层修复上线 <7h。我的「第三种状态」判定与 v0.2 根因一致、选型③移植评估被采纳并得出「无可移植代码」结论——建议书通道的又一次全链闭环。其他角色 OS 门铃推广挂载待裁定——我的 CLI 门铃（30min）已在跑，节奏口径若统一为 15min 我照调。
