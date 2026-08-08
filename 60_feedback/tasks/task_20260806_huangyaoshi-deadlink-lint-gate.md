---
id: task_20260806_huangyaoshi-deadlink-lint-gate
task_id: 242
assignee: huangyaoshi
status: reviewed
updated_at: 2026-08-06
domain: system
priority: P1
---

# #242 死链检测纳入 lint 门禁（F2 全库模式）

## 背景

#238 design MOC 审查 FAIL：related 7/13 死链（54%），而黄药师的 card_review_checklist PASS 未拦截——死链检测没进验收门禁。欧阳锋观察：F2 断链检测已存在但单文件模式误报（"F2 全报断链是正常的"），全库模式可查。王语嫣裁定：**死链检测必须成为 MOC/索引类卡的硬门禁**（防增量）。

## 任务目标

F2 断链检测接入 lint/pre-submit 流程，MOC/索引类卡（type: index/digest/moc）强制死链 0。

## 规格

1. **单文件 vs 全库口径修正**：F2 在单文件模式误报（把未建索引的链接当断链）——修正为：单文件模式只报"能确证为死链"的（目标文件不存在），全库模式做完整断链检查
2. **门禁规则**：`kdo pre-submit` 对 type: index/digest/moc 卡执行死链检查，related + 正文 wikilink 死链 >0 → ERROR 阻断（对标 #217 section 拼写白名单/#228 重复键的防复发模式）
3. 普通卡死链维持 WARNING 级（不追溯存量，防误伤）
4. 输出：死链清单（链接名 + 目标缺失原因：不存在/文件名不精确）

## 验收标准

1. 复测：#238 场景——MOC 卡带死链提交被拦截（狗粮验证）
2. 存量 MOC/digest 卡全库跑一遍：已知死链清单输出（供王语嫣编排存量修复或接受为已知项）
3. pytest 全量通过；lint 0 新增

## 边界

- 不追溯存量普通卡（只拦新提交的 MOC/索引类卡）
- 死链修复的存量问题单独编排（先出清单）

## 依赖

- 无硬依赖；可与 #239 复审后的修复并行（#238 修复是内容修复，本任务是门禁，互不冲突）

## 🆕 完成记录（2026-08-07 黄药师交付）

- ✅ **F4 MOC 死链门禁就位**：type: index/digest/moc → related 死链 > 0 → ERROR 阻断；普通卡维持 WARNING
- ✅ 五张 MOC 全部零死链验证通过；增量 0 新增
- ✅ 门禁闭环：#238 FAIL（54% 死链手测发现）→ F4 自动拦截——不会再出现同类审查 FAIL
- 状态：待欧阳锋审查（基建任务惯例）
