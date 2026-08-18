---
id: task_20260816_codex-migration-t2
assignee: codex
status: queued
priority: P1
wsjf: 3.0
created_at: 2026-08-16
updated_at: 2026-08-16
source: 迁移建议书会审裁定（2026-08-16）
related: #343
---

# T2 纯 wiki 核心角色迁 Windows（#344）

## 涉及 profile
wangyuyan / ouyangfeng / laowantong（Windows profile：ouyangfeng 缺失需补全——黄药师）

## 任务（Codex 执行 + 各 Agent 冒烟）
同 T1 流程（预检→快照→停 WSL→起 Windows→冒烟→观察→验收/回滚）。**ouyangfeng 记忆连续性验收**：迁移后先跑失忆恢复路径（读锚点+最新 daily-context+汇报当前状态）再开始审查工作（8-15 恢复指引过期教训）。

## 冒烟标准
| Agent | 动作 | 通过 |
|:--|:--|:--|
| wangyuyan | 读 production-queue + kdo query | 与迁移前一致 |
| ouyangfeng | 读 1 卡 + source_refs | 溯源路径正确无漂移 |
| laowantong | 读队列 + 模拟领取 | 命令链路正常不实际入队 |

## 验收标准
旧侧停止/新侧稳定/冒烟全过/15 分钟无异常/关键路径无 /mnt/c 间接访问 + ouyangfeng 记忆连续性

## 老顽童记忆继承子项（codex 核实 2026-08-16 加——关键）

**现状**：干活的老顽童 CLI = WSL **默认根实例**（PID 1624，~/.hermes/，非 profiles/laowantong）。三处记忆不对齐：默认根 MEMORY.md（08-16 05:34 最新，实际在用）/ WSL profiles/laowantong（06-26 过期）/ Windows profile（08-11 快照，May/Jun 旧内容）。**直接起 Windows profile 会继承不到最近喂的知识**。

**继承方案（迁移时执行）**：
1. **必搬**：默认根 `~/.hermes/memories/MEMORY.md + USER.md` → **diff 后合并**到 Windows `AppData\Local\hermes\profiles\laowantong\memories\`（防丢 Windows 侧独有有效条目，不整文件覆盖）
2. **SOUL.md 不搬**：Windows profile 的 SOUL 才是老顽童人设（来自 .agent/laowantong-context.md）；默认根 SOUL 是 Nous 默认人设——搬了污染
3. **state.db 可选**（362MB/197 会话）：只想记人设/偏好/工作方法 → 不搬，靠 MEMORY/USER + wiki laowantong-amnesia-recovery.md 兜底；想续具体历史对话 → 停进程备份后迁（SQLite WAL）
4. **验证**：失忆恢复路径跑一遍——起 hermes 问"我是谁、当前任务是什么、KDO 生产纪律是什么"，答对才算继承成功（验收人：欧阳锋）

## 老顽童 CLI 实测补充（2026-08-16 hermes 老顽童 CLI 自析 + 王语嫣采纳——与 codex 核实合并）

**两个位置合并才是完整方案**（codex 核实 default 根 + CLI 自析 profile）：
1. **laowantong profile 记忆**：WSL/Windows 两侧 MEMORY.md/USER.md 内容一致（diff 仅 CRLF）——Windows 已有副本 ✅ 无需搬
2. **default 根记忆（关键补充）**：CLI 会话（PID 1624）记忆在 `~/.hermes/memories/`（WSL 侧，Windows 侧空）——**需补拷 MEMORY.md + USER.md（共 6.3KB）**
3. **知识资产**：wiki 锚点/复盘/错误模式库/技能日志全在 Windows 盘——迁移零影响天然共享 ✅
4. **会话历史**：Windows 侧已有 state.db ✅；skills 8.7M 副本**缺 2 个**（kdo-domain-tag-audit/yuanbao 补拷）

**迁移 5 项清单（有现成 skill 流程，洪七公先例）**：
1. 补拷 2 个缺失 skill
2. config.yaml 路径修复（/home/... → C:/...）+ 删 prefill_messages_file 陷阱行
3. gateway/status.py 打 WinError 87 补丁（os.kill(pid,0) Windows 抛异常——洪七公已打，老顽童要打）
4. 同步一次 laowantong memories（确保最新）
5. **停 WSL 侧 gateway 再启 Windows 侧**（唯一必须注意：WSL/Windows 双开会 gateway 冲突）

## 回滚
同 T1

## 执行门禁
⏸ **挂起：等老顽童 CLI 手头工作完成 + 用户命令**

## 技能丢失事件处置（2026-08-16 王语嫣诊断修复——追加）

**现象**：老顽童 CLI 迁 Windows 后"很多技能丢失"——kdo-self-attack 等 shared 技能不进注册表（`Skill not supported on this platform`, readiness=unsupported）。

**根因**：51 个 shared 技能 frontmatter `platforms: [cli, feishu]`——作者意图"Hermes cli/feishu 端可用"，但 hermes v0.20.0 的 `platforms` 字段语义是 **OS 平台**（PLATFORM_MAP 仅 macos/linux/windows，skill_utils.py:21）。cli/feishu 不匹配 win32 → 全部屏蔽。WSL 侧同款逻辑（这些技能在 WSL 侧其实也从未被 laowantong CLI 加载过——老顽童一直只用本地 28 个技能）。

**修复**：51 处 shared + 2 处 .claude/skills（双轨一致）批量替换 `platforms: [cli, feishu]` → `platforms: [linux, macos, windows]`（保持"全平台可用"原意）；stage-3-tooling 教学示例一并修正（防继续传播错误用法）；备份 `AppData\Local\hermes\_backups\skills-platform-fix-20260816\`（51 文件）。

**验证**：laowantong CLI（AppData\Local 侧）98 local 全 enabled（28 本地+70 shared 全覆盖）；T1 3 profile（.hermes 侧）143 local 全 enabled（48 顶层+70 shared+25 本地）；kdo-self-attack/stage-1-diagnose/strategy 全家/任务编排均在列。注册表按进程启动扫描——**重启 gateway / 新会话生效**。

**教训**：E030 已入错误模式库（skill frontmatter `platforms` 字段语义误用；写 skill 前查 hermes 字段语义文档）。


## 挂起条件解除（2026-08-18 王语嫣编排更新）

- 老顽童 CLI 已确认空闲（2026-08-18 老顽童本尊：活跃待命、无在产任务、失忆恢复完成）
- 用户已下令起链（2026-08-18）——本任务可领取执行
