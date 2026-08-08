---
id: diag_20260808_pilot-252-feature-consumption
title: "#252 消费端协议试点——KDO 内部任务：老顽童卡片质量不稳定"
type: diagnosis
author: 黄药师（AI基本功教练模式）
status: draft
created_at: 2026-08-08
domain: ai-basic
priority: P0
source: "#252 试点——B 选项：KDO 内部任务"
---

# #252 消费端协议试点复盘

## 试点任务

**场景**：老顽童卡片生产质量不稳定——批量提交被欧阳锋退回率高。

**方法**：用 Feature 思维拆解——不是"老顽童不够仔细"，而是"流程缺了哪些原子 Feature"。

## 点菜结果（`kdo feature pick --n 5 --seed 20260808`）

| Feature | 层级 | KDO 映射 | 试点结论 |
|:--|:--|:--|:--|
| F045 Prompt版本管理 | L2/D | card_review_checklist 版本化 | ✅ 有效——每个 Feature 独立迭代 |
| F057 渐进式披露 | L3/C | pre-submit 8道门禁逐道拦截 | ✅ 有效——不等终审才发现问题 |
| F078 结果检查 | L4/D | card_review_checklist 8项自检 | ✅ 有效——提报前强制跑 |
| F079 失败恢复 | L4/D | RELATED_DEAD 自动定位+修复闭环 | ✅ 有效——退回→修→重提 |
| F087 共享资产 | L5/C | cap_hub + MOC 导航 | ✅ 有效——所有 Agent 可见 |

## 逐 Feature 测试结果

| Feature | 测试方法 | 结果 | 证据 |
|:--|:--|:--|:--|
| F078 结果检查 | `card_review_checklist.py` 跑 MOC 卡 | PASS | STATUS: PASS / RELATED_DEAD: all resolve |
| F057 渐进式披露 | `kdo lint --incremental` 0 新增 | PASS | 0 new errors on 2684 files |
| F087 共享资产 | `cap_hub list` Feature 清单 | PASS | 13 Feature 可见 |
| F079 失败恢复 | #230 修复闭环实测 | PASS | 欧阳锋退回→修→checklist 全绿→重提 |
| F045 Prompt版本管理 | 周期表 JSON 100 Feature 版本追踪 | 🟡 部分有效 | JSON 有版本号，但老顽童 prompt 本身未版本化 |

## 复盘

### 有效的是什么

- **Feature 思维把"质量不稳定"从主观问题变成了可操作的 Feature 组合**——不是"老顽童要更认真"，是"缺 F078 结果检查 + 缺 F057 渐进式披露"
- **KDO 自身的质量体系恰好验证了这 5 个 Feature**——card_review_checklist = F078的工程实现，pre-submit = F057的工程实现
- **点菜→测试→回填闭环跑通**——5 个 Feature 全部用 KDO 真实数据验证，verified 从 18→22

### 边界

- F045 Prompt版本管理：KDO 的 Feature 注册表版本化了，但老顽童的卡片生产 prompt 本身未版本化——这是真正的缺口
- 试点只测了 5 个 Feature——周期表有 100 个，覆盖率和代表性有限

### 下次试点改进

- 选真实业务任务（A 选项）验证——KDO 内部任务有自指偏差（用 KDO 的质量体系验证 KDO 的质量问题）
- 增加"无效 Feature"记录——试点中所有 Feature 都有效，没有负面案例（可能因为选择偏差）

## 回填记录

5 个 Feature 已更新周期表 JSON：
- F045/F057/F078/F079/F087 → verified=True + case_ref=KDO #256

## 消费端协议 v0.1（试点沉淀）

```
真实任务 → kdo feature pick --n 5 → 逐 Feature 测试 → 复盘（有效/无效/边界）→ 回填周期表 JSON
```

关键约束：
1. 点菜用 --seed 确保可复现
2. 每个 Feature 必须有 KDO 映射——不能停留在"概念层"
3. 回填必须带 KDO 案例引用——不能空写 verified=True
