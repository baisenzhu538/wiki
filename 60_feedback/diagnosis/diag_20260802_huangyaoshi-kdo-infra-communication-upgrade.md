---
id: diag_20260802_huangyaoshi-kdo-infra-communication-upgrade
type: diagnosis
author: 黄药师
status: proposal
created_at: 2026-08-02
domain: kdo
priority: P1
source: 讲香基本功-李頔-260731 口述稿分析
target: KDO CLI 全部用户触达面（lint / query / pre-submit / cap_hub / MCP / dashboard）
---

# KDO 基础设施"讲香"升级——诊断与任务建议书

> **来源**：黄药师分析李頔《讲香基本功》口述稿（260731），从基础设施视角提取可落地的 CLI 表达升级方案。
> **阅读对象**：欧阳锋（审查优先级）、王语嫣（编排入队）、老顽童（了解 CLI 输出将更可读）。
> **状态**：建议书——待欧阳锋终审确认优先级后，王语嫣拆为任务单入 production-queue。

---

## 一、背景

### 1.1 讲香十指模型概要

李頔将"把价值讲出来"的能力拆解为两只手十根手指：

| 方向 | 五指策略 | 解决的问题 |
|:--|:--|:--|
| **向下做具体** | 场景化 / 口语化 / 数字化 / 故事化 / 素材化 | 用户听不懂、看不见、没有体感 |
| **向上拉价值** | 比喻化 / 情绪化 / 金句话 / 冲突化 / 升华化 | 用户觉得平淡、记不住、不愿意行动 |

### 1.2 为什么基础设施需要"讲香"

KDO CLI 是用户和知识工厂之间的唯一界面。命令输出质量直接影响：

- **老顽童**能否快速理解 lint 错误并修复（减少返工轮次）
- **欧阳锋**审查时看到的是裸数据还是有上下文的诊断
- **王语嫣**编排任务时能否一眼判断工具成熟度
- **外部 Agent（小昭等）**通过 MCP 调用 KDO 时能否正确判断卡片适用性

当前 CLI 输出全部处于"讲香 V1"水平——功能正确但价值感缺失。这导致：用户知道命令能跑通，但不知道"用了之后比不用好在哪"。

---

## 二、当前诊断

### 2.1 各 CLI 触点讲香评分

| 触点 | 当前状态 | 讲香评分 | 核心问题 |
|:--|:--|:--:|:--|
| `kdo lint` 错误输出 | `DK_SECTION MISSING: ## Critique` | 40 | 像编译器报错，不像人在帮你 |
| `kdo query` 结果 | JSON / markdown 裸数据 | 50 | 返回"有什么"，不返回"你该看哪个" |
| `kdo pre-submit` 输出 | `GATE FAILED — 3 errors` | 40 | 失败像惩罚，通过像废话 |
| `cap_hub list` | 文件名列表 | 30 | 完全不可用——不知道每个工具是干什么的 |
| MCP `kdo_search` tool desc | 技术参数说明 | 40 | 外部 Agent 不知道怎么用、何时用 |
| `kdo lint --incremental` 报告 | 数字表格 | 50 | 数字对，但不知道意味着什么 |

### 2.2 跨触点共性根因

1. **缺场景化**：所有输出都在说"命令做了什么"，没说"你什么时刻会需要它"
2. **缺口语化**：错误消息像编译输出而非结对编程
3. **缺数字化+解释**：给了数字但没有锚点判断好坏
4. **缺情绪化**：失败无路径感，通过无成就感
5. **缺升华化**：用户觉得在"写配置/修格式"，不知道在"训练未来 AI 的商业判断力"

---

## 三、分触点迭代建议

### P0-1：`kdo lint` 错误消息场景化+口语化

**当前**：
```
[ERROR] 30_wiki/dk/dk-xxx.md: DK_SECTION MISSING: ## Critique
```

**目标**：
```
[ERROR] 30_wiki/dk/dk-xxx.md: DK_SECTION MISSING: ## Critique
💡 缺 Critique = 只讲了观点没接受质疑。欧阳锋终审会直接退回。
   在"与其他知识的关联"后面加 ## Critique 节，补上再提交省一轮往返。
```

**实现量级**：在 `kdo_lint.py` 中新增 `HINT_MAP` 字典（~15 行），`validate_file()` 输出时追加提示行。

**为什么先做这个**：今天刚实现的 R1/R2 门禁直接受益——门禁拦住之后如果给的是干巴巴的错误码，老顽童照样不知道怎么修。加上场景化提示，门禁从"警察"变成"教练"。

---

### P0-2：`cap_hub list` 场景化

**当前**：
```
tools/agent-spec-duanwangye-publisher.md
tools/agent-spec-hongqigong-multimodal.md
```

**目标**：
```
📦 段王爷发布引擎      — 内容→飞书/多渠道分发
📦 洪七公多模态引擎    — OCR/VLM/图片→prompt
📦 kdo_search MCP      — 外部 Agent 检索 KDO 知识库
🔧 health-check        — 全库健康度扫描
```

**实现量级**：在 `cap_hub/registry.py` 扫描时读取卡片 frontmatter 的 `one_liner` 或 `description` 字段作为标签。

**为什么先做这个**：`cap_hub list` 是各 Agent 启动必跑命令（startup.md 要求），现在是全厂最"不讲香"的触点。30 分→70 分的改进只需读一个 frontmatter 字段。

---

### P1-1：`kdo pre-submit` 输出情绪化+升华化

**当前（通过时）**：
```
✅ GATE PASSED — zero new errors on submitted files.
Ready to submit for review.
```

**目标（通过时）**：
```
✅ 门禁全绿 —— 6 张卡 0 新增错误
   这批发给欧阳锋，他可以跳过格式检查专注审内容深度。
   你省一轮退回往返，他省一小时格式纠错。
   Ready to submit for review.
```

**当前（失败时）**：
```
❌ GATE FAILED — 3 new error(s) on submitted files:
  [ERROR] dk-xxx.md: DK_SECTION MISSING: ## Critique
```

**目标（失败时）**：
```
⚠️ 提交被拦截 —— 3 个问题需要在交欧阳锋审查前修掉
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  [ERROR] dk-xxx.md: DK_SECTION MISSING: ## Critique
  💡 补上再提交。修完→跑 pre-submit→通过→欧阳锋只看内容不看格式。
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
修完这 3 个问题，pre-submit 通过后提交。
欧阳锋审查带门禁通过的卡平均快 3 倍。
```

**实现量级**：修改 `pre_submit.py` 的 main() 输出段，~30 行。

---

### P1-2：`kdo query` 结果场景路由

**当前**：返回卡片列表（按 RRF 排序），用户需要逐张看再判断哪张适合自己。

**目标**：返回结果时按 `scene` 标签分组：
```
🔍 "怎么判断需求是真需求还是伪需求"

📌 如果你在做新项目立项 →
   [[yt-demand-analysis-evaluate]] — 评估三角形

📌 如果你在审查别人的方案 →
   [[dk-demand-analysis-four-forces]] — 四种力量建模

📌 如果你在复盘失败项目 →
   [[case-demand-financial-literacy]] — 刚性误判的真实案例

没找到？试试 "需求分析+避坑" 或 "JTBD+场景错配"
```

**实现量级**：在 `delivery.py` 的 RRF 融合后增加场景分组逻辑，利用已有的 `tags.scene` 字段。

---

### P1-3：MCP `kdo_search` 工具描述场景化

**当前**：
```python
"description": "Search KDO wiki knowledge base using hybrid retrieval"
```

**目标**：
```python
"description": "当你需要查商业方法论、找案例支撑论点、验证某个概念是否存在时调用此工具。搜不到时试试换关键词或加域限定（如 domain:demand）。返回带溯源链接+场景标签的卡片列表。"
```

**实现量级**：修改 `kdo-tools/mcp/tools.py`，1 行字符串替换。

**为什么重要**：外部 Agent（小昭、Codex）通过 MCP 调用 KDO 时，tool description 是它们判断"何时调用"的唯一依据。当前技术描述让 Agent 不知道该不该调、调了能拿到什么。

---

### P2-1：健康仪表盘数字化+冲突化

**当前**：
```
综合健康分: 55/100
source_refs 覆盖率: 80.5%
draft 率: 29.4%
定位声明覆盖率: 14%
```

**目标**：
```
📊 KDO 健康分 55/100
   2,500 张卡 → 约 1,125 张还有改善空间
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴 定位声明  14% — 每 7 张卡只有 1 张讲清了自己"凭什么存在"
   老顽童上次交的 5 张卡 5/5 全齐 → 差距不在能力在覆盖
🟡 draft 率  29.4% — 接近三分之一未出草稿
   目标：月度降至 20%
🟢 source_refs 80.5% — 五张卡有四张可溯源
   目标：月度 90%
```

**实现量级**：修改 `health-check.py` 输出格式，~40 行。

---

### P2-2：CLI 全局——设计原则文档

将讲香十指模型编译为 KDO CLI 输出设计规范，写入 `90_control/cli-design-principles.md`：

| 讲香原则 | CLI 输出规范 | 反模式 |
|:--|:--|:--|
| 场景化 | 每条输出告诉用户"这和你什么场景有关" | "missing required field" |
| 口语化 | 用"你"，不用第三人称 | "the user must provide..." |
| 数字化+锚点 | 给数字时附参照基准 | "8254 errors"（不知道好坏） |
| 情绪化 | 失败给路径感，通过给成就感 | "FAIL" / "PASS" 两个字 |
| 比喻化 | 复杂概念给锚点 | "Graph RAG 索引" |
| 升华化 | 关联更大价值 | "修了一个 YAML 字段" |

---

## 四、优先级矩阵

| 编号 | 触点 | 改动量 | 影响面 | 优先级 | 理由 |
|:--|:--|:--|:--|:--:|:--|
| P0-1 | lint 错误消息 | ~15行 | 老顽童每次提交 | **P0** | 今天刚上线的门禁直接受益 |
| P0-2 | cap_hub list | ~20行 | 全员每次启动 | **P0** | 最低评分(30)→最高提升空间 |
| P1-1 | pre-submit 输出 | ~30行 | 老顽童+欧阳锋 | **P1** | 每次提交必经 |
| P1-2 | query 结果 | ~50行 | 全员检索 | **P1** | 检索是最高频操作 |
| P1-3 | MCP tool desc | ~1行 | 外部 Agent | **P1** | 1 行改动→影响所有外部调用 |
| P2-1 | 健康仪表盘 | ~40行 | 欧阳锋+王语嫣 | **P2** | 周期性查看，非高频 |
| P2-2 | 设计原则文档 | 新文件 | 全员 | **P2** | 写一次，长期参考 |

---

## 五、边界与依赖

- **不改 CLI 行为逻辑**：只改输出格式和提示文本。参数、返回值、协议全部不变。
- **不依赖新依赖**：纯文本修改，零新增依赖。
- **P0 项不跨角色**：都在黄药师职责范围内（kdo_lint.py / cap_hub / registry.py）。
- **P1-P2 项需要王语嫣编排**：P1-1 涉及 pre_submit.py 输出，P1-2 涉及 query 展示逻辑，实际影响老顽童工作流。
- **不追溯旧输出**：改完之后新输出即生效，不要求回填历史日志。

---

## 六、验收方式

| 编号 | 验收标准 |
|:--|:--|
| P0-1 | 跑 `kdo lint` 对缺 Critique 的 dk 卡输出带 `💡` 场景化提示 |
| P0-2 | 跑 `python -m cap_hub list` 输出包含每个工具的一句话用途描述 |
| P1-1 | 跑 `kdo pre-submit` 通过/失败分别输出带路径感的描述 |
| P1-2 | 跑 `kdo query "需求分析"` 返回结果按 scene 分组 |
| P1-3 | MCP tool list 中 kdo_search 描述改为场景化文本 |
| P2-1 | 跑 `python health-check.py` 输出含参照基准和趋势判断 |
| P2-2 | `90_control/cli-design-principles.md` 存在且可读 |

---

## 七、参考

- 讲香基本功口述稿：`00_inbox/讲香基本功-李頔-260731/讲香基本功-李頔-260731-口述.txt`
- 讲香十指模型超级武器库（小抄）：随课发放
- 黄药师行为牌 B5：先读口述稿全文再下结论（本次执行）
- 黄药师行为牌 B6：先找 MOC 再回答（本次未触发——无已有域 MOC 覆盖此主题）
- KDO 基础设施现状：`90_control/scripts/kdo_lint.py` / `pre_submit.py` / `cap_hub/registry.py`

---

*黄药师 · 2026-08-02*
*建议书状态：待欧阳锋终审确认优先级，待王语嫣拆分入 production-queue*
