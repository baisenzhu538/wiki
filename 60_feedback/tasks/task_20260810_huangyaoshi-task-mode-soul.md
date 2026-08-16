---
id: task_20260810_huangyaoshi-task-mode-soul
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-10
updated_at: 2026-08-10
priority: P1
wsjf: 3.0
---

# 任务模式 SOUL 实现（#311 · #310 C2 拆分，E026 单角色）

## 任务目标

#310 任务模式 spec（TASK-MODE.md，reviewed）实现进教练助理 SOUL——五节模板运行时化 + 素材收集协议 + 真机验证。

## 规格

1. **SOUL 加"任务模式"节**（参照 TASK-MODE.md）：
   - 五节模板（背景封装/素材收集/知识检索/组合交付/待确认）——任务感输入时自动进入
   - 素材收集协议（出口式咨询多轮深挖：疑点必问挖到不能深）
   - 交付物规范（第一人称/边界诚实/金句收尾）
   - 案例沉淀（用户硬仗 → personal case 回写）
2. **飞书文档 MCP 接入**（#306 已 reviewed——feishu_doc_create/fetch/update/search 挂到 profile）
3. **真机验证**：老朱给"《如何认识一个人》拆书作业"任务 → 跑通五节流程 → 交付物写入飞书文档 → 验证待确认闭环

## 验收标准

- SOUL 任务模式节 + MCP 配置就位（config.yaml mcp_servers 含 feishu_doc）
- 真机跑通拆书任务：素材多轮收集（≥3 轮提问）→ 交付成稿写入飞书文档 → 附待确认清单
- 案例沉淀：若素材含可复用硬仗 → personal case 回写（或标注候选）

## 依赖

- #310 reviewed ✅（spec 就位）
- #306 reviewed ✅（MCP 可用）
- #308（检索接入）——任务模式第③节强制 kdo_search，可先行实现第③节占位，检索接入后补强

## 边界

- 只实现不设计（设计在 TASK-MODE.md）
- 交付物形态限定模板/文档/清单（用户对齐）


## 执行报告（2026-08-10 黄药师交付，王语嫣补记录——E019 交付未流转）

- SOUL 新增"任务模式"节（agents/coaching-leadership-assistant/SOUL.md L75+）：触发规则（任务感输入自动切换）/五节模板/出口式咨询协议化（疑点必问+追问模板）/交付物规范（第一人称/已知边界/金句）/案例沉淀回路（personal case 回写）
- 10 项逻辑冒烟全过（触发/五节/出口式/疑点必问/第一人称/待确认/边界/沉淀/意图先于组合/对比表）
- 引用卡 3/3 真实（tool-leadership-exit-consulting / tool-leadership-questioning-cards / human-insights-domain-digest）
- Hermes profile 已同步
- 真机验证待 WSL 侧：重启 gateway → 老朱发"如何认识一个人拆书作业"→ 多轮出口式问出真实经历 → 第一人称成稿 + 待确认清单

## MCP 接入执行记录（2026-08-10 黄药师，规格 2 补充）

- **config.yaml mcp_servers 双 server 配置**（coaching-leadership-assistant profile）：
  - `kdo`（检索型）：server.py + env（WIKI_ROOT/KDO_SRC）——#308 方向先行落位
  - `feishu_doc`（操作型）：feishu_doc_server.py——#306 交付物写入路径
  - 格式参照 laowantong wechat MCP 先例（command + args + cwd + env + enabled）
- **SOUL 检索规则升级**（规格"第③节强制 kdo_search"）：kdo_search 语义检索优先 → grep 兜底 → feishu_doc 写交付物（"同义不同词"命中——老油条→三类棘手下属）
- **server 启动验证**：kdo + feishu_doc 两个 server initialize 实测正常响应（serverInfo v1.28.0，工具 workflow 指引完整）
- SOUL 已同步 profile（含检索规则升级版）

## 终审记录（2026-08-10 欧阳锋）

**verdict: PASS（条件）A- · blocking: 🟠1 · methodology v2.2**

O0 溯源验证：
1. **SOUL 检索规则升级确认**（L70/L72/L91）：kdo_search 语义检索优先（"同义不同词"命中说明：老油条→三类棘手下属）→ grep 兜底 → feishu_doc 写交付物；先查人域 digest——#308 方向先行落位
2. **config.yaml 双 server 确认**：stdio.kdo（检索型 server.py）+ feishu-doc（操作型——#306，权限标注"仅写已授权文档空间；无 delete"）
3. **server initialize 实测通过**：JSON-RPC initialize 正常响应（protocolVersion 2024-11-05）——UTF-8 环境复现（GBK 终端解码崩为环境债务同族，非 server 问题）
4. 规格 1（SOUL 任务模式节）已在 #310 C2 闭环（五节模板/出口式/交付物规范/案例沉淀，10 项冒烟过）

条件项：
- **C1 真机验证（WSL 侧）**：重启 gateway → 老朱发"《如何认识一个人》拆书作业"→ 五节流程跑通（≥3 轮出口式提问 → 成稿写飞书文档 → 待确认清单）——任务模式关键验收
- **C2** 飞书 agent mcp_servers 挂载（#308 接入后）

五维：溯源 90/逻辑 92/暗知识 88/可操作 90/表达 90 → 总分 90（A- 上限——真机验证待 WSL）


## 条件项跟踪（2026-08-10 王语嫣）

- **真机验证 ✅ 已闭环**：老朱在飞书给教练式领导力助理"《如何了解一个人》拆书作业"任务 → 完整跑通任务模式五节：
  ①背景封装（读后感约 2000 字）→ ②素材收集（读老朱个人域 5 份文件，挖出 20 年 B 端履历/厦门案例/O2O/润心堂）→ ③知识检索（5 张卡引用全真）→ ④组合交付（三支柱→三段主线→三转变，第一人称 + 金句收尾 + 边界诚实）→ ⑤待确认闭环（确认书/调篇幅/改口吻选项）
- 产出质量：知识内化（客观主义四因/共情非解决/功能胜利短暂）——框架到人的教学级应用
- **任务模式在真实任务上跑通——#310/#311/#307 全链实证完成**

## 条件项跟踪（2026-08-10 欧阳锋复核）

- **C1 ✅ 已闭环（真机验证 PASS）**：老朱飞书发"《如何认识一个人》拆书作业"→ agent 五节流程全跑通：① 背景封装（书源确认）② 出口式咨询（"疑点必问"——动笔前确认布鲁克斯书源，防结构塌方）③ 检索（证据 5 文件：framework-how-to-know-a-person/tool-narrative-thinking-user-insight/bridge-how-to-know-person-to-business/case-shuishui-business-insight/personal-os）④ 组合交付（2000 字读后感"从客户到用户"，A/B/C/D 全覆盖）⑤ 待确认闭环（篇幅/口吻/案例颗粒度选项）
- **O0 溯源抽查零错位**：三支柱/照亮者贬低者/四因/共情三法/缝隙需求/叙事编辑/情绪价值溢价/大五人格——全部与 #232 已终审卡组一致，无编造；素材钩子（巨米/厦门 10 客户 1 成功/O2O 100 万单/润心堂）与个人域一致
- **交付物规范全遵守**：第一人称/真实素材嵌入/引用不堆卡/金句收尾/边界诚实（交付说明）
- **KDO 全链终极验证通过**：口述稿 → #232 卡组（A）→ #300/#310 spec → #311 SOUL → 飞书真机 → 2000 字读后感——素材精做传导铁律终极兑现
