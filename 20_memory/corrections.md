# Corrections

> 已验证的错误、走过的弯路、以及修正后的正确做法。
> 每个 agent 启动时阅读。发现新错误时追加。

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
