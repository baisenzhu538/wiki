---
id: 527
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-25T14:39:53.753752+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- kdo-tools/
- 90_control/quality-gates/
---

# #527 被依赖卡 draft 门禁（消费链引用完整性 lint）

- **任务号**：#527
- **状态**：queued
- **assignee**：huangyaoshi（lint 规则+存量扫描；欧阳锋终审）
- **优先级**：P1（被消费端活依赖的 draft 卡=无保真承诺的数据源——盲测 P4 + 小昭「draft 当定论」双实证）
- **立项**：2026-08-25 王语嫣（小昭检索检测报告建议 4 裁定；老朱对齐确认）

## 背景

`framework-truman-feature-layered-system`（Feature 周期表框架卡）status=draft，但它已是 basic-skills-coach 的活数据源（CLAUDE.md 指定+feature_menu.py 数据链）——frontmatter 状态与下游实际依赖不匹配，违反 E018 精神（被消费的资产必须先过审，否则下游引用无保真）。同族实证：小昭会话 kdo_search 捞出 draft 卡当答案（#524 已治标=标注警示，本单治本=源头清零）。

## 任务

1. **lint 规则**：被任何 agent-spec / CLAUDE.md / SOUL.md / spec 数据链（feature_menu 类工具配置）引用的 30_wiki 卡，`status: draft` 即报警——**WARNING 起步出清单，新引用 ERROR**（红线 4 误拦优先；只向前生效）
2. **存量扫描清单**：全库扫「被依赖且 draft」的卡，落清单（机读 json+人读 md）交王语嫣——欧阳锋按清单排优先过审（第一张=layered-system）
3. 回归测试：构造被引用 draft 卡/无引用 draft 卡（后者不报警——draft 本身无罪，被依赖才报警）两类用例

## 边界

- 不自动改卡状态（过审是欧阳锋的活，门禁只报警）；引用检测覆盖 frontmatter related 之外的「工具配置硬引用」（CLAUDE.md/SOUL.md/数据链路径）
- 与 #524 关系：#524 管检索结果标注（治标已闭环），本单管被依赖源头（治本）；不重复

## 验收

- lint 规则上线+两类用例回归通过；存量清单交付（数量+清单路径）
- layered-system 卡进入欧阳锋优先过审队列（王语嫣通知）
- 欧阳锋终审
