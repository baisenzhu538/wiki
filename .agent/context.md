---
updated: 2026-06-20
active_branch: main
active_task: "老顽童批量工单：全库待办一次性打包（5波），当前第1波门禁清理"
blockers:
  - "第4波新域建设需前置审批：调研方法论域待欧阳锋批准，master域7张卡待确认分配给老顽童"
next_session_hint: "老顽童按 laowantong-batch-2026-06-20.md 执行；每波完成跑门禁并写小结；第4波待欧阳锋审批后启动"
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
| 欧阳锋（Architect） | Obsidian Claudian 插件 | 协调/审查/拍板 |
| 黄药师（Builder） | Windows 终端（PowerShell） | KDO CLI 开发 |
| 王语嫣（Consultant） | Hermes agent → 飞书 | 诊断咨询/反馈 |
| 老顽童（Producer） | **WSL tmux claude（主力）** / Hermes 备用 | 卡片/文章量产 |
| 洪七公（Multimodal） | Hermes agent → 飞书 | 视觉/设计/prompt |
| 段王爷（Publisher） | Hermes agent → 飞书 | 发布/反馈/版本 |

> 角色专属 context 见 `.agent/ouyangfeng-context.md`、`.agent/huangyaoshi-context.md`、`.agent/wangyuyan-context.md`、`.agent/laowantong-context.md`、`.agent/hongqigong-context.md`、`.agent/duanwangye-context.md`。

## 关键路径

| 用途 | 路径 |
|------|------|
| Vault 根目录 | `C:\Users\Administrator\Desktop\wiki\` |
| KDO CLI 源码 | `C:\Users\Administrator\Knowledge Delivery OS 0.0.1\kdo\` |

## 模型与环境

- **模型**：DeepSeek V4 Pro（直连 `api.deepseek.com/anthropic`）
- **飞书 WebSocket**：cc-connect 和 Hermes 均出现 keepalive ping timeout。重启即修复。P-6 已记录。
- **切模型**：涉及五层配置（`.bashrc` / 注册表 / systemd drop-in / `cc-connect config.toml` / session 缓存）。详见 `pitfalls.md`

## 当前共享状态

### 各角色当前任务
- **黄药师**：KF-020+021全修 + S4-1 aliases + kdo_lint(2344→85) + 决策域研究(2卡A级)
- **老顽童**：30张精修A- + source_refs残留清理 + index/log元页面精简(760→2) + 全域案例回溯
- **王语嫣**：六阶段全库审计闭环 + 质量门禁脚本 + 协作修复计划 + 复合卡回填完工
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
3. **攻击者论证在文章中降级为"提及"**——卡片 Critique 有真正的 Kahneman/Taleb 对话，文章只写"Kahneman在[[卡片]]中提醒我们"——是引用卡片而非与攻击者对话
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
