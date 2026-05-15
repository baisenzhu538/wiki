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
