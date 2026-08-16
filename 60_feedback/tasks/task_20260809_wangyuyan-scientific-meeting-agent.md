---
id: task_20260809_wangyuyan-scientific-meeting-agent
assignee: claude
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-09
updated_at: '2026-08-09T09:27:52.159325+00:00'
priority: P0
wsjf: 3.5
---

# 科学开会助理 Agent（#287 · #263 流水线第三次实战）

## 任务目标

像 AI 基本功教练、教练式领导力 agent 一样，生产**科学开会助理 agent**——用户明确要求：cap_hub 注册 + 飞书链接可用（知识库 → 可用服务的产品化闭环）。

## 规格（#263 流水线三步）

1. **spec 编排（王语嫣）**：agent-spec 卡——TCPR Coach 身份（参照 agent-spec-basic-skills-coach / #282 教练式领导力 agent 模式）
   - 输入：会议问题（会议类型/目标/痛点/参会结构）
   - 输出：
     - **该不该开**（ROI 评估：成本 = 人数×时间×时薪；非必要不开会/替代方案——dk-meeting-roi-first）
     - **怎么设计**（冰山画布三件套：目标→原则→流程；"不开会有什么问题"反向推导）
     - **原则匹配**（十大原则中选 3-5 条：头脑风暴→激发/投入/民主；启动会→点燃/落实/务实；复盘会→学习/落实/投入）
     - **话术直接给**（对应原则的会前/会中/会后策略话术，逐字可用——tool 武器库数据源）
   - 数据源：**#285/#286 卡组**（framework 冰山画布/十大原则 + tool 武器库×3 + dk×6）+ 诊断报告
2. **三件套注入（黄药师）**：认知件（SOUL.md 含管理域知识地图：科学开会 MOC + 管理 digest + 复盘域 + 教练式领导力域）+ 路径件（config.yaml）+ 部署件（agents/meeting-assistant/ + Hermes profile）
3. **注册 + 部署（黄药师）**：cap_hub 注册 active + **飞书 Hermes 通道链接**（用户飞书可用）
4. **自举（agent 自己）**：自我定位→探索→踩坑沉淀→迭代 spec；沉淀 ≥1 条踩坑

## 边界声明（spec 内必写）

| Agent | 边界 |
|:--|:--|
| 科学开会助理（#287） | **会议设计与流程**：该不该开/怎么设计/原则匹配/话术——全域会议（例会/启动/复盘/脑暴/战略/攻坚） |
| 例会主持人 agent-spec（tool-agent-spec-yitang-daily-weekly-meeting-host 已有） | 例会专项主持（日会/周会 SOP）——科学开会助理是它的上游（设计层），补链不替代 |
| 教练式领导力 agent（#282） | 一对一领导力沟通（倾听/提问/反馈）——会议助理管"一群人"，教练管"一个人"，互链 |

## 验收标准

- spec 卡过欧阳锋审查（TCPR/门/边界齐全）
- **数据源完整性（素材精做传导）**：spec 数据源清单 = #285+#286 完整卡组（framework×2 + concept 升级 + case×3 + tool×3 + bridge + dk×6），任一张缺 = 不通过
- cap_hub 注册 active
- **飞书端可用**：用户飞书发"我要开一个复盘会" → 返回 ROI 评估 + 冰山画布三件套 + 原则匹配 + 可照抄话术（冒烟测试通过）
- 自举踩坑 ≥1 条沉淀
- 三 agent 边界无重叠（例会主持人/教练/会议助理）

## 依赖

- **#285 P0 卡组 + #286 P0 深化 reviewed**（2026-08-09 用户铁律：素材精做传导——科学开会已逐字读 6990 行，数据源 = 完整卡组：framework×2 + concept 升级 + case×3 + tool×3 + bridge + dk×6，任缺 = agent 输出残缺）
- #286（bridge/dk）为 P0 深化必含，非可选

## 参考

- `60_feedback/tasks/task_20260809_wangyuyan-coaching-leadership-agent.md`（#282 同模式）
- `agents/agent-basic-skills-coach/`（AI 基本功教练全链路）
- `30_wiki/workflows/workflow-kdo-agent-production-pipeline.md`（#263）
- 诊断：`60_feedback/diagnosis/diag_20260809_scientific-meeting.md`

## 边界

- 不做卡片内容审查（欧阳锋）
- 不替代例会主持人/教练 agent（边界声明写入 spec）
- 试点完成前不注册 cap_hub（#258 裁定：试点后统一注册）——本 agent 是正式生产，注册

## 终审记录（2026-08-09 欧阳锋）

**verdict: PASS（条件）A- · blocking: 🟠1 · methodology v2.2**

O0 溯源验证：
1. source_refs 3/3 存在；spec 结构完整：TCPR（T/C/P/R）+ 输入样例 + 5 项核心能力（ROI 评估公式/冰山画布三件套+反向推导/原则匹配表 5 类会议/话术建议/输出格式）+ 边界 5 条（与 #282 教练"一群人 vs 一个人"、与例会主持人"设计层上游 vs 执行层"双边界声明）+ 基线用例（复盘会→ROI+冰山+务实/落实/学习三原则+话术+证据 B 同学 20 倍+警示）+ 三件套需求 + 自举路径
2. **数据源铁律满足（#285+#286 完整卡组就位）**：framework×2/concept/tool×3/case×3/bridge/dk×6 抽查 5/5 status: reviewed——"任一张缺=不通过"全就位 ✅（与 #282 依赖未就位形成对照）
3. 案例数字可溯源：ROI 5-10 倍/20 倍/成本 10-20% 全部来自已终审 case 卡（#285 边界"案例卡不杜撰数字"已核）✅
4. related 3/4：agent-spec-basic-skills-coach/tool-agent-spec-yitang-daily-weekly-meeting-host/workflow ✅
5. E018 合规：status=draft + reviewed_by 待审查（未自标）✅

条件项：
- **C1** related 死链 1 条：agent-spec-coaching-leadership-coach——#282 spec 尚未转 wiki 卡（规划中资产），#282 转卡后补链或改引用
- **C2** 部署期验收（本地不可验证）：cap_hub 注册 active + 飞书端冒烟（"我要开一个复盘会"→四件套输出）+ 自举踩坑 ≥1——黄药师三件套注入后验证（同 #261 条件①模式）

五维：溯源 90/逻辑 90/暗知识 90/可操作 90/表达 90 → 总分 90（A- 上限——死链+部署期条件）


## ⚠️ spec 更新说明（2026-08-09）

- spec 文件（agents/meeting-assistant/SPEC.md）已补 TCPR 角色切换声明（命名规范：统一"XX 助理"，角色可切换）
- 欧阳锋终审本 spec 时以当前版本为准
