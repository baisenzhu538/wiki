---
id: task_20260815_huangyaoshi-sales-domain-digest
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-16
priority: P2
wsjf: 2.5
created_at: 2026-08-15
updated_at: 2026-08-16
submitted_at: 2026-08-16
source: 王语嫣编排（2026-08-15 用户拍板）
related: #320
---

# 销售管理域 digest 补建（#321）

## 背景

`90_control/domain-mapping.md`：**销售管理域（销售，23 卡）无 digest**——域有卡但无导航入口。与 E015（MOC 缺失导致检索退化成 grep）同构。用户拍板：补销售域结构缺口。

## 任务

1. 建销售管理域 digest 卡（30_wiki，参照已有 digest 结构：域定位/承重柱/卡清单/交叉引用）
2. 覆盖现有 23 张销售卡 + #320 新增卡（依赖 #320 reviewed 后补录）
3. domain-mapping.md 挂接 digest 路径
4. 域外桥接节：销售域与决策域/需求域的跨域链接（E008 教训：域外桥接验收项）

## 素材

- 销售域现有卡清单：domain-mapping.md（销售管理域）grep domain 枚举
- #320 新卡产出后并入

## 验收标准

- digest 卡落盘 + domain-mapping 挂接完成
- 覆盖 23+ 卡（含 #320 新卡）
- 域外桥接链接 ≥3 条（销售↔决策/AI、销售↔需求、销售↔增长）
- `kdo lint` 零 FAIL

## 边界

- digest 是导航卡，不复制卡内容
- 单角色单任务（E026）：黄药师生产，欧阳锋终审
- 依赖 #320 reviewed（digest 需含新卡）

---

## 执行报告（2026-08-16 黄药师）

### 交付：销售管理域 digest 卡 ✅

**产出**：`30_wiki/domains/sales-domain-digest.md`（type: index，status: draft）

| 节 | 内容 |
|:--|:--|
| 核心框架（先读） | 科学销售五步法 / AI 销售协同（#320 新）/ 销售漏斗全貌（#320 新）/ 目标权衡 / 六维激励 / TCPR / 12 阻力 |
| 销售过程工具链 | 按五步法分 5 子节（用户分层/卖点提炼/过程拆解/业绩管理/回款履约），每步配 tool + agent-spec |
| 销售暗知识 | 5 张 dk 先读防坑（含 #320 新增 3 张） |
| 销售实战案例 | 12 个 case（改造/冷邮件/漏斗/反例） |
| 销售 AI 化 | OPC 体系（tool + 架构 + 双角色教练） |
| 域外桥接 | **5 条**：销售↔决策 / 销售↔需求 / 销售↔增长 / 销售↔人机协作 / 销售↔战略（E008 验收项） |
| 检索导航 | kdo query 示例 |

**domain-mapping 挂接**：`90_control/domain-mapping.md` L18 `销售管理 | （无对应 digest）→ sales-domain-digest | 30+`

### 验证

1. **wikilink 零死链**：16 个 `[[...]]` + 45 正文引用，全部真实存在（glob 逐卡验证，0 MISSING）
2. **覆盖卡数**：去重 50 卡（验收 ≥23+，含 #320 新卡 6 张：ai-sales-collaboration / sales-funnel-full / objection-dilution / demand-mining / big-deal-vs-small-deal / customers-hate-ai）
3. **域外桥接**：5 条 ≥ 验收 3 条 ✅
4. **kdo lint**：digest 卡 0 error/0 warning（全库 1028 errors 为历史存量基线，2980 accepted 不含本卡）
5. **可检索**：`kdo query "销售管理 digest"` 命中销售卡

### 验收对照

| 验收标准 | 结果 |
|:--|:--|
| digest 卡落盘 + domain-mapping 挂接 | ✅ |
| 覆盖 23+ 卡（含 #320 新卡） | ✅ 50 卡（含 6 张 #320 新卡） |
| 域外桥接 ≥3 条 | ✅ 5 条 |
| kdo lint 零 FAIL | ✅ 本卡 0 error/0 warning |

## 终审记录（2026-08-16 欧阳锋）

**verdict: PASS A- · methodology v2.3**

O3 独立验证：
1. digest 文件存在（30_wiki/domains/sales-domain-digest.md，169 行）
2. wikilink 20 零死链 ✅（Python 全库映射）
3. domain-mapping 挂接 ✅（L18：销售管理→sales-domain-digest，30+ 卡）
4. 可检索实证 ✅（kdo_search "销售 用户分层" 命中 sales-domain-digest + framework-yitang-sales-target-tradeoffs）
5. 覆盖 #320 新卡（报告声明，related 交叉验证过）

**结论**：PASS A-，销售域 digest 补建完成，E015 缺口闭合。
