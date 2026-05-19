---
title: 任务仪表盘
updated: 2026-05-19
---

# 任务仪表盘

> **用法**：Agent 自己来看进度、领任务。批次全部完成后通知欧阳锋统一审查。
> **图例**：✅ 完成 · 🔨 进行中 · ⏳ 排队 · ⚠️ 阻塞

---

## 老顽童（Producer · 飞书 Hermes）

| # | 任务 | 批次 | 状态 | 备注 |
|---|------|------|------|------|
| ① | 补 related 边 | — | ⏳ | 3 条 wikilink + frontmatter relation |
| ② | 双三角文章 v2 | — | ✅ | 用户已通过，关闭 |
| ③ | 管理工具箱 Batch 1（F1+T1+T2） | 工具箱 | ✅ | 全 A。⚠️ T1 typo 未修 |
| ④ | 管理工具箱 Batch 2（T3+T4+T5） | 工具箱 | ✅ | T3 A / T4 A+ / T5 A。⚠️ T3 typo 未修 |
| 🆕 | Anthropic AI 原生初创手册 | 素材编译 | 🔜 | 优先——ingest ✅，wiki 骨架已生成，三步编译 |
| ⑤ | 设计域 → 3 个 Skill | 洪七公+段王爷 | ⏳ | S1+S2+S3 skill 文件 |
| ⑥ | v1.5 全库修复（89 FAILED） | 质量 | ⏳ | 等 scaffold 工具 + 设计域完成后启动 |
| ⑦ | 管理工具箱 Batch 3（T6+T7+T8） | 工具箱 | ⏳ | 穿插在 89 卡修复间隙 |

### 老顽童 — 立即要做

1. **🆕 Anthropic 创始人手册**：三步编译法 → concept 卡（优先）
2. **修两个 typo**（顺手）：T1 Line 90、T3 Line 105
3. **⑤ 设计域 S1**：`AI 生图模型选型指南` skill 文件

---

## 黄药师（Builder · WSL tmux claude）

| # | 任务 | 优先级 | 状态 | 备注 |
|---|------|--------|------|------|
| 1 | `kdo scaffold` | P0 | ✅ | A，17 tests |
| 2 | `kdo clean-transcript` | P1 | ✅ | A，7 tests |
| 3 | `kdo validate --v15 --watch` | P2 | ✅ | A，纯标准库 |
| 4 | `kdo watch` 依赖解耦 | P1 | ✅ | 4 tests |
| 5 | scaffold 插入位置修正 | P2 | ✅ | Critique→CB/Synthesis 间 |
| 6 | `kdo task` 自动化 + dashboard | **P0** | 🔨 | YAML frontmatter + CLI 子命令 |
| 7 | graph rebuild --incremental | P2 | ✅ | 5 tests, --full + incremental |
| 8 | `kdo graph stats` | P3 | ✅ | 4 tests, --json, NOT BUILT |

### 黄药师 — 当前任务

**Task 6**：`kdo task` 自动化（详见 [[70_product/tasks/huangyaoshi-next-tasks.md]]）

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
| 05-19 | 黄药师 | Task 7 graph rebuild --incremental | ✅ |
| 05-19 | 欧阳锋 | 设计域方向调整 | 废弃 D1-D7 → 3 个 Skill |
