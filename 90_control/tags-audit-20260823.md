# 全库标签摸底体检报告（#474 · 2026-08-23）

- 生成时间: 2026-08-23 20:33:15（治理进行中——数字随 #426 批次变动，收官以复扫归零为终态口径）
- 扫描范围: `30_wiki/` 全部卡（2876 张，只读零修改）
- 脏词率: 负向断言 0 + 课程名/来源混入 275（9.6%）| SOFT 观察: {} / 超长短语 {'>12字符': 6877}
- 来源轴缺失: 1234 张
- 空值/格式异常: 573 张（19.9%）

## ①a 脏词·负向断言清单（STRONG+PATTERN，三层分档口径）
- 无

## ①b 脏词·课程名/来源混入清单（#426 迁移映射口径，按域分组）

### ai-basic, ecommerce（1）
- `30_wiki\cases\case-live258-livestream-prompt-v1-v5.md` `scene:livestream` — 来源词混入内容 tag（应拆出来源词）
### ai-collaboration, yitang（3）
- `30_wiki\cases\case-ai-agent-milestone-design.md` `决策高度实操课口述` — 来源词混入内容 tag（应拆出来源词）
- `30_wiki\cases\case-yihang-dual-triangle-ai-organizational-behavior.md` `组织行为学的口述` — 来源词混入内容 tag（应拆出来源词）
- `30_wiki\cases\case-yihang-dual-triangle-tanzhaichao-ai-growth.md` `谭再超案例口述` — 来源词混入内容 tag（应拆出来源词）
### ai-saas, design（1）
- `30_wiki\concepts\aigc文创案例设计课leo文创ip从0到1全流程.md` `文创案例设计课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
### ai-saas, yitang（2）
- `30_wiki\dark-knowledges\dk-ai-judgment-human-responsibility.md` `时代判断力口述` — 来源词混入内容 tag（应拆出来源词）
- `30_wiki\dark-knowledges\dk-ai-judgment-programmer-paradox.md` `时代判断力口述` — 来源词混入内容 tag（应拆出来源词）
### content-production, marketing（1）
- `30_wiki\tools\tool-李诞-销售闭环验证：从0到1的重新定义.md` `文创案例设计课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
### decision-making, modeling（1）
- `30_wiki\tools\tool-cognitive-bias-12-check.md` `后见之明` — X之Y 课程名前缀（应拆为内容词）
### decision-science, ai-collaboration（1）
- `30_wiki\cases\case-decision-ai-assisted-vs-human.md` `决策高度实操课口述` — 来源词混入内容 tag（应拆出来源词）
### decision-science, yitang（3）
- `30_wiki\cases\case-decision-science-lunch-break-compression.md` `决策深度实操课口述` — 来源词混入内容 tag（应拆出来源词）
- `30_wiki\cases\case-decision-science-topcity-negative-revenue-rank.md` `决策实践实操课口述` — 来源词混入内容 tag（应拆出来源词）
- `30_wiki\dark-knowledges\dk-decision-when-to-defer.md` `决策高度实操课口述` — 来源词混入内容 tag（应拆出来源词）
### demand-analysis, yitang（3）
- `30_wiki\cases\case-demand-b2b-enterprise-erp.md` `决策高度实操课口述` — 来源词混入内容 tag（应拆出来源词）
- `30_wiki\cases\case-demand-b2c-consumer-insight.md` `决策高度实操课口述` — 来源词混入内容 tag（应拆出来源词）
- `30_wiki\dark-knowledges\dk-demand-signal-vs-noise.md` `决策高度实操课口述` — 来源词混入内容 tag（应拆出来源词）
### design（1）
- `30_wiki\tools\tool-月白-基于基础形象做动作延展（1到10）.md` `文创案例设计课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
### entrepreneurship（1）
- `30_wiki\concepts\yt-entrepreneur-research-camp.md` `调研行动营口述` — 来源词混入内容 tag（应拆出来源词）
### entrepreneurship, epistemic-foundations（1）
- `30_wiki\concepts\yt-entrepreneur-scientific-method.md` `第二节课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
### healthcare（1）
- `30_wiki\concepts\ai时代判断力口述.md` `时代判断力口述` — 来源词混入内容 tag（应拆出来源词）
### master（2）
- `30_wiki\concepts\master-antifragile-checklist.md` `决策高度实操课口述` — 来源词混入内容 tag（应拆出来源词）
- `30_wiki\concepts\master-decision-hygiene.md` `决策高度实操课口述` — 来源词混入内容 tag（应拆出来源词）
### product（2）
- `30_wiki\concepts\yt-product-kernel-aesthetic.md` `产品内核实操课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\concepts\yt-product-kernel-aesthetic.md` `产品内核迭代课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
### product, yitang（2）
- `30_wiki\dark-knowledges\yt-product-kernel-cost-sensitive-default-no.md` `{'signal': '成本敏感默认不——想加"高成本低信息"项', 'framework_lens': '这个价值项的成本高吗？对转化率的影响你确定吗？', 'follow_up_question': '如果加上去之后收入几乎不动、服务成本直接乘2-3倍，你还加吗？'}` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\frameworks\yt-product-kernel-iteration.md` `产品内核迭代课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
### src-unknown（151）
- `30_wiki\cases\case-truman-motivation-map-12-versions.md` `泛产品设计工具篇口述版` — 来源词混入内容 tag（应拆出来源词）
- `30_wiki\cases\case-truman-poker-deck-roi.md` `决策高度实操课口述` — 来源词混入内容 tag（应拆出来源词）
- `30_wiki\cases\case-一堂-陈贤敏汉堡-hypothesis-validation.md` `关键假设课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\concepts\concept-一堂-hypothesis-driven-business-methodology.md` `产品内核实操课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\concepts\concept-一堂-hypothesis-driven-business-methodology.md` `产品内核迭代课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\concepts\concept-一堂-hypothesis-driven-business-methodology.md` `产品内核验证课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\concepts\yt-barrier-brand-equity.md` `产品内核实操课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\concepts\yt-barrier-brand-equity.md` `产品内核验证课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\concepts\yt-barrier-culture-moat.md` `产品内核实操课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\concepts\yt-barrier-culture-moat.md` `产品内核验证课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\concepts\yt-barrier-data-assets.md` `产品内核实操课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\concepts\yt-barrier-data-assets.md` `产品内核验证课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\concepts\yt-barrier-defensive-strategy.md` `产品内核实操课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\concepts\yt-barrier-defensive-strategy.md` `产品内核验证课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\concepts\yt-barrier-network-effects-deep.md` `产品内核实操课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- …共 151 条
### time-management, marketing（2）
- `30_wiki\cases\case-yitang-copywriting-time-decomposition.md` `底层逻辑之一` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-yitang-copywriting-time-decomposition.md` `底层逻辑之一-Y模型` — X之Y 课程名前缀（应拆为内容词）
### yitang（8）
- `30_wiki\cases\case-gudong-tea-shop-foresight.md` `机会预判课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\cases\case-truman-yitang-foresight.md` `机会预判课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\cases\case-xiaolong-ecommerce-foresight.md` `机会预判课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\tools\tool-prompt-iceberg-demand-analysis.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\tools\tool-prompt-jtbd-scenario-coach.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\tools\tool-prompt-usp-quick-scan.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\tools\tool-一堂-product-kernel-add-subtract.md` `00_inbox/一堂-产品内核实操课-Truman-口述.txt L2378-L2416` — 来源词混入内容 tag（应拆出来源词）
- `30_wiki\tools\tool-一堂-product-kernel-add-subtract.md` `00_inbox/一堂-产品内核实操课-Truman-口述.txt L190-L194` — 来源词混入内容 tag（应拆出来源词）
### yitang, business-formula（1）
- `30_wiki\dark-knowledges\dk-yitang-business-formula-cd-loop-undo-key.md` `落地之夜第六场` — X之Y 课程名前缀（应拆为内容词）
### yitang, business-strategy（4）
- `30_wiki\cases\case-yitang-dongyuan-dance-retention-c-vs-d.md` `落地之夜第六场` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-yitang-xiezefeng-clothing-innovation-param.md` `落地之夜第六场` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-yitang-yewenbin-archery-business-formula.md` `落地之夜第六场` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-一堂-无人餐厅-hypothesis-failure.md` `关键假设课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
### yitang, decision-science（2）
- `30_wiki\cases\case-yitang-shishi-qiushi-pitfall-2-ignore-facts.md` `大坑之二` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-yitang-shishi-qiushi-pitfall-5-over-prediction.md` `大坑之五` — X之Y 课程名前缀（应拆为内容词）
### yitang, demand-analysis（6）
- `30_wiki\cases\case-demand-iceberg-few-shot.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\tools\tool-demand-chai-tui-ping-suan-guide.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\tools\tool-demand-micro-experience-script.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\tools\tool-demand-option-explorer.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\tools\tool-demand-rat-generator.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\tools\tool-demand-report-template.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
### yitang, five-step-method（34）
- `30_wiki\cases\case-demand-ai-fitness-four-forces.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-demand-dialer.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-demand-elderly-smart-device.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-demand-equestrian-three-tasks.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-demand-financial-literacy.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-demand-indonesia-insurance.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-demand-milkshake-jtbd.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-demand-pharma-bigdata.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-demand-restaurant-hiring.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-demand-rural-5g.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-demand-silver-parenting.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-demand-tier4-housekeeping.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-demand-travel-agent.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\dark-knowledges\dk-demand-feature-stacking.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\dark-knowledges\dk-demand-hidden-need.md` `五步法之需求分析` — X之Y 课程名前缀（应拆为内容词）
- …共 34 条
### yitang, growth（21）
- `30_wiki\cases\case-yitang-amazon-growth-flywheel.md` `一堂五步法之增长` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-yitang-lianjia-site-selection-industrialization.md` `一堂五步法之增长` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-yitang-maiyi-cloud-computer-channel.md` `一堂五步法之增长` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-yitang-novel-app-flywheel.md` `一堂五步法之增长` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-yitang-redburger-selection-industrialization.md` `一堂五步法之增长` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-yitang-shuzu-channel-scan-test.md` `一堂五步法之增长` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-yitang-solid-redbull-channel.md` `一堂五步法之增长` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-yitang-topcity-growth-flywheel.md` `一堂五步法之增长` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-yitang-xujian-invoice-saas-channel.md` `一堂五步法之增长` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-yitang-yitang-course-industrialization.md` `一堂五步法之增长` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-yitang-yitang-self-growth-channel.md` `一堂五步法之增长` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-yitang-yitang-shortvideo-industrialization.md` `一堂五步法之增长` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\cases\case-yitang-yitu-lead-industrialization.md` `一堂五步法之增长` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\concepts\concept-yitang-channel-lean-validation-bridge.md` `一堂五步法之增长` — X之Y 课程名前缀（应拆为内容词）
- `30_wiki\dark-knowledges\dk-yitang-channel-exploration-traps.md` `一堂五步法之增长` — X之Y 课程名前缀（应拆为内容词）
- …共 21 条
### yitang, key-assumptions（3）
- `30_wiki\concepts\concept-一堂-key-assumptions.md` `关键假设课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\frameworks\framework-一堂-关键假设-ABCD模型.md` `关键假设课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\tools\tool-一堂-关键假设-ABCD场景分类器.md` `关键假设课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
### yitang, lean-startup（1）
- `30_wiki\dark-knowledges\dk-tool-as-answer-trap.md` `关键假设课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
### yitang, research（15）
- `30_wiki\cases\case-liutao-douyin-team-leader-9m.md` `高阶情报调研课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\cases\case-liutao-electric-bike-localization.md` `高阶情报调研课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\cases\case-yitang-competitor-pricing-intelligence.md` `高阶情报调研课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\cases\case-yitang-consumer-offline-channel-decision.md` `用户调研实操课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\cases\case-yitang-doorstep-nail-service-context.md` `用户调研实操课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\cases\case-yitang-doorstep-pet-feeding-trust.md` `用户调研实操课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\cases\case-yitang-fake-interview-intelligence.md` `高阶情报调研课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\cases\case-yitang-hardware-factory-photo.md` `高阶情报调研课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\cases\case-yitang-jtbd-story-formula.md` `用户调研实操课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\cases\case-yitang-mvp-reward-interview-waste.md` `用户调研实操课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\cases\case-yitang-pet-fostering-user-research.md` `用户调研实操课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\cases\case-zhanglan-amusement-park-undercover.md` `高阶情报调研课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\concepts\concept-ceo-must-do-user-research.md` `用户调研实操课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\concepts\concept-research-delegation-in-scaling.md` `用户调研实操课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
- `30_wiki\tools\tool-yitang-user-interview-5steps.md` `用户调研实操课` — 课程名结尾（禁入 tags，source_refs 唯一归宿）
### yitang, sales（1）
- `30_wiki\tools\tool-yitang-payment-collection-playbook.md` `销售体系之二` — X之Y 课程名前缀（应拆为内容词）

## ② 来源轴缺失清单

- `30_wiki\_archive\concept-一堂-business-prediction.md` source_person=Truman source_context=一堂商业预判课（2026年）
- `30_wiki\_archive\plan_20260531_data-curator-v1.md` source_person=- source_context=（原 legacy，已从 title/context/filename 推断为 
- `30_wiki\_archive\research_methodology.md` source_person=- source_context=（原 legacy，已从 title/context/filename 推断为 
- `30_wiki\bridges\bridge-coaching-leadership-feature-layered.md` source_person=Truman source_context=教练式领导力探索营 × Feature分层体系 跨课桥接
- `30_wiki\bridges\bridge-dual-track-feature-system.md` source_person=欧阳锋/王语嫣 source_context=欧阳锋洞察3：cap_hub质量门禁Feature ≠ 课程解题Feature—
- `30_wiki\bridges\bridge-how-to-know-person-to-business.md` source_person=布鲁克斯 / 水水 source_context=
- `30_wiki\bridges\bridge-meeting-leadership-coaching.md` source_person=Truman source_context=科学开会系列课（认知篇+武器库上下篇）× 教练式领导力探索营
- `30_wiki\bridges\bridge-panproduct-kids-translation.md` source_person=崔磊 source_context=
- `30_wiki\bridges\bridge-个人复盘×知识管理W-Z-K-P.md` source_person=Truman source_context=Truman复盘课批注图230938（W-Z-K-P模型）
- `30_wiki\cases\case-4000-titles-ten-strategies.md` source_person=马易 source_context=Live259 爆炸式调研（2026-08-11 口述）——长期资产原型案例
- `30_wiki\cases\case-ai-assisted-review.md` source_person=Truman source_context=一堂高阶建模能力培训（AI 辅助复盘案例） （单一 source 为完整长文档，
- `30_wiki\cases\case-ai-learning-series-modeling.md` source_person=马易 source_context=Live259 爆炸式调研（2026-08-11 口述）——AI 学习各案例的量
- `30_wiki\cases\case-ai-pet-emotional-product.md` source_person=水水 source_context=水水一堂拆书会 AI宠物案例（L940-990）
- `30_wiki\cases\case-ai-writing-homogenization.md` source_person=一堂《吾辈如神》拆书会主讲人 / 老顽童整理 source_context=一堂《吾辈如神》拆书会（2026-07-01），讨论 AI 生成内容对表达多样性
- `30_wiki\cases\case-bmw-human-ai-collaboration-idle-time.md` source_person=《吾辈如神》拆书会主讲人 source_context=一堂《吾辈如神》拆书会（2026-07-01），讨论 AI 时代人机协作的未来
- `30_wiki\cases\case-child-drawing-rhyme.md` source_person=Truman source_context=一堂高阶建模能力培训（最小建模案例）。单一来源为完整口述稿，内容充分支撑 med
- `30_wiki\cases\case-coaching-dialogue-three-versions.md` source_person=莫非 source_context=教练式领导力探索营——三版本对话案例集
- `30_wiki\cases\case-course-milestone-model.md` source_person=Truman source_context=一堂高阶建模能力培训（课程里程碑模型案例），单一口述来源，内容支撑充分但待第二来
- `30_wiki\cases\case-cross-xingangwan-pharma.md` source_person=项目相关方（录音）/ 王语嫣（整理） source_context=跨域融合计划（策略 A）P1 案例卡；素材来自鑫港湾智慧药柜项目多份内部录音与 
- `30_wiki\cases\case-cross-yuanqi-forest.md` source_person=一堂课程讲义/讲师案例 source_context=一堂精益创业·低成本验证课程（元气森林试错工具箱幻灯片）+ 冉鹏战略课程战略选择
- `30_wiki\cases\case-cui-lei-kids-ai-design-class.md` source_person=崔磊 source_context=
- `30_wiki\cases\case-dental-clinic-formula.md` source_person=孔阳 source_context=一堂 2026-06-13 业务公式拆解培训，连锁口腔诊所案例（单次成交 & 长
- `30_wiki\cases\case-design-principles-90.md` source_person=马易 source_context=Live259 爆炸式调研（2026-08-11 口述）——AI demo 最完
- `30_wiki\cases\case-essence-education-strategy.md` source_person=Truman source_context=一堂高阶建模能力培训（本质建模案例）
- `30_wiki\cases\case-essence-entrepreneurship.md` source_person=Truman 的早期领导 source_context=一堂高阶建模能力培训（本质建模案例）（单一 source 为完整长文档，内容充分
- `30_wiki\cases\case-essence-humanity-trap.md` source_person=Truman source_context=一堂高阶建模能力培训（本质建模案例）（单一 source 为完整长文档，内容充分
- `30_wiki\cases\case-ether-online-acquisition.md` source_person=Truman source_context=一堂课程，规模经济章节；以太资本对接平台用全网调研能力扫描新上创业项目并自动化跟
- `30_wiki\cases\case-feishu-live259-l3-extraction.md` source_person=段王爷（南帝）实战 source_context=2026-08-15 提取 yitang.top/fs-doc Live259《
- `30_wiki\cases\case-feishu-minutes-extraction-attempt.md` source_person=段王爷（南帝）实战 source_context=2026-08-16 尝试提取 yitanger.feishu.cn 妙记逐字稿
- `30_wiki\cases\case-five-step-fake-vs-real-barriers.md` source_person=Truman source_context=一堂五步法壁垒篇
- `30_wiki\cases\case-five-step-growth-first-lever.md` source_person=Truman source_context=一堂五步法增长篇 + 增长周期模型
- `30_wiki\cases\case-friend-circle-aigc-transformation.md` source_person=楚门 source_context=AI×知识管理探索营（2026-08-15 晚直播）——朋友圈 AIGC 转型分
- `30_wiki\cases\case-guang-leng-dian-zi-hx-smj.md` source_person=黄药师 source_context=广冷电子 HX-SMJ 闸机红外光栅项目——四板卡（主控+红外A+红外B+继电器
- `30_wiki\cases\case-gudong-tea-shop-foresight.md` source_person=古董（一堂青岛中心主理人） source_context=Truman在商业预判课第一节课中讲解的预判案例，古董本人有独立完整课程
- `30_wiki\cases\case-gym-membership-formula.md` source_person=孔阳 source_context=一堂 2026-06-13 业务公式拆解培训，线下连锁健身续卡案例（持续复购型）
- `30_wiki\cases\case-hr-saas-feature-usage-trap.md` source_person=孔阳 source_context=一堂 2026-06-13 业务公式拆解培训，逻辑关系章节中的错误示范
- `30_wiki\cases\case-investment-claim-fact-check.md` source_person=楚门 source_context=AI×知识管理探索营（2026-08-15 晚直播）——事实核查案例（L2756
- `30_wiki\cases\case-jh-yitang-vs-sqlhelper.md` source_person=纪浩 source_context=AI俱乐部·人和AI协作（第六期AI共创社，2026-06）
- `30_wiki\cases\case-ji-hao-ai-workspace-chaos.md` source_person=纪浩 source_context=AI俱乐部·AI协作方法论分享（2026年）
- `30_wiki\cases\case-ji-hao-skill-market-problem-validation.md` source_person=纪浩 source_context=AI俱乐部·AI协作方法论分享（2026年）
- `30_wiki\cases\case-ji-hao-skills-market.md` source_person=纪浩 source_context=AI俱乐部-AI协作方法论 分享
- `30_wiki\cases\case-ji-hao-ui-design-constraint-evolution.md` source_person=纪浩 source_context=AI俱乐部·AI协作方法论分享（2026年）
- `30_wiki\cases\case-leadership-communication-failures.md` source_person=莫非 source_context=教练式领导力探索营——沟通失败案例分析
- `30_wiki\cases\case-lean-2b-gray-test.md` source_person=一堂课程讲师（自身业务复盘） source_context=一堂精益创业·低成本验证课程讲义
- `30_wiki\cases\case-lean-adult-education.md` source_person=一堂课程讲师（教学推演案例） source_context=一堂精益创业·低成本验证课程
- `30_wiki\cases\case-lean-building-in-vacuum.md` source_person=一堂课程讲师（教学案例） source_context=一堂精益创业·低成本验证课程
- `30_wiki\cases\case-lean-combination-test-paradigm.md` source_person=一堂课程讲师（含张磊洗发水项目复盘） source_context=一堂精益创业·低成本验证·系统测试曲线课程讲义
- `30_wiki\cases\case-lean-crayfish-combo-test.md` source_person=一堂课程讲师（教学案例） source_context=一堂精益创业·低成本验证·系统测试曲线课程讲义
- `30_wiki\cases\case-lean-electric-scooter-mvp.md` source_person=一堂课程讲师（教学推演案例） source_context=一堂精益创业·低成本验证实操课程
- `30_wiki\cases\case-lean-genki-forest-toolkit.md` source_person=一堂课程讲义/讲师案例 source_context=一堂精益创业·低成本验证课程（元气森林试错工具箱幻灯片）
- …共 1234 条

## ③ 域地图（有轴/无轴）

| 域 | 卡数 | 词池轴 |
|:--|--:|:--|
| yitang | 1182 | — |
| src-unknown | 388 | — |
| ai-collaboration | 354 | ✅ |
| design | 285 | — |
| research | 247 | — |
| management | 162 | — |
| strategy | 159 | — |
| unknown | 144 | — |
| master | 114 | — |
| decision-science | 112 | — |
| business-strategy | 103 | — |
| product | 97 | — |
| ai-saas | 96 | — |
| knowledge-management | 71 | — |
| kdo | 66 | — |
| business-formula | 66 | — |
| learning-methodology | 59 | — |
| modeling | 55 | — |
| conversion-rate | 50 | — |
| healthcare | 45 | — |
| five-step-method | 45 | — |
| personal-os | 43 | — |
| entrepreneurship | 42 | — |
| decision-making | 38 | ✅ |
| yihang | 36 | — |
| personal-growth | 35 | — |
| content-production | 34 | — |
| sales | 33 | — |
| panproduct | 32 | — |
| src_unknown | 27 | — |
| growth | 27 | — |
| demand-analysis | 26 | — |
| innovation | 25 | — |
| ai-basic | 23 | — |
| methodology | 21 | — |
| coaching | 20 | — |
| critical-thinking | 20 | — |
| business-judgment | 19 | — |
| system | 18 | — |
| time-management | 16 | — |
| lean-startup | 15 | — |
| profit-pricing | 15 | — |
| personal | 14 | — |
| agent-capability | 13 | — |
| human-insights | 13 | ✅ |
| ai | 13 | — |
| product-kernel | 12 | — |
| entrepreneur | 11 | — |
| ai-knowledge | 11 | — |
| wanghuan | 11 | — |
| pharmaceutical-retail | 10 | — |
| epistemic-foundations | 10 | — |
| personal-expression | 10 | — |
| human-ai-collaboration | 10 | — |
| agent | 10 | — |
| publishing | 9 | — |
| infrastructure | 9 | — |
| organization | 8 | — |
| operations | 8 | — |
| rust | 8 | — |
| note-taking | 8 | — |
| education | 7 | — |
| skill-building | 7 | — |
| feishu | 6 | — |
| marketing | 6 | — |
| b2b | 6 | — |
| concepts | 6 | — |
| e-commerce | 5 | — |
| organizational-transformation | 5 | — |
| wechat-video | 5 | — |
| key-assumptions | 5 | — |
| governance | 4 | — |
| consulting | 4 | — |
| pan-product | 4 | — |
| cross-domain | 4 | — |
| leadership | 4 | — |
| multimodal | 3 | — |
| extraction | 3 | — |
| browser-automation | 3 | — |
| saas | 3 | — |
| policy-compliance | 3 | — |
| business | 3 | — |
| ai-native | 3 | — |
| opportunity-foresight | 3 | — |
| agent-engineering | 3 | — |
| compliance | 3 | — |
| finance-legal | 3 | — |
| research-methodology | 3 | — |
| unit-economics | 2 | — |
| communication | 2 | — |
| supply-chain | 2 | — |
| risk-warning | 2 | — |
| content-extraction | 2 | — |
| finance | 2 | — |
| financial-model | 2 | — |
| hermes | 2 | — |
| mcp | 2 | — |
| psychology | 2 | — |
| agent-infrastructure | 2 | — |
| kdo-infrastructure | 2 | — |
| bridge | 2 | — |
| decision | 2 | — |
| organizational-design | 2 | — |
| personal-learning | 2 | — |
| production | 1 | — |
| content-industry | 1 | — |
| manufacturing | 1 | — |
| essence | 1 | — |
| electronics | 1 | — |
| hardware-debugging | 1 | — |
| ecommerce | 1 | — |
| user-research | 1 | — |
| talent | 1 | — |
| content | 1 | — |
| 工作汇报 | 1 | — |
| 复盘结构化 | 1 | — |
| personal-productivity | 1 | — |
| wechat-article | 1 | — |
| toutiao-video | 1 | — |
| real-estate | 1 | — |
| call-center | 1 | — |
| personal-knowledge-management | 1 | — |
| multi-agent | 1 | — |
| organizational-politics | 1 | — |
| r-and-d | 1 | — |
| patent | 1 | — |
| hospitality | 1 | — |
| content-moderation | 1 | — |
| industrial-ai | 1 | — |
| interior-design | 1 | — |
| productivity | 1 | — |
| presentation | 1 | — |
| 组织激励 | 1 | — |
| 模型质量管理 | 1 | — |
| fintech | 1 | — |
| content-operations | 1 | — |
| validation | 1 | — |
| economics | 1 | — |
| architecture | 1 | — |
| 卖点直给 | 1 | — |
| 价值感 | 1 | — |
| 讲香价值 | 1 | — |
| o2o | 1 | — |
| 软件交付 | 1 | — |
| pan-product-design | 1 | — |
| product-execution | 1 | — |
| unit-model | 1 | — |
| needs-review | 1 | — |
| skill-engineering | 1 | — |
| tob | 1 | — |
| business-model | 1 | — |
| capability-hub | 1 | — |
| knowledge-graph | 1 | — |
| workflow | 1 | — |
| quality | 1 | — |
| meta-methodology | 1 | — |
| 个人表达力 | 1 | — |
| 火箭模型×十指讲香 | 1 | — |
| 表达力总框架 | 1 | — |
| 私域电商 | 1 | — |
| 销售流程 | 1 | — |
| deliberate-practice | 1 | — |
| personal-development | 1 | — |
| design-thinking | 1 | — |
| field-research | 1 | — |
| prompt-engineering | 1 | — |
| ai-tooling | 1 | — |
| html | 1 | — |
| prezi | 1 | — |
| wechat | 1 | — |
| data-extraction | 1 | — |
| meta | 1 | — |
| engineering | 1 | — |
| team | 1 | — |
| project | 1 | — |
| reading-methodology | 1 | — |
| hr | 1 | — |
| 心理学 | 1 | — |
| 噪声减少 | 1 | — |
| video-production | 1 | — |
| ai-agent | 1 | — |
| market-positioning | 1 | — |
| business-design | 1 | — |
| retail | 1 | — |
| capability | 1 | — |
| problem-solving | 1 | — |
| competitive-analysis | 1 | — |
| platform | 1 | — |
| planning | 1 | — |

## ④ 空值/格式异常清单

- `30_wiki\_archive\obsidian-kdo-内容产出工作流-产品设计大纲.md`: tags 缺失
- `30_wiki\_archive\panproduct\yt-panproduct-demand-five-step-method.md`: tags 缺失
- `30_wiki\_archive\panproduct\yt-panproduct-execution-10x-validation.md`: tags 缺失
- `30_wiki\_archive\panproduct\yt-panproduct-execution-business-modeling.md`: tags 缺失
- `30_wiki\_archive\panproduct\yt-panproduct-execution-core-and-boundary.md`: tags 缺失
- `30_wiki\_archive\panproduct\yt-panproduct-execution-design-principles.md`: tags 缺失
- `30_wiki\_archive\panproduct\yt-panproduct-execution-good-tools.md`: tags 缺失
- `30_wiki\_archive\panproduct\yt-panproduct-execution-hypothesis-decomposition.md`: tags 缺失
- `30_wiki\_archive\panproduct\yt-panproduct-execution-idea-spark.md`: tags 缺失
- `30_wiki\_archive\panproduct\yt-panproduct-execution-incubation-polish.md`: tags 缺失
- `30_wiki\_archive\panproduct\yt-panproduct-execution-liberate-thinking.md`: tags 缺失
- `30_wiki\_archive\panproduct\yt-panproduct-execution-logic-mece.md`: tags 缺失
- `30_wiki\_archive\panproduct\yt-panproduct-execution-low-cost-mvp.md`: tags 缺失
- `30_wiki\_archive\panproduct\yt-panproduct-execution-management-trilogy.md`: tags 缺失
- `30_wiki\_archive\panproduct\yt-panproduct-execution-milestone-breakdown.md`: tags 缺失
- `30_wiki\_archive\panproduct\yt-panproduct-execution-realistic-simulation.md`: tags 缺失
- `30_wiki\_archive\panproduct\yt-panproduct-execution-review-iteration.md`: tags 缺失
- `30_wiki\_archive\panproduct\yt-panproduct-execution-risk-management.md`: tags 缺失
- `30_wiki\_archive\panproduct\yt-panproduct-execution-roi-analysis.md`: tags 缺失
- `30_wiki\_archive\panproduct\yt-panproduct-execution-war-room.md`: tags 缺失
- `30_wiki\_archive\research_methodology.md`: tags 缺失
- `30_wiki\_archive\紫鲸ai_智能体工作流平台_深度分析与产品设计.md`: tags 缺失
- `30_wiki\cases\case-strategy-failure-04-appliance.md`: tags 缺失
- `30_wiki\cases\case-strategy-failure-05-it.md`: tags 缺失
- `30_wiki\cases\case-strategy-failure-06-phone-n.md`: tags 缺失
- `30_wiki\cases\case-strategy-failure-09-boeing.md`: tags 缺失
- `30_wiki\cases\case-strategy-m-brand-profit-model.md`: tags 缺失
- `30_wiki\cases\case-strategy-practice-11-third-place.md`: tags 缺失
- `30_wiki\cases\case-strategy-practice-12-zero-loss.md`: tags 缺失
- `30_wiki\cases\case-strategy-retailer-activity-scope.md`: tags 缺失
- `30_wiki\cases\case-strategy-revival-13-bestore.md`: tags 缺失
- `30_wiki\cases\case-wechat-5291b61bc722d90d.md`: tags 缺失
- `30_wiki\cases\case-wechat-6725b942182f6277.md`: tags 缺失
- `30_wiki\cases\case-wechat-article_4dd7be7cd82f7e80.md`: tags 缺失
- `30_wiki\cases\case-wechat-AWyGiJIRgc.md`: tags 缺失
- `30_wiki\cases\case-wechat-dy_7666832665312982138.md`: tags 缺失
- `30_wiki\cases\case-wechat-f4faadff37c0b43b.md`: tags 缺失
- `30_wiki\cases\case-wechat-tt_7666646931699367986.md`: tags 缺失
- `30_wiki\cases\case-yihang-dual-triangle-AI三角-场景.md`: tags 缺失
- `30_wiki\cases\case-yihang-dual-triangle-AI三角-基本功.md`: tags 缺失
- `30_wiki\cases\case-yihang-dual-triangle-AI三角-数据.md`: tags 缺失
- `30_wiki\cases\case-yihang-dual-triangle-AI可以落地的场景假设.md`: tags 缺失
- `30_wiki\cases\case-yihang-dual-triangle-AI场景.md`: tags 缺失
- `30_wiki\cases\case-yihang-dual-triangle-AI基本功.md`: tags 缺失
- `30_wiki\cases\case-yihang-dual-triangle-AI数据.md`: tags 缺失
- `30_wiki\cases\case-yihang-dual-triangle-一堂DOC-20260704025752.md`: tags 缺失
- `30_wiki\cases\case-yihang-dual-triangle-一堂双三角-AI企业经营数据分析.md`: tags 缺失
- `30_wiki\cases\case-yihang-dual-triangle-一堂双三角-AI时代的竞争力武器库.md`: tags 缺失
- `30_wiki\cases\case-yihang-dual-triangle-一堂双三角-AI落地五部曲.md`: tags 缺失
- `30_wiki\cases\case-yihang-dual-triangle-一堂双三角-一个引擎-三阶六变.md`: tags 缺失
- …共 573 条

## 治理优先级建议

- 脏词/空值: 按域分批治理（#426 模式放量，首批已归零的决策域为模板）
- 来源轴缺失: 建议批量补来源词（拆书/Live/开放麦批次）
- 无轴域: 词池轴建设随素材驱动（#426 词表 v0.3 六轴可复用）

*tags-audit.py 生成 · #474 · 只读扫描零修改*
