---
id: tool-aesthetic-library-builder
title: 审美库采集工具：批量抓取→打分→筛选→生成 DataPack
type: tool
status: draft
author: 老顽童
reviewed_by: pending
confidence: 0.85
trust_level: high
language: zh-CN
created_at: 2026-07-04
updated_at: 2026-07-04
domain:
- yitang
- ai-collaboration
source_refs:
- 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt
- kdo-tools/aesthetic-library-builder.py
related:
- "[[method-yihang-aesthetic-fast-build]]"
- "[[case-yihang-truman-aesthetic-library-practices]]"
- "[[concept-yihang-dual-triangle-core]]"
---

# 审美库采集工具：批量抓取→打分→筛选→生成 DataPack

> **一句话定义**：把 Truman 的审美库建设流程变成可复用的 CLI 工具——指定主题后，从批量抓取、60-99 分打分、精选筛选到生成 Agent 可直接调用的 DataPack，一条命令链完成。

---

## 一、When to Use

需要为某个高价值重复任务建立审美标准时使用。信号：
- 你在做一个需要"判断好坏"的任务（PPT/设计/内容/选品），但没有清晰的判断标准
- AI 在这个任务上的输出质量不稳定，你说不清哪里不好
- 你想让 Agent 自动按你的审美标准筛选/生成内容

---

## 二、子命令

| 子命令 | 做什么 | 输入 | 输出 |
|:---|:---|:---|:---|
| `init <topic>` | 初始化主题工作目录 | 主题名称 | `aesthetic-libs/<topic>/` 目录结构（assets/manifest.json/curated/criteria.md） |
| `collect <topic> --urls/--local` | 批量收集案例 | URL 列表文件 或 本地素材目录 | 下载/复制到 `assets/`，记录到 `manifest.json` |
| `score <topic> --criteria` | 打分筛选 | 评分标准 markdown + LLM API key | `manifest.json` 中每个案例加上 60-99 分数和评分理由 |
| `curate <topic> --top N` | 精选高分案例 | 精选数量 N | 前 N 个高分案例复制到 `curated/` |
| `summarize <topic> --output` | 生成 DataPack | 输出路径 | 可直接被 Agent system prompt 引用的 markdown 文件 |

---

## 三、完整命令链示例

为"商业培训 PPT"建立审美库：

```bash
# 1. 初始化
python kdo-tools/aesthetic-library-builder.py init ppt-commercial-training

# 2. 批量收集（从 URL 列表 + 本地截图目录）
python kdo-tools/aesthetic-library-builder.py collect ppt-commercial-training \
  --urls ppt_urls.txt --local ./raw_ppt_screenshots

# 3. 打分（用评分标准文件 + LLM API）
python kdo-tools/aesthetic-library-builder.py score ppt-commercial-training \
  --criteria criteria/ppt-scoring.md

# 4. 精选 Top 50
python kdo-tools/aesthetic-library-builder.py curate ppt-commercial-training --top 50

# 5. 生成 Agent 可用 DataPack
python kdo-tools/aesthetic-library-builder.py summarize ppt-commercial-training \
  --output ./data_packs/ppt-aesthetic.md
```

---

## 四、输出物

| 输出 | 路径 | 用途 |
|:---|:---|:---|
| 原始素材池 | `aesthetic-libs/<topic>/assets/` | 所有收集的案例 |
| 打分清单 | `aesthetic-libs/<topic>/manifest.json` | 每个案例的评分+理由 |
| 精选库 | `aesthetic-libs/<topic>/curated/` | 高分案例 |
| DataPack | `data_packs/<topic>-aesthetic.md` | Agent system prompt 可引用 |

---

## 五、依赖

- Python 3.x + `requests`, `beautifulsoup4`, `pillow`
- LLM API key（DeepSeek 或 OpenAI，用于自动打分）
- 打分需要评分标准文件（`--criteria`），否则用默认 60-99 标尺

---

## 六、失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| **素材池太窄** | 只收集了 10-20 个案例就打分 | 用 `collect` 多来源扩量——Truman 做图片审美时抓了 5161 张 |
| **只看最好的** | 审美库里全是预算无限级的案例 | 在 `criteria.md` 中定义成本线，打分时按成本线分级 |
| **建完不用** | 审美库建好了但 Agent/团队没有引用 | 用 `summarize` 生成 DataPack，直接写入 Agent system prompt |
| **从不更新** | 审美库半年没更新 | 每个项目结束后用 `collect` 追加新案例 |

---

## 七、Checklist

1. [ ] 主题是否拆到了足够细的颗粒度（不是"设计审美"而是"商业培训 PPT 的封面设计审美"）？
2. [ ] 评分标准文件是否定义了目标、人群和成本线？
3. [ ] 素材池是否 ≥50 个案例？
4. [ ] 每个案例是否有 60-99 分数 + 评分理由？
5. [ ] 精选后的案例是否能说出"90 分 vs 60 分的 3 条具体差异"？
6. [ ] DataPack 是否可被 Agent system prompt 直接引用？

---

## Action Triggers

| 触发场景 | 第一个动作 |
|:---|:---|
| 要在新领域做高质量 AI 协作 | `init <topic>` → `collect` → 一个晚上跑完四步 |
