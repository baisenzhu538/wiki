# 架构决策

格式：日期 → 背景 → 决策 → 原因 → 否决的替代方案。

---

## 2026-05-16: DeepSeek V4 Pro 保留为 WSL 黄药师模型

**背景**：尝试将黄药师从 DeepSeek V4 切换到 Kimi 模型（月之暗面 `kimi-for-coding`）。API 本身可用（Anthropic Messages 协议兼容），Windows PowerShell 下测试通过。但在 WSL 中 `claude.exe` 始终读到 Windows 侧的 DeepSeek 环境变量，无法覆盖。

**决策**：保留 DeepSeek V4 Pro，放弃切换到 Kimi。

**原因**：WSL → Windows exe 的环境变量传递由 Windows 注册表和父进程主导，Linux 侧 `export` 被忽略。要让 Kimi 生效需改 Windows 注册表 + 注销重登 + `wsl --shutdown`，且 tmux session 继承链可能仍有缓存。维护成本高于收益。

**替代方案**：Kimi `kimi-for-coding` — API 测试通过，模型质量待评估。被否决原因：WSL 环境变量传递不可靠，不是模型本身的问题。

**后果**：黄药师固定用 DeepSeek V4 Pro。如果未来要切模型，优先考虑在 Windows 原生终端（而非 WSL）运行 Claude Code。

**⚠️ 2026-05-16 晚修正**：以上根因诊断为**误判**。真正原因不是 WSL 传不了 env var，而是 Claude Code 有独立的**全局设置文件**（`~/.claude/settings.json` 或 Windows 等价路径），其优先级高于环境变量。单独改 env var / 注册表均无效。黄药师后续通过直接改全局设置文件成功切换模型。切模型的正确路径：改全局设置 → 重启，而非逐项改环境变量。该教训已录入 `pitfalls.md` P-1。

---

## 2026-05-16: 创建 .agent/ 外挂大脑（本文件）

**背景**：黄药师 tmux session 被杀后完全失忆，不知道自己是 Builder、不知道 KDO、不知道 Sprint 12。每次恢复上下文消耗大量 token。

**决策**：在 vault 根目录创建 `.agent/` 三个文件（context.md / pitfalls.md / decisions.md），作为 agent 启动时的最小上下文入口。

**原因**：节省 ~80% 上下文恢复 token。三个文件跟着 git 走，换电脑不丢。任何 agent（不限于 Claude Code）都能读。

**替代方案**：Claude Code `/memory` — 被否决，因为锁在工具里、换工具/换电脑就丢。

**后果**：每次 session 结束需花 2 分钟更新 context.md。新 agent 启动时先读这三个文件。

---

## 2026-05-16: Sprint 12 Batch A 审查通过，启动 Batch B

**背景**：黄药师完成 25 张 `type: framework` 的 yt-* 卡 v1.5 回溯升级（外部攻击 + 不要用场景表 + Action Triggers）。欧阳锋按验收标准抽检 5/25（20%）。

**抽检样本**：`yt-model-agent-architecture`、`yt-model-five-step-canvas`、`yt-model-deep-review-iceberg`、`yt-model-product-excellence`、`yt-model-scientific-questioning-map`

**决策**：Batch A 通过。25/25 全部达到 v1.5 三要件标准。黄药师可启动 Batch B（85 张 `type: tool` 卡）。

**原因**：
- 外部攻击 0 straw man——全部引用真实学者（Klein, Edmondson, Argyris, Freire, Norman, Papanek 等）及其具体论证
- 不要用场景表全部含失效机制 + 替代方案，无"根据情况灵活运用"式废话
- Action Triggers 全部含三列完整（触发场景 + 第一动作 + 可验证成功指标）
- 原有 Claims / Constraints 内容未被修改
- `kdo lint` 3 errors / 591 warnings 全部为预存，非本次引入

**否决的替代方案**：无。审查无 blocking issue。

**后果**：
- Batch B（85 张 tool 卡）按 Sprint 12 工单执行，单次 ≤5 张，分 ~17 轮
- 黄药师在 `.agent/context.md` 更新当前任务为 Batch B
- 欧阳锋每域抽检 2 张（共 14 张，~16%）

---

## 2026-05-17：老顽童上岗——科学决策域编译

**背景**：黄药师 Sprint 12 Batch B 任务重（44 张 tool 卡剩余），老顽童空闲。用户在 `00_inbox/科学决策/` 放置了完整的一堂课程素材（6 个口述稿 ~16,000 行 + 35 张 PNG 框架图）。

**决策**：老顽童试工一个模块（AI 行动营 06 口述），产出 3 张卡。欧阳锋审查通过（B+→A-），正式分配科学决策域全部编译工作。

**原因**：
- 试工 3 张卡 0 稻草人、0 废话 trigger、0 空洞不要用场景——理解门禁首次就走通
- 风格偏学术（vs 黄药师偏实战），但质量标准达到
- 让老顽童独立负责一个域，黄药师继续 Batch B，双线互不阻塞

**架构修正**：老顽童首次提案 21 张卡（3 framework + 18 tool），被欧阳锋驳回。最终收缩到 9 张：2 framework（y-model 已有 + full-process 新增）+ 7 tool（habit-shift / width-method / depth-ladder / height-toolkit / consensus-iceberg / review / canvas+ai-partner 已有）。原则：一个可独立使用的工具一张卡，不是一张图一张卡。

**后果**：
- 科学决策域按 01→02→03→04→05 顺序推进，每模块 ≤2 张 tool 卡
- 图片必须全部 OCR，不能跳过——图中含有口述稿未系统展开的结构（共识四层冰山、ABCD 模型、全景图 5 阶段）
- 全部产出后出文章（创业者实操指南 + 人机协作决策方法论）

---

## 2026-05-17：KDO CLI 审计 + 备份策略

**背景**：用户询问 KDO CLI 是否需要优化迭代。另一台电脑的 claudian 从 GitHub 拉取分析声称"KDO CLI 不存在"，实际是只看了 wiki 仓库没找到 KDO 源码目录。

**审计结论**：
- KDO CLI 42 .py 文件 / 11,635 行 / 11 测试文件，核心管线（cards/lint/card-diff/review）正常
- pytest 未安装（一行命令修复）
- Graph RAG 代码完成但依赖未装（sentence_transformers / lightrag），索引接近空
- enrich 的 CJK TODO 检测用固定英文模板，中文页面系统性能失效（655 条 unenriched feedback）

**决策**：
1. KDO 源码备份到坚果云（单机灾备，删 .git/ + 排除 __pycache__），不用 GitHub
2. Graph RAG **战略保留**——为 wiki → MCP server 铺路，补齐依赖+重建索引+跑通验证
3. 小改进排队：pytest 安装（P0）→ lint --quiet → cards --missing 多值
4. CJK enrich 暂时不动——当前手工编译路线不需要，等管线策略确定后再决定修还是废弃

**否决的替代方案**：GitHub 备份——多台电脑的 wiki 仓库曾产生 git 冲突，坚果云单机同步更简单。templates.py 拆分之类重构——能跑不动。

---

## 2026-05-17：科学决策图片不可跳过

**背景**：老顽童声称"没有图片需要 OCR"。欧阳锋验证后发现文件夹有 35 张 PNG，全部未 OCR。关键框架图（共识四层冰山、ROI 全景图、X 型 Y 型对比、双三角模型）中的结构化信息在口述稿中未系统展开。

**决策**：科学决策域编译必须 OCR 全部图片。图片和口述稿互相佐证，跳过图片等于丢失一半信息。

**后果**：老顽童须先 OCR 全部 35 张图，读完六个口述稿，形成完整域架构后再逐模块写卡。不能只读一个口述稿就报方案。
