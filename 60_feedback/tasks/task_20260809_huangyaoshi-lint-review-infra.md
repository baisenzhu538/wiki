---
id: task_20260809_huangyaoshi-lint-review-infra
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-09
updated_at: 2026-08-09
priority: P1
wsjf: 4.5
claimed_at: 2026-08-09
---

## 执行报告（2026-08-09 黄药师）

### P0-1 四类规则实现 ✅（kdo/workspace.py）
| 规则 | 级别 | 函数 | 命中数（全库基线） |
|:--|:--:|:--|:--:|
| R1-a reviewed 缺 reviewed_by/review_date | ERROR | `_lint_status_review_fields` | 461 |
| R1-b 重复节名 | ERROR | `_lint_duplicate_section_names` | 37 |
| R1-c 仓库外路径 | WARNING | `_lint_source_refs_location` | 10 |
| R1-d 行号超界 | WARNING | `_lint_source_refs_line_range` | 0（708 个带行号 ref 全界内，#257 已修 #250 L54） |

### P0-2 每类 ≥2 测试 ✅（tests/test_workspace.py TestLintR1ReviewInfra，9 用例）
- R1-a：缺 reviewed_by ERROR / 缺 review_date ERROR / 完整字段无 ERROR
- R1-b：重复节 ERROR（含节名断言）/ 无重复无 ERROR / frontmatter 键不算重复节
- R1-c：桌面绝对路径 WARNING / 仓库内相对路径无 WARNING
- R1-d：行号超界 WARNING / 界内无 WARNING / **中文路径+空格 L 前缀格式 WARNING**（正则修复验证）

### P0-3 基线报告 ✅
`60_feedback/diagnosis/baseline_20260809_huangyaoshi-lint-r1.md`（含可复现命令 + 清扫任务清单 P1-2）

### P1-1 登记 ✅
- cap_hub features.json：新增 `R1_REVIEW_INFRA`（15 Feature）
- `40_outputs/code/scripts/README.md`：新增"Lint 审查基建 R1 四类规则"节

### 测试验证
- tests/test_workspace.py：47 passed（含 9 个新 R1 用例）
- lint 相关文件（workspace/validate_deep/index_wikilink）：76 passed
- 全量：560 passed / 1 failed（**预存在** Windows smoke test GBK 编码问题，08-05 复盘已记录，非本次引入）

### 顺手修复（范围外，已声明）
- `kdo/commands/delivery.py` `_layer_priority`：graph/BM25 返回 Path 对象时 `"domains/" in path_str` 类型错误（2026-06-29 引入的预存在 bug）——加 `str()` 防御。修复后 smoke test 失败点从类型错误推进到 GBK 解码（预存在环境问题）。

### 遗留（P1-2 清扫任务，另排）
- R1-a 461 张待批量补终审标记（git 追溯 + review_mark.py）
- R1-b 37 张待人工合并重复节（建议老顽童，ai-virtual-coach-prompt 单卡 3 处）
- R1-c 10 张待素材入仓改相对路径

## 终审记录（2026-08-09 欧阳锋）

**verdict: PASS A · blocking: 无 · methodology v2.2**

O3 独立验证全部通过（六项交叉）：
1. **数字独立复现**：照基线报告复现命令实跑全库 → R1-a 461 / R1-b 37 / R1-c 10 / R1-d 0，与执行报告+基线报告逐字一致
2. **源码存在**：workspace.py L1026-1029 四规则调用 + L1427-1519 定义
3. **测试实跑**：TestLintR1ReviewInfra 11 passed（超声明 9 个——R1-d 中文路径正则修复补测，覆盖 R1-a 缺字段×2/完整 / R1-b 重复节/无重复/frontmatter 键不算 / R1-c 桌面路径/仓库内 / R1-d 超界/界内/中文路径）
4. **抽查命中非误报**：R1-a 样例 bridge-dual-track-feature-system.md（status: reviewed 确缺 reviewed_by/review_date）；R1-c 样例 case-yitang-yai-conversion-rate-visit-rate.md（source_refs 确指 Desktop/YAI/ 仓库外）
5. **登记**：cap_hub features.json R1_REVIEW_INFRA + scripts README "Lint 审查基建 R1 四类规则"节
6. **清扫清单**：baseline 报告含 R1-a 461 补标记 / R1-b 37 人工合并（老顽童）/ R1-c 10 入仓

评价：R1-d 0 命中诚实定位为"防增量规则"而非凑数（P-33 诚实原则）；顺手修复 _layer_priority 范围外已声明（P-10 合规）；R1-a 461 是历史审查流程缺口量化——清扫任务另排（建议王语嫣编排，优先于新批次）。**E012 的机器化防线正式上线：'reviewed 无终审记录 = lint ERROR'从此是代码门禁而非人工检查。**

五维：溯源 95/逻辑 95/暗知识 85/可操作 95/表达 90 → 总分 93（A）

# kdo lint 审查基建扩充（#271 · 欧阳锋建议书 R1）

## 任务目标

把欧阳锋反复用人工 grep 查的三类结构问题固化为 lint 规则（每类 ≥2 次实证教训）：

| 规则 | 检测内容 | 实证教训 |
|:--|:--|:--|
| R1-a | `status: reviewed` 但缺 `reviewed_by` 或 `review_date` | E012 三批 19 张（#230/#231/#232）——PASS 后卡片仍 draft |
| R1-b | 重复节名检测（两个 `## Critique` / `## 失败模式`） | E009（#214 case-cui-lei 误改） |
| R1-c | source_refs 路径存在性（仓库内 00_inbox/10_raw/60_feedback；桌面/仓库外 = 违约） | 08-07 复盘：tool/agent-spec 指向桌面路径 git 无法追溯 |
| R1-d | source_refs 行号范围校验（行号 > 源文件总行数 → WARNING） | #213 批 / #250 L54 旧行号残留 |

## 验收标准（沿用欧阳锋 v2.2 四节协议）

【P0/P1 清单】P0-1 四类规则实现（R1-a ERROR / R1-b ERROR / R1-c WARNING / R1-d WARNING）；P0-2 每类 ≥2 测试（正例+反例）；P0-3 全库基线报告（命中数可复现——独立跑一遍得到相同数字）。P1-1 登记 README + cap_hub；P1-2 全库历史违规清零或产出清扫任务清单
【字段级定位】kdo lint 源码 rules 模块 + 测试文件
【证据】错误模式库 E009/E012 / 08-07 技能进化日志 source_refs 规范
【期望形态】`kdo lint` 输出含新规则名与命中列表；pytest 新增用例全绿；基线报告可复现

## 依赖与前置

- 无依赖，可立即开工（黄药师当前无阻塞任务）
- **前置价值**：R1 的 lint 规则是 #273 skill eval 的确定性检查器（回归 eval baseline 对比的基础）

## 参考素材

- 欧阳锋建议书：`70_product/tasks/proposal-review-infra-v22-2026-08-09.md` §二
- `90_control/tool-card-excellence-standard.md`
- 停车场条目 R4（source_refs 存在性校验，已挂）

## 边界

- 只加 lint 规则，不动其他 lint 逻辑
- 历史违规清零动作按基线报告另排（P1-2 产出清单即可）
