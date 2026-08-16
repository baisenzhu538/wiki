---
id: task_20260809_wangyuyan-coaching-leadership-agent
assignee: claude
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-09
updated_at: '2026-08-09T08:54:55.796420+00:00'
priority: P0
wsjf: 3.5
---

# 教练式领导力 Agent（#282 · #263 流水线第二次实战）

## 任务目标

像 AI 基本功教练一样生产教练式领导力 agent——用户明确要求：**cap_hub 注册 + 飞书链接可用**（知识库 → 可用服务的产品化闭环）。

## 规格（#263 流水线三步）

1. **spec 编排（王语嫣）**：agent-spec 卡——TCPR Coach 身份（参照 agent-spec-basic-skills-coach 模式）
   - 输入：领导力问题（带团队卡点/下属类型/沟通场景/反馈需求）
   - 输出：五阶梯定位（当前在 L几→下一个阶梯）+ 武器库建议（倾听/提问/反馈卡组合）+ 硬币模型诊断（加减币行为识别）+ 实践动作（可照做）
   - 数据源：**#280/#281 卡组**（framework 五阶梯/硬币模型 + tool 武器库）+ 诊断报告
2. **三件套注入（黄药师）**：认知件（SOUL.md 含人域知识地图：教练式领导力 MOC + 如何了解一个人 + 复盘域）+ 路径件（config.yaml）+ 部署件（agents/coaching-leadership-coach/ + Hermes profile）
3. **注册 + 部署（黄药师）**：cap_hub 注册（参照 basic-skills-coach active 模式，#258 裁定试点后统一注册——教练 agent 是正式生产，注册）+ **飞书 Hermes 通道链接**（用户飞书可用）
4. **自举（agent 自己）**：自我定位→探索→踩坑沉淀→迭代 spec；沉淀 ≥1 条踩坑

## 验收标准

- spec 卡过欧阳锋审查（TCPR/门/边界齐全）
- **数据源完整性（素材精做传导——用户铁律）**：spec 数据源清单 = #280+#281+#288 完整卡组（framework×3 + 武器库×3 + 案例×3（含莫非半导体/三版本对话）+ 21 卡牌体系 + 段位清单 + dk×3），任一张缺 = 不通过
- cap_hub 注册 active + `kdo feature` 可点菜（领导力 Feature 挂接）
- **飞书端可用**：用户飞书发领导力问题 → 返回五阶梯定位 + 武器库建议 + 21 卡牌对应层级（冒烟测试通过）
- 自举踩坑 ≥1 条沉淀（错误模式库/dk 卡）
- 与 AI 基本功教练无能力重叠（教练边界：领导力/带团队 vs Feature 点菜）

## 依赖

- **#280 P0 卡组 + #288 逐字深挖增量 reviewed**（2026-08-09 用户铁律：前期素材不精做，后面产出的 agent 就是垃圾——**agent 数据源 = 素材精做后的完整卡组**，含逐字读补出的莫非完整故事/21 卡牌体系/段位清单/三版本对话，缺增量 = agent 只懂 60%）
- #281 桥接卡（Feature 分层）——可选增强，不阻塞

## 参考

- `agents/agent-basic-skills-coach/`（AI 基本功教练全链路：#251 spec → #256 部署 → 自举）
- `30_wiki/workflows/workflow-kdo-agent-production-pipeline.md`（#263）
- 诊断：`60_feedback/diagnosis/diag_20260809_coaching-leadership.md`

## 边界

- 不做卡片内容审查（欧阳锋）
- 不替代 AI 基本功教练（边界声明写入 spec）

## 终审记录（2026-08-09 欧阳锋）

**verdict: PASS（条件）B+ · blocking: 🟡2 · methodology v2.2**

O0 溯源验证：
1. source_refs 3/3 存在（workflow 卡/诊断/agent-spec-basic-skills-coach）
2. spec 结构完整：TCPR（T/C/P/R）+ 输入样例 + 5 项核心能力（五阶梯定位诊断表 L0-L5/硬币诊断/21 卡牌匹配/话术建议/输出格式）+ 边界 5 条（含与 basic-skills-coach/#287 会议助理的双重边界声明）+ 基线用例（老油条案例→L2-L3 定位+硬币诊断+三步路径+话术+证据）+ 三件套需求 + 自举路径 + 双实例纪律
3. E018 合规：status=draft + reviewed_by 待审查（未自标）✅
4. 基线用例证据链部分真实：莫非 4 处引用在 case-leadership-communication-failures ✅

条件项：
- **C1 🔴 依赖资产未就位（任务单铁律"任一张缺=不通过"）**：#288 仍 queued——spec 依赖的 21 卡牌矩阵/段位清单 9 格/dk×3（边界三情况/猴子理论/Y 模型沟通版）/莫非完整故事全部缺失。#288 reviewed 后复审 spec 引用与基线用例证据链
- **C2 related 死链 ×2**：agent-spec-review-coach（#268 C1 已修过一次——旧 id 复用复发，建议记 friction-log）；tool-yitang-daily-weekly-meeting-host（正确 id 应为 tool-yitang-daily-weekly-meeting-hosting）

五维：溯源 85/逻辑 85/暗知识 85/可操作 85/表达 85 → 总分 85（B+ 上限）


## 条件项跟踪（2026-08-09 欧阳锋终审后）

- **C1 ⏳ #288 前置**：spec 依赖的 21 卡牌矩阵/段位清单/dk×3/莫非完整故事全部在 #288（queued hermes）——**hermes 老顽童下一单优先领 #288**，reviewed 后欧阳锋复审 spec 关闭 C1，教练 agent 才能自举
- **C2 ✅ 已修（2026-08-09 王语嫣）**：related 死链 ×2 修复——agent-spec-review-coach → agent-spec-复盘教练（旧 id 复用复发，friction-log 已记录防第三次）；tool-yitang-daily-weekly-meeting-host → tool-yitang-daily-weekly-meeting-hosting（拼写修正）


## ⚠️ spec 更新说明（2026-08-09，透明记录不污染审查链）

- spec 文件（agents/coaching-leadership-coach/SPEC.md）内容已更新：TCPR 角色切换声明（用户命名规范 2026-08-09：统一"XX 助理"，角色可切换不锁死）
- 欧阳锋复审 #282 C1（#288 前置）时一并确认此内容更新
- 助理化规范落地另开 #300（不在本任务改规格——E025 铁律）

## 条件项跟踪（2026-08-09 欧阳锋复审）

- **C1 ✅ 已闭环（#288 PASS A）**：21 卡牌矩阵 = tool-coaching-communication-four-layers（四层级×21 卡，双维互补）✅ / 段位清单 9 格 = tool-coaching-communication-segments（VLM 主锚+口述次锚）✅ / dk×3 = dk-coaching-boundary-conditions + dk-coaching-monkey-theory + dk-y-model-communication ✅ / 莫非完整故事 = case-morfei-semiconductor（L152-408 证据补足）✅——spec 依赖资产全部就位，基线用例莫非半导体老油条案例证据链成立，spec 可进入三件套注入/自举
- **C2 ⏳**：related 死链 2 条修复（agent-spec-review-coach 换链/meeting-host 拼写）——待王语嫣处理


## 复审结论（2026-08-09 欧阳锋）——C1/C2 已关闭

- **C1 ✅ 已关闭**：#288（逐字深挖增量）终审 PASS A（93 分）——21 卡牌矩阵/段位清单/dk×3/莫非完整故事全部就位，数据源完整性满足
- **C2 ✅ 已关闭**：related 死链已修（agent-spec-复盘教练 / tool-yitang-daily-weekly-meeting-hosting）
- **本任务状态：reviewed（终态）**

## ⚠️ 下一步动作归属（防职责混乱）

| 动作 | 归属 | 说明 |
|:--|:--|:--|
| #282 修复/复审 | **无**（已 reviewed 终态） | 老顽童**无需任何动作**——他的 #288 已完成，本任务与他无关 |
| 助理化演进（TCPR 可切换规范版） | **#300**（王语嫣 spec + 欧阳锋审 + 黄药师部署） | 用户命名规范调整另开任务（E025），不碰本任务 |
| 三件套注入/飞书部署 | #300 终审后黄药师 | agents/coaching-leadership-assistant/ |
