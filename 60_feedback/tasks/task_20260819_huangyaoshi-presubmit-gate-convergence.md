---
id: 377
assignee: kimi-huangyaoshi
status: in_progress
updated_at: '2026-08-19T14:09:45.807219+00:00'
title: 双 pre-submit 门禁收敛（P2，王语嫣
priority: P2
dependency: []
code_files:
- 90_control/scripts/pre_submit.py
---

# #377 双 pre-submit 门禁收敛（P2）

## 任务目标

诊断并收敛两套同名门禁：`kdo pre-submit`（KDO CLI，L4 纪律法定）vs `90_control/scripts/pre_submit.py`（wiki 侧）。同一批卡两套门禁结论相反，迟早误杀好卡或放过坏卡。

## 背景证据（王语嫣 2026-08-19 实测）

- #376 二刷新卡 13 张：`kdo pre-submit` **PASS**（YAML/WIKILINK/DOMAIN/DK_SECTION 等全 0）；`90_control/scripts/pre_submit.py` **FAIL 13/13**，唯一报错=`source_refs WARN: points to 00_inbox/ not 10_raw/sources/`
- 一刷 21 张已终审卡（dk-model-demystification、framework-knowledge-compound-rocket-six 等）跑 wiki 侧脚本**同样全 FAIL**——同规则
- 即：wiki 侧门禁把一条 WARN 级惯例（source_refs 应指 10_raw/sources/）提升为 ERROR，而全库该素材批次的卡（含欧阳锋已终审 PASS A 的）都违反它

## 执行范围

1. **规则差异诊断**：两套门禁各自检查项全清单对齐，列出所有规则分叉点（不止 source_refs 一条），落诊断表
2. **source_refs 规则专项裁决准备**：回答"00_inbox 素材是否应迁 10_raw/sources/"——若规则有真实价值（素材存放结构问题），则存量卡批量修复属**另立项**范畴，本任务只出建议不动卡；若规则过时，给出降级/删除方案
3. **收敛执行**：以 `kdo pre-submit` 为唯一法定门禁（L4 口径），wiki 侧脚本二选一——对齐 CLI 规则，或文件头标注 deprecated + 指向 CLI。收敛后同一批卡（13 新 + 21 基线抽样 5 张）双跑结果一致
4. 改动限 `90_control/scripts/pre_submit.py` 及必要文档（agents/agent-os.md L4 表述若需澄清，列建议由编排裁决）

## 边界

- 不动任何卡片正文/frontmatter（存量 source_refs 修复若要做，另行立项）
- 不动 KDO CLI 仓（`C:\Users\Administrator\Knowledge Delivery OS 0.0.1\`）——若诊断结论是需要改 CLI 侧，列建议报编排裁决
- 收敛方案涉及"素材存放结构"（00_inbox vs 10_raw PARA 纪律）的判断先报裁决再动手

## 内容价值判断（PROTOCOL §7 合规声明）

- 本任务只改门禁脚本与文档，不删除/移动任何素材与卡片
- 批量三问：改门禁后全库影响面用 dry-run 对比（改动前后各跑抽样批），预期范围声明，非空值不覆盖

## 验收标准

1. 两套门禁检查项差异表（全量，非仅 source_refs）
2. 收敛后同一抽样批（13 新卡 + 5 基线卡）双跑结果一致，或 wiki 侧已标 deprecated 不可误用
3. source_refs 规则去留结论 + 依据（另立项建议或规则降级）
4. 无卡片/素材被改动

## 交付

1. 诊断表 + 收敛后的脚本/标注 + 双跑对比实测
2. 送欧阳锋终审

---

# 执行报告（黄药师 2026-08-19）

## 一、根因诊断（先说机制）

`90_control/scripts/pre_submit.py` 不是独立门禁——它是 `90_control/scripts/kdo_lint.py --incremental` 的**包装器**（只过滤申报文件的 `[ERROR]` 行）。所以真实分叉点是两套规则引擎：**kdo_lint.py（wiki 侧）vs kdo CLI pre_submit（法定）**。

关键缺陷实锤（kdo_lint.py L191-195）：00_inbox 规则的**消息文本写着 "WARN"，但被 append 进 errors 列表**——lint 输出全部为 `[ERROR]` 前缀。王语嫣看到的 "FAIL 13/13" 是这条伪 WARN 真 ERROR 规则触发。

## 二、规则差异全量表

| 规则 | kdo_lint.py（wiki 侧） | kdo pre-submit（CLI 法定） | 分叉 |
|:--|:--:|:--:|:--|
| frontmatter/YAML 可解析 + 必填字段 | ✅ schema | ✅ yaml+frontmatter_metadata | 近似（枚举表各自维护） |
| updated_at 必填（F1） | ✅ | ❌ | **lint 独有** |
| wikilink 断链（F2） | ✅（含回链检查） | ✅（仅解析，无回链） | 口径差异 |
| 重复 ID（F3） | ✅ | ❌ | **lint 独有** |
| MOC 死链（F4） | ✅ | ❌ | **lint 独有** |
| dk 七段（DK_SECTION） | ✅ | ✅ | 一致 |
| section 拼写（SECTION_TYPO） | ✅ | ✅ | 一致 |
| **source_refs 指向 00_inbox** | ✅ **文本写 WARN 实为 ERROR** | ❌（_check_source_reachability 只验存在性） | **实战唯一触发分叉** |
| source_refs 文件存在性 | ✅ | ✅（diagnostic 不拦截） | 级别差异 |
| frontmatter 重复键（DUPLICATE KEY） | ✅ | ❌ | **lint 独有** |
| 写审分离（author==reviewed_by 拦截） | ✅ | ❌ | **lint 独有** |
| R6 搜索可达性（title/aliases） | ✅ | 部分（aliases_has_source_name） | 口径差异 |
| domain 合法 fuzzy | ❌ | ✅ | CLI 独有 |
| 重复 section / outlinks / position 声明 | ❌ | ✅ | CLI 独有 |
| 质量预评分 / 索引新鲜度 | ❌ | ✅（diagnostic / 今日新增门禁） | CLI 独有 |

## 三、复现实测（13 新卡 + 5 基线卡双跑，2026-08-19）

- wiki 侧：❌ FAIL，20 条 ERROR——**全部是** source_refs→00_inbox 一条规则，且全部落在基线卡（framework-knowledge-compound-rocket-six / framework-serendipity-five-channels / tool-wechat-transcript-automation-workflow；含欧阳锋已终审 PASS A 的卡）
- CLI 侧：✅ PASS（18 卡全过，含今日新增的索引新鲜度门禁）
- 与王语嫣 #376 证据一致，现象复现

## 四、收敛执行

**决策：wiki 侧包装器标 deprecated**（不对齐）。依据：
1. 对齐 = 永久维护两套规则引擎，E034（副本漂移）必然重演
2. L4 纪律法定门禁本来就是 `kdo pre-submit`；agents/agent-os.md L388 的表述已指向 CLI
3. 包装器无独有能力（manifest/增量过滤 CLI 的 --files/--batch 都覆盖）
4. 全库无自动化调用该脚本（grep 全库仅历史任务单提及，零活引用）

已执行：`90_control/scripts/pre_submit.py` 文件头 + 运行时 stderr 双重 DEPRECATED 标记，指向 `kdo pre-submit`；脚本保持可运行（不破坏历史追溯），但其结果不再作为交卷依据。

## 五、source_refs→00_inbox 规则去留结论（报编排裁决，未动卡）

**我的结论：该规则与现行铁律冲突，建议删除或降为真 WARN。**

依据链：
1. 规则注释自承"#214 P0 任务单边界未完成"——是个未完成的过渡措施
2. 2026-08-17 用户拍板铁律：**新内容第一站必须是 00_inbox/**，未经处理不入 10_raw——偶遇采集管线的 case 卡 source_refs 合规地指向 00_inbox/wechat-collect/（本场的 case-wechat-* 都是）
3. 该规则以 ERROR 级拦截，会把所有遵守新铁律的卡误判 FAIL——**规则惩罚的恰恰是合规行为**
4. "素材是否应迁 10_raw"是 PARA 存放结构判断——按任务边界，报裁决不定案

若裁决要保留该意图，建议形态：降为真 WARN（不进 errors 列表），且只对新卡生效（存量豁免）——但这属于 kdo_lint.py 的改动，本任务未执行。

## 六、验收对照

| 验收标准 | 结果 |
|:--|:--|
| ① 差异表全量（非仅 source_refs） | ✅ §二，14 项规则逐项对比 |
| ② 双跑一致或 wiki 侧标 deprecated | ✅ deprecated 双标记（文件头+运行时），抽样批 CLI 侧 18/18 PASS |
| ③ source_refs 规则去留结论+依据 | ✅ §五（建议删除/降真 WARN，报裁决） |
| ④ 无卡片/素材被改动 | ✅ 只改 `90_control/scripts/pre_submit.py` 一个文件（git diff 可证） |

## 七、留裁决事项

1. source_refs→00_inbox 规则去留（建议删/降 WARN，见 §五）
2. kdo_lint.py 的"文本 WARN 实为 ERROR"误标问题——lint 输出分级体系建议另立项（lint 本身仍有 F1-F4 等 CLI 没有的规则，lint vs pre-submit 的关系也值得一并定义）
