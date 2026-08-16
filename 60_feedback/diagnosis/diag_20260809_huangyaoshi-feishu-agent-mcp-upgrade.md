---
title: 任务编排建议书：飞书 Agent 接入 kdo MCP（小昭模式迁移）
type: improvement-plan
status: draft
created_at: 2026-08-09
author: 黄药师
audience: 王语嫣
source_refs:
  - "C:\\Users\\Administrator\\.workbuddy\\mcp.json"
  - "kdo-tools/mcp/server.py"
  - "kdo-tools/mcp/config.yaml"
  - "60_feedback/tasks/task_20260809_huangyaoshi-coaching-assistant-deploy.md"
---

# 任务编排建议书：飞书 Agent 接入 kdo MCP（小昭模式迁移）

> 触发：用户分享小昭（WorkBuddy）通过 MCP 连知识库对话的实例，问"她的逻辑和结构对飞书 agent 有没有帮助、强在哪里"。分析后确认：**小昭的强 = 飞书 agent 的弱，本质是"检索机制 vs 提示引导"的区别，且 Hermes 原生支持 MCP client（已有 wechat 先例）——迁移可行**。

## 一、小昭强在哪（洞察总结）

| 维度 | 小昭（WorkBuddy） | 飞书 agent（Hermes）现状 | 差距本质 |
|:---|:---|:---|:---|
| 知识访问 | **MCP 桥**（kdo_search/kdo_read/kdo_onboard/kdo_capabilities） | terminal + grep 文件（SOUL 写死路径） | 检索机制 vs 提示引导 |
| 检索方式 | **语义检索**（RRF = GraphRAG+BM25+MOC 优先） | 关键词 grep（同义不同词就搜不到） | "怎么带老油条" grep "老油条" 可能 0 命中（卡里写"三类棘手下属"） |
| 域全貌 | kdo_onboard 强制先看域地图（MOC 优先机制化） | SOUL 提示"先查 digest"（软引导，可能跳过） | 机制 vs 提示 |
| 自检能力 | kdo_capabilities 实时盘点（"武器全绿"） | 无自检（不知道自己知道什么） | 能力清点缺失 |
| 工具选择 | MCP tool 描述场景化引导（#220 已改） | 无工具选择环节（SOUL 指引 = 一切） | TCPR 事件已证明：SOUL 描述质量 = 回答质量 |

## 二、为什么值得做（证据）

1. **Hermes 原生支持 MCP client**：`~/.hermes/hermes-agent/hermes_cli/config.py` L1857/L2221 处理 `mcp_servers`；`~/.hermes/config.yaml` L641 已有 wechat MCP 先例（laowantong 配过）——**不是新能力，是配一下的事**
2. **kdo MCP server 已存在**：`kdo-tools/mcp/server.py`（4 工具：search/onboard/read/capabilities），config.yaml 已写好 stdio/SSE 配置模板——server 侧零开发
3. **小昭已实战验证**：自检报告"kdo_search 实测返回 5 张卡"——MCP 链路可用
4. **TCPR 事件的教训**：飞书 agent 靠 SOUL 内嵌知识，SOUL 错 = 全错；接上 MCP 后知识库成为**可检索系统**，SOUL 错误有兜底（agent 可搜到正确卡）

## 三、建议任务拆分（王语嫣编排用）

### #A 建议：飞书 agent 接入 kdo MCP（P1，黄药师，0.5-1d）

**目标**：教练式领导力助理 + 科学开会助理接入 kdo MCP（走 server.py），获得语义检索能力。

**产出**：
1. 两个 profile 的 config.yaml 加 `mcp_servers.kdo`（stdio，指向 server.py）——参照 laowantong wechat MCP 先例
2. SOUL 检索规则升级为"三步强制"：先 kdo_onboard 看域 → 再 kdo_search 语义检索 → 后 kdo_read 读卡（小昭 workflow 模式）
3. 冒烟：飞书发"怎么带老油条"→ 验证 agent 调 kdo_search 而非纯 grep
4. 与 basic-skills-coach 边界确认（它是否也接——建议一并接，它管 AI 能力域更需要语义检索）

**验收**：飞书 agent 对"同义不同词"问题（老油条/棘手下属）能命中正确卡；kdo_search 调用可见（日志/trace）

### #B 建议：SOUL 增加"自检节"（P2，黄药师，0.25d）

**目标**：飞书 agent 会话启动时盘点自己的知识范围（小昭 kdo_capabilities 模式）。

**产出**：SOUL 加"## 自检"节——启动时确认：① 我的主域 digest 在哪 ② 我有哪些核心资产卡 ③ 检索规则三步是什么。回答"你知道什么"类元问题时引用真实盘点而非凭记忆。

**验收**：问"你知识库有什么"→ agent 输出真实卡清单（非编造）

### #C 建议：MCP 部署记录补全（P3，黄药师，0.1d）

**目标**：kdo MCP 的挂载点、配置、客户端全部登记（工具登记四步法）。

**产出**：
1. `kdo-tools/mcp/config.yaml` 加"实际部署记录"节：WorkBuddy 已挂载（.workbuddy/mcp.json）+ 飞书 agent 挂载（#A 后）
2. `.agent/toolkit.md` 武器库加 MCP 行（server.py 路径 + 4 工具 + 挂载点列表）

**验收**：新 agent 接 MCP 时照 toolkit 抄配置即可

## 四、依赖与边界

- #A 依赖：无（kdo MCP server 已存在；Hermes 支持已确认）
- #B 依赖 #A（自检节引用的检索能力）——可并行但建议 #A 后
- 边界：不修改 server.py（已稳定）；不与 #287/#303 部署冲突（只加 config + SOUL 检索规则）
- 风险：Hermes MCP 调用的首次冷启动超时（小昭已记录该现象）——SOUL 检索规则注明"首调超时重试一次"

## 五、明确不做

- ❌ 不给飞书 agent 配 GraphRAG 独立索引（server.py 的 search 已含 GraphRAG 融合）
- ❌ 不改造 server.py（4 工具够用）
- ❌ 不让飞书 agent 写知识库（MCP 只读——search/read/onboard/capabilities 全是读操作）

---
*建议书：黄药师 2026-08-09 | 待王语嫣审核编号入队*
