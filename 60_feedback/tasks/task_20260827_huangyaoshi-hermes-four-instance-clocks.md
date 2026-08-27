---
id: 563
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-27T20:06:24.969024+00:00'
version: v0.1
instance: huangyaoshi
code_files: []
---

# #563 hermes 飞书四实例时钟配置（ouyangfeng/huangyaoshi/wangyuyan 裸奔补齐）

- **任务号**：#563
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P1（飞书侧四实例只有一个有时钟且卡死，其余三个裸奔——飞书产线“被@才动”的根因）
- **立项**：2026-08-27 老朱直令「飞书的四个角色都需要配置时钟」，王语嫣诊断实证随附

## 背景（实证链）

- hermes profiles cron 目录实测（08-27 20:30）：
  - `ouyangfeng` / `huangyaoshi` / `wangyuyan`：**连 cron/jobs.json 都不存在**——从未配过任务时钟
  - `laowantong`：唯一有 job（clock-v3，*/15min），但 next_run 卡死 08-26 22:30（#560 重启不恢复 bug）
- 对照本地：role_clock（#553）对四角色的唤醒调度正常（08-27 全天日志连续），
  欧阳锋 CLI 被判「全实例疑似死亡」实为**心跳语义误报**（活着但 idle 无蹭拍，#562 任务2）——
  飞书侧则是**真的没有时钟**，两回事别混淆
- 节奏口径（与 #555 本地一致）：老顽童 15min / 王语嫣 30min / 欧阳锋事件驱动+30min 兜底 / 黄药师 15min

## 任务

1. 为 ouyangfeng / huangyaoshi / wangyuyan 三个 hermes profile 各建时钟 cron job
   （复用 laowantong clock-v3 的 prompt 模板，节奏按上行口径）
2. laowantong clock-v3 卡死恢复（依赖 #560 修复；若 #560 未落地则本单先手动重建 job 止血）
3. 四个 job 心跳写入 role-registry.json（kind=platform, profile=<role>）——飞书实例活性从此可见，
   check-liveness 才能区分「本地死」和「全死」
4. 验收回归：构造一次 pending_review → 飞书欧阳锋在兜底节奏内自起响应

## 边界

- 只配时钟和心跳，不动 SOUL/profile 内容（#561 的活）、不改审批模式（#559 的活）
- hermes cron 恢复逻辑 bug 归 #560，本单不重复修；两单同批施工分开 commit
- 频率不得高于本地节奏口径，防双源唤醒风暴

## 验收

- 四 profile jobs.json 齐 + role-registry 出现四条 kind=platform 心跳 + 欧阳锋兜底唤醒实测；
- 欧阳锋终审

## 执行报告（2026-08-28 黄药师，kimi-cli 会话）

### 交付物

| 项 | 内容 |
|---|---|
| 新时钟 ×4 | ouyangfeng-clock-v1（8bb423783921, */30，事件驱动+兜底）/ huangyaoshi-clock-v1（797bbb2ca8b5, */15）/ wangyuyan-clock-v1（80b947f2c3f0, */30）/ laowantong-clock-v4（d50fa5f284d6, */15）——全部 deliver=local、workdir=wiki、enabled_toolsets=[terminal,file]（对齐 clock-v3 压低 token） |
| prompt 模板 | 复用 clock-v3（第0步终审落点/第1步可领检测/纪律四条），新增**第2步蹭拍心跳**：`role_registry.py heartbeat <role> --tool hermes --kind platform --profile <profile> --channels feishu,todos`——飞书实例活性每次 fire 自刷新 |
| clock-v3 卡死恢复 | **迁居方案（偏离 #560 设想，理由如下）**：laowantong profile 的 tick 属主=两个已禁用计划任务（`\Hermes-Gateway-laowantong`→start-hidden.vbs 起一个 platforms:{} 的空 gateway）；而飞书老顽童实体=laowantong-feishu profile（nssm 服务在跑、ticker 新鲜）。把时钟放进空壳 gateway 不满足老朱直令「飞书的四个角色都需要配置时钟」——唤醒落点必须是飞书实例本体。故 clock-v4 落在 laowantong-feishu，旧 clock-v3 已 pause（paused_reason 写明迁居去向，防旧 gateway 复活后双时钟） |
| role-registry | 四角色补齐 kind=platform 实例（profile 分别为 ouyangfeng/huangyaoshi/wangyuyan/laowantong-feishu），初始心跳已写；此后由时钟 job 每次 fire 自写 |

### 回归实证

- ✅ 准点 fire：03:45 huangyaoshi/laowantong-feishu 两 job 由调度器自然触发（source=builtin）completed；03:43 wangyuyan 手动 trigger completed
- ✅ 心跳自写：三次成功 fire 后 registry platform 心跳 ts 分别刷新到 03:43:40/03:45:43/03:45:51（job 自己写的，非我手工）
- ✅ check-liveness 可见性：`role_registry.py status` 四角色 hermes 实例全部 alive，与本地 cli 实例并列可区分
- ❌ **04:00 fire 全部失败：HTTP 402 Insufficient Balance（DeepSeek）**——四 profile 共用同一 API key（md5 一致），余额在 03:45-04:00 间耗尽；历史 402 曾于 08-19/08-24 出现后恢复。**已急报王语嫣收件箱（04:05）**。时钟机制本身无罪——fire 准点、进入 LLM 调用才失败

### 验收口径自裁

- 验收项「构造 pending_review → 飞书欧阳锋兜底自起」**当前不可证**：欧阳锋 feishu 实例 LLM 调用同样 402，任何唤醒都无法产出响应。本单 complete 本身即构成一次真实 pending_review——余额恢复后欧阳锋时钟（*/30）检测到状态变化即自然闭环，留作延迟验收观察点
- #562 矩阵补课转办（03:45 收件箱）：已核实 4bcff2703 由 #562 交付方补登完毕（行 5 多行聚合口径+行 22 冷却语义），无需我重复动作

### 边界自查

- 未动 SOUL/profile 内容（#561 领地）、未动 config.yaml/审批模式（#559 领地）、未改 hermes 代码（#560 领地）
- 未启用任何已禁用计划任务（避免双 gateway）；旧 clock-v3 仅 pause 未删（留考古）

### F-034 五字段

- **完成内容**：飞书四实例时钟全部上线（3 新建+1 迁居修复），心跳入 role-registry，调度准点已实证；当前唯一阻塞=DeepSeek 402 余额耗尽（外部）。
- **改动文件**：仓外=`C:/Users/Administrator/AppData/Local/hermes/profiles/ouyangfeng/cron/jobs.json`、`C:/Users/Administrator/AppData/Local/hermes/profiles/huangyaoshi/cron/jobs.json`、`C:/Users/Administrator/AppData/Local/hermes/profiles/wangyuyan/cron/jobs.json`、`C:/Users/Administrator/AppData/Local/hermes/profiles/laowantong-feishu/cron/jobs.json`（四时钟新建）、`C:/Users/Administrator/AppData/Local/hermes/profiles/laowantong/cron/jobs.json`（clock-v3 pause+迁居注记）；仓内=`90_control/role-registry.json`（四 platform 实例心跳）、`90_control/todos/wangyuyan.md`（402 急报）
- **验证**：`hermes -p <profile> cron list` ×4 → 各 1 job enabled；`cron runs` → 03:45 huangyaoshi/laowantong-feishu source=builtin completed、03:43 wangyuyan direct completed、04:00 ouyangfeng/wangyuyan failed(HTTP 402)；`role_registry.py status` → 四角色 hermes 全 alive（心跳 ts=03:43:40/03:45:43/03:45:51 为 job 自写）
- **未做项**：验收项「pending_review→飞书欧阳锋兜底自起」因 402 暂不可证（本单 complete 即真实 pending_review，余额恢复后自然闭环=延迟验收观察点）；未启用已禁用计划任务（防双 gateway）；未动 SOUL/config/hermes 代码（#559/#560/#561 领地）
- **需要谁动作**：老朱=DeepSeek 充值或裁定切换 provider（急报已落王语嫣收件箱 04:05）；欧阳锋=终审本单

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

- 🔴 声称但未入仓（untracked）: `C:/Users/Administrator/AppData/Local/hermes/profiles/huangyaoshi/cron/jobs.json`
- 🔴 声称但未入仓（untracked）: `C:/Users/Administrator/AppData/Local/hermes/profiles/laowantong-feishu/cron/jobs.json`
- 🔴 声称但未入仓（untracked）: `C:/Users/Administrator/AppData/Local/hermes/profiles/laowantong/cron/jobs.json`
- 🔴 声称但未入仓（untracked）: `C:/Users/Administrator/AppData/Local/hermes/profiles/ouyangfeng/cron/jobs.json`
- 🔴 声称但未入仓（untracked）: `C:/Users/Administrator/AppData/Local/hermes/profiles/wangyuyan/cron/jobs.json`
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点
