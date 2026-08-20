---
id: 391
assignee: laowantong
status: queued
title: 历史元数据批量收口第一批（P3，#388 终审清单立项）：16 张补 updated_at + 189 张 source_refs 死路径改 src_unknown
priority: P3
dependency: []
---

# #391 历史元数据批量收口第一批

## 来源

#388 同类扫描清单（欧阳锋终审认可"按域分批立项"）中的两个**机械类**（规则明确、无推断风险）：

1. **缺 updated_at：16 张**（如 concept-streaming-extraction-pattern / dk-yb19 等——以实扫为准）
2. **source_refs pending_archive 死路径：189 张**（如 case-gudong-tea-shop-foresight / case-milktea-five-step 等）——#388 已确立处置范式：死路径→`src_unknown`（标准待补标记），真实路径保留

第三类（tags 缺 audience/scene 739 张）是判断类（取值需推断，O0 风险），**不在本单**，待老朱拍板后按域分批另立项。

## 任务目标

两类机械修复批量落地，相关卡 pre-submit 0 ERROR。

## 执行范围

1. **updated_at 补 16 张**：值=补正当日日期，只加这一个字段（同 #385/#388 模式）
2. **source_refs 死路径改 189 张**：pending_archive 不可达路径→`src_unknown`；同卡真实路径保留不动；出处信息正文已保留的不动
3. 产出两张 dry-run 清单（修复前），修复后全量复扫确认归零（E017：修复了≠清干净了）

## 边界

- 批量三问（dry-run 预览+范围声明+非空不覆盖）——189 张是大批量，dry-run 清单必须贴执行报告
- 只动 frontmatter 指定字段，正文零改动，其他字段零改动
- 739 张 tags 类不碰
- 逐批 `kdo pre-submit` 0 ERROR（可分批跑）；diff 统计贴报告
- 完成后 commit 入档（E040：未入 git=未发生）
- 欧阳锋随下批 spot-check 复终审

## 内容价值判断（PROTOCOL §7 合规声明）

- 仅元数据机械修正，无删除/移动，无语义推断

## 验收标准

1. 全库缺 updated_at = 0、source_refs pending_archive 死路径 = 0（修复后全量复扫）
2. pre-submit 0 ERROR
3. dry-run 清单与实际修复一致（无清单外改动）

## 交付

1. 两张清单 + diff 统计 + pre-submit 输出
2. 送欧阳锋终审（随下批 spot-check）
