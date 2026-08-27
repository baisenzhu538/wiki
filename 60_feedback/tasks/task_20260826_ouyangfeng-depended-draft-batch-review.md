---
id: 544
assignee: ouyangfeng
status: in_progress
updated_at: '2026-08-26T15:03:02.279895+00:00'
version: v0.1
instance: ouyangfeng
code_files:
- 30_wiki/
---

# #544 被依赖 draft 卡批次过审（#527 清单 23 张，欧阳锋按优先级过审）

- **任务号**：#544
- **状态**：queued
- **assignee**：ouyangfeng（审查单；终审结论逐张落卡）
- **优先级**：P1（欧阳锋在途表点名等编排——#527 交付备注已预告：清单交王语嫣→欧阳锋按优先级过审，首张 layered-system）
- **立项**：2026-08-26 王语嫣（清欠账：#527 终审备注的编排动作未落单，欧阳锋恢复记忆后在途表挂账）

## 背景

#527（被依赖卡 draft 门禁）交付时产出存量清单：23 张被 agent-spec/CLAUDE.md/数据链引用的 draft 卡。门禁只报警不改状态，处置=逐张过审决定升 reviewed 还是补内容。小昭盲测 P4 实证：layered-system 系 draft 但被 basic-skills-coach 活依赖——消费端踩 draft 的又一实面。

## 任务

1. 按 #527 清单优先级逐张过审，首张=`layered-system` 系（已预告）
2. 逐张落结论：升 reviewed / 退回补内容（FAIL 落点明确）/ 豁免挂账（注明理由）
3. 批次节奏自控，单张粒度终审记录落卡（同既有审查实践）
4. 过审中发现「被依赖但内容不达标」的共性问题 → 建议书报王语嫣（F-036 落点纪律）

## 边界

- 只审 #527 清单内 23 张，不外扩；draft 存量治理大盘（F-058）不在本单
- 本单是审查批，不是生产批：不改卡内容，只判级+给落点

## 验收

- 23 张逐张有结论落卡；首批 ≥5 张完成即算阶段性闭环（余量可续）；王语嫣抽核 2 张

---

## 批次记录（首批 5/10 张 · 2026-08-26 · 欧阳锋）

**进度**：23 条清单去重 = 10 张卡；首批完成 5 张（硬依赖 2 张 + 次优先 3 张），达到「首批 ≥5 张」阶段闭环线。余 5 张（agent-spec 互引簇 + dk-publish-collapse-to-iterate + skill-duanwangye-prezi）续下一批。

| # | 卡 | 结论 | 核心依据 |
|:-:|:--|:--|:--|
| 1 | framework-truman-feature-layered-system | **退回** | P1×2：L2=34 与 JSON 实测 38 不符（六层合计 96≠自述 100）；L113 引语行号误植（真实出处=口述上 L1300） |
| 2 | framework-truman-feature-thinking-core | **退回** | P1：「8 个格刻意留白（门捷列夫空位）」三源全查无出处；P2×2：两处引语添油（"成本越低"/"新手野路子到体系态"原文所无） |
| 3 | tool-zhu-ai-deliberate-practice-roadmap | **退回** | P0×2：source_refs 是正文表格行非路径（lint 3 ERROR 实证）；related: null。另 aliases 混入 tag 语法 |
| 4 | zhu-time-os | **退回（轻量）** | P1：双峰时段表（22:00-01:00 等）三源无出处，源仅支持定性"深夜高效"；落点=老朱本人确认 |
| 5 | framework-visual-analysis-four-dimensions | **退回** | P0×2：source_refs 为散文非路径（lint 因"无斜杠跳过"而 PASS——盲区）；related: null |

**共性发现 → 建议书（已落盘）**：
- `60_feedback/diagnosis/diag_20260826_ouyangfeng-lint-prose-source-refs-blindspot.md` — lint source_refs 检查"无斜杠逃逸"盲区（双对照实证）
- `60_feedback/diagnosis/diag_20260826_ouyangfeng-feature-json-mojibake.md` — feature-periodic-table-v0.8.json note 字段 mojibake 不可逆损坏

**审查方法说明**：每张卡先开 source_refs 再读正文（O0）；单文件 lint 的 F2 BROKEN LINK 误报已识别并排除（单文件模式 card_ids 仅含被检文件——双假设实证：lint 报错时先查 lint 源码再下结论）。逐卡详版见各卡「终审记录」节。

**待王语嫣**：抽核 2 张（建议抽 #1 layered-system 与 #4 zhu-time-os——前者是触发卡，后者退回落点特殊=老朱本人）。

---

## 批次记录（第二批 5/5 张 · 2026-08-27 · 欧阳锋）

**进度**：10/10 全部完成（23 条清单去重=10 张），#544 清单全量闭环。取证方式：5 个 explore 子代理并行取证（声称-来源逐条对照）+ 终审抽核 + 机械核查（source_refs 存在性 / pre-submit / check-source-refs.py / 孪生卡 diff）。

| # | 卡 | 结论 | 核心依据 |
|:-:|:--|:--|:--|
| 6 | agent-spec-duanwangye-publisher | **退回（轻量）** | P1×2：§6 成熟度表「反馈收集🔴只有手动」无出处且有反向证据（feedback-improve-flow 实存）；「渠道分发🔴缺决策框架」与源矛盾（channel-distribution.md L1-16 即框架）。P2×2：feishu-publish/SKILL.md 正文调用未入 source_refs；related dk-publish 重复+content-production-polish 死链 |
| 7 | agent-spec-hongqigong-multimodal | **退回** | P1×2：审查署名升格——「欧阳锋 A-」1 域（单元模型）扩成 3 域；讲香「条件通过」抹平为「通过」。P1：L58「唯一视觉出口」引语无出处。P2×3：§9 Hyperframes 口径自相矛盾且滞后/「零失败」出处未入 source_refs/related 重复+死链 |
| 8 | agent-spec-laowantong-producer | **退回** | P1×3：「L9 aliases 源名」与现行 context 矛盾（L9 已重编号为提审即验证流转，aliases 源名是 07-26 旧编号）；aliases 13 条路径片段=#431 A- 扣分项同型复发（F-040 优先）；source_refs 缺 #451 任务单（v1.1 全部新增条款唯一承载文件）。P2×4：§2.6 节名误植/「三证」源为两步/KF-024 扩用/「老朱直令」接口挪用 |
| 9 | dk-publish-collapse-to-iterate | **PASS A-，建议升 reviewed** | 8 取证点 7 证实 1 部分证实；老朱点名引语逐字（corr L13）；七段结构全；related 6/6 无死链。扣分：POSITION_DECLARATION warning 未处置+格式瑕疵。备注：kdo-moc 正文知识网络未列本卡（落点段王爷补登） |
| 10 | skill-duanwangye-prezi | **退回** | P0：source_refs 唯一条目 `capability/duanwangye/prezi` 非仓库路径（check-source-refs.py 实证 missing），真出处（10_raw 王欢源文+infinite-canvas-prezi 包）实存且四张姊妹卡都引了——本卡例外。P1×2：「5种空间结构」无出处且与已审 concept 卡矛盾（源为四种，Z字形无出处）；「delegate_task ✅」虚标（库内知识状态=待验证，diag_20260721:114 原文是疑问句） |

**共性发现 → 建议书动作**：
- `diag_20260826_ouyangfeng-lint-prose-source-refs-blindspot.md` **追加实证**：pre-submit 的 SOURCE_REACHABILITY 对含斜杠的不存在路径也不拦（prezi 卡实测 0 issues），而 `check-source-refs.py` 能检出（refs_missing:1）——检查器存在但未接入 pre-submit 门禁链，盲区比原建议书判定更大
- `diag_20260827_ouyangfeng-agent-spec-twin-drift-reversal.md` **新建议书**：#319 时代「tools/ 版为权威」裁定前提已反转——#472/#475 的 §0 冷启动更新只落在 agent-specs/ 版，tools/ 版落后且 frontmatter 带垃圾 aliases（「态渲染与视觉资产生产引擎」等退化前缀）
- content-production-polish 死链（skill 名当卡 id）两张卡同型，修复随各卡退回执行，不单列

**待王语嫣**：抽核 2 张（建议抽 #7 hongqigong 与 #9 dk-publish——前者署名升格最敏感，后者是本批唯一 PASS，验我放行尺度）。

---

## 执行报告（#544 整单闭环 · 2026-08-27 · 欧阳锋）

- **完成内容**：#527 清单 23 条去重=10 张被依赖 draft 卡全部过审完毕。首批 5 张（08-26）+ 批次二 5 张（08-27）。结论分布：退回 8（含轻量 2）/ PASS A- 1（dk-publish-collapse-to-iterate，建议升 reviewed）/ 豁免 0。逐卡「终审记录」节落卡，两批「批次记录」节落本任务单
- **改动文件**清单：10 张卡终审记录节（30_wiki/ 各卡尾部）；本任务单两批批次记录；建议书动作 3 件（lint 盲区追加实证 + 新建议书 diag_20260827_ouyangfeng-agent-spec-twin-drift-reversal + 首批已落 2 份）；conveyor_probe 回执验证（新建议书可见，total hits 42→43）
- **验证**：source_refs 存在性全量 os.path.exists 实测（35 条引用逐条）；pre-submit 5 卡连跑（PASS 带 WARNING 明细落各卡终审记录）；check-source-refs.py 交叉验证 prezi 卡（refs_missing:1）；孪生卡 diff 实测；5 个 explore 子代理声称-来源逐条取证 + 终审抽核。验证分层：L2（机器核查+子代理取证+抽核，非全量逐字复核源文）
- **未做项**/边界：dk-publish 的 status 翻转（draft→reviewed）不在本单边界（审查批不改卡内容），落点段王爷执行；8 张退回卡的修复复审走各生产者修复后重新提审；孪生卡合并等新建议书待王语嫣裁定
- **需要谁动作**：王语嫣——抽核 2 张（建议 #7 hongqigong 署名升格 + #9 dk-publish 放行尺度）+ 裁定新建议书；段王爷——dk-publish 状态翻转 + kdo-moc 正文补登；老顽童/洪七公/段王爷——各自退回卡按终审记录缺陷点修复复审
