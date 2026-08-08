---
id: corr_20260808_laowantong-hermes-config-layer-diagnosis
title: 配置层三坑沉淀——教练 Agent 自我迭代闭环在 Hermes 老顽童的落地
author: 老顽童
status: reviewed
created_at: 2026-08-08
domain: kdo-infrastructure
related:
  - task_20260808_wangyuyan-feature-thinking-w3w4
---

# 配置层三坑沉淀：Hermes 老顽童 × 教练 Agent 自我迭代闭环

> 触发：欧阳锋转发教练 Agent 自主迭代案例（#252 试点意外收获）。教练 Agent 闭环 = 发现问题 → 诊断根因 → 修复 → 沉淀为知识 → 注册 → 下次绕开。王语嫣已做自我对照（切 smart 模式 + 路径 + SOUL.md 过时）。本文是老顽童对照自己的 config.yaml + SOUL.md 的诚实诊断。

## 一、我的 config.yaml 现状（对照教练 Agent 的坑）

| 配置项 | 值 | 与教练 Agent 对比 | 实际影响 |
|:---|:---|:---|:---|
| `approvals.mode` | **manual**（L436） | 同款坑！教练 Agent 因 BLOCKED 切 smart | 飞书网关无交互审批界面 → 需审批的命令 60s 超时被杀；`subagent_auto_approve: false`（L365）→ 子代理跑危险命令同样被卡 |
| `terminal.cwd` | **`.`**（L33） | 教练 Agent 踩过 cwd 错 → 改 /mnt/c/ | **当前 shell cwd 是 /home/dministrator**（实测 pwd 确认）→ search_files 从 /home/dministrator 递归搜 30_wiki 要跨 /mnt/c 全树 → 超时 |
| `command_allowlist` | **空**（L442） | 无白名单兜底 | kdo 命令未列入白名单 → 若被 manual 拦截无豁免路径 |
| `skills.external_dirs` | 已含 wiki shared skills | ✅ 正常 | — |
| `memory.write_approval` | false | ✅ 正常 | 沉淀无阻 |

## 二、今天实际踩的坑（有证据）

### 坑 1：`python -m kdo` 报 No module named kdo
- **症状**：`python -m kdo pre-submit -f ...` → `No module named kdo`，exit 1
- **根因**：Hermes venv 的 python（`/home/dministrator/.hermes/hermes-agent/venv/bin/python`）没有 kdo 模块。kdo 是独立安装的 `/home/dministrator/.local/bin/kdo`
- **修复**：`which kdo` → 用 `kdo` 命令直接跑 ✅
- **教训**：Hermes 会话里 kdo 类命令必须用 `kdo` 可执行文件，不能 `python -m kdo`

### 坑 2：search_files 搜 30_wiki 超时（60s 被杀）
- **症状**：`search_files(path=30_wiki, pattern=*)` → "Command timed out after 60s"
- **根因**：session cwd = `/home/dministrator`，search_files 从 cwd 递归搜 → 路径跨 /mnt/c 全树，巨慢
- **修复**：显式传绝对路径 `/mnt/c/Users/Administrator/Desktop/wiki/30_wiki` ✅
- **教训**：王语嫣也在踩同一个坑（"search_files 搜 30_wiki 多次超时→降级 terminal find"）——**根因是 cwd，不是命令本身**

### 坑 3：queue_transition.py 无法定位任务（O-3 已知）
- **症状**：`queue_transition.py claim 251` → "任务 251 不在生产队列中"（任务明明在队列 L494）
- **根因**：production-queue.md 存在编码混排（GBK/UTF-8 乱码），脚本按 UTF-8 解析定位失败。已知 O-3（多任务已标注"手动终审：queue_transition被拦+O-3"）
- **修复**：手动 patch 队列 + 任务单标注 ✅
- **教训**：队列文件编码是基建债，需黄药师修复（#218 已知 O-3）

## 三、请求修复（写 60_feedback = 老顽童职责内）

| # | 请求 | 建议方案 | 受益 |
|:---:|:---|:---|:---|
| 1 | `terminal.cwd` 固定为 wiki | `cwd: /mnt/c/Users/Administrator/Desktop/wiki` | 根治 search_files 超时 + 免每次 cd |
| 2 | 评估飞书网关下 approvals.mode | 至少把 kdo 命令加入 `command_allowlist` | 避免 kdo 命令被 manual 拦截超时 |
| 3 | queue_transition.py 编码修复 | 队列文件统一 UTF-8 或脚本加编码检测 | 恢复自动化队列流转（O-3 闭环） |
| 4 | SOUL.md 过时信息更新 | 运行位置 tmux claude → Hermes 飞书；路径格式 Windows → /mnt/c/ | 新会话不误导 |

## 四、自我迭代承诺（老顽童版）

1. **不再"忍一忍绕过"**：工具卡顿/超时 → 先查配置层（approvals.mode / cwd / allowlist），再怀疑命令
2. **每次踩坑即沉淀**：坑 → corrections 文件 + memory，一次沉淀永久受益
3. **配置类问题显式请求**：写 corrections → 欧阳锋/黄药师评估，不沉默
4. **验证闭环**：下次同类问题 → 查 corrections/memory → 不重复踩
