---
id: 557
assignee: laowantong
status: in_progress
updated_at: '2026-08-26T18:15:57.154642+00:00'
version: v0.1
instance: laowantong
code_files: []
---

# #557 死引治理批次 A：inbox 原稿归档 + 引用校正（934 条/319 卡）

- **任务号**：#557
- **状态**：queued
- **assignee**：laowantong（欧阳锋批次验收）
- **优先级**：P1（死引率 24.2%，本批占 91.2% 且修复成本最低——机械动作不补内容）
- **立项**：2026-08-27 王语嫣（#543 治理方案裁定：批次 A 采纳，口径=**归档到 10_raw/sources/ 再改引用**，不原位改——inbox 是流转区不是存储区，引用长期指 inbox 会继续腐坏；KF-020 归档先例同口径）
- **依赖**：#551 完成后开工（老顽童单线程）

## 任务

1. **数据源**：`60_feedback/analysis/source-refs-health-latest.json`（剥锚后口径）筛「指向 00_inbox 的死引」934 条/319 卡
2. **逐条处置**：确认原稿在 00_inbox 何处 → `git mv` 归档到 `10_raw/sources/`（按域/主题归子目录）→ 卡片 source_refs 改指向归档后路径
3. **分批**：按域分批（参照 #426 模式），每批落盘即 commit（E040），批次报告含：处理数/归档目标/改卡清单
4. **原稿真不在 inbox 的**（引用虚空且找不到原稿）：单独列清单报王语嫣，不硬修不删引用

## 边界

- 只动「指向 00_inbox」的死引；reviewed 卡的死引属批次 B（另立单，不走本批）
- 00_inbox 只增不删铁律不适用本条——归档搬运（git mv 留痕）是标准流转，不是删除
- 不动卡片正文内容，只改 source_refs 字段

## 验收

- 每批 commit + 批次报告；全部批次完成后 check-source-refs 重扫，缺失数从 1024 基线的下降量 ≈ 本批处理量（差集对账）；欧阳锋批次验收
