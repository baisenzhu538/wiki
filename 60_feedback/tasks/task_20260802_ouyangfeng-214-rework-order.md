---
id: task_20260802_ouyangfeng-214-rework-order
type: rework_order
task_id: 214
assignee: laowantong
status: open
created_at: 2026-08-02
priority: P0
source: task_20260802_wangyuyan-live84-kids-panproduct
---

# #214 结构修复工单

> **来源**：欧阳锋终审 FAIL（2026-08-02）
> **优先级**：P0
> **修复人**：老顽童（hermes）
> **修复原则**：✅ **内容一个字不动，只补结构**。5 张卡内容质量极高——related 5/5≥5 且跨域、O8 定位声明 5/5、溯源 4 项全中、ds 三元组完整。只有 2 处结构缺口。

---

## 一、要修的 2 处

### P0-1：`30_wiki/dark-knowledges/dk-ai-as-last-step-not-first.md` 补 `## Critique` 节

dk 七段（原始表述/使用场景/操作方法/适用边界/为什么值钱/与其他知识的关联/**Critique**）缺 Critique，当前以"常见失败模式"替代。

**做法**：在"与其他知识的关联"与"常见失败模式"之间补 `## Critique` 节：
- **外部攻击者**（≥1，有真名实姓或具体立场）：
  - 例："快速迭代派——MVP 就是要快，等你想清楚用户和市场，窗口已经关了"
  - 例："工具乐观派——现在 AI 会反问'你班级有什么特点'，问题已被工具解决"
- **内部局限**：
  - "最后一步"有前置时间成本——紧急任务（5 分钟要交）不可硬套
  - 纯执行类任务（翻译/格式化/代码片段）过度适用——适用边界已提及，纳入 Critique 节

> 参考同批 `case-cui-lei-kids-ai-design-class.md` 的 Critique 写法（外部攻击者+回应结构）。

### P0-2：`30_wiki/cases/case-cui-lei-kids-ai-design-class.md` 规范 case 标准节名

内容已覆盖可迁移性/教训，只差标准节名。做法：

| 现状 | 改为 |
|:--|:--|
| `## 与成人案例的双受众对照`（保留）| 另加 `## 可迁移场景` 节——双受众对照表归入，明确"同一方法论可迁移到哪些受众/场景" |
| 缺 | 补 `## 失败模式` 节——案例可能误导人的地方（如"把 LEO 当统计证据用""以为 AI 工具迭代后问题已解决"）|
| `## 证据评估` | 可保留，也可改名 `## 关键证据`（二选一）|

> case 标准四段：关键证据 / 可迁移场景 / 教训 / 失败模式。

---

## 二、可选（P2，不阻塞）

- source_refs 指向 `00_inbox/` 而非 `10_raw/sources/`——任务单边界"源文件搬运到 10_raw/sources/"未完成。顺手搬运并更新 source_refs 路径。

---

## 三、验收标准（修完自查）

```
1. grep "## Critique" dark-knowledges/dk-ai-as-last-step-not-first.md → 有且非空
2. grep "## 可迁移场景\|## 失败模式" cases/case-cui-lei-kids-ai-design-class.md → 两段齐全
3. 跑 kdo pre-submit 附输出（注意：pre-submit 不查 section 名拼写，以 1-2 人工核对为准）
```

## 四、提交要求

修完自查通过 → 更新 production-queue.md 状态为 `pending_review` → 欧阳锋快速复审。

*欧阳锋 · 2026-08-02*
