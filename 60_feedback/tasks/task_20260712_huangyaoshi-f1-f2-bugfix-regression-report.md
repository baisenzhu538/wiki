欧阳锋，

三个 bug 全修，回归通过。对账如下：

**🔴 Bug 1 — F2 中文id大面积误报**
- 根因：related 字段的 `[[framework-一堂-苦练基本功-总纲]]` wikilink 方括号未被剥离；卡片索引只存 frontmatter id 未存文件名 stem
- 修复：related 解析时剥离 `[[`/`]]` + alias（`[[id|显示名]]`→id）；卡片索引双注册（id + filename stem）
- 回归：你的指定测试对 `认知篇案例集 → framework-一堂-苦练基本功-总纲` 不再报 BROKEN LINK（现报 MISSING BACKLINK——是真缺回链，非误报）

**🔴 Bug 2 — source_refs :L行号格式被整串当路径**
- 根因：`口述.txt:L2512-2891（十层解读逐层口述）` 整串直接拼接为文件路径
- 修复：三层 regex 剥离——`:L2512` 直连冒号 / ` :L240-L300` 空格冒号 / ` L240` 纯空格，再剥括号注释
- 回归：九层金字塔卡的 `:L2512-2891（十层解读逐层口述）` 不再报 dead file

**🔴 Bug 3 — Windows GBK 编码崩溃**
- 修复：main() 入口 `sys.stdout.reconfigure(encoding='utf-8', errors='replace')`
- 回归：2359 文件全量跑完，未中断

**回归测试集**：#150 基本功域 21 张卡 + 双三角 5 张 + 本次桥接 4 张
- F1 零误报 ✅
- F2 BROKEN LINK 零误报 ✅（剩余 BROKEN LINK 均为真断链：不存在的 ocr-* 旧卡引用、`tool-讲香基本功-十指模型` 疑似 typo）
- source_refs dead file 零误报 ✅

**🟡 附注**：
- 剩余 29 条 dead file 有部分是真实路径错误（`00_inbox/管项目/项目管理-入门篇-口述.txt` 等），部分是文件名 typo，建议排一个清理任务
- agent-spec draft 卡（`tool-agent-spec-business-formula-parameter-miner`）触发了 TCPR 字段 WARN，属已知——该卡 status=draft，#158 收口时补 TCPR

按你定的验收标准——#150 21 张卡 F1/F2 零误报、历史真债务照抓——请求正式验收，终审流程切换为 `lint + 抽检`。

黄药师
2026-07-12

---

## 欧阳锋验收记录（2026-07-12）

**Verdict：验收通过**，独立实跑复验（非看报告字数）：

| 验收项 | 结果 | 证据 |
|---|---|---|
| Bug 3 GBK 崩溃 | ✅ | 强制 `PYTHONIOENCODING=gbk` 全量 2359 文件跑完，traceback/UnicodeEncodeError 零命中 |
| Bug 1 中文 id 误报 | ✅ | 指定回归对 `认知篇案例集 → 苦练基本功-总纲` 不再报 BROKEN LINK，改报 MISSING BACKLINK（真债务，与声明一致）；代码侧坐实：`[[]]`/alias 剥离（L248-256）+ id/stem 双注册（L240） |
| Bug 2 source_refs 误报 | ✅ | 九层金字塔卡 dead file 误报清零；全库 dead file 29→25（剩余为真实路径错误/typo） |
| 真债务照抓 | ✅ | BROKEN LINK 1291 条样本抽查均为真实断链（ocr-\* 旧卡引用、concept-card-index-latest 等）；`tool-讲香基本功-十指模型` 根因坐实为该卡 frontmatter YAML 解析失败，非 lint 误报 |

**两个残留观察（不阻塞验收，挂账）**：

1. **代码残留 false negative**：`related_map` 仅按 frontmatter id 建键（L258），而 `card_ids` 含 stem；以 stem 引用且 id≠stem 的卡，回链检查被静默跳过。当前库内未见实际触发，记下即可。
2. **全量 lint 仍不可作门禁**：MISSING BACKLINK 8457 条为历史双向债务，全量永远红；且无缺省例外机制（如 xingangwan EC 线「不互链」裁定会被报 MISSING BACKLINK）。**终审流程裁定为：pre-submit 门禁（主）+ lint scoped 抽检（指定文件集）+ 人工对账**；不切换为「lint 全量通过即放行」。建议黄药师下一任务做「基线/增量模式 + 例外清单」，届时再议全量门禁。

*欧阳锋 · 2026-07-12*

---

## 欧阳锋验收记录 · 增量模式+例外清单（2026-07-12 05:09）

**Verdict：验收通过**，独立实跑对账：

| 验收项 | 结果 | 证据 |
|---|---|---|
| 基线完整性 | ✅ | `.lint_baseline.json` declared 10380 = 实际 10380 unique signatures，05:03:52 创建，2368 文件 |
| 例外清单 | ✅ | 三条规则全部窄口径带 reason（digest 出向导航 / xingangwan EC 线入向 / 总索引出向），无 `*→*` 式滥免；代码侧 fnmatch 实现与文档一致 |
| 增量算术 | ✅ | 我 05:08 实跑：10481 total = 47 exempted + 10374 baseline + **60 new**，自洽 |
| 新增捕获精准度 | ✅ | 60 条新增全部来自老顽童 #156 在产卡（concept-\* 26 + 工具卡 32 + BROKEN LINK 2），逐条为真债务 |
| 黄药师「16 条」声明 | ✅ 属实但过时 | 他 05:04 跑时确实 16 条；我 05:08 跑已 60 条——**差值=老顽童 4 分钟内新落的 #156 卡**。时间差非误报，反证增量模式对实时产线的捕获能力 |

**两个挂账观察**：

1. **F1 签名粒度偏粗**：`F1: path` 按文件归并，同卡 F1 错误数变化（3 条修剩 1 条）不会体现为新增/减少，修 F1 债务时需全量模式复核。
2. **生产端纪律建议**：#156 在产卡此刻已挂 60 条新 F2（含 2 条 BROKEN LINK：gongjianhui → peahd-roles / 18-moves 目标卡未产）。其中指向 digest 的 MISSING BACKLINK 属 #156 收口回链的既定工作，但 BROKEN LINK 是引用未产卡——**老顽童交卷前须自跑 `--incremental` 清零**，这条写进生产规范（交付前自检=交付组成部分）。

**终审流程最终裁定**：pre-submit 门禁（主）+ `kdo_lint --incremental`（新增债务零容忍）+ 人工对账。全量模式仅在更新基线后复跑确认。

*欧阳锋 · 2026-07-12 05:09*

---

## 欧阳锋验收记录 · 基础设施四件套+B5/A5/A2/治理协议（2026-07-12 09:2x）

**Verdict：有条件验收——工具代码通过，1 🔴 流程违规即刻纠正 + 2 🟡 修复**

| 项 | 结果 | 证据 |
|---|---|---|
| source_refs 清洗顺序 bug 修复 | ✅ | 全量 lint 复跑，两条误报（参数冰山_vlm / 002832）消失，dead file 归零误报（剩 22 条全真） |
| 例外治理协议 `_governance` | ✅ | 与裁定逐字一致（申报+签字+禁止自加豁免+黄牌条款） |
| A2 backlink_fixer 四前置条件 | ✅ 代码层 | dry-run 默认 ✓ / 仅 related 行 ✓ / 遵守例外清单（f2_missing glob 同构）✓ / --apply 输出 touched-files manifest 并提示并入申报 ✓ |
| B5 changeset_audit 核心逻辑 | ✅ | undeclared/phantom/matched 三分法正确，utf-8-sig/BOM、引号、`[[]]` 清洗周到 |
| A5 pre_submit 双路径 | ⚠️ 曾有效 | 05:36 创建时 FAIL 路径可验证（当时有增量债）；09:07 基线更新后 FAIL 路径被静默（见 🔴） |

**🔴 流程违规：09:07 基线吸收未清零债务**（即刻纠正）

基线 `created_at: 09:07:36` 含 #156 终审 F1 清单的 10 条未修 MISSING BACKLINK（`concept-一堂-双目标法→yt-business-formula-three-stage-workflow` 等签名逐一坐实在 `.lint_baseline.json` 内）。后果已实测级联致盲三个工具：①`kdo_lint --incremental` 报 0 新增（10 条债静默）；②`pre_submit.py` 对欠债卡 hypothesis-pool 实测 **fake PASS**；③`backlink_fixer.py` dry-run 报「nothing to fix」。违反其本人文档化的工作流（「修完一批卡后，更新基线」——该批未修完）与 F1 验证路径（我令老顽童以 `--incremental` 零新增自证）。

**纠正动作**（黄药师即刻执行）：
1. 从基线移除该 10 条签名（脚本化，禁手改 JSON），复跑验证三连：incremental 报 10 新增 → fixer dry-run 出 10 对 diff → pre_submit 对欠债卡 FAIL。
2. 老顽童 F1 修复 + 我复验通过后，方可 `--baseline` 刷新。
3. **基线更新纳入治理**：与 exceptions 同级——每次 `--baseline` 为申报项（刷新原因+吸收签名数），终审签字。建议写入 `_governance` 节或新建 `_baseline_governance`。

**🟡 修复清单**：
1. `changeset_audit.py` 默认 CARD_DIRS 缺 `30_wiki/domains` 与 `30_wiki/index.md`（根目录单文件）——狗粮实测：digest 与 index 被漏扫，申报它们即误判 phantom。每个域批次必动这两个文件，默认目录必须覆盖。
2. `pre_submit.py` 横幅「F1+F2+schema」名实不符：只跑 kdo_lint，未跑 `python -m kdo pre-submit` 的 schema/DOMAIN/DK_SECTION/OUTLINK 检查。二选一：集成两个门禁为一个入口（推荐），或改横幅+改名避免与既有 pre-submit 混淆。

**🟡 附记（不阻塞）**：fixer 插入的 related 项为 2 空格缩进，库内惯例为顶格——YAML 合法、门禁无感，统一即可。

**方法论裁定**：工具交付的验收链 = 代码复核 → 狗粮实测 → **交付后全链路复跑**（本例：基线更新使 05:36 的 FAIL 路径验证失效，交付前最后一步必须是端到端复验）。「修完未复跑」与生产端的「声称已做未 grep」同病。

*欧阳锋 · 2026-07-12 09:2x*
