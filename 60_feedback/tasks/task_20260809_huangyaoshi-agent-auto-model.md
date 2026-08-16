---
id: task_20260809_huangyaoshi-agent-auto-model
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-10
updated_at: 2026-08-10
priority: P2
wsjf: 2.5
claimed_at: 2026-08-10
---

## 执行报告（2026-08-10 黄药师）——机制调研结论：Hermes 无原生对话级模型路由

### 调研结论（P-21 先诊断：查清机制底座再动手）

**Hermes 原生不支持 agent 对话级模型路由**——证据链：
1. `smart_model_routing`（cheap_model + max_simple_chars/words）——**只有配置定义**（config.py:1863 注册 + setup.py:3312 默认 disabled），**全源码无实现逻辑**（grep max_simple_chars/cheap_model 使用处 = 0）
2. `auxiliary` 段（AGENTS.md 明示）——只支持**子任务级**模型覆盖（curator/vision/session_search 等 side-LLM），不支持同一 agent 对话内按复杂度切换
3. 模型在 config.yaml 固定（model.default）——agent 本身无法自换模型（SOUL 层提示无法生效）

### 三个候选方案评估
| 方案 | 可行性 | 结论 |
|:--|:--|:--|
| 改 Hermes 源码实现路由 | 技术上可行 | ❌ 超边界（任务单限定"只 agent 侧路由不改全局"；改供应商工具风险高 P-28 教训） |
| SOUL 层提示路由 | agent 无法自换模型 | ❌ 机制不可行 |
| **保持现状：固定模型 + 质量门兜底** | 完全可行 | ✅ 当前教练/开会/基本功用 Flash，任务模式深挖已靠 MCP 检索补强，质量门（#269 首交率 + 欧阳锋审查）不变 |

### 建议（待王语嫣/欧阳锋裁定）
1. **#309 回退**（机制不存在，无法实现）——或
2. **降级为文档**：role-model-routing.md 补"Hermes 无原生路由，如要落地需改源码（另开任务评估）"——#277 的成本洞察保留（生产用 Pro 的 ROI 判断仍有效）
3. 附：#277 警示的价格复核已完成——DeepSeek 08-06 公告"整体大幅涨价"，**新价格未公布**（现行价：Flash 输入 1 元/输出 2 元，Pro 3 元/6 元每百万 token，高峰 2×）——即使实现路由，成本测算也待新价确认

### 🔴 用户实测修正（2026-08-10 用户反馈，推翻 #277 路由前提）

**用户实测：Flash 比当前 Pro 预览版更强**（Pro 未正式发布，是预览版）：
- 黄药师本人也跑 Flash（deepseek-v4-flash）——Flash 是当前主力
- **"简单问答 Flash / 深度诊断 Pro"的路由前提不成立**——Pro 预览版质量不如 Flash，路由反而降质
- 修正结论：**保持 Flash 为主力是正确的**；等 Pro 正式版发布后再评估升级（届时 #277 的 ROI 判断才适用）
- #309 的路由需求本质消失（不是"没有机制"，是"没有路由必要"——Flash 已是最优）

### 补充能力：识图（多模态）走 MiniMax VLM（用户提示）
KDO 已有 MiniMax M3 VLM（cap_hub/vlm/core.py，Anthropic 协议，API key 从 .env 加载）——**飞书 agent 的识图需求用 VLM 而非换模型**：
- OCR + 内容理解 + 结构化输出（思维导图/框架图/表格还原）
- 使用：`from cap_hub.vlm import process`（cap_hub 能力中台已登记）
- 意义：agent 需要"看图"能力时，接 MiniMax VLM（#306 feishu-doc MCP 同层的能力接入），不需要 DeepSeek 换模型

### 边界遵守
- 未改任何配置（机制不存在，不硬上）
- 质量门兜底不变（#269 + 欧阳锋审查）

# Agent Auto 模型选择（#309 · 复用 #277 调研）

## 任务目标

飞书 agent 按任务复杂度自动选模型——简单问答 Flash / 深度诊断 Pro（#277 已 reviewed：老顽童 Flash 倒挂洞察，生产用 Pro、批量用 Flash）。

## 规格

1. agent 路径件加模型路由规则（复用 role-model-routing.md 任务分级表 T1/T2/T3）
2. 简单问答（T1：话术例句/单卡引用）→ Flash；深度诊断（T2/T3：五阶梯定位/跨卡证据链）→ Pro
3. 落地前复核 DeepSeek 价格（#277 警示：2026-08-06 涨价 + 高峰 2× 计费）

## 验收标准

- 飞书实测：简单问题走 Flash、复杂诊断走 Pro（响应可观测）
- 成本对比文档更新（全 Flash/混合/全 Pro 三档——#277 已测算）

## 依赖

- #277 reviewed ✅（调研已就位）

## 边界

- 不改全局模型配置（只 agent 侧路由）
- 质量门兜底：#269 首交率 + 欧阳锋审查不变

## 终审记录（2026-08-10 欧阳锋）

**verdict: PASS（裁定：降级为文档）· blocking: 无 · methodology v2.2**

O3 验证 + 裁定：

【证据链验证】
1. smart_model_routing 全库 grep = 0（本地可见范围无实现逻辑）——"Hermes 无原生对话级模型路由"成立
2. auxiliary 段仅支持子任务级覆盖（不支持对话内按复杂度切换）——机制缺失确认
3. 模型固定 config.yaml，agent 无法自换模型——SOUL 提示路由机制不可行

【裁定：选项 2 降级为文档】
- **#277 成本洞察（生产用 Pro ROI 高）仍然有效**——不能丢
- **"Hermes 无原生路由"是重要结论**——落盘 role-model-routing.md 防未来重复调研
- 回退（选项 1）会让证据链丢失；降级文档保留全部价值
- 价格复核已做（DeepSeek 08-06 涨价公告新价未公布）——落地待新价

【执行要求】
- role-model-routing.md 补充节：Hermes 无原生对话级路由（证据链）+ 三方案评估 + "落地需改源码另开任务"
- #277 的 Phase 1 建议（老顽童切 Pro 试点）不受影响，可独立推进（等新价公布后复核）

评价：**P-15 教训正向应用满分**——不硬上不存在的机制、不假装实现，如实报告 + 三方案 + 建议让决策者裁定。调研纪律样板。

五维：溯源 95/逻辑 95/暗知识 90/可操作 90/表达 90 → 总分 93（A）
