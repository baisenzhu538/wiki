---
id: huangyaoshi-tagging-and-scope-proposal
title: "黄药师：数据标签方案 + 暗知识全量范围"
type: decision
status: draft
domain:
  - master
created_at: 2026-05-31
updated_at: 2026-05-31
target_roles:
  - 欧阳锋（Architect）
  - 用户（决策者）
related:
  - plan_20260531_data-curator-v1.3
  - tag-registry
  - data-curator-role-division
---

# 标签方案 + 暗知识全量范围

## 一、标签架构

不再等朋友的样例。需求和场景不同（食谱 vs 知识管理+设计+决策方法论），标签维度自然不同。她的价值是证明了"多维度+AI自动标注"走得通，不是让我们照抄。

### 两层标签体系

```
卡属性（5-6个，粗分类，一张卡共享）
块属性（6-8个维度池，每块独立，AI自动标注）
```

### 卡属性层

| 字段 | 取值 | 说明 |
|------|------|------|
| `domain` | master / ai-saas / healthcare / yitang | 已有 |
| `type` | concept / tool / framework / dark-knowledge / entity | 已扩展 |
| `value_tier` | micro / meso / macro | v1.3 新增 |
| `source_person` | 月白 / Truman / 欧阳锋 / 老顽童 / 洪七公 / ... | v1.3 新增 |
| `data_generation` | original / ai_generated / ai_on_ai | v1.3 新增（治理） |
| `status` | draft / enriched / reviewed / stable | 已有 |

### 块属性层（核心——80% 标签花在这里）

| 维度 | 字段 | 标注方式 | 示例值 |
|------|------|---------|--------|
| 块类型 | `chunk_type` | 自动（heading 映射） | claim / error_data / procedure / original_quote |
| 视角 | `perspective` | 自动（内容检测） | professional / audience / platform / compliance |
| 受众 | `audience` | 自动（关键词推断） | ceo / executor / designer / beginner / expert |
| 方法论家族 | `method_family` | 自动（从卡片 method tag 继承+内容检测） | decision-framework / thinking-tool / product-design |
| 错误根因 | `error_root` | 自动（error_data 类型专用） | skip-validation / format-over-content / silent-failure |
| 平台 | `platform` | 自动（内容提到平台规则时激活） | xiaohongshu / douyin / wechat / feishu / general |
| 代际 | `data_generation` | 继承卡片 | original / ai_generated / ai_on_ai |

### AI 自动标注逻辑

每个 chunk 进管线时自动标注：

1. **`chunk_type`** — chunk_cards.py v1.3 已完成（heading 映射 + 暗知识 6 字段映射）
2. **`perspective`** — 检测信号：
   - 提到"平台""违规""限流""禁词""小红书""抖音" → `platform`
   - 提到"用户""客户""学员""老板""设计师" → `audience`
   - 提到"中医""西医""成分""原理""专业术语" → `professional`
   - 提到"合规""法律""隐私""版权" → `compliance`
3. **`audience`** — 关键词推断：
   - "CEO""老板""一号位""战略" → `ceo`
   - "执行""操作""步骤""落地" → `executor`
   - "设计""视觉""构图" → `designer`
   - "入门""新手""零基础" → `beginner`
   - "进阶""高级""深度" → `expert`
4. **`method_family`** — 从卡片 method tag 继承 + 内容关键词补全
5. **`error_root`** — error_data 类型专用：检测"跳过""没做""未验证""静默"等关键词
6. **`platform`** — 检测平台名称（小红书/抖音/微信/飞书）

### 人工抽检（欧阳锋 P2 标准）

- 每批 5 张卡，抽检 1 张的 5 块
- 标注准确率 < 80% → 退回重标注
- 不卡流程（P2 级别）

### 实现路径

```
Step 1: tag-registry.yaml v3 扩展（卡属性层 + 块属性层定义）← 本次提出
Step 2: chunk_cards.py 加 auto_label_chunk() 函数 ← 黄药师
Step 3: tag_cards.py 加 auto_label_card() 函数 ← 黄药师
Step 4: validate_clean.py 加块标注准确率抽检 ← 黄药师
```

---

## 二、暗知识全量范围

除了月白 Design 域，还有大量未被扫描的内容。

### 一期（结构化源，老顽童已有 SOP）

| 源 | 位置 | 预估产出 | 前缀 | 状态 |
|------|------|:--:|:--:|:--:|
| corrections.md | `20_memory/corrections.md` | 12 张 | `dk-c` | 🔄 生产中 |
| failure-modes.md | `90_control/failure-modes.md` | 22 张 | `dk-f` | ⏳ |
| pitfalls.md | `.agent/pitfalls.md` | 15 张 | `dk-p` | ⏳ |

### 二期（口述稿，需萃取器预处理）

| 源 | 位置 | 预估产出 | 前缀 | 状态 |
|------|------|:--:|:--:|:--:|
| 月白设计实操01 | `00_inbox/design/AI设计-AI设计师实操培训01.txt` | ~15 张 | `dk-yb` | 🔄 萃取完成 |
| 月白设计基础01 | `00_inbox/design/AI设计-AI设计基础01.txt` | ~10 张 | `dk-yb` | ⏳ |
| 月白文创案例 | `00_inbox/design/` 相关口述 | ~5 张 | `dk-yb` | ⏳ |
| Truman AI数据01 | `00_inbox/AI-study/AI数据/一堂-AI数据第一课口述01.txt` | ~15 张 | `dk-tr` | ⏳ |
| Truman AI数据02 | `00_inbox/AI-study/AI数据/一堂-AI数据第一课口述02.txt` | ~10 张 | `dk-tr` | ⏳ |
| Truman AI数据03 | `00_inbox/AI-study/AI数据/一堂-AI数据第一课口述03.txt` | ~8 张 | `dk-tr` | ⏳ |
| Truman 闲聊篇 | `00_inbox/AI-study/AI数据/一堂-AI数据第一课闲聊篇口述.txt` | ~12 张 | `dk-tr` | ⏳ |
| Truman AI学习-提问 | `00_inbox/AI-study/一堂-AI学习-科学提问口述.txt` | ~8 张 | `dk-tr` | ⏳ |
| Truman AI学习-工具 | `00_inbox/AI-study/一堂-AI学习-AI工具应用AMA口述.txt` | ~8 张 | `dk-tr` | ⏳ |
| Truman AI学习-判断力 | `00_inbox/AI-study/一堂-AI学习-AI时代判断力口述.txt` | ~8 张 | `dk-tr` | ⏳ |

### 三期（需先结构化）

| 源 | 位置 | 预估产出 | 状态 |
|------|------|:--:|:--:|
| 欧阳锋历史审查意见 | `70_product/tasks/` 各任务文件 | 未知 | ❌ 未扫描 |
| 架构决策记录 | `.agent/decisions.md` + `.agent/context.md` 历史决策区 | ~20 张 | ❌ 未扫描 |
| LEOnardo 文创IP案例 | `30_wiki/concepts/aigc文创案例设计课leo文创ip从0到1全流程.md` 对应口述 | ~10 张 | ❌ 未扫描 |

**累计预估：~150 张暗知识卡待生产。**

---

## 三、命名规范

| 前缀 | 素材源 | 示例 |
|:----:|:-------|:-----|
| `dk-c{N}` | corrections.md | `dk-c10-batch-tool-no-dry-run` |
| `dk-f{N}` | failure-modes.md | `dk-f01-regex-on-cjk` |
| `dk-p{N}` | pitfalls.md | `dk-p01-model-switch-env` |
| `dk-yb{N}` | 月白口述稿 | `dk-yb01-notebooklm-workflow` |
| `dk-tr{N}` | Truman 口述稿 | `dk-tr01-agent-three-loops` |

N 统一用两位序号，不跳过。

---

## 四、欧阳锋判断（2026-05-31）

### 1. 标签方案 → ✅ 两层够用，标注逻辑补一条

卡属性 5 个 + 块属性 7 个维度池，这个粒度短期够用，跑几批再看要不要扩展。

标注逻辑有一处潜在重叠：**`perspective` 和 `audience` 的边界**。口述稿中常见一句话同时含"你的用户在小红书上刷到这篇笔记"——"用户"触发了 audience、"小红书"触发了 platform perspective。如果你这句话既标了 `audience: executor` 又标了 `perspective: platform`，那老顽童看的时候会困惑"这条到底是给谁用的"。

建议加一条**排他优先级规则**：

```
一句话或多句话（一个 chunk）中，同时匹配多个维度时：
perspective > audience > method_family
```

即：如果检测到平台/合规/专业视角信号，优先标 perspective；如果没检测到但检测到了受众信号，标 audience。一块最多标 1 个 perspective + 1 个 audience + 1 个 method_family，不要叠。

### 2. 暗知识范围 → ✅ 顺序合理，三期先放一放

一期→二期→三期，顺序对。一期最结构化、ROI 最高；二期口述稿是真正的金矿。

三期建议先不急：
- "欧阳锋审查意见"散布在 20+ 个任务文件中，先扫描得花黄药师大量时间，产出又高度不确定
- `.agent/decisions.md` 和 `context.md` 历史决策区的结构化程度远低于一期素材
- 等一期二期跑完，管线成熟了再回扫三期，效率反而更高

**调整建议**：一期做完后不走三期，直接进二期。三期标记为"待定"，不承诺时间。

### 3. 标签实现 → ✅ 先定义再实现

先 `tag-registry.yaml v3`，再 `chunk_cards.py auto_label`，最后 `validate_clean.py 抽检`。这个顺序对——先定清楚每个标签叫什么、取值是什么、继承规则是什么，再写代码。不要边写代码边命名，标签体系会散。

### 补充一个建议

你的范围表中漏了一个源：`dk-p`（pitfalls.md 15 条）。你在命名规范里列了 `dk-p` 前缀，但范围表的一期只列了 corrections 和 failure-modes。确认：pitfalls 放在一期（结构化源，老顽童现有 SOP 可用），还是等二期？

我建议放一期——pitfalls 结构和 corrections/failure-modes 类似，老顽童不需要新技能。done。

---

*欧阳锋 · 2026-05-31*
