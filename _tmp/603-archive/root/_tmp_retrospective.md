## 概要

今日完成 #166、#167 终审释放；签审并通过 #168A v2.1 方案，批准 A-1 OCR 迁移 apply；随后复验发现 #168A A-2/A-3 仍有残留未清，#168B 老顽童加的 40 条边落在 7 个 YAML 损坏文件里，整体 #168 还不能 close。

---

## 关键决策

| 决策 | 理由 | 结果 |
|:---|:---|:---|
| #166 业务公式教练 agent 迭代 → PASS / A | 六钉全落，单文件改动，pre-submit PASS，边界清晰 | 已 `queue_transition.py review ... --grade A`，状态落盘 |
| #167 C 域审计返工 → PASS / A- | 0 error 达标；剩余 91 warning 中 88 条 lint 行号锚点误报、3 条 OCR 存量；71 文件可归因 | 已 `queue_transition.py review ... --grade A-`，状态落盘 |
| #168A v2.1 方案签审通过 | v1 三处致命错误（A-1 lint 排除 vs 物理迁移、A-2 大小写口径错、A-3 全库 frontmatter 口径错）全部修正 | 签审记录追加到 `90_control/.sandbox/proposal-168A-graph-island-governance.md` |
| #168A A-1 apply 批准 | 184 卡已迁、旧路径 source_refs 已清，但发现 kdo REQUIRED_DIRS 与 60_feedback diagnosis source_refs 两处漏网 | 现场补修 `kdo/templates.py` 与 2 份诊断报告后批准 apply |
| #168A A 段暂不 PASS | 复验发现 1 张 OCR 卡仍有 needs-review、17 张 tool 卡复合 domain 未拆、1 张 AI 簇 concept 仍有 3 条 pending_unknown | 退回黄药师修复 |
| #168B 暂不 PASS | 7 个核心文件 frontmatter YAML 损坏，新边落在非法缩进里，标准解析器读不出 | 退回老顽童修 YAML |

---

## 思维盲点

1. **#168A v1 签审时没先读任务单原文，只看提案就批。**
   - 为什么漏掉：惯性信任黄药师的提案自述，没核对 `task_20260712_wangyuyan-graph-island-governance.md` 里王语嫣“物理移出”的裁定，导致 v1 的“lint 排除”方案差点放行。
   - 后果：v1 被打回，浪费一轮往返。

2. **没第一时间定位到 `kdo/templates.py` 是 REQUIRED_DIRS 的真实配置位置。**
   - 为什么漏掉：搜索范围局限在 `C:/Users/Administrator/Desktop/wiki/` 内，不知道 kdo 包安装在 `C:/Users/Administrator/Knowledge Delivery OS 0.0.1/kdo/templates.py`；黄药师说找不到就信了。
   - 后果：若 A-1 apply 后没改它，`kdo lint` 会报 `30_wiki/raw/ocr: Required directory is missing`，新增 error 归不到任何生产者头上。

3. **对 B 段 `pre-submit 0 warning` 过于信任，没独立用 `yaml.safe_load` 验证 frontmatter。**
   - 为什么漏掉：把 lint/pre-submit 当成充分条件，没意识到它们不抓 YAML 缩进损坏；而图谱解析依赖 YAML。
   - 后果：40 条新边“写进去了但图谱不认”，B 段表面达标实际悬空。

4. **没预料到非 ASCII 文件名会让黄药师的脚本漏扫。**
   - 为什么漏掉：Git Bash 下 `git status` 默认对中文路径做 C-style quoting，之前踩过坑但没形成 checklist，复验时才发现 17 个文件仍在 `yitang- ai-saas` 状态。
   - 后果：A-2 报告“138 次全拆”不实，实际残留 17 次。

---

## 顿悟

1. **`pre-submit PASS` / `lint 0 new error` 不等于变更可被系统正确消费。** YAML 结构合法性、索引覆盖范围、required directory 配置是独立于 lint 的第三道防线，终审必须手动抽查。

2. **迁移类任务的验收必须包含“全库 grep 旧路径”+“required directory 配置”+“所有 source_refs（含 60_feedback/90_control/.agent）”三重校验**，不能只看主目录 `30_wiki`。

3. **对 producer 的 dry-run 报告，必须要求附“被修改文件的完整路径列表”**，纯数字总括不可信——本轮 A-2 的“30 卡/138 次”和实际残留 17 次的差距就是教训。

---

## 过程资产

| 新增/更新 | 路径 |
|:---|:---|
| kdo REQUIRED_DIRS 更新 | `C:/Users/Administrator/Knowledge Delivery OS 0.0.1/kdo/templates.py` |
| 诊断报告 source_refs 更新 | `60_feedback/diagnosis/diag_20260708_yitang-y-model-cross-domain-fusion-deep-dive-v2.md` |
| 诊断报告 source_refs 更新 | `60_feedback/diagnosis/diag_20260709_yitang-expression-pitch-increment-deep-dive.md` |
| #168A 签审记录追加 | `90_control/.sandbox/proposal-168A-graph-island-governance.md` |
| A-2 残留清单 | 17 张 tool 卡（见上文关键决策表） |
| A-3 残留清单 | `30_wiki/concepts/紫鲸ai智能体工作流平台.md`（3 条 `[[pending_unknown]]`） |
| A-1 残留清单 | `10_raw/ocr-cards/ocr-微信图片_20260507004802_38_32.md`（needs-review domain） |
| B 段 YAML 损坏清单 | 7 文件：`framework-一堂五步法-单元模型.md`、`framework-一堂五步法.md`、`tool-一堂五步法-换档检查清单.md`、`concept-yihang-dual-triangle-core.md`、`tool-ai-deliverable-polish-loop.md`、`case-demand-milkshake-jtbd.md`、`case-demand-pharma-bigdata.md` |

---

## 元反思

1. 建立**迁移/批量修改任务终审自检清单**：
   - ① `yaml.safe_load` 抽查被改文件 frontmatter；
   - ② `git -c core.quotepath=false` 列全被改文件路径；
   - ③ 全库 grep 旧路径（含 `60_feedback/`、`90_control/`、`.agent/`）；
   - ④ 检查 kdo `REQUIRED_DIRS` 与相关脚本硬编码路径；
   - ⑤ 申报数字必须附脚本输出原文，不接受总括。

2. 以后遇到“pre-submit 通过但结构可能损坏”的场景，直接跑独立解析器复验，不再假设 lint 已覆盖。

3. 对 producer 的“找不到某配置文件/某文件不存在”说法，要扩展搜索范围到 installed packages 和 `.` 全库，不能仅凭 wiki 内搜索就采信。

---

## Truman复盘

### 逐轮映射

| 轮次 | 人做了什么 | 双三角 | AI做了什么 | 双三角 |
|:---|:---|:---|:---|:---|
| 1 复验 #166 | 读 prompt 第四节/五节/六节/八节，核六钉与 68 个 wikilink 目标 | 体系：核对迭代点是否形成可执行规则 | 跑 `kdo pre-submit`，读取任务单与队列 | 数据：执行门禁与状态查询 |
| 2 终审 #166 | `queue_transition.py review ... --grade A`，追加终审记录 | 决策：单文件、六钉全落给 A | 更新 frontmatter、生成 dashboard | 执行：状态落盘 |
| 3 复验 #167 | 跑 `kdo lint --domain business-formula`，grep index.md 7 卡，读鑫港湾归属说明 | 体系：按审计报告 §六逐项核对 | 跑 lint、统计文件变更、读取 task/frontmatter | 数据：输出指标与文件清单 |
| 4 终审 #167 | `queue_transition.py review ... --grade A-` | 决策：0 error 达标但 warning 未全清，子任务超时扣半档 | 更新队列、任务单、dashboard | 执行：状态落盘 |
| 5 签审 #168A v2.1 | 读 proposal，核对任务单口径，确认三子任务无硬伤后签审 | 审美：识别 v1→v2 的修正质量 | 读取 proposal 与任务单，列出签审记录 | 执行：文本追加 |
| 6 A-1 apply 前补漏 | 发现 kdo REQUIRED_DIRS 与 diagnosis source_refs 两处漏网，现场补修 | 体系：把迁移影响的配置链补全 | 编辑 kdo/templates.py 与两份 diagnosis 文件 | 执行：具体文件修改 |
| 7 A 段复验 | 跑 `yaml.safe_load`、grep 旧路径、扫描 composite domain、AI 簇 pending_unknown | 体系：用独立解析器验证 producer 报告 | 输出残留清单与计数 | 数据：复验报告 |
| 8 B 段复验 | 用 `yaml.safe_load` 扫 56 个改动文件，发现 7 个 frontmatter 损坏 | 审美：识别“边写进去但解析不出”的结构病 | regex 抽 related 确认边存在，但报告 YAML 损坏 | 数据：双向边验证 |

### 飞轮效应

本轮加速了“结构合法性检查”回路：过去只认 lint/pre-submit，现在把 `yaml.safe_load` 和 `core.quotepath` 编码检查纳入终审 checklist。这个回路一旦跑通，后续批量 domain/related/frontmatter 任务的质量会显著提高。

### 对照实验

- **无人协作**：欧阳锋自己要逐一打开 56+ 文件核对，耗时数小时，且容易漏掉 YAML 缩进这种非直观错误。
- **无AI协作**：AI 能跑脚本但不知道项目特定的“物理迁移必须改 kdo REQUIRED_DIRS”“YAML 损坏会导致边悬空”等上下文，会按字面通过。
- **合在一起**：AI 秒级扫描 + 人根据项目知识判定“这 7 个文件必须修”，20 分钟内定位全部残留，质量高于任何一方单独工作。

### 下次改进

- **Agent 自身**：在 review-check.py 或 pre-submit 中增加 `yaml.safe_load` 全量 frontmatter 校验，把本轮人工发现变成门禁自动拦截。
- **方法论卡更新**：建议把“迁移任务终审清单”写入 `system-kdo-quality-gates.md` 或 `agent-native-card-design.md` 的“批量修改任务”一节，固化本次教训。
