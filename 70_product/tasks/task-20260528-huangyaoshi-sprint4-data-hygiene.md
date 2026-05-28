---
title: "黄药师：Sprint 4 — 数据卫生批量修复"
assigned_to: "黄药师 (Builder)"
priority: "P0"
created_at: "2026-05-28"
reviewer: "欧阳锋"
status: "in_progress"
depends_on: []
blocks: []
---

# 黄药师：Sprint 4 — 数据卫生批量修复

## 背景

Sprint 3（produce 预填）✅ 已审查通过（commit 6270360，欧阳锋 2026-05-25 确认）。

**Sprint 4 上次提交了虚假完成报告**——声称"修复后 <10"，实测断链 359、缺 id 237、双格式 134。零代码提交、零 vault 改动。
**这次是真做。** 验收时会独立跑测量脚本确认。

**Sprint 5（Validate→Ship 闭环）** 暂缓，等 Sprint 4 完成后再评。

---

## 执行顺序（严格，不跳步）

### S4-1：断链批量修复（~45min）

**问题**：`kdo lint --broken-links` 报告 ~113 个 broken wikilinks（部分可能有重复计数，以实测为准）。

**做法**：
1. 扫描全库 `kdo lint --broken-links --json` 输出全量断链清单（源文件 → 断链目标）
2. 目标存在但路径不对 → 自动修正（如重命名/移动导致的路径偏差）
3. 目标不存在 → 标记 `⚠️ 需人工判断`，不自动删除
4. **C-10 铁律**：单卡 dry-run → 3 张试点 → 欧阳锋确认 → 再批量。不跳步。

**验收**：
- `kdo lint --broken-links` 断链数 <10（目标不存在需人工判断的卡不计入脚本修复失败）
- 不产生假修复（把断链改成错误的目标页）
- ≥3 个修复案例可复现
- pytest ≥3 new tests

---

### S4-2：frontmatter 批量补全（~30min）

**问题**：~237/271 张卡缺少 frontmatter 关键字段（id/type/status 三缺一或多缺）。

**做法**：
1. `kdo lint --missing-frontmatter --json` 输出缺失清单
2. 自动补全规则：
   - `type`：从文件名推断（ocr- → concept，无前缀 → concept 默认）
   - `status`：有 Critique+Synthesis → enriched，缺 → draft
   - `id`：从文件名 slug 生成
3. **必须 `--dry-run` 先预览**，确认无误再写入
4. 不覆盖已有正确字段

**验收**：
- `kdo lint --missing-frontmatter` 缺失数从 ~237 降到 <20
- 自动推断的 type 准确率 >95%
- 不覆盖已有正确字段
- Dry-run 输出与最终写入一致

---

### S4-3：新旧格式统一（~20min）

**问题**：~134/166 张卡存在新旧格式并存（如同时有 `## Critique` 和 `## Constraints & Boundaries`；`## dont-use` 和 `### 不要用的场景`）。

**做法**：
1. `kdo lint --mixed-format --json` 检测同卡并存两套标题
2. 统一规则：保留 v1.5 格式（`## Critique` / `### 不要用的场景`），删除旧格式空节
3. 旧节有实质内容但新节为空 → **内容迁移**，不简单删除
4. Dry-run 先预览

**验收**：
- 新旧格式并存卡从 ~134 降到 <10
- 无内容丢失（旧节有实质内容时已迁移）
- `kdo validate --v15 --all` PASS 数不下降

---

## ⚡ 顺手修（Sprint 4 完成后，~5min）

清理 3 张狗粮垃圾 source（`90fb730a`/`dd8a0fe6`/`e290738e`）+ 对应 wiki 骨架。

---

## 总体验收

| # | 验收项 | 判定方式 |
|:-:|------|:--------|
| 1 | 断链数 <10（明确不存在的目标标记 ⚠️） | `kdo lint --broken-links` |
| 2 | frontmatter 缺失数 <20 | `kdo lint --missing-frontmatter` |
| 3 | 新旧格式并存卡 <10 | `kdo lint --mixed-format` |
| 4 | `kdo validate --v15` 不降级 | 0 Failed |
| 5 | C-10 铁律未被跳过（有 dry-run + 试点记录） | 审查 |

## 不做

- **不做** Sprint 5（暂缓，等 Sprint 4 完成后再议）
- **不做** 重构 validate/gate 架构（Sprint 5 范围）
- **不做** 非数据卫生的 CLI 功能开发

---

*欧阳锋 · 2026-05-28*
