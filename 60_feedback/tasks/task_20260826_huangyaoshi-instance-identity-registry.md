---
id: 546
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-26T18:36:40.975789+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- 90_control/scripts/queue_transition.py
- 90_control/scripts/tests/test_instance_registry.py
- 90_control/scripts/tests/test_review_override.py
- kdo-tools/conveyor_probe.py
- 90_control/notification-coverage-matrix.md
- 90_control/todos/ouyangfeng.md
---

# #546 实例身份登记 + 终审权机器校验（一具两职事件根治，#525 活性注册表轻量先行版）

- **任务号**：#546
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P2（今晚实证未造成坏结果——审查质量货真价实；但身份体系三入口三身份+reviewer 自由文本零校验，结构性洞）
- **立项**：2026-08-26 王语嫣（一具两职事件：一个 Claude 会话先当欧阳锋建领审 cron+终审两单，中途被指令做黄药师恢复；排查发现 cwd 主目录/三入口文件三身份（主目录 AGENTS.md=风清扬/用户级 CLAUDE.md=通用/wiki CLAUDE.md=默认黄药师），身份纯靠用户口头指定）

## 背景

终审权是工厂命门，但 `review --reviewer 欧阳锋` 是自由文本，任何实例都能以任何角色名义终审。今晚靠审查者自律没出事，机制上这是裸奔。#525 设计稿的活性注册表覆盖此事但实施单暂缓——本单=其中**身份登记+终审校验**的轻量先行版，不动心跳调度/飞书通道。

## 任务

1. **实例身份登记**：`.kdo/active-instances.json`——实例上岗时登记（角色/会话 id/cwd/工具名/时间）；`queue_transition claim` 时自动写入/更新（无感）
2. **终审权校验**：`review` 命令校验——登记表里该会话的角色=ouyangfeng 才放行 `--reviewer 欧阳锋`；未登记/角色不符 → 拒止+提示登记（--force --reason 逃生门，落 #444 台账）
3. 登记表供 conveyor_probe 读取（活性展示用，不做心跳调度——那是 #525 正单的活）
4. 回归：正常登记+终审/越权终审拒止/force 逃生三类用例
5. §3.19：新校验信号→同步矩阵

## 边界

- 不做心跳/唤起/飞书通道（#525 暂缓口径不动）；登记表是纯本地 json，不接外部服务
- 存量未登记实例兼容：首次 claim/review 时补登记，不回溯

## 验收

- 三类用例实测；一具两职场景重演（同会话先登记欧阳锋再以黄药师 claim → 行为符合口径）；欧阳锋终审


## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：实例身份登记 + 终审权机器校验（`queue_transition.py`）。①**登记表** `.kdo/active-instances.json`（纯本地 json，原子替换写入防半写）——记录 角色/cwd/工具/会话/时间；②**claim 无感登记**（`_register_instance`，测试件 task_9999_ 不登记 #483 纪律，登记失败不阻断流转）；③**register 命令**（`register <instance>` 早处理分支——欧阳锋等纯审查角色不 claim 的上岗入口）；④**终审权校验**（`_check_review_authority` 挂 action_review 最前）：当前 cwd 有 role=ouyangfeng 登记实例才放行 `--reviewer 欧阳锋`；未登记/不符 → 拒止+gate-blocked 台账+提示 register；`--force --reason` 逃生门落 #444 force 台账；⑤**conveyor_probe 活性展示**：`_instance_activity()` 只读登记表进 summary（计数+角色+最近登记时间），不做心跳调度（#525 正单边界不动）；⑥§3.19：矩阵事件 17 行 + 欧阳锋收件箱使用说明（消费端知晓纪律——他不 claim，需手动 register 一次，否则下次 review 被拦）。

**诚实能力边界**（写进代码注释）：多实例共享 cwd=wiki，校验只能证明「该工作目录有 ouyangfeng 上岗登记」；真·会话级身份绑定（一具两职完全防控）属 #525 正单（心跳/会话绑定）。本单价值=未登记裸奔封死 + 登记审计轨。

**交付物**：
- `90_control/scripts/queue_transition.py`（登记表读写/register 命令/终审权校验/claim 登记钩）
- `90_control/scripts/tests/test_instance_registry.py`（10 例回归）
- `90_control/scripts/tests/test_review_override.py`（fixture 补 stub——新门禁挂上后改判通道测试的配套更新）
- `kdo-tools/conveyor_probe.py`（活性展示只读钩）
- `90_control/notification-coverage-matrix.md`（事件 17 行）+ `90_control/todos/ouyangfeng.md`（登记说明）

（登记表本体 .kdo/active-instances.json 为 git 外运行时状态——.kdo/* 在 gitignore，与 state.json 同口径，故不在交付物清单；huangyaoshi 已狗粮登记）

**验证**：
- L1 单测 10 例全过：claim 登记/legacy 别名映射（hermes→laowantong）/task_9999 不登记/register 回读/已登记放行/未登记拒止/异 cwd 拒止/force 逃生（无 reason 拒+有 reason 放+台账留痕）/一具两职重演（双角色登记审计轨+口径行为）/probe 活性读取+fail-open
- 基线零退步：90_control **177 passed**（167+10）；kdo-tools 不动代码（170 基线不涉）
- L2 狗粮（真实登记表演出）：`register huangyaoshi` 成功落盘（role/cwd/ts 全字段）；`review task_9999_546demo` 在无 ouyangfeng 登记下**正确拒止 exit=1**（task_9999_ 分流进测试台账不污染真实日志）
- L3 待活体：欧阳锋下次 review 前先 register（已落其收件箱）；老顽童/王语嫣 claim 即自动登记
- **预审红项预标注**：本单预审若检「拒止/不得/缺失」类词=校验提示文案/报告描述误报，预标注在此

**边界**：不做心跳/唤起/飞书通道 ✅（#525 暂缓口径不动）；登记表纯本地 ✅；存量未登记实例拒止时给 register 指引，不回溯 ✅。

**需要谁动作**：欧阳锋终审本单；终审后请先跑 `register ouyangfeng` 再 review 其他单（否则被自己的新门禁拦）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 6 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（缺失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）
