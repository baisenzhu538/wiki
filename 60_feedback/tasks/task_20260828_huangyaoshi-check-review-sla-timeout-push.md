---
id: 574
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-29T05:40:34.416938+00:00'
version: v0.1
code_files:
- 90_control/scripts/check-review-sla.py
- 90_control/scripts/tests/test_check_review_sla.py
- 90_control/scripts/health-check.py
instance: huangyaoshi
reviewed_by: 欧阳锋
review_date: '2026-08-29'
grade: A-
---

# #574 check-review-sla 升级「超时必推」+ 推送通道对齐调研（R1+R3 合并立项）

- **任务号**：#574 ｜ **状态**：queued ｜ **assignee**：huangyaoshi（欧阳锋终审）｜ **优先级**：P1
- **立项**：2026-08-28 王语嫣裁定（欧阳锋建议书 `diag_20260828_ouyangfeng-review-wakeup-gap.md`，R1+R3 合并，R2 欧阳锋自执行）

## 背景

待审提醒断链（#573 事件实证）：todos/cron/webhook 三通道全部工作但止于「文件/群」，无一能真实唤醒审查者会话——#573 提审后挂审 40min 无人响应，直到用户飞书追问才叫醒。性质=推送通道与唤醒通道不匹配的机制断链，非「agent 不自觉」。且 #521 R2 老朱已拍板「终审类通知不静默」未落地。

## 任务

1. **R1（治本门禁）**：check-review-sla.py 升级「超时必推」——pending_review 最大年龄 30min → 推送提醒（复用 conveyor_probe._send_hook 加签，零新基建）+ todos 落盘；2h → 升级 @ 负责人/老板。消息含「#xxx 待终审 + 挂审时长 + 任务单路径」。
2. **R3（调研，并入本单）**：webhook 群机器人接收端（17f2a4cd-50b8-4e4e-9036-ec26b0c9d67d）是否用户/老朱可见常用；若不可见，评估角色 webhook 指向「gateway 监听 DM 入站通道」或统一 cron deliver=feishu；调研 Hermes gateway 是否支持 webhook 入站（消息进输入流=「提醒即唤醒」完全自动化）。

## 验证

- R1：构造 31min 挂审样例 → 触发 webhook 推送 + todos 落盘；2h 样例 → 升级消息含 @ 标记。
- R3：调研结论落档（webhook 接收端可见性 + gateway 入站可行性）。
- 回归：#573 同场景重演——提审后 30min 内审查者会话被真实唤醒（用户/老朱飞书可见提醒即达标）。

## 边界

- 本单不改判任何既有机制（#520 叫醒通道/探针全保留），只补「超时升级」与「通道对齐」两环。
- R2（ouyangfeng-clock-v1 deliver local→feishu）不占本单——欧阳锋自改非共享基建，即时见效。
- 复用 #519 空转报警（check-conveyor-state）同族先例：「有异常必须响」机制化。
- 若实现触碰 conveyor_probe.py/queue_transition.py/role_clock 三基础设施文件，按第七信号精度纪律（08-28 裁定）在任务单 frontmatter 预标 matrix_exempt: true+理由。

## 关联

- 欧阳锋建议书 `diag_20260828_ouyangfeng-review-wakeup-gap.md`（R1+R2+R3 全采纳裁定）
- #520 R3（check-review-sla 初版，SLA_HOURS=2h 只 print 无推送）/ #519（空转报警同族）/ #521 R2（老朱拍板「终审类通知不静默」）

## 需要谁动作

- **黄药师**：R1+R3 施工，回归验证
- **欧阳锋**：终审本单；R2 自改 ouyangfeng-clock-v1 deliver→feishu（与本单并行，不占产线）

## 补充要求（2026-08-28 王语嫣追加，老朱指令）

**断链治理范围收窄**：只覆盖产线三角色（老顽童/欧阳锋/黄药师），**风清扬排除**——观察者、日 2 拍、不阻塞产线，不纳入 clock deliver→feishu + 收件箱消费改造。

**R3 落地扩一档**：调研结论落档后，产出「产线三角色 clock 配置规范」——各角色 clock cron ① deliver local→feishu（值守结果直达飞书 Home，无新事 [SILENT] 静默，有实质动作才推）② prompt 加「主动读 90_control/todos/<role>.md 收件箱并执行待办」。R2（欧阳锋自改 ouyangfeng-clock-v1 deliver→feishu）即首例，老顽童/黄药师按此规范对齐。

> 依据：老朱反馈「文件到收件箱，接收方视而不见」——单靠王语嫣时钟自动干活不够，接收方不消费即断链。治本链 = 各角色 clock deliver→feishu（R2 模式）+ 主动消费收件箱（prompt 环节）+ R3 gateway 入站（提醒即唤醒）。

## 执行报告

**文件清单**：
- `90_control/scripts/check-review-sla.py`（R1 主体：分级推送 30min 提醒 / 2h 升级）
- `90_control/scripts/tests/test_check_review_sla.py`（7 例重写）
- `90_control/scripts/health-check.py`（check-review-sla 描述更新）
- `90_control/notification-coverage-matrix.md`（新增信号 23「挂审超时必推」）
- `90_control/infrastructure-inventory.md`（check-review-sla 行描述 + 测试数更新）
- `60_feedback/diagnosis/diag_20260829_huangyaoshi-review-wakeup-gateway-inbound.md`（R3 调研，新建）
- `60_feedback/tasks/task_20260828_huangyaoshi-check-review-sla-timeout-push.md`（本任务单）

**完成内容**：R1 照做 + R3 gateway 入站调研（clock 规范因时钟停用过时跳过）。①R1：check-review-sla.py 升级「超时必推」——pending_review 最大年龄 30min→推审查者（ouyangfeng）webhook + todos 落盘；2h→升级推 ouyangfeng + wangyuyan 群（@负责人/老板，老朱在群可达）；复用 conveyor_probe._send_hook/_load_hooks/_append_role_todo 加签（零新基建）；--dry-run 只打印；通知类打印走 stderr（#568 族）。②R3：调研落档——webhook 群机器人接收端=出站单向、无 chat_id 元数据、#573 实证非常驻可见；Hermes gateway 入站=支持独立 webhook 平台（platforms.webhook）但本机未启用，正确路径已厘清待裁定档次。③矩阵同步：新增信号 23（§3.19 铁律1 登账；本单未触碰 conveyor_probe/queue_transition/role_clock 三基础设施文件，故无 matrix_exempt 预标）。

**验证**：
- L1 单测：test_check_review_sla.py **7 例全过**（31min 提醒推 ouyangfeng / 3h 升级推两通道含 @ / 划掉行跳过 / 零积压 / 段标记缺失 / dry-run 无副作用 / 10min 不推）。
- L2 狗粮：dry-run 构造样例实测——31min→提醒分支 exit 0、121min→升级分支 exit 1 含 @、29min→不推；真实队列 --dry-run「零积压」exit 0。
- 回归 #573 同场景：当前队列 REVIEW-PENDING 零活跃行，无法真实重演「提审→30min→唤醒」；L3 活体留待本单提审后（#574 自身成 pending_review，超时后触发提醒）。

**未做项**：
- **R1 调度缺口（如实声明）**：check-review-sla 仍挂 health-check 日级（每日 02:07），「30min 提醒」不会在 30min 实时触发（日级只保证每日检查一次）。分钟级调度原挂 role_clock（5min，矩阵信号 20）已随 08-29 老朱定调时钟停用下线。若「30min 提醒」要实时生效，需后续立项把 check-review-sla 挂 conveyor_probe（10min 探针）或独立计划任务——这会触碰 conveyor_probe.py（三基础设施文件之一），超出本单「R1 照做 + R3 调研」明确范围，留王语嫣编排决策。
- 「产线三角色 clock 配置规范」过时跳过（时钟停用，08-29 老朱定调）。
- webhook 群接收端「是否常驻可见」需用户/老朱口头确认（代码侧无法判断，见 R3 调研 §一）。

**需要谁动作**：欧阳锋终审本单；王语嫣裁决 R1 调度缺口（是否立项高频调度）+「提醒即唤醒」落地档次（webhook 入站重 / R2 值守拍轻）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 6 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（缺失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）

## 终审记录（2026-08-29 欧阳锋）

**结论：PASS A-**（#574 R1+R3 合并单闭环；R1 调度缺口为条件项，已如实声明并路由王语嫣裁决）

### 通过维度（全部 O3 独立复验，非采信报告）

| 验收项 | 证据 | 状态 |
|:--|:--|:--|
| R1 30min 提醒：推审查者 webhook + todos 落盘 | L1 test_remind_over_30min 独立复跑过；L2 狗粮 31min 独立复现——dry-run 消息含「#505 + 挂审 31min + 任务单路径」三要素；check-review-sla.py L112-120 提醒分支、L107-108 todos 落盘（`if not dry_run` 保护） | ✅ |
| R1 2h 升级：@ 标记 + 双通道 | L1 test_escalate_over_2h 独立复跑过（roles=[ouyangfeng,wangyuyan] 且 "@" in msg）；L2 狗粮 121min 复现 rc=1、消息「🚨 @负责人 @老朱」 | ✅ |
| R1 边界与零副作用 | 29min 不推 / 10min 不推 / 划销行跳过 / 零积压 / 段标记缺失 exit 1 / dry-run 不落 todos——7 例全过；真实队列 --dry-run 实测「1 单待终审，最大年龄 3min」exit 0 零副作用（#574 自身即活体行） | ✅ |
| R3 调研落档 | diag_20260829 四节：①webhook 出站单向、无 chat_id 元数据（.feishu_webhooks.json 四角色 {url,key} 亲验）、#573 实证非常驻可见 ②gateway platforms.webhook 未启用、三通道区分表、正确路径厘清 ③clock 规范过时标注 ④待裁定项清晰 | ✅ |
| 矩阵同步（§3.19 铁律1） | notification-coverage-matrix.md 信号 23 登账（含豁免理由标注）；本单未触碰 conveyor_probe/queue_transition/role_clock 三基础设施文件（仅 import 复用函数），无 matrix_exempt 预标合理 | ✅ |
| 交付入仓（#522 门禁） | 67f9b51eb（feat R1+R3）+ e726d85be（complete）双 commit；六交付物 git status 零未提交改动 | ✅ |

### 代码审查要点

- 复用 conveyor_probe._load_hooks/_send_hook/_append_role_todo（L683/L714/L774 亲验，签名逐参匹配）；_send_hook 校验响应 body code（2026-08-23 假发送教训在案）——推送层可靠
- 分级阈值严格大于：30min 整点不推 31min 推、120min 整点不升 121min 升，与测试/狗粮输出逐字一致
- 跨年回退（submitted > now → year-1）、划销行跳过（`- ~~` 前缀）、通知类打印走 stderr（#568 族）逻辑完备
- dry-run 双保护：_push dry 分支不发送 + todos 落盘有 `if not dry_run` 守卫——零副作用实证

### 降级 A- 理由（非质量瑕疵——端到端生效依赖后续立项）

- 验收项 3「#573 回归：30min 内真实唤醒」为**条件性达成**：check-review-sla 仍挂日级 health-check（02:07），「30min 提醒」不会在 30min 实时触发。分钟级调度需触碰 conveyor_probe.py（三基础设施文件之一），超出本单「R1 照做 + R3 调研」明确边界。黄药师在「未做项」如实声明并路由王语嫣裁决——声明诚实、边界守纪（未越界施工），不构成 FAIL；但端到端「超时必推」的实时性留待立项，故记条件项降 A-。

### 存在性核查（负向表述锚点，F-035/#433）

**存在性核查**

| 负向表述 | 核查证据 |
|:--|:--|
| 「30min 提醒未实时接线」 | health-check.py L91 挂载行仅日级描述；check-review-sla.py 无独立分钟级计划任务注册（grep 计划任务目录零命中）；conveyor_probe.py 无调用点（复用仅限 import 函数，非挂载） |
| 「产线三角色 clock 配置规范未产出」 | diag §三 明确标注「过时跳过」及原因（08-29 老朱定调时钟停用）；任务单「未做项」段同声明——前提消失=规范过时，边界声明合理，不构成缺失 |

### 残余风险 / 观察项

- **R1-1（P2，路由王语嫣裁决）**：30min 实时提醒依赖高频调度立项（建议挂 conveyor_probe 10min 探针或独立计划任务）
- R1-2（P3）：webhook 群接收端「常驻可见」需老朱/用户口头确认（代码侧无法判断，R3 §一）
- R1-3（P3）：R2 ouyangfeng-clock-v1 deliver→feishu 是否随时钟停用下线，交欧阳锋/王语嫣确认（diag §三 残留有效性）

### 反馈路由

反馈编排者王语嫣（R1-1 裁决待办 + 提醒即唤醒 tier 拍板）+ 抄送生产者黄药师（闭环确认）。
