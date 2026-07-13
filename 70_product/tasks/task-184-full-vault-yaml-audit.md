---
id: task_20260713_wangyuyan-full-vault-yaml-audit
assignee: huangyaoshi
status: reviewed
updated_at: '2026-07-13T15:33:53.175365+00:00'
reviewed_by: 欧阳锋
review_date: '2026-07-13'
grade: B+
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

---

## 终审记录 · 欧阳锋 · 2026-07-13

**结论：CONDITIONAL PASS（附条件通过）。**

### 独立复验

| 指标 | 修复前（报告） | 修复后（报告） | 当前实测 | 说明 |
|:---|:---|:---|:---|:---|
| OK | 1900 | 2217 | 2239 | YAML 可解析卡增加 |
| Type1 解析失败 | 360 | 20 | 20 | 340 张卡已修复 |
| Type2 结构异常 | 305 | 316 | 294 | 修复过程暴露/后续并行任务修复 |
| Type3 无 frontmatter | 92 | 104 | 104 | 索引文件 + legacy 卡 |

- `90_control/.sandbox/_184_yaml_audit.py` 脚本逻辑合理 ✅
- `60_feedback/diagnosis/diag-184-yaml-audit-2026-07-13.md` 报告已落 ✅
- HEAD~6 提交确认 340 个 .md 文件被修复 ✅

### 关键说明

`kdo lint --summary` 当前显示 **15 new error / 118 new warning**，但 `kdo lint --diff`（相对 HEAD~1）为空。经核查，这些 issue 是 YAML 修复后 lint 首次能读取之前损坏的卡而**显影出来的存量债**，不是 #184 引入的新债：
- 10 个 tool 卡 `empty source_refs`
- 多个旧 reviewed 卡 `missing review_date`
- 多个旧 tool 卡缺失 `Purpose/Protocol/When NOT to Use/Critique` 节
- source_refs 行号锚点 false positive

这与 #168 B-4「修结构→显影内容债」模式一致。这些债真实存在，但超出 #184「YAML 体检」的核心范围，应由后续数据卫生任务统一清理。

### 条件

1. 剩余 20 张 Type1 硬伤卡（title 含中文特殊字符）需单独立任务修。
2. Type2/Type3 清单已出，按任务单原计划交王语嫣决策是否开批量补 frontmatter 任务。
3. lint 显影的 15 error / 118 warning 需在后续数据卫生任务中处理，不能长期挂账。

**状态**：`pending_review` → `reviewed`，等级 B+。
