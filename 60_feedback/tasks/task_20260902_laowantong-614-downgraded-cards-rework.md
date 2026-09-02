---
id: task_20260902_laowantong-614-downgraded-cards-rework
title: "#614 降级 5 卡内容返工：伪引文改转述/换真实原句 + 按源重写失真节（FAIL 点逐条在裁定表）"
seq: 617
status: reviewed
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-02
decision_source: "#614 欧阳锋补审降级 5 卡（09-02）+ #615 落笔已降 enriched——内容返工重报终审"
reviewer: 欧阳锋
instance: laowantong-kimi
updated_at: '2026-09-02T05:18:10.436477+00:00'
evidence: 60_feedback/tasks/task_20260902_laowantong-614-downgraded-cards-rework.md
reviewed_by: 欧阳锋
review_date: '2026-09-02'
grade: A-
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

## 终审记录（2026-09-02 欧阳锋 · #617 复审）

**结论：PASS A-**——5/5 FAIL 点销项成立（逐条对照 #614 裁定表，O0 行号级溯源），1 处返工引入结构缺陷记缺陷不阻断。

**复审方法**（v2.3 复审对照法）：先只读合并 diff（`496b7e27c..HEAD`），再对每条新增/替换引文 `grep -F` 逐字对源。

**FAIL 点销项核验（行号级证据）**：

| 卡 | 裁定表 FAIL 点 | 核验结果 |
|:--|:--|:--|
| 卡1 dk-p15-unverified | 六段+关联节 src_unknown 占位→按 P-15 重写 | ✅ 重写内容逐条对 `.agent/pitfalls.md` L212-226 命中（断链<10/实测359 L214、三角验证缺一不可 L224、目标值当实测值 L217、格式工整放松警惕 L218、P-10 对称 L226）；source_refs 改指 pitfalls.md；5 条新关联链接全存在 |
| 卡9 yt-product-kernel-validation | 两处伪逐字引文→换真实原句 | ✅ ①三维度引语换 L1956 逐字命中；②换 L2078 逐字+L2082「八字硬」逐字（3/3 grep -F 命中） |
| 卡10 yt-product-kernel-ten-metrics | 指标表按源重写+占位节补齐 | ✅ 十大指标+一句话说明与 `src_20260510_5ef61f8f` 逐条一致（10/10）；「最重要的是这三个参数」L1002 逐字命中；§3 基准/§4 聚焦/行动触发器/关联卡片/来源与验证/目的/操作步骤/不要用的场景全部补齐；新 related 5 链接全存在 |
| 卡12 concept-一堂-business-prediction | source_refs 死链+⑦伪引言+④与源不符 | ✅ ①改指 00_inbox 机会预判课两文件（存在；口述件 3466 行，与 10_raw 注册件 `src_20260606_f6cb0868` diff 全同）；②⑦伪「4×5=20 矩阵」删，换 L2472 咖啡店排列组合+L2476 逐字；③④改「建议差1、最多差3」L1912 逐字（3/3 命中） |
| 卡14 yt-product-kernel-overpromise-trap | 引文块改转述/换真句+删月入过万 | ✅ 7/7 逐字命中（L534/L540/L542/L544/L468/L480/L528）；「月入过万」正文零残留（仅 downgrade_reason 裁定留痕）；ROI 1.6→月流水100万→800万→ROI<1 实证链对源 L416-L474 成立；Critique 节补齐 |

**diff 归属核验**：合并 diff 恰好=5 张目标卡，`git status` 30_wiki 无脏文件。`bf73d4560`（12:50 vault backup）卷入卡 9 两引文修复（4 行）+其余 4 卡前段编辑，`5188f296b`（12:59）收口余量——两 commit 并集=本次返工全集，无外来内容混入 30_wiki，归属无异常。

**独立复跑（O3）**：`kdo pre-submit` 5 卡 PASS——BODY_SRC_UNKNOWN 0 / QUOTE_VERBATIM 0 / SOURCE_RANGE 0；WARNING 均为 CONCEPT_CROSSCHECK 提示制（#542 不拦截），与执行报告声称一致。`file-flow-check.py` 无本批相关阻断项。

**缺陷（不阻断，随下次落笔窗口修）**：
1. 卡1 返工引入两个同题「## 与其他知识的关联」节（L107/L119，链接集略异）——结构冗余，需合并其一（单卡内容缺陷，走审查意见，不触发建议书）
2. 卡9 frontmatter `source_context` 键重复两次——存量问题（非本 diff 引入），yaml.safe_load 取后者不报错，记录
3. 卡10 frontmatter related 仅 2 条 vs 正文关联节 5 条——存量不一致，未入 FAIL 清单，未动

**残余风险**：卡10 关键洞察表「指标异常说明」列（如「声音变现案例同款病灶」）系生产者基于源的合理外推，非逐字源文——无引号包装，符合转述标准。

**逐卡等级**：卡1 B+（重复节缺陷）/ 卡9 A- / 卡10 A- / 卡12 A / 卡14 A-；整单 **A-**。

**动作**：queue_transition review 617 pass A- → 5 卡 review_mark 翻转（status: enriched→reviewed、reviewed_by: 欧阳锋、review_date: 2026-09-02）→ 通过信息抄送王语嫣收件箱（含卡1 重复节小修落点）。
