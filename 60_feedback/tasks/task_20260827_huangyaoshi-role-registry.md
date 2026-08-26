---
id: 552
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-26T21:41:19.117153+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- 90_control/scripts/role_registry.py
- 90_control/role-registry.json
- 90_control/scripts/tests/test_role_registry.py
- 90_control/scripts/queue_transition.py
- kdo-tools/on_duty.py
- kdo-tools/tests/test_on_duty.py
- 90_control/infrastructure-inventory.md
reviewed_by: 欧阳锋
review_date: '2026-08-26'
grade: A
---

# #552 角色活性注册表 + 心跳写钩（#525 四拆之一）

- **任务号**：#552
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P1（老朱 08-27 拍板 #525 四拆落地；角色时钟系统化的地基单）
- **立项**：2026-08-27 王语嫣（#525 设计稿终审 PASS A 后拍板实施，设计稿=`90_control/role-clock-architecture.md`）

## 任务

1. **注册表落地**：`90_control/role-registry.json`——结构按设计稿 §1（角色→instances[]→tool/kind/heartbeat_ts/channels + active 指针）；从轻 JSON 单文件，不落数据库
2. **心跳写钩**：CLI 会话启动写一次 + 会话内时钟每拍蹭写（单行 JSON 更新，单角色单活跃实例写自己键，无锁竞争）
3. **活性判定函数**：heartbeat 年龄 >2×该角色节奏=疑似死亡（复用 #519 state 年龄口径）；全死→gate-blocked.log 机器自报（复用 #471 通道，不新造报警器）
4. **多实例并存口径**：同角色双活→唤醒双发（消费幂等各自去重）；active 仅用于单执行者防双写

## 边界

- 本单只建注册表+心跳写钩，调度器在 #553；不改 conveyor_probe
- 严格按设计稿 §1 施工，不扩设计（设计变更走新建议书）

## 协同备注

- #550（取消夜间静默）实施时若本单已交付：**在岗判定优先读注册表心跳**，事件库/L1 扫描降为兜底——两单联动口径以此为准

## 验收

- 注册表 schema 与设计稿 §1 逐条对照；心跳写入/活性判定/降级自报三用例回归；欧阳锋终审


## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：角色活性注册表+心跳写钩（#525 四拆之一，严格按设计稿 §1 施工）。①**注册表** `90_control/role-registry.json`（轻 JSON 单文件，原子替换写入）：schema=角色→instances[]（tool/kind/session_scope/profile/heartbeat_ts/channels）+active 指针，与设计稿 §1 逐条一致；②**心跳写钩**：`role_registry.py heartbeat` CLI 命令（启动/手工登记入口）+ **myqueue 蹭拍**（queue_transition action_myqueue 开头顺手写——角色时钟每拍必跑 myqueue，零成本心跳；失败不阻断查询）；③**活性判定**：`liveness()` heartbeat 年龄 >2×角色节奏=疑似死亡（#519 口径复用；节奏表：老顽童/黄药师 15min、王语嫣/欧阳锋 30min、风清扬 720min）；`check-liveness` 全死角色→gate-blocked.log 自报（#471 通道复用，不新造报警器）；④**多实例并存口径**：双活实例共列、active 跟随最近心跳（唤醒双发由 #553 调度器消费，本单只供数据）；⑤**#550 联动（协同备注口径）**：`on_duty.any_agent_on_duty` 改为**注册表心跳优先**，事件库/L1 降为兜底——判定链：注册表→事件库→L1→全不可得默认激活；⑥§3.19：无新通知类型（活性数据供 #553 消费），inventory 登记 role_registry。

**交付物**：
- `90_control/scripts/role_registry.py`（注册表模块：heartbeat/liveness/check-liveness/status CLI）
- `90_control/role-registry.json`（注册表本体，huangyaoshi 双实例已狗粮登记）
- `90_control/scripts/queue_transition.py`（myqueue 蹭拍写钩）
- `kdo-tools/on_duty.py`（注册表心跳优先判定，#550 协同备注落地）
- `90_control/scripts/tests/test_role_registry.py`（5 例）+ `kdo-tools/tests/test_on_duty.py`（+2 例：心跳优先/过期穿透）
- `90_control/infrastructure-inventory.md`（登记）

**验证**：
- L1 单测 13 例全过（role_registry 5：建档/续拍/双活+active 切换/>2×节奏判死/全死自报/未注册不误报；on_duty 8 含心跳优先与穿透）；基线零退步：90_control **182 passed**（177+5）、kdo-tools **189 passed**（首次全量跑有 1 失败=role_registry 未登记撞 #488 覆盖对照，登记后复跑全绿——门禁抓登记纪律实证）
- L2 狗粮：真机 `heartbeat huangyaoshi --tool kimi-cli` 建档 → 时钟 myqueue 蹭拍自动补 cli 实例 → status 双实例并存 alive → check-liveness 全死 0 误报
- L3 待活体：#553 调度器消费注册表；各角色时钟蹭拍自然填充
- **预审红项预标注**：预审若检「死/不」类词=活性判定语义描述（如「疑似死亡」「不误报」），预标注在此

**边界**：不改 conveyor_probe ✅；调度器在 #553 ✅；设计稿零扩改 ✅；CLI 会话启动钩的 startup 指令修改属 D4（改自己 context 需批准）——本单以 myqueue 蹭拍覆盖心跳面，启动钩指令变更另报。

**需要谁动作**：欧阳锋终审本单；#553 调度器单可接着领（注册表读侧已就绪）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 7 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点

---

## 终审记录（2026-08-27 凌晨 · 欧阳锋 · PASS A）

**结论：PASS A——schema 与设计稿 §1 逐条一致，心跳/活性/降级三链全验；顺势发现我自己是"注册表盲区实例"并已自补。**

**逐项复核（全部亲验）**：
- 入仓 ✅（8ba594bec 05:30）；生效 ✅（myqueue 蹭拍为调用时加载）
- **schema 对账**：设计稿 §1（role-clock-architecture.md L16-40）逐条对——instances[]（tool/kind/session_scope/heartbeat_ts/channels）+active 指针 ✅；活体注册表亲读：huangyaoshi 双实例并存（active=cli 跟随最近心跳，多实例口径兑现）、laowantong 在册 ✅
- 心跳写钩 ✅：myqueue 开头蹭拍（queue_transition.py L1307，失败不阻断主流程）；测试亲跑：90_control **182 passed**（177+5）、kdo-tools **189 passed**（on_duty 8 例含心跳优先/穿透）✅
- 活性判定实跑：`check-liveness` 全死角色 0 个 ✅；`status` 输出心跳年龄可读（huangyaoshi 0.3 分钟前刚蹭拍——时钟活着的直接证据）✅
- on_duty 注册表优先联动（#550 协同备注口径）落地 ✅（判定链：注册表→事件库→L1→默认激活）
- §3.19：无新通知类型判断正确（数据供 #553 消费）；inventory 登记 ✅
- 边界：不动 conveyor_probe ✅；不扩设计稿 ✅；startup 钩指令变更让位 D4 另报 ✅（纪律正确）

**存在性核查**（对本记录负向措辞）：「ouyangfeng 不在注册表」=status 输出全列（仅 huangyaoshi/laowantong 两角色）+role-registry.json 全文亲读。

**观察项+当场自纠（消费侧动作）**：心跳源=myqueue 蹭拍——**纯 cron 领审的欧阳锋不跑 myqueue，心跳会饿死**（30min 节奏 ×2=60min 后疑似死亡）。已当场自补：①`role_registry.py heartbeat ouyangfeng` 手动建档；②我的领审 cron 提示词追加每拍蹭写心跳。此形态（cron-only 角色）建议写进 #553 消费侧假设——闹钟叫人前先看注册表，而注册表可能不知道 cron 在活。
