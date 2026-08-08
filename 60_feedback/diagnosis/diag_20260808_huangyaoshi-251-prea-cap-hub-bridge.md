---
id: diag_20260808_huangyaoshi-251-prea-cap-hub-bridge
title: "#251 先行A：双轨 bridge cap_hub 侧——12 lint Feature 清单+边界"
type: diagnosis
author: 黄药师
status: draft
created_at: 2026-08-08
domain: kdo
priority: P0
source: "#251 编排——王语嫣安排黄药师先行A/B"
---

# #251 先行A：双轨 bridge cap_hub 侧输入

> 给老顽童 bridge 卡生产备料——12 个 lint Feature 的完整清单、边界说明、独立测试用例。

## 双轨定义（欧阳锋洞察 3）

| 轨 | 内容 | 来源 | 用途 |
|:--|:--|:--|:--|
| capability 轨 | AI 基本功 100 Feature | #248 周期表 JSON | 课程教学内容，消费端点菜 |
| lint 轨 | KDO 质量门禁 12 Feature | cap_hub/features.json | 知识工厂质量保障，卡生产门禁 |

**混编红线**：两轨不交叉。capability 轨无 lint 语义，lint 轨无课程内容。

## Lint 轨 12 Feature（cap_hub/features.json）

| ID | 名称 | 边界 | 独立测试 |
|:--|:--|:--|:--|
| F1_UPDATED_AT | updated_at 必填 | 仅拦缺日期——不检查日期格式 | 缺字段→ERROR |
| F2_BACKLINK | 双向链接 | 全库模式确认真断链；单文件模式不报 | A→B无回链→ERROR |
| F3_DUPLICATE_ID | 重复ID | 同id不同文件→ERROR；同id同文件=正常 | 两文件同id→ERROR |
| F4_MOC_DEADLINK | MOC死链 | 仅 index/digest/moc 类型触发 | MOC卡死链>0→ERROR |
| DK_7_SECTIONS | dk七段 | 仅 dk 类型触发；不追溯存量 | 缺Critique→ERROR |
| SEC_TYPO | 段名拼写 | 白名单匹配；非白名单不报 | Critque→ERROR |
| R6_SEARCH | 搜索可达性 | title空→ERROR；缺aliases→WARN；缺tags→WARN | 空title→ERROR |
| DUP_KEY | 重复键 | 6个关键字段；存量在基线 | 双aliases→ERROR |
| REVIEW_MARK | 终审标记 | CLI，非门禁；只写不读 | --dry-run→预览 |
| REACH_CHECK | 可发现性自查 | CLI，提交前自检；非门禁 | 关键词命中→PASS |
| HINT_MAP | 错误场景化提示 | UX，追加到lint输出；非门禁 | 错误输出含场景提示 |
| CARD_CHECKLIST | 复审自检 | CLI，提报前自检；非门禁 | 全PASS→可提报 |

## 边界说明（老顽童 bridge 卡直接引用）

1. **门禁 vs CLI vs UX**：8 个门禁(ERROR级阻断) + 3 个 CLI(自检工具) + 1 个 UX(输出增强)
2. **触发条件**：门禁在 kdo lint / pre-submit 自动触发；CLI 需主动调用
3. **不溯存量**：DUP_KEY/R6/DK_7/F4 第一版只拦新提交，存量在基线
4. **与 capability 轨的关系**：两轨在数据源层面物理隔离——feature_menu.py 只读 capability JSON，kdo_lint.py 只读 wiki 文件。无交叉路径

## bridge 卡建议（给老顽童）

建议建 `bridge-kdo-lint-features-capability`：
- 左端：12 lint Feature（本清单）
- 右端：100 capability Feature（周期表 JSON）
- 桥接点：Feature 思维的一致性——两轨都用"原子化最小技术单位"定义能力
- 核心关系：capability 轨的 Feature 思维直接指导了 lint 轨的 Feature 注册表设计（口述 L1402-1450）
