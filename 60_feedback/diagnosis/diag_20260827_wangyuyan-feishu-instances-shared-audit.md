---
id: diag_20260827_wangyuyan-feishu-instances-shared-audit
type: diagnosis
status: orchestrated
author: 王语嫣
audience: 老朱
date: 2026-08-27
---

# 飞书四实例「三共享」诊断：记忆/上下文/基础设施（老朱 08-27 指令）

> 触发：老朱指令——飞书欧阳锋/老顽童/黄药师/王语嫣是在外生产线，应与本地 CLI 同名实例共享记忆、共享上下文、共享 KDO 工厂基础设施。
> 方法：逐 profile 实证（SOUL.md/config.yaml/cron/executions.db/进程/schtasks），与本地 CLI 角色启动协议对账。

## 一、总评

**三共享现状：1/3 及格，2/3 断裂。** hermes gateway 进程活着（5 个，22:56 启动）、ticker 心跳在跳（01:46 实测）——**通道层活着**；但记忆层三个 profile 断、上下文层唯一的任务时钟卡死、SOUL 与角色定义漂移两处。飞书实例目前=「能收到飞书消息的影子」，不是「共享工厂的同名人」。

## 二、逐实例体检

| 实例 | SOUL 记忆锚点 | SOUL 角色定义 | 任务时钟 | approvals.mode |
|:--|:--|:--|:--|:--|
| ouyangfeng | ❌ 零锚点 | ✅ 已对齐（Reviewer，08-26 修） | ❌ 无 jobs（仅 ticker 心跳） | ✅ smart |
| laowantong | ❌ 零锚点 | ⚠️ 半旧（Producer 对，但指向 /mnt/c WSL 路径+2026-06-20 旧任务清单） | ⚠️ **有但卡死**（clock-v3 */15min，last_run 22:23，hermes 22:56 重启后 next_run 停 22:30 不推进） | ❌ **manual** |
| huangyaoshi | ✅ 有（20_memory 锚点+queue_transition 纪律） | ✅ 对齐（Builder） | ❌ 无 jobs | ❌ **manual** |
| wangyuyan | ❌ 零锚点 | 🔴 **严重漂移**（还是旧版「诊断咨询者……不动手改」，与现行「操作系统/方向把关/队列维护」两个物种） | ❌ 无 jobs | ✅ smart |

## 三、关键发现（按严重度）

1. **🔴 hermes cron 调度器重启不恢复**（新发现，今晚老顽童"装死"的飞书侧真相）：laowantong-clock-v3 enabled/scheduled 正常，last_run 22:23:58 ok，但 hermes 进程 22:56 重启后 **next_run_at 永远停在 22:30**——错过 fire 点的 job 不再被调度。同机 ticker（其他三 profile 的心跳）01:46 正常——**心跳活着、任务死了**，调度器对 jobs.json 和 ticker 的恢复逻辑不对称
2. **🔴 wangyuyan SOUL 角色定位漂移一个版本代际**：旧「诊断咨询者」（不维护队列/不裁定/不动手）vs 现行「操作系统+方向把关+任务标注」——飞书王语嫣按这个 SOUL 跑会是个废角色
3. **🟡 记忆锚点三缺一模式**：只有黄药师 SOUL 挂了 20_memory 失忆锚点+queue_transition 纪律；其余三个 profile 失忆即裸奔
4. **🟡 laowantong SOUL 路径陈旧**：写 /mnt/c（WSL）+ 两个月前的任务清单——实例早已迁 Windows（cron job workdir 是对的，SOUL 没跟上）
5. **🟡 manual 残留两 profile**（已随洞察报告立 #559 止血）
6. **✅ 值得肯定**：laowantong-clock-v3 的 prompt 设计是对的（queue_transition status+myqueue+收件箱落盘，终审落点检测先行）——证明飞书时钟的「正确形态」已被验证过，只是基建（重启恢复）没跟上

## 四、与 #525（系统级角色时钟）的关系裁定

- **不另建 hermes cron 时钟**——#553 role_clock（schtasks 系统级）落地后，hermes 只是传输适配器（设计稿 §3：hermes=profile 消息）。飞书四实例时钟等 #553 统一路由，不搞双轨
- **但 hermes cron 卡死 bug 必须修**——role_clock 的 hermes 适配器依赖 hermes 侧能收消息；且 laowantong-clock-v3 在 #553 落地前是飞书侧唯一时钟，它是现役资产不是废纸
- 老顽童 kimi 会话侧：等 #555 开通（15min 节奏已在册）

## 五、立项

| 单 | 内容 | 负责 | 优先级 |
|:--|:--|:--|:--|
| #560 | hermes cron 调度器重启不恢复排查（job 错过 fire 点后 next_run 不推进） | 黄药师 | P1 |
| #561 | 飞书四实例 SOUL.md 对齐刷新：记忆锚点三补一+wangyuyan 角色定义重写+laowantong 路径/清单更新+统一加「读 todos 收件箱+myqueue」协议段（口径王语嫣随单附） | 黄药师执行 | P1 |

不立项的：飞书时钟补齐（等 #553 统一调度，防双轨）；#509 飞书黄药师挂起项（仍等老朱拍模型/挂点/app_secret——不占队列）。

## 六、回放：老朱三问的完整答案

「为什么昨天正常今天不正常」全链路：昨天老顽童时钟=hermes profile cron（系统级，老朱记得对）跑到 22:23 → 22:56 hermes 重启 → job 卡死（发现 1）→ 23:03 老朱 kimi 会话叫醒的是**另一个实例**（kimi 侧老顽童，无 cron）→ 双实例双断。我今晚先误判「时钟活在会话里」，再误判「hermes 实例没在跑」——两层各错一半，已记 E057。
