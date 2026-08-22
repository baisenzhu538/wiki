---
id: 409
assignee: huangyaoshi
status: queued
title: 库级 YAML 修复（P2，欧阳锋 08-22 立项）：parse-error 58 张 YAML 结构损坏修复——#373 同类，不伪装归零
priority: P2
dependency: []
code_files:
- 90_control/scripts/full-library-rescan.py
updated_at: '2026-08-22T03:52:42.698942+00:00'
---

# #409 库级 YAML 修复（parse-error 58 张）

## 来源

- 用户 08-22 授权"清理遗留库级债务"；#399 遗留建议 1（欧阳锋裁决：YAML 损坏修复单独立项）
- 当前基线（`full-library-rescan` 实测，2026-08-22）：**parse-error 剩余 58**（08-21 基线 61，master-moc 编码修复后下降）
- 错误模式：`YAML parse error: while parsing a block mapping / expected <block end>, but found '-'`——frontmatter 列表块（related/source_refs 等）结构坏，与 #373 已知编码损坏同族

## 任务目标

修复全库 58 张 YAML 结构损坏卡，使 `full-library-rescan --check parse-error` 归零。**修复前任何"归零"声明须附该工具输出（#399 纪律），解析失败卡显式列清单，不伪装归零。**

## 执行范围

1. **先出清单**：`full-library-rescan --check parse-error` 拿全量 58 张清单（已确认样例：case-strategy-* 6 张 / concept-smart-medicine-cabinet-* 6 张 / ai-native-im-multi-agent / concept-kdo-review-workflow / graph-rag / fd-forward-deployment 等）
2. **逐张修复**：yaml 级解析定位坏块（缩进/列表结构），**只修结构不改变内容语义**；每张修复后 yaml.safe_load 通过 + `kdo pre-submit` 抽检
3. **归零验收**：`full-library-rescan --check parse-error` → 剩余 0（附输出到执行报告）
4. **回归确认**：修复后 `kdo index --rebuild` 索引文件数对比（58 张修复前后索引覆盖）

## 边界

- **不动 00_inbox 素材层**（素材只读纪律；该层 GBK 文件另议）
- 不改变卡内容语义——纯结构修复；涉及内容歧义无法机械修复的，列清单退回（写清卡名+位置+原因，给生产者）
- 修复后 commit 入档（E040）
- 交付物涉及 90_control 工具改动（如需升级扫描器容错）按 code_files 声明跨仓路径（#380 门禁）

## 验收标准

1. `full-library-rescan --check parse-error` = 0（**附工具输出**，归零声明纪律）
2. 抽查修复卡：yaml 可解析 + 内容语义无改动（diff 对比仅结构变化）
3. 修复前后清单差异有说明（58 → 0 的路径）
4. 欧阳锋终审抽"修复真实性"（是否真的 yaml 级修复而非绕过/删除字段）

## 交付

1. 执行报告：修复前清单 → 逐张修复说明（或退回清单）→ 归零工具输出
2. 送欧阳锋终审

## 执行报告（#409 黄药师 · 2026-08-22 · 终审 FAIL 补件）

### 1. 归零工具输出（#399 纪律）

```
[full-library-rescan] 全库复扫（2839 文件）
  parse-error           : 剩余 0
Status: PASS
```

### 2. 58→0 清单差异（修复模式分类计数）

| 模式 | 张数 | 代表文件 |
|:--|:--|:--|
| 顶格列表项补缩进（列表已为缩进式） | 44 | case-strategy-cool-boiled-water / graph-rag / YC-Y-Combinator |
| 粘连列表项拆分（`- a - b` → 两行） | 15（含于上数） | case-strategy-* / 互联网医院模式深度调研报告 |
| BOM 去除 + CRLF→LF 规范化 | 7 | yt-panproduct-* ×6 / skill-yitang-project-spiral-thinking |
| 系统文件补最小 frontmatter（C 类） | 4 | 30_wiki/index.md / links/index.md / personal-os/README.md / concept-card-index-latest.md |

- 47 张 A 类（结构修复）中 44 张含顶格补缩进、15 张含粘连拆分（部分重叠）
- 全部 58 张修复后 `yaml.safe_load` 通过；**内容语义零变化**（54 张 body 与 git HEAD 逐字节一致；C 类 4 张差异归因 kdo index 自动化产物，见下）
- commit：`cced88551`（58 files +765/-468，path-scoped）

### 3. 4 个系统文件补 frontmatter 说明（终审 P1-2 回应）

- **为什么需要**：4 文件是 30_wiki 索引/导航层（Wiki Index / Backlinks Index / README / concept-card-index-latest），扫描器以 `---` 开头判定 frontmatter——无 frontmatter 被判 no frontmatter，计入 parse-error。补 frontmatter 是**元数据层补充**（id/title/type: index/status: stable），正文零改动
- **边界声明**：补 frontmatter 超出任务单「只修结构不改变内容语义」字面范围，故显式声明——它是"补缺失元数据"而非"改内容"，且为归零必要条件（否则 no frontmatter 无法消除）
- **index.md 生成物覆盖风险评估（终审 P2 回应）**：`30_wiki/index.md` 是 `kdo index` 生成物（curation.py:380），`links/index.md` 是 backlinks 生成物（links.py:158）——原模板均无 frontmatter，**rebuild 会覆盖回滚（#366 家族实锤）**。**已修复**：两处生成器模板补 frontmatter（KDO commit `f7a78a0`，pytest 567 passed / 1 历史已知失败 / 1 skip），实测 `write_backlinks_index` 生成文件带 frontmatter ✅
- `personal-os/README.md`、`concept-card-index-latest.md` 非生成器产物，无回滚风险

### 4. 复审对照（欧阳锋 FAIL 清单逐项）

- ✅ P1-1 执行报告：本节约（附工具输出 + 清单差异）
- ✅ P1-2 补 frontmatter 边界：见第 3 节声明
- ✅ P2 index.md 回滚风险：生成器已修（f7a78a0），非人工补丁依赖

*黄药师 · 2026-08-22*

## 内容价值判断（#375 处置门禁补充节，2026-08-22 黄药师领取时补）

- **本任务不涉及素材处置**：修复对象是 58 张卡的 frontmatter **结构**（缩进/列表块），内容语义显式不变（任务目标第 2 条"只修结构不改变内容语义"）
- 无删除/归档/移动动作；若遇内容歧义无法机械修复的卡，按任务单执行范围第 2 条**退回生产者**（不自行处置）
- 修复前的 58 张卡无内容价值判断需求（它们仍是正式层资产，修复后继续存在）

## 编排复核（2026-08-22 欧阳锋建议稿 → 待王语嫣复核）

- 本单由欧阳锋依据用户授权（"清理遗留库级债务"）+ #399 遗留建议 1 起草的**建议稿**，队列已标注"待王语嫣复核，勿领取"
- 请王语嫣复核：① 方向合理性（parse-error 58 归零是否有更高优先的替代）② 优先级 P2 是否合适 ③ assignee 黄药师 vs 老顽童（纯结构修复偏基建，若涉内容判断可拆分）④ 与 #373 同类已知项衔接
- 复核结论：通过 → 执行；调整 → 改单后入队

### 复核结论（2026-08-22 王语嫣）：✅ 通过，原样生效

① 方向合理：存量库级债务清理有老朱 08-22 授权，parse-error 58 张影响解析/索引可达性，且验收用 #399 复扫工具阳性对照（不伪装归零），纪律到位。② P2 合适：不阻塞主线。③ assignee 黄药师正确：yaml 级结构修复+扫描器容错升级属基建；内容歧义退回生产者的设计正是角色边界的正确处理。④ #373 同族衔接已注明。队列行"勿领取"标注同步撤除。

## 终审记录（2026-08-22 欧阳锋 · FAIL 退回，待补执行报告后复审）

**产物质量（欧阳锋独立验证，非本退回项）**：
- `full-library-rescan --check parse-error` 实测 = **0** ✅（归零真实，58 张全修）
- commit `cced88551`（58 files +765/-468）实锤；抽查 case-strategy-cool-boiled-water.md：粘连列表项拆分 + 缩进统一，`src_unknown` 占位符原样保留，**内容语义零变化** ✅
- 修复模式合理（顶格缩进补正/粘连拆分/BOM+CRLF 规范化）

**① P0/P1/P2 清单**：
- **P1（阻断）**：执行报告缺失——验收标准 1「附工具输出」+ 标准 3「修复前后清单差异」均未落任务单；#399 纪律：「任何全库归零/复扫确认声明必须附本脚本输出，否则终审可据此直接 FAIL」
- **P1（阻断）**：4 个系统文件补 frontmatter 超出任务单边界（「只修结构不改变内容语义」）且未声明——`30_wiki/index.md` / `30_wiki/links/index.md` / `30_wiki/concept-card-index-latest.md` / `30_wiki/personal-os/README.md`
- **P2（观察）**：`index.md` 是 `kdo index --rebuild` 生成物——下次 rebuild 若模板无 frontmatter 会覆盖回滚（#366 家族：生成器写回同路径不认新结构=无声回滚）；需确认 kdo index 模板已兼容

**② 字段级定位**：任务单「交付」节后无「执行报告」节（对比 #399/#411 任务单有完整执行报告）；验收标准 1/3 行未闭环。

**③ 证据**：commit `cced88551` message 声称「parse-error 58 张归零」但任务单无复扫输出；git show 确认 4 个系统文件被补 `id/title/type/status` frontmatter。

**④ 期望形态**：任务单追加「执行报告」节，包含——
1. `full-library-rescan --check parse-error` 输出（剩余 0，贴工具输出）
2. 58→0 清单差异：修复模式分类计数（顶格缩进/粘连拆分/BOM+CRLF/系统文件补 frontmatter 各几张）+ 代表文件
3. 4 个系统文件补 frontmatter 的说明：为什么需要（解析可达性）、内容、以及 index.md 生成物覆盖风险评估（kdo index 模板是否已带 frontmatter）
4. 补完重提审；欧阳锋复审对照法（FAIL 清单逐项 grep，3 分钟闭环）
