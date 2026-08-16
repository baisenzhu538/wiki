---
session_id: huangyaoshi-2026-08-10
agent_id: huangyaoshi
date: 2026-08-10
created_at: 2026-08-09T19:11:58.126712+00:00
updated_at: 2026-08-09T19:11:58.126712+00:00
---

# huangyaoshi · 2026-08-10

---
session_id: huangyaoshi-2026-08-10
agent_id: huangyaoshi
date: 2026-08-10
created_at: 2026-08-10
---

# Truman 11章复盘 · 黄药师 · 2026-08-10

## 差异栏（vs 2026-08-09 复盘）

本次会话与上次的最大不同：**从"批量交付基建"转向"让知识库被 agent 真正用起来"**——上次是 11 件交付（#267-283 基建链），这次的核心是 **WorkBuddy 对比分析 → 任务模式（#310/#311）→ MCP 接入（#306/#308）→ 真机验证跑通**。另一个视角变化：上次"凭记忆写 TCPR 定义"踩了 E020 大坑，这次**每次回答问题前都先检索验证**（书名校验、卡名验证、MCP 配置验证）——E020 教训当天起效。第三个变化：**接受了用户多次实测修正**（Flash 强于 Pro 预览版、Hermes 无原生路由、.wslconfig 内存限制）——从"我的推断"转向"实测优先"。

## 1. 做了什么

### 任务模式全链（WorkBuddy 差距 → 落地）
- #310 任务模式 spec 终审 A- → C1 卡名修正 + C2 SOUL 实现（五节模板/出口式咨询/案例沉淀）
- #311 任务模式 SOUL：SOUL 任务模式节 + **MCP 双 server 接入**（kdo 检索 + feishu_doc 操作）+ 检索规则升级
- **真机验证跑通**：老朱拆书作业——教练助理五节流程完整执行（背景→多轮出口式问出履历→三支柱卡组检索→2000 字第一人称成稿→待确认闭环）
- #308 MCP 接入：**3 agent 全覆盖**（教练/开会/基本功）——config mcp_servers + SOUL 检索规则 + 引用来源行 + 自检节，终审 A

### 操作型 MCP（#306）
- feishu_doc_server.py（4 工具 create/fetch/update/search）——lark-cli 封装
- 全链路冒烟（创建→写入→回读→搜索）+ C1 三处登记（cap_hub/config/toolkit）+ C2 测试文档删除（high-risk 需确认）

### 调研与修正
- #277 模型路由：#309 调研结论——**Hermes 无原生对话级路由**（smart_model_routing 仅配置无实现）
- **用户实测修正**：Flash 强于 Pro 预览版 → 路由前提不成立，保持 Flash 主力正确
- #305 索引验证：实测检索/统计正常（kdo_capabilities 实时扫磁盘），state.sqlite 旧但无功能依赖
- 小昭自检报告验证：先误判（搜错地方——小昭是 WorkBuddy 不是 Codex），后更正（.workbuddy/mcp.json 就是我配的）

### WSL 性能诊断
- .wslconfig 锁 memory=4GB/processors=2 → 多 gateway swap（540Mi/1Gi）→ 反应慢根因
- 记入停车场 P-31（用户要求先想清楚再动）

## 2. 关键决策

| 决策 | 理由 | 结果 |
|:---|:---|:---|
| MCP 接入 3 agent 全覆盖（含 basic-skills-coach） | WorkBuddy 差距分析：语义检索是飞书 agent 最大短板 | #308 终审 A |
| 任务模式五节模板运行时化（SOUL 而非改 spec） | 不碰已终审 spec（#300），SOUL 是运行时层 | #310 C2 闭环 |
| Hermes 无原生路由 → 建议回退/降级文档 | P-21 查清机制底座（源码无实现），不硬上不存在的机制 | #309 提审 |
| 接受用户实测修正（Flash>Pro 预览版） | 实测 > 推断（P-42 证据效力层级） | 路由前提推翻 |
| WSL 性能改进入停车场 | 影响面大（wsl --shutdown 全量重启），用户要求先想清楚 | P-31 待讨论 |

## 3. 新资产

### 基建（今日新增/升级）
- `kdo-tools/mcp/feishu_doc_server.py` — 操作型 MCP（#306）
- `agents/coaching-leadership-assistant/SOUL.md` — 任务模式节 + 检索规则升级 + 引用来源行 + 自检节（#310/#311/#308）
- `agents/meeting-assistant/SOUL.md` — 同上（#308）
- `agents/agent-basic-skills-coach/system-prompt.md` — 同上（#308）
- 3 profile config.yaml — mcp_servers 双 server（kdo + feishu_doc）
- `kdo-tools/mcp/config.yaml` — deployments 部署记录节
- `.agent/toolkit.md` — MCP 服务表
- cap_hub features.json — FEISHU_DOC_MCP（20 features）
- `60_feedback/diagnosis/diag_20260809_huangyaoshi-feishu-agent-mcp-upgrade.md` — 建议书

### 文档/报告
- #306/#308/#309/#311 任务单执行报告 + 队列流转
- 停车场 P-31（WSL 性能）

## 4. 新问题/阻塞

- **Hermes 无原生对话级模型路由**——#309 建议回退/降级，待欧阳锋裁定
- **DeepSeek 08-06 涨价新价未公布**——模型成本测算待新价
- **WSL 内存瓶颈**（P-31）——多 gateway swap，待用户决策
- 真机验证条件项（#308 C1/#311 C1）——WSL 侧重启 gateway 后飞书实测

## 5. 踩坑

- **E020 复发风险**：昨天 TCPR 定义错误——今天每次写 SOUL/引用前先 grep 验证卡名/定义（书名校验 1 次、卡名验证 3 次、MCP 配置验证 2 次）——E020 教训内化
- **小昭身份误判**：搜 .codex 没找到 MCP 配置 → 质疑小昭声明 → 实际是 WorkBuddy（.workbuddy/mcp.json）——"搜错地方 + 看到路径没打开验证"
- **#309 调研弯路**：先按 #277 假设 Pro 更强 → 用户实测推翻——推断不敌实测

## 6. 下次启动最需要记住

- **MCP 双 server 已接入 3 个飞书 agent**（kdo 检索 + feishu_doc 操作）——重启 gateway 后生效
- **任务模式已真机验证跑通**（老朱拆书作业五节流程）——教练助理有交付物能力
- **Hermes 无原生模型路由**——#309 待裁定（回退 or 降级文档）
- **用户实测 > 我的推断**（Flash>Pro 预览版）——回答前先验证
- **停车场 P-31**：WSL 内存瓶颈待用户决策（未动）
- **E020 教训**：写 SOUL/引用前先 grep 验证卡名定义
- 队列 290 全清（queued/pending_review=0），我的任务全交付
- **失忆恢复口令**：读本文件 + .agent/huangyaoshi-context.md + B1-B6 牌组

## 7. 必做

- [x] B1 门禁：今日产出（#306/#308/#309/#311）全部入队流转
- [x] 技能进化日志更新
- [x] 失忆恢复锚点更新
- [x] daily-context 复盘写入

## 8. 黄牌/表扬

- 🟢 **任务模式真机验证跑通**：从 WorkBuddy 差距分析到飞书 agent 跑通拆书作业——"从客户到用户"2000 字成稿，五节流程完整
- 🟢 **MCP 接入 3 agent 全覆盖**：#306 操作型 + #308 检索型——飞书 agent 从"提示引导"升级"可检索系统"
- 🟢 **E020 教训当天内化**：每次引用前验证——今天 0 个死链、0 个错定义
- 🟡 **小昭身份误判**：搜错地方 + 没打开验证——"看到路径"≠"验证内容"
- 🟡 **#309 推断被实测推翻**：P-42 证据效力——推断放最后

## 9. 五步法反思

- 实事求是：Hermes 无原生路由是查源码查出来的（不是猜的）；Flash>Pro 是用户实测的（不是我推断的）
- 解放思想：任务模式的本质不是"改 spec"是"让 spec 运行时生效"——SOUL 是运行时层
- 知行合一：WorkBuddy 差距分析 → 当天就落地为 MCP 接入 + 任务模式——不隔夜
- 关键假设：假设 Hermes 支持路由 → 查源码证伪；假设 Pro 更强 → 用户实测证伪——两个假设都被实测修正
- 迭代：从"飞书 agent 弱"到"3 agent 全接入"——分析→建议书→裁定→实现→真机，全链闭环

## 10. 角色定位

黄药师=Builder。本场产出：操作型 MCP（#306）+ 任务模式 SOUL 实现（#310/#311）+ 检索 MCP 3 agent 接入（#308）+ 模型路由调研修正（#309）+ WSL 性能诊断（P-31）。不做卡片生产（老顽童），不做任务编排（王语嫣），不做终审（欧阳锋）。跨角色协作：给王语嫣建议书（MCP 升级）、接受用户实测修正、给欧阳锋提审 4 单。
