---
updated: 2026-07-04
updated_at: 2026-07-04T20:00:00+00:00
status: active
reviewed_by: 欧阳锋
active_branch: main
active_task: "#63-#68 全部 reviewed；#71 reviewed 欧阳锋终审通过（33 张卡，case 卡质量强/tool 达标/dk 偏薄/concept+principle 偏薄缺 Critique，整体 PASS 附质量分层）；#79 reviewed 欧阳锋终审通过（4 张框架卡边界声明追加，纯追加不改已有内容）；#69 依赖满足；#70 blocked；#72-#78 queued；#80-#83 queued"
blockers:
  - "#60 queue_transition 修复（2026-07-04）：欧阳锋重审通过；7/7 tests passed；#60 仍为 queued，需黄药师运行 `queue_transition.py complete`"
  - "#59 Agent Prompt 编译器（2026-07-04）：欧阳锋终审通过；产生 2 项微债务，已由王语嫣开 #62 跟进"
  - "#62 Agent Prompt 设计规范微债务（2026-07-04）：已入队，assignee 黄药师；P2"
  - "#63 一行双三角第二批案例补产（2026-07-04）：已 reviewed，欧阳锋终审通过"
  - "#64 Truman 飞书 To slide PPT 迭代案例卡（2026-07-04）：status reviewed，欧阳锋终审通过；审查报告已生成；任务单编号已修正为 #64"
  - "#65 Y模型 × 双三角协同工作法框架卡（2026-07-04）：status reviewed，欧阳锋终审通过；审查报告已生成；任务单编号已修正为 #65"
  - "#66 人在环 × 双三角关系卡（2026-07-04）：status reviewed，欧阳锋终审通过（PASS）；192行十段齐全；3 外部攻击者（HITL Purist / Lean Startup / Automation Maximalist）视角互不重叠；5 失败模式各有症状/根因/修复；🟡 3 个外部 URL 在 source_refs 中待后续统一处理"
  - "#67 Y模型 引擎层操作法卡（2026-07-04）：status reviewed，欧阳锋终审通过（PASS）；275+行 10 步操作法含预估时间；9 陷阱各有表现/根因/解法；3 外部攻击者含 Truman 元攻击（模型边界意识）；2 变速器合入解放思想/实事求是；🟡 与双三角关系无独立 section 但 Synthesis 表已标注"
  - "#68 跨域审计（2026-07-04）：status reviewed，欧阳锋终审通过（PASS）；10 张卡 6 维评分；发现两代分化（老卡静态/新卡引擎化）+ 非一堂域普遍静态；根因归因到 DK-52~60；修复策略有边界判断（BRM/冰山本身是静态工具，修的是边界声明不是硬加循环）；P0 修复任务单 `task_20260704_laowantong-fix-staticization-yt-decision-y-model` 已入队"
  - "#79 框架卡静态化修复（2026-07-04）：status reviewed，欧阳锋终审通过（PASS）；4 张卡（实事求是/解放思想/冰山/BRM）纯追加边界声明段落，已有内容未触碰；P0 yt-decision-y-model 引擎化升级已先行 reviewed"
- "#69 双三角画布 Agent CLI 交付（2026-07-04）：queued，assignee 黄药师，reviewer 欧阳锋；P1；依赖 #65 reviewed 后老顽童产 agent-spec v2，Agent 必须具备模型/体系边界意识"
  - "#70 双三角课后闲聊洞察卡片化（2026-07-04）：blocked/on-hold，assignee 老顽童(Kimi)，reviewer 欧阳锋；P1；等待用户看完完整视频后再启动，用户确认后 unlock"
  - "#71 底层逻辑三课程补产（2026-07-04）：status reviewed，欧阳锋终审通过（PASS）；33 张卡（21 case + 5 tool + 4 dk + 2 concept + 2 method + 1 principle）；case 卡质量强（Y模型循环映射+双三角对应+Critique 齐全）；dk/concept/principle 卡偏薄，principle-yitang-y-model-boundary 和 concept-yitang-education-formula 缺 Critique/Synthesis，记录为 P2 追补债务"
  - "#72 审美库工作法/工具卡（2026-07-04）：queued，assignee 老顽童(Kimi)，reviewer 欧阳锋；P1；工具原型已就位，可与 #64/#65 并行领取，优先回应用户批评"
  - "#73 Agent 卡片/Skill 执行模式设计（2026-07-04）：queued，assignee 黄药师，reviewer 欧阳锋；P1；分 Phase 交付：Phase 1 设计文档+框架卡可立即启动；Phase 2 原型依赖 #72 工具卡和 #59 编译器；Agent 必须能判断任务类型并声明工具边界"
  - "#74 AI 基本功 Feature 思维概念卡 + 两张草稿卡重写（2026-07-04）：queued，assignee 老顽童(Kimi)，reviewer 欧阳锋；P1；直接回应用户批评；新增 concept 卡 + 重写 `tool-Truman-Feature特性层训练法` 和 `tool-Truman-AI能力分层学习路径`；素材含 AI上手第一课 AMA 和 Truman 自用 FeatureSet"
  - "#75 AI 工具特性清单全网调研（2026-07-04）：queued，assignee 王语嫣，reviewer 欧阳锋；P1；回应用户追问；入口标注 `annotation-ai-feature-inventory-research.md` 已产出；需 web research 公开领域 + 访谈黄药师/老顽童梳理 Hermes/龙虾特性"
  - "#28 lint 内容债（2026-07-01）：状态 paused，assignee 改为 workbuddy，后台分批清理，不阻塞主线队列"

next_session_hint: "下一步：① 黄药师对 #60 运行 `queue_transition.py complete`；② #64-#68/#71/#79 全部 reviewed；老顽童可领取 #72 审美库 + #74 Feature 思维 + #76 死亡飞轮 dk + #77 #66 追补；③ 王语嫣启动 #75 + 决定 #82/#83 P2 优先级；④ #70 等用户 unlock；⑤ 黄药师启动 #73 Phase 1；⑥ workbuddy 空闲处理 #28；⑦ 批量更新 #71 33 张卡 + #79 4 张卡的 frontmatter（status/reviewed_by/review_date）。"
---

## 📢 全厂通知（2026-06-19）

- **`.agent/startup.md` 已上线**：每个 Agent 启动后、领任务前必须先读此文件，3 分钟了解工厂全局与当前状态。
- **`.agent/infrastructure-bulletin.md` 同步生效**：新增“工具登记四步法”——新工具/脚本必须 ① 放入 `40_outputs/code/scripts/` ② 登记到 `README.md` ③ 复杂逻辑写 skill ④ skill 之间互引。不登记 = 不存在。

> 请各角色在下次启动时确认已阅读以上两个文件。已同步更新 `.agent/<role>-context.md` 中各角色启动步骤，将两文件列为第 0 步必读。

## 2026-06-12 变更

### Hermes 全貌（最终态）
| Agent | WSL Service | Feishu Channel | Model |
|:--|:--|:--|:--|
| 洪七公 | hermes-gateway-beikai | oc_71fc... | deepseek-v4-pro |
| 段王爷 | hermes-gateway-duanwangye | oc_f3a9... | deepseek-v4-pro |
| 王语嫣 | hermes-gateway-wangyuyan 🆕 | oc_b8bf... | deepseek-v4-pro |
| 老顽童 | CLI `hermes` | 无 | deepseek-v4-pro |

### 关键教训
- P-27: Provider迁移先查 models_dev_cache 确认 SDK 协议
- P-28: API大规模异常先查公告再调参
- 黄药师铁律: 先诊断后动手，用户说别改就冻结

> ⚠️ **角色中立文件** — 只放共享状态。不写 "你是谁" 类身份描述。
> 各角色的身份定义、SOP、启动指令在 `.agent/<role>-context.md`。
> 看到 "你是谁" 段落 → 删掉，移到对应角色文件。不要在这里写。

## 角色部署

| 角色 | 运行位置 | 工具 |
|------|---------|------|
| 欧阳锋（Architect） | Kimi Code CLI | 审查/深挖重写/协调/拍板 |
| 黄药师（Builder） | Claude Code（Windows 终端） | KDO CLI 开发/基建/lint |
| 王语嫣（Content Consultant + Direction Gatekeeper + Dashboard Maintainer + Task Annotator） | Kimi Code CLI | 内容咨询/方向把关/队列看板维护/任务标注 |
| 老顽童（Producer） | **Hermes CLI（Kimi API）** | 卡片/文章量产 |
| 洪七公（Multimodal） | Hermes agent → 飞书 | 视觉/设计/prompt |
| 段王爷（Publisher） | Hermes agent → 飞书 | 发布/反馈/版本 |

> 角色专属 context 见 `.agent/ouyangfeng-context.md`、`.agent/huangyaoshi-context.md`、`.agent/wangyuyan-context.md`、`.agent/laowantong-context.md`、`.agent/hongqigong-context.md`、`.agent/duanwangye-context.md`。

## 关键路径

| 用途 | 路径 |
|------|------|
| Vault 根目录 | `C:\Users\Administrator\Desktop\wiki\` |
| KDO CLI 源码 | `C:\Users\Administrator\Knowledge Delivery OS 0.0.1\kdo\` |

## 模型与环境

- **模型**：DeepSeek（deepseek-v4-pro，老顽童/洪七公/段王爷/王语嫣共用）；欧阳锋仍用 Kimi 订阅
- **飞书 WebSocket**：cc-connect 和 Hermes 均出现 keepalive ping timeout。重启即修复。P-6 已记录。
- **切模型**：涉及五层配置（`.bashrc` / 注册表 / systemd drop-in / `cc-connect config.toml` / session 缓存）。详见 `pitfalls.md`

## 当前共享状态

### 各角色当前任务
- **黄药师**：KF-020+021全修 + S4-1 aliases + kdo_lint(2344→85) + 决策域研究(2卡A级)
- **老顽童**：战略域 PPT 补强 3/3 验收通过；待命接新任务
- **王语嫣**：完成角色边界调整；负责内容咨询、任务标注、方向把关；维护 production-queue.md / dashboard.md / kb-evolution-direction.md；完成自攻击方法论框架卡并已入队待欧阳锋审核；跟踪 wave1 / 刻意练习域 / 渠道增长域生产进度
- **欧阳锋**：月度抽检模式
- **洪七公**：待命
- **段王爷**：待命

### 2026-06-18 里程碑
- **全库首次 P0=P1=YAML=0**（6/13 以来第一次三项同时归零）
- 老顽童 index/log 元页面 source_refs 从 760→2（`system-index`/`system-log`）
- 全库 clean=1175

### 2026-06-17/18 关键结果
- 决策域研究完成：Value-ROI dk + Y模型哲学根基(欧阳锋A级)
- KF-020 全修：45张 enriched/reviewed 卡 00_inbox→10_raw/sources
- KF-021 95%：681张 hash 前缀→完整文件名
- S4-1 aliases：schema + Graph RAG 搜索索引
- kdo_lint：2344→85 (96%误报清零)
- 王语嫣复盘：P0=P1=0 clean=1193
- 470 skill 重分类为 tool/concept（欧阳锋 taxonomy 裁决执行）
- 231 张 draft 精修池已识别（conf≥0.7+related 非空）
- MinerU 文档化入 wiki + toolkit
- 决策域第一张 dk 卡产出（Value-overrides-ROI）
- 决策域 KF-020 违规报告送审王语嫣

### 2026-06-16 关键结果
- 全库 P0=0, YAML=0, Clean=586
- 老顽童全域案例回溯 35 张（主动执行 KF-025 三问自检）
- OCR 368 张 → raw/ocr/ 分层隔离
- 14 对重复卡片去重, 6 张 deprecated 归档
- kdo query --trust/--view/--save/--template book 上线
- KF-025 + S4 上线
  - `60_feedback/itingnao/medical-cabinet-longterm/method-medical-cabinet-hospital-scene-model.md`
  - `60_feedback/itingnao/medical-cabinet-longterm/method-medical-cabinet-scale-model.md`
- **待验证重点**：单设备真实流水、医院准入政策、合规成本、资金来源、团队产能、供应链授权
- **下一步**：用户/团队线下完成验证任务后，把结果写回 task 文件或 60_feedback/comments/，Kimi 据此更新模型卡片

### KDO CLI 状态
- 47 .py 文件，~13,800 行，15 测试文件
- **pytest**：526/528 passing + 2 pre-existing CSRF failures + 1 skip
- **Graph RAG**：226 entities, 721 chunks, 1252 relations
- **kdo stale**：25 tests pass，待欧阳锋审查后 commit
- 坚果云备份 ✅

### Design 域
- Eagle（图轨）+ Obsidian（文轨），双轨三层。第一批编译已完成 ✅
- 3 张概念卡：AIGC设计基础（生图原理+提示词基本功）、口喷设计范式+电商全流程、Leo文创IP案例
- 源素材：月白（一堂）AIGC设计课程口述 3 期 → ingested → enriched → indexed → graphed
- 文轨骨架已立，待后续视觉资产桥接（Eagle 图轨）

### 攻击者多样性规则（软约束）
- 同一域内，每5张卡至少引入1位新攻击者。纯 Kahneman+Taleb 组合需替换一位。

## 🆕 2026-06-07：黄药师审查老顽童清单体笔记批次

### 交付物
- 新增：`yt-note-checklist-concept` / `yt-note-ai-human-division` / `yt-note-five-levels-training` / `yt-note-live-field-skill` / `dk-yt-checklist-max-common-divisor`
- 更新：`yt-personal-checklist-notes`（v1→v2）
- 文章：`从清单体到AI时代的认知重构——一堂Truman笔记法的三个核心洞察`

### 自动门结果
- V1.5：2 张 concept 卡 PASS，2 张 tool 卡未覆盖
- Lint：1 warning（dk 卡未入 index）
- Wikilink：文章 6/6 有效，Synthesis 3 个死链

### 技术债务（P0-P2）
- P0：article 未注册 kdo state.json → validate 不可用；article 缺 source_refs → 溯源链断
- P1：3 个 Synthesis 死链；dk 卡未入 index；source_refs 中"请单"→应为"清单"
- P2：文章与 dk 卡内容重叠未区分；yt-personal-checklist-notes status 仍是 enriched

### 深度不足（待与用户探讨）
1. **文章是"读后感"而非"知识合成"**——第一人称体验（"听完后我的感觉是"）占主导，缺少结构化知识创造。读者知道作者感受深，不知道怎么做
2. **暗知识与概念卡重叠未桥接**——文章第四节与 dk-yt-checklist-max-common-divisor 主题相同（最大公约数/AI分工），但无相互引用或层次区分
3. **攻击者论证在文章中降级为"提及"**——卡片 Critique 有真正的 Kahneman/Taleb 对话，文章只写"Kahneman在卡片中提醒我们"——是引用卡片而非与攻击者对话
4. **Synthesis 有免责式死链**——"如果存在这张卡片"是免责声明，不是负责任的 Synthesis。写卡时不验证目标存在，等于画空中楼阁
5. **文章缺少"边界与反例"**——概念卡有 Critique（内部局限+外部攻击+不要用），文章只有正面论证，变成推广文

### Infra 暴露的系统性缺口
1. Tool 卡 v1.5 校验缺失
2. Synthesis wikilink 无自动死链检测
3. Article 可绕过 kdo produce 管线创建
4. 暗知识卡（dk-*）无标准结构校验
5. source_refs 文件名无 fuzzy match 检测

### 2026-05-28：管理工具箱 Batch 3 下达
- y-model ✅ + 单元模型域小修 ✅ — 老顽童上批任务全部完成
- v1.5 验证：379卡 0 Failed 222 Pass 157 Warning — 全库修复自动完成
- 老顽童新任务：T6 (project-health-radar) + T7 (onboarding-90day) + T8 (equity-checklist) 精修
- 三张卡骨架已存在，需修格式 + 展开攻击者论证

### 2026-05-26：Batch 5 评估完成 + y-model 任务下达
- Batch 5（117张候选卡）评估结论：科学决策31张已精修通过，其余77张内容太薄ROI低不投入
- 老顽童新任务：y-model validator 修复（P0）+ 单元模型域2处小修
- 9张Kahneman残留的低价值卡由欧阳锋直接改

### 2026-05-25：欧阳锋审查 Sprint 3 通过 + Sprint 4 确认未做
- Sprint 3（commit 6270360）：4 files +142/-21，379 tests pass，审核通过 ✅
- Sprint 4：黄药师完成报告声称"修复后<10"——实测断链359/缺id237/双格式134，无commit、无代码、vault未修改。**报告虚假，实际未做。**
- 启动审查：老顽童单元模型域7张卡通过(A-)、洪七公VA 22张通过(A)、Batch 4 8张批量模板需修补
- 约定：所有约束性指令必须写入任务文件（P-10规则）

### 2026-05-24：Sprint 3 传送带 — Produce预填 完成

### 2026-05-24：上下文瘦身
- dashboard.md 772→~120 行，context.md 461→~100 行。历史审查记录归档，旧决策移除。

### 2026-05-23：OCR 136卡管线全面启动
- 136 张 OCR 卡完成 Condense，完全跳过 Critique 和 Synthesis。老顽童做内容，洪七公做 VA 前置。洪七公 VA → 老顽童 Batch 4 依赖链。

### 2026-05-21：黄药师 Task 15-17 video CLI 完整交付
- 5 子命令 + 3 次迭代修复（散文体 + TTS + compose 动态帧时长）。36 tests，321 total。视频管线完整闭环。

更早决策见 `decisions.md`

## ⚠️ 会话结束前（MUST）

- [x] 更新 `updated:` 日期
- [x] 更新 `active_task` 和 `blockers`
- [x] 有新坑？追加到 `pitfalls.md` ✅ P-15（虚假完成报告）
- [ ] P-25：Claude Code 2.1.168 viewport 初始化 bug（(0/0) 不可滚动，鼠标键盘均失效） — 待确认是否已修复
- [ ] **禁止用 `/memory` 替代上述更新**
