---
title: 任务仪表盘
updated: 2026-05-19
---

# 任务仪表盘

> **用法**：欧阳锋审查/Agent 完成任务后更新此表。各任务详细 brief 在对应 agent 的任务文件里。
> **图例**：✅ 完成 · 🔨 进行中 · 🔜 下一个 · ⏳ 排队 · ⚠️ 阻塞

---

## 老顽童（Producer · 飞书 Hermes）

| # | 任务 | 批次 | 状态 | 备注 |
|---|------|------|------|------|
| ① | 补 related 边 | — | ⏳ | 3 条 wikilink + frontmatter relation |
| ② | 双三角文章 v2 | — | ✅ | 用户已通过，关闭 |
| ③ | 管理工具箱 Batch 1（F1+T1+T2） | 工具箱 | ✅ | 全 A。⚠️ T1 typo 未修 |
| ④ | 管理工具箱 Batch 2（T3+T4+T5） | 工具箱 | ✅ | T3 A / T4 A+ / T5 A。⚠️ T3 typo 未修 |
| ⑤ | 设计域 7 张卡 | 设计域 | 🔜 | Step 0 清理 ✅，Step 1 Ingest 可开工 |
| ⑥ | v1.5 全库修复（89 FAILED） | 质量 | ⏳ | 等 scaffold 工具 + 设计域完成后启动 |
| ⑦ | 管理工具箱 Batch 3（T6+T7+T8） | 工具箱 | ⏳ | 穿插在 89 卡修复间隙 |

### 老顽童 — 立即要做

1. **修两个 typo**（5 分钟）：T1 Line 90、T3 Line 105
2. **⑤ 设计域 Step 1**：`kdo ingest` 两份清理后的转录稿 → `10_raw/sources/`

---

## 黄药师（Builder · WSL tmux claude）

| # | 任务 | 优先级 | 状态 | 备注 |
|---|------|--------|------|------|
| 1 | `kdo scaffold` | P0 | ✅ | A，17 tests |
| 2 | `kdo clean-transcript` | P1 | ✅ | A，7 tests |
| 3 | `kdo validate --v15 --watch` | P2 | ✅ | A，纯标准库 |
| 4 | `kdo watch` 依赖解耦 | P1 | ✅ | 4 tests |
| 5 | scaffold 插入位置修正 | P2 | ✅ | Critique→CB/Synthesis 间 |
| 6 | `kdo task` 自动化 + dashboard | **P0** | 🔨 | **优先级提升**——用户要求立即做 |
| 7 | graph rebuild --incremental | P2 | 🔜 | 增量 <5s vs 全量 ~30s |
| 8 | `kdo graph stats` | P3 | ⏳ | 输出合法 + --json |

### 黄药师 — 当前任务

**Task 6（原 Task 8 提前）**：`kdo task` 自动化

要做什么：
- `kdo task dashboard` → 自动扫描所有任务文件 YAML frontmatter，生成此仪表盘
- `kdo task mine` → Agent 查自己的待办
- `kdo task done <id>` → Agent 标记完成
- `kdo task review <id> --verdict A` → 欧阳锋记录审查结论
- `kdo task verify` → 检查所有任务引用的文件/工具是否存在

核心思路：任务文件头部加 YAML frontmatter（结构化状态），CLI 读/写 frontmatter，dashboard 自动聚合。不改现有 Markdown brief 内容。

---

## 洪七公（Multimodal）

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| — | 待激活 | ⚠️ | 任务派发协议待定义 |

## 段王爷（Publisher）

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| — | 待激活 | ⚠️ | 任务派发协议待定义 |

---

## 阻塞项

| 谁 | 什么事 | 卡在哪 |
|----|--------|--------|
| 老顽童 | 两个 typo 没修 | T1 Line 90、T3 Line 105 |

---

## 最近完成

| 日期 | 谁 | 任务 | 结果 |
|------|-----|------|------|
| 05-19 | 黄药师 | Task 5 scaffold 插入修正 | ✅ |
| 05-19 | 黄药师 | Task 4 watchdog 解耦 | ✅ |
| 05-19 | 老顽童 | T5 typo 修复 | ✅ |
| 05-19 | 欧阳锋 | 设计域转录稿清理 | ✅ → `00_inbox/design/cleaned/` |
