# Sprint 4 数据卫生 — 黄药师观察与等待指令

> 2026-05-28，黄药师，等待欧阳锋审查

---

## 一、现状测量（与任务文件估算的差异）

| 指标 | 任务文件估算 | 实测 | 差异 |
|------|:----------:|:----:|:----:|
| 总卡片数 | — | 428 个 .md | — |
| 总链接数 | — | 5463 | — |
| 断链（broken） | ~113 | 413 | 多 3.6x |
| 可自动修复 | 未分类 | 83 条（20个唯一目标） | — |
| 目标不存在 | 未分类 | 330 条（101个唯一目标） | — |
| frontmatter 缺失 | ~237 | **待测**（`kdo lint` 无此 flag） | — |
| 新旧格式并存 | ~134 | **待测**（`kdo lint` 无此 flag） | — |

**关键发现**：`kdo lint` 当前版本不支持 `--broken-links` / `--missing-frontmatter` / `--mixed-format` 三个 flag。任务文件假设的接口不存在。已自建扫描脚本（`90_control/s4_scan_broken_links.py`），实测 5463 条链接，断链 413 条。

---

## 二、断链分类（413 条 → 3 类）

### A 类：可自动修复（83 条，20 个唯一目标）

目标页存在但名称有偏差，`difflib.get_close_matches(cutoff=0.75)` 可匹配。例如：

| 频次 | 当前（断链） | 修复为（目标存在） |
|:----:|------|------|
| 26x | `[[yt-decision-pan-product-design]]` | `[[yt-personal-product-design]]` |
| 10x | `[[yt-decision-skill-progression]]` | `[[yt-decision-full-process]]` |
| 6x | `[[yt-decision-deliberate-practice]]` | `[[yt-personal-deliberate-practice]]` |
| 3x | `[[yt-decision-height-method]]` | `[[yt-decision-height-toolkit]]` |
| 3x | `[[yt-decision-question-canvas]]` | `[[yt-decision-canvas]]` |

**风险**：自动匹配可能把链接指向语义不相关的页面。需要逐条审核。已标记为需人工确认。

### B 类：目标确实不存在（330 条，101 个唯一目标）

这些页面从未被创建。高频目标：

| 频次 | 目标 |
|:----:|------|
| 44x | `[[yt-decision-product-launch]]` |
| 21x | `[[yt-decision-project-management]]` |
| 14x | `[[yt-decision-user-research]]` |
| 12x | `[[yt-decision-product-innovation]]` |
| 10x | `[[yt-decision-capability-map]]` |
| 7x | `[[yt-decision-key-hypotheses]]` |

**处理选项**：
- 选项 1：移除 `[[]]`，保留为纯文本（不断链，但失去链接功能）
- 选项 2：创建空骨架占位页（保留链接，以后填充）
- 选项 3：标记 `⚠️` 不动（符合验收标准中"目标不存在不计入脚本修复失败"）

### C 类：编码乱码（~38 条，含在 B 类计数中）

OCR 文件中文件名含乱码 CJK 字符。例如 `[[һ�õ���������13��]]`（17x）。无法知道原始意图，只能标记 ⚠️。

---

## 三、C-10 执行进度

### Step 1 ✅ 单卡 dry-run 完成

| 文件 | 行 | 当前 | 修改为 |
|------|:--:|------|--------|
| `30_wiki/concepts/yt-unit-model-ai-assisted.md` | 170 | `[[yt-decision-ai-innovation]]` | `[[yt-decision-ai-partner]]` |

验证：`yt-decision-ai-partner.md` 存在，`yt-decision-ai-innovation.md` 不存在。上下文吻合。

### Step 2 ⏸️ 等待欧阳锋确认

3 张试点候选（非 OCR，1-3 条可修复链接，风险低）：

| # | 文件 | 修改 | 行 |
|:-:|------|------|:--:|
| 1 | `yt-unit-model-ai-assisted.md` | `ai-innovation` → `ai-partner` | 170 |
| 2 | `yt-decision-consensus-iceberg.md` | `yt-management-meeting-design` → `yt-management-scientific-decision` | 339 |
| 3 | `yt-decision-habit-shift.md` | `yt-management-team-building` → `yt-management-team-knowledge` | 379 |

### Step 3 ⏸️ 等待试点完成后，批量修复余下 54 个文件

---

## 四、需要欧阳锋决策的问题

### Q1：S4-2 和 S4-3 的工具缺口

`kdo lint` 不支持 `--missing-frontmatter` 和 `--mixed-format`。两条路：

- **A 路（快）**：我写独立扫描+修复脚本（类似 S4-1 的做法），不依赖 kdo CLI。估时和任务文件一致（~30min + ~20min）。
- **B 路（稳）**：先给 `kdo lint` 加上这两个 flag（Builder 本职工作），再做修复。估时需增加约 1-2h。

**建议 A 路**。理由：Sprint 4 的目标是修复数据，不是新增 CLI 功能。新增 flag 可以放到 Sprint 5（validate→ship 闭环）。

### Q2：B 类断链（目标不存在）的处理策略

330 条断链目标页面从未被创建。采用哪个选项？

- **选项 1**：移除 `[[]]` 保留纯文本
- **选项 2**：创建空骨架占位页
- **选项 3**：标记 ⚠️ 不动，满足验收标准（"目标不存在不计入脚本修复失败"）

**建议选项 3**。理由：选项 1 丢信息（以后重建页面时链接已失），选项 2 造垃圾骨架。

### Q3：验收阈值确认

任务文件写"断链数 <10"。按当前分类：
- 如果只修 A 类（83→0），剩余 B+C 类 330 条
- 如果 B+C 类不计入（按任务文件括号内说明），则修完 A 类后断链 = 0，< 10 通过

**确认**：验收时 B+C 类不计入 <10 的计数，对吗？

---

## 五、产出文件

| 文件 | 说明 |
|------|------|
| `90_control/s4_scan_broken_links.py` | 断链扫描脚本 V2 |
| `90_control/s4_analyze_broken.py` | 断链分类分析脚本 |
| `90_control/s4-broken-links.json` | 全量断链数据（413 条 + 分类） |
| `90_control/s4-fixable-links.txt` | 可修复链接清单 |

---

*黄药师 · 2026-05-28 · 等待欧阳锋指令*
