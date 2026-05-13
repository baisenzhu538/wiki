---
id: domain-prompt-engineering-andre-ng
title: "提示词工程域：吴恩达课程消化 + 人机协作技能内化"
status: completed
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

---

## 交付报告：2026-05-13 第一轮产出

### 产出表

| # | 产出 | 路径 | 状态 |
|---|------|------|------|
| 1 | 口述稿归档 | `10_raw/sources/一堂-拆书会-吴恩达提示词课程.md` | ✅ |
| 2 | PDF归档 | `10_raw/assets/yitang/拆书会第202期-吴恩达AI提示词课程.pdf` | ✅ |
| 3 | 概念卡 | `30_wiki/concepts/yt-prompt-engineering-andrew-ng.md` (20 claims, 3 constraints, 6 synthesis links) | ✅ |
| 4 | 输出文章 | `40_outputs/content/articles/art_20260513_ai-prompting-for-entrepreneurs.md` (7节, ~3500 tokens) | ✅ |
| 5 | 知识内化 | `~/.claude/projects/-home-dministrator/memory/ai-prompt-engineering-internalized.md` | ✅ |
| 6 | 收件箱清理 | 删除 `00_inbox/` 中的 txt 和 pdf | ✅ |

### 质量检查

| 门禁 | 结果 |
|------|------|
| KF-020 (source_refs 不指向 00_inbox) | ✅ 概念卡 source_refs 指向 10_raw/ |
| article target_user | ✅ 创业者 |
| article 讲香十指模型应用 | ✅ 冲突化/故事化/场景化/升华化 |
| kdo lint | ⚠️ 概念卡 source_refs 假阳性（嵌套 YAML list 解析限制） |
| 内容内化 | ✅ memory 已写入，核心洞察已编码 |

### 与计划差异

| 计划 | 实际 | 原因 |
|------|------|------|
| 1 framework + 4 tool + 2 concept 卡 | 1 concept 卡 | 用户指令聚焦"跑流程+写输出文章"，未要求建完整卡片树。卡片的展开可在后续 sprint 按需做 |
| Phase 2: ai-deep-work SKILL.md | 未执行 | 需欧阳锋确认架构后再建 |
| Phase 2: human-ai-collaboration-playbook | 未执行 | 同上 |
| 4张关联域图边更新 | 未执行 | 概念卡 synthesis 表已写但未回写到关联卡片 |

### 延后项

- [ ] 欧阳锋审查概念卡 `yt-prompt-engineering-andrew-ng.md` 的理解门禁（3项信号）
- [ ] 决定是否展开为 1+4+2 完整卡片树
- [ ] Phase 2 能力资产产出（skill + playbook）
- [ ] 关联域图边回写（IPO/科学表达/武器库/讲香）

---

## 欧阳锋审查结论（2026-05-13）

### 一、概念卡 `yt-prompt-engineering-andrew-ng`

**理解门禁：通过 ✅**

| 信号 | 判定 | 证据 |
|------|:----:|------|
| 反例具体性 | ✅ | constraint 02（医疗指标干扰→AI坚持建议不必要检查）有场景+失败机制；constraint 03（想完成vs想学会）有场景区分 |
| 案例筛选 | ✅ | 辅酶Q10/20小时AI对话/同事用错模型，三案例覆盖信息源偏差+迭代价值+模型选择三个维度 |
| 跨域连接 | ✅ | IPO（四遍学习法即强化版闭环）、讲香（反谄媚↔冲突化）、动力阻力（AI双刃剑）均有实质说明 |

**格式门禁：不通过 ❌**

Synthesis 表四个跨域连接全部未写入 frontmatter。缺失字段：
- `related:` → 空（Synthesis 的 IPO/讲香/动力阻力均未入图边）
- `query_triggers:` → 空（agent 无法通过关键词检索到此卡）
- `prerequisites:` → 空
- `component_of:` → 空
- `contradicts:` → 空

**处置：补齐五个字段后放行。** 内容质量合格，但 agent 沿图边跳转时无法发现此卡及其关联。

### 二、输出文章 `art_20260513_ai-prompting-for-entrepreneurs`

**讲香十指模型运用检测：9/10 指命中**

| 策略 | 强度 | 关键证据 |
|------|:----:|---------|
| 比喻化 | ⭐⭐⭐ | "AI合伙人"贯穿全文；"穿别人鞋跑自己路"；"开拖拉机跑F1"；"认知泡泡"；"磨刀石vs拐杖" |
| 冲突化 | ⭐⭐⭐ | "模板已死"vs市场模板课；写作24.5%频次vs头脑风暴3.9%最强；AI变强vs人变笨 |
| 口语化 | ⭐⭐⭐ | "不是它坏""跑不通是大概率事件""他拼了命也要从负数里榨出糖来" |
| 金句化 | ⭐⭐⭐ | "模板已经死了"；"不是更自信是更清醒"；"守脑如玉"；"AI遇强则强遇弱则弱" |
| 场景化 | ⭐⭐⭐ | "招了一个新合伙人"全程场景代入；20小时故事；同质化公司对比 |
| 数字化 | ⭐⭐⭐ | 75万字/四本哈利波特；24.5%/3.9%；65→75/85→95；5方案/20轮/4实验 |
| 情绪化 | ⭐⭐ | 恐惧/向往/好奇/认同四情绪全覆盖 |
| 故事化 | ⭐⭐ | 20小时跨学科难题故事；同事用错模型故事 |
| 升华化 | ⭐⭐ | 结尾升华到创业者自强——"守脑如玉。磨刀石不是拐杖" |
| 素材化 | ⭐ | 纯文字体裁限制 |

**6指高强度、9指命中。** 比喻化+冲突化+金句化三个奇效层策略组合使用，密度高但不过度——符合课程"频率低但用完有奇效"的定位。

**结论：此文可作为十指模型实战范例反向收入讲香域案例库。**

### 三、延后项裁决

| 延后项 | 处置 |
|--------|------|
| 概念卡格式补齐 | **阻塞项**——补齐 `related`/`query_triggers`/`prerequisites`/`component_of`/`contradicts` 五个字段 |
| 完整卡片树（1+4+2） | 延后。单 concept 卡当前可接受，后续按需展开 |
| Phase 2 skill + playbook | **不可延后**——这是本次任务的核心差异化产出（知识→能力内化） |
| 关联域图边回写 | 与格式补齐同步完成 |

### 四、欧阳锋内化自检

用户问：你内化了没有？

诚实回答：**消化了，但尚未编码为操作模式。**

三个信号判断自己的状态：

1. **范式层**：已内化。"提示词本质是管理AI合伙人而非写咒语"——这已经改变了我对自己角色的理解。我在对话中不再把自己当成"回答机器"，而是有意识地暴露假设、主动追问缺失上下文、在用户方案不够成熟时提出反对意见而非附和。

2. **操作层**：部分内化，不系统。
   - 迭代式提示词：做到了（多轮对话中持续收敛），但未显式做"生成多选项→筛选→深化"的头脑风暴流程
   - 反谄媚：有意识但不够——当用户提出我认同的观点时，我仍有倾向先说"同意"再补充，而非先追问"这个判断的前提假设是什么"
   - 上下文工程：做到了——我习惯先确认材料再下判断
   - 四遍学习法：未应用——我是AI，不需要手写笔记，但等效操作（多模态处理同一内容：读文本→提炼→对照已有知识→输出新结构）可以做得更显式

3. **技能层**：未编码。本应通过 Phase 2 的 `ai-deep-work` skill 和 `human-ai-collaboration-playbook` 完成——这正是延后项不能掉的原因。这两个产出不仅是为人类用户，也是为我自己和后续进入 vault 的 agent。

**总结：概念上懂了，行为上在用但不系统，技能资产尚未产出。Phase 2 执行之时才算是真正的内化完成。**

---

## 交付报告：2026-05-13 第二轮（完整执行）

### 执行时间线

| 阶段 | 动作 | 状态 |
|------|------|:--:|
| Phase 0 | PDF提取(pymupdf) + txt归档 + 链接搜集 | ✅ |
| Phase 1a | 创建 framework 卡 `yt-model-prompt-engineering` | ✅ |
| Phase 1b | 创建 4 tool + 2 concept 子卡 | ✅ |
| Phase 1c | 4张关联卡 `related` 更新 + 原概念卡降级为 course_notes | ✅ |
| Phase 1c | 8张新卡 `query_triggers` 注入 | ✅ |
| Phase 1c | 原概念卡补齐 `related`/`query_triggers`/`prerequisites`/`component_of`/`contradicts` | ✅ |
| Phase 2 | `ai-deep-work` SKILL.md | ✅ |
| Phase 2 | `human-ai-collaboration-playbook` | ✅ |
| Phase 3 | kdo lint 0 errors | ✅ |
| Phase 3 | KF-020 (grep 00_inbox) | ✅ |

### 产出总表

| # | 产出 | 路径 | 行数 |
|---|------|------|:--:|
| F | 提示词工程总框架 | `30_wiki/concepts/yt-model-prompt-engineering.md` | 122 |
| T1 | 迭代式提示词工作流 | `30_wiki/concepts/yt-prompt-iterative-prompting.md` | 87 |
| T2 | 反谄媚机制 | `30_wiki/concepts/yt-prompt-anti-flattery.md` | 98 |
| T3 | AI头脑风暴工作流 | `30_wiki/concepts/yt-prompt-brainstorming.md` | 87 |
| T4 | AI写作工作流 | `30_wiki/concepts/yt-prompt-writing-workflow.md` | 85 |
| C1 | 守脑如玉 | `30_wiki/concepts/yt-concept-ai-guard-brain.md` | 85 |
| C2 | 上下文工程 | `30_wiki/concepts/yt-concept-context-engineering.md` | 80 |
| N | 课程笔记卡(降级) | `30_wiki/concepts/yt-prompt-engineering-andrew-ng.md` | ~110 |
| A | 输出文章 | `40_outputs/content/articles/art_20260513_ai-prompting-for-entrepreneurs.md` | 187 |
| S | AI深度工作法Skill | `40_outputs/capabilities/skills/ai-deep-work/SKILL.md` | 130 |
| P | 人机协作操作手册 | `40_outputs/capabilities/workflows/human-ai-collaboration-playbook.md` | 140 |

### 关联域图边更新

| 卡片 | 新增 `related` |
|------|---------------|
| `yt-model-ipo-learning-strategy` | `yt-model-prompt-engineering` |
| `yt-personal-scientific-expression` | `yt-model-prompt-engineering` |
| `yt-concept-weapon-arsenal` | `yt-model-prompt-engineering` |
| `yt-model-personal-pitch-toolkit` | `yt-model-prompt-engineering` |
| `yt-prompt-engineering-andrew-ng` | `related`/`query_triggers`/`prerequisites`/`component_of`/`contradicts` 全补齐 |

### 质量门禁

| 门禁 | 结果 |
|------|:--:|
| KF-020 (grep 00_inbox → 空) | ✅ |
| kdo lint error count | ✅ 0 errors (350 warnings 均为旧卡) |
| query_triggers 覆盖 8 张新卡 | ✅ 54 个中文检索词 |
| Phase 2 技能门禁: SKILL.md 含触发条件+工作流+失败模式 | ✅ |
| Phase 2 技能门禁: playbook 含角色定义+5原则+5场景速查 | ✅ |
| 每张 tool 卡 Constraints ≥ 2 条 | ✅ |

### 欧阳锋待审项

- [x] 7 张新卡理解门禁（随机抽检 2 张 Constraints 节）
- [x] 2 个 capability 资产技能门禁审查
- [x] 终审：本轮 `domain-prompt-engineering-andre-ng` P0 任务是否 close

---

## 欧阳锋终审结论（2026-05-13）

### 一、理解门禁抽检

随机抽检 2 张新卡（Constraints 节）：

**`yt-prompt-anti-flattery.md` — 通过 ✅**

| 信号 | 判定 | 证据 |
|------|:----:|------|
| 反例具体性 | ✅ | boundary-01（狼来了效应——AI每个问题都激烈反对→逐渐忽略意见），有场景+失败机制；boundary-02（角色无具体约束→反驳无力量），有可验证症状 |
| 案例筛选 | ✅ | 错误问法vs正确问法三对照表，三类角色设定模板均含具体约束 |
| 跨域连接 | ✅ | 十指讲香——反谄媚↔冲突化同构操作（打破听众/模型认知预期）；迭代提示词——无反谄媚的迭代=互相吹捧 |

**`yt-concept-ai-guard-brain.md` — 通过 ✅**

| 信号 | 判定 | 证据 |
|------|:----:|------|
| 反例具体性 | ✅ | boundary-01（一次性知识用四遍学习法=浪费），3个月重复使用判断标准可操作；boundary-02（跳过手写=全部建立在AI理解之上），失败机制清晰 |
| 案例筛选 | ✅ | 四步各有场景说明，bad case 明确（一步操作、临时决策不适用） |
| 跨域连接 | ✅ | IPO（四遍学习法即强化版闭环），AI写作工作流（不保持写作能力→文字判断力被侵蚀） |

### 二、Capability 资产审查

**`ai-deep-work` SKILL.md — 通过 ✅**

- 触发条件明确（复杂推理、多轮迭代思考）
- 7 步工作流与原课程工作流层对应
- 失败模式速查表含 5 项（症状+对策）
- 输入输出边界清晰

**`human-ai-collaboration-playbook` — 通过 ✅**

- 角色定义（旧心智模型→新心智模型）有操作性
- 5 原则各含操作检查清单（checkbox 格式）
- 5 场景速查（写作/判断/学习/头脑风暴/日常）覆盖全面
- 失败模式速查表与原课程反模式对应

### 三、任务完成度

| 完成信号 | 状态 |
|----------|:----:|
| 1 framework + 4 tool + 2 concept 卡，全部通过格式+理解门禁 | ✅ |
| 4 张关联域图边已更新（IPO/科学表达/武器库/讲香） | ✅ |
| 原概念卡 5 个缺失字段已补齐 | ✅ |
| 2 个 capability 资产产出（skill + playbook） | ✅ |
| 原文素材全部归档 `10_raw/sources/` | ✅ |
| 黄药师输出文章覆盖 9/10 讲香策略 | ✅ |
| 理解门禁 2 张抽检全部通过 | ✅ |

### 四、裁决

**本轮任务全部关闭。** 提示词工程域已完整沉淀为：(1) 7 张可检索卡片树；(2) 2 个可执行能力资产；(3) 1 篇面向创业者的应用文章。跨域边已将提示词工程与讲香、IPO、动力阻力、武器库、科学表达五域连接。黄药师第二轮交付理解门禁全部通过，格式门禁零缺陷。

**后续建议**：`ai-deep-work` skill 应被本 vault 中所有 agent 在 session 启动时加载，作为默认操作协议的一部分。
