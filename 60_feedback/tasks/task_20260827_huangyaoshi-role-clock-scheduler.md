---
id: 553
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-26T21:59:46.050402+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- kdo-tools/role_clock.py
- kdo-tools/kdo-role-clock.cmd
- kdo-tools/tests/test_role_clock.py
- 90_control/notification-coverage-matrix.md
- 90_control/infrastructure-inventory.md
- 90_control/todos/laowantong.md
---

# #553 role_clock 角色心跳调度器 + schtasks 挂载（#525 四拆之二）

- **任务号**：#553
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P1（依赖 #552 注册表先行）
- **立项**：2026-08-27 王语嫣（#525 设计稿 §2/§3，老朱拍板实施）

## 任务

1. **调度器**：`kdo-tools/role_clock.py`——每角色唤醒节奏可配置（注册表 `wake_cron` 字段）；调度循环：查注册表→到点/有信号→路由唤醒到 active 实例通道→写心跳日志
2. **schtasks 挂载**：系统级 5 分钟节拍（设计稿定案——这是「系统级时钟」的落点，不绑任何 CLI 会话）
3. **唤醒语义统一层**（设计稿 §3）：统一 payload=「【叫醒】<role>：读 todos/<role>.md 未读段 + 看板名下状态（有任务按队列序施工；无任务报告待命）」；传输适配器薄壳：feishu webhook / cli todos 落盘 / hermes profile 消息
4. **红线自检**（设计稿 §8）：只做唤醒路由无裁决权；活性判定失败→降级报警不自动切执行权；误发>漏发（不对称偏误拦）；心跳/唤醒/降级全留日志
5. 与 conveyor_probe 分工不变：探针看信号、调度器催人，两单例不合并

## 边界

- 唤醒语义不含业务判断（「该干什么」判读在角色侧）
- 不引入新平台依赖（现有 Windows+Python 栈）

## 验收

- 调度循环+三适配器+降级路径回归；**活体验收=老顽童角色时钟真实唤醒一次**（收件箱出现【叫醒】payload 且消费记录可查）；§3.19 矩阵登记；欧阳锋终审


## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：角色心跳调度器落地（#525 四拆之二，设计稿 §2/§3/§8）。①**调度器** `kdo-tools/role_clock.py`：`run` 单拍——读注册表 → 到点（pace：老顽童/黄药师 15min、王语嫣 30min、风清扬 720min，可用注册表 wake_pace_min 覆盖）或事件驱动（欧阳锋=有待终审即醒，10min 防抖）→ 唤醒 → state 记 last_wake（幂等不重发）；②**schtasks 系统级挂载**：`kdo-role-clock` 每 5 分钟跑 `kdo-role-clock.cmd`（已注册，首拍 06:02 实跑）；③**唤醒语义统一层**：payload 统一文案「【叫醒】<role>：读 todos + 看板名下状态…」，适配器薄壳——todos/<role>.md 恒落盘 + active 实例含 feishu 通道时复用 conveyor_probe 加签 webhook；④**红线自检**：活性全死 → 照常唤醒（误发>漏发）+ 走 role_registry 全死自报（不自动切执行权）；唤醒日志写 `.kdo/role-clock.log` **不进胶囊事件层**（机器心跳会把 #550 on_duty 撑成常在岗——判定失效，显式规避）；⑤§3.19：矩阵事件 20 行。

**交付物**：
- `kdo-tools/role_clock.py` + `kdo-tools/kdo-role-clock.cmd`（调度器+包装）
- `kdo-tools/tests/test_role_clock.py`（5 例回归）
- `90_control/notification-coverage-matrix.md`（事件 20 行）+ `90_control/infrastructure-inventory.md`（登记）
- `90_control/todos/laowantong.md`（活体验收的【叫醒】行——消费证据）

**验证**：
- L1 单测 5 例全过：pace 到点/期内不触发/欧阳锋事件驱动+防抖+无信号不触发/唤醒 todos+日志双留痕/整拍循环幂等/全死照常唤醒+降级报警；基线：kdo-tools **194 passed**、90_control **182 passed** 零退步
- L2 狗粮：`run --dry-run` 真注册表三角色到点判定正确；**活体验收达成**：`wake laowantong` 真实落盘——todos/laowantong.md 出现【叫醒】payload + role-clock.log 消费记录可查（任务书验收条原文满足）
- L3 待活体：schtasks 06:02 起每 5 分钟自跑；老顽童 hermes 实例心跳登记后 feishu 适配器自动生效（当前 registry 无 laowantong 实例 → todos 单通道，如实）
- **预审红项预标注**：预审若检「不/无」类词=红线口径描述（如「不切执行权」「不误报」），预标注在此

**边界**：唤醒语义零业务判断 ✅；无新平台依赖 ✅；与 conveyor_probe 分工不变（探针看信号/调度器催人）✅；唤醒不写胶囊事件层（#550 联动防自欺，主动声明）✅。

**需要谁动作**：欧阳锋终审本单；各角色时钟迁系统级后的会话 cron 退役属 #555（四拆之四）范围。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 6 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点
