---
id: task_20260703_laowantong-yitang-Y-model-stub-completion
title: "#51 收尾：实事求是 / 解放思想 framework 卡补全"
type: task
status: queued
priority: P1
assignee: 老顽童(Kimi)
reviewer: 欧阳锋
created_at: 2026-07-03
updated_at: 2026-07-03
expected_cards: 2
dependencies:
  - "task_20260703_laowantong-yitang-Y-model-foundation-production reviewed"
source_refs:
  - 00_inbox/实事求是/_processed/实事求是_整合笔记.md
  - 00_inbox/实事求是/_processed/vlm_summary.json
  - 00_inbox/解放思想/_processed/解放思想_整合笔记.md
  - 00_inbox/解放思想/_processed/CASE_CANDIDATES.md
related:
  - yt-decision-y-model
  - framework-yitang-shishi-qiushi
  - framework-yitang-jiefang-sixiang
  - yt-entrepreneur-truth-seeking
  - yt-model-liberate-thinking-layers
---

# #51 收尾：实事求是 / 解放思想 framework 卡补全

> 任务来源：`#51` 终审时因素材未到位保留 2 个 framework stub；现在素材已处理就位，需补全后重新提交终审。

---

## 一、背景

`#51` 一堂底层逻辑域任务终审结论为：5 张新卡完整交付 + 2 张 framework 卡建 stub + 3 张旧卡迁移。

但终审后，实事求是、解放思想两门课的素材已经处理并就位：

- `00_inbox/实事求是/_processed/实事求是_整合笔记.md`
- `00_inbox/实事求是/_processed/vlm_summary.json`
- `00_inbox/解放思想/_processed/解放思想_整合笔记.md`
- `00_inbox/解放思想/_processed/CASE_CANDIDATES.md`（148 条案例候选）

因此 2 个 stub 现在可以补全。

---

## 二、需要补全的 2 张卡

### Card 1: `framework-yitang-shishi-qiushi`

**类型**：framework  
**主域**：epistemic-foundations / yitang / decision-science  
**素材来源**：`实事求是_整合笔记.md` + `vlm_summary.json`

**必须包含的 section**：
1. 一句话：实事求是 = 把「我希望是真的」和「事实是什么」分开。
2. 在 Y模型中的位置：从「相信因果规律」生长出的第一层能力。
3. 核心动作：定量描述、规律边界识别、红队蓝队、魔鬼代言人、反面证据搜索。
4. 常见自欺信号：确认偏误、愿望思维、叙事美化、动机性推理、事后合理化。
5. 验证成本阶梯：常识 → 情报 → 实验 → 全量投入。
6. AI 反幻觉映射：如何把实事求是嵌入 AI 输出校验。
7. Agent Y模型三段映射：理论来源 / 事实输入 / 知行合一 / 幻觉风险 / fallback。
8. 科学类比使用说明：如何把这个框架迁移到其它决策场景。
9. Checklist ≥8 项。
10. Anti-patterns ≥4 个。
11. Critique ≥3 个外部反对者 + ≥2 个内部局限。
12. Related ≥5 条，含跨域。

### Card 2: `framework-yitang-jiefang-sixiang`

**类型**：framework  
**主域**：epistemic-foundations / yitang / decision-science  
**素材来源**：`解放思想_整合笔记.md` + `CASE_CANDIDATES.md`

**必须包含的 section**：
1. 一句话：解放思想 = 不被行业常识、路径依赖、既有框架绑架，用底层规律指导上层创新。
2. 在 Y模型中的位置：从「实事求是」生长出的第二层能力。
3. 六层认知模型（整合旧卡 `yt-model-liberate-thinking-layers` 可用部分）。
4. 隐含假设挖掘方法：反常识提问、跨界类比、极端场景假设、反事实推理。
5. 与渠道探索、需求冰山、泛产品设计的桥接。
6. AI 反幻觉映射：如何让 AI 从 L1-L2 模式匹配上升到 L3-L5 第一性原理推理。
7. Agent Y模型三段映射。
8. 科学类比使用说明。
9. Checklist ≥8 项。
10. Anti-patterns ≥4 个。
11. Critique ≥3 个外部反对者 + ≥2 个内部局限。
12. Related ≥5 条，含跨域。
13. **案例使用原则**：从 `CASE_CANDIDATES.md` 中选取 2-3 个高价值候选，嵌入作为例证，不轻易丢弃。

---

## 三、旧卡迁移确认

补全后确认以下 2 张旧卡的迁移提示和 related 指向正确：

- `yt-entrepreneur-truth-seeking` → 指向 `framework-yitang-shishi-qiushi`
- `yt-model-liberate-thinking-layers` → 指向 `framework-yitang-jiefang-sixiang`

（`yt-entrepreneur-scientific-method` 已在 #51 中指向 `yt-decision-y-model`，无需本次处理。）

---

## 四、验收标准

- [ ] `framework-yitang-shishi-qiushi` 完整补全，`kdo pre-submit` PASS，无新增 ERROR。
- [ ] `framework-yitang-jiefang-sixiang` 完整补全，`kdo pre-submit` PASS，无新增 ERROR。
- [ ] 2 张卡均包含 AI 反幻觉映射、Agent Y模型三段映射、科学类比使用说明。
- [ ] `framework-yitang-jiefang-sixiang` 至少嵌入 2 个来自 `CASE_CANDIDATES.md` 的案例。
- [ ] 2 张旧卡迁移提示和 related 正确。
- [ ] `#51` 任务单状态可随之更新为 fully reviewed 或重新提交欧阳锋终审。
- [ ] 欧阳锋终审通过。

---

## 五、队列位置

- **入队编号**：`#56`
- **状态**：`queued`
- **预计工时**：老顽童 1-2 天 + 欧阳锋终审 0.5 天

---

*王语嫣 2026-07-03*
