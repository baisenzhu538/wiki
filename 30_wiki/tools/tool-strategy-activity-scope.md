---
id: tool-strategy-activity-scope
title: 活动范围：价值链分析+边界决策——做什么/不做什么
type: tool
status: enriched
confidence: 0.90
trust_level: high
domain:
  - strategy
source_refs:
  - 00_inbox/战略专题/冉鹏PPT截图/引擎点火20260110 战略破局（冉鹏）(1)_119_vlm_desc.md
created_at: "2026-06-21"
updated_at: "2026-06-21"
author: 老顽童（初版）→ 黄药师v2标准补强
reviewed_by: 欧阳锋
related:
  - "[[framework-strategy-business-design]]"
---

# 活动范围：价值链分析+边界决策

> 业务设计六要素第4要素。核心问题：**价值链中哪些自己做、哪些交给合作伙伴？你的边界在哪？**

## 操作步骤

### Step 1：画出完整价值链
从原材料→研发→生产→营销→销售→交付→售后，列出全部环节

### Step 2：分类每个环节
| 分类 | 标准 | 动作 |
|:--|:--|:--|
| 核心 | 不可替代，差异化来源 | 自己做 |
| 重要 | 影响体验但非差异化 | 紧密合作 |
| 一般 | 标准化，可替代 | 外包 |
| 不做 | 耗费资源但非必需 | 砍掉 |

### Step 3：边界决策自检
- 我们做这件事的理由是"只有我们能做好"还是"我们一直在做"？
- 如果外包，最大的风险是什么？
- 如果自建，核心能力能否复制到新环节？

## Agent 执行指令

```python
def activity_scope_analysis(chain: list[str]):
    results = {}
    for link in chain:
        score = ask(f"在价值链环节「{link}」上：1-5分评价——我们的差异化依赖度、现有能力匹配度、外包风险度")
        category = "核心" if score["差异化"]>=4 else "重要" if score["差异化"]>=2 else "一般"
        results[link] = {"评分": score, "分类": category, "决策": "自建" if category=="核心" else "合作/外包"}
    return results
```

## 失败模式

| 失败 | 症状 | 修复 |
|:--|:--|:--|
| 边界太宽 | 什么都想做，资源分散 | 强制分类后砍掉"一般"类 |
| 外包核心环节 | 把差异化来源外包了 | 先问"这个环节和我们的差异化直接相关吗？" |

---

*老顽童初版 · v2补强 · 2026-06-21*
