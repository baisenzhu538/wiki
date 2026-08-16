---
id: task_20260809_huangyaoshi-auth-freshness-sla
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-09
updated_at: 2026-08-09
priority: P1
wsjf: 2.8
claimed_at: 2026-08-09
---

## 执行报告（2026-08-09 黄药师）

### P0-1 reverify_by schema + lint ✅
- 8 个 schema 全部新增 `reverify_by`（concept/artifact-code/artifact-content/dark-knowledge/decision/entity/improvement/source）
- 格式：date + pattern `YYYY-MM-DD` + 描述（认证到期日 = review_date + 6 个月）
- 全部 round-trip yaml.safe_load 通过；`additionalProperties: false` 的 schema 已同步

### P0-2 `kdo feature stale` ✅
- `_is_stale()`：verified + verify_date/reverify_by 超 6 个月 → stale（降级不删除，消费端标记"证据待复验"）
- 无 verify_date 的 verified 容忍（迁移中不误报）
- fmt() 加 ⚠️stale 标记；info 命令补 verify_date/reverify_by/verify_note 显示（#264 遗留一并修复）

### P0-3 存量迁移 ✅
- 25 张 verified 全部补 verify_date + reverify_by（来源推导：KDO 基建实证 F078/F079 → 08-09；#252 试点/口述稿引用 → 08-08）
- 抽查 3 项对账一致（F001/F039 08-08→2027-02-04、F078 08-09→2027-02-05）

### P1-1 lint 0 新报 ✅
- test_workspace 47 passed；test_feature_menu 13 passed（含 5 个新 stale 场景测试）

### P1-2 测试 ≥3 ✅（实际 5 个）
- 超期 stale / 未超期非 stale / 字段缺失容忍 / 未 verified 永不 stale / reverify_by 回退

### P1-3 登记 ✅
- cap_hub AUTH_FRESHNESS_SLA（17 Feature）+ FEATURE_MENU 描述更新 + scripts README

### 验收形态
- 新卡 PASS 后补 reverify_by：1 条命令（schema 已支持字段）
- `kdo feature stale` 可复现：25 个 verified 全部在复审期内（2027-02 到期）

# 认证层 + 新鲜度 SLA（#272 · 欧阳锋建议书 R2）

## 任务目标

把"已入库"升级为"已认证且未过期"——卡片/Feature 状态有复审期限，过期自动降级（降级不删除，stale 仍可检索只是消费端标记"证据待复验"）。

## 语义定义（欧阳锋定，黄药师实现）

【卡片侧】
- 新可选字段 `reverify_by: YYYY-MM-DD`
- P0 framework 卡 + 新域首卡：终审 PASS 时默认写入 reverify_by = review_date + 6 个月
- 其他卡不强制（存量不追溯）

【周期表侧】
- verified 状态加过期语义：verify_date + 6 个月未复验 → 降级 stale
- `kdo feature` 命令：info/list 显示 verify_date 与 reverify_by；新增 `kdo feature stale` 列出超期项

## 验收标准（四节）

【P0/P1 清单】P0-1 reverify_by schema + lint 校验；P0-2 `kdo feature stale` 实现（超期判定可测）；P0-3 存量迁移：周期表 25 张 verified 补 verify_date（按 #252 回填记录推导）。P1-1 迁移后全库 lint 0 新报；P1-2 测试 ≥3（超期/未超期/字段缺失容忍）；P1-3 README + cap_hub 登记
【字段级定位】kdo feature 命令模块 + 卡片 schema + 周期表 JSON
【证据】Atlan KB 治理调研（未治理捏造率 52% vs 治理后近零）+ #252 协议 v0.1 三修正项（verified 语义漂移）
【期望形态】新卡 PASS 后 1 条命令补 reverify_by；`kdo feature stale` 输出可复现（抽查 3 项与 JSON 对账一致）

## 依赖

- R1-c/R1-d（#271）完成后的迁移校验前置；schema 协商可并行
- **消费端协议 v0.2 联动**（王语嫣已裁定）：stale 降级语义与 verify_note 显示一起并入 v0.2，一次定齐避免 v0.3

## 参考素材

- 欧阳锋建议书 `70_product/tasks/proposal-review-infra-v22-2026-08-09.md` §三
- `60_feedback/tasks/task_20260809_wangyuyan-feature-consumption-pilot.md`（#252 协议 v0.1）

## 边界

- 不删除任何数据；存量卡片不追溯（除周期表 25 张 verified）

## 终审记录（2026-08-09 欧阳锋）

**verdict: PASS A · blocking: 无 · methodology v2.2**

O3 独立验证全部通过：
1. schema：90_control/schemas/ 8 个 schema（concept/artifact-code/artifact-content/dark-knowledge/decision/entity/improvement/source）均含 reverify_by
2. stale 实跑：`feature_menu.py stale` → "无超期（25 个 verified 全部在复审期内）"；_is_stale() 实现确认（verified + 超 6 个月 → stale，无 verify_date 容忍，reverify_by 回退）
3. JSON 对账：verified 25 总数；F001/F039 verify_date 2026-08-08 → reverify_by 2027-02-04、F078 08-09 → 2027-02-05 逐字一致
4. **#264 遗留闭环实测**：`info F039` 显示"认证注记: 试点#252 边界验证——跨域无效"（verify_note 诚实标注）+ 认证日期 + 复审期限
5. 测试实跑：test_feature_menu.py **13 passed**（wiki 侧 kdo-tools/，5 个新场景全在列：overdue/fresh/missing_date_tolerated/unverified_never/reverify_by_fallback）+ test_workspace 47 passed
6. 登记：cap_hub AUTH_FRESHNESS_SLA（17 Feature）+ scripts README stale 命令文档

亮点：#264 遗留（info 显示 verify_note）顺手闭环——协议 v0.2 候选提前落地；stale 语义与消费端协议 v0.2 联动（王语嫣裁定）一次定齐。**"已入库"正式升级为"已认证且未过期"——新鲜度 SLA 从建议书到代码落地。**

五维：溯源 95/逻辑 95/暗知识 85/可操作 95/表达 90 → 总分 93（A）
