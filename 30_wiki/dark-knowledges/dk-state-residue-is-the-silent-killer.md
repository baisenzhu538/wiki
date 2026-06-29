---

id: dk-state-residue-is-the-silent-killer
title: 状态残留是自动化系统里最隐蔽的 bug
type: dk
dark_knowledge_type: cross-domain-pattern
status: enriched
domain:
- master
- kdo
- ai-collaboration
source_person: KDO 团队复盘
source_context: 第27节master系统暗知识精修：P-1/P-2/P-3/P-6/P-14/F-3 共同暴露的状态残留问题
source_refs:
- src_unknown
related:
  - [[ai-collaboration-domain-digest]]
  - [[fix-data-curator-parse-bug]]
  - [[pending_unknown]]
  - [[pending_unknown]]
  - [[pending_unknown]]
bridges_to:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
author: 老顽童
reviewed_by: 欧阳锋
review_date: '2026-06-19'
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: src_unknown
  framework_lens: 环境/身份残留
  follow_up_question: 执行环境里是否有上一次登录、缓存、session、token、进程未被清理？
- signal: src_unknown
  framework_lens: 临时状态被重置
  follow_up_question: 消失前是哪一个缓存/session/token/进程在起作用？
- signal: src_unknown
  framework_lens: 僵尸/残留累积
  follow_up_question: 运行结束后，是否有进程、session、临时文件没有被清理？# 状态残留是自动化系统里最隐蔽的 bug
updated_at: 2026-06-28

---

## 原始表述 / 核心洞察

在第 27 节清理 master 系统暗知识时，同一类问题反复出现：

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

**核心洞察**：自动化系统里最隐蔽、最难复现、最耗时的 bug，往往不是逻辑错误，而是"状态残留"——旧的环境变量、缓存、session、token、进程、临时文件没有被清理，导致当前执行的是"别人的上下文"。更危险的是，这些残留通常只在特定组合下触发，换一台机器、重启一次、重新登录一次就消失了，让调试者误以为是"偶发"。

## 原始表述

- src_unknown（待补充来源原话）

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **建立"干净环境"基线**：
   - src_unknown
   - src_unknown
2. **强制清理脚本**：
   - src_unknown
   - src_unknown
3. **使用短命凭证与自动刷新**：
   - src_unknown
   - src_unknown
4. **共享状态文件加锁与版本戳**：
   - src_unknown
   - src_unknown
5. **任务结束后强制清理**：
   - src_unknown
   - src_unknown
6. **把"重启后是否复现"作为诊断标准**：
   - src_unknown

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown

| 失败模式 | 典型症状 | 根因 | 修复方法 |
|:
|:---|:---|:---|
| **环境变量残留** | 模型/endpoint 已经切换，但调用还是旧的 | 旧 env 未被覆盖或清理 | 每次执行前打印并校验关键 env |
| **session 缓存身份** | tmux/screen 恢复后权限/配置不对 | session 文件里保存了旧身份 | 关键 session 不长期存活，重新登录重建 |
| **token 本地过期** | 偶尔报 401/403，重新登录就好 | 缓存 token 未自动刷新 | 每次请求前校验 token 有效期 |
| **僵尸进程抢资源** | 端口被占、token 被耗尽、文件锁不释放 | 进程异常退出未被清理 | 任务结束 finally 清理 + 定期僵尸扫描 |
| **共享状态文件被覆盖** | 指令"已记录"但未执行 | 多进程无锁写 state.json | 文件锁 + 版本号 + 写前校验 |
| **工作目录漂移** | 脚本在新目录下找不到文件 | 上次执行改掉了 cwd 或相对路径 | 脚本开始时显式 cd 到项目根或绝对路径 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
