---
title: Config Cascade Debug Skill
type: capability
subtype: skill
status: ready
target_user: 黄药师（Builder）— 诊断"改了配置但没生效"类问题
delivery_channel: local
source_refs: []
wiki_refs: []
definition_of_done:
  - task boundary explicit
  - inputs and outputs explicit
  - tool permissions declared
  - eval cases present
  - feedback path declared
artifact_id: config-cascade-debug-v1
created_at: 2026-05-16
updated_at: 2026-05-16
origin: builtin
---

# Config Cascade Debug Skill

## Capability Type

skill

## Mission

诊断"我改了配置但系统行为没变"类问题。核心原理：**配置不是平铺的——它们有优先级级联（cascade）。你改的那个文件可能被更高优先级的全局配置、缓存、或父进程环境变量静默覆盖。** 本 skill 提供系统性诊断流程，防止在错误方向上反复尝试。

## Target User

黄药师（Builder）或任何遇到"改配置不生效"的 agent。

## 为什么需要这个 Skill

历史上同一模式反复发作三次：

| 事故 | 改了哪里 | 真正生效的是 | 浪费 |
|------|---------|------------|------|
| P-1: Claude Code 切模型 | `.bashrc` / `.profile` / Windows 注册表 | Claude Code 全局设置文件 | 整个下午 |
| P-3: Hermes API Key | profile `.env` | `~/.hermes/.env`（全局） + `auth.json` 缓存 | 半天 |
| P-4: Hermes auth.json | `.env` 新 Key | `auth.json` 的 credential_pool 旧缓存 + `last_status: exhausted` | 半天 |

**本质都是同一个 bug**：在 cascade 的低优先级层修改，被高优先级层覆盖。诊断方向错了，试一万次也不生效。

## Inputs

- 用户描述：改了什么、期望什么行为、实际什么行为
- 涉及的工具/服务名称

## Outputs

- 该工具的**配置级联图**（优先级从高到低）
- 当前实际生效的值及其来源（"你现在看到的这个配置，是从哪个文件的第几行读到的"）
- 修复方案（改哪一层、是否需要清缓存）

## 核心概念：配置级联

```
高优先级（覆盖下面）
    │
    ├── Layer 0: 运行时缓存（auth.json credential_pool、session token、内存状态）
    │
    ├── Layer 1: 全局设置文件（~/.claude/settings.json、~/.hermes/.env）
    │
    ├── Layer 2: 父进程环境变量（systemd Environment=、tmux session env）
    │
    ├── Layer 3: 用户级环境变量（~/.bashrc export、Windows HKCU\Environment）
    │
    ├── Layer 4: Profile 级配置（~/.hermes/profiles/<name>/.env）
    │
    ▼
低优先级（被上面覆盖）
```

**关键反直觉点**：你直觉上认为"最具体的配置"（如 profile 级）优先级最高——但通常相反，全局配置和缓存优先。

## Procedure

### Phase 1 — 停止，画级联图

**在动手改任何东西之前**，先回答：

1. 这个工具在哪里读配置？列出所有已知配置文件路径
2. 这些文件之间的优先级是什么？（全局 > profile？缓存 > env？）
3. 当前实际生效的值是什么？（用工具自带的 status/info 命令，或日志反推）

**反模式**：不知道级联结构就改配置 → 大概率改错层 → 不生效 → 再改另一层 → 也不生效 → 多轮试错后放弃或误判。

### Phase 2 — 逐层验证

从高优先级到低优先级，逐层确认"这一层当前的值是什么"：

```
逐层自问：
  □ Layer 0（缓存）：有没有 .json/.cache/.state 文件缓存了旧值？
  □ Layer 1（全局配置）：全局设置文件里写的什么？
  □ Layer 2（父进程）：启动这个进程的父进程传了什么环境变量？
  □ Layer 3（用户级）：用户级环境变量（.bashrc / 注册表）的值？
  □ Layer 4（Profile/局部）：profile 级配置文件的值？
```

**一旦某一层的值与期望不同 → 这就是覆盖源。修复这一层，而非更低层。**

### Phase 3 — 修复 + 验证

1. 在正确的层修改配置
2. 清除该层之上的所有缓存（缓存层会记住旧值）
3. 重启进程/服务
4. 验证：用工具自带的 status/info 确认新值已生效，不只靠"改了文件"

## 已知工具的级联图

### Claude Code

| 优先级 | 层 | 路径 | 备注 |
|:--:|------|------|------|
| **0** | 全局设置 | `~/.claude/settings.json`（Windows: `%USERPROFILE%\.claude\settings.json`） | **最高优先**。改 env var 无效时，检查这里 |
| 1 | 父进程 env | tmux session 的环境变量（session 创建时快照） | `tmux kill-session` 后重建以刷新 |
| 2 | 用户级 env | `~/.bashrc` export / `HKCU\Environment` | 被全局设置覆盖 |
| 3 | WSL Linux export | 仅在 Linux 原生进程中生效，`claude.exe`（Windows PE）不读 | **基本无效，不要依赖** |

### Hermes Gateway

| 优先级 | 层 | 路径 | 备注 |
|:--:|------|------|------|
| **0** | auth.json 缓存 | `~/.hermes/auth.json` → `credential_pool.<provider>[]` | **最高优先**。`last_status: exhausted` 会导致跳过该 Key 不重试 |
| 1 | 全局 .env | `~/.hermes/.env` | Hermes 启动时 `load_dotenv` 加载此文件 |
| 2 | systemd 环境 | `systemctl --user cat <service>` 中的 `Environment=` | 覆盖 .env |
| 3 | Profile .env | `~/.hermes/profiles/<name>/.env` | **不被读取**（Hermes 源码只读全局 .env） |

### 通用启发法（不限于特定工具）

遇到"改了不生效"时，按此顺序排查：

1. **缓存**：有没有 `.json` / `.cache` / `.state` / `.token` 文件存储了旧值？
2. **全局**：有没有全局设置文件（`~/.config/` / `~/.<app>/` / `%APPDATA%`）覆盖了局部？
3. **父进程**：启动脚本 / systemd service 文件 / Dockerfile 有没有注入环境变量？
4. **用户级**：`.bashrc` / `.profile` / `HKCU\Environment` 的值？

## 禁止清单

- ❌ 不知道级联结构就改配置 → 先画级联图
- ❌ 改了一个文件不生效就再改另一个 → 找到覆盖源再改
- ❌ 只改配置文件不清缓存 → 缓存会记住旧值
- ❌ 用 `export` + 重启进程验证 → 很多进程的 env 在启动时快照，`export` 不影响已运行的进程
- ❌ 在 WSL 里 `export` 然后期待 Windows exe 读到 → 跨 OS 边界不传 env

## 关联

- `pitfalls.md` P-1 / P-2 / P-3 / P-4
- `decisions.md` 2026-05-16 (DeepSeek vs Kimi —— 诊断修正)
- [[hermes-gateway-revival|Hermes Gateway Revival Skill]]（Hermes 专项修复）
