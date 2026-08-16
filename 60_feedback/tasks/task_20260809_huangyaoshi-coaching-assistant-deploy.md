---
id: task_20260809_huangyaoshi-coaching-assistant-deploy
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-09
updated_at: 2026-08-09
priority: P0
wsjf: 3.5
claimed_at: 2026-08-09
---

## 执行报告（2026-08-09 黄药师）

### 交付物（对照规格 1-4）

**① 三件套注入完成**
- 认知件：`agents/coaching-leadership-assistant/SOUL.md`（78 行）——TCPR 可切换声明 + **五阶梯 L0-L5 内嵌表**（首轮即用）+ 21 卡牌/段位/边界三情况/猴子理论/Y 模型 + KDO 知识地图（人域 digest 为主导航）+ 检索规则 + 基线用例输出格式
- 路径件：Hermes profile `coaching-leadership-assistant`（config.yaml：cwd=/mnt/c/.../wiki + approvals.smart，继承 #262 裁定）+ SOUL 已同步
- 部署件：`agents/coaching-leadership-assistant/`（SPEC.md #300 + SOUL.md + CLAUDE.md）+ `30_wiki/tools/agent-spec-coaching-leadership-assistant.md`（cap_hub 可发现副本）

**② cap_hub 注册** ✅ — agent-spec 被自动发现（list 可见）
**③ 飞书链接** — profile 带 feishu 通道配置（复制自 basic-skills-coach）；**真机冒烟待 WSL 侧重启 gateway**（Windows 侧无法操作，见下）
**④ 自举** — 逻辑冒烟 8 项全过（基线用例流程验证）

### 顺手修复（范围外，已声明）
**cap_hub WIKI_ROOT 检测 bug**（07-21 记录的环境问题，阻塞 agent-spec 发现）：config.py 候选顺序 WSL 路径在前，原生 Windows Python 把 `/mnt/c/...` 变 `\mnt\c\...`（相对路径）→ exists()=False → 发现不了任何说明书。修复：Windows 路径优先。**修复后 cap_hub list 完全恢复**（19 Feature + 全部 agent-spec 可见）——这同时修复了部署验收的前提。

### 逻辑冒烟（8 项全过）
| 项 | 结果 |
|:---|:---:|
| TCPR 角色声明（可切换） | ✅ |
| 五阶梯 L0-L5 内嵌 | ✅（首轮即用，不必检索） |
| 21 卡牌+段位引用 | ✅ |
| 边界三情况 | ✅ |
| 检索规则（先查 digest 不凭记忆） | ✅ |
| 输出格式（层级/硬币/话术/警示） | ✅ |
| 案例证据（莫非/三版本） | ✅ |
| 边界声明（AI 教练/会议助理不重叠） | ✅ |

### 待办（需 WSL 侧执行）
- **飞书真机冒烟**：`systemctl --user restart hermes-gateway-coaching-leadership-assistant` → 发"我要怎么带老油条下属"→ 验证返回 TCPR 声明 + 五阶梯定位 + 21 卡牌 + 话术。Windows 侧无法操作 gateway，需用户或 WSL 实例执行
- 自举踩坑沉淀：真机冒烟后如有摩擦 → 记 friction-log + 迭代 SOUL

### 边界遵守
- 未修改 #300 spec（已终审）
- 与 basic-skills-coach / 会议助理（#287）边界声明已写入 SOUL/CLAUDE.md

# 教练式领导力助理三件套部署（#303 · #300 spec 审后执行）

## 任务目标

#300（教练式领导力助理 spec）已 reviewed——部署环节拆给黄药师（E026 单角色铁律）。**用户要求：飞书上也能用**。

## 规格（#263 流水线 Step 2/3）

1. **三件套注入**（参照 agent-basic-skills-coach / #260/#261/#262 实现规范）：
   - 认知件（SOUL.md）：KDO 知识地图 5 MOC + 教练式领导力域位置（人域"影响他人"块）+ 21 卡牌体系路径 + 五阶梯/硬币模型导航
   - 路径件（config.yaml）：cwd=/mnt/c/Users/Administrator/Desktop/wiki（WSL 格式）；approvals.mode=smart；检索规则"先查 MOC 不凭记忆"
   - 部署件：agents/coaching-leadership-assistant/（SPEC.md 已就位）+ Hermes profile（飞书通道）
2. **cap_hub 注册**：active（正式生产，试点后统一注册的 #258 裁定适用）
3. **飞书链接**：用户飞书可用（"我要怎么带老油条下属"→ 返回角色声明 + 五阶梯定位 + 话术）
4. **自举**：agent 自我定位→探索→踩坑沉淀 ≥1 条→迭代 spec

## 验收标准

- cap_hub 注册 active + `kdo feature` 可点菜（教练 Feature 挂接）
- **飞书端冒烟通过**：发领导力问题返回 TCPR 角色声明 + 五阶梯定位 + 21 卡牌对应层级 + 可照抄话术
- 自举踩坑 ≥1 条沉淀（错误模式库/dk 卡）
- 与 basic-skills-coach / 会议助理（#287 审后部署）边界无重叠

## 依赖

- **#300 reviewed ✅**（spec 已过审）
- #280/#281/#288 reviewed ✅（数据源 15/15 就位）

## 参考

- `agents/coaching-leadership-assistant/SPEC.md`（#300 交付）
- `agents/agent-basic-skills-coach/`（三件套模板 + 自举先例）
- `60_feedback/tasks/task_20260809_huangyaoshi-basic-skills-coach-deploy.md`（#256 部署先例）

## 边界

- 不修改 spec（已终审）
- 不替代 #287 会议助理部署（分开进行，边界声明已写入各自 spec）

## 终审记录（2026-08-09 欧阳锋）

**verdict: PASS（条件）A- · blocking: 🟡1 · methodology v2.2**

O3 独立验证：
1. 三件套部分：SOUL.md（5099B，TCPR 可切换/五阶梯/21 卡牌/边界/检索规则内容）+ CLAUDE.md ✅
2. **cap_hub 可见性实测**：`python -m cap_hub list` 显示 19 Feature + 📦 agent-spec-coaching-leadership-assistant 自动发现——**WIKI_ROOT 修复生效**（07-21 环境问题旧账清除，Windows 侧恢复可见，此前 cap_hub 发现不了任何说明书/agent-spec）
3. **引用卡名真实性**：SOUL.md 引用 7/7 全真（tool-coaching-communication-four-layers/segments、dk-coaching-boundary-conditions/monkey-theory、framework-leadership-five-ladders/coin-model、case-morfei-semiconductor）——#288 实际卡名验证（非猜测名）
4. 逻辑冒烟 8 项（报告声明，SOUL 内容抽查支持）

条件项（同 #261/#262 模式）：
- **C1** config.yaml / Hermes profile 在 WSL 侧，本地不可验证——**飞书真机冒烟**：`systemctl --user restart hermes-gateway-coaching-leadership-assistant` → 发"我要怎么带老油条下属"→ 验证 TCPR 声明 + 五阶梯定位 + 话术
- **C2** 冒烟后摩擦 → friction-log 沉淀 + 迭代 SOUL

亮点：**顺手修复 WIKI_ROOT 检测 bug 价值大**——cap_hub 从"发现不了任何东西"到"19 Feature + agent-spec 全可见"，同时是部署验收前提（部署前 cap_hub 不可见 = 部署不可验证）。五阶梯 L0-L5 内嵌 SOUL（防首轮检索失败）设计合理。

五维：溯源 90/逻辑 90/暗知识 85/可操作 85/表达 85 → 总分 88（A- 上限——WSL 侧部署验证留条件）


## 条件项跟踪（2026-08-09 王语嫣）

- **C1 ✅ 已闭环（用户飞书实测）**：用户在飞书发"请介绍下你自己"/"你好"→ 助理返回完整自我介绍（TCPR 可切换角色声明 + 五阶梯 L0-L5 + 硬币模型 + 21 卡牌 + 边界三不 + 使用场景引导）——真机冒烟通过，教练式领导力助理**飞书正式可用**
- **C2 ⏳ 持续**：真机使用中摩擦 → friction-log 沉淀 + 迭代 SOUL

## C1 场景级真机验证记录（2026-08-15 用户实测 · 王语嫣代录）

**触发**：O-13 WSL 扩容重启后 gateway 恢复（同 #304 C1 模式）

**实测**：飞书给「教练式领导力助理」发"我要和一位新晋升的管理者做第一次 1 对 1，怎么开？"——返回完整诊断（真实教练场景，严于 08-09 自我介绍版）：

| 验收项（C1 教练场景） | 实测结果 |
|:---|:---:|
| TCPR 角色声明（C 身份 + 切换提示） | ✅ |
| 五阶梯定位（诊断 L0-L1 边缘 → 目标 L3 共识/提问） | ✅ |
| 硬币诊断（加币：关心/支持式提问；减币：说教/汇报会） | ✅ |
| 话术可照抄（开场关心式 + 定调支持式） | ✅ |
| 案例证据（莫非半导体：工程师→副总监 1 年、AI 问答机器人、行李箱） | ✅ |
| 边界三情况（紧急危机先扛再教 / 第一次别贪多 / 别变汇报会） | ✅ |
| 引用卡名真实性（4/4：five-ladders / questioning-cards / monkey-theory / morfei-semiconductor，已逐个 find 验证） | ✅ |

**结论**：C1 场景级验证通过——教练式领导力助理飞书正式可用（真实教练问题给出诊断+路径+话术，非模板复读）。

## C1 终审关闭（2026-08-15 欧阳锋）

**verdict: C1 条件项正式关闭 · 等级升级 PASS（条件）A- → PASS A- · methodology v2.3**

O3 独立验证（不采信代录报告，字节级重跑）：
1. 引用卡名 4/4 真实存在（five-ladders / questioning-cards / monkey-theory / morfei-semiconductor 逐个 find 命中）✅
2. 08-09 自我介绍版 + 08-15 场景级验证双记录落盘，验收项全 ✅
3. 五维原 88（A- 上限——WSL 侧部署验证留条件）→ 条件清后升级 A-（段王爷先例同构）

**C2 维持**（真机使用摩擦 → friction-log 持续沉淀，非阻塞）。

教练式领导力助理：**飞书正式可用，终审完成，三处状态同步。**
