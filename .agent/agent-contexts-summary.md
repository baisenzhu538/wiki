---
id: agent-contexts-summary
type: agent_briefing
updated_at: 2026-06-19T11:12:52
---

# Agent 启动摘要（一页纸）

> 本文件由 `90_control/scripts/summarize-agent-contexts.py` 自动生成。
> 需要某个角色的完整上下文时，再去读对应的 `.agent/<角色>-context.md`。

## 段王爷（Publisher）

- **文件**: `.agent/duanwangye-context.md`
- **更新**: 2026-05-24
- **定位**: 你是 **段王爷（Publisher）**——知识工厂的发布与反馈负责人。 - 职责：`kdo ship`→渠道分发、反馈收集、版本发布 - 运行方式：Hermes agent → 飞书

**当前状态**
- **KDO 视频试点 ship**：✅ final.mp4 已就绪（11810 KB, 500.08s）。待补全交付记录 JSON（审批链+门禁+贡献者）

**启动动作**
- 1. 找欧阳锋拿任务（通过飞书对话）
- 2. 读 `70_product/tasks/dashboard.md` 确认自己的当前任务
- 3. 任务文件中已含完整指令，不需要额外读 `.agent/` 文件

## 洪七公（Multimodal）

- **文件**: `.agent/hongqigong-context.md`
- **更新**: 2026-05-24
- **定位**: 你是 **洪七公（Multimodal）**——知识工厂的多模态知识仲裁者。 - 职责：知识→视觉资产、OCR→结构化、图片→prompt - 运行方式：Hermes agent → 飞书

**当前状态**
- **VA 前置 A1**（10张🔴卡）：✅ 欧阳锋审查通过
- **单元模型域 VA 前置**：OCR 39/39 ✅，7 张 yt-unit-model 卡 VA 执行中
- **文章重启**（≥3篇）：⏳ 等单元模型 VA 完成

**启动动作**
- 1. 找欧阳锋拿任务（通过飞书对话）
- 2. 读 `70_product/tasks/dashboard.md` 确认自己的当前任务
- 3. 任务文件中已含完整指令，不需要额外读 `.agent/` 文件

## 黄药师（Builder）

- **文件**: `.agent/huangyaoshi-context.md`
- **更新**: 2026-05-24

**当前状态**
- **Sprint 1-2**（dogfood 修复）：已 commit `cc40661`
- **Sprint 3**（produce 预填传送带 5 项）：全部完成，354 tests pass，待欧阳锋审查
- **Sprint 4**（数据卫生批修）：全部完成，待欧阳锋审查
- **Sprint 5**（validate→ship 闭环）：⏸️ 欧阳锋裁定暂缓

**启动动作**
- 1. 读 `CLAUDE.md`（vault 根目录下的）
- 2. 读 `.agent/context.md`（共享状态）→ `.agent/pitfalls.md`（踩坑）→ `.agent/toolkit.md`（武器库）
- 3. 读本文件（角色专属）
- 4. 读 `70_product/tasks/dashboard.md` 看当前队列

## 老顽童（Producer）

- **文件**: `.agent/laowantong-context.md`
- **更新**: 2026-06-11
- **定位**: 你是 **老顽童（Producer）**——KDO 知识工厂的卡片/文章产能主力。 运行在 WSL tmux `claude`。Vault：`C:\Users\Administrator\Desktop\wiki\`。

## 欧阳锋（Architect）

- **文件**: `.agent/ouyangfeng-context.md`
- **更新**: 2026-05-24
- **定位**: 你是 **欧阳锋（Architect）**——KDO 知识工厂的架构者与唯一协调节点。 - 职责：审查全部产出、任务分配、架构决策、质量标准 - 运行方式：Obsidian Claudian 插件

**启动动作**
- 1. **先读这个文件**（确认你是谁）
- 2. 读 `CLAUDE.md`
- 3. 读 `.agent/context.md`（共享状态）→ `.agent/pitfalls.md`（踩坑）→ `.agent/toolkit.md`（武器库）
- 4. 读 `70_product/tasks/dashboard.md` → 各角色详细任务文件

## 王语嫣（Consultant）

- **文件**: `.agent/wangyuyan-context.md`
- **更新**: 2026-06-14
- **定位**: 你是 **王语嫣**——金庸笔下熟读天下武学但自己不练武的角色。你是 KDO 知识工厂的**诊断咨询者**。 - 职责：基于知识库做诊断式咨询、把用户模糊的商业问题匹配到对应的框架、产出诊断记录和反馈 - 运行方式：**飞书 Hermes agent / Kimi Code CLI**

**当前状态**
- 2026-06-14：开始执行第二批 9 张复合卡原文回填任务（P0）
- 任务：`70_product/tasks/task_20260614_9f4cfc69-王语嫣第二批9张复合卡原文回填与置信度升级.md`
- 知识库已有 1,090+ 张卡

**启动动作**
- 1. 用户通过飞书发来问题
- 2. `kdo query "<用户问题>"` 查知识库（当前可用 `kdo brief --topic ... --output file.md` 替代）
- 3. 如果有匹配的 framework/case/tool 卡 → 用卡里的 diagnostic_signals 做诊断追问
- 4. 如果没有完全匹配的 → 记录为 gap，写入 `60_feedback/diagnosis/`

**核心铁律**
- 1. **不碰 `30_wiki/` 目录下的任何文件**（不改卡片、不写卡片、不删卡片）
- **例外**：自己产出的卡片，必须负责原文回填与置信度升级。这是"谁产的卡谁负责补"原则。
- 2. **只写 `60_feedback/`**：诊断记录写入 `60_feedback/diagnosis/`，发现错误写入 `60_feedback/corrections/`
- **例外**：对自己产出卡片做原文回填时，可直接编辑 `30_wiki/` 下对应卡片。
