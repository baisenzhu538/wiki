# 30_wiki 知识卡基线扫描报告

> 生成时间：2026-06-15 01:02:03
> 扫描范围：`30_wiki/` 下所有 `.md` 文件
> 总卡片数：1313

## 一、整体概况

| 指标 | 数量 | 占比 |
|---|---|---|
| 总卡片数 | 1313 | 100% |
| draft 状态 | 617 | 47.0% |
| enriched 状态 | 531 | 40.4% |
| stable 状态 | 11 | 0.8% |
| 无 source_refs | 219 | 16.7% |
| 无 author | 1216 | 92.6% |
| 无 reviewed_by | 978 | 74.5% |
| 空壳/微小文件 | 0 | 0.0% |
| 高置信低信任 | 152 | 11.6% |

## 二、问题标签分布

| 问题标签 | 数量 | 占比 |
|---|---|---|
| no-author | 1216 | 92.6% |
| no-trust-level | 1095 | 83.4% |
| no-reviewer | 978 | 74.5% |
| no-confidence | 971 | 74.0% |
| draft | 617 | 47.0% |
| no-source | 219 | 16.7% |
| high-conf-low-trust | 152 | 11.6% |
| high-conf-no-trust | 150 | 11.4% |
| no-id | 94 | 7.2% |
| no-title | 28 | 2.1% |
| no-status | 21 | 1.6% |
| no-type | 16 | 1.2% |
| theme-source | 5 | 0.4% |

## 三、按目录问题分布

| 目录 | draft | no-source | no-author | no-reviewer | empty-or-tiny | high-conf-low-trust |
|---|---|---|---|---|---|---|
| cases | 20 | 0 | 35 | 23 | 0 | 12 |
| concepts | 427 | 153 | 966 | 754 | 0 | 125 |
| dark-knowledges | 112 | 4 | 122 | 114 | 0 | 2 |
| decisions | 34 | 36 | 34 | 38 | 0 | 0 |
| entities | 0 | 5 | 6 | 2 | 0 | 0 |
| frameworks | 3 | 3 | 9 | 7 | 0 | 1 |
| projects | 0 | 3 | 3 | 3 | 0 | 0 |
| systems | 3 | 10 | 6 | 8 | 0 | 0 |
| tools | 18 | 5 | 35 | 29 | 0 | 12 |

## 四、Author 分布（前 30）

| Author | 数量 |
|---|---|
| (no author) | 1216 |
| 老顽童 | 54 |
| 王语嫣 | 22 |
| 黄药师 | 7 |
| 孔阳 | 5 |
| 黄药师（基于 Truman 口述提取） | 4 |
| 审查者欧阳锋 | 2 |
| 黄药师（Builder） | 1 |
| 黄药师 (Builder) | 1 |
| 周伯通 | 1 |

## 五、Reviewer 分布（前 30）

| Reviewer | 数量 |
|---|---|
| (no reviewer) | 978 |
| 黄药师 | 154 |
| 老顽童 | 90 |
| laowantong | 33 |
| 周伯通 | 15 |
| ['黄药师', 'laowantong'] | 12 |
| 洪七公 | 10 |
| 老顷童（精修） | 7 |
| Claude | 7 |
| 黄药师（Builder体验Producer） | 3 |
| 欧阳锋 | 2 |
| 老顷童 | 2 |

## 六、Domain 分布（前 50）

| Domain | 数量 |
|---|---|
| yitang | 510 |
| design | 230 |
| master | 104 |
| ai-collaboration | 96 |
| ai-saas | 53 |
| product | 45 |
| healthcare | 42 |
| business-strategy | 30 |
| modeling | 25 |
| ai | 25 |
| learning-methodology | 18 |
| entrepreneur | 17 |
| personal-growth | 15 |
| personal | 14 |
| consulting | 10 |
| note-taking | 8 |
| education | 6 |
| pharmaceutical-retail | 6 |
| ['ai-saas'] | 6 |
| AI | 6 |
| kdo | 6 |
| 决策 | 5 |
| skill-engineering | 4 |
| management | 4 |
| ['master'] | 4 |
| ['healthcare'] | 4 |
| agent-infrastructure | 3 |
| policy-compliance | 3 |
| learning | 3 |
| SaaS | 3 |
| execution | 2 |
| product-design | 2 |
| decision-making | 2 |
| product-strategy | 2 |
| risk-warning | 2 |
| ['yitang'] | 2 |
| structured-thinking | 2 |
| 产品 | 2 |
| 信息素养 | 2 |
| 落地 | 2 |
| 认知 | 2 |
| 分销系统 | 2 |
| financial-model | 2 |
| 私域电商 | 2 |
| decision-science | 2 |
| personal-life | 1 |
| strategy | 1 |
| entrepreneurship | 1 |
| essence | 1 |
| user-research | 1 |

## 七、高危卡片清单（示例）

以下卡片同时存在多个高危问题标签，需优先处理：

| 文件路径 | 状态 | Author | Reviewer | Source数 | Confidence | Trust | 问题标签 |
|---|---|---|---|---|---|---|---|
| 30_wiki/concepts/ai单元模型口述蒋老师.md | enriched | (空) | (空) | 1 | 0.85 | (空) | no-author;no-reviewer;high-conf-low-trust;high-conf-no-trust;no-trust-level |
| 30_wiki/concepts/kdo-flywheel.md | stable | (空) | (空) | 0 | (空) | (空) | no-id;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/kdo-yaml-frontmatter-safety.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/knowledge-error-self-exposure.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/master-ai-info-literacy.md | enriched | (空) | (空) | 1 | 0.9 | (空) | no-author;no-reviewer;high-conf-low-trust;high-conf-no-trust;no-trust-level |
| 30_wiki/concepts/master-antifragile-checklist.md | enriched | (空) | (空) | 1 | 0.88 | (空) | no-author;no-reviewer;high-conf-low-trust;high-conf-no-trust;no-trust-level |
| 30_wiki/concepts/master-cognitive-bias-checklist.md | enriched | (空) | (空) | 1 | 0.85 | (空) | no-author;no-reviewer;high-conf-low-trust;high-conf-no-trust;no-trust-level |
| 30_wiki/concepts/master-decision-hygiene.md | enriched | (空) | (空) | 1 | 0.9 | (空) | no-author;no-reviewer;high-conf-low-trust;high-conf-no-trust;no-trust-level |
| 30_wiki/concepts/master-first-principles.md | enriched | (空) | (空) | 1 | 0.85 | (空) | no-author;no-reviewer;high-conf-low-trust;high-conf-no-trust;no-trust-level |
| 30_wiki/concepts/master-systems-thinking.md | enriched | (空) | (空) | 1 | 0.85 | (空) | no-author;no-reviewer;high-conf-low-trust;high-conf-no-trust;no-trust-level |
| 30_wiki/concepts/research_methodology.md | superseded | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-AI场景探索STAR模型.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-AI工具选型决策.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-AI时代IPO模型重构.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-AI时代提示词优化法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-AI能力分层学习路径.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-AI辅助思考伙伴养成.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-AI输出审慎判断与交付确认.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-Feature特性层训练法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-Skill全生命周期管理.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-XY-Problem识别与真实问题定位.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-上下文质量管理（AI协作）.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-个人判断力系统建设（达克效应应对）.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-人在环渐进自动化策略.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-低质量动作识别与拒绝.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-信息输入持续补全（防AI错误累积）.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-判断力产品化与系统赋能.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-双三角模型应用.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-复杂项目AI落地稳定性保障.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-多Agent通信协作方案.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-开源模型与商业模型融合方案.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-技术社区严肃提问法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-提示词优化底层方法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-数学题与语文题区分法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-本地记忆与云端记忆管理.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-知识库最佳实践构建.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-短视频自动化上传工作流.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-科学提问法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-职场异步协作提问法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-语义对齐沟通法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-Truman-问题定义澄清法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-ai-ai-workspace-setup.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-ai-evidence-check.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-ai-narrative-test.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-ai-old-small-checklist.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-ai-oral-spray-input.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-ai-parallel-validation.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-ai-prd-for-ai.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-ai-problem-validation.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-ai-purpose-bias-check.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-ai-system-redundancy.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-ai-voice-input-doubao.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-李诞-个人IP的重新定义与输出策略.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-李诞-内容创作中的观察训练法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-李诞-判断工作价值的交易成本视角.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-李诞-短视频-脱口秀创作：从-风格-自然-的无效建议中解脱.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-李诞-销售闭环验证：从0到1的重新定义.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-李诞-阅读重读机制：与书籍的-因缘-相遇.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-李诞-面对过去错误的平静心法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-水水-保持系统冗余.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-水水-利用叙事驱动决策.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-水水-利用基因漂变视角.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-水水-区分风险与不确定性.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-水水-接受发散性世界观.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-水水-构建自利叙事.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-水水-用感性维度构建溢价.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-水水-练习坦然说不知道.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-水水-警惕概率虚妄安全感.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-水水-警惕错误归因.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-水水-识别关键偶然因素.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-水水-识别数据折磨陷阱.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-水水-识别模型局限性.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-水水-识别自证预言陷阱.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-水水-识别超级传播者风险.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-水水-识别饥饿效应.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-水水-避免原生家庭万能归因.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-水水-降低故事逻辑要求.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-纪浩-AI使用边界管理法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-纪浩-AI工具脚本化约束.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-纪浩-Agent开工检查单制作法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-纪浩-Problem与Question区分法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-纪浩-任务交付物标准化.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-纪浩-低成本输出验证法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-纪浩-处理AI生成代码运行异常.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-纪浩-多视角切换思考法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-纪浩-新手心态启动法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-纪浩-案例池构建法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-纪浩-线上问题应急值守.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-纪浩-评估AI从零写UI的可行性.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-纪浩-识别AI不可维护代码.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-纪浩-里程碑验证法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-纪浩-问题导向备课法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-纪浩-项目启动五问法.md | draft | (空) | (空) | 0 | (空) | (空) | draft;no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-问题驱动式深度思考笔记.md | draft | (空) | (空) | 1 | 0.86 | (空) | draft;no-author;no-reviewer;high-conf-low-trust;high-conf-no-trust;no-trust-level |
| 30_wiki/concepts/skill-马易-AI任务拆解提升控制度.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-马易-AI搜索公网数据增强（合规边界）.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-马易-AI答疑运营风格适配.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-马易-AI能力团队复制.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-马易-AI落地前置条件验证.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |
| 30_wiki/concepts/skill-马易-AI落地四阶段验证法.md | needs-review | (空) | (空) | 0 | (空) | (空) | no-author;no-reviewer;no-source;no-confidence;no-trust-level |

> 注：完整清单见 `kcard-inventory-2026-06-14.csv`，共 1057 张高危卡片。

## 八、下一步建议

1. **阶段 1 元数据治理**：先为无 author/reviewer/id 的卡片补全基础字段；
2. **阶段 2 高危清理**：优先处理 `empty-or-tiny`、`no-source` + `no-author` + `no-reviewer` 的卡片；
3. **阶段 3 作者审查**：从老顽童、黄药师等关键作者开始；
4. **阶段 4/5 分层与 domain 审查**：按可信度和业务域抽样深入。
