# Kimi Code CLI 对 OCR 卡与 yt 成品卡混放的独立判断

**日期**：2026-06-16  
**核实依据**：全库扫描 + frontmatter 分析  
**角色**：独立判断

---

## 一、核实结果

### 1.1 OCR 卡实际分布

| 目录 | OCR 卡数量 | 备注 |
|:-----|:----------:|:-----|
| `30_wiki/concepts/` | **184 张** | 全部 OCR 卡 |
| `30_wiki/dark-knowledges/` | **0 张** | 无 `ocr-` 前缀卡 |
| **合计** | **184 张** | |

> 注：用户提到"1 张在 dark-knowledges/"，经扫描未发现。可能指某张 `dk-` 卡内容来源于 OCR，但按文件名和 frontmatter 标准，OCR 卡均集中在 concepts/。

### 1.2 OCR 卡 frontmatter 特征（统一）

```
trust_level: low  — 100%（184/184）
status: draft     — 100%（184/184）
confidence: ≤0.6  — 100%（184/184）
```

所有 OCR 卡都是**低信任原始素材**，未经过精修。

### 1.3 yt-* 成品卡 frontmatter 特征（对比）

`30_wiki/concepts/` 下 `yt-*` 卡共 **229 张**：

```
trust_level: medium/high/medium-high  — 90%（204/229）
status: enriched/reviewed             — 83%（191/229）
confidence: 0.7-0.9                   — 94%（215/229）
```

是典型的**精修成品卡**。

### 1.4 混合程度

`30_wiki/concepts/` 总卡数 **981 张**：

- OCR 卡：184 张（**18.8%**）
- yt-* 成品卡：229 张（**23.3%**）
- 其他概念卡：568 张（57.9%）

**每 5 张 concepts/ 卡中就有 1 张是 OCR 原始素材**，与精修过的 yt 成品卡无物理隔离。

---

## 二、问题影响分析

### 2.1 检索召回污染（真实存在）

如果 RAG/搜索不根据 `trust_level` 或 `status` 过滤：
- 查询"一堂五步法"时，可能同时召回 `yt-five-step-method.md`（enriched）和 `ocr-一堂-个人修炼-五步法.md`（draft/low）
- AI 拿到低质量 OCR 内容后，可能输出噪声、错误解读、或降低回答置信度
- 用户直接浏览 concepts/ 目录时，184 张 OCR 卡严重干扰可读性

### 2.2 统计和指标失真

- concepts/ 目录被 OCR 卡稀释，外人/新 agent 会误判整个目录质量
- 质量门禁统计中，OCR 卡虽然单独标记，但混入总体后拉低"concepts/ 平均质量"
- Graph RAG 如果把 OCR 卡当普通实体摄入，会引入大量未校验节点和边

### 2.3 生产流程混乱

- 老顽童作为 Producer，在 concepts/ 中找卡时会被 OCR 卡淹没
- OCR 卡本应是"原始素材层"，却进入了"精修知识层"
- 缺少"OCR → 精修 → 升级 → 移入 concepts/"的标准流程

---

## 三、我的独立判断

### 3.1 这不是 P0 危机，但是 P1 结构性问题

理由：
- OCR 卡有统一标记（`trust_level=low`, `status=draft`, `confidence≤0.6`），**可以被过滤**
- 没有 immediate 的数据损坏或 P0 阻塞
- 但长期会污染检索、误导用户、拖慢精修进度

**我的评级：P1（中高）结构性问题，需要规划解决，不必停掉所有其他工作。**

### 3.2 "混在一起"的罪魁祸首是目录边界模糊

KDO 的分层设计理论上应该是：

```
10_raw/        → 原始素材（录音、OCR、截图、文献）
30_wiki/       → 精修知识（concept, framework, tool, case, dk...）
```

但实际操作中，OCR 被直接卡片化后塞进了 `30_wiki/concepts/`，打破了分层。

**这不是某一个人的失误，是 ingestion 流程缺少"原始素材卡该放哪"的规范。**

### 3.3 不能简单删除 OCR 卡

OCR 卡虽然 trust_level=low，但仍有价值：
- 是 Truman/月白/纪浩等 source 的原始记录
- 部分 OCR 卡后续会被精修为正式概念卡
- 删除会丢失原始素材和溯源链

正确做法是**隔离 + 可升级**，不是删除。

---

## 四、解决方案建议

### 方案 A（推荐）：建立 `30_wiki/raw/` 原始素材层

把 184 张 OCR 卡从 `concepts/` 迁移到 `30_wiki/raw/ocr/`。

**优点**：
- 物理隔离原始素材和精修知识
- 搜索/索引可以默认排除 `30_wiki/raw/`
- 保留 OCR 卡，不丢素材
- 未来其他原始素材卡（截图、速记）也有地方放

**缺点**：
- 需要迁移 184 张卡，更新内部链接
- 需要改 `templates.py`、索引扫描路径、graph ingest、validate 范围
- 需要黄药师写迁移脚本并测试

**适合**：中长期根本解决。

### 方案 B（短期快速缓解）：搜索层过滤

不改目录，只在 RAG/搜索/Graph ingest 中默认过滤 `trust_level=low` 或 `status=draft` 的卡。

**优点**：
- 改动小，见效快
- 不破坏现有路径和链接

**缺点**：
- 没有解决目录混乱
- 用户直接浏览 concepts/ 仍然会被 OCR 卡干扰
- 长期会让"concepts/ 里什么都有"的问题更严重

**适合**：立即执行，作为方案 A 的过渡。

### 方案 C（折中）：OCR 卡单独子目录

在 `30_wiki/concepts/` 下建 `concepts/ocr/` 子目录，把 OCR 卡移进去。

**优点**：
- 比方案 A 改动小
- 仍在 concepts/ 命名空间下

**缺点**：
- 子目录增加复杂度
- 没有真正建立 raw/ 分层
- 搜索过滤时还是要依赖 trust_level，不能只靠路径

**适合**：如果担心改动太大，可作为过渡方案。

---

## 五、我的最终建议

**立即执行方案 B + 中期执行方案 A**：

1. **黄药师本周做方案 B**：
   - 在 `kdo query`、`kdo graph query`、搜索索引中默认过滤 `trust_level=low`
   - 提供 `--include-raw` 参数，需要时才包含 OCR 卡
   - 更新 Graph RAG ingest，跳过或单独处理 trust_level=low 的节点

2. **黄药师下周做方案 A 的迁移脚本**：
   - 写脚本把 `concepts/ocr-*.md` 迁移到 `30_wiki/raw/ocr/`
   - 自动更新 `related` 链接、source_refs、index
   - 跑全量 lint 和质量门禁验证

3. **老顽童负责 OCR 卡精修升级判断**：
   - 哪些 OCR 卡值得精修为正式概念卡
   - 精修完成后移入 `concepts/`
   - 不值得精修的保留在 `raw/ocr/`

4. **建立 SOP**：
   - 未来所有 OCR/截图/速记原始素材卡，默认进 `30_wiki/raw/`
   - 只有经过精修、status 升到 enriched/reviewed 后，才进入 `30_wiki/concepts/` 或对应目录

---

## 六、对当前任务的影响

我之前给老顽童排的 E1-E5 任务中，没有专门处理 OCR 混放问题。建议插入：

| 新任务 | 优先级 | 负责人 | 说明 |
|:-------|:------:|:-------|:-----|
| 搜索层过滤 trust_level=low | P1 | 黄药师 | 立即缓解召回污染 |
| OCR 卡迁移到 `30_wiki/raw/ocr/` | P1 | 黄药师脚本 + 老顽童验收 | 中期根本解决 |
| OCR 精修升级判断 | P2 | 老顽童 | 持续进行 |

---

## 七、结论

用户指出的"OCR 卡和 yt 成品卡混在 concepts/"问题**真实存在**，且比单纯数字更严重：
- 184 张 OCR 卡占 concepts/ 的 18.8%
- 会污染检索、误导 AI、干扰生产

但这不是要删除 OCR 卡的理由，而是要**建立原始素材层和精修知识层的隔离**。

我的建议：**短期搜索过滤，中期迁移到 `30_wiki/raw/ocr/`，长期建立 OCR → 精修 → 升级的 SOP。**

---

Kimi Code CLI
2026-06-16
