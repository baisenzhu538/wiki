---
assignee: kimi
status: queued
updated_at: '2026-07-12'
reviewed_by: pending
---
# 任务 #164：C 域收尾清理（双卡去重 + draft 件 status 升级）

> 编排：王语嫣 | 生产：老顽童（A 段）+ 黄药师（B 段） | 终审：欧阳锋
> 优先级：P2（C 域体检遗留，不阻塞任何主线）
> 来源：2026-07-12 王语嫣 C 域整体体检（脚本扫描）

## A 段：expert-interview 双卡去重（老顽童）

背景：#156 终审 F5 裁定——`framework-yitang-expert-interview-10steps`（旧·通用 framework）与 `yt-tool-business-formula-expert-interview-10`（新·C 域 tool）**双卡并存、互链不合并**，并明确「**内容去重留 #158 收口后的清理任务**」。#158 已收官，清理未执行。

交付：
1. 逐段比对两卡内容重叠，产出分工标注：
   - 旧卡（通用版）：文首注明「C 域业务公式课程原位版见 `yt-tool-business-formula-expert-interview-10`」；与 C 域版重复的步骤细节段落，精简为指向新卡的引用（旧卡保留通用方法论骨架，不删卡——既有资产、index 在册、可能有外链）
   - 新卡（C 域课程原位版）：保持现状（图 002213 一等准+口述行号），确认 related 互链注释「通用版」已在
2. 两卡 pre-submit PASS；申报制（文件+行号）

## B 段：黄药师 4 件 draft→enriched（黄药师）

背景：#158 已 reviewed，黄药师预写件修复回填已完成（桥接卡 TODO=0、miner source_refs 已全换口述行号——王语嫣亲验），但 4 件 status 仍挂 draft：
- `framework-business-formula-dual-triangle-bridge`
- `framework-business-formula-y-model-bridge`
- `framework-business-formula-fundamentals-bridge`
- `tool-agent-spec-business-formula-parameter-miner`

交付：4 件 status: draft → enriched（frontmatter 单字段），逐件 pre-submit PASS，申报制。

## 验收点（欧阳锋用）

1. A 段：双卡分工标注清晰、无内容重复段落、互链注释双向、旧卡零删除
2. B 段：4 件 status 升级+门禁全过（升级前可顺带核验 miner source_refs 口述行号——digest L105 挂账销项）
3. 扫窗自查申报=实动
