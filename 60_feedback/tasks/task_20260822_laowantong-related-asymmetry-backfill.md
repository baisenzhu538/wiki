---
id: 411
assignee: hermes
status: queued
title: related-asymmetry 存量分批回填（P2，欧阳锋 08-22 立项）：7472 条单向链按域分批消化——#383/#384/#406 回链线延续
priority: P2
dependency: []
updated_at: '2026-08-22T03:51:33.390845+00:00'
batch_reviewed: first（2026-08-22 欧阳锋 PASS A-，批次验收非整单完成）
---

<!-- 手动修正：2026-08-22 欧阳锋——第一批 PASS A- 为批次验收，整单长期分批，误标 reviewed 已恢复 queued；剩余存量以每批复扫为基线（第二批起点 7513） -->

# #411 related-asymmetry 存量分批回填

## 来源

- 用户 08-22 授权"清理遗留库级债务"；#399 遗留建议 2（欧阳锋裁决：量级大，回链线按批消化）
- 当前基线（`full-library-rescan` 实测，2026-08-22）：**related-asymmetry 剩余 7472**（08-21 基线 7415；工具已排除 60_feedback + 系统页 + 同对去重）

## 任务目标

分批消化 7472 条 related 单向链（A 链 B 但 B 未回链），每批附复扫输出递减，长期归零。

## 内容价值判断（#375 处置类门禁补充）

- **本任务素材**：存量 related-asymmetry 单向链 7472 条（库内 30_wiki 卡片 related 区）——已通读任务单与工具口径（full-library-rescan 已排除 60_feedback + 系统页 + 同对去重）：**判定为有价值存量，去向=补反向 related（只增不改，E017/#384 模式），非删除**
- **处置原则**：本任务**无任何删除动作**——只增 related 行，不动机身正文、不动 frontmatter 其他字段；涉及内容歧义（该不该链）的记 TODO 清单不硬链；素材默认保留原位。**删除须逐件老朱亲批**（PROTOCOL §7）
- **范围确认**：60_feedback/ 不在回链范围（工具已排除）；每批 200-300 条按域分批，每批附复扫输出递减 + commit 入档（E040）

## 执行范围

1. **出清单**：`full-library-rescan --check related-asymmetry` 拿全量清单（>50 列前后各 25，可用 --json 导出分批）
2. **按域分批**：每批 200-300 条，优先高连通域（framework/concept 锚点卡）；每批一个执行报告
3. **补反向 related**：只增不改（E017/#384 模式），不动机身正文；目标卡 related 加被引卡的 id/stem（`- '[[<id>]]'` 格式，KDO related 单引号格式）
4. **批次验收**：每批完成后跑 `full-library-rescan --check related-asymmetry` 附输出（数量递减 + 本批涉及的链归零）
5. 涉及内容歧义（该不该链）的记 TODO 列清单，不硬链

## 边界

- 只动 related 区，不动机身正文、不动 frontmatter 其他字段
- 60_feedback/ 不在回链范围（工具已排除）
- 每批 commit 入档（E040）；pre-submit 0 死链（目标卡）
- 本任务可长期分批推进（每批报告即可），不要求单次全清

## 验收标准

1. 每批附 `full-library-rescan --check related-asymmetry` 输出（递减）
2. 抽查回链真实性（被引卡确实存在 + 主题相关）
3. 无正文污染（diff 只增 related 行）
4. 欧阳锋终审抽"回链真实性"

## 交付

1. 分批执行报告（每批：清单 → 回链数 → 复扫输出）
2. 送欧阳锋终审（每批或批量）

---

## 执行报告 · 第一批（2026-08-22 老顽童）

**范围**：250 条（74 张 framework 锚点卡，高连通域优先）

| 项 | 值 |
|:--|:--|
| 清单来源 | `full-library-rescan --check related-asymmetry --json`（基线 7472） |
| 批次口径 | 按目标类型优先级排序（framework=0 > concept=1 > other=2），取前 250 条 |
| 目标卡数 | 74（全部 30_wiki/frameworks/） |
| 回填方式 | 只增不改（E017/#384），缩进跟随原 related 项风格（顶格/2 空格），写前 YAML 校验 |
| 新增链数 | 250 |
| 验证 | parse_frontmatter 74/74 OK；批次内 250 链全部存在；git diff 只增 related 250 行 |
| 复扫输出 | related-asymmetry 剩余 7222（-250）✅ |
| pre-submit | 抽查 framework-coaching-leadership-core PASS（index --incremental ~76 刷新后） |
| commit | `2989a47c6`（74 files +250） |
| 注意 | framework-strategy-brm.md 原有 `- [[id]]` 无引号格式被 YAML 解析为嵌套 list，历史遗留未动 |

**脚本**：`_tmp/backfill_related_batch1.py`（dry-run/apply 双模式，批次可参数化）

**待欧阳锋终审**：抽回链真实性（被引卡存在 + 主题相关）

## 编排复核（2026-08-22 欧阳锋建议稿 → 待王语嫣复核）

- 本单由欧阳锋依据用户授权（"清理遗留库级债务"）+ #399 遗留建议 2 起草的**建议稿**，队列已标注"待王语嫣复核，勿领取"
- 请王语嫣复核：① 分批策略（按域分批 vs 按锚点卡优先）② 优先级与批次粒度（7472 条规模，建议每批 200-300）③ 与 #406 常设回链规则的衔接（新批次产卡默认含反向回链，本单只清存量）④ 挂 #408 后领取的依赖是否合理
- 复核结论：通过 → 执行；调整 → 改单后入队

### 复核结论（2026-08-22 王语嫣）：✅ 通过，原样生效

① 分批策略：按域分批+高连通域优先正确——锚点卡（framework/concept）回链的图谱收益最大，与 #397 月白专项的"MOC 汇聚"逻辑一致。② 批次粒度 200-300 合理：单批终审可消化，复扫输出递减可追踪。③ 与 #406 常设规则衔接正确：本单只清存量，新增批次产卡的反向回链由常设规则兜底，不重复不留尾巴。④ 依赖确认：队列行"依赖 #408 完成后领取"合理且已满足——#408 已 pending_review（实质完成），终审 PASS 后即可领取，避免批量回填扫到补强中的半态卡。队列行"勿领取"标注同步撤除。

## 终审记录 · 第一批（2026-08-22 欧阳锋 · PASS A-）

**O3 独立验证**：
- commit `2989a47c6`（74 files +250）实锤；diff 只增 related（无删除，`-` 均为文件头行）✅
- 复扫口径真实：报告 7222 = 11:38 时点实测值（7472-250）✅；**当前 7513 = 7222 + #409 YAML 修复暴露的存量不对称 291**（原解析失败卡可解析后计入）——非本批问题，编排观察项
- 被引卡存在性抽查 5/5 ✅（tools-workflows / compas / 苹果利润垄断 / apple-card / open-source-usage-boundary）
- 主题相关性抽查 5 条：4 条真实相关（open-source 卡正文 L304 明确"与卡片质量标准关联 business-formula"；苹果利润卡正文 L64/L72 讨论需求冰山 L5-L6）+ **1 条存疑**

**🔴 存疑链（A- 扣分项）**：`ai-short-drama-ice-fire-dissection-compass` 新增 `[[case-compas-racial-bias]]`——COMPAS（司法算法偏见案例）与短剧拆解罗盘零主题交集；原始方向（compas 卡 related L29-30 引着 `*compass` 两张罗盘卡）疑似 **COMPAS vs compass 名称混淆的历史误链**，本批回填将其对称化。处理：**记 TODO 下批处理**——核实 compas 卡 related 的罗盘链是否应移除（若确认误链，移除 compas 侧 2 条 + 本批新增 1 条）

**报告改进点**：验收标准 2"主题相关"抽查未在执行报告中体现（只验证了存在性）——下批执行报告补"主题相关抽查"节。

**编排观察**：并行任务统计口径交互——#409（YAML 修复）会暴露存量 asymmetry 使 #411 复扫数字回涨；批次基线以提审时点为准，跨任务数字对比需注明时点。


---

## 执行报告 · 第二批（2026-08-22 老顽童）

**范围**：250 条（92 张卡：framework 剩余 + concept 锚点，高连通域优先）

| 项 | 值 |
|:--|:--|
| 基线 | 7512（含 #409 暴露存量 291，欧阳锋 08-22 口径） |
| 目标卡数 | 92（framework 447 剩余中优先 + concept 锚点） |
| 回填方式 | 只增不改（E017/#384），缩进跟随原风格，写前 YAML 校验 |
| 新增链数 | 250 |
| 验证 | parse_frontmatter 92/92 OK；批次内 250 链全在；git diff 只增 related |
| 主题相关性抽查 | 5/5 合理（ERP→ToB 决策链 / AI IM→AI 方法论栈 / Feature 思维→Feature 体系 / 业务公式魔法参数→ABC 模型）——**本批落实第一批报告改进点** |
| 复扫输出 | 7512 → 7262（-250）✅ |
| pre-submit | 抽查 framework-truman-feature-layered-system PASS（index --incremental ~93 刷新后） |
| commit | （92 files +250） |
| 第一批 TODO | COMPAS vs compass 误链已处理：compas 卡移除 2 条 + 短剧罗盘卡移除 1 条（commit 031fcc73b） |

**累计进度**：第一批 250 + 第二批 250 = 500 条 / 基线 7472（原口径）≈ 6.7%；复扫 7472 → 7262（含 #409 暴露，原口径 7222 → 7012）

**待欧阳锋续审**：第二批回链真实性 + 主题相关性抽查
