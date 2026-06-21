---
id: tool-strategy-risk-management
title: 风险管理：麦肯锡7S七维对齐诊断
type: tool
status: enriched
confidence: 0.90
trust_level: high
domain:
  - strategy
source_refs:
  - 00_inbox/战略专题/冉鹏PPT截图/引擎点火20260110 战略破局（冉鹏）(1)_126_vlm_desc.md
created_at: "2026-06-21"
updated_at: "2026-06-21"
author: 老顽童（初版）→ 黄药师v2标准补强
reviewed_by: 欧阳锋
related:
  - "[[framework-strategy-business-design]]"
---

# 风险管理：麦肯锡7S七维对齐

> 业务设计六要素第6要素。核心问题：**战略设计完成后，组织能不能承接？如果≥3个S不同步，战略大概率失败。**

## 操作步骤：7S诊断

| S | 维度 | 诊断问题 |
|:--|:--|:--|
| Strategy | 战略 | 我们的战略方向清晰吗？ |
| Structure | 结构 | 组织架构支持这个战略吗？ |
| Systems | 系统 | 流程/IT/考核体系对吗？ |
| Shared Values | 共享价值观 | 团队真的认同这个方向吗？ |
| Style | 风格 | 领导风格和管理文化匹配吗？ |
| Staff | 员工 | 现有团队能力够吗？ |
| Skills | 技能 | 核心技能在内部还是外包？ |

### 评估标准
每个S打分：✅对齐 / ⚠️部分对齐 / ❌不对齐
- ≥3个❌→ 战略执行有重大风险
- 1-2个❌→ 可管理，但需行动计划

## Agent 执行指令

```python
def mckinsey_7s_check(strategy_statement: str):
    seven_s = ["战略", "结构", "系统", "共享价值观", "风格", "员工", "技能"]
    results = {}
    for s in seven_s:
        results[s] = ask(f"基于战略「{strategy_statement}」，我们的「{s}」是否对齐？✅对齐/⚠️部分对齐/❌不对齐。给出具体证据。")
    red_count = sum(1 for v in results.values() if "❌" in v)
    risk = "🔴重大风险" if red_count >= 3 else "🟡需关注" if red_count >= 1 else "🟢低风险"
    return {"诊断": results, "❌数": red_count, "风险等级": risk}
```

## 失败模式

| 失败 | 症状 | 修复 |
|:--|:--|:--|
| 只看硬S | 只分析战略/结构/系统，忽略价值观/风格 | 四个软S（价值观/风格/员工/技能）必须纳入 |
| 诊断不行动 | 发现了3个❌但没有行动计划 | 每个❌必须配一个负责人+截止日期 |

## 外部验证

| 主张 | 验证 | 来源 |
|:--|:--|:--|
| 麦肯锡7S | ✅ 1980年Tom Peters/Robert Waterman开发 | 冉鹏PPT引用为风险管理工具(slides 126-129) |

---

*老顽童初版 · v2补强 · 2026-06-21*
