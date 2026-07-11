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
