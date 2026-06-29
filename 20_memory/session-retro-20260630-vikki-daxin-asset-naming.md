---
id: session-retro-20260630-vikki-daxin-asset-naming
title: 2026-06-30 会话复盘：Vikki/大馨提炼、素材命名、AI 自动标签
type: retro
status: active
created_at: 2026-06-30
updated_at: 2026-06-30
reviewed_by: 欧阳锋
source_refs:
- 00_inbox/AI-study/0071Vikki战队-2群 · 认知精华提炼.md
- 00_inbox/AI-study/0017大馨战队 · 短视频内容拆解方法论精华提炼.md
- 30_wiki/tools/tool-月白-设计文件八要素命名法.md
related:
- [[kimi-consulting-skills-from-yai-20260629]]
- [[production-queue]]
---

# 2026-06-30 会话复盘

## 对话主题

1. Vikki-human-speech skill 角色归属确认
2. 大馨战队短视频拆解方法论提炼与任务编排
3. #29 羊奶渠道桥接卡终审通过与状态同步
4. 月白设计文件命名法回顾与素材命名方案
5. AI 自动识别图片内容并按 KDO 标准打标签的可行性分析

---

## 关键决策

### 决策 1：Vikki-human-speech skill 归属

- **洪七公**：不学（多模态/视觉角色）
- **老顽童**：学基础版，用于卡片/文章生产去 AI 味
- **段王爷**：学完整版，用于 ship 阶段渠道改写
- **已落地**：写入 `.agent/context.md`、`.agent/laowantong-context.md`、`.agent/duanwangye-context.md`

### 决策 2：Vikki + 大馨战队群聊认知有机融合

将两个来源的群聊精华从 3 个任务扩展为 5 个任务，形成完整内容生产增强包：

| 任务 | 内容 | 负责人 |
|:---|:---|:---|
| #30 | content-production-polish skill 2.0（Vikki 信息×情绪 + 大馨 6 维度/4 模板/5 人性开关） | 老顽童 |
| #31 | KDO 卡片质量标签体系（Vikki 五标签 + 大馨品牌三度） | 黄药师 |
| #32 | 开源知识使用边界概念卡（Vikki 蒸馏事件 + 大馨抄作业/AI 拆解边界） | 老顽童 |
| #33 | 大馨核心方法论卡片化（创始人 IP 三定位、品牌三度、内容经营 6 步闭环、短视频 6 维度拆解工具、案例卡） | 老顽童 |
| #34 | 社群知识生产失败模式库（Vikki 5 + 大馨 5 融合） | 老顽童 |

### 决策 3：素材命名采用「七要素法」

区别于月白面向设计成品的「八要素命名法」，素材作为「原料」采用七要素：

```
类型_项目_场景_来源_版权状态_技术参数_日期_序号.扩展名
```

关键原则：
- 版权状态必须标注
- 来源必须标注
- 不用 `v1/v2/最终版`，用 `001/002/003`

### 决策 4：AI 自动打标签采用「半自动工作流」

- AI 可自动识别：类型、场景、风格、技术参数、日期、序号
- 必须人工确认：项目、来源、版权状态
- 不是全自动，而是「AI 预填 + 人工决策」

---

## 产出文件

| 文件 | 类型 | 状态 |
|:---|:---|:---|
| `30_wiki/tools/tool-asset-file-naming-convention.md` | tool 卡 | draft，pre-submit PASS |
| `60_feedback/tasks/task_20260629_vikki-info-emotion-skill-upgrade.md` | 任务单 | queued，范围已扩展 |
| `60_feedback/tasks/task_20260629_vikki-five-tag-quality-labels.md` | 任务单 | queued，范围已扩展 |
| `60_feedback/tasks/task_20260629_vikki-open-source-knowledge-boundary.md` | 任务单 | queued，范围已扩展 |
| `60_feedback/tasks/task_20260630_daxin-methodology-cards-production.md` | 任务单 | queued，新增 |
| `60_feedback/tasks/task_20260630_community-knowledge-failure-modes.md` | 任务单 | queued，新增 |
| `70_product/tasks/production-queue.md` | 生产队列 | 已更新至 #34 |
| `.agent/context.md` | 共享上下文 | 已更新 blocker 记录 |

---

## 验证结果

- 所有新建/修改任务单 `kdo pre-submit`：PASS
- 素材命名工具卡 `kdo pre-submit`：PASS
- `.agent/context.md` `kdo pre-submit`：PASS

---

## 下一步

### 高优先级（按队列）

1. **#28 lint 内容债按 domain 分批清理**
   - 当前 claimed-kimi 进行中
   - 全量 lint WARNING 基线 2656
   - 需继续处理 body 过短、L2 Critique 等

2. **#30-34 Vikki/大馨 提炼任务**
   - 等待老顽童/黄药师按队列领取
   - #31 由黄药师负责 schema 设计

### 中优先级

3. **AI 素材自动打标签试点**
   - 先定义素材 taxonomy（受控词表）
   - 选择一个项目（如「润之美 618」）试点
   - 评估用现有洪七公 VLM pipeline 还是 API

4. **月白素材命名工具卡终审**
   - 当前 status: draft
   - 需欧阳锋审查

---

## 经验教训

1. **群聊精华需要「双源融合」**：单独看 Vikki 或大馨都不够完整，Vikki 提供「讲人话」心法，大馨提供「短视频脚本」骨架，两者互补。

2. **命名规范要分阶段**：设计成品和素材是不同阶段的资产，不能共用同一套命名法。月白的八要素针对成品，需要为素材单独建立七要素法。

3. **AI 自动化的边界要清晰**：AI 能识别内容，但无法判断业务上下文（项目、版权、来源）。自动化方案必须预留人工确认环节。

4. **任务编排要「有机」**：新增任务时考虑依赖和避免重复（如 #30 已覆盖短视频脚本模板，#33 中的对应工具卡标记为可选）。

---

## 待用户确认/决策

1. 是否立即启动 AI 素材自动打标签试点？如果启动，选哪个项目试点？
2. `tool-asset-file-naming-convention.md` 是否需要欧阳锋立即终审，还是等 #31 标签体系确定后再统一审？
3. #30-34 五个任务是否需要调整优先级或负责人？
