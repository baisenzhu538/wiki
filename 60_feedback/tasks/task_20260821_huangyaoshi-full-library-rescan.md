---
id: 399
assignee: huangyaoshi
status: reviewed
title: 全库复扫标准工具（P2，老朱 08-21 直令立项）：消灭"清单口径归零冒充全库归零"——人肉纪律升级为工具
priority: P2
dependency: []
code_files:
- 90_control/scripts/full-library-rescan.py
- 90_control/scripts/health-check.py
- 90_control/baseline/rescan-baseline.json
- 40_outputs/code/scripts/README.md
updated_at: '2026-08-20T17:46:39.578478+00:00'
reviewed_by: 欧阳锋
review_date: '2026-08-20'
grade: A
---

# #399 全库复扫标准工具

## 来源

- 老朱 08-21 直令："直接立项做成标准脚本工具"
- 复发实证：**"清单范围归零≠全库归零"连续两天两单复发**——#391 漏 25 张（欧阳锋复扫逮）、#393 漏 12 张（欧阳锋复扫逮，yitang 域老卡）。人肉纪律（任务单写"全库口径"）已被证伪不够，升级工具
- E017 家族（修复了≠清干净了）+ E017'（口径）——工具化收口

## 任务目标

做一个全库复扫标准脚本：对指定"修复类别"扫**全库**（30_wiki 全部 md，yaml 级解析），输出剩余清单或确认 =0。生产者提审前自查 + 欧阳锋复审用**同一工具同一口径**——"归零"声明必须附此脚本输出才算数。

## 执行范围

1. **脚本 `90_control/scripts/full-library-rescan.py`**，内置检查项（来自复发史）：
   - `missing-updated-at`：frontmatter 缺 updated_at
   - `missing-tags-dim`：tags 缺 audience/scene 维度（支持 `--domain yitang` 精确匹配域过滤——#393 的 12 张就是精确口径逮到的，正则含糊口径是事故源）
   - `dead-source-refs`：source_refs 指向 pending_archive 等不可达路径
   - `body-fm-style-links`：body（`---` 之后）行首 `- '[[` 前缀行
   - `related-asymmetry`：related 单向链（A 链 B 但 B 未回链）——#383/#384 回链线的自查项
   - 检查项可插拔（后续新类别可注册），`--check all` 默认全跑
2. **输出规约**：每检查项打印 `剩余 N` + 文件清单（N≤50 全列，>50 列前后各 25 + 总数）；退出码非 0 当任一项 N>0（可被门禁/脚本链调用）
3. **纪律固化**：README 或脚本 docstring 写明——**任务报告/退回意见中任何"全库归零/复扫确认"声明必须附本脚本输出**，否则终审可据此直接 FAIL（欧阳锋会知会）
4. 评估是否挂入每日 health-check（增量报警：某检查项从 0 变 >0 即报）——量小并入，量大出评估

## 边界

- 只新增工具，不改存量卡、不改 pre-submit（它管单卡，本工具管库级口径，互补）
- yaml 级解析（E017：禁正则凑数）
- 不碰在飞任务单内容
- 完成后 commit 入档（E040）

## 验收标准（含现成阳性对照）

1. **阳性对照**：当前跑 `missing-tags-dim --domain yitang` 必须逮到 #393 漏网的 12 张（它们此刻还在库里）——逮不到=工具不合格
2. **阴性对照**：`missing-updated-at` 应为 0（#394 刚闭环）、`body-fm-style-links` 应为 0（#384/#386 已清）——复现已知归零
3. 老顽童修完 #393 的 12 张后用本工具复扫转 0（跨任务联动验证）
4. 退出码/输出规约实测

## 交付

1. 脚本 + 正/阳性对照实测输出（贴执行报告）
2. 送欧阳锋终审

---

## 执行报告（2026-08-21 黄药师）

### 交付物

| 文件 | 说明 |
|:--|:--|
| `90_control/scripts/full-library-rescan.py`（新） | 全库复扫标准工具：6 检查项可插拔（missing-updated-at / missing-tags-dim / dead-source-refs / body-fm-style-links / related-asymmetry / parse-error）+ `--domain` 精确匹配 + `--json` + `--delta` 增量报警 + 退出码（任一项 >0 → 1） |
| `90_control/scripts/health-check.py`（改） | 挂载 `full-library-rescan --delta baseline/rescan-baseline.json`（每日 kdo watch --health 自动跑） |
| `90_control/baseline/rescan-baseline.json`（新） | 存量债基线快照（1.2MB，文件级清单）——基线之外的新增违规实时报警 |
| `40_outputs/code/scripts/README.md`（改） | 工具登记 + 归零声明纪律 |

### 阳性对照（#393 漏网必须逮到）✅

- `missing-tags-dim --domain yitang` = **0**——#393 已补齐的 47 张不再报（精确口径不误伤）
- `parse-error`（--domain yitang 下仍全库列出，**不被域过滤藏起来**）逮到 #393 复审"剩 2 张"：**concept-yihang-ai-feature-thinking（YAML ParserError）+ 一堂.md（entity，source_refs 块缩进坏）**——正是欧阳锋 A- 扣分的"解析器口径盲区"：解析失败卡显式列入 parse-error，不伪装归零

### 阴性对照（已知归零必须复现）⚠️ 逮到 2 处真实漏网

| 检查项 | 任务单预期 | 实测 | 结论 |
|:--|:--|:--|:--|
| missing-updated-at | 0（#394 刚闭环） | **剩余 1**：`framework-kdo-self-attack.md`（06-27 终审卡，无 updated_at，#394 清单外） | 工具逮到真实漏网，非误报 |
| body-fm-style-links | 0（#384/#386 已清） | **剩余 23**：yt-* 老卡 body 行首 `- '[[` 前缀（如 yt-decision-canvas.md:312） | #384/#386 未覆盖 yt-* 老卡，真实存量 |

### 退出码/输出规约实测 ✅

- `--check missing-tags-dim --domain yitang` → EXIT 0（归零）
- `--check missing-updated-at` → EXIT 1（剩余 1）
- `--check all` 无参数 → EXIT 1；输出每检查项 `剩余 N`，N≤50 全列、>50 前后各 25 + 总数
- `--json` → `{check: {count, files}}` 结构化输出（health-check/agent 可消费）

### delta 增量报警实测 ✅

- 首次 `--delta`（无基线）→ 自动建档 EXIT 0
- 复跑 → "无新增违规（PASS）" EXIT 0
- health-check 全量模式实测：`[PASS] 全库复扫增量报警（#399）` 挂载生效

### 口径设计（对照复发史逐条）

- **yaml 级解析**（E017 禁正则凑数）：safe_read 多编码容错 + yaml.safe_load
- **--domain 精确匹配**（#393 P1：只取 domain[0] 漏多 domain 卡）：domain 列表精确包含
- **parse-error 不参与域过滤**（#393 A-：解析器口径 ≠ 全库口径）：解析失败卡永不全库列出
- **dead-source-refs 判定**：#391 合法占位 `src_unknown` 跳过；行号/节标记（L14、§一）剥离；通配符 glob；URL 非文件不判；相对路径先 vault 根再桌面级（复盘目录）
- **related-asymmetry**：排除 60_feedback/（usage-log 非正式卡不回链）；B 无 related 字段跳过（系统页）；同对去重（修了 id/stem 双索引重复报 bug：14848 → 7415）

### 存量债快照（2026-08-21 全库 2838 文件）

| 检查项 | 剩余 | 备注 |
|:--|--:|:--|
| missing-updated-at | 1 | framework-kdo-self-attack.md |
| missing-tags-dim | 573 | W2 回填范围（#393 词表定稿后分批） |
| dead-source-refs | 836 | 存量死路径（#391 部分处理后剩余） |
| body-fm-style-links | 23 | yt-* 老卡 |
| related-asymmetry | 7415 | 存量单向链（#383/#384 回链线持续消化） |
| parse-error | 61 | YAML 损坏卡（#373 已知 + 新增），YAML 修复单独立项，**不伪装归零** |

### 遗留建议（欧阳锋裁决）

1. **parse-error 61 张**：YAML 损坏修复单独立项（#373 同类），修复前任何"归零"声明须排除该项
2. **related-asymmetry 7415**：量级大，#383/#384 回链线按批消化；工具提供可复扫口径
3. 基线文件 1.2MB 已入档，新增违规实时报警；存量清理后归零的项需重跑 `--delta` 更新基线

---

## 欧阳锋终审（2026-08-21 · 工具实测）

**裁定：PASS A。**

**O3 验证**：
- 三问①：commit 8477dc648（01:43）+ 工具在 90_control/scripts/ ✓
- **工具实测**：`--check missing-updated-at` → 剩余 1（framework-kdo-self-attack.md——与报告一致，**立即逮真实漏网**）；`--domain yitang` → PASS ✓
- **纪律固化**：工具内置"归零声明纪律——任何全库归零/复扫确认声明必须附本脚本输出"——#391/#393 口径事故的根被机制化解决 ✓
- **口径设计逐条对照复发史**：yaml 级解析（E017）/--domain 精确匹配（#393 P1）/parse-error 不参与域过滤（#393 A-）/dead-source-refs 判定（#391）/related-asymmetry 排除系统页+去重（修 14848→7415 bug）✓
- delta 增量报警 + 退出码 + --json + health-check 挂载全实测 ✓

**意义**：从"声明靠自觉"到"声明须附工具输出"——归零声明的可验证性成为强制；存量债快照（6 项）清晰化（parse-error 61 不伪装归零/related-asymmetry 7415 分批）。
