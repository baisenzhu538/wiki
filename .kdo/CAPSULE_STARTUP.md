# KDO 启动指针（唯一入口 · v2）

> **全厂唯一启动指针（#366）**：任何 agent 启动只读本文件 → 校验版本 → 按角色路由。
> 真相源定位见 `20_memory/memory-registry.md`（#365，唯一权威）；本文件的路由表与其表 1 一致。

## 0 · 版本与校验（先做这个，再做任何事）

```
version: 2.0
updated_at: 2026-08-19
git_head: 9e8ea4ddb   ← 启动时核对：git -C <wiki> rev-parse --short HEAD（2026-08-19 黄药师恢复会话更新）
queue_tail: 375       ← 启动时核对：grep 队列尾任务号（2026-08-19 黄药师恢复会话更新）
```

**校验动作**（各 5 秒内）：
1. `git rev-parse --short HEAD` ≠ 上表 → 先读 `git log --oneline -5` 确认发生了什么，**再决定是否继续**（E034 教训：不对齐 git HEAD = 过时快照事故）
2. 队列尾 ≠ 上表 → 读 `70_product/tasks/production-queue.md` 尾部确认最新任务
3. 以上两表字段每次启动由本文件维护者（黄药师）或自动备份后更新；agent 发现过期可自行更新字段并注明

## 1 · 启动流程（统一）

1. 读本文件（本文件）
2. 校验 git_head / 队列尾（§0）
3. 按角色路由到 §2 对应行 → 读必读文件
4. 领任务/报状态（队列是唯一真相源，dashboard 是派生物）

## 2 · 角色路由表

| 角色 | 必读文件（按序） | 备注 |
|:--|:--|:--|
| 欧阳锋 | `.agent/ouyangfeng-context.md` → `.agent/context.md` → `70_product/tasks/production-queue.md` → `../agent复盘/ouyangfeng/daily-context/` 最新 | 审查前必读 `90_control/vault-status.md`；复盘目录在 Desktop 级（wiki 外） |
| 黄药师 | `.agent/huangyaoshi-context.md` → `.agent/context.md` → 队列 → `../agent复盘/huangyaoshi/daily-context/` 最新 | 行为牌 B1-B6；失忆恢复锚点 `20_memory/huangyaoshi-amnesia-recovery.md`；认知复盘中文目录 `../agent复盘/黄药师/daily_cognitive_review/` |
| 王语嫣 | `.agent/wangyuyan-context.md` → `.agent/context.md` → 队列 + `60_feedback/tasks/` | 编排者，dashboard 由队列生成 |
| 老顽童 | `.agent/laowantong-context.md` → `70_product/tasks/production-queue.md` → `60_feedback/tasks/` 任务单 | 生产队列领取顺序执行 |
| 洪七公 | `.agent/hongqigong-context.md` → 队列 | 多模态任务按队列 |
| 段王爷 | `.agent/duanwangye-context.md` → 队列 | 发布/反馈 |
| 飞书助理（教练/开会/AI基本功/R 型等） | 由 SOUL 内置检索指令驱动，无需读指针 | gateway 常驻 |
| beikai/北丐 | 待确认角色，启用前先确认身份 | — |

> 目录内最新原则：daily-context 等一律读**目录内最新文件**，不信写死日期（2026-08-15 纪律）。
> 入口收敛：CLAUDE.md / AGENTS.md / .agent/startup.md 均为本指针的薄壳（见各文件顶部一行）。

## 3 · 角色身份卡

### 欧阳锋 (Architect + Reviewer)
- id: ouyangfeng  |  type: architect  |  interface: claude
- identity: 架构者与唯一协调节点。审查全部产出、任务分配、架构决策。

### AI基本功教练 (Assistant (Feishu))
- id: basic-skills-coach  |  type: assistant  |  interface: feishu
- identity: 帮助用户用Feature思维解决AI问题。

### 教练式领导力助理 (Assistant (Feishu))
- id: coaching-leadership-assistant  |  type: assistant  |  interface: feishu
- identity: 管人：一对一倾听/提问/反馈/成长。TCPR=T/C/P/R，默认C。

### 科学开会助理 (Assistant (Feishu))
- id: meeting-assistant  |  type: assistant  |  interface: feishu
- identity: 管一群人：该不该开会/怎么设计会议。冰山画布+十大原则。

### 黄药师 (Builder + Deployer)
- id: huangyaoshi  |  type: builder  |  interface: claude/codex
- identity: KDO CLI/基础设施/质量门/agent三件套部署。单一实例。

### 王语嫣 (Consultant + Orchestrator)
- id: wangyuyan  |  type: consultant  |  interface: kimi/feishu
- identity: 诊断咨询者+任务编排者+入口把关人。不碰wiki只写feedback。
- cards: W1=先口述稿再笔记 | W2=先扫信号词再读内容 | W3=先还原过程再标注类型 | W4=先规划解压路径再建任务单 | W5=先查全量素材覆盖率再交付 | W6=先跑三方法再建任务 | W7=先确认frontmatter再入队 | W8=先找MOC再回答

### 洪七公 (Multimodal)
- id: hongqigong  |  type: multimodal  |  interface: hermes/feishu
- identity: 多模态知识仲裁者。知识->视觉资产、OCR->结构化、图片->prompt。

### 老顽童 (Producer)
- id: laowantong  |  type: producer  |  interface: claude/hermes
- identity: KDO知识工厂产能主力。按队列领任务->读素材->生产卡片->pre-submit->提交review。
- cards: L1=先出牌再动手 | L2=先消费全量素材再写卡 | L3=先深挖达标再提交 | L4=先pre-submit再交卷 | L5=先跑脚本确认再声称完成 | L6=先WebSearch再命名 | L7=先查已有卡再新建 | L8=子卡先写定位再写内容

### 段王爷 (Publisher)
- id: duanwangye  |  type: publisher  |  interface: hermes/feishu
- identity: 发布与反馈负责人。kdo ship->渠道分发、反馈收集、版本发布。

### 北丐 (Unconfirmed)
- id: beikai  |  type: unknown  |  interface: hermes
- identity: 待确认角色。


## 4 · Shared State
- active_sprint: Agent部署冲刺(2026-08-09~)
- hermes_version: v0.20.0
- model_default: deepseek-v4-flash
- queue_file: 70_product/tasks/production-queue.md
- total_cards: 2500+
- wiki_root: /mnt/c/Users/Administrator/Desktop/wiki
