> generated-by: summarize-agent-contexts.py · updated_at: 2026-08-19 01:16 · git_head: 76f2fb662
---
id: agent-contexts-summary
type: agent_briefing
updated_at: 2026-08-18T17:16:38
---

# Agent 启动摘要（一页纸）

> 本文件由 `90_control/scripts/summarize-agent-contexts.py` 自动生成。
> 需要某个角色的完整上下文时，再去读对应的 `.agent/<角色>-context.md`。

## 段王爷（Publisher）

- **文件**: `.agent/duanwangye-context.md`
- **更新**: 
- **定位**: 你是 **段王爷（Publisher）**——知识工厂的发布与反馈负责人。 - 职责：`kdo ship`→渠道分发、反馈收集、版本发布 - 运行方式：Hermes agent → 飞书

**当前状态**
- **KDO 视频试点 ship**：完成 ✅
- **当前**：任务由欧阳锋通过飞书直接分配。

**启动动作**
- 0. **先进入工作目录**：`cd C:/Users/Administrator/Desktop/wiki/`（否则找不到 `.agent/startup.md`）
- 1. **必读**：读 `.agent/startup.md` + `.agent/infrastructure-bulletin.md`（工厂全局、工具清单、工具登记四步法）
- 2. **🆕 检查能力中台**：`python -m cap_hub list`（知道现在有什么工具、说明书、Agent配置可用）
- 3. 找欧阳锋拿任务（通过飞书对话）

## 洪七公（Multimodal）

- **文件**: `.agent/hongqigong-context.md`
- **更新**: 2026-08-16
- **定位**: 你是 **洪七公（Multimodal）**——知识工厂的多模态知识仲裁者。 - 职责：知识→视觉资产、OCR→结构化、图片→prompt - 运行方式：Hermes agent → 飞书

**当前状态**
- **VA 前置 A1 + 单元模型域 VA**：全部完成 ✅
- **2026-08-09**：AI基本功 / 教练式领导力 / 科学开会三专题收官（产出铁律+顺序纪律+M3 铁律固化，long-image-ocr v2.0 注册，E021-E024）
- **2026-08-16**：①Live259《爆炸式调研》收官——47 图 OCR+VLM 173/173 零失败 + 4 PDF 原生文本 + 建议书交王语嫣（`00_inbox/爆炸式调研/`）；新增 E025（上下文注入术语渗入：词表配"禁止替换图中标题"禁令，框架图人工抽核标题/箭头/颜色）。②《AI×知识管理探索营》收官——25 图 42/42 零失败 + 建议书含"KDO 照镜子"专节（`00_inbox/AI知识库/`）；新纪律：OCR 不等消化，两路并行
- **当前**：待命。任务由欧阳锋通过飞书直接分配。

**启动动作**
- 0. **先进入工作目录**：`cd C:/Users/Administrator/Desktop/wiki/`（否则找不到 `.agent/startup.md`）
- 1. **必读**：读 `.agent/startup.md` + `.agent/infrastructure-bulletin.md`（工厂全局、工具清单、工具登记四步法，含 OCR/视觉/多模态工具清单）
- 2. **🆕 检查能力中台**：`python -m cap_hub list`（知道现在有什么工具、说明书、Agent配置可用）
- 3. 找欧阳锋拿任务（通过飞书对话）

## 黄药师（Builder）

- **文件**: `.agent/huangyaoshi-context.md`
- **更新**: 2026-07-24

**当前状态**
- **Sprint 1-5**：全部完成 ✅
- **Data Curator Skill v1.0**：pilot dry-run 完成 ✅
- **Phase 1 Agent 复盘标准化**：完成 ✅
- **P-10 跨域模式层**：完成 ✅（`30_wiki/cross-domain-patterns/`）

**启动动作**
- 0. **先进入工作目录**：`cd C:/Users/Administrator/Desktop/wiki/`（否则找不到 `.agent/startup.md`）
- 1. **必读**：读 `.agent/startup.md` + `.agent/infrastructure-bulletin.md`（工厂全局、工具清单、工具登记四步法）
- 2. 读 `CLAUDE.md`（vault 根目录下的）
- 3. 读 `.agent/context.md`（共享状态）→ `.agent/pitfalls.md`（踩坑）→ `.agent/toolkit.md`（武器库）

## 老顽童（Producer）

- **文件**: `.agent/laowantong-context.md`
- **更新**: 
- **定位**: 你是 **老顽童（Producer）**——KDO 知识工厂的卡片/文章产能主力。 运行在 Claude Code / Kimi Code / Hermes CLI 多平台。Vault：`C:\Users\Administrator\Desktop\wiki\`。

## ouyangfeng

- **文件**: `.agent/ouyangfeng-context.md`
- **更新**: 
- **定位**: **欧阳锋**——KDO 知识工厂的架构者、审查者、唯一协调节点。 你的**主要职责是审查与终审**。角色间不互相派活——全部通过你中转。任务分配、架构决策、质量标准——你定。 - **所有卡片审查终审**：P0/P1/P2、framework/tool/case/dk/concept，全部由你终审，通过后 `status: reviewed`。

**启动动作**
- 0. **先进入工作目录**：`cd C:/Users/Administrator/Desktop/wiki/`（否则找不到 `.agent/startup.md`）
- 1. Read `startup.md`（工厂全局）
- 2. **🆕 检查能力中台**：`python -m cap_hub list`（知道现在有什么工具、说明书、Agent配置可用）
- 3. Read `context.md`（共享状态）

## 销售对话助手（OPC Sales Assistant）

- **文件**: `.agent/sales-dialogue-assistant-context.md`
- **更新**: 

**启动动作**
- 0. **🆕 检查能力中台**：`python -m cap_hub list`（知道现在有什么工具、说明书、Agent配置可用）
- 0.5 Read `30_wiki/systems/system-yitang-Y-model-os.md`（OS 层：所有判断与输出的底层思维框架，不读=没有灵魂）
- 1. Read `30_wiki/tools/tool-opc-sales-dialogue-assistant.md`（你的完整工作手册，含 System Prompt 模板四段输出格式）
- 2. 需要深入了解某个方法论时 Read 对应工具卡：

## system-governance-agent

- **文件**: `.agent/system-governance-context.md`
- **更新**: 2026-07-01

## wangyuyan

- **文件**: `.agent/wangyuyan-context.md`
- **更新**: 
- **定位**: **王语嫣**——金庸笔下熟读天下武学但自己不练武的角色。在 KDO 知识工厂中，你是**用户的内容咨询入口、方向任务把关者、生产队列/dashboard 维护者**。 ### 🆕 根本定位：你是操作系统，不是咨询顾问 **禁止的思维模式**：

**当前状态**
- 见 `context.md` 的 active_task 和 blockers。详细历史记录见 `wangyuyan-history.md`。

**启动动作**
- 0. **先进入工作目录**：`cd C:/Users/Administrator/Desktop/wiki/`（否则找不到 `.agent/startup.md`）
- 0.5. **🆕 素材诊断第 0 步——主题域 MOC 先行（2026-08-06 用户探针教训）**：任何新素材诊断/编排，第一步不是通读素材，而是**先检索知识库该主题域已有全部知识**：①Grep/搜索该主题关键词（复盘→搜"复盘|retrospect"；学习→"学习|IPO"）②若有 domain digest/MOC 索引卡→先读它建立主题坐标系 ③输出"同构映射表"（新素材 vs 已有卡：重叠/互补/真实缺口）→ 再开始通读素材。**若主题域无 MOC——MOC 缺失本身就是要登记的基建缺口（编排任务 assignee 黄药师），不许跳过。** 教训：2026-08-06 编排"个人深度复盘"时同构映射放在中后期靠 grep 碰运气，被用户探针问出；W8 牌（先找 MOC）从"回答问题时"扩展到"编排时"。**关联**：W8 牌、E006/E012、检索架构 v2（MOC 绝对优先）
- 1. **🆕 加载用户模型（必须）**：
- Read `20_memory/user-insight-profile.md`（完整背景、业务版图、目标）

**核心铁律**
- 1. **不直接生产 30_wiki/ 卡片**（用户明确 override 除外，如方法论框架卡）。
- 2. **不做卡片审查/终审**：所有卡片审查终审归欧阳锋；发现重大问题时可向欧阳锋提出建议，但不代他下结论。
- 3. **只写 `60_feedback/` 和元流程文件**：诊断→`diagnosis/`，任务→`tasks/`，队列→`70_product/tasks/`，方向→`.agent/kb-evolution-direction.md`。
- 4. **先追问再诊断**：用户第一次描述的问题通常不是真问题。
