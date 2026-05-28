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
| frontmatter 缺失 | ~237 | **245**（240缺id / 5无frontmatter / 3缺type / 1缺status） | ✅ 吻合 |
| 新旧格式并存 | ~134 | **134**（130混用+4纯旧格式） | ✅ 精确 |

**关键发现**：`kdo lint` 当前版本不支持 `--broken-links` / `--missing-frontmatter` / `--mixed-format` 三个 flag。任务文件假设的接口不存在。已自建三套扫描脚本完成全量检测。

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

### Step 2 ✅ 已完成（2026-05-28）

3 张试点卡片已写入，等待欧阳锋审查：

| # | 文件 | 修改 | 行 | 状态 |
|:-:|------|------|:--:|:--:|
| 1 | `yt-unit-model-ai-assisted.md` | `ai-innovation` → `ai-partner` | 170 | ✅ |
| 2 | `yt-decision-consensus-iceberg.md` | `yt-management-meeting-design` → `yt-management-scientific-decision` | 339 | ✅ |
| 3 | `yt-decision-habit-shift.md` | `yt-management-team-building` → `yt-management-team-knowledge` | 379 | ✅ |

### Step 3 ⏸️ 等待试点审查通过后，批量修复余下 54 个文件（80 条可修复链接）

---

## 四、S4-2：frontmatter 缺失详情（245 张卡）

**扫描脚本**：`90_control/s4_scan_frontmatter.py`
**输出**：`90_control/s4-frontmatter-missing.json`

| 问题类型 | 数量 | 说明 |
|----------|:----:|------|
| 缺 `id` 字段 | 240 | 占绝大多数，可自动从文件名 stem 生成 |
| 无 frontmatter 块 | 5 | 需补完整 frontmatter 骨架 |
| 缺 `type` 字段 | 3 | 均可推断为 `concept` |
| 缺 `status` 字段 | 1 | 可根据内容推断（有 Critique+Synthesis → enriched / 缺 → draft） |

**修复策略**：
- `id`：从文件名 slug 生成，不覆盖已有正确 id
- `type`：从文件名前缀推断（ocr- → concept，默认 concept）
- `status`：基于内容检测（有 Critique+Synthesis → enriched）
- 无 frontmatter 的 5 张卡先补完整骨架
- `--dry-run` 先预览，确认无误再写入

---

## 五、S4-3：新旧格式并存详情（134 张卡）

**扫描脚本**：`90_control/s4_scan_mixed_format.py`
**输出**：`90_control/s4-mixed-format.json`

| 类型 | 数量 | 处理方式 |
|------|:----:|------|
| 新旧并存（`## Critique` + `## Constraints & Boundaries`） | 130 | 删除旧格式空节/迁移内容后删除 |
| 纯旧格式（仅 `## Constraints & Boundaries`，无 `## Critique`） | 4 | 重命名为 `## Critique` |

**注意**：旧节 `## Constraints & Boundaries` 在有实质内容但新节为空时 → 内容迁移，不简单删除。

---

## 六、顺手修 ✅ 已完成

3 张狗粮垃圾 source（`90fb730a` / `dd8a0fe6` / `e290738e`）及 source-registry.yaml、log.md 引用已清理。无对应 wiki 骨架页。

---

## 七、需要欧阳锋决策的问题

### Q1：S4-2 和 S4-3 的工具缺口（已自行解决）

`kdo lint` 不支持 `--missing-frontmatter` 和 `--mixed-format`。**已自建扫描脚本完成检测**（`90_control/s4_scan_frontmatter.py` + `90_control/s4_scan_mixed_format.py`）。修复脚本同理走独立脚本路线（A 路），不依赖 kdo CLI。待欧阳锋批准后执行。

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
