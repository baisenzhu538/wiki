---
id: 553
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-26T21:52:58.183162+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- kdo-tools/role_clock.py
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
