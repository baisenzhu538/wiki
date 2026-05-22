---
title: "Wiki 健康度全面分析 2026-05-23"
type: "assessment"
created_at: "2026-05-23T00:00:00+00:00"
audience: ["用户", "欧阳锋"]
domain: "master"
---

# Wiki 健康度全面分析 2026-05-23

## 总览

| 维度 | 当前值 | 健康等级 | 趋势 |
|------|--------|---------|------|
| 卡片总数 | 366 | — | — |
| 总 wiki 页数 | 408 | — | — |
| 源文件 | 295 source / 417 raw | 黄 | 122 raw 未摄入 |
| 收件箱 | 590 文件 | 红 | 积压严重 |
| Artifact 质量 | 28 产物, 75 失败 | 红 | 结构性缺失 |
| Graph RAG | 406 节点 / 1252 边 | 绿 | 运行正常 |
| KDO 测试 | 373 passed, 1 skipped | 绿 | 全绿 |
| OCR 卡 | 136 张, 全部 enriched | 黄 | 第一遍过但结构弱 |

---

## 一、卡片结构健康度（致命问题：过半卡片是孤岛）

### 1.1 卡片结构分层

```
research (最低层)                           178  (49%)  ← 仅摘要+源引用，无推理结构
pan-product-upgraded (CB·Critique·FG·Syn)   97  (27%)  ← 全结构，高价值
standard-concept (Constraints·Critique·Syn) 71  (19%)  ← 较完整
standard-concept (旧版 Condense·Critique)   20  ( 5%)  ← 缺 Synthesis
```

**解读**：将近一半卡片（178 张）处于 "research" 最低结构层级——只有摘要和源引用，没有 Critique（质疑评估）和 Synthesis（对标连接）。这类卡片本质上是"已归档但未编译"的原始笔记，不是可复用的知识资产。

### 1.2 孤岛问题（189/366 卡片无人链接）

| 指标 | 数值 |
|------|------|
| 被至少一张其他卡片链接 | 177 (48%) |
| 完全无入链（孤岛） | **189 (52%)** |
| 反向链接索引 | 552 个 target |

**解读**：超过一半的卡片在知识网络中是"断头路"——没有其他卡片引用它们。这意味着：
- 这些卡片即使有价值，也无法被查询/浏览路径发现
- 知识网络的实际可用直径远小于理论直径
- 大量 OCR 卡片（136 张）均属此类孤岛，它们彼此之间也无链接

### 1.3 OCR 卡片专项

| 指标 | 数值 |
|------|------|
| OCR 卡总数 | 136 |
| 已 enriched | 136 (100%) |
| 缺 Critique 关键词（假设/边界/反转/前提） | ~130+ / 140 |
| 缺 2 个以上外部 wikilink | 136 (全部) |
| Condense 不足 3 条实质性 bullet | 部分 |

**根因**：这些卡最初是用正则表达式而非 LLM 做的第一遍 enrichment（当时 Kimi 端点未配置），内容质量远低于三遍 LLM 编译标准。现在 LLM 已通，可以批量重跑 `kdo enrich --all --llm`。

---

## 二、收件箱危机（590 文件积压）

### 2.1 Inbox 分布

| 目录 | 数量 | 状态 |
|------|------|------|
| `00_inbox/` (顶层) | **233** | 红——应分流到子目录 |
| `00_inbox/ocr_ingest/` | 140 | 待处理 |
| `00_inbox/ideas/` | 112 | 待处理 |
| `00_inbox/科学决策/` | 76 | 批量子目录 |
| `00_inbox/prompts/` | 6 | 低量 |
| `00_inbox/design/` | 5 | 低量 |
| `00_inbox/water-sense/` | 3 | 低量 |
| `00_inbox/links/` | 1 | 低量 |
| `00_inbox/business-research-skill/` | 14 | skill 套装 |
| **合计** | **590** | |

### 2.2 顶层 Inbox 文件类型（233 件）

```
.txt  126   原始文本, 未分类
.png   82   截图, 未 OCR 未分类
.md    14   未分类 markdown
.jpg    6   图片未分类
.webp   4   图片未分类
.zip    1   压缩包
```

**解读**：233 个文件直接散落在 `00_inbox/` 顶层，违反工作空间结构。其中 126 个 `.txt` 和 82 个 `.png` 是最危险的积压——它们甚至没有被放入 `screenshots/` 或 `ideas/` 子目录。这意味着 KDO 的 `capture` 命令没有被严格使用，大量"裸投"文件直接进了 inbox。

---

## 三、Artifact 质量（28 产物，75 失败项）

```
总数:     28
失败:     75 项
警告:     15 项
平均:     2.7 失败/产物
```

### 3.1 失败项分布（典型）

| 检查项 | 典型归属 |
|--------|----------|
| `source_refs` | content/article |
| `definition_of_done` | content/article |
| `feedback_path` | content/article |
| `content_audience` | content/article |
| `content_draft_nonempty` | content/article |

**解读**：大部分 artifact 是在定义质量门之前创建的，缺 source_refs 意味着无法溯源，缺 audience 意味着不知道为谁写，缺 definition_of_done 意味着不知道何时算完成。这些 artifact 的"完工程度"不可验证。

---

## 四、源与知识覆盖

### 4.1 源覆盖

| 指标 | 数值 |
|------|------|
| 原始文件 (10_raw) | 417 |
| 已编译 source (.md) | 295 |
| 未摄入 raw 文件 | 122 (29%) |
| raw 中图片 (png/jpg/webp) | 96 |
| raw 中 HTML/PDF | 2 |

**解读**：122 个 raw 文件尚未被 `kdo ingest` 处理成 source file，其中 96 个是图片——这些可以走 `kdo ocr`（如果 MinerU 可用）或现有 PaddleOCR pipeline 提取为文本。

### 4.2 矛盾追踪

仅 1 条矛盾记录，已标记 resolved。考虑到 366 张卡的规模，矛盾追踪严重不足——要么确实无矛盾（乐观估计），要么矛盾未被捕获（更可能）。

---

## 五、基础设施健康

| 组件 | 状态 | 备注 |
|------|------|------|
| KDO CLI 测试 | 绿 | 373/373 passed, 1 skipped |
| Graph RAG | 绿 | 406 节点, 1252 边 |
| LLM 接入 | 绿 | Anthropic 协议已通, Kimi API |
| `kdo lint` | 黄 | 大量 wikilink 断裂告警 |
| Broken wikilinks | ~150+ WARNINGs | yt-* 系列引用未创建的概念 |
| MinerU 运行时 | 红 | onnxruntime DLL 缺失 |
| Git 状态 | 黄 | kdo/llm.py, ocr.py, cli.py, tests 未提交 |

---

## 六、优先级修复路线

### P0 — 阻塞项（本周）

| 序号 | 行动 | 责任人 |
|------|------|--------|
| 1 | **Inbox 分流**：233 个顶层文件按类型归入 `screenshots/` / `ideas/` / `ai-chats/` | 老顽童 |
| 2 | **136 OCR 卡 LLM 重编译**：`kdo enrich --all --llm`（现在 LLM 已通） | 黄药师 (触发) + 老顽童 (执行) |
| 3 | Git commit：llm.py + ocr.py + cli.py + tests | 黄药师 |

### P1 — 结构债（两周内）

| 序号 | 行动 | 责任人 |
|------|------|--------|
| 4 | **升级 178 张 research 卡**到至少 standard-concept | 老顽童 + 欧阳锋审定 |
| 5 | **补链**：135+ 张 OCR 卡各加 ≥2 个外部 wikilink | 老顽童、洪七公（图卡对应） |
| 6 | 122 个 raw 文件 `kdo ingest`，96 个图片走 OCR 管道 | 洪七公 + 黄药师 |
| 7 | 28 个 artifact 补 source_refs + audience + DoD | Publisher (段王爷) |

### P2 — 系统债（一个月内）

| 序号 | 行动 | 责任人 |
|------|------|--------|
| 8 | 189 张孤岛卡逐步建立入链（优先高价值 research 卡） | 老顽童 |
| 9 | 矛盾追踪审计——主动找出并记录潜在矛盾 | 知识仲裁者 |
| 10 | MinerU 运行时修复（VC++ Redistributable + 模型） | 黄药师 |
| 11 | Broken wikilinks 清理——yt-* 引用需创建或去除 | 老顽童 + 欧阳锋 |

---

## 七、关键风险警示

1. **Inbox 腐烂风险**：590 个文件中有 126 个 `.txt` 和 82 个 `.png` 裸文件——价值未知，可能有用也可能已是噪声。再不加分流，噪声比会不可逆地上升。

2. **孤岛知识风险**：52% 卡片无入链意味着查询 `kdo query` 只能通过语义匹配命中，无法通过结构链（A→B→C）发现——"存在但找不到" = 不存在。

3. **Artifact 空壳风险**：28 个产物中大部分是骨架（draft 为空），投入了创建成本但从未产出价值。要么填充，要么标记废弃。

4. **OCR 卡链路断裂**：136 张 OCR 卡虽然打了 `enriched` 标签，但每个都是独立孤岛——它们来自连续截图的碎片，彼此应该有天然的前后关系，但未建立。

---

*报告由 kdo lint + kdo status + kdo validate + 文件系统扫描自动采集，`
`人工分析撰写。下次评估建议在 P0 项完成后的下一个周日执行。*
