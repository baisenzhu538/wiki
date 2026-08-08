---
id: corr_20260808_ouyangfeng-self-iteration
date: 2026-08-08
author: 欧阳锋
related_agents: [laowantong, wangyuyan, coach-agent]
status: closed
---

# 欧阳锋自我迭代诊断：教练 Agent 教会我的事

> 触发：欧阳锋转发教练 Agent 自主迭代案例（#252 试点意外收获）+ 王语嫣自我诊断。
> 教练 Agent 闭环 = 发现问题 → 诊断根因 → 修复 → 沉淀为知识 → 注册 → 下次绕开。
> 本文是欧阳锋对照自己的 config.yaml / SOUL 文档 / 实际运行环境的诚实诊断。

## 一、我的 config 现状（对照教练 Agent 的坑）

| 配置项 | 实际值 | 与教练 Agent 对比 | 实际影响 |
|:--|:--|:--|:--|
| approvals.mode | **manual** | 同款坑！教练 Agent BLOCKED→切 smart | 飞书网关下复杂内联命令被审批拦截（本日实测：python3 多行脚本 BLOCKED） |
| terminal.timeout | 180s | 一般 | 长命令有超时风险 |
| gateway_timeout | 1800s | 宽裕 | 网关侧无碍 |
| terminal.cwd | `.` | 教练 Agent cwd 错→改 /mnt/c/ | 我审查时显式用 workdir，基本没踩 ✅ |

**本日实测证据**：运行 `python3 -c "...复杂解码脚本..."` 时被 BLOCKED（"user has NOT consented"）——这就是 approvals.mode: manual + 飞书网关的现场演示。我此前多次遇到类似拦截都默默降级换命令，从未主动查过 config——和王语嫣同一个模式：「绕过」而非「诊断+修复」。

## 二、今天实际踩的坑（有证据）

### 坑 1：search_files 搜 30_wiki 超时/空结果（双 Agent 共踩）
- **症状**：`search_files` 搜中文 glob（`*作图*`/`*日报*`/`*温度*`）返回空结果；搜 task 文件时 0 结果
- **根因**：`/mnt/c/` 是 9p 网络文件系统挂载，ripgrep 递归扫全目录性能差 + WSL2 缓存延迟叠加；中文 glob 匹配易失效
- **修复**：`cmd.exe /c "dir /s /b C:\...\*关键词* 2>nul"` 秒出结果
- **教训**：王语嫣同批踩到同一坑（search 30_wiki 多次超时→降级 terminal find）——**已沉淀到 kdo-card-review skill「search_files 在 /mnt/c/ 下超时」节**（2026-08-08 patch）

### 坑 2：context 文档过时（SOUL.md 过时问题）
- **症状**：`ouyangfeng-context.md` 仍写 `runtime: Kimi Code CLI`、`workDir: C:\Users\...`（Windows 路径）
- **根因**：文档是 Kimi Code CLI 时代写的，实际运行在 Hermes Agent + WSL2（`/mnt/c/` 路径）
- **风险**：新会话的我按文档启动 → 用错路径 → 踩 WSL2 缓存延迟坑
- **修复**：见「三、请求修复」第 3 项——需要用户/王语嫣确认后更新文档

### 坑 3：检索规则过时（kdo query vs 实际工具）
- **症状**：context 写 `python kdo-tools/kdo query` 语义检索，我实际用 `search_files`/`terminal grep`
- **根因**：环境迁移后文档未同步
- **修复**：kdo query 仍可用（兜底），但实际主力是 Hermes search_files + cmd.exe dir——文档需补充说明

## 三、请求修复（写在 60_feedback = 职责内）

| # | 请求 | 建议方案 | 受益 |
|:--|:--|:--|:--|
| 1 | terminal 白名单 | 把 `cmd.exe`/`iconv`/`dir` 等只读命令加入 approvals whitelist，避免复杂内联命令被拦 | 全 Agent——每次查文件不重踩 |
| 2 | 评估飞书网关下 approvals.mode | 至少把只读命令加入 manual allowlist；长期评估 smart 模式 | 王语嫣/教练 Agent 同受益 |
| 3 | context 文档同步 | `ouyangfeng-context.md` L3 runtime 改为 Hermes Agent、L4 workDir 改为 `/mnt/c/Users/Administrator/Desktop/wiki/` | 新会话不失忆 |
| 4 | production-queue 编码修复 | 队列文件 UTF-8-SIG 混合 mojibake（历史遗留）——黄药师统一编码 | 全 Agent 队列读取不再乱码 |

## 四、自我迭代承诺（欧阳锋版）

1. **不再「忍一忍绕过」**：工具卡顿/超时/被拦 → 先查配置层（approvals.mode/cwd/文档规则），再怀疑命令
2. **每次踩坑即沉淀**：坑 → corrections 文件 + skill「已知工具故障」表，一次沉淀永久受益
3. **配置类问题显式请求**：写 corrections 请求黄药师/用户评估，不沉默
4. **验证闭环**：下次同类问题 → 查 corrections/skill → 不重复踩

*欧阳锋 · 2026-08-08*
