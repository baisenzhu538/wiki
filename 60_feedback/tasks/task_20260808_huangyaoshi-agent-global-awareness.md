---
id: task_20260808_huangyaoshi-agent-global-awareness
task_id: 261
assignee: huangyaoshi
status: queued
updated_at: 2026-08-08
domain: system
priority: P0
---

# #261 KDO 全局认知标准化（所有角色 agent）

## 背景（用户期望 + 实测触发）

用户明确期望："所有 agent 都必须知道 KDO 全局，专门的 agent 对专门域更熟悉"。实测发现：
- 角色 agent（王语嫣/老顽童/洪七公/欧阳锋）认知层靠"启动路径注入"（context+agent-os）✅，但 **MOC 清单未同步**（5 个 MOC 建于 #236 后，context 可能滞后）
- **段王爷无 agents/ 部署**（agents/duanwangye/ 不存在——Hermes gateway 直挂，需确认其全局认知来源）
- **飞书端（Hermes）全体无检索层**（Hermes 不支持 kdo_search 类 MCP 工具——coach 已补 MCP 桥 #260，其他角色未接）

## 任务目标

所有角色 agent 的 KDO 全局认知三件套标准化（认知层/路径层/检索层）：

### 1. 认知层：各角色 context 同步"KDO 知识地图"
- `.agent/<角色>-context.md` 统一追加：5 个 MOC 清单（复盘/design/master/product/kdo）+ 各域 digest 入口 + "域知识问题先查 MOC 再回答"（W8 规则 agent 版）
- 覆盖：wangyuyan/laowantong/hongqigong/ouyangfeng/duanwangye（段王爷先建 context 或确认其认知来源）

### 2. 路径层：段王爷部署确认
- 确认 agents/duanwangye/ 是否需要建（或段王爷的认知来源=Hermes gateway 独立 prompt）——黄药师裁定并补齐

### 3. 检索层：飞书端 MCP 桥推广（#260 的 coach 桥复用）
- 把 coach 的 kdo_search/kdo_read MCP 桥（黄药师 #260 已写）推广到所有 Hermes gateway 角色（王语嫣/老顽童/洪七公/段王爷）
- 统一桥规范（对齐 #260 的 30 行实现 + kdo query 语义：MOC 优先 + BM25 融合）

## 验收标准

1. 5 个角色 context 全部含 MOC 清单 + 检索规则（grep 可查）
2. 段王爷部署确认（agents/ 或 gateway prompt 落盘）
3. 飞书端任一角色实测："KDO 有哪些域？查复盘方法论"→ 应答命中 MOC 导航（飞书实测）
4. 桥规范落盘（cap_hub 或 90_control——对齐 #260）

## 依赖 / 边界

- #260（coach MCP 桥——复用其实现）
- 与 #252 试点并行（试点后可在飞书端复测）
- 不改变各角色职责边界（只加"全局认知+检索"，不加权限）

---

## 🆕 域清单单一真相源对齐（2026-08-09 飞书端抽查暴露——并入本任务作为事实层统一条件）

**触发**：飞书端抽查"KDO 有哪些域"——两个 agent 答案不一致（段王爷答 5 MOC+12 digest 来自 domains/ 目录；另一实例答 10 路由域来自 domain-routes.yaml）——**域的权威清单无单一真相源**（domain-routes.yaml 10 域 / domains/ 18 卡 / #240 中文白名单 15 个，三处不同步）。

**任务内容（域清单对齐，黄药师）**：
1. 裁定权威源：`90_control/domain-routes.yaml`（检索路由）与 `30_wiki/domains/`（卡导航）——建议：路由为检索权威、domains 为卡导航权威，两者映射表对齐（10 路由 ↔ 18 卡 ↔ 15 中文域）
2. 三处对齐 + 补同步规则：新增域必须三处登记（routing/domains/白名单）
3. 产出：域清单权威映射表（30_wiki/domains/ 或 90_control/ 落盘）

**验收**：任一 agent 问"KDO 有哪些域"→ 两实例答案一致（同一份权威清单）；映射表可查。

---

## 领取安排（2026-08-09 用户裁定 A——黄药师串行）

**领取顺序**：#264（E018+协议+注册）→ #262（权限标准化）→ **#261 剩余（域清单对齐）**——串行领取，不插队。

**域清单对齐执行要点**（黄药师领取时）：
- 裁定权威源（建议：卡导航视图 19 个为权威 + 路由 10 个为检索视图，两视图映射表）
- 三处对齐（domain-routes.yaml/domains/目录/中文白名单）+ 新增域三处登记规则
- 产出映射表落盘后，#261 条件全部关闭（主体 ✅ + 抽查 ✅ + 域对齐 ✅）
