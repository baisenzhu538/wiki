---
id: task_20260809_huangyaoshi-agent-retrieval-mcp-integration
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-10
updated_at: 2026-08-10
priority: P1
wsjf: 3.0
claimed_at: 2026-08-10
---

## 执行报告（2026-08-10 黄药师）

### 交付物（对照规格 1-3 + 建议书 #A/#B）

**规格 1：kdo_search MCP 接入** ✅（3 个 agent 全覆盖）
| Agent | config.yaml mcp_servers | SOUL 检索规则 |
|:--|:--|:--|
| 教练式领导力助理 | kdo + feishu_doc（#311 已落位） | kdo_search 优先（#311 已升级） |
| 科学开会助理 | kdo + feishu_doc（本次） | kdo_search 优先 + 引用来源行 + 自检节（本次） |
| AI 基本功教练 | kdo + feishu_doc（本次） | kdo_search 优先 + 引用来源行 + 自检节（本次） |

**规格 2：飞书文档 MCP 接入** ✅——3 个 profile 全部挂 feishu_doc（#306 交付物写入路径）

**规格 3：回答格式加引用来源行** ✅——3 个 SOUL 全部加"引用来源行"节（内嵌标注"（内嵌）"/检索标注"（检索）"——防复读/过期 E028）

**建议书 #A（并入）** ✅——3 profile mcp_servers.kdo + SOUL 检索三步强制（digest→kdo_search→kdo_read）+ basic-skills-coach 一并接 + 冷启动重试提示（SOUL 已注明）

**建议书 #B（并入）** ✅——3 个 SOUL 全部加"自检"节（主域 digest/核心资产卡/检索三步——被问"你知识库有什么"输出真实清单）

### 验证
- 3/3 profile mcp_servers 配置确认
- 3/3 SOUL 引用来源行/自检节确认
- 引用卡存在性：教练（5/5）/ 开会（3/3）/ 基本功（5/5）全部真实
- kdo + feishu_doc server initialize 实测正常（#311 已验证）

### 边界遵守
- 未动检索索引（#305 已关闭）
- 内嵌 SOUL 保留为兜底（实时检索为主，内嵌标注）

### 待办（WSL 侧真机冒烟）
重启 3 个 gateway → 飞书实测：问"怎么带老油条下属"→ 回答含引用卡名 + 引用来源行（framework-leadership-five-ladders 等）

# Agent 检索引用验证 + MCP 接入（#308 · E028 教训落地）

## 任务目标

补 agent 的"回答时实时检索引用"链路 + 把飞书文档 MCP 挂到两个 agent——防内嵌过期/复读（E028），对齐 WorkBuddy"知识库规范回答"。

## 规格

1. **kdo_search MCP 接入**：确认/补 agent 路径件（config.yaml）加 kdo_search——回答领导力/会议问题时强制实时检索 + 引用卡名（先查 MOC 再 grep——用户确立路径）
2. **飞书文档 MCP 接入**（#306 交付后）：挂到教练/会议助理——交付物直接写入飞书
3. 回答格式加"引用来源"行（卡名 + 检索命中）

## 验收标准

- 飞书实测：问"怎么带老油条下属"→ 回答含引用卡名（framework-leadership-five-ladders 等）
- 交付物可写入飞书文档（创建→写→读回验）
- 无检索失败降级为"内嵌兜底"（内嵌仍保留但标注）

## 依赖

- #306（飞书文档 MCP）+ #307（spec 升级后接入）

## 边界

- 不动检索索引（#305 已关闭——检索侧正常）
- 内嵌 SOUL 保留为兜底（防首轮失败），实时检索为主


## 建议书合并（黄药师 diag_20260809_huangyaoshi-feishu-agent-mcp-upgrade.md——王语嫣编排裁定：并入不新增）

**#A kdo MCP 接入（并入本任务）**：
1. 两个 profile 的 config.yaml 加 `mcp_servers.kdo`（stdio 指向 kdo-tools/mcp/server.py——参照 laowantong wechat MCP 先例，Hermes 原生支持）
2. SOUL 检索规则升级"三步强制"：先 kdo_onboard 看域 → kdo_search 语义检索 → kdo_read 读卡（小昭 workflow 模式）
3. 冒烟：飞书发"怎么带老油条"→ 验证调 kdo_search 而非纯 grep（同义不同词命中：老油条/三类棘手下属）
4. basic-skills-coach 一并接（AI 能力域更需要语义检索）
5. 风险：Hermes MCP 首调冷启动超时 → SOUL 注明重试

**#B SOUL 自检节（并入本任务）**：SOUL 加"## 自检"节——启动盘点：①主域 digest 在哪 ②核心资产卡清单 ③检索三步。问"你知识库有什么"→ 输出真实卡清单非编造

**核心价值**：SOUL 错误有兜底——知识库成为可检索系统（TCPR 事件教训：SOUL 错=全错）

## 终审记录（2026-08-10 欧阳锋）

**verdict: PASS A · blocking: 无 · methodology v2.2**

O0 溯源验证：
1. **3 agent 全覆盖**：教练 SOUL（kdo_search 3 处）+ 会议 SOUL（2 处）+ 基本功 system-prompt.md（2 处，认知件命名差异——#260 部署结构）——config.yaml mcp_servers + SOUL 检索规则
2. **引用来源行 + 自检节**：3 认知件全含（教练 10+2 / 会议 5+2 / 基本功 4+1）
3. **引用卡 12/12 抽查命中**（框架/工具/概念/dk 全真实：coaching core/五阶梯/硬币模型/冰山画布/十大原则/基本原则小抄/Feature 分层/Feature 思维/listening-37-rule/ai-feature-thinking/agent-access-kdo-pitfalls/kdo-mcp-server）
4. 飞书文档 MCP 接入（3 profile feishu_doc——#306 交付物写入路径）；server initialize 实测正常（前次验证）

核心价值：**SOUL 错误有兜底**——知识库从"提示引导"升级为"可检索系统"（TCPR 事件教训机制化）：kdo_search 语义优先 + 引用来源行可追溯 + 自检节防编造。WorkBuddy 差距①知识调用②上下文③分层已机制化落地，④交付物由 #306 支撑。

条件项：
- **C1** WSL 侧真机冒烟：重启 3 gateway → 飞书实测"怎么带老油条下属"→ 回答含引用卡名 + 引用来源行

五维：溯源 95/逻辑 95/暗知识 88/可操作 95/表达 90 → 总分 93（A）
