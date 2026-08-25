---
type: analysis
status: registered
audience: 王语嫣
date: 2026-08-25
author: 王语嫣
source: "老朱提供小昭对话上下文打包（桌面 对话上下文_2026-08-24_18点后.zip），explore 全量通读 7561 行 + raw.jsonl 交叉验证"
---

# 消费端实况：小昭（WorkBuddy/Claw）使用知识库证据报告（2026-08-24 18:00-22:44）

> 用途：#524 立项依据 + #517/#518 加重证据 + F-057/F-058 停车场依据。原始语料：`_tmp/xiaozhao-ctx-20260824/`（临时，证据已固化在本文）。

## 会话轮廓

用户消息 15 条：灵光链接解读（OpenClaw vs Hermes）→ 工具架构连环追问×5 → 「Mock+GraphRAG」机制之问 → MCP 实跑对比 → 卡片溯源核实 → 库级统计（来源于我的卡/draft 数）→ 5 卡终审评估+draft 聚类 → 打包上下文。18:00 前（压缩摘要）：四份作业/心得写作（全部基于知识库素材）。

## 关键证据（行号 = ctx md）

1. **检索漏卡→MCP 立功**：msg1 Grep 关键词全库检索漏掉最对口的 `tool-ai-agent-feature-comparison`（标题无字面命中）；msg11 kdo_search 靠 GraphRAG/MOC 语义关联捞到第 5 名（L4110-4193，2 秒返回无冷启动超时）。
2. **draft 当答案风险实证**：捞到的核心卡 `status: draft / reviewed_by: 待审`（L4193）；小昭自警「纯 MCP 流程不看 status，容易把草稿当定论」（L4400）。
3. **kdo_search 结果混入非卡片**：10 条结果含 SKILL.md/README（无 status）、10_raw 原始素材（type=unknown）；前两名 score 并列 0.181 仅沾边；最相关的 `framework-multi-agent-collab-chain-six`（第 2 名）被消费端略过未读——MCP 给对了，缺「该读哪条」引导。
4. **reviewed 卡带 lint 级结构损坏过审（加重 #517/#518）**：`dk-lz-code-is-disposable` 有畸形行 `- src_unknown# 代码正在变成…`（标题被吞进 diagnostic_signals）+ 使用场景 4 处占位；`dk-lz-ai-native-organization` 2 处 `signal: src_unknown` 且正文标题粘连进 YAML 块（L5775/L5832）。两卡均 reviewed（欧阳锋审）。
5. **draft 计数三口径打架**：rg grep 1189 → 小昭 Python 全量 1260 → 王语嫣复测 30_wiki 770 / 全库（除 _tmp/.git）1110。差值主因：71 张 draft 躺在 `_tmp/` 等 .gitignore 忽略目录，对遵守 ignore 的检索天然隐身。**口径未定义前任何 draft 统计都不可引用**。
6. **卡片入库不回流来源者**：`tool-ai-agent-feature-comparison` 8-8 入库、署名「老朱（一手体感）」，老朱 8-24 见到时的反应是「是不是它拿咱俩聊天自动生成草案？」（L4479）——入库 16 天来源者不知情。全库 `source_person: 老朱` 仅 3 张。
7. **alias 语义强度致误读**：「龙虾=OpenClaw」既有 alias 强化了小昭把老朱架构误读为「4 角色 OpenClaw 部署」，被老朱当场纠正（L1975：「我是一个 hermes、两个 claude code、一个 codex，通过上下文交接」）。误读还写进了作业和 memory。
8. **索引存在但未被消费**：`30_wiki/concept-card-index-latest.md` 在检索中命中但小昭从未打开——索引没被消费端当入口。
9. **凭证无遮挡（安全观察项）**：小昭取证时把 `~/.workbuddy/mcp.json` 的 Bearer token 完整读进上下文（L3549）；老朱对话中明文贴过 MiniMax key。消费端取证路径无凭证防护。
10. **错误归因沉淀进记忆**：rg 行首锚定 pattern 全 0 被小昭错诊为「BOM/不可见字符」并写进它自己的 memory（L5263）；实测非 BOM（王语嫣复验：同 pattern 限定 `30_wiki/` 即正常）——agent 本地记忆的错误结论不自纠。
11. **冷启动超时顾虑改变行为**：小昭 memory 记「kdo_search 首次调用偶发超时」（L3446），导致它全程绕开 MCP 走文件系统直达——#356 治本单的消费端代价实证。
12. **知识库立功时刻**：外部链接抓取失败时库内 spec+逐字稿拼出完整回答（L733-760）；逐字稿原文支撑小昭纠正老朱错误记忆而不编造（L1688-1797）；frontmatter 溯源三字段干净回答「这卡什么时间、是不是自动生成」（L4560-4620）。

## 王语嫣裁定落点

- #524（kdo_search 消费端契约）立项依据 = 证据 1/2/3/11
- #517/#518 加重证据 = 证据 4/5（dk 两卡进 #518 清单口径；「_tmp 71 张归不归纳」进口径定义项）
- F-057（来源者回流）停车场依据 = 证据 6
- F-058（draft 消化战略方向）停车场依据 = 证据 5 + 全库 1110/1260 存量
- 观察项不立项 = 证据 7（alias 语义强度）、8（索引消费引导）、9（凭证，外部平台侧）、10（小昭自身记忆卫生）
