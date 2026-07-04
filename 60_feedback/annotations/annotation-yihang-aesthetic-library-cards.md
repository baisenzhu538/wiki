---
id: annotation-yihang-aesthetic-library-cards
type: annotation
status: active
source_refs:
  - 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt
related:
  - '[[method-yihang-aesthetic-fast-build]]'
  - '[[tool-aesthetic-library-builder]]'
  - '[[case-yihang-truman-aesthetic-library-practices]]'
  - '[[annotation-yihang-dual-triangle-master]]'
  - '[[extraction-yihang-dual-triangle-main]]'
---

# 审美库三张卡入口标注

> 本标注把 Truman 建立审美的具体做法、工具、数字、命令行全部摊开，作为 #72 三张卡（method / tool / case）的直接生产入口。

---

## 一、背景：为什么必须产这三张卡

用户对王语嫣的批评是：「越来越抽象」「遗漏了 Truman 做审美的具体做法」「以后要建 agent，怎么让 agent 根据知识库解决实际问题」。

这三张卡的目标就是把「审美」从抽象概念变成可批量复制、可被 Agent 调用的工作流 + 工具 + 案例。

---

## 二、原始素材地图

| 素材段落 | 行号 | 内容 |
|:---|:---|:---|
| 审美定义 | 行 692-716 | 审美 = 判断力，不是品味 |
| Truman 做审美的家底 | 行 766-846 | 10+ 个审美库的具体做法和数字 |
| PPT 审美 | 行 460-502、514-524 | Keynote 转模型、配图指南、课程大纲方法论 |
| 官网审美 | 行 778-782 | Top 20 在线教育公司官网扫描 |
| 图片审美 | 行 788-802 | 爬虫抓 Cubox 5161 张，打分精选 244 张 |
| 视频审美 | 行 806 | 抓 C Dance 867 个，精选 16 个 |
| 音乐审美 | 行 812-814 | 网易 10 年 600+ 首歌建审美记忆模型 |
| 实事求是审美 | 行 824-829 | 李开复提示词 + 市场最佳实践研究报告 |
| Cloud 技能审美 | 行 830 | 扒 Cloud 官方高阶指南 |
| 段子审美 | 行 834 | 抓取段子类型建立最佳实践库 |
| 设计师审美 | 行 838 | 扫描人类顶级设计师最佳实践 |
| 短视频审美 | 行 840 | 扒抖音和热门频道最佳实践 |
| 审美快速建立三步法 | 行 4228-4250 | 拆细颗粒度话题 → 找超出想象案例 → 幻想美好作品 |
| 知识层与数据层解耦 | 行 5026-5078 | 审美+体系进核心提示词，DataPack 插件化组合 |

---

## 三、`method-yihang-aesthetic-fast-build`：审美快速建立工作法

### 3.1 一句话

审美不是品味，是通过密集最佳实践输入、显性化打分、快速拉起的判断力。

### 3.2 原文依据

> 「审美不是品味，是判断力。」（行 692-716）
> 「审美是可以建立的，不是靠你过去，你可以现场建立审美，靠的是极短的时间内快速学习。」（行 220）
> 「想解决个问题，先把自己审美拉上去。」（行 846）

### 3.3 四步工作法

| 步骤 | 动作 | 关键问题 | 原文行号 |
|:---|:---|:---|:---|
| **Step 1：拆细颗粒度话题** | 把大主题拆成 10-20 个可独立判断的细分维度 | 这个领域里「好」有哪些维度？ | 行 4228-4250 |
| **Step 2：超量案例浸泡** | 收集远超当前判断力的最佳实践案例（本地 + 网络） | 全球最好的案例长什么样？ | 行 4228-4250、766-846 |
| **Step 3：打分筛选** | 用 60-99 分标尺给案例显性化打分 | 这个案例好在哪？差在哪？ | 行 798-802 |
| **Step 4：幻想美好作品 + 减法还原** | 想象目标作品最美好的样子，挑最关键要素复刻 | 我想要的美好结果是什么？最少需要哪几个要素？ | 行 4228-4250 |

### 3.4 适用边界

- **适用**：高价值、可重复、需要与 AI 协作的任务（PPT、官网、图片、视频、音乐、文本、Agent 角色）。
- **不适用**：一次性任务、纯直觉艺术创作、没有标杆可参考的全新领域。

### 3.5 与双三角/Y模型的关系

- **双三角**：审美是人类三角顶点；审美库是数据资产的高级形态。
- **Y模型**：审美建立本身就是「理论侧（找标杆）+ 事实侧（打分验证）」的循环。

### 3.6 Checklist（≥8 条）

- [ ] 是否已经把这个主题的「好」拆成可判断的维度？
- [ ] 收集的案例数量是否足够大（建议至少 50-100+）？
- [ ] 是否使用了 60-99 分标尺给案例打分？
- [ ] 打分标准是否已经显性化（不是「我感觉好」）？
- [ ] 是否找到了超出当前想象力的标杆案例？
- [ ] 是否已经幻想出目标作品最美好的样子？
- [ ] 是否做了减法，只复刻最关键要素？
- [ ] 是否把审美库沉淀为可被 Agent 调用的 DataPack？

### 3.7 Anti-patterns（≥4 条）

1. **把「我喜欢」当成审美**：没有维度、没有标杆、没有校准。
2. **只收藏不评分**：案例堆积但判断标准没有显性化。
3. **追求完美第一步**：想等审美足够好再动手，结果飞轮转不起来。
4. **用一个审美库套所有场景**：PPT 审美和音乐审美是两套库，不能混用。

---

## 四、`tool-aesthetic-library-builder`：审美库采集工具

### 4.1 一句话

把 Truman 的审美库建设流程变成可复用的 CLI 工具，为任意主题批量生成可被 Agent 调用的审美 DataPack。

### 4.2 When to Use

- 需要为某个高价值、可重复任务快速建立审美库。
- 需要生成 DataPack 供 Agent system prompt 引用。
- 需要把隐性审美判断显性化为 60-99 分评分。

### 4.3 输入

| 输入 | 说明 |
|:---|:---|
| 主题描述 | 如「商业培训 PPT」「SaaS 官网 Hero 区」「短视频开场 3 秒」 |
| 本地素材目录 | 已有的图片/视频/文档/Keynote 等 |
| URL 列表 | 需要爬取的最佳实践页面 |
| 评分标准 markdown | 60-99 分各档的判定标准 |

### 4.4 输出

- 主题工作目录（`assets/` + `manifest.json` + `curated/`）
- 精选高分布案例（按分数/维度分层）
- 可直接被 Agent system prompt 引用的 DataPack markdown

### 4.5 子命令

```bash
python kdo-tools/aesthetic-library-builder.py init <topic>
python kdo-tools/aesthetic-library-builder.py collect --local ./raw --urls urls.txt
python kdo-tools/aesthetic-library-builder.py score --criteria criteria.md
python kdo-tools/aesthetic-library-builder.py curate --top 50
python kdo-tools/aesthetic-library-builder.py summarize --output ./data_packs/<topic>.md
```

### 4.6 依赖

- Python 包：`requests`、`beautifulsoup4`、`pillow`
- LLM API key：DeepSeek / OpenAI
- 已有原型：`kdo-tools/aesthetic-library-builder.py`

### 4.7 示例：为「商业培训 PPT」建立审美库

```bash
# 1. 初始化主题目录
python kdo-tools/aesthetic-library-builder.py init ppt-commercial-training

# 2. 收集本地 Keynote + 网络案例
cd ppt-commercial-training
python ../kdo-tools/aesthetic-library-builder.py collect \
  --local "~/Keynote/一堂课件" \
  --urls "best-practice-urls.txt"

# 3. 用评分标准打分
python ../kdo-tools/aesthetic-library-builder.py score \
  --criteria "ppt-aesthetic-rubric.md"

# 4. 精选 Top 50
python ../kdo-tools/aesthetic-library-builder.py curate --top 50

# 5. 输出 DataPack
python ../kdo-tools/aesthetic-library-builder.py summarize \
  --output "./data_packs/ppt-commercial-training-aesthetic.md"
```

### 4.8 Checklist（≥6 条）

- [ ] 主题是否已经拆细到可判断的维度？
- [ ] 本地素材和网络素材是否已去重？
- [ ] 评分标准是否已经写入 markdown？
- [ ] LLM 评分结果是否已人工抽检校准？
- [ ] 精选案例是否覆盖了 60-99 分的完整分布？
- [ ] 输出的 DataPack 是否可被 Agent system prompt 直接引用？

### 4.9 Anti-patterns（≥4 条）

1. **不拆细维度就收集**：导致案例堆积但无法判断。
2. **完全依赖 LLM 打分**：没有人工抽检校准。
3. **只选 90+ 分案例**：缺少 60-80 分的反面教材，审美会失衡。
4. **DataPack 不做版本管理**：审美库会随时间迭代，需要版本和来源追溯。

---

## 五、`case-yihang-truman-aesthetic-library-practices`：Truman 审美库建设实践

### 5.1 人物

Truman（一堂创始人），过去一年（约 2025 年前后）。

### 5.2 时间线

| 阶段 | 时间 | 动作 |
|:---|:---|:---|
| 工具迷信期 | 2023-2025 初 | 反复尝试 Gamma、Cubox、NotebookLM 等工具，燃起希望→失望→清零 |
| 系统觉醒期 | 2025 年 | 意识到不是工具问题，而是审美+体系+数据+基本功的系统问题 |
| 审美库建设期 | 过去一年 | 围绕 PPT、官网、图片、视频、音乐、文本等建立多个审美库 |
| 应用期 | 2026 年春 | 飞书 ToSlide、官网、音乐、Agent 等产出效率大幅提升 |

### 5.3 动作清单（必须量化）

| 审美库 | 动作 | 数量/结果 | 行号 |
|:---|:---|:---|:---|
| **PPT 审美** | 建知识站场/Home；把所有过去 Keynote 转成模型；做配图指南；做课程大纲方法论；萃取官方最佳实践和数据 | 沉淀为飞书 ToSlide 工作流；1000 页高阶营可控 | 行 460-502、514-524 |
| **官网审美** | 让 AI 找全球最大 Top 20 在线教育公司官网；逐字看完每个网页；把 header、亮点等抽成最小元素 | 完成一堂官网系统性审美 | 行 778-782 |
| **图片审美** | 爬虫抓取 Cubox 开源社区作品（带提示词），智能打分 60-99 | 5161 张中筛选出 244 张 | 行 788-802 |
| **视频审美** | 抓 C Dance 2.0 视频，打分 | 867 个中筛选出 16 个 | 行 806 |
| **音乐审美** | 把网易过去 10 年收藏的 600+ 首歌喂给 AI，建「审美记忆模型」 | 600+ 首 | 行 812-814 |
| **实事求是审美** | 研究李开复提示词 + 市场最佳实践，做研究报告 | 一套多层消除幻觉/让 AI 靠谱的最佳实践 | 行 824-829 |
| **Cloud 技能审美** | 扒下 Cloud 官方所有技能高阶指南 | 建立高阶指南模型和最佳实践 | 行 830 |
| **段子审美** | 为「奥斯卡」写段子 Agent，抓取喜欢的段子类型、教育段子、脱口秀大会段子 | 建立段子最佳实践库 | 行 834 |
| **设计师审美** | 让 AI 全面扫描人类顶级设计师最佳实践 | 设计师风格/方法库 | 行 838 |
| **短视频审美** | 扒抖音和热门频道视频最佳实践 | 短视频脚本/节奏库 | 行 840 |

### 5.4 结果

- 半年做审美的速度比过去三年都快。
- 为飞书 ToSlide、官网、音乐、Agent 角色等提供了审美天花板。
- 证明了「审美不是品味，是可训练的判断力」。

### 5.5 核心洞察

1. **AI 不会超过人的审美**：想解决高价值问题，先把自己审美拉上去。
2. **每个高价值任务都值得独立建审美库**：PPT、官网、图片、视频、音乐、文本、Agent 角色等。
3. **审美库最终要变成 Agent 可调用的 DataPack**：核心提示词（审美+体系）与 DataPack（数据）解耦，像插件一样组合。

### 5.6 对双三角的贡献

把「审美」从抽象概念变成可批量复制的工作流，为人类三角顶点提供了可执行的操作路径。

---

## 六、三张卡的交叉关系

```
case-yihang-truman-aesthetic-library-practices
        ↓
method-yihang-aesthetic-fast-build
        ↓
tool-aesthetic-library-builder
        ↓
Agent DataPack（被 agent-solver / canvas-agent 调用）
```

- **case 卡**回答「谁做了什么、结果如何」。
- **method 卡**回答「普通人怎么复刻」。
- **tool 卡**回答「有没有现成的 CLI 能跑」。

---

## 七、与 #70 课后闲聊的关系

#70 中也有一张 `method-yihang-aesthetic-fast-build`（来自课后闲聊的软装案例）。建议：

- **#72 的 method 卡作为主干版本**，覆盖 Truman 的完整做法和工具链。
- **#70 的 method 卡作为 companion/补充**，从课后闲聊角度补充软装案例和口语化表达。
- 两张卡通过 `related` 互相链接，避免重复。

---

## 八、建议产出

| 产出 | ID | 类型 | 优先级 |
|:---|:---|:---:|:---:|
| 审美快速建立工作法 | `method-yihang-aesthetic-fast-build` | method | P0 |
| 审美库采集工具 | `tool-aesthetic-library-builder` | tool | P0 |
| Truman 审美库建设实践 | `case-yihang-truman-aesthetic-library-practices` | case | P0 |

---

## 九、验收标准

- 3 张卡全部 `kdo pre-submit` 通过。
- method/tool/case 三类卡结构完整，不出现「漂亮话」代替具体动作。
- tool 卡必须能对照 `kdo-tools/aesthetic-library-builder.py` 脚本讲清楚每一步。
- case 卡必须出现 Truman、具体时间线、量化动作和结果。
- 至少反向更新 5 张已有卡 `related`。
- 欧阳锋终审通过。

---

## 十、自攻击

- **反例**：某些天才设计师不需要审美库也能产出好作品；方法是给普通人的脚手架。
- **成本**：建立审美库本身耗时，低价值任务不值得。
- **边界**：审美库不能替代真实用户反馈，最终 judgment 仍需人做。
