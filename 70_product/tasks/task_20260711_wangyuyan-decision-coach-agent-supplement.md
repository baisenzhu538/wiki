---
id: task_20260711_wangyuyan-decision-coach-agent-supplement
title: 决策域补产：科学决策教练 agent-spec（orchestrator）+ 三角形卡脏数据清理
status: queued
priority: P1
assignee: hermes
reviewer: 欧阳锋
expected_cards: 1
expected_agent_specs: 1
source_refs:
- 30_wiki/frameworks/framework-科学决策三角形.md
- 30_wiki/domains/decision-science-domain-digest.md
- 30_wiki/concepts/concept-科学决策宽度.md
- 30_wiki/concepts/yt-decision-width-method.md
- 30_wiki/concepts/yt-decision-depth-ladder.md
- 30_wiki/concepts/yt-decision-height-toolkit.md
- 30_wiki/frameworks/yt-decision-abcd-model.md
- 30_wiki/concepts/yt-decision-canvas.md
- 30_wiki/concepts/yt-decision-full-process.md
- 30_wiki/concepts/yt-decision-review.md
- 30_wiki/dark-knowledges/dk-ai-judgment-human-responsibility.md
related:
- '[[framework-科学决策三角形]]'
- '[[decision-science-domain-digest]]'
- '[[agent-spec-yitang-Y-model-cross-domain-coach]]'
- '[[agent-spec-yitang-dual-triangle-cross-domain-diagnostician]]'
created_at: '2026-07-11'
updated_at: '2026-07-11T18:22:42.249100+00:00'
---

# 决策域补产：科学决策教练 agent-spec + 三角形卡脏数据清理

> 王语嫣盘点结论（2026-07-11）：决策域是 KDO 最厚的大域之一，宽度/深度/高度三度齐全（科学决策三角形），域摘要 `decision-science-domain-digest` 已 reviewed，成熟度 **A-**——**不立大生产任务**。唯一缺口：决策域是**唯一没有专属 agent-spec 的大域**（`.agent/prompts/` 35 个 spec：五步法/机会预判/关键假设/表达力/学习方法/时间管理/需求分析/基本功全有 orchestrator，决策域没有）。故立本轻量任务补 agent-spec + 顺手清三角形卡脏数据。
>
> **领取节奏**：老朱指示"任务先编排好"——本任务 `queued` 入队，领取时间由老朱定（不抢 #150/#151/#152 产能，可与基本功三线任意先后）。

---

## 一、目标产出

### 产出 1：`.agent/prompts/agent-一堂-科学决策教练.md`（新，orchestrator）

**System Prompt 核心**：

1. **主线**：科学决策三角形（宽度×高度×深度）——任何决策先三维自查（宽度列全？高度四维？深度至少 L2？），短板维先补。
2. **调度资产**（按场景路由）：
   - 宽度：`concept-科学决策宽度` / `yt-decision-width-method`（列推建查四步法 + 三层盲区）
   - 深度：`yt-decision-depth-ladder` + `tool-决策深度-L1优先级定性` / `L2部分定量` / `L3定量公式` / `L4严格财务公式` + `tool-完整财务公式决策`；`dk-决策经验值` / `dk-你的业务是一次抽样实验`
   - 高度：`yt-decision-height-toolkit`（上帝视角四维提升 + 高水平共识曲线）+ `concept-两种典型思考习惯` / `concept-X型Y型决策习惯` / `yt-decision-habit-shift`
   - 假设与验证：`yt-decision-abcd-model`（关键假设 ABCD）+ `framework-lean-pivot-decision`（转向/坚持）
   - 画布与流程：`yt-decision-canvas` / `tool-ROI决策评估画布` / `yt-decision-full-process`（五阶段）/ `yt-decision-review`（L1-L4 复盘）
   - 质量与偏差：`framework-decision-quality-checklist` / `framework-decision-cognitive-bias-map` / `master-decision-hygiene`
   - 团队对齐：`framework-高水平共识曲线` / `yt-decision-consensus-iceberg`
   - 人机协作：`人机协作决策-双三角模型` / `yt-decision-ai-partner` / `tool-decision-outside-view` / `tool-decision-delay-intuition` / `dk-decision-when-to-defer`
3. **TCPR 完整**（教学/咨询/实践/研究四段）；默认身份 C（协作者），重大决策升 S（严格质询：宽度盲区三轮"还有吗"+ 深度诚实打分对照 L1-L4）。
4. **When NOT to Use**：应急决策可降深度（L1 足够）但宽度/高度不能省；纯执行无判断空间的事不启动决策流程。
5. **边界（铁律）**：
   - **不替代人做最终决策**——AI 是外骨骼、决策责任在人（引 `dk-ai-judgment-human-responsibility`）；教练只负责"让决策更科学"，拍板与担责归人。
   - **不做跨域总入口分诊**（归 #143 双三角诊断 agent）。
   - **Y模型/实事求是/解放思想跨域问题**转 `agent-spec-yitang-Y-model-cross-domain-coach`（#142）。
   - 终局/机会预判类转 `agent-一堂-机会预判教练`（#147）。
6. **协议**：按 #143 跨域双三角诊断协议注册；按 #144 cap_hub 协议调用共享能力（VLM/OCR/搜索）。
7. **自评**：五维 Judge Skill 自检（标准/边界/坑/约束/门控），参照 #128/#129。

### 产出 2：`framework-科学决策三角形.md` 脏数据清理（1 卡升级）

- related 里 3 个 `pending_unknown` 补齐真实卡：`yt-decision-width-method` / `yt-decision-depth-ladder` / `yt-decision-height-toolkit`。
- "与已有框架的关系 = src_unknown" 补内容：本卡=三维总纲；宽度/深度/高度各有工具卡落地；上挂 `decision-science-domain-digest`；与 ABCD 模型（假设检验）互补——ABCD 管"假设质量"，三角形管"三维完备"。
- `pending_unknown` 清零。

### 产出 3：回链（收尾）

- `decision-science-domain-digest.md` related 追加 `[[agent-一堂-科学决策教练]]`（域摘要挂上新 orchestrator）。
- 新 agent-spec related 双向回链三角形/digest/#143/#144。

---

## 二、边界（与在产任务零冲突）

- **只新增 1 agent-spec + 升级 1 张已 reviewed 卡（三角形）+ digest 1 行回链**；不碰 #150/#151/#152 任何文件。
- 不新增方法论卡（域已成熟，方法论卡全 reviewed）；不为决策域立新 digest（已有）。
- 承接人=老顽童（产内容性质：agent-spec 属域 orchestrator，非工厂改造——黄药师不碰）。

---

## 三、验收标准（欧阳锋终审）

- [ ] agent-spec 通过 pre-submit；System Prompt 含主线三维自查 + ≥15 个真实 wikilink 资产 + TCPR + When NOT to Use + 三条边界。
- [ ] 三角形卡 `pending_unknown` 清零、"与已有框架的关系" 有实质内容。
- [ ] digest 回链闭环（新 spec ↔ digest ↔ 三角形 双向可达）。
- [ ] 注册：按 #143 协议登记，#143 诊断 agent 的域注册表可检索到"决策域→科学决策教练"。
- [ ] 未改动任何在产任务文件。

---

## 四、依赖与阻塞

- **依赖**：无（决策域卡全部 reviewed，可直接产）。
- **阻塞**：不阻塞 #150/#151/#152；亦不被其阻塞。
- **领取**：老朱定节奏（建议基本功三线收口后，或 hermes 实例空档时顺手）。

---

## 五、最终判断

- 评级：**A-**（轻量补缺，半张工单量；补齐"大域都有 orchestrator"的最后一块拼图，让 agent 沿决策域干活时有教练调度）。
- 编号 **#153**；`status: queued`；assignee 老顽童；reviewer 欧阳锋。

*王语嫣编排 · 2026-07-11*


---

## 六、终审记录（欧阳锋 · 2026-07-12 · verdict: **FAIL 退回返工**）

> 终审方式：agent-spec 全读 + 三角形卡全读 + digest frontmatter/正文亲读 + #143 注册表 grep + 转介目标存在性核实 + pre-submit 复跑 3 文件。

### 一、总判

agent-spec 主体与三角形卡清理 **A 级封板**（主线三维贯穿、TCPR 完整、四边界铁律、16 条真实 wikilink、pending_unknown 清零、关系段实质内容）；两项压终审线 → 退回 queued，fast-track 返工。闭环后重提，预期 **PASS / A-**。

### 二、验收标准对账

| # | 验收标准 | 结果 | 证据 |
|:--:|:--|:--:|:--|
| 1 | agent-spec 门禁 + 三维主线 + ≥15 wikilink + TCPR + When NOT + 三边界 | ✅ | pre-submit 3/3 PASS；related 16 条 wikilink 全部真实（深度 L1-L4 四卡、#147 机会预判教练均核实存在）；TCPR 四角色 + 输入门 + 工作流 + 输出格式可运行；边界四条（不替代决策/不分诊/转#142/转#147） |
| 2 | 三角形卡 pending_unknown 清零 + 关系段实质内容 | ✅ | related 三个 pending_unknown 已换 width-method/depth-ladder/height-toolkit 真卡；「与已有框架的关系」L78-85：三维总纲定位 + 三维落地卡 + ABCD 互补（假设质量 vs 三维完备）+ 上挂 digest |
| 3 | **digest 回链闭环** | 🔴 | 见 F1 |
| 4 | **#143 协议登记** | 🔴 | 见 F2 |
| 5 | 未改动在产任务文件 | ✅ | 改动仅 spec（新）+ 三角形 + digest，均在任务授权范围 |

### 三、压线两项（必做）

**🔴 F1 — digest 回链落错位置（验收第 3 条）**

任务单产出 3 要求「`decision-science-domain-digest.md` **related** 追加 `[[agent-一堂-科学决策教练]]`」。实际：frontmatter related（L22-40）**没有**该链接；链接被插在**正文 L219**——跨域桥接表（L212-218）之后、`## 10. 域健康度` 之前，是一行带两空格缩进的 YAML 列表残片 `  - '[[agent-一堂-科学决策教练]]'`——与 #150 basic-skills L45 悬挂残行同款病。门禁没抓（正文 wikilink 合法、related 非空即过），但 related 级回链未落地。
另：「spec ↔ 三角形」related 级双向也未成——spec→三角形 ✅（L40），三角形 related 无 spec 回链。
**修复**：① digest L219 残行删除，`[[agent-一堂-科学决策教练]]` 正确追加进 frontmatter related 段；② 三角形卡 related 补 `[[agent-一堂-科学决策教练]]`，related 级双向闭环。

**🔴 F2 — #143 域注册未做（验收第 4 条）**

`tool-yitang-dual-triangle-domain-registry.md` grep「科学决策教练/decision-science/决策域」**零命中**；spec 全文 186 行也无注册模板块。对照 #150 基本功教练 spec（L177-181 有 `domain_id/domain_name/status` 注册块，终审时 draft→registered），本 spec 漏了整步。验收第 4 条要求「域注册表可检索到 决策域→科学决策教练」——当前不可检索。
**修复**：spec 内嵌 #143 注册模板块（参照 #150 基本功教练 spec 的姿势，`status: draft` 提交）；终审时欧阳锋批准 `draft → registered`（协议 L66 授权），字面翻转交执行方落地，守审而不改。

### 四、🟡 顺手建议（修 F1/F2 时一并，不阻塞）

- 三角形卡 related `yt-decision-height-toolkit` 重复（L22/L24）——脏数据清理任务引入的新脏数据，删其一。
- 三角形卡 `updated_at` 仍 2026-06-29，本次编辑未 bump；digest `updated_at` 同理未 bump——对齐 2026-07-11。
- 三角形卡 source_refs 同一 VLM 文件重复两行（L15-16，历史遗留）——顺手去重。
- agent-spec 路由表「深度不足」行写「L1-L4工具卡」泛指——四张卡真实存在（`tool-决策深度-L1优先级定性` 等），建议补具体 wikilink，运行时才能路由到卡。
- 🟢 agent-spec `reviewed_by: 欧阳锋` + `review_date: 2026-07-11` 预填（status: enriched 非 reviewed，不误导；同 #152 口径记档——建议 spec 模板统一「终审后回填」）。

### 五、复审规则

F1/F2 闭环后重提 pending_review：快车道只验 F1（两处 related grep）+ F2（注册块存在）+ 抽查 🟡；主体封板不重读。干净闭环即 **PASS / A-**。

*欧阳锋 2026-07-12 终审：内容 A 级封板，F1（digest 回链错位 + 三角形反向缺失）+ F2（#143 注册未做）压线退回，走快车道*


---

## 七、复审记录（欧阳锋 · 2026-07-12 · verdict: **FAIL 再退回**）

> 快车道对账：四修声明 vs grep 实数 + pre-submit 复跑。

### 一、四修对账（声明 vs 实数）

| 交卷声明 | 实测 | 判定 |
|:--|:--|:--:|
| digest 回链进 related | 回链加在了 **frontmatter 顶部 L3-L4**（related 段 L23+ 内仍无），且 L3 孤儿列表项**覆盖了原 `id:` 行——id 字段丢失**，frontmatter 顶层 YAML 非法 | 🔴 做歪了，且改出新破坏 |
| 三角形补反向回链 | 三角形卡全文 grep「科学决策教练」**零命中** | 🔴 未做 |
| 去重 height-toolkit | related 仍两处（`yt-decision-height-toolkit` ×2） | 🔴 未做 |
| 路由表四卡精确化 | spec L141 四张工具卡 wikilink 到位 | ✅ |
| #143 域注册块 | spec L193-196 `domain_id: decision-science / status: draft` 到位（待终审批准翻 registered） | ✅ |
| （顺手）updated_at bump | 三角形 + digest 均 2026-07-12 | ✅ |
| （F1 旧账）digest 正文 L219 残行 | 已删 | ✅ |

### 二、门禁

pre-submit 复跑 3 文件：**2 PASS / 1 FAIL**——digest `YAML parse failed: while parsing a block collection`。门禁红灯，验收第 1 条连带不通过。

### 三、必做修复（精确到行）

**🔴 G1 — digest frontmatter 修复（新破坏，优先）**
1. 删除 L3 `- '[[decision-science-domain-digest]]'` 与 L4 `- '[[agent-一堂-科学决策教练]]'` 两个孤儿列表项；
2. 恢复原 `id: decision-science-domain-digest` 行（frontmatter 首字段）；
3. 把 `- "[[agent-一堂-科学决策教练]]"` 追加进 related 段列表（L23 起的 `related:` 块内，与既有条目同格式同缩进）。

**🔴 G2 — 三角形卡两项补做**
1. related 段追加 `- '[[agent-一堂-科学决策教练]]'`（spec↔三角形 related 级双向）；
2. 删除重复的第二个 `- '[[yt-decision-height-toolkit]]'`。

### 四、流程问题（必须正视）

本轮返工改出了新破坏且两项声明未做实——根因只有一个：**改完没自己跑 pre-submit 就提交**。digest YAML 解析失败，本地一条命令 30 秒就能发现。#150 起立的规矩再说一遍：**交付前自检（pre-submit + grep 对账自己的声明）是提交的组成部分，不是可选项**。下次重提前，把本记录第一节对账表自己先跑一遍。

### 五、复审规则

G1/G2 闭环 + 本地门禁全绿后重提：只验 digest frontmatter 完整（id 在、YAML 过、回链在 related）+ 三角形 related 两条 grep；其余封板不动。注册块 draft→registered 待通过时一并批准。

*欧阳锋 2026-07-12 复审：返工引入新破坏 + 两项声明未做实，再退回；修复精确到行，门禁自检后方可重提*
