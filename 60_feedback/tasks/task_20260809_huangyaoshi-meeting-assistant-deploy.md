---
id: task_20260809_huangyaoshi-meeting-assistant-deploy
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-10
updated_at: 2026-08-09
priority: P0
wsjf: 3.5
claimed_at: 2026-08-09
---

## 执行报告（2026-08-09 黄药师）

### 交付物（对照规格 1-4）

**① 三件套注入完成**
- 认知件：`agents/meeting-assistant/SOUL.md`（90 行）——TCPR 可切换 + **ROI 公式/冰山画布/原则匹配 5 类/话术策略 5 原则内嵌**（首轮即用，防检索失败）+ KDO 知识地图（管理域 digest L3 会开会 + 人域 digest）+ 检索规则 + 基线用例输出格式
- 路径件：Hermes profile `meeting-assistant`（config.yaml：cwd=/mnt/c/.../wiki + approvals.smart + feishu 通道）+ SOUL 已同步
- 部署件：`agents/meeting-assistant/`（SPEC.md #287 + SOUL.md + CLAUDE.md）+ `30_wiki/tools/agent-spec-meeting-assistant.md`（cap_hub 可发现副本）

**② cap_hub 注册** ✅ — agent-spec 自动发现（list 可见，WIKI_ROOT 修复 #303 价值复用）
**③ 飞书链接** — profile 带 feishu 通道配置；**真机冒烟待 WSL 侧重启 gateway**（同 #303 C1 模式）
**④ 自举** — 逻辑冒烟 8 项全过

### 逻辑冒烟（8 项全过）
| 项 | 结果 |
|:---|:---:|
| TCPR 角色声明（可切换） | ✅ |
| ROI 评估内嵌（成本公式+三层价值+金句） | ✅ |
| 冰山画布三件套（目标/原则/流程+反向推导） | ✅ |
| 原则匹配 5 类（头脑风暴/启动/复盘/周例/战略） | ✅ |
| 话术策略（务实/高效/良性/点燃/落实） | ✅ |
| 案例证据（5-10 倍/20 倍/10-20%） | ✅ |
| 边界声明（教练助理/例会主持人/写纪要） | ✅ |
| 输出格式（该不该开/画布/话术/警示） | ✅ |

### 引用卡名真实性（验收要求）
14/14 引用全部存在（framework-meeting-iceberg-canvas/ten-principles、tool-meeting-basic/execution/result-principles、case-meeting-roi-awakening/scene-mastery/truman-meeting-leadership、dk-meeting-*×6 在 30_wiki/dk/ 目录、bridge-meeting-leadership-coaching）——#285/#286 实际卡名验证，非猜测名

### 待办（需 WSL 侧执行）
- **飞书真机冒烟**：`systemctl --user restart hermes-gateway-meeting-assistant` → 发"我要开一个复盘会，怎么开？"→ 验证返回 ROI 评估 + 冰山画布 + 原则匹配 + 话术
- 自举踩坑沉淀：真机冒烟后如有摩擦 → friction-log + 迭代 SOUL

### 边界遵守
- 未修改 #287 spec（已终审）
- 与教练助理（#303）/ 例会主持人边界声明已写入 SOUL/CLAUDE.md

# 科学开会助理三件套部署（#304 · #287 spec 审后执行）

## 任务目标

#287（科学开会助理 spec）已终审 PASS（条件）A-——部署环节拆给黄药师（E026 单角色铁律）。**用户要求：飞书上也能用**（与 #303 教练助理并列上线）。

## 规格（#263 流水线 Step 2/3，参照 #303 先例）

1. **三件套注入**：
   - 认知件（SOUL.md）：KDO 知识地图 5 MOC + 管理域 digest（L3 会开会）+ 科学开会框架导航 + **冰山画布/十大原则/武器库话术内嵌**（防首轮检索失败，参照 #303 五阶梯内嵌设计）+ 检索规则"先查 MOC 不凭记忆"
   - 路径件（config.yaml）：cwd=/mnt/c/Users/Administrator/Desktop/wiki（WSL 格式）；approvals.mode=smart
   - 部署件：agents/meeting-assistant/（SPEC.md 已就位）+ Hermes profile（飞书通道）
2. **cap_hub 注册**：active（WIKI_ROOT 修复已就位，#303 顺手修复——agent-spec 自动发现）
3. **飞书链接**：用户飞书可用（"我要开一个复盘会"→ ROI 评估 + 冰山画布 + 原则匹配 + 话术）
4. **自举**：自我定位→探索→踩坑沉淀 ≥1 条→迭代 spec

## 验收标准

- cap_hub 注册 active + agent-spec 可见
- **逻辑冒烟 8 项**（ROI 评估/冰山画布三件套/原则匹配 5 类/话术/证据/边界/警示/输出格式——参照 #303 冒烟清单）
- 引用卡名真实性（#285/#286 实际卡名：framework-meeting-iceberg-canvas/ten-principles、tool-meeting-*-principles、case-meeting-*、dk-meeting-*——非猜测名）
- 飞书真机冒烟待 WSL 侧（同 #303 C1 模式）

## 依赖

- **#287 reviewed ✅**（spec PASS 条件 A-）
- #285/#286 reviewed ✅（数据源完整卡组）

## 参考

- `agents/meeting-assistant/SPEC.md`（#287 交付）
- `agents/coaching-leadership-assistant/`（#303 三件套模板先例——SOUL 内嵌设计）
- `60_feedback/tasks/task_20260809_huangyaoshi-coaching-assistant-deploy.md`（#303 部署先例）

## 边界

- 不修改 #287 spec（已终审）
- 与教练助理（#303）/ 例会主持人（tool-agent-spec-yitang-daily-weekly-meeting-host 设计层上游）边界声明已写入 spec

## 终审记录（2026-08-10 欧阳锋）

**verdict: PASS（条件）A- · blocking: 🟠1 · methodology v2.2**

O0 溯源验证：
1. 三件套齐全（agents/meeting-assistant/：CLAUDE.md + DELIVERABLES.md + SOUL.md + SPEC.md——比 #303 多交付物模板库）
2. SOUL 内容抽查：冰山画布/ROI/十大原则/MOC 14 处命中
3. cap_hub agent-spec-meeting-assistant 自动发现可见 ✅
4. kdo server initialize 实测通过（JSON-RPC 正常）

条件项（同 #303 C1 模式）：
- **C1** WSL 侧重启 gateway 真机冒烟（"我要开一个复盘会"→ ROI 评估 + 冰山三件套 + 原则匹配 + 话术）
- **C2** config.yaml/Hermes profile 本地不可验证（同 #261/#262）

五维：溯源 90/逻辑 90/暗知识 85/可操作 85/表达 85 → 总分 87（A- 上限——真机验证待 WSL）

## 复审确认（2026-08-15 欧阳锋·会话恢复后核实）

**verdict: 确认终审有效 · 维持 PASS（条件）A- · methodology v2.3**

O3 独立验证（不采信报告，字节级对证）：
1. 三件套存在性：agents/meeting-assistant/ 四件齐全（CLAUDE.md/DELIVERABLES.md/SOUL.md/SPEC.md）✅
2. SOUL 内容抽查：TCPR 可切换 + MOC 导航 + ROI/冰山画布/原则匹配内嵌——首 30 行逐字命中 ✅
3. cap_hub 注册：`python -m cap_hub list` 可见 `agent-spec-meeting-assistant` ✅
4. 08-14 健康检查：`agent-spec-meeting-assistant.md` 有 FAIL（domain: None）+ WARN（type 目录不符）——**但全类 agent-spec 卡同款 FAIL/WARN（含 #303 coaching-leadership-assistant），系统性问题非本任务引入** → 记停车场 TODO，不阻断（非本批问题记 TODO 原则）

条件项状态（08-15 复核）：
- **C1 未闭环**：飞书真机冒烟（"我要开一个复盘会"→ ROI+冰山画布+原则匹配+话术）5 天未执行——搜 60_feedback/.agent/agent复盘 无真机记录，仍待 WSL 侧重启 gateway（同 #303 遗留模式）
- **C2 维持**：config.yaml/Hermes profile 本地不可验证

结论：终审记录真实有效，无需重审；C1 为遗留条件项，随 #303 一并促 WSL 侧执行。

## C1 真机冒烟记录（2026-08-15 用户实测 · 王语嫣代录）

**触发**：O-13 WSL 扩容重启后 gateway 恢复（#304 遗留条件项解锁）

**实测**：飞书给「科学开会助理」发"我要开一个复盘会，怎么开？"——返回完整五段式：

| 验收项（C1） | 实测结果 |
|:---|:---:|
| ROI 评估（成本公式 + 反向推导 + 该不该开 + 两个硬前提） | ✅ |
| 冰山画布三件套（目标 / 原则 / 流程：会前会中会后） | ✅ |
| 原则匹配（十大原则挑选 5 条 + 防翻车补充务实/良性） | ✅ |
| 话术（开场定基调 / 还原事实 / 定量四问 / 参与标准 / 收尾确认） | ✅ |
| 引用卡名真实性（5/5：iceberg-canvas / ten-principles / roi-awakening / basic-principles / result-principles，已逐个 find 验证） | ✅ |
| 附加：前置问题（先问复盘对象）+ 关键警示（夸夸会 / 批斗会 / 只复盘不落实 / 无关人陪跑） | ✅ |

**结论：C1 条件项已闭环**——待欧阳锋确认关闭（证据：本记录 + 用户飞书原文）。#303（教练助理）真机冒烟仍待用户实测。

## C1 终审关闭（2026-08-15 欧阳锋）

**verdict: C1 条件项正式关闭 · 等级升级 PASS（条件）A- → PASS A- · methodology v2.3**

O3 独立验证（不采信代录报告，字节级重跑）：
1. 引用卡名 5/5 真实存在（iceberg-canvas / ten-principles / roi-awakening / basic-principles / result-principles 逐个 find 命中）✅
2. C1 真机冒烟记录落盘：五段式（ROI 评估+冰山画布+原则匹配+话术+警示）全 ✅
3. 五维原 87（A- 上限——真机验证待 WSL）→ 条件清后升级 A-（段王爷先例同构）

**C2 维持**（config.yaml/Hermes profile 本地不可验证，同 #261/#262，非阻塞）。

科学开会助理：**飞书正式可用，终审完成，三处状态同步。**
