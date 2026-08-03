---


id: tool-aesthetic-library-builder
title: 审美库采集工具：批量抓取→打分→筛选→生成 DataPack
type: tool
status: reviewed
author: 老顽?
reviewed_by: ŷ
review_date: 2026-07-04
confidence: 0.85
trust_level: high
language: zh-CN
created_at: 2026-07-04
updated_at: '2026-07-04'
domain:
- yitang
- ai-collaboration
source_refs:
- 00_inbox/人机协作双三?一堂双三角-人机协作模型-口述.txt
- kdo-tools/aesthetic-library-builder.py
aliases:
  - 审美库采集工具
  - DataPack生成
  - 批量抓取
discoverable_by:
  - 审美库采集工具：批量抓取→打分→筛选→生成 DataPack
  - 审美库采集工具
  - 批量抓取→打分→筛选→生成
related:
- "[[method-yihang-aesthetic-fast-build]]"
- "[[case-yihang-truman-aesthetic-library-practices]]"
- "[[concept-yihang-dual-triangle-core]]"
---
# 审美库采集工具：批量抓取→打分→筛选→生成 DataPack

> **一句话定义**：把 Truman 的审美库建设流程变成可复用的 CLI 工具——指定主题后，从批量抓取�?0-99 分打分、精选筛选到生成 Agent 可直接调用的 DataPack，一条命令链完成�?
---

## 一、When to Use

需要为某个高价值重复任务建立审美标准时使用。信号：
- 你在做一个需�?判断好坏"的任务（PPT/设计/内容/选品），但没有清晰的判断标准
- AI 在这个任务上的输出质量不稳定，你说不清哪里不�?- 你想�?Agent 自动按你的审美标准筛�?生成内容

---

## 二、子命令

| 子命�?| 做什�?| 输入 | 输出 |
|:---|:---|:---|:---|
| `init <topic>` | 初始化主题工作目�?| 主题名称 | `aesthetic-libs/<topic>/` 目录结构（assets/manifest.json/curated/criteria.md�?|
| `collect <topic> --urls/--local` | 批量收集案例 | URL 列表文件 �?本地素材目录 | 下载/复制�?`assets/`，记录到 `manifest.json` |
| `score <topic> --criteria` | 打分筛�?| 评分标准 markdown + LLM API key | `manifest.json` 中每个案例加�?60-99 分数和评分理�?|
| `curate <topic> --top N` | 精选高分案�?| 精选数�?N | �?N 个高分案例复制到 `curated/` |
| `summarize <topic> --output` | 生成 DataPack | 输出路径 | 可直接被 Agent system prompt 引用�?markdown 文件 |

---

## 三、完整命令链示例

�?商业培训 PPT"建立审美库：

```bash
# 1. 初始�?python kdo-tools/aesthetic-library-builder.py init ppt-commercial-training

# 2. 批量收集（从 URL 列表 + 本地截图目录�?python kdo-tools/aesthetic-library-builder.py collect ppt-commercial-training \
  --urls ppt_urls.txt --local ./raw_ppt_screenshots

# 3. 打分（用评分标准文件 + LLM API�?python kdo-tools/aesthetic-library-builder.py score ppt-commercial-training \
  --criteria criteria/ppt-scoring.md

# 4. 精�?Top 50
python kdo-tools/aesthetic-library-builder.py curate ppt-commercial-training --top 50

# 5. 生成 Agent 可用 DataPack
python kdo-tools/aesthetic-library-builder.py summarize ppt-commercial-training \
  --output ./data_packs/ppt-aesthetic.md
```

---

## 四、输出物

| 输出 | 路径 | 用�?|
|:---|:---|:---|
| 原始素材�?| `aesthetic-libs/<topic>/assets/` | 所有收集的案例 |
| 打分清单 | `aesthetic-libs/<topic>/manifest.json` | 每个案例的评�?理由 |
| 精选库 | `aesthetic-libs/<topic>/curated/` | 高分案例 |
| DataPack | `data_packs/<topic>-aesthetic.md` | Agent system prompt 可引�?|

---

## 五、依�?
- Python 3.x + `requests`, `beautifulsoup4`, `pillow`
- LLM API key（DeepSeek �?OpenAI，用于自动打分）
- 打分需要评分标准文件（`--criteria`），否则用默�?60-99 标尺

---

## 六、失败模�?
| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| **素材池太�?* | 只收集了 10-20 个案例就打分 | �?`collect` 多来源扩量——Truman 做图片审美时抓了 5161 �?|
| **只看最好的** | 审美库里全是预算无限级的案例 | �?`criteria.md` 中定义成本线，打分时按成本线分级 |
| **建完不用** | 审美库建好了�?Agent/团队没有引用 | �?`summarize` 生成 DataPack，直接写�?Agent system prompt |
| **从不更新** | 审美库半年没更新 | 每个项目结束后用 `collect` 追加新案�?|

---

## 七、Checklist

1. [ ] 主题是否拆到了足够细的颗粒度（不�?设计审美"而是"商业培训 PPT 的封面设计审�?）？
2. [ ] 评分标准文件是否定义了目标、人群和成本线？
3. [ ] 素材池是�?�?0 个案例？
4. [ ] 每个案例是否�?60-99 分数 + 评分理由�?5. [ ] 精选后的案例是否能说出"90 �?vs 60 分的 3 条具体差�?�?6. [ ] DataPack 是否可被 Agent system prompt 直接引用�?
---

## Action Triggers

| 触发场景 | 第一个动�?|
|:---|:---|
| 要在新领域做高质�?AI 协作 | `init <topic>` �?`collect` �?一个晚上跑完四�?|
