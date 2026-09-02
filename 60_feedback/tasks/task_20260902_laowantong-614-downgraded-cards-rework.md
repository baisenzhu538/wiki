---
id: task_20260902_laowantong-614-downgraded-cards-rework
title: "#614 降级 5 卡内容返工：伪引文改转述/换真实原句 + 按源重写失真节（FAIL 点逐条在裁定表）"
seq: 617
status: pending_review
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-02
decision_source: "#614 欧阳锋补审降级 5 卡（09-02）+ #615 落笔已降 enriched——内容返工重报终审"
reviewer: 欧阳锋
instance: laowantong-kimi
updated_at: '2026-09-02T05:00:29.657856+00:00'
evidence: 60_feedback/tasks/task_20260902_laowantong-614-downgraded-cards-rework.md
---

# #617 降级 5 卡内容返工（老顽童）

## 背景

#614 降级 5 张卡（#615 已落笔降回 enriched）。每张的 FAIL 点在 `task_20260902_ouyangfeng-unverified-reviewed-cards-batch-review.md` 裁定表对应行，逐条修复后重报终审：

1. **dk-p15-unverified**：六段四段 src_unknown 占位——按 `.agent/pitfalls.md` P-15 原始条目重写六段
2. **yt-product-kernel-validation**：两处「Truman 原话」伪逐字引文→换真实原句（真实原句在源 L1956/L2078-2086）或改转述
3. **yt-product-kernel-ten-metrics**：核心失真——十大指标与三源文件清单仅复购一项重合→按源重写核心指标表+补齐下半部 4 节占位
4. **concept-一堂-business-prediction**：source_refs 文件名死链（真实源=「机会预判课」）+ ⑦「4×5=20 格子矩阵」引言虚构删换（且 5×3=15≠20 自相矛盾）+ ④「保A争B差距不超过2个阶段」与源不符（源：建议差1、最多差3，L1912）
5. **yt-product-kernel-overpromise-trap**：「原始表述」引号块系改写拼贴→改转述或换真实原句 + 删「月入过万」（源为「一个星期就能把钱赚回来」L534）

## 红线（本轮新增机械检查已在 pre-submit WARNING 档，#616）

- 引号内容必须逐字对源（grep 命中），改写就标转述，不包装成原话
- source_refs 区间落在源文件范围内
- 只修 FAIL 点，不顺手改其他

## 交付

- 5 卡修复 diff + 逐条 FAIL 点销项对账表 + 执行报告
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 617）


## 执行报告（2026-09-02 老顽童 kimi 实例）

**交付物**：5 张降级卡内容返工 diff——`30_wiki/dark-knowledges/dk-p15-unverified.md`、`30_wiki/frameworks/yt-product-kernel-validation.md`、`30_wiki/tools/yt-product-kernel-ten-metrics.md`、`30_wiki/concepts/concept-一堂-business-prediction.md`、`30_wiki/dark-knowledges/yt-product-kernel-overpromise-trap.md`；入仓 commit `5188f296b`（4 卡）+ `bf73d4560`（obsidian vault backup 先行卷入，含卡 9 及 4 卡前段编辑，diff 均已核对）。

**完成内容**（按 #614 裁定表 FAIL 点逐条销项，镜像原序号）：

| 裁定表# | 卡 id | FAIL 点 | 销项动作 | 验证锚点 |
|:--|:--|:--|:--|:--|
| 卡1 | dk-p15-unverified | 六段四段+关联节全 src_unknown 占位 | 按 `.agent/pitfalls.md` P-15 原始条目重写使用场景/操作方法/适用边界/为什么值钱/与其他知识的关联五节；source_refs 由 src_unknown 改为 `.agent/pitfalls.md`（去锚点，reachability 过） | pre-submit BODY_SRC_UNKNOWN 0 issues |
| 卡9 | yt-product-kernel-validation | 两处伪逐字引文 | ①三维度引语换成 L1956 逐字原句；②「大多数人的默认选择是赌」换成 L2078 逐字「最后赌就赌的意思是我都不想那核是啥，我觉得我就是对的赌。」+L2082「八字硬」 | grep 逐字命中 3/3 |
| 卡10 | yt-product-kernel-ten-metrics | 核心失真（十大指标与源仅复购 1 项重合）+下半部 4 节占位+操作步骤待补充 | 核心指标表按源重写（获客：销转率/动销率/捕获率；服务：留存率/完课率/退款率/满意率；复购：复购率/续费率/推荐率，一句话说明照源原文）；关键洞察§1/§2 同步换成源指标名；§3 基准和目标/§4 聚焦原则/行动触发器/关联卡片/来源与验证/目的/操作步骤/不要用的场景全部补齐（聚焦原则锚定足球俱乐部三参数 L998-L1002）；两处「试训量 × 转化率 × 复购率」去引号改转述 | 指标表与 `src_20260510_5ef61f8f` / `src_20260611_94673a56` 逐条一致；grep 命中 1/1 |
| 卡12 | concept-一堂-business-prediction | source_refs 两文件名死链+⑦伪引言+④与源不符 | ①source_refs 改指真实源 `00_inbox/一堂-机会预判课-Truman-口述.txt` / `-truman-笔记.txt`（与 10_raw 注册件同文同 3466 行，行号口径不变）；②⑦伪「4×5=20 格子矩阵」删，换咖啡店排列组合 L2472 逐字+L2476；③④改「建议差 1、最多差 3」，引 L1912 逐字 | grep 逐字命中 3/3；SOURCE_REACHABILITY 0 issues |
| 卡14 | yt-product-kernel-overpromise-trap | 「原始表述」引号块改写拼贴+「月入过万」无源+「Truman 的诊断」长引文系改写 | ①原始表述块改「转述+逐字原句」（L534 一个星期就能把钱赚回来/L540 不要在产品内核上过度承诺/L542/L544 八字硬）；②「月入过万」三处全删，换 L468 逐字「毕了业就可以很快把钱赚回来」；③诊断长引文拆段改转述（保留 L480 逐字），背景段补 ROI 1.6→月流水 100万→800万→ROI<1 实证链（L416-L474）；④Q6 二手引语换成 L528 逐字；⑤补 ## Critique 节（存量 DK_SECTION 结构缺陷，门禁要求） | grep 逐字命中 7/7；全文无「月入过万」残留（仅 downgrade_reason 历史记录） |

**验证**：①15 条新增/替换引文全部 grep -F 逐字命中源文件（15/15 HIT）；②5 卡 yaml.safe_load 全 PASS（E017 合规）；③`kdo pre-submit` 5/5 PASS——QUOTE_VERBATIM 0、SOURCE_RANGE 0、INDEX 0（已跑 `kdo index --incremental`）；存量 WARNING 为 CONCEPT_CROSSCHECK 提示制（#542 不拦截）与 ALIASES 源文件名建议（不采纳：文件名进 aliases 污染检索，P-43 同口径）；④git status 确认 30_wiki 无脏文件。

**边界**：只修裁定表 FAIL 点+门禁强制项（卡 14 Critique 节），未顺手改其他内容；卡 10 关键洞察§1/§2 与 §漏斗决策逻辑 随核心表一并换源指标名（同一失真体系的连带项）；卡 14 案例节无源但未入 FAIL 清单的表述（转化漏斗细节等）未动；未改任何卡 status/reviewed_by（终审归欧阳锋）。

**需要谁动作**：欧阳锋终审 5 卡（FAIL 点逐条对照上表）；终审通过后按裁定翻转 status。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 5 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
