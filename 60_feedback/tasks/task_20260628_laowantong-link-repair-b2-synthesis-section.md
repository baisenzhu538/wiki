---
id: task_20260628_laowantong-link-repair-b2-synthesis-section
type: task
status: queued
assignee: 老顽童
priority: P1
created_at: 2026-06-28
updated_at: 2026-06-28
reviewer: 欧阳锋
source_refs:
- 70_product/tasks/production-queue.md
- 60_feedback/tasks/task_20260628_wangyuyan-next-phase-orchestration.md
---

# B2：Synthesis section 死链/占位清理

## 目标

清理正文 `## Synthesis`（或等效总结 section）中的 `[[src_unknown]]` 死链和纯文本 `src_unknown` 占位，确保每张非 draft 卡片的 Synthesis section 出链 ≥ 2。

## 范围

- 正文中 Synthesis section 含 `[[src_unknown]]` 或纯文本 `src_unknown` 的卡片
- 预计文件数：100-200 张
- 来源清单：通过正文扫描生成

## 规则

1. **读 Synthesis section 上下文**：根据本卡主题，从正文或相关卡中推断应链接到的 concept/framework/dk。
2. **优先使用真实 wikilink**：如 `[[concept-xxx]]`、`[[framework-yyy]]`、`[[dk-zzz]]`。
3. **无法推断的**：替换为 `[[pending_unknown]]` 或纯文本 `待补充链接`，不允许保留 `[[src_unknown]]` 死链。
4. **每张卡 Synthesis 出链 ≥ 2**：若正文素材不足，至少放 2 个 `[[pending_unknown]]` 占位。
5. 不编造与卡片主题无关的链接。

## 执行方式

- **必须人工审核**，不允许自动写入：
  - 老顽童逐张阅读 Synthesis section 和正文
  - 手动填入或替换链接
  - 每张卡改完后跑 `kdo pre-submit -f <路径>`
- 批量提交前跑 `kdo pre-submit -f <清单> --expect-changes <数量>`。

## 验证

- `kdo lint` 中 Synthesis section 相关死链/占位 ERROR 清零
- 抽检 20 张卡，确认 Synthesis 出链 ≥ 2 且与主题相关
- `kdo pre-submit` 全量通过
