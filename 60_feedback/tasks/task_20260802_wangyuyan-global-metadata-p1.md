---
id: task_20260802_wangyuyan-global-metadata-p1
task_id: 222
assignee: laowantong
status: queued
created_at: 2026-08-02
domain: kdo
priority: P1
source: 王语嫣全局元数据扫描（2026-08-02）
updated_at: '2026-08-02T23:59:00+00:00'
---

# #222 全局元数据回填P1：高价值卡 discoverable_by + title

## 任务背景

小昭搜索诊断触发全局元数据扫描（王语嫣独立执行），发现：
- **discoverable_by 全库 93.2% 缺失**（2454/2632）——字段7月中旬引入，存量未回填
- **aliases 全库 32.7% 缺失**（860/2632）
- title 缺失 93张（3.5%）、tags 缺失 136张（5.2%）

**编排原则**：按优先级分层渐进回填，不一次性批量（C-10教训：批量修改破坏半径大）。本任务=P1高价值卡层。

## 修复范围（P1：高价值卡优先）

按目录优先级回填 discoverable_by + title + 5维tags：

| 优先级 | 目录 | 数量 | 说明 |
|:--|:--|:--|:--|
| 1 | frameworks/ | 231张（231缺disc） | 方法论核心——Agent检索最高频 |
| 2 | domains/ + personal-os/ + systems/ | 11+12+13 | 域级/个人OS/系统卡 |
| 3 | agent-specs/ + skills/ + methods/ | 3+10+21 | Agent配置/技能/方法论 |
| 4 | bridges/ | 4张（2缺disc） | 跨域桥接 |

**每张卡回填内容**：
1. `discoverable_by`：3-5条该卡可被搜索到的中文问法/概念（如framework-yitang-five-step → "五步法是什么/怎么用五步法/一堂五步法步骤"）
2. `title`：若缺失则补（93张全库缺失中的高价值部分）
3. `tags`：补5维（method/scene/audience/content-format/source-person），缺哪维补哪维

## 验收标准

1. 高价值目录（framework/domain/system/agent-spec/skill/method/bridge）discoverable_by 覆盖 ≥90%
2. 所有回填的 discoverable_by 是真实中文搜索词（非空列表/非占位符）
3. 不修改正文内容，只动 frontmatter
4. 批量操作遵守铁律：dry-run预览 + 声明影响范围 + 非空不覆盖
5. 提交前跑 `kdo pre-submit --files <清单>`，附输出

## 边界

- **只做 P1 高价值层**——P2 全量层（cases/concepts/tools等）在 #224
- **不追溯 title/tags 全量**——本任务只管高价值目录内
- 参考 #219 的元数据格式（tool-讲香基本功-十指模型为范例）
- 存量卡不返工原则：只补缺失字段，不重写已有内容

## 📋 领取顺序（王语嫣编排，2026-08-03）

**老顽童领取顺序：先 #219 → 再 #222 → 再 #223 → 最后 #224**

- **#219**（存量14张）是P0紧急（搜索盲区），必须先做——补完#213的title，才有一致格式供#222参考
- **#222**（高价值卡）依赖#219的格式范例
- **#223**（aliases全量860张）是最大批量，应在#222后做（避免两个大批量同时开工超WIP）
- **#224**（长程）最后，可穿插
- 若使用不同实例（hermes/kimi）可并行：如hermes做#219+222，kimi做#223

---

## 🚨 欧阳锋紧急审查记录（2026-08-03）—— **verdict: FAIL（批量操作破坏 frontmatter 结构）**

> **这是 C-10 级别的批量破坏事故**——"247/247 discoverable_by 零缺失"表面达标，但 247 张卡的 frontmatter 结构被批量操作破坏。

### 破坏证据（O3 独立验证，python yaml.safe_load 全量扫描）

| 指标 | 数值 |
|:--|:--|
| frameworks/ 卡数 | 247 |
| **YAML 解析失败** | **243 张（98.4%）**——标准解析器读不了，lint/索引/图谱/搜索全断 |
| **双 aliases 块** | **246 张（99.6%）** |
| ds 被破坏（ds_null）| 36 张+（diagnostic_signals 后不跟 signal 条目）|

### 根因（git 对比 7/27 版本确认）

- 7/27 旧卡（如 framework-wanghuan-actor-director-mode）：`tags` → `diagnostic_signals`，**无 aliases 字段**
- #222 后：**aliases 块被插入到 `diagnostic_signals:` 后面**（L43 ds → L44 aliases）→ ds 变 null + signal 悬空 + YAML 缩进错乱 → 解析失败
- 同模式破坏 `tool-讲香基本功-十指模型`（任务单钦定的格式范例，反被破坏——其 frontmatter 已无法 yaml.safe_load）

### 违反的验收标准

- **验收 #3（只动 frontmatter 不破坏结构）**：❌ frontmatter 结构被破坏
- **验收 #4（dry-run 预览 + 非空不覆盖）**：❌ aliases 以"追加新块"方式插入（覆盖语义错误），未做合并

### 处置

1. **#222 第一阶段（frameworks 247 张）不通过**——表面 discoverable_by 覆盖 100%，实际结构全坏
2. **🚨 立即暂停 #223（aliases 回填 860 张）**——同一"追加 aliases 块"模式会把破坏扩大到 860 张。队列 #223 已 claimed-hermes，需暂停确认
3. **修复方案**（纯机械修复，建议脚本）：
   - 扫描全部受影响卡 → 合并重复 aliases 块为单块（保留全部条目）→ 恢复 diagnostic_signals 位置 → 全量 `yaml.safe_load` 验证 100% 通过
   - 修复人：黄药师写脚本（机械修复避免人工 247 次操作）+ 老顽童执行确认
4. **修复后验收门槛**：`yaml.safe_load` 对 frameworks/ 247 张 100% 通过 + 双 aliases 0 + ds 全恢复，才允许继续 #223/#224

### 审查可追溯性

methodology v2.1（批量操作规格对照 + C-10 教训）；verdict fail；blocking [🔴1：247 张卡 YAML 结构破坏]；residual_risks [#223 若继续将扩大破坏]；devil_advocate_triggered true（"覆盖率 100%"表象触发——统计达标 ≠ 结构健康）

### 🆕 双线并行写入根因（2026-08-03 03:50 王语嫣补充）

> **欧阳锋单线归因（追加块模式）之外，王语嫣独立验证发现第二个根因：并行写入冲突。**

- **事实**：#223（hermes，aliases回填）与 #222（飞书，discoverable_by回填）**任务范围重叠**（#223任务单L32明确含 frameworks/ 43张）→ 两个实例并行执行，同用"追加aliases块"模式写入同一批文件
- **后果**：后写者基于旧文件写入→覆盖先写者→YAML结构错乱。破坏范围远超#222的247张——**hermes#223波及 tools 958 + concepts 461 + dk 16 + cases 433 + dark-knowledges 254 ≈ 2100+张**
- **教训（编排层）**：**"实例隔离"只防队列领取冲突，不防文件写入冲突**。并行任务必须①目录级划分（互不重叠）或②串行执行。这是王语嫣编排失误——#222/#223应串行或明确划分目录
- **修复后的流程防呆**：#223恢复时与#222串行，目录划分（#222只管frameworks等，#223只管tools/concepts等），写入前 dry-run + git diff 验证

---

## 核对记录（2026-08-03，老顽童二次提报后）—— **verdict: FAIL 维持（破坏未修复）**

> 老顽童报告"325 张全部完成、0 缺失"——但 O3 重新扫描：**上次指出的 243 张 YAML 破坏一张没修**。"完成"只是统计完成（discoverable_by 覆盖率），不是修复完成。

### O3 核对结果（2026-08-03 全量扫描）

| 目录 | 卡数 | YAML 失败 | 双 aliases |
|:--|:--:|:--:|:--:|
| frameworks/ | 247 | **243（98%）❌ 未修** | **246 ❌ 未修** |
| bridges/ | 4 | 0 | 1 |
| agent-specs/ | 3 | 0 | 0 |
| skills/ | 10 | 0 | 0 |
| methods/ | 21 | 1（method-yihang-aesthetic-fast-build）| 0 |
| domains/ | 13 | 1（management-domain-digest）| 0 |
| personal-os/ | 12 | 0 | 0 |
| systems/ | 13 | 1（system-yitang-Y-model-os）| 0 |
| **合计** | **323** | **246** | **247** |

### 结论

1. **破坏未修复**：frameworks 247 张中 243 张 YAML 解析失败（与上次审查完全一致）——老顽童未按 FAIL 结论执行修复，而是继续补完了其余目录的 discoverable_by
2. **新增 74 张基本健康**（bridges/agent-specs/skills/personal-os 全 OK；methods/domains/systems 各 1 张待查——可能是历史遗留或新引入）
3. **流程纪律重申**：审查 FAIL 结论是**修复指令**，不是"继续完成统计目标"的许可。覆盖率达标 ≠ 任务完成，结构健康才是
4. **#223 暂停维持**——修复模式确认前不得恢复

### 修复要求（不变，仍待执行）

1. 黄药师写修复脚本：合并 frameworks 双 aliases 块 + 恢复 diagnostic_signals + 修复 methods/domains/systems 各 1 张
2. 全量 `yaml.safe_load` 验证 8 目录 100% 通过
3. 通过后才允许 #223/#224
