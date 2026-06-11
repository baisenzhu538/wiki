# 欧阳锋任务指令 · 2026-06-11

> 本轮目标：桥接卡量产 + 图谱修复收尾 + 诊断积累

---

## 🎯 总优先级

1. **黄药师**：加扫描目录（5分钟） → 修完图谱最后一步
2. **老顽童**：桥接卡量产（Hypothesis-Driven 系列 + 5 Whys）→ 课转卡补判断标准检查 → 旧卡逐步补互链
3. **王语嫣**：等自迭代提案审查 → 继续诊断 + 标注新缺口
4. **洪七公**：待命

---

## 老顽童

**任务文件：** `70_product/tasks/laowantong-next-tasks.md`

### 顺序

| 顺序 | 任务 | 说明 |
|:----:|:-----|:------|
| **1** | **桥接卡量产：Hypothesis-Driven 系列** | P0。concept + skill + dk 三张一组，见下方要求 |
| **2** | **桥接卡量产：5 Whys** | P0。轻量工具卡，见下方要求 |
| **3** | **课转卡自查** | 确认所有课转技能卡都已补"判断标准"小节 |
| **4** | **旧卡补互链** | 有空时逐步补。目标：每张旧卡 related 字段至少填 2 个关联 |

### 桥接卡量产要求

每张卡必须满足以下三条（缺一退回）：
1. **Bridge 节**已写（正文内，阐述与一堂体系的桥接关系）
2. **`bridges_to`** frontmatter 已填（至少 1 条）
3. **Synthesis 链接 ≥5 个**，其中至少 2 个同域横向链接

### 攻击者选择参考

- **Hypothesis-Driven** → Kahneman（确认偏误）+ Eric Ries（精益创业）
- **5 Whys** → Taleb（过度简化）+ Senge（系统思考）
- 参考 Issue Tree 的组合（Christensen + Mintzberg），避免每次都选 Kahneman+Taleb

---

## 黄药师

**任务文件：** `70_product/tasks/huangyaoshi-next-tasks.md`

只有一个事：

**把 `frameworks/`、`tools/`、`cases/` 加到 Graph RAG 扫描目录**

老顽童把桥接卡放在 `30_wiki/frameworks/` 和 `30_wiki/tools/`，纪浩案例放在 `30_wiki/cases/`。当前 `_collect_all_wiki_pages` 没扫这三个目录，这些卡不会被摄入图。

改 `graph.py` 的 `_collect_all_wiki_pages`：

```python
wiki_subdirs = [
    root / "30_wiki" / "concepts",
    root / "30_wiki" / "frameworks",   # 新增
    root / "30_wiki" / "tools",         # 新增
    root / "30_wiki" / "cases",         # 新增
    root / "30_wiki" / "systems",
    root / "30_wiki" / "entities",
    root / "30_wiki" / "decisions",
    root / "30_wiki" / "projects",
]
```

做完 `kdo graph rebuild --full`。5 分钟。

**做完后 Task E 正式关门，黄药师待命。**

---

## 王语嫣

**任务文件：** `70_product/tasks/wangyuyan-next-tasks.md`

### 自迭代提案

你产的 `proposal-self-learning-cron.md` 我还没完整审查。等我审完会给反馈。

### 诊断

继续核心职责。如果有新的概念缺口，按之前格式在诊断记录 Gap 节标注。

---

## 洪七公

**当前无任务。** 待命。

---

# 老顿童（laowantong）完成记录 · 2026-06-11

## 完成汇总

| 任务 | 状态 | 产出物 |
|:-----|:----:|:--------|
| 桥接卡量产：Hypothesis-Driven 系列 | ✅ | `30_wiki/frameworks/concept-mckinsey-hypothesis-driven.md`<br>`30_wiki/tools/skill-mckinsey-hypothesis-driven-workflow.md`<br>`30_wiki/concepts/dk-mckinsey-hypothesis-driven-pitfalls.md` |
| 桥接卡量产：5 Whys | ✅ | `30_wiki/tools/concept-toyota-5-whys.md` |
| 课转卡自查 | ✅ | 30 张课转技能卡全部补上"判断标准"小节（`skill-一堂-*` 7 张 + `skill-纪浩-*` 23 张） |
| 旧卡补互链 | ✅ 部分 | 已补 28 张核心卡片（`skill-纪浩-*` 16 张 + `frameworks/` 3 张 + `tools/` 9 张）；全库仍有约 800+ 张卡缺 related，后续按"有空时逐步补" |

## 质量门槛

- 4 张桥接卡全部通过三条红线：Bridge 节 ✓、bridges_to ≥1 条 ✓、Synthesis 链接 ≥5 个且同域横向 ≥2 个 ✓
- Hypothesis-Driven 攻击者：Kahneman（确认偏误）+ Eric Ries（精益创业）
- 5 Whys 攻击者：Taleb（过度简化）+ Senge（系统思考）

## 额外修复

- 修复 `30_wiki/tools/concept-mckinsey-issue-tree.md` frontmatter YAML 引号嵌套错误
- 修复 `30_wiki/concepts/case-truman-poker-deck-roi.md` title YAML 引号嵌套错误
- 全库 YAML 解析错误从 2 个降至 0 个

## 待后续处理

- 全库约 800+ 张卡片仍缺 related 或 related<2，建议按优先级（frameworks → tools → concepts → skills/cases）分批补充
- 部分纪浩技能卡的 related 采用了"通用相关——纪浩体系总纲+真需求四要素"，后续可根据各卡主题精细化

