---
id: "diag_20260611_huangyaoshi-producer-experience"
type: "diagnosis_record"
created_at: 2026-06-11
status: "completed"
source: "黄药师（Builder）临时体验Producer角色，执行Task F"
---

# 黄药师 Producer 体验报告：五步法审计 + 工具链摩擦

> Task F：Builder 临时做一次 Producer，走完整生产流程，记录摩擦点。

---

## 五步法审计

### 覆盖评估

| 步骤 | 卡数 | 判断 | 缺口 |
|:----|:---:|:-----|:-----|
| 需求分析 | 25 | 充足 | — |
| 产品内核 | 8 | 有核心缺实操案例 | 缺"如何判断产品内核是否验证通过"的判断标准卡 |
| 商业模式/单元模型 | 54 | 非常充足 | — |
| **增长** | **7** | **框架多实操少** | **缺"从产品内核到增长的衔接判断"、"第一个增长杠杆的选择方法"** |
| **壁垒** | **5** | **最薄弱** | **缺"真壁垒 vs 假壁垒的判别案例"** |

### 最明显缺口

**第三步（商业模式）到第四步（增长）之间的衔接盲区。** 

现有增长卡（7 张）全是框架/周期模型/获客工具，没有一张讲"**什么时候可以开始做增长**"这个前置判断。结果是生产者学完增长篇后，知道增长有哪些类型，但不知道自己的项目是否"准备好了"可以进入增长阶段。

选此缺口，产出一张 case 卡：`case-five-step-growth-first-lever`——三个跨越案例（产品内生增长/渠道匹配增长/定价结构增长），含 LTV/CAC≥3 的衔接判断标准。

### v1.5 验证结果

PASS。external-attacks + dont-use + action-triggers 全部通过。

---

## 工具链摩擦

### 摩擦 1：`kdo produce` 不能创建 wiki 卡片 🔴

`kdo produce content/article` 只能产出 `40_outputs/` 下的发布物（文章/视频/教程），不能创建 `30_wiki/concepts/` 下的知识卡片。作为 Producer 的核心工作（写卡），没有 CLI 工具支持骨架生成。

**建议**：增加 `kdo scaffold --card <id>` 的增强版，或新增 `kdo produce wiki/concept --topic`。当前 scaffold 只补缺失信号（Critique/Synthesis），不创建新卡。

### 摩擦 2：`kdo validate --v15` 表分隔符识别 bug 🔴

Validator 的 `_count_dont_use` 和 `_count_action_triggers` 用 `line.strip().startswith("|---")` 识别 Markdown 表分隔行。但标准 Markdown 表支持对齐格式 `|:---|:---|`，导致用对齐格式的表被判定为 0 行。

**复现**：写 `| 列1 | 列2 |\n|:---|---:|` → validate 报 count=0。

**建议**：改为 `re.match(r'^\|[-: ]+\|', line.strip())` 兼容对齐格式。

### 摩擦 3：`diagnostic_signals` 缺默认提示

`_check_diagnostic_signals` 正确报了 WARN，但 case 卡写 diagnostic_signals 比较费力——需要人工构思 signal/framework_lens/follow_up_question 三元组。目前没有模板或提示词帮助。

**建议**：`kdo scaffold` 或 `kdo enrich` 对 framework/tool/case 卡自动预填 diagnostic_signals TODO 骨架（已在 E2 中实现 enrich 预填，但 scaffold 还没做）。

### 摩擦 4：三步编译法的"对标"步骤缺自动辅助

写 Synthesis 时需要手动查同域卡片、手动判断关系类型、手动写 ≥30 字关联说明。这些都是纯手工活，容易遗漏。

**建议**：`kdo cards --domain <domain>` 已经能列出同域卡，但如果能自动建议"可能相关的卡片"（基于 title/query_triggers 相似度），对标效率会大幅提升。这其实是 Graph RAG 的 `kdo graph query` 已经在做的事——只是没有集成到写卡流程里。

---

## 我的建议

| 优先级 | 改什么 | 为什么 |
|:--|:-----|:-----|
| P0 | 修 validate 表分隔符对齐格式 bug | 一行正则的事，影响所有使用标准 Markdown 表的生产者 |
| P1 | `kdo scaffold` 增加创建新卡功能 | 让 Producer 可以通过 CLI 创建卡片骨架，而不是全部手写 YAML frontmatter |
| P2 | `kdo enrich` 的 Synthesis 建议 | 在 enrich 阶段自动推荐可能相关的卡片和关系类型 |
| P3 | diagnostic_signals 预填骨架 | E2 已有 enrich 预填，补 scaffold 预填即可 |

---

黄药师（Builder 体验 Producer）
2026-06-11
