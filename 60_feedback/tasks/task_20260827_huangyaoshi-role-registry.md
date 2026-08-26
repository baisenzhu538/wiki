---
id: 552
assignee: huangyaoshi
status: queued
updated_at: '2026-08-27T01:05:00+00:00'
version: v0.1
instance: huangyaoshi
code_files:
  - 90_control/role-registry.json
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
