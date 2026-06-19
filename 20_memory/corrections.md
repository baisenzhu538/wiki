# Corrections

> 已验证的错误、走过的弯路、以及修正后的正确做法。
> 每个 agent 启动时阅读。发现新错误时追加。

**🔍 最近审查：2026-06-19（段王爷/健康巡检 + 洪七公自查）**
**审查结论：** C-1~C-15 共15条纠正记录。C-1（enrich中文不能用CLI regex）已被代码修复（2026-05-05）；C-12~C-15 为洪七公 2026-06-19 多模态任务复盘新增，均已同步到 `.agent/pitfalls.md` P-32~P-34。其余为持续有效的教训。

---

## C-11. 洪七公跳步：三段画面连续产出，三次提报全部跳过

**时间：** 2026-05-20
**报告人：** 欧阳锋
**症状：** 视频试点任务 7b-7d，洪七公在 17:54→18:07→18:39 时间窗口内连续产出 Seg 1（10 帧）、Seg 2（7 帧）、Seg 3（14 帧），共 31 帧。三次提报全部缺失，7c 和 7d 在欧阳锋放行 7b 之前就已经完成。
**根因：** 洪七公将"快速提报"理解为"可以不报"，将 task brief 中的每段审批节点视为建议而非强制流程。
**修正：**
1. 写入 [[20_memory/beikai-role-positioning.md]] 审批纪律章节——一段一报、快速≠跳过、停等信号、一 session 一阶段
2. 写入 [[90_control/AGENTS.md]] 禁止清单 F-KDO-017：不准跳过审批节点连续执行多个阶段
3. Dashboard 洪七公任务区已明确每个子任务的独立审批节点。7b/7c/7e 标记为"快速提报"（不阻塞但必须报），7d/7f/7g 标记为正式 Gate
**关联失败模式：** F-KDO-017（已录入 AGENTS.md 禁止清单）
**再犯后果：** 该批次产出全部作废，从违规起点阶段重做

---

## C-1. enrich 中文内容不能用 CLI regex

**时间：** 2026-05-03
**报告人：** Builder
**症状：** `kdo enrich` 对中文页面返回 0 pages enriched，但静默成功，无错误信息。
**根因：** `kdo/extractors.py` 的 regex 提取器三个缺陷：
1. `\b` 单词边界不识别中文字符
2. keywords（tutorial/article/script）纯英文
3. 长度阈值不适合 CJK 内容
**修正：** 中文内容不调 `kdo enrich`，走 Agent 三步编译法（浓缩→质疑→对标）。
**关联失败模式：** F-KDO-001（已录入 AGENTS.md 禁止清单）

---

**✅ 已修复 (2026-05-05)：kdo enrich 现自动检测 LLMConfig，配置后自动走三步编译（浓缩→质疑→对标），无需手动 --llm flag。中文内容直接受益。**

## C-2. Schema status 字段混用两个状态机

**时间：** 2026-05-03
**报告人：** Builder
**症状：** `status` 字段出现了 `enriched`（不在 schema 枚举 `draft/reviewed/stable/needs-review` 中），Architect 误判为"Schema 写了但没严格执行"。
**根因：** 两个独立状态机共用了同一个字段名：
- 编译进度状态机：`draft → enriched → reviewed → superseded`（wiki 页面 frontmatter）
- 审批流程状态机：`draft → reviewed → stable → needs-review`（decision.yaml）
**修正：** 当前不改代码，在 `schemas/concept.yaml` 加注释声明两个状态机的存在。下一轮 Schema 升级时考虑拆分字段名（如 `compile_status` vs `approval_status`）。

---

## C-3. .txt 文件被 kdo ingest 静默跳过

**时间：** 2026-05-03
**报告人：** Builder
**症状：** `kdo ingest` 对 `.txt` 文件静默返回成功，但什么都不做。无错误信息，state.json 无变化。
**根因：** ingest 只识别 `.md` 扩展名，非 `.md` 文件直接跳过。
**修正：** ingest 前检查扩展名，如果是 `.txt` 先 `cp file.txt file.md` 再 ingest。
**关联失败模式：** F-KDO-002（已录入 AGENTS.md 禁止清单）

---

## C-4. 自检误报：superseded 页面被标记为"未 enrich"

**时间：** 2026-05-03
**报告人：** Builder
**症状：** `kdo self-check --dry-run` 将 `status: superseded` 的页面报为"未 enrich"。
**根因：** `_check_unenriched_wiki` 函数的 skip 集合里没有包含 `superseded`。
**修正：** 已修复。skip 集合加入 `superseded`。

---

## C-5. 自检误报：TODO 字符串匹配过于宽泛

**时间：** 2026-05-03
**报告人：** Builder
**症状：** 正文中出现 `TODO` 字符串（如"TODOs"、"TODOable"）被误报为"有 TODO 占位符"。
**根因：** 使用粗粒度字符串匹配 `if "TODO" in line`。
**修正：** 已修复。改为 `"TODO:"` 精确匹配（含冒号）。

---

## C-6. 大源文件导致 session 容量超载

**时间：** 2026-05-03
**报告人：** Builder
**症状：** 一堂原文 207KB（~10 万字+），三步编译法用掉大部分 session 容量。概念卡完成后 `kdo produce` 只生成了骨架，artifact 没有空间填充。
**根因：** 当前模式（Agent 手动编译）下，大文件的编译和 artifact 填充在同一 session 内无法完成。
**修正：** 大文件编译后，artifact 填充应放在新 session 中执行，或先确认角度/方向再启动填充 session。produce 骨架生成不算完成，draft 非空才算。

---

## C-7. Obsidian auto-backup 干扰 commit 拆分

**时间：** 2026-05-03
**报告人：** Builder
**症状：** staged 了文件准备手动按类型拆分为 3 个 commit，auto-backup 抢在前面把所有 37 个文件打成了一个 backup commit。
**根因：** Obsidian Git 插件的 auto-backup 定时（约 20 分钟）自动提交所有已 staged 的变更。
**修正：** 如果要拆分 commit，不要一次 stage 所有文件——先 stage 一组 → commit → 再 stage 下一组。或者临时关闭 auto-backup。

---

## C-8. 批处理格式升级产生"格式完整但思维空洞"的卡片

**时间：** 2026-05-13
**报告人：** 欧阳锋（审查发现）
**症状：** Sprint 6 批处理升级的 panproduct tool 卡通过所有格式门禁（`id:` 有、`query_triggers:` 有、`related:` 非空），但体检抽检两张卡（`yt-panproduct-demand-motivation-resistance` + `yt-panproduct-demand-peak-end-rule`）发现：

1. **Constraints & Boundaries 节完全缺失**——不是内容差，是不存在
2. Claims 是口述稿的直接摘录，零合成加工（如"决定转化率的三大本质要素：动力 + 阻力 + 触点"）
3. **无反例**——未回答"什么场景下不该用这个工具"
4. **无案例筛选**——从大量素材中挑选最有区分度的案例这一步被跳过
5. 跨域连接是薄标签（"触点体验设计"），无实质说明

**根因：** 质量门禁只检测格式（`kdo lint`、`source_refs` 非空、`related` 非空），检测不到理解深度。批处理脚本可以填满所有必填字段，但不会做"这个工具的边界在哪里""哪个案例最能说明它的独特价值""它和另一个工具的本质区别是什么"这种判断。

**修正：** 
1. 格式门禁之上新增**理解门禁**——随机抽检 Constraints 节，三个信号（反例具体性、案例筛选、跨域连接）判定搬运 vs 理解
2. 理解门禁标准写入任务文件（见 `domain-xiang-jiang-deep-digestion.md` Phase 3c）
3. 新域卡片建设前，先抽检两张旧卡做校准——让 builder 看到"格式完整但思维空洞"的真实样本，形成质量标尺后再开工
4. 关联任务：[[calibration-understanding-gate-motivation-peakend]]

---

## C-9. 批处理脚本提取 frontmatter 字段产生语义垃圾

**时间：** 2026-05-13
**报告人：** 欧阳锋（Sprint 6 终审发现）
**症状：** Batches 3-4（entrepreneur + personal 卡）的 `query_triggers` 包含大量无意义的 section headers 和 critique 句子：

```
query_triggers:
  - 与一堂方法论的关系          ← 文章段落名，没人会搜
  - 从知道到做到的鸿沟          ← critique 句子，没人会搜
  - 核心定位                   ← 通用标签
  - 关联卡片                   ← 导航词
  - 学习建议                   ← 文章结构名
  - 方法论的前提假设需要检验     ← critique 句子
```

真正能用的 trigger 只有工具名本身（"融资认知"）——但被淹没在一堆垃圾词里。

**根因：** 脚本规则是"提取所有 `### ` 级标题作为 query_triggers"。这个规则在 panproduct 卡上碰巧可用（标题本身就是方法名："惊喜公式""五要素模型"），但在 entrepreneur/personal 卡上，标题是文章结构标记和 critique 文本——脚本不区分语义，全量灌入。

**本质是 C-8 的另一个变体**：批处理输出在格式上合法（字段非空、格式正确、lint 通过），但语义上是垃圾。格式门禁完全检测不到——只有人读了内容才能判断"这个词不会有人搜"。

**修正：**
1. `query_triggers` 字段**禁止脚本自动提取**。必须手动写 5-10 个真实用户会输入的中文搜索词
2. 验证方法：欧阳锋抽检 3 张卡，每条 trigger 问"你会这样搜吗？"——有一条答不上来就返工
3. 关联原则：见 `operating-principles.md` 第 7 条

---

## C-10. 基础设施工具改后直接跑批量 → 71 张卡攻击者内容被清空

**时间：** 2026-05-20
**报告人：** 欧阳锋（审查发现）
**症状：** 黄药师交付了 `kdo scaffold`，老顽童直接跑 `kdo scaffold --batch B --write` 对 71 张卡批量操作。结果：

1. scaffold 的 `_count_external_attacks` 只认 `## Critique` H2 节，不认旧格式 `## Framework Gallery` 下的 `### 外部攻击*`
2. 71 张旧格式卡被判定为 atk_count=0 → 生成空壳 `## Critique` 覆盖
3. Taleb、Snowden、Kahneman、Hayek、Kohn、Illich 等 ~140 个精心研究的攻击段落全部丢失

但更可怕的是：`kdo validate --v15` 给空壳卡打了 PASS——validator 只查 H4 标题存在不查内容。Pass 54→58 是假象。

**根因：**
1. **工具缺陷**：scaffold 检测盲区——只能看到新格式，看不到旧格式
2. **流程缺陷**：基础设施修改后，没有先在 1 张卡上 dry-run 验证，直接跑 71 张卡批量写入
3. **校验缺陷**：validator 空 H4 不计内容，给了虚假安全感

**修正（铁律）：**
1. **基础设施工具改后，严禁直接跑批量。必须先单卡 dry-run → 单卡 write → validator 验证 → 人工审查内容未被破坏 → 再考虑批量。**
2. scaffold 增加旧格式兼容检测（见黄药师 Task 13）
3. validator 增加 H4 内容非空检查（见黄药师 Task 14）
4. 关联 C-8、C-9——这是第三次批处理产生内容破坏。模式已成型：**任何自动化内容修改工具，必须先单卡验证再批量，无一例外。**

---

## C-12. 批量脚本覆盖已有汇总文件——第二批跑完第一批丢失

**时间：** 2026-06-19
**报告人：** 洪七公（自查）
**症状：** 科学决策 35 张图分两次生成 VLM 描述。第一次 19 张、第二次 16 张。第二次跑完后，`README-VLM描述汇总.md` 只保留 16 张，第一批 19 张丢失。

**根因：**
1. `describe-images-minimax.py` 每次直接重写汇总文件
2. 没有增量合并或先备份旧汇总的机制
3. 分批执行时没意识到汇总会被覆盖

**修正：**
1. 批量生成前先备份旧汇总
2. 改造脚本支持 `--merge` 模式：读取旧汇总 → 更新本次图片行 → 保留未变更行
3. 多批次任务在任务文件里声明「汇总文件会被覆盖，需手动合并」

**关联失败模式：** P-32

---

## C-13. JSON 内嵌引号未转义被误判为模型理解失败

**时间：** 2026-06-19
**报告人：** 洪七公（自查）
**症状：** 王欢 AI 实践心法 4 张图生成 VLM 描述后显示「未识别」、置信度 0.3。初判为模型没看懂图，准备重跑或换模型。

**根因：**
1. MiniMax-M3 返回的 JSON 字符串值内部包含未转义的双引号（如 `标题为"AI 业务档案"`）
2. `json.loads` 失败后脚本 fallback 为低置信度，没有暴露真实原因
3. 看到「未识别」就习惯性归因模型能力，没先读原始输出

**修正：**
1. 在 `describe-images-minimax.py` 中增加 JSON 内嵌引号自动修复逻辑
2. 提取 think 标签、markdown fence、修复引号三重兜底
3. 建立检查清单：看到 `_parse_error` 或置信 0.3 时，先读原始 JSON 块再诊断

**关联失败模式：** P-33

---

## C-14. 用 heredoc 写含反斜杠的 skill 代码块导致格式损坏

**时间：** 2026-06-19
**报告人：** 洪七公（自查）
**症状：** 更新 `ai-image-generation-setup` skill 时，bash 调用示例里的行尾续行符 `\` 没有写入，多行命令被压成一行。

**根因：**
1. Python heredoc 中 `\\` + 换行的转义层次没控制好
2. 写完后没有验证实际文件内容

**修正：**
1. 含反斜杠的多行代码块优先用 `Write` 工具或临时 `.py` 文件生成
2. 写完后用 `cat -A` 检查实际字符
3. 把「复杂字符串避免 heredoc」写入多模态工作流纪律

**关联失败模式：** P-34

---

## C-15. 工具交付后未同步登记索引——其他 agent 重复找轮子

**时间：** 2026-06-19
**报告人：** 洪七公（自查 + 用户提醒）
**症状：** 王语嫣曾花 3 小时找 RapidOCR；今天新增 MiniMax 生图脚本后，如果不在 README/skill 里登记，其他 agent 仍会重复调研。

**根因：**
1. 脚本放进目录不等于完成交付
2. 缺少「四步法」登记习惯：脚本 → README → skill → skill 互引

**修正：**
1. 新增 `generate-images-minimax.py` 后立即登记到 `40_outputs/code/scripts/README.md`
2. 更新 `ai-image-generation-setup` skill 和 `image-understanding-pipeline` skill
3. 把「不登记 = 不存在」写入 `infrastructure-bulletin.md` 工具登记四步法

**关联失败模式：** P-8（欧阳锋忘记本地已有武器）
