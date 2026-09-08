---
id: task_20260908_huangyaoshi-ai-data-domain-infra
title: "基建：ai-data-domain-digest 补建 + 本域散卡注册 domain-mapping + 双三角AI数据重复卡去重（#682 编排）"
seq: 686
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-08
decision_source: 老朱 09-08 19:25 拍板全做（#682 编排）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-08T13:24:03.791374+00:00'
---

# #686 黄药师基建单：AI数据域 MOC 补建 + 注册 + 重复卡去重

> 规格源=诊断报告 `60_feedback/diagnosis/diag_20260908_wangyuyan-ai-data-ai-basic-deep-dig.md` §〇（MOC 先行结论）+ §五-基建缺口登记【实证】。

## 背景（存在性核查锚，报告已实证）

- AI数据域 digest **缺失**：`30_wiki/domains/` 14 张 digest 无该域；`90_control/domain-mapping.md` 未注册；5 张 MOC 均不覆盖；相关卡散挂 ai-collaboration/kdo/yihang 域下
- **重复卡实锤**：`case-yihang-dual-triangle-AI数据.md` 与 `case-yihang-dual-triangle-AI三角-数据.md` 双卡同图源（`00_inbox/人机协作双三角/AI数据.png` 两次 VLM 提取）

## 工作项（3 项）

1. **ai-data-domain-digest 补建**：`30_wiki/domains/ai-data-domain-digest.md`，骨架参照 `30_wiki/domains/ai-basic-domain-digest.md`；资产路标覆盖本域现有散卡（concepts×2/tool×7/case×3/article×1，清单见诊断报告 §五-基建缺口登记）+ 在产新卡族（#683 P0 八张，产毕后回填路标可二次补）
2. **domain-mapping 注册**：本域 12+ 散卡注册进 `90_control/domain-mapping.md`（ai-data 域条目新建），同步 `30_wiki/index.md` digest 索引
3. **重复卡去重合并**：`case-yihang-dual-triangle-AI数据` vs `case-yihang-dual-triangle-AI三角-数据` 合并为一卡——保留信息更全者为主卡，另一卡做 redirect/合并标注；两卡全部被引处（grep related/source_refs）改指主卡；source_refs 只追加不替换（F-KDO-015）

## 验收标准

1. digest 骨架与 ai-basic-domain-digest 同构；`kdo pre-submit` PASS
2. domain-mapping 注册后 `kdo query` 该域可召回 digest
3. 去重合并后 grep 全库无指向被并卡的死链（`check_dead_links.py` 或 grep 复核）
4. 基建改动先单卡 dry-run→单卡 write→验证→再批量（F-KDO-013）；批量写入需人工批准（F-KDO-014）
5. 欧阳锋终审

## 边界

- 只做基建/注册/去重，不做内容判断与卡片正文改写（内容归老顽童/欧阳锋）
- #683 在产新卡的路标回填可等 P0 终审后二次补，本单先注册存量散卡


## 执行报告（黄药师 2026-09-08，#686）

### 1. 交付物

| # | 文件 | 变更 |
|:--|:--|:--|
| 1 | `30_wiki/domains/ai-data-domain-digest.md` | 新建——域入口 MOC，骨架同构 ai-basic-domain-digest |
| 2 | `30_wiki/cases/case-yihang-dual-triangle-AI三角-数据.md` | 主卡：aliases +3 追加、source_refs 追加图源、正文追加「合并记录」节（薄卡独有【基础结构】【待标注提示】verbatim 搬入） |
| 3 | `30_wiki/cases/case-yihang-dual-triangle-AI数据.md` | 转 redirect stub：merged_into 指主卡 + 正文合并说明（原 OCR 与两节已入主卡，无信息损失） |
| 4 | `90_control/domain-routes.yaml` | 新增 AI数据 路由（keywords/index_cards/search_dirs） |
| 5 | `90_control/domain-mapping.md` | 两视图映射表新增 ai-data 行 |
| 6 | `30_wiki/index.md` | digest 索引行 +1；双三角数据主卡行补 source；薄卡行改指主卡（redirect 标注） |
| 7 | `90_control/vault-status.md` | 快照刷新（2960 卡 / 67 域） |

### 2. 验证方式与结果

| 验收项 | 方法 | 结果 |
|:--|:--|:--|
| digest 骨架同构 + pre-submit PASS | 逐节对照 ai-basic-domain-digest；`kdo pre-submit --files` 三卡 | ✅ PASS（8 WARNING 均存量：双卡 TAGS 软期/CONCEPT_CROSSCHECK/VLM_TWO_SECTION 存量提示；首轮 FAIL 的 src_unknown 占位措辞已修、INDEX 新鲜度已跑 `kdo index --incremental` 后复过） |
| kdo query 召回 digest | `kdo query "AI数据域 数据判断力"` | ✅ digest 以 0.85 召回榜首（带【未审 draft】标注=#380 正确行为）；graph 重建 12 页后 coverage 探针全目录 gap=0 |
| 去重后无死链 | `check_dead_links.py` 全库 + grep 复核 | ✅ 全库 83 条死链均为 agent-traces 存量（与本单无关）；活文档指向薄卡引用=0（仅自动生成索引待自愈 + 主卡合并记录自指 + digest 路标 redirect 标注，均合法） |
| 批量纪律（F-KDO-013/014） | 全程单点写入：1 新建 + 2 单卡改造 + 3 注册文件单行插入，无批量写 | ✅ 合规 |

### 3. 影响范围

7 文件（上表）；索引面 search_index +1 / graph 12 页；不动任何卡 frontmatter domain 归属、不动信号面文件（矩阵免登记）、不碰 #683 在产卡。

### 4. 边界与不做（初判=待证命题核查记录）

- 任务单前提 5 项开工前逐条实证全成立（digest 缺失/映射未注册/双卡实存/骨架实存/诊断报告实存）；claim 时 #679 门禁 WARNING（缺 initial_assessment 字段）即本次核查的触发，核查记录落本节
- 任务单引诊断报告 §五「清单见基建缺口登记」——该节实际只给计数（concepts×2/tool×7/case×3/article×1）未列名单；13 张名单由 Builder 按诊断报告口径（马易族执行层+AI数据课体系+双三角数据族）扫库重建，与计数精确吻合（见 digest 路标）；若与编排者原意有出入属路标可修正项
- #683 P0 八张实测已产毕（含 reviewed 标记），digest 路标直接收录，无需二次补
- 不做：散卡 frontmatter domain 归属改写（13 张批量改=F-KDO-014 需人工批准，未获授权）；薄卡 tags 补词（存量治理归 #426）；全库另有疑似重复族（AI三角-场景 vs AI场景、AI三角-基本功 vs AI基本功、人类三角-* vs 人*、数据标注维度最佳实践调研报告 vs data-labeling-best-practices-report 同题双卡）——本单只裁任务点名的 AI数据 一对，其余交编排裁量

### 5. 遗留与风险

- 薄卡 redirect 后若消费方仍直链旧名：stub 实存不构成死链，且 aliases 已并入主卡（检索可归一）；自动生成索引（concept-card-index-latest/links/index）下次生成自愈
- tags 门禁 09-14 HARD 后 redirect stub（内容词 0）将被拦——存量治理归 #426 内容侧批次，非生产侧债务
- vault backup Step 9 由 30min schtasks（kdo-vault-git-backup）承载，本次随提交自动入备；D 盘 bundle 备份走既有节拍，未另行手动触发

### 五字段摘要（#429 F-034 机器可读）

**交付物**：`30_wiki/domains/ai-data-domain-digest.md`（新建域MOC）；`30_wiki/cases/case-yihang-dual-triangle-AI三角-数据.md`（主卡吸收薄卡）；`30_wiki/cases/case-yihang-dual-triangle-AI数据.md`（转redirect）；`90_control/domain-routes.yaml`+`90_control/domain-mapping.md`+`30_wiki/index.md`（三处域注册）；`90_control/vault-status.md`（快照）；详见上方执行报告表。

**完成内容**：ai-data域digest补建（路标13散卡+8张P0）+ 路由/映射/索引三处注册 + 双三角AI数据重复卡去重合并（主卡=AI三角-数据，薄卡redirect零信息损失）。

**验证**：`kdo pre-submit --files <三卡>` → ✅ PASS（8 WARNING均存量）；`kdo query "AI数据域 数据判断力"` → digest 0.85召回榜首带【未审 draft】标；`kdo index --incremental` + `kdo graph rebuild`（12页）+ coverage探针全目录 gap=0；`python 90_control/scripts/check_dead_links.py` 全库83条死链均agent-traces存量，本单三卡零死链。

**边界**：不动13张散卡frontmatter domain归属（批量改属F-KDO-014需人工批准）；薄卡tags/双卡VLM两段式为存量治理归#426/#518；全库另有疑似重复族（AI场景/AI基本功/人类三角族/数据标注报告同题双卡）仅登记不扩裁；#683 P0八张实测已产毕（reviewed），digest路标已直接收录。

**需要谁动作**：欧阳锋终审本单（digest是否达标#686验收5条）；王语嫣知悉——13张散卡名单系按诊断报告口径扫库重建（§五原节仅给计数），如与编排原意有出入可修正路标；#426内容侧排期时留意09-14 tags HARD对redirect stub的存量拦截。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 7 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（缺失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）
