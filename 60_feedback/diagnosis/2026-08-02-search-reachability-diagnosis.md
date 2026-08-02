---
id: diagnosis-20260802-search-reachability
title: "诊断报告：KDO 搜索可达性问题——以「创新者的窘境」为例"
type: diagnosis
status: open
created_at: 2026-08-02
created_by: 小昭（外部 agent）
severity: P1
affected_roles:
  - 老顽童（生产规范）
  - 黄药师（搜索基建）
  - 欧阳锋（审查清单）
domain:
  - kdo-infrastructure
  - knowledge-quality
---

# 诊断报告：KDO 搜索可达性问题

## 一、现象

2026-08-02，用户通过小昭（外部 agent）使用 `kdo_search` 检索"创新者的窘境"，**未返回对应卡片**。但该卡片实际存在于知识库中：

- **卡片 ID**：`framework-christensen-disruptive-innovation`
- **路径**：`30_wiki/frameworks/framework-christensen-disruptive-innovation.md`
- **状态**：`reviewed`（已通过欧阳锋终审）
- **入库时间**：2026-08-02（当天新建，源文件 `src_20260802_创新者的窘境_秦鹏拆书.txt`）
- **内容质量**：正文完整（含原始表述、核心结构、Critique、Synthesis、失败模式、操作方法），confidence 0.92

搜索关键词与结果：
- `"创新者的窘境"` → 0 条匹配（top result score 仅 30.381，完全不相关）
- `"创新者窘境 颠覆式创新 破坏性创新"` → 0 条匹配

最终通过文件系统 `ls | grep` 才找到，绕过了 KDO 搜索。

## 二、根因分析

### 2.1 卡片元数据缺陷（生产侧）

检查 `framework-christensen-disruptive-innovation` 的 frontmatter：

```yaml
id: framework-christensen-disruptive-innovation
title: ""              # 🔴 标题为空
# aliases: 缺失        # 🔴 无中文别名
# tags: 缺失           # 🔴 无标签（其他卡均有 audience/scene/skill-level）
```

**对比正常卡片**（以 `tool-讲香基本功-十指模型` 为例）：
```yaml
title: "讲香基本功：十指模型完整40策略"
aliases: ["十指模型", "十指40策略", "个人修炼"]
tags: ["audience:executor", "scene:execution", "skill-level:intermediate", "method:十指模型", "source-person:李頔"]
```

**影响**：
- `title` 为空 → BM25 搜索丢失最高权重字段的得分
- 无 `aliases` → "创新者的窘境"、"破坏性创新"、"颠覆性创新"、"克里斯滕森" 等中文搜索词无法匹配
- 无 `tags` → 丢失标签维度的检索能力
- 正文虽含"创新者的窘境"关键词，但 BM25 对正文的权重远低于 frontmatter 字段

### 2.2 搜索引擎能力限制（基建侧）

`kdo_search` 返回 `"engine": "BM25"`，表明当前使用纯关键词匹配：

- **无语义搜索**：搜"创新者的窘境"不会匹配到"disruptive innovation"——中英文之间无同义词映射
- **无模糊搜索**：不支持近似匹配、拼写容错
- **Graph RAG 未接入 kdo_search**：KDO 有 Graph RAG 能力（需通过 `kdo graph query` 单独调用），但主搜索接口未集成，导致用户一个入口搜不到、需要知道两个入口才能覆盖

### 2.3 索引刷新滞后（基建侧）

该卡片当天入库，但搜索结果中完全不存在。可能原因：
- `kdo index --rebuild` 未在新卡入库后执行
- 或索引是定时刷新而非实时增量更新
- 无论哪种，**当天入库的卡片当天搜不到**是用户体验断裂

### 2.4 审查清单遗漏（审查侧）

卡片 `status: reviewed`，`reviewed_by: 欧阳锋`——已通过终审。但以下问题未被拦截：
- title 字段为空
- 无 aliases（尤其是中文搜索词）
- 无 tags

说明 L3 终审清单中**缺少"搜索可达性"检查项**。

## 三、影响评估

| 影响面 | 评估 |
|:--|:--|
| **用户信任** | 用户搜不到当天刚入库的卡片 → 对知识库检索能力失去信心 |
| **知识利用率** | 搜不到 = 不存在。高质量卡片如果搜不到，生产成本完全浪费 |
| **普遍性** | 需排查：是否所有今天入库的新卡都有同样问题？是否老卡也存在 title 空/无 aliases 的情况？ |
| **外部 agent 协作** | 小昭作为外部 agent 完全依赖 kdo_search 检索知识库，搜索不可达 = 协作通道断裂 |

## 四、修复建议

### 4.1 紧急修复（本周）

| # | 动作 | 责任人 | 优先级 |
|:--|:--|:--|:--|
| 1 | **修复 `framework-christensen-disruptive-innovation` 的 frontmatter**：补 title、aliases（"创新者的窘境"、"破坏性创新"、"颠覆性创新"、"克里斯滕森"、"Christensen"）、tags | 老顽童 | P0 |
| 2 | **执行 `kdo index --rebuild`** 刷新搜索索引 | 黄药师 | P0 |
| 3 | **排查今日其他新卡**（讲香基本功十指模型等）是否存在同类元数据缺陷 | 老顽童 | P0 |

### 4.2 短期改进（两周内）

| # | 动作 | 责任人 | 优先级 |
|:--|:--|:--|:--|
| 4 | **L3 终审清单增加"搜索可达性"检查项**：title 非空、aliases 含中文搜索词、tags 完整 | 欧阳锋 | P1 |
| 5 | **新卡入库后自动触发增量索引**（或至少在 production-queue 完成批次后统一 rebuild） | 黄药师 | P1 |
| 6 | **全库扫描**：检查是否存在其他 title 为空 / 无 aliases 的卡片，生成清单 | 黄药师 | P1 |

### 4.3 中期改进（一个月内）

| # | 动作 | 责任人 | 优先级 |
|:--|:--|:--|:--|
| 7 | **kdo_search 集成 Graph RAG**：BM25 + Graph RAG 双引擎合并排序，框架卡优先 | 黄药师 | P2 |
| 8 | **中英文同义词词典**：建立 card id 英文 ↔ 中文标题/别名的映射表，搜索时自动扩展 | 黄药师 | P2 |
| 9 | **产卡模板强化**：`kdo scaffold` 生成的骨架卡强制要求 title、aliases、tags 非空才能通过 L1 门禁 | 黄药师 + 老顽童 | P2 |

## 五、复现路径

```
1. kdo_search query="创新者的窘境" → 0 results
2. kdo_search query="创新者窘境 颠覆式创新 破坏性创新" → 0 results
3. ls 30_wiki/frameworks/ | grep christensen → 找到文件
4. kdo_read card_id="framework-christensen-disruptive-innovation" → 内容完整
5. 检查 frontmatter → title 空、无 aliases、无 tags
```

## 六、关联

- 涉及卡片：`framework-christensen-disruptive-innovation`
- 关联卡片（可能存在同类问题）：`bridge-christensen-reverse-mapping`、`framework-christensen-value-network`、`concept-christensen-rpv-model`
- 工厂文档参考：`90_control/kdo-industrialization-manual.md`（铁律）、`.agent/pitfalls.md`（踩坑记录）
- 建议新增 pitfall：**"搜不到 = 不存在——卡片元数据不完整导致搜索盲区"**

---

> 本报告由小昭（外部 agent）生成。小昭通过 KDO MCP 检索知识库时发现问题，非工厂生产 SOP 产物。建议欧阳锋分发至老顽童（修复卡片）和黄药师（修复索引+基建）。
