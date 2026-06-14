# 阶段 4 可信度分层批量修正日志

**处理时间**：2026-06-15  
**处理范围**：30_wiki 全库 1339 张卡片  
**处理规则**：
- 缺失 confidence：按 status/source 填充默认值
- 缺失 trust_level：按 status/source/confidence 填充默认值
- 高置信低来源：confidence ≥ 0.95 → 0.85；0.90–0.94 → 0.80

## 统计

- 补充 confidence：968 张
- 补充 trust_level：1095 张
- 下调 confidence：19 张
- 跳过（无 frontmatter）：6 张
- 跳过（YAML 解析错误）：0 张

## 详细变更清单

### `wiki\30_wiki\cases\case-ether-online-acquisition.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\cases\case-five-step-fake-vs-real-barriers.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\cases\case-five-step-growth-first-lever.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\cases\case-gudong-tea-shop-foresight.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\cases\case-jh-yitang-vs-sqlhelper.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\cases\case-milktea-five-step.md`
- 补充 confidence: 0.85
- 补充 trust_level: high

### `wiki\30_wiki\cases\case-shampoo-product-kernel.md`
- 补充 confidence: 0.85
- 补充 trust_level: high

### `wiki\30_wiki\cases\case-treadmill-demand-analysis.md`
- 补充 confidence: 0.85
- 补充 trust_level: high

### `wiki\30_wiki\cases\case-truman-ai-partner.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\cases\case-truman-motivation-map-12-versions.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\cases\case-truman-personal-growth-map-creation.md`
- confidence 从 0.9 下调至 0.8（source 仅 1 个）

### `wiki\30_wiki\cases\case-truman-poker-deck-roi.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\cases\case-truman-prd-checklist-evolution.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\cases\case-truman-yitang-foresight.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\cases\case-xiaolong-ecommerce-foresight.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\cases\case-一堂-AI高考志愿-kernel-mismatch.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\cases\case-一堂-无人餐厅-hypothesis-failure.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\cases\case-一堂-陈贤敏汉堡-hypothesis-validation.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\cases\case-半肥猫-conversion-hacker-skill.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\cases\case-半肥猫-course-to-skill.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\cases\case-半肥猫-from-assignment-to-tool.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\cases\case-半肥猫-skill-ab-test.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\cases\case-广冷电子-hx-smj.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\cases\case-纪浩-ai-workspace-chaos.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\cases\case-纪浩-focus-prompt-design.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\cases\case-纪浩-from-zip-to-five-layers.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\cases\case-纪浩-skill-market-problem-validation.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\cases\case-纪浩-skills-market.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\cases\case-纪浩-ui-design-constraint-evolution.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\2026-05-17-深夜感想.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ai-collaboration-mindset-shift.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\ai-landing-scene-selection.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\ai-learning-closed-loop.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\ai-native-五层进阶从答案到效率到作品到产品到系统.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ai-俱乐部人和-ai-协作-五层结构.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ai-俱乐部人和-ai-协作-参考案例对比一堂-vs-sql-helper.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\aigc文创案例设计课leo文创ip从0到1全流程.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\aigc设计基础01ai生图原理与提示词基本功.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\aigc设计师实操培训01口喷设计范式与电商ai设计全流程.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\aima-ai思维卡-外部链接归档.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ai单元模型口述蒋老师.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\ai数据理解第一课.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ai时代判断力口述-3.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ai时代判断力口述.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\anthropic-官方发布创始人手册打造-ai-原生初创公司.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\business-analysis.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\business-research-skill-oscar-13-weapon-system.md`
- 补充 confidence: 0.75

### `wiki\30_wiki\concepts\concept-ai-native-organization-five-steps.md`
- 补充 trust_level: low

### `wiki\30_wiki\concepts\concept-five-step-growth-to-barrier-transition.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\concept-mckinsey-issue-tree.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\concept-mckinsey-mece.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\concept-一堂-business-prediction.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\concept-一堂-hypothesis-driven-business-methodology.md`
- 补充 confidence: 0.85
- 补充 trust_level: high

### `wiki\30_wiki\concepts\concept-一堂-kernel-iteration.md`
- 补充 confidence: 0.85
- 补充 trust_level: high

### `wiki\30_wiki\concepts\concept-一堂-kernel-validation.md`
- 补充 confidence: 0.85
- 补充 trust_level: high

### `wiki\30_wiki\concepts\concept-一堂-key-assumptions.md`
- 补充 confidence: 0.85
- 补充 trust_level: high

### `wiki\30_wiki\concepts\concept-一堂-product-kernel.md`
- 补充 confidence: 0.85
- 补充 trust_level: high

### `wiki\30_wiki\concepts\concept-半肥猫-ai-learning-toolification-methodology.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\concept-纪浩-ai-collaboration-five-layer.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\concept-纪浩-ai-collaboration-methodology.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\contingency-decision-making.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\course-to-skill-conversion.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\data-labeling-best-practices-report.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\deepseek-v4-在知识管理系统中的应用.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\design-ai-image-generation.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ec工业化规范手册-v2.8.0.md`
- 补充 confidence: 0.8

### `wiki\30_wiki\concepts\EC工业化规范手册.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\find-old-do-small.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\graph-rag.md`
- 补充 confidence: 0.75

### `wiki\30_wiki\concepts\HIS系统开发实现方案-架构师指南.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\HIS系统深度调研.md`
- 补充 confidence: 0.85

### `wiki\30_wiki\concepts\kdo-flywheel.md`
- 补充 confidence: 0.9
- 补充 trust_level: high
- confidence 从 0.9 下调至 0.8（source 仅 0 个）

### `wiki\30_wiki\concepts\kdo-yaml-frontmatter-safety.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\kdo_product_design_agent_final.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\kimi-深度调研集群方法论-deep-research-swarm.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\knowledge-delivery-os-快速体验指南-飞书云文档.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\knowledge-error-self-exposure.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\learning-thinking.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\master-ai-info-literacy.md`
- 补充 trust_level: medium-high
- confidence 从 0.9 下调至 0.8（source 仅 1 个）

### `wiki\30_wiki\concepts\master-antifragile-checklist.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\master-cognitive-bias-checklist.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\master-decision-hygiene.md`
- 补充 trust_level: medium-high
- confidence 从 0.9 下调至 0.8（source 仅 1 个）

### `wiki\30_wiki\concepts\master-first-principles.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\master-knowledge-compound.md`
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\master-systems-thinking.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\meta-prompt-eng.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\obsidian-kdo-内容产出工作流-产品设计大纲.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\ocr-ai俱乐部-人和ai协作-纪浩-五层结构-图片01.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-ai俱乐部-人和ai协作-纪浩-参考案例-图片02.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-ocr_screenshot2.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-ocr_snipaste_2026-05-15_21-39-40.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-screenshot1.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-screenshot2.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-truman的个人成长五步法.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-truman的选择两条职业成长路线.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-ai学习-truman自用的ai-featureset.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-ai学习-提问工程化.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-ai学习-提问进化路线图.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-ai清单体笔记系统故事线-truman-图片01.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-ai清单体笔记训练段位图-truman-图片02.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-tcpr模型-皇冠模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-个人修炼-y模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-个人修炼-全景图muse模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-个人修炼-双三角模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-个人修炼-提问刻意练习画布.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-个人修炼-科学学习ipo-全景策略.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-个人修炼-科学学习ipo完整清单.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-个人修炼-科学学习ipo模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-个人修炼-科学提问刻意练习.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-个人修炼-表达力火箭模型-执行武器库.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-个人修炼-表达力火箭模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-个人修炼-解放思想.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-个人修炼-讲香十指模型-超级武器库.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-个人修炼-讲香基本功-十指模型修炼地图.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-个人修炼-讲香基本功.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-个人修炼-课程清单.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-人机协作-双三角模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-创业必修-课程清单.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-abcd策略模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-tcpr底层网络协议.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-修炼地图.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-动态预测.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-单sku模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-单商圈模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-单城市模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-单客户模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-单履约模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-单柜子模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-单用户模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-单订单模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-单销售模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-单门店模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-基准值.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-壁垒预判.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-外部对抗地图.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-多模型情况.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-学练用.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-对抗小抄.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-对抗小抄01.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-对抗小抄02.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-扭蛋机案例.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-找全成本实操难点.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-找单元模型实操难点.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-找基准值实操难点.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-斧子尺子梯子.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-斧子尺子梯子详解.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-最简单元模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-段位专家.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-示例.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-示例01.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-规模对抗实操难点.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-规模经济对抗武器库.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-单元模型-象限分析法.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-地图-个人地图.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-地图-个人地图_conv.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-地图-创业地图.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-地图-创业地图_conv.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-地图-管理地图.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-地图-管理地图_conv.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-案例拆解-课程清单.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-泛产品设计-十年苦练30招.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布-案例01.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布-案例02.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布-案例03.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布-案例04.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-roi高阶训练全景图.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-x型y型决策习惯对比.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-一堂双三角磨合追求-从入门到无限进步.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-人机协作决策.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-关键假设abcd模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-关键训练清单重要.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-决策三角形.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-发现决策.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-商业模式-完整财务公式决策.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-宽度-个人.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-宽度-企业.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-宽度-团队.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l1优先级定性.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l2部分定量.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l3定量公式.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l4-案例01.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l4严格财务公式.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-你的业务是一次抽样实验.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-决策经验值.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例01.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例02.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例03.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例04.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例05.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例06.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-稀缺机会窗口.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-稀缺资源清单.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-项目方案评估三角形.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-高度-两种典型的思考习惯.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-科学决策-高水平共识曲线重要.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-管理必修-课程清单.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂-高阶体系探索营-三种咨询可能性.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂doc-单元模型-十大单元模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂y模型-科学成事道理.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂y模型steps策略集.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂y模型实操工作流.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂个人地图高潜力成长者修炼全景图.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂五步法-产品内核画布.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂五步法画布.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂产品内核-十大典型指标.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂刻意练习十年成长指数.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂提炼过的因果模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂最佳转化率动力曲线图.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂泛产品设计-十年修炼爬山地图.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂泛产品设计-多出牌多练习.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂泛产品设计36计-全套地图.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂深度复盘冰山图.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂转化率-10大容易浪费的触点.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂进步大地图.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-一堂进步大地图_compressed.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-优秀泛产品设计者的自我修养.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-婚礼操盘-用户和场景.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-婚礼规划.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-审美提升的层级.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-微信图片_20260507004746_32_32.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-微信图片_20260507004751_33_32.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-微信图片_20260507004755_34_32.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-微信图片_20260507004758_35_32.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-微信图片_20260507004801_37_32.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-微信图片_20260507004802_38_32.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-微信图片_20260507004804_39_32.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-微信图片_20260507004806_40_32.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-微信图片_20260507004811_41_32.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-审美卡片-最佳实践建模.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-审美卡片-最佳实践收集.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-审美卡片-最佳实践池子.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-审美卡片-美好作品想象.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-审美工具箱指南.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-一堂五步法.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-动力阻力.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-场景推演.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-多视角思考.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-峰终定律.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-惊喜公式.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-用户分层.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-用户视角.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-行业分析画布.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-需求挖掘.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-项目背景分析.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-roi分析.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-业务建模.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-低成本测试mvp.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-假设拆解.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-内核和边界.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-努力仿真.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-十倍速验证.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-善用佳软.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-复盘迭代.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-攻坚会.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-灵感闪现.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-管理三段论.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-解放思想.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-设计原则.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-逻辑mece.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-酝酿式打磨.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-里程碑拆解.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-风险管理.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计-需求工具箱指南.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计的应用场景示意图.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计者的三大自我修养.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计者的自我修养.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计落地工具篇指南.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-泛产品设计落地篇.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-萃取总结.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-顶级产品追求的方向-乔布斯.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-项目背景问题思考的8个维度.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\ocr-预判模型.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\paddleocr-skill.md`
- 补充 confidence: 0.75

### `wiki\30_wiki\concepts\pilot-atomic-chunk-comparison.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\prd-as-ai-instruction.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\product-ux.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\research_methodology.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-1视角升级思考法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-ai-ai-workspace-setup.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-ai-evidence-check.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-ai-four-elements-validation.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-ai-info-literacy-three-layer.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-ai-landing-five-steps.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-ai-narrative-test.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-ai-old-small-checklist.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-ai-oral-spray-input.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-ai-parallel-validation.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-ai-prd-for-ai.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-ai-problem-question-check.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-ai-problem-validation.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-ai-purpose-bias-check.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-ai-research-five-steps.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-ai-scene-four-elements.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-ai-system-redundancy.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-ai-voice-input-doubao.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-ai辅助学习.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-cognitive-bias-12-check.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-decision-delay-intuition.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-decision-outside-view.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-first-principles-assumption-classify.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-mece体系框架法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-react行动推理循环.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-AI场景探索STAR模型.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-AI工具选型决策.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-AI时代IPO模型重构.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-AI时代提示词优化法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-AI能力分层学习路径.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-AI辅助思考伙伴养成.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-AI输出审慎判断与交付确认.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-Feature特性层训练法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-Skill全生命周期管理.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-XY-Problem识别与真实问题定位.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-上下文质量管理（AI协作）.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-个人判断力系统建设（达克效应应对）.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-人在环渐进自动化策略.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-低质量动作识别与拒绝.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-信息输入持续补全（防AI错误累积）.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-判断力产品化与系统赋能.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-双三角模型应用.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-复杂项目AI落地稳定性保障.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-多Agent通信协作方案.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-开源模型与商业模型融合方案.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-技术社区严肃提问法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-提示词优化底层方法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-数学题与语文题区分法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-本地记忆与云端记忆管理.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-知识库最佳实践构建.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-短视频自动化上传工作流.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-科学提问法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-职场异步协作提问法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-语义对齐沟通法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-Truman-问题定义澄清法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-一堂-business-prediction-15-char.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-一堂-five-step-validation.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-一堂-hypothesis-validation-three-axe.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-一堂-kernel-three-questions.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-一堂-product-kernel-add-subtract.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-一堂-product-kernel-canvas.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-一堂-spectrum-positioning.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-三层目标对齐法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-三阶追问法穷尽决策要素.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-专家访谈十步法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-专家访谈学习.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-专题笔记整理.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-专题笔记脑图整理法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-主动摘要压缩上下文.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-人生红点战略对齐.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-从案例中学习.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-从案例中学习正反案例法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-代入场景推演要素法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-任务拆解为工作流.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-体系框架构建.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-使用一页纸速查卡快速调用框架.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\skill-使用优先级快筛卡锁定核心矛盾.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-使用概念辨析卡区分易混淆概念.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-六维窗口期扫描法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-分享输出检验法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-分层标注重点信息.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-创始人二当家分工协作模式.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-制作行业化要素检查清单.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-动手建模提炼.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-动手建模法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-区分获客渠道计算单元roi.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-半肥猫-ai-research-validation.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-半肥猫-course-to-skill-workflow.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-半肥猫-优先使用官方权威信源做证据.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-半肥猫-判断课程是否值得做成Skill.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-半肥猫-动态读取-向量化管理迭代知识.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-半肥猫-告诉AI当前日期限制数据时效.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-半肥猫-将学习成果沉淀为PRD文档.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-半肥猫-按语义切分文档做向量化.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-半肥猫-清洗资料为Markdown格式喂给AI.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-半肥猫-用AI做结构化用户调研.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-半肥猫-用Skill做对比测试验证效果.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-半肥猫-用YAML格式做知识库原子化标签.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-半肥猫-设计Skill的评分规则与风险边界.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-半肥猫-课程Skill化的八步工作流.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-半肥猫-边学边练边沉淀的AI学习法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-半肥猫-追问AI证据并标注信源.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-半肥猫-飞书多维表格-自建机器人做团队数据协同.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-反向提示获取优化建议.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-反向教学深化理解.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-反向记录整理思路.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-反向采访挖掘深度.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-四层联系建立法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-城市合伙人模式复制能力.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-增强数据供给.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-复盘推演法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-复盘推演练习.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-多模型对比抽卡.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-多源输入法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-多轮确认防偏差.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-对标借鉴他人决策维度.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-寻找学习教练法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-封装可复用skill.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-将未中标成本纳入循环计算真实投标成本.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-应用人员降级公式实现标准化.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-建立知识联系.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-建立策略-要素映射表设计对抗策略.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-快招品牌总部模拟调研.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-思维链显化推理.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-思维验证交叉检验.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-执行对标研究三步法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-按分阶练习路径渐进掌握方法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-按图索骥改良外部模板.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-按月份摊销收入成本做计划.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-推行分层标准化策略.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-提升笔记练习频次的方法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-提升笔记阅读舒适度.md`
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-提示词结构化迭代.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-敏捷发布快速迭代搭建体系.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-数据分层供给.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-80分效率设计策略.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-A-B双轨反推模式选择.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AIGC产品白底图制作.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AIGC人群画像驱动详情页规划.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AIGC反向拆解法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AIGC文字大小精确控制.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AIGC模型选型决策法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AIGC橱窗陈列设计流程.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AIGC海报信息优先级排序法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AIGC生成人物证件照.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AIGC设计作业复盘法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AIGC餐饮海报优化一抽流.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI一句话改图尺寸.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI人物特征精准描述法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI去字-稿定设计加字工作流.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI去文字-稿定设计快速出图法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI图片印刷落地预处理.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI图片去文字处理.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI图片风格逆向提取（抄图法）.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI图生图尺寸快速转换.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI对话式海报修改（免PS）.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI对话情绪管理法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI工艺图人工复核法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI平台算法咨询法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI归纳共性描述法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI抽卡效率控制法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI提示词精准约束法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI改图指令精细化.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI智价比评估决策.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI模型选择决策法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI模型选择策略.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI海报快速生成法（15分钟无PS）.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI生图与图生图决策法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI生成IP表情包.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI生成图小字控制法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI生成图片排版控制-尺寸优先法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI生成棉花娃娃形象.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI生成电商白底图.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI电商图人工过审处理.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI精准替换产品技巧.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI自动生成多语种专业名词提示词.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI设计-质价比-决策框架.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI设计三段式里程碑流程.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI设计严苛批评法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI设计反馈萃取法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI设计底层逻辑：从设计到作图到改图.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI设计落地文件标准生成.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI设计里程碑拆解法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI课程内容深度梳理法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI质价比评估方法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI逆向反推描述法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI需求拆解咨询法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-AI高清重绘去模糊.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-PPT全AI生成工作流.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-PPT内容框架AIGC生成法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-PPT风格锁定工作流.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-PS图层规范管理.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-RGB转CMYK印刷预检.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-RGB转CMYK色彩校准法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-Token效价比决策公式.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-Token效价比决策法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-Token智甲比控制法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-一抽流改图法（自然语言精准许愿法）.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-一抽流长提示词写作法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-三步作业反馈法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-产品反光修复术.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-产品替换式场景合成法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-产品白底图标准化制作.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-产品风格选择：测而非定.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-价格带视觉策略匹配.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-供应商信息对齐清单法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-像素图高清重绘修复法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-光影灰度控制能力构建.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-关键要素提取改图法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-具体化优点萃取与复用.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-分层自洽海报生成法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-分步迭代改图法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-创作与执行双模式切换.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-包材工艺参数核对法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-卖点可视化海报设计法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-印刷DPI标准设置.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-叙事性场景海报构建.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-口喷作图工作流.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-口喷式AIGC设计法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-口喷式设计工作流.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-口述作图法（口喷设计）.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-后台数据AI诊断法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-商业项目AI模型选型决策.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-图像信息逆向解析训练.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-图片逆向反推提示词法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-图片逆向提示词提取.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-图生图产品替换与场景合成.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-圈图指定修改法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-基于基础形象做动作延展（1到10）.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-基于白底图做动作延展.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-基于需求拆解找设计参考.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-多窗口并行工作法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-多语种专业名词提示词策略.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-多语言提示词精准法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-多语言提示词降幻觉法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-官方提示词最佳实践迁移.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-实物包装产业链实践.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-实物包装落地训练法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-审美刻意练习法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-封面情绪转化法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-小红书双重搜索法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-小红书封面趋势判断法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-小红书平台内容策略：从美图经济到沙雕梗图.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-工厂对接信息清单制作.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-左手Cubox右手里程碑学习法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-左脑画面描述训练法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-强约束画面尺寸比例.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-微信公众号封面AI设计-尺寸强约束法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-手机外设计逻辑切换法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-手绘草稿AI转化工作流.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-批量生成多视角素材.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-找AI要平台专属方法（模型对抗法）.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-控制产品画面尺寸比例.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-提示词优化：信息流海报文字修复.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-提示词长度控制法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-文件命名与图层命名规范.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-文件命名与存档规范（口述暗示）.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-文件命名与平台适配规范.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-文创产品AI设计到生产的卡点预判.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-文创材质成本调研与精益选择.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-文创材质调研与精益选择.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-新媒体平台流量逻辑-问平台亲儿子AI法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-新媒体热点物料快速迭代法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-新手设计师基本功训练法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-普通人AI快速上手法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-普通人AI设计80分法则.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-智能扩图-拓图双方案.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-替换大法改图.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-最佳实践素材收集法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-服务体验类去AI感设计.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-未知领域审美建构法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-模型性价比选型决策.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-模型识别与边界测试法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-正向反馈强化AI生成.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-泛产品设计能力迁移法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-海报二维码快速替换法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-海报文字错误修复法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-灵感画布建立法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-烧Token快速积累体感.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-用AIGC做设计专家批评复盘.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-用一堂方法论找最佳实践并拉满执行.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-电商场景图三类分类法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-电商场景图三类构建法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-电商白底图生成与场景图匹配.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-电商白底图生成与高清处理.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-电商白底图生成与高清重绘.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-电商详情页起承转合架构法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-眼高手低训练法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-眼高手低转化法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-短视频封面-音量战争-设计法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-短视频封面一秒吸睛法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-短视频封面高亮吸睛法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-社群直播海报利益点提炼法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-竞品图精益替换法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-精准共用提示词撰写.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-精准提示词撰写法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-精准提示词消除模型幻觉.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-精准改图提示词写法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-纳米级抄大师训练法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-线下实体门店设计真实体感验证.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-线下门店设计复杂度评估.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-背景消除与分辨率修复.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-色块分区控制法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-薅AIGC羊毛资源法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-行业配色快速确定法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-表情包风格筛选与确定.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-视角替换专用提示法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-设计参考图精准定位法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-设计基本功回归法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-设计师AI工具习惯切换.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-设计师AI资产四类型沉淀.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-设计文件八要素命名法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-设计素材脱敏处理规范.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-设计能力蒸馏封装法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-设计需求口头化表达法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-设计项目MVP拆解法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-设计项目里程碑拆解法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-课程资料文件命名规范.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-课程问题预埋法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-资深设计师AI工具切换法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-跨境电商产品图替换法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-醒图人脸精修法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-里程碑思维-找对标优先于做设计.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-里程碑思维拆解设计流程.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-风格不变局部调整.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-风格探索试错法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-餐饮海报AB测试法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-月白-餐饮类线下设计调性把控.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-李诞-个人IP的重新定义与输出策略.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-李诞-内容创作中的观察训练法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-李诞-判断工作价值的交易成本视角.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-李诞-短视频-脱口秀创作：从-风格-自然-的无效建议中解脱.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-李诞-销售闭环验证：从0到1的重新定义.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-李诞-阅读重读机制：与书籍的-因缘-相遇.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-李诞-面对过去错误的平静心法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-模型匹配调度.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-模型组合调用.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-水水-保持系统冗余.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-水水-利用叙事驱动决策.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-水水-利用基因漂变视角.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-水水-区分风险与不确定性.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-水水-接受发散性世界观.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-水水-构建自利叙事.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-水水-用感性维度构建溢价.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-水水-管理决策权重偏差.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\skill-水水-练习坦然说不知道.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-水水-警惕概率虚妄安全感.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-水水-警惕错误归因.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-水水-识别关键偶然因素.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-水水-识别数据折磨陷阱.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-水水-识别模型局限性.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-水水-识别自证预言陷阱.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-水水-识别超级传播者风险.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-水水-识别饥饿效应.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-水水-避免原生家庭万能归因.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-水水-降低故事逻辑要求.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-深度分层学习.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-清单小抄制作.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-清单小抄工具箱法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-清单式笔记法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-渐进式披露上下文.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-现场建模式萃取笔记.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-用topdown方式整理内化笔记.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-用旗舰店替代纯招商投入.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-用清单体记备忘笔记.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-知识库团队管理.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-知识树存储记忆法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-稀缺资源机会成本比对法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-立即实践转化法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-Agent开工检查单制作法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-Agent技能市场设计法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-AI使用边界管理法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-AI对话上下文隔离.md`
- 补充 trust_level: medium-high
- confidence 从 0.9 下调至 0.8（source 仅 1 个）

### `wiki\30_wiki\concepts\skill-纪浩-AI工作空间与导诊台设计法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-AI工具脚本化约束.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-Do-first-PDCA渐进迭代法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-problem-validation-four-checks.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-Problem与Question区分法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-任务交付物标准化.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-低成本输出验证法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-处理AI生成代码运行异常.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-多视角切换思考法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-新手心态启动法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-日志驱动排查法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-案例池构建法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-真需求四要素验证法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-线上问题应急值守.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-评估AI从零写UI的可行性.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-识别AI不可维护代码.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-里程碑验证法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-问题导向备课法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-纪浩-项目启动五问法.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-自我反馈修正笔记姿势.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-自我反馈检验.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-获取他人反馈优化笔记.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-设定管理杠杆率指标评估效率.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-设计对抗效果追踪看板.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-费曼学习法三句话提炼.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-费曼学习法实践讲香课题.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-费曼简单提炼法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-辩证讨论法.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-辩证讨论深化.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-逐字稿练习演讲.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-通过综合案例沙盘走通全流程.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-通过请吃饭获取行业内部资料.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-遵循规模前倾原则设计组织架构.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-采用滚动预测机制.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-问题驱动式深度思考笔记.md`
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-项目复盘基本功.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\skill-马易-AIGC项目ROI评估.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-AI任务拆解提升控制度.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-AI搜索公网数据增强（合规边界）.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-AI答疑运营风格适配.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-AI能力团队复制.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-AI落地前置条件验证.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-AI落地四阶段验证法.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-AI落地场景筛选-四有新人法则.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-AI落地场景识别-拆工作流找场景.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-AI落地场景识别与拆分.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-AI落地能力内化训练.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-AI落地认知速成-最佳实践学习法.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-AI项目上线-先平行再独行.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-AI项目需求拆解筛选.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-RPA数据整合法.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-业务为先的AI中台建设.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\skill-马易-业务问题AI化拆解-餐饮设计案例法.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-中国企业AI落地五步法.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-低置信度样本黄金漏斗处理.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-公寓获客自跑通原则.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-关键假设识别与验证.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-减少输入噪音法.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-判断标准快速产出法.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-工作流优先于AIGC的决策方法.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-工作流拆解找场景.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-平台模式验证法.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-成为首位F工程师.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-数字员工FD拆解落地.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-数据存储架构选择.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-数据标注正确法.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-时间序列大模型场景识别.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-最小场景优先落地法.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-深度沉浸需求挖掘.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-痛点驱动的数字化.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-知识库-回答技巧双建设.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-视频转化关键要素标注校验.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-销售智能体体系搭建路径.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-隐性知识萃取与模型化.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-隐私安全分层解决.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-需求创造验证法.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\skill-马易-风口痛点识别法.md`
- 补充 confidence: 0.7
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\sprint-2-门禁举证验收.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\structured-ai-workspace.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\tinyfish-agentic-web-infrastructure.md`
- 补充 confidence: 0.75

### `wiki\30_wiki\concepts\tools-workflows.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\truman-perspective-skill.md`
- 补充 confidence: 0.75

### `wiki\30_wiki\concepts\voice-input-doubao.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\web-scraping-三剑客-scrapling-crawl4ai-firecrawl.md`
- 补充 confidence: 0.75

### `wiki\30_wiki\concepts\writing-content.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yc-放出一套ai-native-公司组织方法论直接把公司当操作系统来设计中层管理变成了-markdown.md`
- 补充 confidence: 0.8

### `wiki\30_wiki\concepts\yitang-course-map.md`
- 补充 confidence: 0.9
- 补充 trust_level: high
- confidence 从 0.9 下调至 0.8（source 仅 0 个）

### `wiki\30_wiki\concepts\yitang-huazong-ama-by-industry.md`
- 补充 confidence: 0.9
- 补充 trust_level: high
- confidence 从 0.9 下调至 0.8（source 仅 1 个）

### `wiki\30_wiki\concepts\yitang-huazong-ama-summary.md`
- 补充 confidence: 0.9
- 补充 trust_level: high
- confidence 从 0.9 下调至 0.8（source 仅 1 个）

### `wiki\30_wiki\concepts\yt-case-mandatory-cases.md`
- 补充 confidence: 0.85
- 补充 trust_level: high

### `wiki\30_wiki\concepts\yt-composite-pan-product-methodology.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-concept-ai-guard-brain.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-concept-context-engineering.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-concept-weapon-arsenal.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-entrepreneur-research-camp.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-entrepreneur-spin-selling.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-foresight-15-char-mantra.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-foresight-ab-steady-state.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-foresight-addition-subtraction.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-foresight-deliverables-four-levels.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-foresight-probability-engineering.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-foresight-ten-fatal-flaws.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-management-basic-skills.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\yt-management-company-culture.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\yt-management-conversion-hacking.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\yt-management-finance-basics.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\yt-management-founder-role.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\yt-management-goal-management.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\yt-management-leadership-levels.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\yt-management-onboarding.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\yt-management-partnership-equity.md`
- 补充 confidence: 0.75

### `wiki\30_wiki\concepts\yt-management-project-management.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\yt-management-scientific-decision.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\yt-management-scientific-hiring.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\yt-management-scientific-meetings.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\yt-management-strategy-meeting.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\yt-management-team-knowledge.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\yt-model-aesthetic-progression.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-conversion-optimization.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-deep-review-iceberg.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-deliberate-practice-growth.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-dual-triangle-competitiveness.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-entrepreneur-map.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-five-step-canvas.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-ipo-complete-checklist.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-ipo-learning-strategy.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-liberate-thinking-layers.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-management-map.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-muse-ai-framework.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-pan-product-36-strategies.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-pan-product-aesthetic-toolkit.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-pan-product-climbing-map.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-pan-product-demand-toolkit.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-pan-product-execution-toolkit.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-pan-product-three-virtues.md`
- 补充 trust_level: medium-high
- confidence 从 0.9 下调至 0.8（source 仅 1 个）

### `wiki\30_wiki\concepts\yt-model-personal-map.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-personal-pitch-toolkit.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-prediction-model.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-product-core-metrics.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-product-excellence.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-progress-map.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-prompt-engineering.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-questioning-practice-canvas.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-scientific-questioning-map.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-truman-career-routes.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-truman-five-step-growth.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-model-y-organization.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-note-ai-human-division.md`
- 补充 trust_level: low

### `wiki\30_wiki\concepts\yt-note-checklist-concept.md`
- 补充 trust_level: low

### `wiki\30_wiki\concepts\yt-note-deliberate-practice-four-elements.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-note-expert-interview-modeling.md`
- 补充 trust_level: low

### `wiki\30_wiki\concepts\yt-note-extensive-research-input.md`
- 补充 trust_level: low

### `wiki\30_wiki\concepts\yt-note-fact-pattern-insight.md`
- 补充 trust_level: low

### `wiki\30_wiki\concepts\yt-note-l4-internalization.md`
- 补充 trust_level: low

### `wiki\30_wiki\concepts\yt-note-l6-extraction.md`
- 补充 trust_level: low

### `wiki\30_wiki\concepts\yt-note-problem-solving-capability.md`
- 补充 trust_level: low

### `wiki\30_wiki\concepts\yt-panproduct-aesthetic-collection.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-aesthetic-imagination.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-aesthetic-modeling.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-aesthetic-pool.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-demand-five-step-method.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-demand-industry-canvas.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-demand-motivation-resistance.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-demand-multi-perspective.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-demand-need-discovery.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-demand-peak-end-rule.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-demand-project-background.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-demand-scenario-walkthrough.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-demand-surprise-formula.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-demand-user-perspective.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-demand-user-segmentation.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-execution-10x-validation.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-execution-business-modeling.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-execution-core-and-boundary.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-execution-design-principles.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-execution-good-tools.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-execution-hypothesis-decomposition.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-execution-idea-spark.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-execution-incubation-polish.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-execution-liberate-thinking.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-execution-logic-mece.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-execution-low-cost-mvp.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-execution-management-trilogy.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-execution-milestone-breakdown.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-execution-realistic-simulation.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-execution-review-iteration.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-execution-risk-management.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-execution-roi-analysis.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-panproduct-execution-war-room.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-personal-deep-review.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-personal-ipo-learning.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-personal-knowledge-extraction.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-personal-pan-product-02.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-personal-pan-product-aesthetics.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-personal-pan-product-concepts.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-personal-pan-product-exploration.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-personal-pan-product-practice.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-personal-pan-product-tools.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-personal-thinking-models.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-personal-y-model-exploration-2.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-personal-y-model-practice.md`
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-pitch-aphorism.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-pitch-colloquialization.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-pitch-conflict.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-pitch-emotionalization.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-pitch-materialization.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-pitch-metaphor.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-pitch-quantification.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-pitch-scenarization.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-pitch-storytelling.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-pitch-sublimation.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-prompt-anti-flattery.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-prompt-brainstorming.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-prompt-engineering-andrew-ng.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-prompt-iterative-prompting.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-prompt-writing-workflow.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-research-action-camp-launch.md`
- 补充 confidence: 0.85
- 补充 trust_level: high

### `wiki\30_wiki\concepts\yt-research-mindset.md`
- 补充 trust_level: low

### `wiki\30_wiki\concepts\yt-research-user-jtbd.md`
- 补充 trust_level: low

### `wiki\30_wiki\concepts\yt-research-weaponry-course.md`
- 补充 confidence: 0.85
- 补充 trust_level: high

### `wiki\30_wiki\concepts\yt-scale-economy-weapon-library.md`
- confidence 从 0.9 下调至 0.8（source 仅 1 个）

### `wiki\30_wiki\concepts\yt-skill-checklist-as-ai-protocol.md`
- 补充 trust_level: low

### `wiki\30_wiki\concepts\yt-skill-p-role-prompt-design.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-skill-storyline-contrast-analysis.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-skill-storyline-key-elements.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-skill-storyline-problem-solving.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-skill-storyline-target-tradeoff.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-skill-storyline-timeline.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-system-course-catalog.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-system-course-map-lecture.md`
- 补充 confidence: 0.85
- 补充 trust_level: high

### `wiki\30_wiki\concepts\yt-tool-best-practice-learning.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-tool-equity-checklist.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-tool-fab-persuasion.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-tool-foresight-canvas.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-tool-mental-model-refinement.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-tool-onboarding-90day.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-tool-project-health-radar.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\yt-tool-y-model-ruler.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\concepts\yt-unit-model-overview.md`
- 补充 confidence: 0.85
- 补充 trust_level: high

### `wiki\30_wiki\concepts\互联网医院模式深度调研报告.md`
- 补充 confidence: 0.8

### `wiki\30_wiki\concepts\人机协作决策-双三角模型.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\保达云诊所深度调研报告.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\在设计小伙伴的反馈还挺好的.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\存储策略.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\学会提问在信息洪流中锻造批判性思维的利刃.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\开源HIS系统代码深度分析报告.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\数据标注维度最佳实践调研报告.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\concepts\紫鲸ai_智能体工作流平台_深度分析与产品设计.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\紫鲸ai智能体工作流平台.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\老朱的水感-2026年5月.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\街顺app全面调研报告.md`
- 补充 confidence: 0.85

### `wiki\30_wiki\concepts\视觉prompt三层操作系统-srom-visual-os.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\诊所o2o外卖平台业务深度调研报告.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\concepts\轻量级诊所HIS调研全清单.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\那今天不会.md`
- 补充 confidence: 0.8
- 补充 trust_level: medium

### `wiki\30_wiki\concepts\鑫港湾his系统分阶段整改报告.md`
- 补充 confidence: 0.8

### `wiki\30_wiki\dark-knowledges\dk-ai-entrepreneur-technical-blindspot.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-ai-judgment-human-responsibility.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-ai-judgment-programmer-paradox.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-c1-cjk-regex-silent-fail.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-c10-batch-tool-no-dry-run.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-c11-hongqigong-skip-review.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-c2-dual-status-machine.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-c3-txt-ingest-skip.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-c4-selfcheck-superseded.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-c5-todo-false-positive.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-c6-large-source-overflow.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-c7-auto-backup-conflict.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-c8-format-complete-mind-empty.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-c9-batch-trigger-garbage.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-ef-001-sn74lvc2g07-open-drain.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\dark-knowledges\dk-ef-002-bom-version-async.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\dark-knowledges\dk-ef-003-hand-soldering-bom-divergence.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\dark-knowledges\dk-ef-004-missing-diagnostic-firmware.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\dark-knowledges\dk-f1-regex-on-cjk.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-f10-broken-source-refs.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-f11-encyclopedia-style.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-f12-builder-context-deadlock.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-f13-handwritten-yaml-parser.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-f14-accuracy-measurement-mismatch.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-f2-txt-ingest-skip.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-f3-state-json-race-condition.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-f4-wrong-workdir.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-f5-stale-feedback-ref.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-f6-cjk-skeleton-corruption.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-f7-surface-translation.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-f8-phony-wikilink.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-f9-generic-critique.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-foresight-source-material-blindness.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\dark-knowledges\dk-foresight-tier-skip-illusion.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-jh-llm-time-blindness.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-lz-ai-native-organization.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-lz-code-is-disposable.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-mckinsey-hypothesis-driven-pitfalls.md`
- 补充 confidence: 0.85
- 补充 trust_level: medium-high

### `wiki\30_wiki\dark-knowledges\dk-modeling-ai-self-retrospection.md`
- 补充 confidence: 0.7

### `wiki\30_wiki\dark-knowledges\dk-modeling-timely-review-session-window.md`
- 补充 confidence: 0.7

### `wiki\30_wiki\dark-knowledges\dk-my-ai-landing-three-barriers.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-note-maximum-common-divisor.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-note-rookie-disaster-veteran-heaven.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-note-surplus-brainpower.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-p1-model-switch-env.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-p10-oral-ban.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-p11-regex-cutoff.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-p13-token-burn.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-p14-zombie.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-p15-unverified.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\dark-knowledges\dk-p16-validate-reads-state-json.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-p17-accuracy-gap.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-p18-yaml-parser.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-p19-quote-yaml.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-p2-tmux-cache.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-p20-bigram-fail.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-p3-auth-cache.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-p4-batch-format-empty.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-p5-cc-connect-config.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-p6-session-resume-fail.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-p7-ocr-skip.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-p8-toolkit-forget.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-p9-glob-miss.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-pseudo-demand-trap.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-signal-cluster-illusion.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-truman-document-is-real-project-is-fake.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-truman-flag-note-taking.md`
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-truman-iteration-to-aesthetic-ceiling.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-truman-knowledge-extraction-three-schools.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb1-aigc-mvp-before-ps.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb10-theory-moat-designer.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb11-visual-book-reverse.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb12-ai-image-analysis-replace-training.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb13-zero-shot-style-transfer.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb14-multi-image-commonality.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb15-reverse-image-description.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb16-ecommerce-product-image-vs-lucky-draw.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb17-product-lifestyle-photography.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb18-small-shop-image-mismatch.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb19-visual-strategy-price-match.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb2-llm-muddy-clear-muddy.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb20-ai-eye-high-principle.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb21-ecommerce-pricing-independent-model.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb22-visual-presentation-scene-match.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb23-ai-pre-screen-three-minutes.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb24-ai-poster-de-ai-feeling.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb25-solution-driven-visual-design.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb26-chinese-food-photography-props.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb27-pseudo-layer-evasion.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb28-prompt-expiration-management.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb29-prompt-migrate-copy-first.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb3-diffusion-stepwise-vs-human-holistic.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb30-ecommerce-channel-version.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb31-style-first-controlnet.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb32-doubao-size-composition.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb4-nano-banana-style-reproduction.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb5-style-asset-archive.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb6-midjourney-chinese-text-fix.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb7-design-demand-80-10-10.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb8-file-naming-eight-elements.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yb9-cubox-deployment-failure.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-yitang-business-formula-plus-times-trap.md`
- 补充 confidence: 0.85

### `wiki\30_wiki\dark-knowledges\dk-一堂-wishful-thinking-kills-startups.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-半肥猫-atomic-no-standard.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-半肥猫-real-business-is-the-engine.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-半肥猫-silky-answer-warning.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-半肥猫-silky-answers-are-dangerous.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-半肥猫-skill-rejection-value.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-纪浩-ai-cant-design-structure.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-纪浩-constraint-beats-talent.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-纪浩-logs-fastest-ignored.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-纪浩-newbie-can-validate.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-纪浩-novice-mindset-advantage.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-纪浩-pdca-starts-from-do.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-纪浩-problem-vs-question.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\dk-纪浩-simple-complex-routing.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\dark-knowledges\yt-note-ai-p-role-not-c-role.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\dark-knowledges\yt-note-p-c-role-boundary-realworld.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\dark-knowledges\yt-note-three-level-evolution.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\decisions\agent-ecosystem-design.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\data-curator-role-division.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\fix-dark-knowledge-extractor-llm.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\decisions\fix-data-curator-parse-bug.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\decisions\gold-standard-manual-labels.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\high-density-composite-compilation-strategy.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\decisions\huangyaoshi-data-alignment-response.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\huangyaoshi-extractor-upgrade-report.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\huangyaoshi-tagging-and-scope-proposal.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\kdo-15-dimension-label-spec.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\kdo-ec-industrialization-migration-proposal.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\kdo-priority-checklist.md`
- 补充 confidence: 0.6

### `wiki\30_wiki\decisions\kdo-protocol-implementation-roadmap.md`
- 补充 confidence: 0.6

### `wiki\30_wiki\decisions\label-accuracy-standard-alignment.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\labeling-final-consolidation.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\labeling-research-alignment.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\modeling-capability-for-kdo.md`
- 补充 trust_level: high

### `wiki\30_wiki\decisions\ouyangfeng-data-alignment-response.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\ouyangfeng-labeling-research-review.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\plan_20260501_05858800-improvement-plan.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\plan_20260501_47264869-improvement-plan.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\plan_20260501_8001399c-improvement-plan.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\plan_20260501_85a84b92-improvement-plan.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\plan_20260501_8ecb74e3-improvement-plan.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\plan_20260501_97170532-improvement-plan.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\plan_20260501_ca61cdd7-improvement-plan.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\plan_20260501_e1e150b9-improvement-plan.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\plan_20260503_f3e9a2b1-improvement-plan.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\plan_20260531_data-curator-v1.1.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\decisions\plan_20260531_data-curator-v1.3.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\decisions\plan_20260531_data-curator-v1.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\decisions\proposal-ai-domain-mastery-pipeline.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\proposal-deep-synthesis-infrastructure.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\proposal-graph-rag-star-fix.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\proposal-kdo-flywheel-infrastructure.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\proposal-prompt-injection-infrastructure.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\proposal-yaml-frontmatter-standardization.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\decisions\sprint-6-cli-gap-proposal.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\three-party-data-alignment.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\decisions\truman-ai-partner-design-analysis.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\entities\Kimi-月之暗面.md`
- 补充 confidence: 0.85

### `wiki\30_wiki\entities\YC-Y-Combinator.md`
- 补充 confidence: 0.85

### `wiki\30_wiki\entities\一堂.md`
- 补充 confidence: 0.9
- 补充 trust_level: high
- confidence 从 0.9 下调至 0.8（source 仅 0 个）

### `wiki\30_wiki\entities\七件事集团.md`
- 补充 confidence: 0.9

### `wiki\30_wiki\entities\紫鲸AI.md`
- 补充 confidence: 0.85

### `wiki\30_wiki\entities\鑫港湾.md`
- 补充 confidence: 0.85

### `wiki\30_wiki\frameworks\concept-maister-trusted-advisor.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\frameworks\concept-mckinsey-7s.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\frameworks\concept-mckinsey-hypothesis-driven.md`
- 补充 confidence: 0.85
- 补充 trust_level: medium-high

### `wiki\30_wiki\frameworks\concept-mckinsey-mece.md`
- 补充 confidence: 0.85
- 补充 trust_level: medium-high

### `wiki\30_wiki\frameworks\concept-minto-pyramid-principle.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\frameworks\framework-logic-cleanliness-five-levels.md`
- confidence 从 0.9 下调至 0.8（source 仅 1 个）

### `wiki\30_wiki\frameworks\model-quality-four-levels.md`
- confidence 从 0.92 下调至 0.8（source 仅 1 个）

### `wiki\30_wiki\frameworks\sales-pitch-bias-patterns.md`
- confidence 从 0.92 下调至 0.8（source 仅 1 个）

### `wiki\30_wiki\frameworks\smart-device-foodservice-automation.md`
- confidence 从 0.95 下调至 0.85（source 仅 1 个）

### `wiki\30_wiki\frameworks\yt-decision-abcd-model.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\frameworks\yt-unit-model-ladder.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\frameworks\yt-unit-model-overview.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\projects\互联网医院项目.md`
- 补充 confidence: 0.85
- 补充 trust_level: high

### `wiki\30_wiki\projects\诊所O2O项目.md`
- 补充 confidence: 0.85
- 补充 trust_level: high

### `wiki\30_wiki\projects\鑫港湾HIS项目.md`
- 补充 confidence: 0.85
- 补充 trust_level: high

### `wiki\30_wiki\systems\agent-external-brain-design.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium-low

### `wiki\30_wiki\systems\agent-native-card-design.md`
- 补充 confidence: 0.85
- 补充 trust_level: high

### `wiki\30_wiki\systems\graph-rag-retrieval-layer.md`
- 补充 confidence: 0.9
- 补充 trust_level: high
- confidence 从 0.9 下调至 0.8（source 仅 0 个）

### `wiki\30_wiki\systems\kdo-batch-produce-req014.md`
- 补充 confidence: 0.65
- 补充 trust_level: low

### `wiki\30_wiki\systems\kdo-protocol.md`
- 补充 confidence: 0.6

### `wiki\30_wiki\systems\kdo-watch-health-check-layer.md`
- 补充 confidence: 0.65
- 补充 trust_level: low

### `wiki\30_wiki\systems\obsidian-git-sync-protocol.md`
- 补充 confidence: 0.6

### `wiki\30_wiki\systems\sprint-2-gate-enrich-evidence.md`
- 补充 confidence: 0.6
- 补充 trust_level: low

### `wiki\30_wiki\systems\workflow-knowledge-collision.md`
- 补充 confidence: 0.85
- 补充 trust_level: high

### `wiki\30_wiki\systems\一堂方法论体系总图.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\tools\concept-mckinsey-issue-tree.md`
- 补充 confidence: 0.85
- 补充 trust_level: medium-high

### `wiki\30_wiki\tools\concept-toyota-5-whys.md`
- 补充 confidence: 0.85
- 补充 trust_level: medium-high

### `wiki\30_wiki\tools\sk-ai-ai-workspace-setup.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\tools\sk-ai-evidence-check.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\tools\sk-ai-landing-five-steps.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\tools\sk-ai-narrative-test.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\tools\sk-ai-old-small-checklist.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\tools\sk-ai-parallel-validation.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\tools\sk-ai-prd-for-ai.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\tools\sk-ai-problem-validation.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\tools\sk-ai-purpose-bias-check.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\tools\sk-ai-question-problem-checklist.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\tools\sk-ai-system-redundancy.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\tools\sk-ai-voice-input-doubao.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\tools\skill-mckinsey-hypothesis-driven-workflow.md`
- 补充 confidence: 0.85
- 补充 trust_level: medium-high

### `wiki\30_wiki\tools\skill-note-keyword-bolding.md`
- 补充 trust_level: low
- confidence 从 0.9 下调至 0.8（source 仅 1 个）

### `wiki\30_wiki\tools\skill-note-layer-constraint.md`
- 补充 trust_level: low
- confidence 从 0.92 下调至 0.8（source 仅 1 个）

### `wiki\30_wiki\tools\skill-note-one-line-one-point.md`
- 补充 trust_level: low
- confidence 从 0.95 下调至 0.85（source 仅 1 个）

### `wiki\30_wiki\tools\yt-note-five-levels-training.md`
- 补充 trust_level: low

### `wiki\30_wiki\tools\yt-note-live-field-skill.md`
- 补充 trust_level: low

### `wiki\30_wiki\tools\yt-pitch-metaphor.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\tools\yt-pitch-quantification.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\tools\yt-pitch-storytelling.md`
- 补充 trust_level: medium-high

### `wiki\30_wiki\tools\yt-tool-ai-ppt-maker.md`
- 补充 confidence: 0.7
- 补充 trust_level: low

### `wiki\30_wiki\tools\yt-tool-unit-model-ai-assisted.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\tools\yt-tool-unit-model-benchmark.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\tools\yt-tool-unit-model-construction.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\tools\yt-tool-unit-model-dynamic.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium

### `wiki\30_wiki\tools\yt-tool-unit-model-selection.md`
- 补充 confidence: 0.75
- 补充 trust_level: medium
