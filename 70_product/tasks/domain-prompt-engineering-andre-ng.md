---
id: domain-prompt-engineering-andre-ng
title: "提示词工程域：吴恩达课程消化 + 人机协作技能内化"
status: active
priority: P0
assigned_to: 黄药师
architect: 欧阳锋
domain: master
created: 2026-05-13
target: 2026-05-15
---

## ⚠️ 前置任务

完成 [[calibration-understanding-gate-motivation-peakend]]（已完成 ✅）和 [[domain-xiang-jiang-deep-digestion]]（已完成 ✅）。理解门禁标准沿用。

---

## 背景

新材料入仓：

| 文件 | 类型 | 内容 |
|------|------|------|
| `00_inbox/一堂-拆书会-吴恩达提示词课程.txt` | 口述稿 | 一堂拆书会对吴恩达"给所有人的AI提示词课程"的深度笔记+解读，~2700行 |
| `00_inbox/拆书会第202期：《给所有人的人工智能提示词课程》 .pdf` | PDF | 同内容的拆书会课件（1.4MB），需转换 |

**这不仅是"加几张卡"。** 提示词工程是人机协作的操作系统层知识——它影响本 vault 中所有 agent 和人类用户的协作方式。产出应包含：(1) 知识卡片（wiki 层）；(2) 可执行技能（capabilities 层）。

---

## 一、欧阳锋初步消化

### 课程核心判断

吴恩达课程 + 一堂拆书会的核心贡献不是"提示词技巧列表"，而是一个**范式转换**：

| 旧范式 | 新范式 |
|--------|--------|
| 提示词是咒语，需要学习模板 | 提示词是管理AI合伙人的对话，需要迭代 |
| AI是答案生成机器 | AI是被校准、追问、约束、反驳的智能伙伴 |
| 好的提示词是一次性写出来的 | 好的提示词在交互中自然涌现 |
| AI帮我们省事 | AI帮我们拔高上限 |
| 用AI写作从正文开始 | 用AI写作从大纲开始（大纲是杠杆） |

### 六个核心概念（初步判断，供架构讨论）

1. **迭代式提示词**（第一性原理）：提示词的核心不是一次写对，是连续迭代——每轮反馈就是新的上下文
2. **反谄媚机制**：AI天然倾向于顺从用户。去掉所有积极形容词、先问缺点再问优点、引入反对者角色
3. **上下文工程**：刀刃在提示词里——充分不等于越多越好，独特答案只能来自独特约束
4. **AI头脑风暴**：使用频率仅 3.9% 但价值最高的场景——生成选项而非唯一答案，先加法后减法
5. **AI写作工作流**：大纲→要点→全文（自上而下构建），润色则反过来（逐句逐段，自下而上）
6. **守脑如玉**：AI越来越聪明时，人必须保持大脑锋利。AI的价值是拉升上限，不是填平下限

### 与本 vault 的交叉点

- 讲香十指模型中的"武器库"概念在这里再次出现：吴恩达课程本身就是一套"提示词武器库"
- IPO 学习模型中，提示词能力属于"输出"环节——如何高质量与AI协作输出
- 科学表达（火箭模型）中，三级火箭"情感共鸣"的边界问题与AI反谄媚同构
- 泛产品方法论中的"约束条件产生洞察"与提示词中"独特约束产生独特答案"完全同构

---

## 二、执行计划

### Phase 0：素材准备（立即执行）

**0a. PDF 转文本**
```bash
# PDF → Markdown（用 Python 提取）
python3 -c "
from pdfminer.high_level import extract_text
text = extract_text('拆书会第202期：《给所有人的人工智能提示词课程》 .pdf')
with open('拆书会第202期-提示词课程.md', 'w') as f:
    f.write(text)
"
```
产出：`00_inbox/拆书会第202期-提示词课程.md`

**0b. 文本素材处理**
- `一堂-拆书会-吴恩达提示词课程.txt` → 拷贝为 `.md`（C-3 规则）
- 对比 txt 和 PDF 提取内容，标记差异段落

**0c. 寻找原课程链接**
- 搜索 B 站 "吴恩达 提示词" 或 "Andrew Ng prompt engineering"
- 搜索课程英文原名（Generative AI for Everyone / ChatGPT Prompt Engineering for Developers）
- 如找到链接，归档到 `00_inbox/links/`

### Phase 1：KDO 管线 + 架构决策

**1a. kdo ingest**
```bash
kdo ingest --kind source "00_inbox/一堂-拆书会-吴恩达提示词课程.md"
```

**1b. 架构方案（需欧阳锋确认后再执行）**

建议卡片拆分：

```
yt-model-prompt-engineering.md                   ← framework：提示词工程总框架
  ├── yt-tool-iterative-prompting.md             ← tool：迭代式提示词工作流
  ├── yt-tool-ai-anti-flattery.md                ← tool：反谄媚机制（去正向形容词/角色扮演/分段评分）
  ├── yt-tool-ai-brainstorming-workflow.md       ← tool：AI头脑风暴工作流
  ├── yt-tool-ai-writing-workflow.md             ← tool：AI写作工作流（大纲→要点→全文）
  ├── yt-concept-ai-guard-brain.md               ← concept：守脑如玉原则
  └── yt-concept-context-engineering.md          ← concept：上下文工程（充分≠越多越好）
```

关联域图边更新：
| 卡片 | 操作 |
|------|------|
| `yt-model-ipo-learning-strategy` | `related` 新增提示词 framework |
| `yt-personal-scientific-expression` | `related` 新增提示词 framework（表达与提示词的输出同构） |
| `yt-concept-weapon-arsenal` | `related` 新增提示词 framework（吴恩达课程是提示词武器库） |
| `yt-model-personal-pitch-toolkit` | `related` 新增提示词 framework（讲香与提示词共享迭代+约束方法论） |

**1c. 建卡**

按理解门禁标准执行。每张 tool 卡 Constraints 至少 2 条。

---

### Phase 2：技能内化（产出 capabilities）

提示词工程不只是"知识"，更是**可执行的操作系统**。需产出两个能力资产：

**2a. Skill：`ai-deep-work`（AI 深度工作法）**

位置：`40_outputs/capabilities/skills/ai-deep-work/SKILL.md`

内容：
- 触发条件：当 agent 或用户需要进行复杂推理、多轮迭代思考时
- 输入：一个未完全定义的复杂问题 + 用户已有的上下文
- 工作流：
  1. 先给背景和约束（上下文工程）
  2. 生成多个选项而非一个答案（头脑风暴）
  3. 追问依据、暴露假设、寻求反驳（反谄媚）
  4. 分项判断、设定标准（结构化评分）
  5. 形成实验/方案（落地闭环）
- 失败模式：一次性提问就接受答案、忘记反谄媚导致AI只说好话

**2b. Playbook：`human-ai-collaboration-playbook`（人机协作操作手册）**

位置：`40_outputs/capabilities/workflows/human-ai-collaboration-playbook.md`

内容：
- 角色定义：AI是合伙人不是工具（已有仓库角色体系的重校准）
- 关键原则：守脑如玉、拔上限非填下限、迭代优于模板
- 场景速查：
  - 写作 → 大纲→要点→全文工作流
  - 判断 → 多模型交叉验证 + 分项评分
  - 学习 → 手写笔记→口述→AI整理→直播分享（四遍学习法）
  - 决策 → AI辅助判断但绝不依赖（高风险决策需人类专家交叉验证）

---

## Phase 3：质量门禁

### 格式门禁
- [ ] `grep '"00_inbox' 30_wiki/concepts/yt-*.md` → 空
- [ ] 所有新卡 `source_refs` 指向 `10_raw/`
- [ ] 所有新卡 `related` 非空
- [ ] `kdo lint` → 0 errors

### 理解门禁（沿用讲香域标准）
- [ ] 欧阳锋随机抽检 2 张新卡，读 Constraints 节
- [ ] 反例具体性 / 案例筛选 / 跨域连接三项信号绿灯
- [ ] 追问：至少 1 个反例能解释"为什么是这个工具的边界"

### 技能门禁
- [ ] `ai-deep-work` SKILL.md 包含：触发条件、输入输出、工作流步骤、失败模式
- [ ] `human-ai-collaboration-playbook` 包含：角色定义、关键原则、场景速查（≥4 个场景）

---

## 完成信号

- 提示词域：1 framework + 4 tool + 2 concept 卡，全部通过格式+理解门禁
- 关联域 4 张卡片图边已更新
- 2 个 capability 资产产出（skill + playbook），通过技能门禁
- 原文素材全部归档 `10_raw/sources/`
- 欧阳锋终审通过
