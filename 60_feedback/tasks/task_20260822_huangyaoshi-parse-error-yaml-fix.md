---
id: 409
assignee: huangyaoshi
status: queued
title: 库级 YAML 修复（P2，欧阳锋 08-22 立项）：parse-error 58 张 YAML 结构损坏修复——#373 同类，不伪装归零
priority: P2
dependency: []
code_files:
- 90_control/scripts/full-library-rescan.py
updated_at: '2026-08-21T20:30:00+00:00'
---

# #409 库级 YAML 修复（parse-error 58 张）

## 来源

- 用户 08-22 授权"清理遗留库级债务"；#399 遗留建议 1（欧阳锋裁决：YAML 损坏修复单独立项）
- 当前基线（`full-library-rescan` 实测，2026-08-22）：**parse-error 剩余 58**（08-21 基线 61，master-moc 编码修复后下降）
- 错误模式：`YAML parse error: while parsing a block mapping / expected <block end>, but found '-'`——frontmatter 列表块（related/source_refs 等）结构坏，与 #373 已知编码损坏同族

## 任务目标

修复全库 58 张 YAML 结构损坏卡，使 `full-library-rescan --check parse-error` 归零。**修复前任何"归零"声明须附该工具输出（#399 纪律），解析失败卡显式列清单，不伪装归零。**

## 执行范围

1. **先出清单**：`full-library-rescan --check parse-error` 拿全量 58 张清单（已确认样例：case-strategy-* 6 张 / concept-smart-medicine-cabinet-* 6 张 / ai-native-im-multi-agent / concept-kdo-review-workflow / graph-rag / fd-forward-deployment 等）
2. **逐张修复**：yaml 级解析定位坏块（缩进/列表结构），**只修结构不改变内容语义**；每张修复后 yaml.safe_load 通过 + `kdo pre-submit` 抽检
3. **归零验收**：`full-library-rescan --check parse-error` → 剩余 0（附输出到执行报告）
4. **回归确认**：修复后 `kdo index --rebuild` 索引文件数对比（58 张修复前后索引覆盖）

## 边界

- **不动 00_inbox 素材层**（素材只读纪律；该层 GBK 文件另议）
- 不改变卡内容语义——纯结构修复；涉及内容歧义无法机械修复的，列清单退回（写清卡名+位置+原因，给生产者）
- 修复后 commit 入档（E040）
- 交付物涉及 90_control 工具改动（如需升级扫描器容错）按 code_files 声明跨仓路径（#380 门禁）

## 验收标准

1. `full-library-rescan --check parse-error` = 0（**附工具输出**，归零声明纪律）
2. 抽查修复卡：yaml 可解析 + 内容语义无改动（diff 对比仅结构变化）
3. 修复前后清单差异有说明（58 → 0 的路径）
4. 欧阳锋终审抽"修复真实性"（是否真的 yaml 级修复而非绕过/删除字段）

## 交付

1. 执行报告：修复前清单 → 逐张修复说明（或退回清单）→ 归零工具输出
2. 送欧阳锋终审
