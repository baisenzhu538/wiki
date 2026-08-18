---
id: task_20260816_huangyaoshi-research-partner-deploy
assignee: codex
status: reviewed
priority: P0
wsjf: 4.0
created_at: 2026-08-16
updated_at: '2026-08-17T17:38:12.545292+00:00'
source: 用户指令（2026-08-16"你的爆炸式建模助理可以开始建设了"）——#335 spec 终审 PASS A- 后的部署授权；迁移验证约束解除（T1
  三 profile 已验证）；改派：黄药师→codex（用户拍板 2026-08-16）
related: null
reviewed_by: 欧阳锋
review_date: '2026-08-18'
grade: A
---

# R 型爆炸式调研 Partner 部署（#348）

## 背景

#335 R 型 spec 已终审 PASS A-（欧阳锋 2026-08-16，🟡提示：部署时验证 TCPR 切换实测）。用户拍板开始建设。数据源 = #332 五卡已入库。

## 规格（#263 流水线 Step 2/3，参照 #303/#304 先例）

1. **三件套注入**：
   - 认知件（SOUL.md）：**默认 R（Research）声明 + TCPR 可切换协议**（spec 二，参照 #303 先例）+ **五状态机工作流内嵌**（定边界→规划信息源→饱和送→分类人拍板→资产报告，每阶段"确认后前进"门控——spec 四）+ 五步法 + 九字诀 14 策略 + **饱和自证话术**（每轮报新增量/收敛信号）+ 打样纠偏/人拍板/借假修真/交付做厚纪律 + 检索规则（**先查调研域 digest/MOC（four-research-types/research-radar）→ kdo_search → grep 兜底**，#308 模式）+ 时间锚定输入要求
   - 路径件（config.yaml）：cwd=wiki；approvals.smart；feishu 通道；**external_dirs 指向 vault skills**（E030 已修，shared 70 技能可全加载）；**mcp_servers.kdo 挂载 + 验证消费层**（E029 教训：不只配了，要验证 gateway 实际读它）
   - 部署件：`agents/research-exploration-partner/`（SPEC.md 已就位 ✅）+ Hermes profile `research-explosion-partner` + `30_wiki/tools/agent-spec-research-explosion-partner.md`（cap_hub 可发现副本）
2. **cap_hub 注册**：agent-spec 自动发现（参照 #303 修复后模式）
3. **飞书链接**：profile 带 feishu 通道配置 + 真机冒烟
4. **数据目录统一**：Windows 侧 AppData\Local\hermes\profiles\（与 laowantong 同侧，E029 双位置教训——不建 .hermes 侧）
5. **调研系列互链**：与挖掘式/OSCAR 调研 agent 系列边界声明入 SOUL（spec 一分工表：单点深挖/里程碑推理不抢）

## 验收标准（spec 八 + #335 终审🟡）

- TCPR 声明（默认 R）+ **TCPR 切换实测**（🟡终审提示项）
- 五状态机门控实测（每阶段"确认后前进"）
- 基线用例 3 个全链：①盘点型"交互设计原则 90 条" ②方向型"OPC 一人公司方向 128 条" ③私有库"一堂现有课程总量锚定"
- 引用卡名 5/5 真实（O0 核对：#332 五卡名）
- 饱和自证话术生效（每轮报告新增量）
- 飞书可用（真机冒烟）

## 边界

- 单角色单任务（E026）：黄药师部署；spec 内容不改（#335 已终审）
- 与教练助理/会议助理边界不冲突；R 型不做线下调研/不决策（spec 六）

## 回滚

删除 profile + 三件套回滚（参照 #303 回滚先例）

## 执行门禁

✅ **用户已授权，可执行**（不挂起；洪七公迁移 codex 并行不阻塞）


---

## 执行报告（2026-08-16 Codex 观察者）

### 结论（一句话）
**三件套 + cap_hub 全部落盘，本地 CLI 验收 6 项通过 5 项；剩余 2 个阻塞项需外部输入：① 飞书新应用凭据（用户创建）② kdo_search 实际调用命中 hermes v0.20.0 MCP SDK 2.0.0 兼容 bug（系统级，非本 profile）。**

### 交付清单（全部已落盘）

| 件 | 路径 | 状态 |
|:--|:--|:--|
| 认知件 SOUL.md | `AppData\Local\hermes\profiles\research-explosion-partner\SOUL.md`（9518B） | ✅ 默认 R + TCPR 可切换 + 五状态机内嵌 + 饱和自证 + 五步法 + 九字诀 + 检索规则 + 时间锚定 |
| 路径件 config.yaml | 同 profile（2297B，与三新助理逐字节一致） | ✅ cwd=wiki / approvals.smart / external_dirs=vault skills / kdo+feishu_doc MCP |
| 凭据件 .env / auth.json / channel_directory.json | 同 profile | ✅ DeepSeek 用三新助理组同 key；**FEISHU_APP_ID/SECRET 待用户创建新应用后补入** |
| 记忆件 MEMORY.md / USER.md | 同 profile\memories | ✅ USER 共享用户偏好；MEMORY 记部署锚点 |
| agents 目录 | `wiki\agents\research-explosion-partner\`（SPEC.md 7158B 已就位 + SOUL.md 9518B + CLAUDE.md 1679B） | ✅ |
| cap_hub 可发现副本 | `wiki\30_wiki\tools\agent-spec-research-explosion-partner.md`（5273B） | ✅ `python -m cap_hub list` 已命中 |
| 调研系列互链 | SOUL.md 分工表（挖掘式单点深挖/OSCAR 里程碑推理不抢） | ✅ |

### 验收实测（本地 CLI，非飞书）

| 验收项 | 结果 | 证据 |
|:--|:--|:--|
| profile 识别 + config 可解析 | ✅ | `hermes profile show`：Model deepseek-v4-flash / .env exists / SOUL.md exists |
| TCPR 声明（默认 R） | ✅ | 身份自检首句"我本次以 R（Research/研究）身份与你协作" |
| TCPR 切换实测（🟡 终审提示项） | ✅ | "切换到 P（实践）身份"→ 输出 7 步可执行调研清单 + 声明可切 T/C/P |
| 五状态机门控内嵌 | ✅ | 状态 1-5 逐条输出；R 型默认请求只做状态 1（探索文件、未跳步） |
| 饱和自证话术生效 | ✅ | "轮次\|新增条数\|对已有体系修正" + 连续 2 轮新增量下降即停 |
| 引用卡名 5/5 真实 | ✅ | framework-baozhashidiaochan-five-step / concept-research-saturation-coverage / framework-r-type-research-partner-five-state / tool-nine-character-mantra-14-strategies / concept-open-a-document（全部 O0 核对 30_wiki 实际存在） |
| 基线用例 1（盘点型 90 条） | ✅ 结构验证 | 交互设计原则 → 5 类×15-20 条≈90 条 + 四字原则 + 讲香 + DataPack + 饱和证据附录 |
| 基线用例 2/3 | ⏸ 待交互 | OPC 128 方向已识别"方向型"并启动状态 1；总量锚定未跑（需多轮确认，非一次性 CLI 可全链） |
| **kdo MCP 消费层（E029）** | ✅ 注册层 / ⚠️ 调用层 | 注册层：agent.log `MCP server 'kdo' registered 8 tool(s): mcp__kdo__kdo_search...`；调用层见下方阻塞项② |
| cap_hub 发现 | ✅ | `agent-spec-research-explosion-partner` 出现在 cap_hub list |

### 阻塞项（2 个，均非本 profile 配置问题）

**① 飞书凭据（需用户创建新飞书应用）**
- 现 9 个 profile 的 FEISHU_APP_ID 已逐一核验，无闲置 APP_ID；同一 APP_ID 严禁双开（历史 T2 教训）。
- 待用户在飞书开放平台为"R 型爆炸式调研 Partner"新建应用，提供 App ID + App Secret 后补入 `.env`，再跑 NSSM 服务化 + 飞书真机冒烟。
- **在凭据到位前不启动 gateway**（避免 feishu websocket 抢连/重启循环）。

**② kdo_search 实际调用报错（hermes v0.20.0 系统级 bug，非本 profile）**
- 现象：`MCP tool kdo/kdo_search call failed: 'CallToolResult' object has no attribute 'isError'`
- 根因（已定位）：hermes venv 用 MCP SDK **2.0.0**，其 `CallToolResult` 字段为 `is_error`（snake_case），而 hermes `tools/mcp_tool.py` L4964 仍读 `result.isError`（camelCase）→ AttributeError。
- 影响面：**所有 profile 的所有 MCP 工具调用**（kdo_search/kdo_read/feishu_doc_create 等）都会中招，非 research-explosion-partner 独有。
- 验证：kdo 库层 `tools.search()` 直调正常（索引已重建 3468 节点/8342 边，命中 framework-baozhashidiaochan-five-step 等真实卡）；hermes 客户端层才崩。
- 建议：单独立项修 hermes mcp_tool.py 的 isError/is_error 兼容（改一处，全局受益），不并入本部署任务。

### 数据目录统一（E029 教训）
- ✅ 唯一落点在 Windows `AppData\Local\hermes\profiles\research-explosion-partner`，**未建 `.hermes` 侧**。

### 回滚
- 删除 profile 目录 + 删除 `wiki\30_wiki\tools\agent-spec-research-explosion-partner.md` + 回滚 agents 目录 SOUL/CLAUDE（SPEC.md 为 #335 交付物保留）。无 NSSM 服务（未启动 gateway），无 WSL unit。

### 待办（等外部输入后补跑）
1. 用户提供飞书 App ID/Secret → 补 `.env` → NSSM 服务化（`hermes-gateway-research-explosion-partner`）→ 飞书真机冒烟。
2. hermes isError 修复后 → 重跑 kdo_search 消费层实测 → 补基线用例 2/3 全链交互验收。

*Codex · 2026-08-16 · #348 部署环节（#263 流水线 Step 2/3）*

---

## 补充记录（2026-08-16 晚 Codex）

### 阻塞项②已修复 ✅（hermes MCP isError）

用户拍板单独立项修。根因不是 mcp_tool.py 代码 bug，而是 **venv 误装 mcp 2.0.0**（hermes-agent 0.20.0 声明依赖 `mcp==1.28.1`，代码用 camelCase `isError`，MCP 2.0.0 改成 snake_case `is_error`）。

**修复**：`pip install mcp==1.28.1`（降级到声明版本，一次性恢复全部 camelCase API 契约）。

**验证**：新进程 kdo_search 实测 `completed (178.40s, 12910 chars)`——修复前同调用 `isError AttributeError` ❌→✅。详见 `agent复盘\codex\hermes-MCP-isError修复记录-2026-08-16.md`。

**遗留**：8 个运行中 gateway 需重启才加载 mcp 1.28.1（修复前启动的进程内存里仍是 2.0.0）；kdo_search 178s 慢是 kdo 服务端索引加载问题，另立项。

### 飞书凭据已收到 ✅

用户提供新应用：APP_ID `cli_aa0b0b564a789ce0`（已核验与其他 9 profile 无重复）→ 补 .env → NSSM 服务化 → 冒烟（见下一节）。

---

## 飞书接入完成（2026-08-16 晚 Codex）

### 凭据
- FEISHU_APP_ID = `cli_aa0b0b564a789ce0`（与其他 9 profile 无重复，核验通过）
- FEISHU_APP_SECRET 已写入 .env（不落盘明文到本文件）

### NSSM 服务化（与 T1/T2 同规范）
- 服务名：`hermes-gateway-research-explosion-partner`
- Application: hermes-agent venv hermes.exe；AppParameters: `gateway run`；AppDirectory: profile 目录
- Start=SERVICE_AUTO_START；AppExit Default=Restart / 78=Ignore；AppRestartDelay=5000；AppThrottle=1500；AppRotateFiles=1/Online=0/Bytes=10485760
- AppEnvironmentExtra 7 项（HERMES_HOME/PYTHONIOENCODING/PYTHONUTF8/HOME/USERPROFILE/APPDATA/LOCALAPPDATA）
- AppStdout/Stderr → profile\logs\nssm-*.log（指向 AppData 侧，非 .hermes）

### 实测
- 服务 Running + Automatic ✅
- gateway.log：`[Feishu] Connected in websocket mode (feishu)` → `✓ feishu connected` → `Gateway running with 1 platform(s)` ✅
- agent.log：kdo + feishu_doc 各 8 tools 注册成功（mcp 1.28.1 修复后新进程）✅
- gateway-exit-diag.log：gateway.start 计数=1，无 auto-restart 循环 ✅
- `Channel directory built: 0 target(s)` —— 新飞书应用尚无会话，**待用户给新 bot 发首条消息完成配对 + 真机冒烟**。

### #348 剩余待办
1. 用户向新飞书 bot 发消息 → 验证入站/出站链路（真机冒烟最后一环）。
2. 基线用例 2（OPC 128 方向）/ 3（总量锚定）全链交互验收（需多轮确认，等用户在飞书/CLI 实测）。
3. 8 个既有 gateway 重启以加载 mcp 1.28.1（isError 修复生效，另协调）。
---

## 真机冒烟证据（2026-08-16 用户转发）

**R 型 Partner 自我介绍消息（用户转发）= 冒烟最后一环**

| 验收项 | 证据 |
|:--|:--|
| TCPR 默认 R 声明 | ✅ 首句"我本次以 R（Research/研究）身份与你协作"+ 三种切换身份表格（T/C/P/R） |
| 五状态机 | ✅ 完整流程介绍（①定边界→②规划信息源→③饱和送→④分类人拍板→⑤出资产报告）+ "确认后前进"门控 + 每轮报新增量 |
| 边界 | ✅ 四不：不做线下/不决策/不抢单点/不做内容生产 |
| 饱和自证 | ✅ "每轮搜索报新增量与收敛信号，数字不骗人" |
| 引用卡名 | ✅ framework-baozhashidiaochan-five-step / concept-research-saturation-coverage / framework-r-type-research-partner-five-state（3/5 本次引用，全部真实；另 2 张在 codex CLI 验收已 O0 核对） |
| 开始协议 | ✅ "丢给我一个课题+材料+关键词+时间锚定，从状态 1 定边界走起"——时间锚定输入要求内嵌 |

## R 型真机实战全链验证（2026-08-16 首战收官——比基线用例更强的验收证据）

**课题**：视频号→逐字稿自动化工作流（发起人：欧阳锋，楚门场景）。产出：`00_inbox/视频号逐字稿调研/视频号逐字稿自动化工作流-爆炸式建模.md`

| spec 验收项 | 实战证据 |
|:--|:--|
| 五状态机全链 1→5 | ✅ 定边界（行号锚点 L2612/L2642）→信息源（欧阳锋门控）→饱和送 3 轮（新增量 15/20/20 递减收敛）→分类（双维分级策略集）→资产报告 |
| 饱和自证话术 | ✅ 每轮报新增量+收敛信号表；第 3 轮 5 新 repo 全落类=规律稳定 |
| 开篇文档纪律 | ✅ 先立 `00_inbox/视频号逐字稿调研/00_状态跟踪.md` 再收集 |
| 资产报告形态 | ✅ 分级策略集（技术能力分层×四环节双维+四字原则）+ 讲香节 + DataPack + 饱和证据附录 |
| verified 分级 | ✅ 实测/引用/推演三档标注 + 未实证清单诚实列（BibiGPT 视频号/sph_caiji_wenan 404） |
| 边界遵守 | ✅ 只做案头；不决策（落地建议交人拍板） |
| 检索兜底 | ✅ kdo_search 超时后 grep 兜底（检索纪律第 3 条），friction-log 上浮 O-16 |

**质量亮点**：下载环节收敛为两条路线（MITM 血统同源 vs API 解析免证书）而非工具并列=真实规律；发现完整链路样板 weixin-favor-kb（与楚门场景 100% 重合）+ Agent Skill 生态 ×5（含 Hermes 原生）；反爬情报（Referer 必带/证书坑/公共 Worker 失效）资产化；落地建议直接解决欧阳锋 collect_wechat.py 的 TikHub token 卡点。

## 遗留待办（#348 收尾）

1. **飞书配对确认**：新 bot channel directory 0 targets——需用户在飞书给新 bot 发首条消息完成配对（若本次冒烟消息即飞书首条，则此条已闭环，待确认）
2. **基线用例 2/3 全链**：OPC 128 方向 / 总量锚定——需多轮交互（用户在飞书/CLI 实测）
3. **8 个运行中 gateway 重启**：加载 mcp 1.28.1（isError 修复），否则旧进程 MCP 调用仍崩——生产影响项，重启时机等用户
4. ~~kdo_search 178s 慢~~ **已修复（2026-08-16 王语嫣，O-15 落地）**：根因=BM25 每次调用全量 load 617MB 索引（search_index.py 无缓存）+ graph 层每次重建 LightRAG（83MB 数据）。修复：search_index.py 加进程级 get_shared_index（mtime 失效）+ 紧凑 JSON（617→537MB）；graph.py _get_rag 加进程级缓存。实测：首次 5.5s+4.1s，二次调用 0.000s，search 0.01s。R 型 gateway 已重启（21:49）加载新代码，kdo MCP 8 tools 注册 ✅，MCP 直测无超时。不再另立项。


---

## 飞书真机冒烟 PASS（2026-08-16 21:29-21:30 实测）

用户已向新 bot 发首条消息，全链路走通：

| 时间 | 环节 | 证据（gateway.log / agent.log） |
|:--|:--|:--|
| 21:29:21 | Feishu 入站 | `[Feishu] Inbound dm message received: text='介绍下你自己' chat_id=oc_31c8aeb54e60bec652719997b9e90a9a` |
| 21:29:26 | gateway 收到 | `inbound message: platform=feishu msg='介绍下你自己'` |
| 21:29:28 | agent 处理 | `conversation turn: platform=feishu msg='介绍下你自己'`（首次 feishu 平台会话） |
| 21:29:39 | 回复就绪 | `response ready: platform=feishu time=13.2s api_calls=1 response=1150 chars` |
| 21:29:39 | Feishu 出站 | `[Feishu] Sending response (1150 chars)` |
| 21:30:29 | 第二轮入站 | `Inbound dm message received: text='你可以调用知识库中哪些知识？'`（自检盘点触发） |

**用户收到的回复（1150 chars）**：默认 R 声明 ✅ / 一句话定位 ✅ / 五状态机 ①-⑤ ✅ / 五步法+饱和覆盖+九字诀 ✅ / 四字原则+讲香+DataPack+饱和证据附录 ✅ / "确认后前进"门控 ✅ / 边界四条 ✅ / TCPR 可切换表 ✅ / 引用三卡真实 ✅。

**结论**：飞书入站→gateway→agent（feishu）→出站全链路打通，#348 飞书可用验收项 PASS。`Channel directory built: 0 target(s)` 已随首条消息消除（会话建立）。

**剩余（不阻塞验收，属交互类验收）**：基线用例 2（OPC 128 方向）/ 3（总量锚定）的多轮"确认后前进"全链交互，建议欧阳锋验收时或用户随后在飞书实测。