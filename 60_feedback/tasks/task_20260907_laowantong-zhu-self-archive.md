---
id: task_20260907_laowantong-zhu-self-archive
title: "识己档案补强：性格三维+失败模型五层结构化入 personal-os（老朱拍板同意，隐私受控）"
seq: 676
status: pending_review
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-07
decision_source: 老朱 09-07 拍板「同意」（#667 产卡范围第一项）
reviewer: 欧阳锋
instance: laowantong
updated_at: '2026-09-07T00:50:38.890089+00:00'
---

# #676 识己档案补强（老顽童）

## 任务（源=老朱的个人域/ 识己 7 件，#667 判定）
1. **性格三维**（跳跃性思维/完美主义/偏好主导，各带优势劣势双面）→ `30_wiki/personal-os/zhu-self-cognition.md`（新建识己档案，结构化清单体）
2. **失败模型五层**（认知迁移失败/被性感驱动/决策标准缺陷…源=洞察-老朱思维模型与失败复盘-20260906）→ 同文件核心节（数字分身线第一优先弹药）
3. 特质与方向适配评估要点并入
4. 每条内容带源锚（源文件+行号），隐私标注 `permission: personal-os-only`（不外流）

## 边界
- 只做结构化整理提炼，零虚构；识己素材不进 30_wiki 公开卡（personal-os 受控区）
- 深度对话/insight 4 件（业务认知档案）另行处置不在本单

## 验收
zhu-self-cognition.md 落盘（性格三维+失败五层+方向适配三节，全带源锚）+ 老顽童自检 + 老朱抽验

## 执行报告（老顽童 09-07 08:50）

**交付物**：`30_wiki/personal-os/zhu-self-cognition.md`（新建，识己档案三节：性格三维+源列两项特质随源全录 / 失败模型五层+能力底盘+认知升级+用人标准+自检表 / 方向适配四方向+时效对照防误用节；70 处唯一行号锚经脚本校验全部在界，24 处关键锚内容级逐一对源核验）

**完成内容**：三份核心源逐字精读（老朱性格诊断报告/洞察-思维模型与失败复盘-20260906/特质与职业方向分析报告）；性格三维（跳跃性思维/完美主义/偏好主导）各带表现+优势+劣势三面带锚；失败五层逐层带锚（认知迁移/性感驱动/取舍+品牌梦多线失血/单元模型未跑通就扩张/识人失败指望牛人）并随源全录能力底盘六项、认知升级五条、用人标准四条、失败模式×自检动作八对、复盘机制（对话驱动+周日 21:00 核销）、决策标准转向证据（选销售=缺口驱动）；方向适配四方向（药食同源极高/健康饮料中/To B 极低/新中式低）+源给评估三维与对治动作；两处源间矛盾如实登记不裁断（To B 投入频次「十年 1-2 次」vs「一年 1-2 天」双锚）；2025-12 报告时效警示+2026-09-06 现状对照节（防把历史排序当现状误用）；permission: personal-os-only 已标，零公开卡；kdo query 检索记录节已附（0 相关命中，与 #667 真空缺口结论一致）

**验证**：①锚点机械校验脚本——70 个唯一行号锚全部在界（bad: 0）；②24 处关键锚内容级抽验全部匹配（含矛盾点两锚 L77/L45 双实锤）；③`kdo pre-submit -f 30_wiki/personal-os/zhu-self-cognition.md` → **PASS**（经 3 轮修复：补 aliases 发现性、逐字引文带源文件自带粗体标记去省略号、`kdo index --incremental` 消 INDEX 错误）；④剩余 1 条 提示制 WARNING（CONCEPT_CROSSCHECK）已人工核对——单元模型/王宁长期主义两概念真相关已加 related 链接（[[yt-entrepreneur-unit-model]]/[[framework-popmart-long-termism-operating-philosophy]]，存在性已 ls 实证），「知识编码体系对比」系检索记录节引用的无关命中标题、「五层结构」系 AI 协作五层与失败模型五层同词异义、「度分析」系子串巧合——均非概念主张，无冲突。完整输出：

```
====================================================================
  Pre-Submit Gate Report
====================================================================
  Files checked: 1
  Passed:        1
  Failed:        0

  [YAML]: 0 issues
  [WIKILINK]: 0 issues
  [DOMAIN]: 0 issues
  [DK_SECTION]: 0 issues
  [OUTLINK]: 0 issues
  [ALIASES]: 0 issues
  [POSITION_DECLARATION]: 0 issues
  [SOURCE_REACHABILITY]: 0 issues
  [QUALITY_SCORE]: 0 issues
  [BODY_SRC_UNKNOWN]: 0 issues
  [VLM_TWO_SECTION]: 0 issues
  [CONCEPT_CROSSCHECK]: 1 warnings
    🟡 30_wiki/personal-os/zhu-self-cognition.md
       本卡涉及已有概念：思维模型（权威定义见 [[yt-personal-thinking-models]]）、度分析（权威定义见 [[yt-entrepreneur-concentration-analysis]]）、知识编码体系对比（权威定义见 [[framework-knowledge-naming-systems-comparison]]）、一堂单元模型（权威定义见 [[bridge-利润-单元模型-定价闭环]]）、五层结构（权威定义见 [[ai-俱乐部人和-ai-协作-五层结构]]）——请人工核对与权威定义的一致性（#542 提示制不拦截；小昭事故根因 3 降档版）
  [QINGDANTI_STRUCTURE]: 0 issues
  [QUOTE_VERBATIM]: 0 issues
  [SOURCE_RANGE]: 0 issues
  [KDO_QUERY_LOG]: 0 issues

  ✅ Result: PASS（1 条 WARNING 在列——有警在身，非全清，终审前自行掂量）
====================================================================
```

**边界**：源外 4 件（深度对话×2/insight×2，业务认知档案）按任务边界未采；零虚构——源外内容仅两类且已标注（矛盾登记不裁断、时效对照两源均带锚）；§3 方向适配系 2025-12 快照已在节首+防误用节双处警示，不构成当前建议；claim 时队列前方 #667（wangyuyan 的单）pending_review 挂审，按 #504 审查等待期占位口径 --force 领取（台账 90_control/force-exceptions.log 已留痕）；status 留 draft——验收含老朱抽验，抽验后由终审方定转正

**需要谁动作**：欧阳锋——终审本单；老朱——抽验档案（重点建议抽：§1.5 矛盾登记表 To B 频次两说谁准、§2 五层是否与自评一致、§3.3 时效对照是否如实）；黄药师——无（增量索引已自行跑，未动全量 rebuild）

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 1 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
