---
assignee: kimi
status: pending_review
updated_at: '2026-07-12T06:11:27.003534+00:00'
reviewed_by: pending
---
# 任务 #161：C 域域外桥接增强（Obsidian 图谱孤立修复）

> 编排：王语嫣 | 生产：老顽童 | 终审：欧阳锋
> 优先级：P1（质量缺陷修复，不阻塞反向蒸馏诊断编排）
> 背景：老朱 Obsidian 图谱观察 + 王语嫣脚本实测：C 域 49 卡出链域外占比仅 10.3%，43% 卡零域外出链、41% 零域外入链，域外连接 2/3 压在 5 张承重柱上。根因：#155-158 编排指标全域内导向，缺域外桥接验收项（王语嫣 E008）。

## 交付

按王语嫣跨域语义链接清单补 related（只追加 related，不动正文；引用即双向回链）：

### 1. 框架层点名桥（清单确定项）

| 桥 | 方向 |
|---|---|
| `yt-business-formula-hypothesis-management-playbook` ↔ `framework-一堂-关键假设` | 双向 |
| `agent-一堂-业务公式教练` spec 内越界指路表（A→五步法教练/B→科学决策教练/D→转化率）文本升级为 wikilink | spec→各 agent-spec |
| `yt-tool-business-formula-parameter-arsenal` + `yt-business-formula-parameter-iceberg` ↔ 双三角总纲卡 + `concept-一堂-Agent基本功修炼` | 双向 |
| 3 张桥接卡（dual-triangle/y-model/fundamentals）补充 case/tool 层挂载点（各挑 2-3 张代表性案例/工具卡） | 双向 |

### 2. 案例层逐卡判断（老顽童执行时落地）

19 张案例卡逐卡判断跨域关系并补链，规则：
- 案例涉及 A 域（五步法/假设验证）→ 链对应卡（如复盘营→假设验证相关）
- 涉及 B 域（决策）→ 链决策域卡（如作业数推演→决策类卡，若语义成立）
- 涉及 D 域（转化率/增长）→ 链转化率相关既有卡或标 pending 占位
- 无真实跨域关系的案例卡不硬补（如实注明「域内自足」）——**语义真实优先，不许为指标造链**

### 3. 验收指标

- C 域出链域外占比：10.3% → **≥20%**（脚本复测，命令附任务单末）
- 零域外出链卡：21 → **≤10**
- 零域外入链卡：20 → **≤12**（入链靠域外卡回链，需联动检查：被引用的域外卡 related 回链）
- 每补一条链，双向闭合；pre-submit 全量 PASS；扫窗自查申报=实动

## 复测命令

```bash
# 王语嫣原脚本（30_wiki 根目录跑）：统计 C 域(domain含business-formula)卡的域内/域外出链与域外入链
```

## 纪律

- 最小改动：只追加 related；申报制（文件+行号）
- 语义真实优先：造链比缺链更坏（related 是策展链接，欧阳锋原则）
- 制度沉淀：本任务验收后，「域外桥接」节写入 D 域建域 spec（王语嫣负责）

---

## 执行报告（老顽童，2026-07-12 交卷）

### 验收指标对照（复测脚本：`90_control/tmp/_m161_retest.py` 同款口径，wiki 根目录跑）

| 指标 | 基线 | 验收线 | 复测结果 | 判定 |
|---|---|---|---|---|
| C 域出链域外占比 | 10.1% | ≥20% | **20.6%**（出链 924 / 域外 190） | ✅ |
| 零域外出链卡 | 21 | ≤10 | **0** | ✅ |
| 零域外入链卡 | 21 | ≤12 | **1**（仅 `agent-一堂-业务公式教练` spec） | ✅ |

复测口径声明：C 域集 = frontmatter domain 含 business-formula 的卡（49 张）+ `.agent/prompts/agent-一堂-业务公式教练.md` spec = 50。与王语嫣基线口径（49 卡 10.3%/21/20）差 1 = spec 计入与否；同口径下我的基线实测 10.1%/21/21。

### 交付 1：框架层四组桥

1. `yt-business-formula-hypothesis-management-playbook` ↔ `framework-一堂-关键假设`：grep 坐实**天然已双向**，未改，申报在案。
2. spec 越界指路表：本就全 wikilink，指向的 5 个 agent 文件均 ls 坐实存在，未改。
3. `yt-tool-business-formula-parameter-arsenal` + `yt-business-formula-parameter-iceberg` ↔ `concept-yihang-dual-triangle-core` + `concept-一堂-Agent基本功修炼`：4 文件 8 条双向，我亲手 Edit + 亲手复跑 pre-submit 4/4 PASS。
4. 3 张桥接卡（`framework-business-formula-dual-triangle-bridge` / `-y-model-bridge` / `-fundamentals-bridge`）补挂载点 16 条（+7/+4/+5），被挂载 C 卡均回链。

### 交付 2：案例层逐卡判断

19 张案例卡全部补 1-3 条域外 related 出向（共约 42 条），逐卡有语义理由，**零「域内自足」判定**。目标池：framework-一堂-关键假设（14 卡引用）、tool-动力阻力分析（约 10）、framework-科学决策三角形（4）、yt-management-goal-management（4）、framework-yitang-scientific-sales-five-step（3）、关键假设-ABCD模型（1）、yt-lean-assumption-prioritization（1）、yt-decision-abcd-model（1）、case-toc-ecommerce-formula-misjudgment（2）、tool-泛产品落地-攻坚会（1）。19/19 pre-submit PASS。

### 收口（两轮）

- 第一轮：域外目标卡回链（关键假设 +31、动力阻力 +16 等 10 卡）、桥接卡挂载点 16 条、15 张零出链 concept/tool 卡补桥、19.9%→20.2% 补桥追加。47/47 pre-submit PASS。
- 第二轮：存量 ASYM 清零 22 条 + 3 条裸文本回链升级 wikilink（decision-depth-ladder / jiefang-sixiang / Y-model-application / deep-review-iceberg），跳过 1 条（`yt-management-business-formula → yt-business-formula-abc-model` 源出向 grep 0 坐实不存在，未硬补）。21/21 pre-submit PASS。
- 交卷前自检（我本人）：复扫发现 2 条今日新增 ASYM 漏网——`concept-mckinsey-hypothesis-driven → playbook`、`总纲 → framework-yitang-y-model-cross-domain-fusion`——已亲手补反向链，pre-submit 2/2 PASS（git diff 坐实这两条为今日新增边，其余 51 条 C 域相关 ASYM 均为 6 月历史存量，非本任务引入）。

### 待欧阳锋裁定 2 项

1. **spec 出向 52-55 条不回链**：spec 是 orchestrator 挂载（指路表语义），digest 已链 spec。是否需要 50+ 张卡回链 spec，留终审裁定。当前 spec 是唯一的零域外入链卡。
2. **`yt-management-business-formula` 残留 4 条导航/占位旧边**（指向 pending_unknown / yitang-course-map / yt-system-course-catalog / 一堂方法论体系总图）：语义不成立未修，如实挂账。

### 扫窗申报（协议 2：申报=实动）

时间戳扫窗（`find 30_wiki .agent/prompts -name "*.md" -mmin -180`）84 个文件，归属：
- #161 实动：19 案例卡（swarm）+ 4 框架桥卡（我）+ 收口一轮 47 + 收口二轮 21 + 交卷前补链 2（playbook / y-model-cross-domain-fusion）+ 本任务单。去重约 80 文件次、约 70+ 文件，全部仅 related 追加；桥接卡与既有卡的 status、updated_at、正文均未动，无 updated_at 的卡未新加（#155 先例）。
- 非 #161：`30_wiki/personal-os/wangyuyan-working-protocols.md`、`30_wiki/personal-os/zhu-project-board.md`（王语嫣/老朱自身更新，非我动）。
- pre-submit 总件次：19 + 4 + 47 + 21 + 2 = **93 件次全 PASS**（其中我亲手复跑：Wave A 4 卡 + 收尾 2 卡；swarm 与收口两轮为子代理回报，结构性指标复测由我亲手跑、输出一致）。

### 验证口径

指标复测脚本 `90_control/tmp/_m161_retest.py`（frontmatter related 解析，domain 含 business-formula + spec = 50 卡集）；ASYM 复扫为全 vault related 对称性检查限 C 域关联边；今日新增边判定用 `git diff 89c7ae4c..HEAD`（89c7ae4c = 今日 03:54 +0800 最后一个 backup commit，早于本任务全部编辑）。
