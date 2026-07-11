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
