---
title: "Architect 审查：老顽童批量 OCR 处理"
type: "assessment"
subject: "老顽童 (Producer)"
reviewer: "欧阳锋 (Architect)"
status: "needs-fix"
created_at: "2026-05-22T00:00:00+00:00"
updated_at: "2026-05-22T00:00:00+00:00"
target: "批量 OCR 处理管线 — 655 张图 → OCR → ingest → enrich → index rebuild"
---

# Architect 审查：老顽童批量 OCR 处理

## 结论：**C** — 管线能跑，但质量门被整体绕过，产出污染严重。

**待洪七公交叉审查确认。**

---

## 一、规模数字

| 维度 | 数据 |
|---|---|
| 变更文件 | **488 files**, +29,281 / -202 lines |
| OCR 概念卡片 | **140 张** `30_wiki/concepts/ocr-*.md` |
| 新建源文件 | **155 个** `10_raw/sources/src_20260522_*.md` |
| 源注册表 | **7,675 行**（+2,170 行） |
| 自动反馈 | **841 个** `60_feedback/auto/` 文件（其中 171+ 为本日新增） |
| 非 OCR 草稿卡 | ~10 张（business-analysis、design-ai-image-generation 等） |
| 测试 | kdo test suite: 373/373 通过 |

---

## 二、三个致命问题

### 🔴 P0：源注册表严重污染

`90_control/source-registry.yaml` 被注入大量垃圾条目：

```yaml
# 设计讨论录音碎片被当成独立 source
title: "那今天不会。"
title: "在设计小伙伴的反馈还挺好的。"
title: "值班主"              # 出现 3 次——截断的录音识别

# YAML frontmatter 分隔符被当成标题
title: "---"                 # 出现 27 次
```

搜索不足 15 字符的 title 有 **数百条**。批量 ingest 没有做：
- 最低标题长度过滤（应 ≥4 汉字）
- YAML 标记符拒收（`---`、`...` 等）
- 语义合理性验证

### 🔴 P0：130/140 张卡片虚假标记 "enriched"

抽样三张：

| 卡片 | status | Reusable Knowledge | Open Questions |
|---|---|---|---|
| [[ocr-一堂y模型-科学成事道理.md]] | `enriched` | `TODO` | `TODO` |
| [[ocr-审美提升的层级.md]] | `enriched` | `TODO` | `TODO` |
| [[ocr-预判模型.md]] | `draft` | `TODO` | `TODO` |

**130 张卡片 frontmatter 标注 `enriched`，但 body 中 Reusable Knowledge / Open Questions 全是 `TODO` 占位。**

`kdo enrich` 填充了模板骨架（标题、source_refs、管道免责声明），但**没有做任何实际知识提取**。标注 "enriched" 是 false positive——这些卡片只是 OCR 原文 + 公式化占位，未经三步编译法处理。

### 🟡 P1：自动反馈洪水

`60_feedback/auto/` 有 841 个文件，主流是 `*-unenriched-wiki-page-*`。`kdo enrich` 的 lint 检测到"未富集"卡片后自动生成反馈——但卡片本身就是 enrich 出来的，形成反馈闭环噪声。卡片刚创建未富集是正常状态，不是缺陷。

---

## 三、正面发现

- **OCR 原始提取质量 OK**：PaddleOCR 确实从图片中提取了可读中文。`ocr-预判模型` 的 N 要素/雷达图/Checklist 三层结构提取准确。
- **管线自动化跑通了**：655 张图 → OCR → ingest → enrich → index rebuild 全链路没有崩溃。
- **源文件格式规范**：`10_raw/sources/` 下文件 frontmatter 完整，`source_refs` 双向链接正确。
- **测试没挂**：373/373 通过。
- **原始 OCR 文本有沉淀价值**：图片中的知识已被提取为可检索文本，这是正向积累——问题出在包装层（status 标注、注册表条目），不是核心内容。

---

## 四、改进要求

| 优先级 | 问题 | 要求 |
|---|---|---|
| **P0** | 源注册表污染 | 加最小标题长度过滤（≥4 汉字）、拒收 YAML 标记符（`---`、`...`） |
| **P0** | enrich 假阳性 | `kdo enrich` 只有在确实填充了 Reusable Knowledge / Open Questions 时才改 status 为 `enriched`；只填骨架的不改 |
| **P1** | 反馈洪水 | `unenriched-wiki-page` 自动反馈逻辑修正：卡片创建 24h 内未富集是正常状态，不应触发反馈 |
| **P2** | 卡片命名 | `ocr-` 前缀在概念卡里没有语义——累积到一定数量后建议合并到已有卡片或用 `kdo route` 判断是否值得独立成卡 |

---

## 五、判词

> 老顽童把管线造出来了，能跑，速度也够。但"跑通"之后没有回头检查"跑对了没"——注册表被 YAML 标记符和录音碎片填满，130 张卡谎报 enriched。这不是技术问题，是质量门禁被绕过了。
>
> **修完 P0 两项后升 B+，不改就是 C。**

---

## 六、待洪七公交叉验证

以下点请洪七公从视觉处理视角验证：

1. OCR 提取的文本与 140 张原图的视觉信息差距有多大？（表格结构、层级缩进、高亮标记是否丢失？）
2. `deep-image-parser` 的 prompt 模板在这些图片上能比 PaddleOCR 多还原多少结构？
3. 哪些 `ocr-*` 卡片值得用 deep-image-parser 重做？
4. 源注册表污染的 root cause 是 ingest 逻辑缺陷还是批量脚本的 input parsing bug？

---

*欧阳锋 (Architect) · 2026-05-22*
