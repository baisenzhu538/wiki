---
id: task_20260809_huangyaoshi-moc-index-register
task_id: 266
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-09
updated_at: 2026-08-09
domain: system
priority: P1
---

# #266 4 张 MOC 卡补登记 index.md（检索可达性修复）

## 背景（飞书王语嫣域复核发现）

复核 KDO 域结构：12 digest 全部在 index.md 登记 ✅，但 **design-moc / product-moc / master-moc / retrospective-moc 未在 index.md 域摘要节登记**——导航卡不登记=检索可达性缺口（#219 同类问题：索引不登记=搜不到）。

## 任务内容

1. 4 张 MOC 卡（design/product/master/retrospective）补登记 index.md（域摘要节或 MOC 导航节——黄药师按索引规范裁定位置）
2. 登记后验证：`kdo query "设计 MOC"/"复盘 MOC"` 可命中
3. 与 #236 复盘 MOC 的历史登记对比：确认是"未登记"还是"登记了但格式/位置不一致"——如果是后者，只需对齐

## 验收标准

1. 4 张 MOC 在 index.md 可查（grep 命中）
2. kdo query 命中（检索可达）
3. 索引重建后 lint 0 新增

## 边界

- 只补登记，不改 MOC 卡内容
- 新域登记规则（#261 domain-mapping：路由+卡+映射表三处）是否需含 index.md——一并裁定（新增域四处登记：路由+卡+映射+index）

---

## 补审记录（欧阳锋 2026-08-09 终审）

**结论：PASS，等级 A**。5 MOC 补登 + 四处登记规则 + 域结构健康全部独立核验通过。

### 核验（O3 实测）

| 验收项 | 结果 | 证据 |
|:--|:--|:--|
| 5 MOC 补登 index.md | ✅ | retrospective/design/master/product/kdo 五张均在 index.md（任务单说 4 张——kdo-moc 已顺带在列，5/5 全覆盖）|
| 登记规则四处 | ✅ | domain-mapping.md"新增域登记规则"第 4 条：检索侧 index.md 追加（防 #219 类检索盲区——卡建了但搜不到），四处缺一不可 |
| 域结构健康 | ✅ | domains/ 19 张卡（digest+MOC）全部有 index.md 登记，零遗漏 |
| 边界遵守 | ✅ | 只补登记未改 MOC 卡内容 |

**#219 教训正式固化**：欧阳锋 context 中"跑 kdo index 刷新搜索索引（#219 教训：索引过期 5 天 → 外部 agent 搜书名 0 结果）"——现在"索引登记"成为新域注册的四处之一，从人工兜底变为强制规则。
