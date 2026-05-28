---
title: "黄药师：Sprint 4 — 数据卫生批量修复"
assigned_to: "黄药师 (Builder)"
priority: "P0"
created_at: "2026-05-28"
reviewer: "欧阳锋"
status: "completed"
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

## ⚡ 欧阳锋答疑（2026-05-28）

### Q1：`kdo lint` 缺 `--missing-frontmatter` / `--mixed-format` flag → 选 A 路还是 B 路？

✅ **批准 A 路**——写独立脚本修复，不新增 kdo CLI flag。

理由：Sprint 4 的目标是修数据，不是开发 CLI。新增 flag 放到以后。
S4-2 和 S4-3 复用 S4-1 的独立脚本模式（`90_control/s4_*.py`）。

### Q2：B 类断链（330 条目标不存在）怎么处理？

✅ **批准选项 3**——标记 ⚠️ 不动。

理由：选项 1 丢信息（以后建页面时链接已失），选项 2 造垃圾骨架。记下高频目标列表以后评估是否需要补页。

### Q3：验收阈值确认——B+C 类不计入 <10？

✅ **确认**。验收时：
- A 类（可自动修复 83 条）→ 修复后 0
- B 类（目标不存在 330 条）+ C 类（乱码 38 条）→ 标记 ⚠️，不计入 <10 计数
- 最终 `kdo lint --broken-links` 报告中"可修复"类为 0 即通过

---

## 勘误

原任务文件写 `kdo lint --broken-links` / `--missing-frontmatter` / `--mixed-format`——**这些 flag 不存在**。黄药师已确认。S4-1/S4-2/S4-3 全部用独立脚本（`90_control/s4_*.py`）。

---

## 执行顺序（严格，不跳步）

## 黄药师 C-10 进度确认

你的 C-10 Step 1（单卡 dry-run）✅ 正确。3 张试点候选也选得好——低风险、非 OCR、链接少。
**批准 Step 2：对这 3 张卡执行写入，然后让我确认。**

3 张试点：
1. `yt-unit-model-ai-assisted.md` L170: `ai-innovation` → `ai-partner`
2. `yt-decision-consensus-iceberg.md` L339: `meeting-design` → `scientific-decision`
3. `yt-decision-habit-shift.md` L379: `team-building` → `team-knowledge`

### S4-1：断链批量修复（~45min）

**实测数据**（黄药师已扫）：5463 条链接，断链 413 条。
- **A 类**（可自动修复）：83 条 / 20 个唯一目标
- **B 类**（目标不存在）：330 条 / 101 个唯一目标 → ⚠️ 不动
- **C 类**（编码乱码）：~38 条 → ⚠️ 不动

**做法**：
1. C-10 三步曲：单卡 dry-run ✅ → 3 张试点（已选好）→ 欧阳锋确认 → 批量 54 个文件
2. A 类修复用 difflib.get_close_matches(cutoff=0.75)，**但你 flag 的风险成立——自动匹配可能指向语义不相关页面。**
   - **追加安全阀**：修复前打印 `[当前] → [修复后]` 对照表，人工确认后再批量
3. B+C 类标记 ⚠️，不动

**验收**：
- A 类 83 条全部修复
- 0 条假修复
- 3 个试点案例可复现

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
| 1 | A 类断链 83 条全部修复，0 假修复 | `90_control/s4_scan_broken_links.py` 复查 |
| 2 | frontmatter 缺失数 <20 | `90_control/s4_scan_frontmatter.py` |
| 3 | 新旧格式并存卡 <10 | `90_control/s4_scan_mixed_format.py` |
| 4 | `kdo validate --v15` 不降级 | 0 Failed |
| 5 | C-10 铁律未被跳过（dry-run + 试点记录可查） | 审查 |

## 不做

- **不做** Sprint 5（暂缓，等 Sprint 4 完成后再议）
- **不做** 重构 validate/gate 架构（Sprint 5 范围）
- **不做** 非数据卫生的 CLI 功能开发

---

## 欧阳锋审查意见（2026-05-28）

### 验收结果

| # | 验收项 | 目标 | 实测 | 判定 |
|:-:|:------|:---:|:----:|:----:|
| 1 | A类断链修复 | 83→0 | **83→0** ✅ 0假修复 | ✅ **PASS** |
| 2 | frontmatter 缺失 | <20 | **245→0** ✅ | ✅ **PASS** |
| 3 | 新旧格式并存 | <10 | **134→0** ✅ | ✅ **PASS** |
| 4 | `kdo validate --v15` | 0 Failed | **0 Failed** ✅ 219P/160W | ✅ **PASS** |
| 5 | C-10 铁律 | Step 2→3 | 3试点→批量54文件，流程完整 | ✅ **PASS** |

### 签发

> **Sprint 4：PASS ✅**
>
> 三个子任务全部完成，所有验收指标达标。A类断链83→0，frontmatter 245→0，新旧格式134→0。v1.5验证0 Failed。C-10铁律未被跳过。
>
> **Sprint 5（Validate→Ship 闭环）可启动。** 建议等当前老顽童/洪七公管线完成后评估 Sprint 5 优先级。

*欧阳锋 · 2026-05-28*
