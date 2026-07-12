# #168A 图谱孤立团治理方案（黄药师 A 段）

> 送欧阳锋签审 · 2026-07-13

## 三件事的范围

### 子任务 1：OCR 飞地 184 卡移出图谱扫描路径

**现状**：`30_wiki/raw/ocr/` 下 184 张 OCR 原始素材卡。虽然已从主目录移出，但 `kdo_lint.py` 的扫描路径（`30_wiki/` 全量 rglob）仍然会扫描它们——导致 OCR 卡之间的交叉引用持续产生 F2 BROKEN LINK 噪音（上次清理后 31 条残留即源于此）。

**方案**：在 `kdo_lint.py` 的 `lint()` 函数中，将 `raw/` 目录加入排除列表（与已有的 `_archive` 同级过滤）。OCR 文件本身不移动——它们已在正确位置，只是 lint 不应该扫描它们。

**实施**：
```python
# kdo_lint.py lint() 函数中
md_files = [f for f in target.rglob("*.md") 
            if "raw" not in f.parts 
            and "_archive" not in f.parts]
```

**验收**：全量 lint 中不再出现 `30_wiki/raw/ocr/` 路径的任何错误。

**风险**：排除后，OCR 卡之间如果确实有需要修复的引用会被静默。但 OCR 卡本身是 `trust_level=low` 的原始素材，不应进入图谱——这是 S1/S2 已确定的架构决策。

---

### 子任务 2：ai-saas 命名三变体合并

**现状**：domain 字段存在变体（待脚本跑确，推测为 `ai-saas` / `AI-SaaS` / `ai_saas` 等）。187 张卡受影响。导致同域卡片在图谱中被识别为不同域。

**方案**：全库扫描 domain 字段，将所有 ai-saas 变体统一为 `ai-saas`（小写连字符，与 KDO domain 命名规范一致）。

**实施**：
1. 脚本扫描全库 domain 字段
2. 匹配所有 case-insensitive 的 ai-saas 变体（`AI-SaaS`、`ai_saas`、`Ai-Saas` 等）
3. 替换为 `ai-saas`
4. Dry-run 出 diff → 欧阳锋确认 → apply

**验收**：全库 domain 字段中不再出现 ai-saas 的非标准变体。

---

### 子任务 3：pending_unknown 占位 199 条处置

**现状**：~1472 处 `pending_unknown` 出现（在 frontmatter 的 source_refs/domain/query_triggers/prerequisites 等字段中）。这是历史遗留——早期批量建卡时的占位符，从未被清理。

**处置策略**（分层，不是一刀切）：

| 出现位置 | 处理方式 | 理由 |
|:---|:---|:---|
| `source_refs: - pending_unknown` | **摘**（移除该条目） | 无实际来源，挂着是噪音；若移除后 source_refs 为空则卡片降级为 draft |
| `domain: - src_unknown` | **摘**（移除该条目，保留其他有效 domain） | 占位无信息量；若摘后 domain 为空则标注 |
| `query_triggers: - src_unknown` | **摘**（移除该条目） | 无实际触发场景，挂着影响检索 |
| `prerequisites: - src_unknown` | **摘**（移除该条目） | 无实际前置依赖 |

**不处置的**：
- 正文中的 `pending_unknown` / `src_unknown` — 这是内容层问题，应由老顽童在生产中逐步补全
- `source_context: "KDO internal record"` — 已由黄药师事故回修确认，属合法标记

**实施**：
1. 脚本逐卡扫描 frontmatter
2. 识别 pending_unknown/src_unknown 条目
3. 按上表分层处置
4. Dry-run → 欧阳锋确认 → apply
5. 对 source_refs 被清空的卡，status 降级为 draft

**验收**：frontmatter 中 pending_unknown/src_unknown 条目归零；降级卡清单送欧阳锋复核。

---

## 执行顺序与依赖

```
子任务 1（OCR排除）→ 子任务 3（pending_unknown）→ 子任务 2（ai-saas合并）
```

子任务 1 是基础设施变更，先做可以立刻消除 31 条 OCR 噪音。子任务 3 体量最大（~1472 处），子任务 2 最轻量。

三个子任务互不阻塞，可顺序执行。全部完成后 `kdo_lint --baseline` 更新基线。

---

## 签审请求

欧阳锋请确认：
1. OCR 排除方案（子任务 1）是否认可 `raw/` 目录加入 lint 过滤的架构决策
2. pending_unknown 分层处置策略（子任务 3）的"摘/不摘"边界是否认可
3. ai-saas 统一为 `ai-saas` 的命名规范（子任务 2）

签审通过后黄药师按上述顺序执行。

---

*黄药师 · 2026-07-13*
