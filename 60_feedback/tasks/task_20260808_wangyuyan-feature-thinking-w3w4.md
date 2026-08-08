---
id: task_20260808_wangyuyan-feature-thinking-w3w4
task_id: 251
assignee: laowantong
status: reviewed
updated_at: 2026-08-08
domain: ai-basic
priority: P1
---

# #251 Feature 思维 W3 补链 + W4 Agent Spec（规格层——老顽童）

> ⚠️ 范围修正（2026-08-08 王语嫣编排修正——一任务一执行者纪律）：**部署层（层次 2/3）已拆出为 #256（黄药师独立任务）**。本任务仅含老顽童的规格产出：W3 补链（bridge/回链/对账）+ W4 agent-spec 卡。黄药师部署见 `task_20260808_huangyaoshi-basic-skills-coach-deploy.md`（#256）。

## 背景

W1（#249）+ W2（#250）完成后启动。

## W3 补链（3 项）

### 251-A：bridge-双轨Feature体系（黄药师协调 cap_hub）
- **quality-gate Feature（cap_hub/features.json，12 个 lint 类：updated_at/双 aliases/重复 ID/MOC 完整性）vs capability Feature（课程周期表 100 个解题 Feature）**
- 王语嫣已验证：cap_hub features.json 灵感来源注明"Truman Feature思维（口述 L1402-1450）"——**同源但不同用**（欧阳锋洞察 3）
- bridge 卡回答：两个注册表各管什么/为什么不混编/消费端如何区分（lint 规则当解题武器=误用）
- related：[[concept-kdo-feature-registry]]、[[tool-ai-feature-inventory]]、[[framework-truman-feature-layered-system]]

### 251-B：回链（AI 三角·基本功定义段）
- 新卡回链到双三角 AI 基本功体系（口述下 L1434-1444：Feature 思维=双三角基本功第一课）
- 与 [[concept-yihang-dual-triangle-core]] 等双三角卡互链

### 251-C：对账 merge（tool-ai-feature-inventory + 周期表 JSON）
- 将 `tool-ai-feature-inventory` 与 #248 周期表 100 Feature 对账：重叠/互补/冲突
- 产出：对账表（inventory 的 Feature → 周期表编号），不重复建卡

## W4 Agent Spec + 可运行部署（一次到位——用户裁定 B）

### agent-basic-skills-coach（AI 基本功教练 Agent：规格 + 部署 + 实测）

**层次 1：agent-spec 卡（老顽童）**
- 参考先例：#150 苦练基本功域教练 Agent（concept-一堂-Agent基本功修炼）+ #246 复盘教练 agent-spec（已 reviewed）
- TCPR 身份：Coach
- **输入**：用户的 AI 基本功问题（"用哪个 Feature 解决 XXX？""L0-L5 哪层够用？""怎么提高作图质量？"）
- **输出**：Feature 路径建议（从哪个 Feature 开始→叠什么→到什么层级→预期效果）+ 关键警示（"能用 Partner 别上 Workerman""别一上来就搭工作流"）
- **依赖资产**：#248 周期表 JSON（菜单）+ #254 kdo feature 工具（点菜数据源）+ #249 分层体系（判断到哪层够用）+ #250 案例库（证据链）+ 四场景（匹配场景）
- **边界**：不替用户执行（只给路径）；不跑 lint/index；不写 30_wiki
- 迭代日志：飞书王语嫣建议书的输入输出示例作为基线用例

**层次 2：可运行部署（老顽童 + 黄药师能力中台配合）**
- `agents/agent-basic-skills-coach/` 目录落地（CLAUDE.md + system prompt + 数据源接入）
- 工具接入：#254 `kdo feature` 命令（点菜/查询——agent 的 Feature 菜单数据源）
- 运行接入：黄药师能力中台（cap_hub 注册 agent + 工具权限）
- 部署参考：`agents/sales-dialogue-assistant/` 部署模式

**层次 3：实测（用 #252 消费端试点做第一个真实用例）**
- 试点任务由 agent 执行：真实任务 → agent 点菜 5-10 Feature → 测试 → 复盘 → 回填周期表 JSON
- 试点通过 = agent 实测通过（一步两得：消费端协议验证 + agent 验证）

## 验收标准

1. 双轨 bridge 卡：两个注册表边界清晰 + 消费端区分指引
2. 对账表产出（inventory→周期表映射，无重复卡）
3. **agent-spec：注入可用 + 实测示例通过**
4. **部署：agents/agent-basic-skills-coach/ 可运行（cap_hub 注册 + kdo feature 接入 + 真实任务实测）**
5. pre-submit PASS；lint 0 新增

## 依赖

- #249 + #250 reviewed（框架+案例完成，Agent 依赖资产就位）
- **#254 reviewed（kdo feature 点菜工具——agent 的数据源底座）**
- 黄药师配合（cap_hub 双轨确认 + 能力中台接入）
- → **#252 消费端试点依赖本任务部署完成**（试点由 agent 执行）

## 🆕 黄药师先行项（2026-08-08 加注——看板清空后立即启动，不依赖 #249）

黄药师可先行启动 #251 的两个部分（#249 老顽童框架层完成后全量解锁）：

**先行 A：W3-A 双轨 bridge 的 cap_hub 侧输入**
- 产出：cap_hub/features.json 的 12 个 lint 类 Feature 清单（id/name/category）+ 边界说明（与 capability 轨的区分）
- 输入给老顽童的 bridge 卡生产（不阻塞——bridge 卡在 #249 后生产，但输入先行备好）

**先行 B：W4 部署的能力中台接入准备**
- 产出：cap_hub Agent 注册规范确认（参考 agents/sales-dialogue-assistant/ 部署模式）+ agent-basic-skills-coach 的接入预留
- 等 #249/#250 完成 + spec 产出后，直接按规范落部署（加速部署环节）

**验收**：两项产出落盘（60_feedback/ 或 cap_hub 规范文档），#251 全量启动时直接可用。

---

## 补审记录（欧阳锋 2026-08-08，先行 A/B + W4 spec 部分）

**结论：先行产物 PASS（条件），等级 bridge A- / agent-spec A- / 注册规范 ✅**。完整验收等 #249 reviewed + 部署层次 2/3 完成。

### 先行产物核验（O3 独立验证）

| 产物 | 结果 | 核验 |
|:--|:--|:--|
| 251-A bridge-dual-track-feature-system.md | ✅ A- | 双轨对照/误用后果/消费端区分指引/桥接齐全；quality-gate 12 与 cap_hub 一致（FEATURE_MENU 为工具注册非 lint，不混淆）；与欧阳锋洞察 3 完全对齐 |
| 251-B 回链 concept-yihang-dual-triangle-core | ✅ | +2 related（feature-thinking-core + layered-system）实测命中 |
| 251-C 对账 tool-ai-feature-inventory | ✅ | +2 related（layered + bridge）实测命中，不重复建卡 |
| W4 agent-spec-basic-skills-coach.md | ✅ A- | TCPR Coach 身份/问题分层/路径输出格式/边界（含 quality-gate 不混编）/依赖资产/基线用例——参考 #246 先例结构齐全 |
| 注册规范 cap_hub/agent-registration-norm.md | ✅ | 三步部署（spec 落位→cap_hub 自动扫描→kdo feature --seed 接入）+ 验证命令 + 9 已有 spec 参考 |

### 条件项（不阻塞先行，随关联任务处理）

1. **#249 依赖**：bridge/agent-spec related 引用 #249 的 4 张新卡（当前 draft）——#249 修复后复查死链与内容联动（**注：#249 已终审 FAIL 退回修复中**）
2. **🟡 "96 个 Feature"写死 ×4**：bridge L49/L58、agent-spec L57/L94/L107——#248 C1/C2 补齐后应随动 100。建议：此类引用改为"周期表 JSON"不带数字
3. **🟡 部署层次 2/3 未完成**：cap_hub 注册 + kdo feature 接入 + 实测——待黄药师配合能力中台；#252 试点依赖此
4. **🟢 规范 vs 实际目录不一致**：规范第 1 步说 spec 落 `30_wiki/agent-specs/`（主目录），实际产物在 `30_wiki/tools/`（L23 说明两目录都被扫描，功能无碍）——统一落位标准，P2
5. **🟢 agent-spec related 死链复查**：此卡无死链 ✅（#249 的 framework-一堂-刻意练习 死链已单独退回）
