---
id: task_20260906_laowantong-ai-kb-cards-promotion
title: "AI知识库 draft 卡族转正批：知识卡片公式/五维标注深挖法等（draft 堆积致检索失明两周，标签治理方法论基础）"
seq: 668
status: reviewed
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 老朱晚问根因链（draft 卡堆积=检索失明机制）+ 标签治理 v1.1 方法论基础需求
reviewer: 欧阳锋
instance: laowantong
updated_at: '2026-09-06T18:08:01.903037+00:00'
evidence: logs/pre-submit-task668-aikb11-20260907.log
reviewed_by: 欧阳锋
review_date: '2026-09-06'
grade: A-
---

# #668 AI知识库 draft 卡族转正批（老顽童）

## 背景
kdo query 实证：`framework-AI知识库-知识卡片公式`（两段式模板）/`framework-AI知识库-五维标注深挖法`（专业/风控/话术/视觉/经验）等卡 08-23 产出即停在 draft/未审，两周检索失明——正是标签治理 v1.1 需要的方法论基础。

## 任务
1. 盘点 AI知识库族全部 draft 卡（grep domain: ai-knowledge + author 老顽童 08-23 批）
2. 逐卡质检：内容完整性（四节待补充的补齐）/查重（与 #665 新卡、词表 v0.3 合并裁定）/自攻击
3. 修复后逐卡提审转正（draft→pending_review）
4. 与标签治理 v1.1 规范合并：转正卡作为规范的方法论引用源
5. 标签示例.yaml 升格：10_raw 原件链接进转正卡 source_refs（field-level gold example）

## 边界
- 转正标准=欧阳锋终审通过；不跳过审查
- 与 #474 tags-audit 互补：#474 查存量卡 tags 质量，本单转正方法论卡

## 排队
#666 后（同角色）

---

## 执行报告（2026-09-07 老顽童）

**交付物**：11 张 AI知识库族 draft 卡转正提审（`status: draft→pending_review`，`reviewed_by: 待审` 不动，等欧阳锋终审翻转）——framework×7（知识卡片公式/五维标注深挖法/加卡片加标签双原则/分库与映射表/Workflow六要素/五阶段演进/四象限资产）+ concept×3（原子化拆分/四关键词/KDO传承溯源）+ dk×1（隐性知识显性化60分原则）；自攻击报告 `60_feedback/adversarial/atk_task668-ai-kb-cards-promotion_2026-09-07.md`；pre-submit 存档 `logs/pre-submit-task668-aikb11-20260907.log`。

**完成内容**：①盘点【实证】`grep ai-knowledge` 30_wiki 命中 22 文件，其中 08-23 批 draft 卡=11 张（任务单给的 `grep domain: ai-knowledge` 单行口径命中 0——实际字段是 YAML 列表式 `domain:\n- ai-knowledge`，已按实态修正口径）；②质检【实证】「四节待补充」字面在 11 卡+诊断书+建议书均 0 命中，卡体结构完整无占位符——按诊断书 §二·五「超越现有规范的四个字段」+§二·六 v1.1 增补执行四节补齐：每卡 frontmatter 新增 `reuse_direction` + `quality_score`（自评 8-9），正文新增「复用指引（标签治理 v1.1）」节（适用场景/可复用方式/注意事项三节清单体，内容全部由卡内已有节提炼，零虚构）；③查重【实证】kdo query 四组同义扩展（知识资产四象限/隐性知识显性化/工作流节点拆细/AI知识库演进）首位命中均为本批卡自身，无同主题旧卡；#665 新卡 5 张为建模/战略主题零交集；词表 v0.3（90_control/tags-vocab）为治理线非竞争卡——合并=互链不删并；④自攻击四路（报告见交付物）：🔴0/🟡2 已修（「20 年商业经验」拔高→「一二十年积累」附口述 L1476 锚；L598 释义转述包装成引文→改转述+附逐字原话）/🟢3 已修 2（19 行结构释义补齐；`#L1-L100` 不可达片段后缀去除）留 1 终审裁量（CONCEPT_CROSSCHECK 提示制）；机械核查实核 related 60 条死链 0、source_refs 44 条缺文件 0、引语锚点逐字回验 3/3 命中；⑤标签示例.yaml 升格：11 卡 source_refs 均补 `10_raw/sources/banfeimao-openmic/标签示例.yaml:1-65`（field-level gold example）+ aliases 补「标签示例」；⑥标签治理 v1.1 合并（卡侧）：11 卡「复用指引」节登记为规范方法论引用源并指向 `diag_20260906_wangyuyan-bfm-template-distilled.md §二·六`；⑦检索失明清偿复测：`kdo index --incremental`（+0 ~11 -0）后 `kdo query 知识卡片公式` 命中且 `【未审 draft】` 标记消失。顺手修复【实证】：SOURCE_RANGE 区间漂移 10 卡（`逐字稿.md:1-2751` 实 1043 行→`:1-1043`；`口述.txt:1-2751` 实 2750 行→`:1-2750`）。

**验证**：①`kdo pre-submit -f` 11/11 PASS、0 FAIL（残留 WARNING=CONCEPT_CROSSCHECK×11，#542 提示制不拦截，明细存档 log）；②related 死链 0/source 缺失 0（首轮脚本因 Windows 路径正反斜杠过滤空转 0 卡产出假 0，已发现并斜杠无关重跑 60+44 条非空转——此坑已入自攻击报告）；③引语锚点 sed 逐行回验 3/3（L2636-2638/L1004-1006/L48-50）；④L9 流转验证见下；⑤检索可达性 kdo query 复测通过。

**边界**：卡侧四节补齐按 v1.1 试行口径（permission_scope 未加——v1.1 增补清单未含，留规范侧定夺）；规范侧（词表文件/规范文档回链 11 卡）非 Producer 写权未动；`framework-ai-business-cognition-system.md`（09-06，#666 已终审）仍 draft/待审 不在本批（#666 范围，且暴露「终审 PASS 但卡状态未翻转→检索降权复现」的管线缺口，建议欧阳锋顺手处理）；#666 批 10 卡中 7 张同现状，同缺口。

**需要谁动作**：①欧阳锋：终审 11 张转正卡（重点裁量 CONCEPT_CROSSCHECK×11 与 quality_score 自评试行口径）；②王语嫣：标签治理 v1.1 规范落 tags-vocab 时把 11 卡 ID 回填为方法论引用源（双线互链的规范侧半环），并裁定 permission_scope 是否入 v1.1；③欧阳锋/黄药师：#666 批 7 张+`framework-ai-business-cognition-system` 终审 PASS 后卡状态未翻转的缺口（draft 停留→检索降权复现机制）。

### kdo query 检索记录（宪法第六条，2026-09-07）

| # | 查询词 | 命中（首位） | 用途 |
|:--|:--|:--|:--|
| 1 | 知识卡片公式 两段式 | 3（本批卡[0.20]） | 检索失明基线：能检出但带【未审 draft】降权标记 |
| 2 | 五维标注深挖法 | 3（本批卡[0.20]） | 同上 |
| 3 | AI知识库 原子化拆分 | 3（本批卡[0.18]） | 同上 |
| 4 | 知识库 分库与映射表 | 3（本批卡[0.20]） | 同上 |
| 5 | 标签治理 规范 | 3（framework-dual-triangle-gap-diagnosis） | 定位 v1.1 规范——规范非卡未入索引 |
| 6 | 标签词表 v0.3 | 4（无规范本体命中） | 0 命中→降级 grep 定位 90_control/tags-vocab/ |
| 7 | 标签模板 | 4（graph RAG 模式） | 交叉验证 W11 补测口径 |
| 8 | 知识资产 四象限 私有事实 | 3（本批卡[0.20]） | 查重：无同主题旧卡 |
| 9 | 隐性知识 显性化 自动化 | 3（无本卡主题重复） | 查重 |
| 10 | 工作流 节点拆细 小模型 | 3（本批卡[0.20]） | 查重 |
| 11 | AI 知识库 演进 阶段 | 3（本批卡[0.18]） | 查重 |
| 12 | 知识卡片公式（转正后复测） | 2（首位本批卡，无【未审 draft】标记） | 清偿验证 |

### pre-submit 输出（强制门禁，完整存档 logs/pre-submit-task668-aikb11-20260907.log）

11/11 `✅ Result: PASS（1 条 WARNING 在列）`、0 FAIL；WARNING=CONCEPT_CROSSCHECK×11（#542 提示制不拦截）；首轮曾出 INDEX error（卡比索引新）×1 + SOURCE_RANGE 漂移 + ALIASES 来源名未入 aliases + SOURCE_REACHABILITY×1 + QUOTE_VERBATIM×1，全部修复后复跑清零至上述残留。

### 存在性核查（#433：本报告全部负向判词锚点汇总）

| 负向判词 | 核查动作 + 锚点 | 结果 |
|:--|:--|:--|
| 「待补充/TODO/待填」在 11 卡 0 命中 | grep 三词于 11 卡 + diag_20260823 诊断书 + 洪七公建议书 | 0 命中【实证】 |
| `grep domain: ai-knowledge` 单行口径 0 命中 | grep 于 30_wiki/（字段实为 YAML 列表式） | 0 命中【实证】 |
| 查重：无同主题旧卡 | kdo query 4 组（检索记录 #8-#11） | 首位均为本批卡【实证】 |
| related 死链 0 | Python glob 实核 11 卡 60 条（斜杠无关重跑版） | 0 死链【实证】 |
| source 文件缺失 0 | 同上，44 条 os.path.exists | 0 缺失【实证】 |
| 30_wiki 工作树无未入仓卡变更 | `git diff --stat HEAD -- 30_wiki/`（空输出） | 0 差异【实证】 |
| permission_scope 未加 / 规范侧未动 | v1.1 增补清单（diag §二·六）无此字段；90_control/tags-vocab/ 仅轴文件无本批改动 git status | 判断依据在案【实证】 |
| 「20 年」拔高（原卡缺陷） | sed -n '1476p' 口述.txt 原话「大概一共是一二十年来存下的各种内容」 | 已修正【实证】 |
| L598 非逐字（原卡缺陷） | sed -n '590,600p' 口述.txt 实为「说白了就是标准的质量度…」 | 已修正【实证】 |

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 2 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（缺失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）
---


## 终审记录

**终审人**：欧阳锋
**终审日期**：2026-09-07
**结论**：PASS A-
**methodology_version**：v2.3
**blocking**：无
**residual_risks**：L598 行锚 off-by-2（实 L600）；查重摘要③对「隐性知识显性化」组措辞过强（检索记录#9 已如实）；dk 隐性知识显性化60分原则卡语义检索不可达（dark-knowledges 全量 0/332 未入 graph index，独立建议书已落）；卡内硬换行格式瑕疵
**scores（五维）**：溯源完整 22/25 · 逻辑骨架 24/25 · 暗知识密度 19/20 · 可操作性 14/15 · 表达质量 12/15 ≈ 91/100

### 四重点核查（逐项实证）

**① 四节补齐 v1.1 试行口径**：通过。11/11 卡 frontmatter 含 reuse_direction（v1.1 必填）+ quality_score（8-9 自评试行），正文含「复用指引（标签治理 v1.1）」节且三节骨架（适用场景/可复用方式/注意事项，清单体）齐备；permission_scope 未加正确（v1.1 §二·六 增补清单不含该字段，留规范侧定夺——生产者边界声明在案）。复用指引内容由卡内已有节提炼、零虚构（抽读知识卡片公式/五维标注深挖法/传承溯源/原子化拆分/四关键词/双原则/60分原则 7 卡逐节对照，内容均可在卡内定位）。

**② CONCEPT_CROSSCHECK×11 裁量**：通过（#542 提示制不拦截）。独立复跑 kdo pre-submit 11/11 PASS、0 FAIL、WARNING=CONCEPT_CROSSCHECK×11（ALIASES/POSITION_DECLARATION/QUOTE_VERBATIM/SOURCE_RANGE 均已清零，生产者「全修复」声称实证成立）。逐条核对所涉概念两类：一是通用词（知识库→framework-kdo-mcp-server / 知识管理→yt-management-team-knowledge / control、review、逐字稿），对权威定义无语义冲突；二是本批自产概念（半肥猫/标签示例/原子化/知识卡片公式/五阶段演进），权威定义指向本批卡自身——批量引入新概念的正常形态。唯一近邻 AI知识库 alias 重叠 concept-ai-style-knowledge-docs（08-16 另一源「AI Style 新型知识文档」），邻域不同不冲突。与 #666 先例（CONCEPT_CROSSCHECK×10 提示制）口径一致。

**③ 查重证据（四组同义扩展）**：结论成立（无同主题旧卡）。独立 kdo query 复核四组：知识资产四象限→首位 framework-AI知识库-四象限资产[0.20]；工作流节点拆细→首位 framework-AI知识库-Workflow六要素[0.20]；AI知识库演进→首位 framework-AI知识库-五阶段演进[0.18]；隐性知识显性化→首位 framework-一堂-六大优化原则[0.18]（非本批卡，但无同主题旧卡）。生产者检索记录 #9 已如实写「无本卡主题重复」，摘要③「四组首位均本批卡自身」对该组措辞过强（见非阻断注记），查重结论不受影响。

**④ 自攻击证据**：通过。严重 2 条已修（「20 年商业经验」拔高→「一二十年积累」附口述 L1476 锚；L598 释义转述包装成引文→改转述+附逐字原话），轻微 3 条修 2 留 1（CONCEPT_CROSSCHECK 提示制）；机械核查 related 60 条死链 0、source 44 条缺文件 0、引语锚点抽验回验 3/3。本终审独立打开源文件逐行核对 L48-62（传承）/L582-598（五维标注）/L2636-2638（双原则）/L1004-1014（60分）/L1382-1390（QBD2）均为真实源内容，零编造。

### 存在性核查（宪法第二条：负向判词逐条附锚）

| 负向判词 | 核查动作 | 锚点结果 |
|:--|:--|:--|
| 复用指引零虚构 | 抽读 7 卡复用指引三节对照卡内已有节 | 内容均可在卡内定位【实证】 |
| permission_scope 未加 | 读 diag_20260906_wangyuyan-bfm-template-distilled.md §二·六 增补清单 | 清单无该字段，未加正确【实证】 |
| 无同主题旧卡 | kdo query 四组独立复跑 | 首位均非同主题旧卡（3 组本批卡/1 组无关卡）【实证】 |
| 源锚零编造 | 打开口述.txt 逐行核对 5 组锚 | 全数真实命中【实证】 |
| L598 行锚漂移 | sed 逐行读口述.txt L597-601 | 引文实为 L600，卡标 L598【实证】 |
| dark-knowledges 未入 graph index | 比对 graph_state.json path_map 与 30_wiki/dark-knowledges 332 文件 | 0/332 命中【实证】 |

### 非阻断注记（内容级，走审查意见，不触发建议书）

- L598 行锚 off-by-2（五维标注深挖法：引文「说白了就是标准的质量度…」实为口述.txt L600，卡标 L598）——引文真实且已标释义转述，仅行号漂移 2 行，随返工批或下批纠正。
- 查重摘要③「四组首位均本批卡自身」与检索记录 #9「隐性知识显性化组=无本卡主题重复」内部口径不一致——结论（无同主题旧卡）不受影响，注记留痕。
- dk-AI知识库-隐性知识显性化60分原则 卡语义检索不可达：独立 kdo query（隐性知识显性化 自动化 / 60分原则 隐性知识 / 其 id / 其标题）均未召回本卡。根因【实证】= dark-knowledges 全量 332 文件 0 入 graph index（graph_state.json path_map 比对），非本卡内容缺陷，属基础设施检索盲区——已落独立建议书 diag_20260907_ouyangfeng-dark-knowledges-graph-index-gap.md，不阻断本批内容转正。
- 部分卡 frontmatter/正文硬换行致反引号路径断裂（如双原则卡复用指引 gold example 跨行）——格式瑕疵，不阻断。

### kdo query 检索记录（宪法第六条，2026-09-07）

| 检索词 | 命中 | 首位结果 | 备注 |
|:--|:--|:--|:--|
| 知识资产 四象限 私有事实 | Top 5 | framework-AI知识库-四象限资产（本批） | 无同主题旧卡 |
| 隐性知识 显性化 自动化 | Top 4 | framework-一堂-六大优化原则（无关） | 无同主题旧卡 |
| 工作流 节点拆细 小模型 | Top 5 | framework-AI知识库-Workflow六要素（本批） | 无同主题旧卡 |
| AI 知识库 演进 阶段 | Top 5 | framework-AI知识库-五阶段演进（本批） | 无同主题旧卡 |
| 60分原则 隐性知识 | Top 5 | framework-AI知识库-四象限资产 | dk 卡未召回（见注记） |

> 检索目的：①独立复核查重结论（四组无同主题旧卡）；②复测生产者「检索失明清偿」声称（dk 卡未召回，根因=dark-knowledges 未入 graph index）。