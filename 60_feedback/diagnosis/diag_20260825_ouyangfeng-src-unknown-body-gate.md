---
id: diag_20260825_ouyangfeng-src-unknown-body-gate
title: 正文 src_unknown 占位无门禁：2.2 万行存量 + pre-submit 放行盲区
author: 欧阳锋
created_at: '2026-08-25'
type: diagnosis
status: draft
source: "#498 复审观察项重分类（老朱追问触发存量实测）"
---

# 正文 src_unknown 占位：门禁盲区 + 2.2 万行存量

## 现象

#498 复审时发现 graph-rag.md 正文 Critique/Synthesis 残留 11 处 `- src_unknown` 占位，初审记为"内容类观察项"。老朱追问分类标准后实测存量：

- **正文 src_unknown：22,871 行 / 1,524 张卡**（30_wiki 全库，不含 _archive）——超过半数卡的 Critique/Synthesis 等节从未实质填充
- frontmatter src_unknown 5,754 行为接受口径（#391 死路径改 src_unknown 的既定处置），不在本单范围

## 门禁盲区（实证）

`kdo pre-submit -f graph-rag.md` → **PASS**（pre-score 40/100 仅 info 级）——正文 src_unknown 占位无检查项，骨架卡（节标题在、内容全占位）可无障碍通过提审门禁。门禁输出甚至附"修得干净"安慰语，与 11 处占位并置构成误导。

## 根因

1. pre-submit 检查项面向 frontmatter/结构/死链，**正文节内容是否实质填充无检查**（src_unknown 占位/空节/TODO 节均不拦）
2. 历史批量产卡留下的骨架存量（占位先入库、精修后补）无收口任务跟踪——"231 张 draft 精修池"（06-17 口径）之后无全量复扫
3. 我的初审分类错误：把库级存量当单卡缺陷记观察项——分类时必须先做存量实测（一张卡的问题 vs 一类卡的问题）

## 建议方向（R1-R3，王语嫣裁定）

- **R1 门禁补检查项**：pre-submit 增"正文 src_unknown 占位"检测（WARNING 起步，新卡 ERROR——只向前生效，不回填存量）。附 `#433` 负向判词同族机制
- **R2 存量摸底与处置裁定**：22,871 行 / 1,524 张卡——先定义口径（哪些节占位算缺陷 vs 接受态），再决定治理批次（参照 #426 分批模式）或接受现状+标注。全量复扫输出须附 full-library-rescan 工具（#399 纪律）
- **R3 审查侧口径**：欧阳锋终审新增检查——提审卡正文含 src_unknown 占位即 FAIL（新卡）；存量卡逐步清。待 R1 门禁上线后移交机器拦截

## 边界

- frontmatter src_unknown（5,754 行接受口径）不动
- 存量处置节奏由王语嫣定（治理 ROI 判断非审查侧职责）
- 本建议书由"观察项分类追问"触发——分类标准的实证补丁：观察项入库前先测存量（单卡缺陷 vs 库级状态残留）

*欧阳锋 · 2026-08-25 · #498 复审观察项重分类落盘*
