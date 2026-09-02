---
id: task_20260902_ouyangfeng-unverified-reviewed-cards-batch-review
title: 14 张无终审佐证 reviewed 卡批量补审（E018 家族历史遗留，#613 上报清单裁定）
seq: 614
status: in_progress
assignee: ouyangfeng
created_by: wangyuyan
created_at: 2026-09-02
decision_source: null
reviewer: 王语嫣（编排层复核落点）
instance: ouyangfeng-kimi
updated_at: '2026-09-02T03:12:31.772327+00:00'
---

# #614 十四张无佐证 reviewed 卡批量补审（欧阳锋）

## 背景

#613 排查实证（两轮，yaml 全库扫）：14 张卡 `status: reviewed` 但无任何卡级终审记录——其中轮 2 的 7 张产品内核族铁证：status 翻转发生在 vault backup commit（e20cbce48）里，review_date 是生产者创建日自填，全库 grep 无欧阳锋 PASS 记录。清单与证据链：`60_feedback/tasks/task_20260902_laowantong-586batch-reviewedby-residue-fix/排查补齐报告-613.md` §3（3.1 七张 + 3.2 七张）。

## 任务

对 14 张卡逐张给补审裁定（证据包已在报告 §3，卡本身在 30_wiki 可读）：

- **过**：内容达标 → 裁定 PASS + grade，我安排补齐 frontmatter（reviewed_by/review_date=补审日）
- **不过**：内容不达标 → 裁定降级 enriched（或 FAIL 点清单），进正常返工流
- **拿不准**：标注需深审，单列

## 边界

- 你只下裁定不动卡片 frontmatter（写审分离）；落笔由老顽童按你的裁定执行
- 14 张清单以报告 §3 为准，不扩 scope

## 交付

- 14 行裁定表（卡 id → PASS+grade / 降级+理由 / 需深审）落本任务单执行报告节
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 614）

## 执行报告

**交付物**：本节 14 行裁定表（终审意见书，先落盘再跑脚本，O9）；系统性模式建议书 `60_feedback/diagnosis/prop_20260902_ouyangfeng-586batch-fake-quotes-and-ref-drift.md`。

**完成内容**：14 张卡逐张全量通读（合计 3145 行）+ O0 溯源核查（4 路并行核查员，打开每张卡 source_refs 指向的源文件，对关键数字/引言/行号逐条对源，取证含源文件行号+原文摘句）→ 逐张下裁定：PASS 9（A-×4 / B+×5）、降级 enriched 5、需深审 0。

**验证**：源文件存在性逐条核（卡 12 两张 source_refs 文件名死链实测不存在，真实源为「机会预判课」文件）；关键声明对源——卡 4 7/7 命中、卡 5 核心 6 条命中、卡 6 6/6、卡 7 7/7、卡 8 六项全命中、卡 9 框架本体命中但 2 处伪引文、卡 10 指标清单与源仅 1/10 重合、卡 11 五句引言逐字命中、卡 13 三案例+行号命中、卡 14 结构论述命中但核心引文块系拼贴、卡 3 source_refs 5/5+related 8/8 存在。裁定一致性原则：**编造（伪引文/无源核心内容）→ 降级；标注不准（区间错位/文件名错但源真实存在且内容吻合）→ PASS 记缺陷**。

**边界**：未动任何卡片 frontmatter 与正文（写审分离，落笔归老顽童）；清单严格以排查补齐报告-613 §3 的 14 张为准，未扩 scope；500 张缺 review_date 历史欠账按报告 §4 边界不动。

**需要谁动作**：① 老顽童落笔——9 张 PASS 卡补 `reviewed_by: 欧阳锋`/`review_date: 2026-09-02`/`grade: <见裁定表>`（走 `review_mark.py`，非空不覆盖）；5 张降级卡 status 改回 enriched 进返工流，按各行 FAIL 点修复后重报终审；裁定表中「落笔时随修」项（卡 3 两处路径、卡 5/6/7/8 引用区间、卡 11/13 diagnostic_signals 结构）随本轮落笔一并修。② 王语嫣编排层复核落点 + 裁定建议书。

### 14 张卡裁定表（2026-09-02 欧阳锋补审）

| # | 卡 id | 类型 | 裁定 | 理由（对源证据） |
|:--|:--|:--:|:--|:--|
| 1 | dk-p15-unverified | dk | **降级 enriched** | 六段模板四段（使用场景/操作方法/适用边界/为什么值钱）+关联节全 `src_unknown` 占位——格式合规但内容空洞，reviewed 不成立；源已不可溯（source_refs=src_unknown），按 `.agent/pitfalls.md` P-15 原始条目重写六段后重审 |
| 2 | high-density-composite-compilation-strategy | decision | **PASS B+** | 决策本体（v1.0 错误分析/v2.0 细粒度卡+Hub 层/三阶段执行/验收标准）完整自洽，系内部决策记录，src_unknown 源可接受；缺陷不阻断：禁止事项节 5 条占位、阶段三验证「待补充链接」、related 仅 2 条 |
| 3 | tool-kdo-wechat-serendipity-collect | tool | **PASS A-** | source_refs 5/5 存在、related 8/8 无死链、guide §六运维节在、管线当日仍在产（#607/#608 实证）；缺陷落笔随修：§Skill 挂载声明的 `.claude/skills/wechat-serendipity-collect/` 不存在（声明失实）、组件表 `kdo-tools/yuanbao_cookie_extract.py` 路径错（实际在 40_outputs/code/scripts/） |
| 4 | case-qinpeng-iot-module-tiering | case | **PASS B+** | 7/7 关键声明对源命中（同行130卖69 L1426-1428/市占5%→20% L1436/便宜20%够+回调 L1480-1488/千三万一良品率 L1512/四格矩阵 L1580-1606/过亿两轮1亿市场第二 L1642-1646/淘宝日10-20人 L1396-1398）；缺陷：无外部 Critique、失败模式节重复两段 |
| 5 | case-shampoo-product-kernel | case | **PASS A-** | 核心叙事 6 条全命中（张磊 L1026/二三十瓶 L1110/两专家 L1134/牛奶金句 L1138-1142/四步路径/高级成分 L1148），Critique 双外部攻击者（Kotler/Ries）达标；缺陷落笔随修：迭代课两引用区间指错段落（排列组合实际在 L2916-2944）、卖点矩阵真实但依赖未列入 refs 的 OCR 源 `src_20260611_89407193`——补引用即可 |
| 6 | case-yitang-chuanhe-seasoning-kernel | case | **PASS B+** | 6/6 数字命中（3万→五六百线索→3-4单 L322-336/V2 7-8家 L432/V3 稳定30家 L466/3万→6万团队20人 L478/万店亿收 L650）；缺陷：第二引用区间错位（L700-1150 是车库案例）、「V6.0」编号系卡片自构（源止于 5.0，品类扩展是结果汇报）需注明 |
| 7 | case-yitang-zhongzheng-parking-garage | case | **PASS B+** | 7/7 全数字命中（12vs8车位翻1.5倍 L882/1.4万vs2.5万 L900-948/传感器4→2200组8个月 L986-996/15人2月→2人2天4000指标 L1066-1100/毛利8-9% L726/4城3000位6000万 L1136-1142）；缺陷：第二引用区间错位（L2069-2253 是自习室段） |
| 8 | yt-product-kernel-iteration | framework | **PASS A-** | 五方向命名/六段位（L96-150）/自习室80cm60cm窗帘45平19座（L2144-2168）/猫粮三段（L2834-2856）/银行风控3天2人30+行（L3304-3356）/一堂讲课40-50%（L2224-2228）全命中，十段结构+7失败模式齐；缺陷落笔随修：猫粮案例行号（L2824-2900）未列入来源区间、笔记标注 11KB 实测 10.3KB |
| 9 | yt-product-kernel-validation | framework | **降级 enriched** | 🔴 两处加引号「Truman 原话」查无原文：三维度「必须有/来了更好/走得通」整段零命中；「大多数人的默认选择是赌——你们知道有多少人是这样创业的吗」零命中（真实原句在 L1956/L2078-2086）。框架本体（三维度/六策略/访谈前两原则）对源成立——伪逐字引文触 O0 红线，FAIL 点=替换为真实原句或改转述，修后重审 |
| 10 | yt-product-kernel-ten-metrics | tool | **降级 enriched** | 🔴 核心失真：卡列十大指标（精准度/CAC/试训/关键转化/激活/付费转化/功能使用/复购/NPS/流失）与全部三个源文件清单（销转率/动销率/捕获率/留存率/完课率/退款率/满意率/复购率/续费率/推荐率）仅复购一项重合——标题承诺的指标体系无源，系外部通用增长指标移植；叠加下半部 4 节占位+操作步骤待补充。FAIL 点=按源重写核心指标表+补齐占位节 |
| 11 | yt-product-kernel-do-without-belief | dk | **PASS A-** | 小鹅通引言五句逐字命中（L2782/2792/2794/2796/2798）、六段+Critique+失败模式齐、解构忠实原意；缺陷落笔随修：frontmatter diagnostic_signals 5 条 `signal: src_unknown` 待补 |
| 12 | concept-一堂-business-prediction | concept | **降级 enriched** | 🔴 source_refs 两文件名死链（「商业预判课」不存在，真实源=「机会预判课」，内容主体可信）；⑦「ToB 内训 4×5=20 格子矩阵」引言虚构（L2282-2306 实为请 AI 做加法段，且 5×3=15≠20 自相矛盾）；④「保A争B差距不超过2个阶段」与源不符（L1912：建议差1、最多差3）。主体（P/L型 L298/光谱七阶段 L1538-1546/15字诀 L1172-1190/三类硬伤/小峰案例 L586-588）已核可信——FAIL 点=修文件名+删换⑦+修正④，修后重审 |
| 13 | yt-product-kernel-cost-sensitive-default-no | dk | **PASS B+** | 三案例+行号+「成本乘2-3倍收入几乎不动」（L2686-2688）+蓝翼三连追问（L2700-2706）全命中；缺陷：①「同学互评+优秀作业展示」无源（全文+笔记均无）需标注为建议或删 ②红色引言系拼接改写（语义一致，源 L2606）建议改转述 ③frontmatter diagnostic_signals 空、signal 条目错置于 tags 下——随落笔修 |
| 14 | yt-product-kernel-overpromise-trap | dk | **降级 enriched** | 🔴 核心证据块失真：「原始表述」引号块包装成 Truman 口述（标 L524-L568）实为改写拼贴、全文无逐字版本；「月入过万」无源（源为「一个星期就能把钱赚回来」L534）；「Truman 的诊断」长引文系改写。结构性论述（前后端 KPI 不一致/Q6 引用属实/L2480 逐字）成立——FAIL 点=引文块改转述或换真实原句+删「月入过万」，修后重审 |

**裁定统计**：PASS 9（A-：卡 3/5/8/11；B+：卡 2/4/6/7/13）｜降级 enriched 5（卡 1/9/10/12/14）｜需深审 0。

### 出口自检（建议书钩子）

本批发现跨卡系统性模式（非单卡内容缺陷，属生产纪律问题）——已落建议书 `60_feedback/diagnosis/prop_20260902_ouyangfeng-586batch-fake-quotes-and-ref-drift.md`：
1. **伪逐字引文**（3 张：卡 9/12/14）——改写/拼贴包装成「Truman 原话+行号」，O0 对源才暴露；
2. **source_refs 行号区间/文件名漂移**（5 张：卡 5/6/7/8/12）——区间指错段落或文件名不存在但真实源存在；
3. 建议：老顽童生产闸门加「引号内容必须逐字对源（grep 命中）+ source_refs 区间抽验」两项机械检查。
4. 摩擦记录：`queue_transition.py claim` 落盘时将本任务单 frontmatter `decision_source` 原值抹为 null——建议脚本保留既有非空字段（随建议书一并上报）。
