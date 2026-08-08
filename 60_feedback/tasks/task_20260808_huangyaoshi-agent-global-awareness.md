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
