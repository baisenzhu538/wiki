---
id: task_20260816_huangyaoshi-kdo-mcp-rollout
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-16
priority: P1
wsjf: 3.5
created_at: 2026-08-16
updated_at: 2026-08-16
submitted_at: 2026-08-16
source: #324 终审 PASS A-（2026-08-16 欧阳锋）→ P1 立项
related: #324 #308 #263
---

# P1 统一检索层：kdo MCP 全 agent 推广 + 索引事件驱动化（#325）

## 背景

#324 诊断终审 PASS A-（欧阳锋 2026-08-16）：知识传导最大缺口是检索接入不均。P1 = 统一检索层，收益最大改动最小。**按终审 TODO 修正核算口径**：推广范围按实际 gateway 部署核算（Windows 侧 8 + WSL 侧 8 profiles），编译产物按 38 个实际清单核算。

## 实测现状（2026-08-16 王语嫣复核，终审口径修正）

**Windows 侧 Hermes profiles（~/.hermes/profiles/，8 个）**：
- 已挂 kdo MCP（3）：basic-skills-coach / coaching-leadership-assistant / meeting-assistant
- **待补（5）**：duanwangye / hongqigong / laowantong / wangyuyan / note-coach

**WSL 侧 Hermes profiles（8 个）**：
- 已挂 kdo MCP（6）：beikai（kdo+openmontage 双挂，保留不动）/ duanwangye / laowantong / laowantong-feishu / ouyangfeng / wangyuyan
- **待确认（2）**：duan / kimi-test——疑似测试 profile，确认用途后决定补挂或豁免

**快照型 agent**：编译产物 38 个（.agent/prompts/，最新 Jul 15 01:33，全部早于 8 月新卡）；真正部署的快照型 agent = 销售对话助理（CLAUDE.md 写死 5 卡路径）、AI 基本功教练

## 任务

1. **Windows 侧 5 个 profile 补挂 kdo MCP**：复制已挂 profile 的 mcp_servers 节（`kdo-tools/mcp/server.py`，参照 basic-skills-coach config.yaml）
2. **WSL 侧 duan/kimi-test 确认**：用途核实——废弃则豁免并标注；在用则补挂
3. **快照型 agent 加检索指令**：销售对话助理 / AI 基本功教练 CLAUDE.md 加"先 kdo query 再查路径表"（新知识优先检索，路径表兜底）
4. **索引事件驱动化（E028 机制化）**：kdo 生产流水线（#263）加"终审闭环 → 索引增量更新"环节——生产端报告完成时触发索引刷新（或 watchdog 检测卡 mtime 变更自动增量更新）

## 验收标准

- Windows 5 个 + WSL 确认后的 profile 全部挂 kdo MCP
- 每个新增 profile `kdo server initialize` 实测通过 + 一次检索冒烟（如 `kdo query "SPIN"` 命中）
- 快照型 agent CLAUDE.md 检索指令落盘
- 索引事件驱动环节落盘（#263 流水线文档更新）
- 回归：已有 3+6 个 profile 不受影响（不动其 config）

---

## WSL duan/kimi-test 用途确认（2026-08-16 黄药师实测）

| profile | 证据 | 结论 |
|:--|:--|:--|
| duan | SOUL=段王爷角色（与 Windows 侧 duanwangye 重复）；`platforms: {}` 无平台绑定；无 gateway.pid 未运行；cron 空 | **废弃 → 豁免**（不挂 MCP，不删除文件） |
| kimi-test | SOUL=未编辑默认模板（Hermes Agent Persona 样例）；provider kimi-coding；无 gateway.pid 未运行 | **测试 profile → 豁免** |

豁免理由：两个均非在用 gateway（无 pid、无平台绑定），挂载无实际消费方；保留文件不删除（用户资产）。若未来启用任一 profile，按本任务相同模式补挂即可。

## 边界

- 不动已挂 MCP 的 profile（beikai 的 openmontage 保留——混合挂载是既成事实，不评判）
- 不动 WSL gateway 运行中的服务（挂载配置修改后由用户/黄药师在合适时机重启生效）
- 单角色单任务（E026）：黄药师执行，欧阳锋终审

---

## 执行报告（2026-08-16 黄药师）

### 1. Windows 5 profile 补挂 kdo MCP ✅

**挂载**：`~/.hermes/profiles/{duanwangye,hongqigong,laowantong,wangyuyan,note-coach}/config.yaml` 各追加 `mcp_servers.kdo` 节（与 basic-skills-coach 模板一致：`C:\Program Files\Python312\python.exe` + `kdo-tools/mcp/server.py` + `WIKI_ROOT/KDO_SRC` env）。**只挂 kdo 检索 server，不扩散 feishu_doc 操作型 MCP**（#325 范围=统一检索层）。

**安全**：每文件先备份 `config.yaml.bak-kdo-mcp-20260816`；挂载后 yaml.safe_load 全量解析验证（assert mcp_servers.kdo.enabled=True）——5/5 通过。

**验收（协议级实测）**：MCP stdio initialize → notifications/initialized → tools/list → tools/call kdo_search：
- initialize ✅（serverInfo: kdo v1.28.0，244 frameworks/106 skills/10 workflows/8 agent specs）
- tools/list ✅（4 工具：kdo_search/kdo_onboard/kdo_read/kdo_capabilities）
- **检索冒烟 ✅**：`kdo_search("SPIN 销售")` 命中 `yt-entrepreneur-spin-selling`（SPIN销售法）
- exit 0 全程

> ⚠️ 挂载配置在 config 层——**WSL 侧已挂的 gateway 不受影响**；Windows 侧新挂的 5 个 profile 待各自 gateway 重启后生效（不动运行中服务，边界声明）。

### 2. WSL duan/kimi-test 确认 ✅（见上节"WSL duan/kimi-test 用途确认"）

两 profile 均废弃/测试 → **豁免**，不挂 MCP，文件保留。

### 3. 快照型 agent 检索指令落盘 ✅

| agent | 文件 | 变更 |
|:--|:--|:--|
| 销售对话助手 | `agents/sales-dialogue-assistant/CLAUDE.md` | 新增"检索纪律"节：先 `kdo query` 再查路径表（路径表兜底）；引用卡名检索实证（E020） |
| AI基本功教练 | `agents/agent-basic-skills-coach/CLAUDE.md` | 同上 + 数据源周期表 JSON v0.8→**v1.0**（含 evidence 分级，顺带修正过期引用） |

**实证**：`kdo query "销售 用户分层" --limit 3` 命中 `framework-yitang-sales-target-tradeoffs`（销售目标权衡框架）——检索链路可用。

### 4. 索引事件驱动化（E028 机制化）✅

`30_wiki/workflows/workflow-kdo-agent-production-pipeline.md`：
- **新增 Step 4"索引事件驱动化"**：终审闭环（reviewed）→ `kdo index --rebuild` → `kdo query` 自检 → 传导生效；含 4 个机制化落点（提审提醒/批处理/单卡即时/事件驱动替代轮询）+ 反面教材 #305（8-09 索引过期 4 天 85 卡检索不到）
- **失败模式补 E028 行**：索引过期 → 终审闭环后 rebuild + query 自检
- `kdo index --rebuild` 命令实证存在（--help 通过）

### 5. 回归

- 已挂 MCP 的 3+6 profile config **0 修改**（仅新增 5 个目标文件）
- feature_menu 等既有工具未动
- 快照 agent CLAUDE.md 仅追加检索纪律节，原路径表保留（兜底）

### 验收对照

| 验收标准 | 结果 |
|:--|:--|
| Windows 5 + WSL 确认后全挂 | ✅ 5 挂 + 2 豁免（废弃/测试） |
| 新增 profile kdo initialize + 检索冒烟 | ✅ 协议级实测（initialize/tools/call 全过，SPIN 命中） |
| 快照 agent 检索指令落盘 | ✅ 2 个 CLAUDE.md |
| 索引事件驱动落盘（#263 文档） | ✅ Step 4 + 失败模式 |
| 回归：已有 3+6 不动 | ✅ 0 修改 |

### 遗留/建议

- **新 agent 出生模板固化**（P2-DYN-01 ①）：#263 流水线部署步骤加"挂 kdo MCP"为固定动作——P2 立项时执行（设计已在停车场 P2-DYN-01）
- **健康检查升级**（P2-DYN-01 ②）：08-14 health-check 加"MCP 挂载/新卡可检索"巡检项——P2 立项时执行
- Windows 侧 5 profile 的 gateway 重启时机由用户/各 agent 安排（挂载即配置就绪）

## 终审记录（2026-08-16 欧阳锋）

**verdict: PASS A · methodology v2.3**

O3 独立验证（全部字节级重跑，不采信报告）：
1. **5 profile 挂载 ✅**：duanwangye/hongqigong/laowantong/wangyuyan/note-coach 的 config.yaml 均含 mcp_servers.kdo 节（server.py + WIKI_ROOT/KDO_SRC env），备份 .bak-kdo-mcp-20260816 5/5 存在，yaml.safe_load 5/5 解析 enabled=True
2. **只挂 kdo 不扩散** ✅：5 个 mcp_servers 节仅 kdo 一个键（无 feishu_doc）
3. **回归 3+6 零修改** ✅：已挂 3 profile mtime 08-10 未动
4. **WSL 豁免双证** ✅：duan/kimi-test platforms 空 + 无 gateway.pid（未运行）——豁免成立
5. **快照 agent 检索指令** ✅：销售对话助手 CLAUDE.md 检索纪律节（L15-21）+ AI 基本功教练（含周期表 v1.0 修正）
6. **事件驱动化落盘** ✅：#263 工作流 Step 4（L143-160）+ E028 失败模式行（L251）
7. **协议级实测（独立重跑）** ✅：kdo_search("SPIN 销售") → 命中 yt-entrepreneur-spin-selling，PASS

边界遵守：未动运行中服务（gateway 重启时机由用户安排）；WSL 侧 beikai openmontage 混合挂载保留。

遗留 P2-DYN-01（①新 agent 模板固化 ②health-check MCP 巡检）已在任务单登记，P2 立项时执行。

**结论**：PASS A，统一检索层落地完成，验收通过。

## 遗留修正（2026-08-16 欧阳锋·#326 立项核查发现）

**🔴 实质遗漏：P1 覆盖率虚标——5 个运行中 gateway 实际未获 kdo 检索**

O3 字节级核查（#326 立项时验证"8+6 profiles 巡检"范围，发现 #325 核算前提错误）：

| 事实 | 证据 |
|:---|:---|
| 8 个运行中 gateway 分两侧 | systemctl WorkingDirectory：3 个新助理（basic-skills-coach/coaching-leadership-assistant/meeting-assistant）→ Windows 侧；5 个生产角色（beikai/duanwangye/laowantong/laowantong-feishou/ouyangfeng/wangyuyan）→ **WSL 侧** |
| WSL 侧 6 个 profile 挂载 | 全部**无 kdo**（beikai=openmontage、duanwangye/laowantong=wechat、laowantong-feishu/ouyangfeng/wangyuyan=无 MCP）——与任务书"已挂 kdo MCP（6）"声明**不符** |
| #325 补挂的 Windows 5 profile 实际使用 | duanwangye/laowantong/wangyuyan 的 gateway WorkingDirectory 指向 **WSL 侧副本**（Windows 副本空挂）；hongqigong/note-coach 无 gateway 服务（闲置） |

**影响**：P1"统一检索层"实际生效覆盖 = 3/8 运行中 gateway（未变化）；5 个生产角色（洪七公/段王爷/老顽童/王语嫣/欧阳锋 WSL 实例）仍无 kdo 检索——#324 诊断的"检索接入不均"核心缺口**未修复**。

**修正动作**：
1. #326 巡检范围改为"按实际运行 gateway 的 profile 位置（8 个 service WorkingDirectory）逐挂载验证"，不得按目录名/文件修改
2. 补挂动作应作用于 WSL 侧 profile（`~/.hermes/profiles/{beikai,duanwangye,laowantong,laowantong-feishu,ouyangfeng,wangyuyan}/config.yaml`），或按 O-12 方向迁移后统一处理
3. 本修正并入 #326 任务书，P1 收尾与 P2 巡检一并闭环

**教训**：验收"补挂完成"不能只看目标文件被改——必须验证"实际运行进程读的配置文件"是否被改（双位置部署下目录名相同≠文件相同）。
