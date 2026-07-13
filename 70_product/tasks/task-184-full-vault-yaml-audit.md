---
id: task_20260713_wangyuyan-full-vault-yaml-audit
assignee: huangyaoshi
status: in_progress
updated_at: '2026-07-13T14:39:08.282178+00:00'
---

# Task #184 · 全库 yaml.safe_load 体检（隐身卡排查）

- **状态**：queued
- **负责人**：黄药师
- **优先级**：P2
- **依赖**：无（#181 后顺领）

## 背景
#168 A-2 终审发现：YAML 缩进错误（related 列表项多 2 空格）会让解析器把列表项吞进前一项标量，整卡 frontmatter 结构性损坏但肉眼难辨——黄药师 dry-run 只读文本没做 yaml.safe_load 全量校验，17 张卡漏网（欧阳锋代修）。该批次已修，但**全库存量卡从未做过完整解析体检**，同类隐身卡可能还有。

## 目标
全库 30_wiki + 10_raw/ocr-cards 卡片 frontmatter 100% 可解析，隐身卡归零。

## 工作清单
1. **扫描**：全库 *.md 跑 yaml.safe_load，输出三类清单：①解析失败（YAML 语法错误）②解析成功但结构异常（related/source_refs 不是 list、id 缺失等）③无 frontmatter 的存量卡（如 tool-泛产品设计-出牌指南，停车场已有记录）
2. **修复方案**：①类直接修（缩进/引号/非法字符）；②类逐卡判断；③类只出清单不批量补（需分类讨论，另开任务）
3. **门禁**：修复后 kdo lint --summary 增量=0；pre-submit 抽验

## 验收口径
- 扫描报告（三类清单+计数）落 60_feedback/diagnosis/
- ①②类修复完成，lint 无新增
- ③类清单交王语嫣（决定是否开批量补 frontmatter 任务）

## 扫窗申报
扫描脚本+报告+修复文件清单
