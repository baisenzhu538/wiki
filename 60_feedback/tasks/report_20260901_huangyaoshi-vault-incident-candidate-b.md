---
id: report-590-candidate-b
title: "#590 候选 b 侦查报告——排除：本机 agent 会话非 02:00 删除操作者；候选 c（外部入侵）升级为唯一剩余候选"
type: report
status: delivered
created_by: 黄药师（施工）+ 王语嫣（第二棒代笔收尾，独立复验加强）
created_at: 2026-09-01
task_ref: "#590"
source_refs:
- "D:\\KDO-memory\\usn_full_20260831-0215.txt（#589 归档 USN dump）"
- 60_feedback/tasks/report_20260901_huangyaoshi-vault-incident-rootcause.md
---

# #590 候选 b 侦查报告

## 结论（双向结论中的：排除）

**候选 b（本机 agent 会话/脚本执行危险命令）排除**——三重独立否定：
1. **无作案窗口的会话**：事故窗口（01:30-02:05）11 个 hermes profile 中仅 wangyuyan（主会话 Mnemosyne 测试+cron 时钟拍）、laowantong 有消息活动，且两者活动内容与删除无关联（见 §1）；9 profile 零消息
2. **无作案工具痕迹**：kimi-cli 5 实例零新会话+user-history 危险命令零命中；90_control/scripts 100 个+kdo-tools 定时脚本静态审查，删除类操作仅限锁文件/旧备份/滚动清理，**无任何指向 wiki 主仓的清理路径**
3. **作案速度超交互极限**（王语嫣独立复验加强）：USN 秒级分布实测——wiki 删除 1487 条中 **1470 条挤在 2:00:55 单秒**（2:00:54 仅 11 条，2:01:03 尾部 6 条），同秒全盘其他文件删除背景仅 9 条。工具调用循环的 agent（每步 LLM 往返秒级起步）和人工都不可能达到单秒 1470 项且精确保留 objects 的删除节奏——这是原生进程级批量 API 的签名

**lint worktree 关联性：无关**（王语嫣亲验 birth time）：6 个 `.kdo_lint_baseline_*` 创建于 06-28/07-04/07-13×2/07-21，全部为 6-7 月陈旧残留，与 02:00 窗口零时间关联；其 worktree 元数据本就随事故消失成孤儿。

## §1 会话存在面（黄药师第一棒实测）

| 宿主 | 结果 |
|------|------|
| hermes 11 profiles（state.db messages 表逐 profile） | 窗口内活跃仅 wangyuyan（652 条：主会话 46c5cf38+cron 拍 020006）、laowantong（321 条）；其余 9 profile 零消息 |
| hermes gateway 存活面 | wangyuyan/huangyaoshi/ouyangfeng/laowantong-feishu 四 gateway 08-31 00:39 重启后存活；其余 6 个 pid 已死（08-26 起） |
| kimi-cli（5 实例心跳在 registry） | .kimi-code 会话目录 08-31 窗口零新会话；user-history 2 文件危险命令零命中 |
| 系统级 schtasks | TaskScheduler 事件日志 01:58-02:10 精确窗口：02:00:00 整点**零触发**；02:01:00 仅 kdo-inbox-watch+wechat-link-monitor（常规 10min 拍，其脚本删除面=零） |
| 脚本静态审查 | 90_control/scripts（100 个）+kdo-tools 定时脚本：删除操作仅 queue_lock.py 锁文件/vault-backup.py 旧备份/bundle.bat 滚动清理——无 lint worktree 清理跑偏路径 |

窗口内唯一活跃编排活动的时间线（黄药师自 state.db/时钟日志重建）：
01:55 老朱派活 → 01:55-02:01 王语嫣主会话 Mnemosyne 方法论验证（读文档+装环境+跑测试，无删除类工具调用）→ 02:00:06 cron 时钟拍启动 → **02:00:13 cron 拍跑 queue status 成功** → 02:00:52 .git 元数据开始被删 → 02:00:54-55 工作树删除大潮 → 02:01:29-40 cron 拍发现异常 → 02:04:38 判定事故 → 02:07-02:11 手工恢复+bundle。

## §2 秒级铁证（王语嫣第二棒独立复验，命令+输出）

```
python 复跑归档 USN dump（GBK 解码）：
wiki × 2026/8/31 2:00-2:01 × 0x80000200（文件删除|关闭）= 1487 条
秒级分布：2:00:54 → 11 条 | 2:00:55 → 1470 条 | 2:01:03 → 6 条
对照：02:00:xx 全盘非 wiki 删除关闭单秒峰值 = 9 条
```

样本行：`3162120192,"src_20260619_16e607de_30_wiki_concepts_yt_management_project_management.md",148,0x80000200,"文件删除 | 关闭","2026/8/31 2:00:54"`

**消解第一棒遗留的「待核对矛盾」**：cron 拍 02:00:13 queue status 成功读取 ≠ 与删除矛盾——删除开始于 02:00:52（.git 元数据），status 读取在其前 39 秒，时序自洽。矛盾不成立，消项。

注：第一棒自报「1503 条」与本次实测 1487 条差 16 条，系统计口径差（本报告口径=wiki 路径×2:00-2:01 窗口×0x80000200；以秒级复跑实测为准）。

## §3 候选 c（外部入侵/恶意软件）升级——给老朱的拍板清单

候选 a（坚果云，#589 本端高置信排除+云端待老朱对账）与候选 b（本双单排除）之后，**候选 c 成为唯一剩余候选**。操作者画像：懂 git plumbing（两阶段：先 .git 元数据 2:00:52、后工作树 2:00:54-55；精确保留 objects）、进程级批量能力、02:00 整点附近活动、无本机调度器足迹。

建议清单（按优先级，请老朱拍板执行项）：
1. **杀扫**：Windows Defender 完整扫描+Malwarebytes 第二引擎扫描（本机+组网内 makkapakka 家用机同做）
2. **改密**：Windows 登录密码、坚果云账号密码、git 凭据（GitHub token 等全部轮换）
3. **开审计**：安装 Sysmon（Event ID 1 进程创建/2 文件创建时间改动）+对 Desktop 目录配置文件删除 SACL 审计——下次再有目录级删除，进程名直接留痕（#589 遗留「取不到的铁证」就此补上）
4. **查暴露面**：确认 3389/RDP 是否暴露公网；筛查 08-31 前后 4624 登录事件日志（登录类型 10=远程桌面）

## §4 交付与边界

- 本单未执行任何清理（红线遵守）；影子仓未动
- 不重复 #589 考古面（坚果云/计划任务/事件日志/回收站）
- USN dump 归档于 D:\KDO-memory\usn_full_20260831-0215.txt（只读复用）

## 待老朱输入（对齐面）

- 坚果云网页版云端回收站 08-31 01:30-02:30 删除记录（#589 已留操作指引）——若云端有 wiki 批量删除记录=外部下发通路实锤；若无=外部直连本机或本机恶意软件
- 08-29/08-30「前天出事」现象描述（双凌晨 USN 零事件，待现象对齐判断记忆偏差或异源事件）
