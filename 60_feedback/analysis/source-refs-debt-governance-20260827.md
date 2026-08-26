# source_refs 死引治理方案（#543 交付 · 报王语嫣裁定）

> 生成：2026-08-27 黄药师 | 数据：`source-refs-health-latest.json`（同日全量扫描，剥行号锚后口径）
> 任务边界：本文件只出方案，不批量修卡；裁定后另立执行单（#426 分批模式）

## 数字基线（剥锚后实测）

- 全库 2878 卡 / 5910 条 source_refs / 文件路径类 4226 条
- **缺失 1024 条（死引率 24.2%）**，污染 8 条（已知模式）
- **行号锚误报挤占量：仅 2 条**（占 0.2%）——08-26 的 1024 口径基本未被锚污染，死引是真实缺失
- 注：域×status 透视中多域卡重复计数，分项合计略大于 1024

## 聚类发现（三条主线）

### ① 指向 00_inbox 的死引 934 条 / 319 卡（91.2%）——修复成本最低

原稿就在 inbox，卡片引了虚空相对路径。修复动作=归档搬运或路径校正，不用补内容。
典型：`30_wiki/personal-os/README.md` 等卡引 `00_inbox/...` 下不存在路径。

### ② reviewed 卡死引 441 条——终审漏项，优先级最高

已终审卡带死引 = 终审时 source_refs 可达性未拦住（预审 SOURCE_REACHABILITY 剥锚 bug 今日才修）。
域分布 Top：management 79 / conversion-rate 69 / ai-collaboration 47 / business-strategy 40 / sales 23。

### ③ 域集中度：business-formula 318 + conversion-rate 204 = 51%

两个域占一半死引，疑似同源批量入库事故（建议治理前先查这两域的入库批次）。

## status 分布

| status | 缺失条数（含多域重复计数） |
|---|---|
| enriched | 506 |
| reviewed | 441 |
| draft | 305 |
| pending_review | 18 |
| stable | 1 |

## 分批治理方案（报裁定）

| 批次 | 范围 | 条数 | 修复动作 | 依赖 |
|---|---|---|---|---|
| A | 指向 00_inbox 的死引（319 卡） | 934 | 归档搬运/路径校正（机械化，成本最低） | 需先定「inbox 原稿归档到 10_raw 还是原位改引用」口径 |
| B | reviewed 卡死引 | 441 | 逐域人工核对（终审漏项，不可纯机器修） | 批次 A 完成后启动，按域拆执行单 |
| C | draft/enriched 长尾 | 余量 | 随各域生产任务顺带治理 | 不专列 |

**附带报裁**：src_id 类引用（`src_YYYYMMDD_xxx`）连 `.kdo/source_id_map.json` 都未注册——是否把「src_id 必须注册」挂进 pre-submit，随本方案一并裁定（任务书边界第 2 条）。

## 例行化（已落地，不等裁定）

- `check-source-refs.py --report-dir 60_feedback/analysis --max-missing 1024 --max-contaminated 8` 已挂 health-check（每日 02:07 kdo-health-daily）
- 报告落盘：`60_feedback/analysis/source-refs-health-latest.{md,json}`（每日刷新）
- 阈值=今日基线，**超基线=新增死引才 FAIL**；治理推进后阈值由王语嫣裁定下调
