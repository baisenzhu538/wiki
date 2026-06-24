# 跨域链接审计报告

**执行时间**：2026-06-24 21:09
**总检查卡数**：1959
**异常卡数**：255

## 1. framework/tool 卡未跨域（253 张）

| 卡 ID | 类型 | 自身域 | 当前跨域 |
|:--|:--|:--|:--|
| `framework-strategy-basics-01-core` | framework | strategy | 无 |
| `framework-strategy-basics-02-insight` | framework | strategy | 无 |
| `framework-strategy-basics-03-layout` | framework | strategy | strategy |
| `framework-strategy-basics-04-system` | framework | strategy | 无 |
| `framework-strategy-five-basics` | framework | strategy | strategy |
| `master-ai-info-literacy` | framework | mastersource_person: Truman | mastersource_person: Truman |
| `master-cognitive-bias-checklist` | tool | mastersource_person: Truman | mastersource_person: Truman |
| `master-decision-hygiene` | framework | mastersource_person: Truman | mastersource_person: Truman |
| `master-first-principles` | tool | mastersource_person: Truman | mastersource_person: Truman |
| `skill-ai-landing-five-steps` | tool | ai-collaboration | 无 |
| `skill-ai-research-five-steps` | tool | ai-collaboration | 无 |
| `skill-ai-scene-four-elements` | tool | ai-collaboration | 无 |
| `skill-cognitive-bias-12-check` | tool | decision- 决策 | 无 |
| `skill-decision-delay-intuition` | tool | decision- 决策 | 无 |
| `skill-first-principles-assumption-classify` | tool | learning-methodology- 创新 | 无 |
| `skill-月白-80分效率设计策略` | tool | design- design | design- design |
| `skill-月白-A-B双轨反推模式选择` | tool | design- design | design- design |
| `skill-月白-AIGC产品白底图制作` | tool | design- design | design- design |
| `skill-月白-AIGC人群画像驱动详情页规划` | tool | design- design | design- design |
| `skill-月白-AIGC反向拆解法` | tool | design- design | design- design |
| `skill-月白-AIGC文字大小精确控制` | tool | design- design | design- design |
| `skill-月白-AIGC模型选型决策法` | tool | design- design | design- design |
| `skill-月白-AIGC橱窗陈列设计流程` | tool | design- design | design- design |
| `skill-月白-AIGC海报信息优先级排序法` | tool | design- design | design- design |
| `skill-月白-AIGC生成人物证件照` | tool | design- design | design- design |
| `skill-月白-AIGC设计作业复盘法` | tool | design- design | design- design |
| `skill-月白-AIGC餐饮海报优化一抽流` | tool | design- design | design- design |
| `skill-月白-AI一句话改图尺寸` | tool | design- design | design- design |
| `skill-月白-AI人物特征精准描述法` | tool | design- design | design- design |
| `skill-月白-AI去字-稿定设计加字工作流` | tool | design- design | design- design |
| `skill-月白-AI去文字-稿定设计快速出图法` | tool | design- design | design- design |
| `skill-月白-AI图片印刷落地预处理` | tool | design- design | design- design |
| `skill-月白-AI图片去文字处理` | tool | design- design | design- design |
| `skill-月白-AI图片风格逆向提取（抄图法）` | tool | design- design | design- design |
| `skill-月白-AI图生图尺寸快速转换` | tool | design- design | design- design |
| `skill-月白-AI对话式海报修改（免PS）` | tool | design- design | design- design |
| `skill-月白-AI对话情绪管理法` | tool | design- design | design- design |
| `skill-月白-AI工艺图人工复核法` | tool | design- design | design- design |
| `skill-月白-AI平台算法咨询法` | tool | design- design | design- design |
| `skill-月白-AI归纳共性描述法` | tool | design- design | design- design |
| `skill-月白-AI抽卡效率控制法` | tool | design- design | design- design |
| `skill-月白-AI提示词精准约束法` | tool | design- design | design- design |
| `skill-月白-AI改图指令精细化` | tool | design- design | design- design |
| `skill-月白-AI智价比评估决策` | tool | design- design | design- design |
| `skill-月白-AI模型选择决策法` | tool | design- design | design- design |
| `skill-月白-AI模型选择策略` | tool | design- design | design- design |
| `skill-月白-AI海报快速生成法（15分钟无PS）` | tool | design- design | design- design |
| `skill-月白-AI生图与图生图决策法` | tool | design- design | design- design |
| `skill-月白-AI生成IP表情包` | tool | design- design | design- design |
| `skill-月白-AI生成图小字控制法` | tool | design- design | design- design |
| `skill-月白-AI生成图片排版控制-尺寸优先法` | tool | design- design | design- design |
| `skill-月白-AI生成棉花娃娃形象` | tool | design- design | design- design |
| `skill-月白-AI生成电商白底图` | tool | design- design | design- design |
| `skill-月白-AI电商图人工过审处理` | tool | design- design | design- design |
| `skill-月白-AI精准替换产品技巧` | tool | design- design | design- design |
| `skill-月白-AI自动生成多语种专业名词提示词` | tool | design- design | design- design |
| `skill-月白-AI设计-质价比-决策框架` | tool | design- design | design- design |
| `skill-月白-AI设计三段式里程碑流程` | tool | design- design | design- design |
| `skill-月白-AI设计严苛批评法` | tool | design- design | design- design |
| `skill-月白-AI设计反馈萃取法` | tool | design- design | design- design |
| `skill-月白-AI设计底层逻辑：从设计到作图到改图` | tool | design- design | design- design |
| `skill-月白-AI设计落地文件标准生成` | tool | design- design | design- design |
| `skill-月白-AI设计里程碑拆解法` | tool | design- design | design- design |
| `skill-月白-AI课程内容深度梳理法` | tool | design- design | design- design |
| `skill-月白-AI质价比评估方法` | tool | design- design | design- design |
| `skill-月白-AI逆向反推描述法` | tool | design- design | design- design |
| `skill-月白-AI需求拆解咨询法` | tool | design- design | design- design |
| `skill-月白-AI高清重绘去模糊` | tool | design- design | design- design |
| `skill-月白-PPT全AI生成工作流` | tool | design- design | design- design |
| `skill-月白-PPT内容框架AIGC生成法` | tool | design- design | design- design |
| `skill-月白-PPT风格锁定工作流` | tool | design- design | design- design |
| `skill-月白-PS图层规范管理` | tool | design- design | design- design |
| `skill-月白-RGB转CMYK印刷预检` | tool | design- design | design- design |
| `skill-月白-RGB转CMYK色彩校准法` | tool | design- design | design- design |
| `skill-月白-Token效价比决策公式` | tool | design- design | design- design |
| `skill-月白-Token效价比决策法` | tool | design- design | design- design |
| `skill-月白-Token智甲比控制法` | tool | design- design | design- design |
| `skill-月白-一抽流改图法（自然语言精准许愿法）` | tool | design- design | design- design |
| `skill-月白-一抽流长提示词写作法` | tool | design- design | design- design |
| `skill-月白-三步作业反馈法` | tool | design- design | design- design |
| `skill-月白-产品反光修复术` | tool | design- design | design- design |
| `skill-月白-产品替换式场景合成法` | tool | design- design | design- design |
| `skill-月白-产品白底图标准化制作` | tool | design- design | design- design |
| `skill-月白-产品风格选择：测而非定` | tool | design- design | design- design |
| `skill-月白-价格带视觉策略匹配` | tool | design- design | design- design |
| `skill-月白-供应商信息对齐清单法` | tool | design- design | design- design |
| `skill-月白-像素图高清重绘修复法` | tool | design- design | design- design |
| `skill-月白-光影灰度控制能力构建` | tool | design- design | design- design |
| `skill-月白-关键要素提取改图法` | tool | design- design | design- design |
| `skill-月白-具体化优点萃取与复用` | tool | design- design | design- design |
| `skill-月白-分层自洽海报生成法` | tool | design- design | design- design |
| `skill-月白-分步迭代改图法` | tool | design- design | design- design |
| `skill-月白-创作与执行双模式切换` | tool | design- design | design- design |
| `skill-月白-包材工艺参数核对法` | tool | design- design | design- design |
| `skill-月白-卖点可视化海报设计法` | tool | design- design | design- design |
| `skill-月白-印刷DPI标准设置` | tool | design- design | design- design |
| `skill-月白-叙事性场景海报构建` | tool | design- design | design- design |
| `skill-月白-口喷作图工作流` | tool | design- design | design- design |
| `skill-月白-口喷式AIGC设计法` | tool | design- design | design- design |
| `skill-月白-口喷式设计工作流` | tool | design- design | design- design |
| `skill-月白-口述作图法（口喷设计）` | tool | design- design | design- design |
| `skill-月白-后台数据AI诊断法` | tool | design- design | design- design |
| `skill-月白-商业项目AI模型选型决策` | tool | design- design | design- design |
| `skill-月白-图像信息逆向解析训练` | tool | design- design | design- design |
| `skill-月白-图片逆向反推提示词法` | tool | design- design | design- design |
| `skill-月白-图片逆向提示词提取` | tool | design- design | design- design |
| `skill-月白-图生图产品替换与场景合成` | tool | design- design | design- design |
| `skill-月白-圈图指定修改法` | tool | design- design | design- design |
| `skill-月白-基于基础形象做动作延展（1到10）` | tool | design- design | design- design |
| `skill-月白-基于白底图做动作延展` | tool | design- design | design- design |
| `skill-月白-基于需求拆解找设计参考` | tool | design- design | design- design |
| `skill-月白-多窗口并行工作法` | tool | design- design | design- design |
| `skill-月白-多语种专业名词提示词策略` | tool | design- design | design- design |
| `skill-月白-多语言提示词精准法` | tool | design- design | design- design |
| `skill-月白-多语言提示词降幻觉法` | tool | design- design | design- design |
| `skill-月白-官方提示词最佳实践迁移` | tool | design- design | design- design |
| `skill-月白-实物包装产业链实践` | tool | design- design | design- design |
| `skill-月白-实物包装落地训练法` | tool | design- design | design- design |
| `skill-月白-审美刻意练习法` | tool | design- design | design- design |
| `skill-月白-封面情绪转化法` | tool | design- design | design- design |
| `skill-月白-小红书双重搜索法` | tool | design- design | design- design |
| `skill-月白-小红书封面趋势判断法` | tool | design- design | design- design |
| `skill-月白-小红书平台内容策略：从美图经济到沙雕梗图` | tool | design- design | design- design |
| `skill-月白-工厂对接信息清单制作` | tool | design- design | design- design |
| `skill-月白-左手Cubox右手里程碑学习法` | tool | design- design | design- design |
| `skill-月白-左脑画面描述训练法` | tool | design- design | design- design |
| `skill-月白-强约束画面尺寸比例` | tool | design- design | design- design |
| `skill-月白-微信公众号封面AI设计-尺寸强约束法` | tool | design- design | design- design |
| `skill-月白-手机外设计逻辑切换法` | tool | design- design | design- design |
| `skill-月白-手绘草稿AI转化工作流` | tool | design- design | design- design |
| `skill-月白-批量生成多视角素材` | tool | design- design | design- design |
| `skill-月白-找AI要平台专属方法（模型对抗法）` | tool | design- design | design- design |
| `skill-月白-控制产品画面尺寸比例` | tool | design- design | design- design |
| `skill-月白-提示词优化：信息流海报文字修复` | tool | design- design | design- design |
| `skill-月白-提示词长度控制法` | tool | design- design | design- design |
| `skill-月白-文件命名与图层命名规范` | tool | design- design | design- design |
| `skill-月白-文件命名与存档规范（口述暗示）` | tool | design- design | design- design |
| `skill-月白-文件命名与平台适配规范` | tool | design- design | design- design |
| `skill-月白-文创产品AI设计到生产的卡点预判` | tool | design- design | design- design |
| `skill-月白-文创材质成本调研与精益选择` | tool | design- design | design- design |
| `skill-月白-文创材质调研与精益选择` | tool | design- design | design- design |
| `skill-月白-新媒体平台流量逻辑-问平台亲儿子AI法` | tool | design- design | design- design |
| `skill-月白-新媒体热点物料快速迭代法` | tool | design- design | design- design |
| `skill-月白-新手设计师基本功训练法` | tool | design- design | design- design |
| `skill-月白-普通人AI快速上手法` | tool | design- design | design- design |
| `skill-月白-普通人AI设计80分法则` | tool | design- design | design- design |
| `skill-月白-智能扩图-拓图双方案` | tool | design- design | design- design |
| `skill-月白-替换大法改图` | tool | design- design | design- design |
| `skill-月白-最佳实践素材收集法` | tool | design- design | design- design |
| `skill-月白-服务体验类去AI感设计` | tool | design- design | design- design |
| `skill-月白-未知领域审美建构法` | tool | design- design | design- design |
| `skill-月白-模型性价比选型决策` | tool | design- design | design- design |
| `skill-月白-模型识别与边界测试法` | tool | design- design | design- design |
| `skill-月白-正向反馈强化AI生成` | tool | design- design | design- design |
| `skill-月白-泛产品设计能力迁移法` | tool | design- design | design- design |
| `skill-月白-海报二维码快速替换法` | tool | design- design | design- design |
| `skill-月白-海报文字错误修复法` | tool | design- design | design- design |
| `skill-月白-灵感画布建立法` | tool | design- design | design- design |
| `skill-月白-烧Token快速积累体感` | tool | design- design | design- design |
| `skill-月白-用AIGC做设计专家批评复盘` | tool | design- design | design- design |
| `skill-月白-用一堂方法论找最佳实践并拉满执行` | tool | design- design | design- design |
| `skill-月白-电商场景图三类分类法` | tool | design- design | design- design |
| `skill-月白-电商场景图三类构建法` | tool | design- design | design- design |
| `skill-月白-电商白底图生成与场景图匹配` | tool | design- design | design- design |
| `skill-月白-电商白底图生成与高清处理` | tool | design- design | design- design |
| `skill-月白-电商白底图生成与高清重绘` | tool | design- design | design- design |
| `skill-月白-电商详情页起承转合架构法` | tool | design- design | design- design |
| `skill-月白-眼高手低训练法` | tool | design- design | design- design |
| `skill-月白-眼高手低转化法` | tool | design- design | design- design |
| `skill-月白-短视频封面-音量战争-设计法` | tool | design- design | design- design |
| `skill-月白-短视频封面一秒吸睛法` | tool | design- design | design- design |
| `skill-月白-短视频封面高亮吸睛法` | tool | design- design | design- design |
| `skill-月白-社群直播海报利益点提炼法` | tool | design- design | design- design |
| `skill-月白-竞品图精益替换法` | tool | design- design | design- design |
| `skill-月白-精准共用提示词撰写` | tool | design- design | design- design |
| `skill-月白-精准提示词撰写法` | tool | design- design | design- design |
| `skill-月白-精准提示词消除模型幻觉` | tool | design- design | design- design |
| `skill-月白-精准改图提示词写法` | tool | design- design | design- design |
| `skill-月白-纳米级抄大师训练法` | tool | design- design | design- design |
| `skill-月白-线下实体门店设计真实体感验证` | tool | design- design | design- design |
| `skill-月白-线下门店设计复杂度评估` | tool | design- design | design- design |
| `skill-月白-背景消除与分辨率修复` | tool | design- design | design- design |
| `skill-月白-色块分区控制法` | tool | design- design | design- design |
| `skill-月白-薅AIGC羊毛资源法` | tool | design- design | design- design |
| `skill-月白-行业配色快速确定法` | tool | design- design | design- design |
| `skill-月白-表情包风格筛选与确定` | tool | design- design | design- design |
| `skill-月白-视角替换专用提示法` | tool | design- design | design- design |
| `skill-月白-设计参考图精准定位法` | tool | design- design | design- design |
| `skill-月白-设计基本功回归法` | tool | design- design | design- design |
| `skill-月白-设计师AI工具习惯切换` | tool | design- design | design- design |
| `skill-月白-设计师AI资产四类型沉淀` | tool | design- design | design- design |
| `skill-月白-设计文件八要素命名法` | tool | design- design | design- design |
| `skill-月白-设计素材脱敏处理规范` | tool | design- design | design- design |
| `skill-月白-设计能力蒸馏封装法` | tool | design- design | design- design |
| `skill-月白-设计需求口头化表达法` | tool | design- design | design- design |
| `skill-月白-设计项目MVP拆解法` | tool | design- design | design- design |
| `skill-月白-设计项目里程碑拆解法` | tool | design- design | design- design |
| `skill-月白-课程资料文件命名规范` | tool | design- design | design- design |
| `skill-月白-课程问题预埋法` | tool | design- design | design- design |
| `skill-月白-资深设计师AI工具切换法` | tool | design- design | design- design |
| `skill-月白-跨境电商产品图替换法` | tool | design- design | design- design |
| `skill-月白-醒图人脸精修法` | tool | design- design | design- design |
| `skill-月白-里程碑思维-找对标优先于做设计` | tool | design- design | design- design |
| `skill-月白-里程碑思维拆解设计流程` | tool | design- design | design- design |
| `skill-月白-风格不变局部调整` | tool | design- design | design- design |
| `skill-月白-风格探索试错法` | tool | design- design | design- design |
| `skill-月白-餐饮海报AB测试法` | tool | design- design | design- design |
| `skill-月白-餐饮类线下设计调性把控` | tool | design- design | design- design |
| `tool-demand-agent-case-match` | tool | ai-collaboration | demand-analysis |
| `tool-demand-agent-signal-substitute` | tool | ai-collaboration | demand-analysis |
| `tool-demand-blindspot-checklist` | tool | demand-analysis | demand-analysis |
| `tool-strategy-business-summary` | tool | strategy | strategy |
| `tool-strategy-capability-matrix` | tool | strategy | strategy |
| `tool-strategy-competition-traps` | tool | strategy | strategy |
| `tool-strategy-fishbone` | tool | problem_solving | strategy |
| `tool-strategy-five-see-three-set` | tool | strategy | strategy |
| `tool-strategy-four-layers` | tool | strategy | strategy |
| `tool-strategy-four-moves` | tool | strategy | strategy |
| `tool-strategy-map` | tool | strategy | strategy |
| `tool-strategy-nine-problems` | tool | strategy | strategy |
| `tool-strategy-sentence-formula` | tool | strategy | strategy |
| `yt-entrepreneur-growth-flywheel` | tool | entrepreneurship | mastersource_person: Truman |
| `yt-entrepreneur-liberate-thinking` | tool | entrepreneurship | mastersource_person: Truman |
| `yt-entrepreneur-research-cognition` | tool | entrepreneurship | mastersource_person: Truman |
| `yt-panproduct-demand-industry-canvas` | tool | product- yitang | product- yitang |
| `yt-panproduct-demand-multi-perspective` | tool | product- yitang | product- yitang |
| `yt-panproduct-demand-need-discovery` | tool | product- yitang | product- yitang |
| `yt-panproduct-demand-project-background` | tool | product- yitang | product- yitang |
| `yt-panproduct-demand-scenario-walkthrough` | tool | product- yitang | product- yitang |
| `yt-panproduct-demand-user-segmentation` | tool | product- yitang | product- yitang |
| `yt-panproduct-execution-10x-validation` | tool | product- yitang | product- yitang |
| `yt-panproduct-execution-business-modeling` | tool | product- yitang | product- yitang |
| `yt-panproduct-execution-design-principles` | tool | product- yitang | product- yitang |
| `yt-panproduct-execution-good-tools` | tool | product- yitang | product- yitang |
| `yt-panproduct-execution-idea-spark` | tool | product- yitang | product- yitang |
| `yt-panproduct-execution-incubation-polish` | tool | product- yitang | product- yitang |
| `yt-panproduct-execution-management-trilogy` | tool | product- yitang | product- yitang |
| `yt-panproduct-execution-milestone-breakdown` | tool | product- yitang | product- yitang |
| `yt-panproduct-execution-realistic-simulation` | tool | product- yitang | product- yitang |
| `yt-personal-ai-capability` | tool | personal-growth- yitang | mastersource_person: Truman |
| `yt-personal-ipo-learning` | tool | personal-growth- yitang | mastersource_person: Truman |
| `yt-personal-y-model-exploration-2` | tool | personal-growth- yitang | mastersource_person: Truman |
| `yt-pitch-aphorism` | tool | content-production- personal | yitang- master |
| `yt-pitch-conflict` | tool | content-production- personal | yitang- master |
| `yt-pitch-emotionalization` | tool | content-production- personal | yitang- master |
| `yt-pitch-materialization` | tool | content-production- personal | yitang- master |
| `yt-pitch-sublimation` | tool | content-production- personal | yitang- master |
| `yt-tool-unit-model-ai-assisted` | tool | yitang- master | 无 |
| `yt-tool-unit-model-benchmark` | tool | yitang- master | 无 |
| `yt-tool-unit-model-construction` | tool | yitang- master | 无 |
| `yt-tool-unit-model-dynamic` | tool | yitang- master | 无 |
| `yt-tool-unit-model-selection` | tool | yitang- master | 无 |
| `学会提问在信息洪流中锻造批判性思维的利刃` | framework | ai-saas | mastersource_person: Truman |

## 2. bridge 卡目标域覆盖（0 张不足）

✅ 全部 bridge 卡目标域覆盖 ≥2


## 3. domain digest 链接不足（2 个）

| digest ID | 当前 linked digests | 建议 |
|:--|:--|:--|
| `five-step-domain-digest` | 无 | 补充 2+ 个相关域 digest |
| `yitang-research-domain-digest` | five-step-domain-digest | 补充 2+ 个相关域 digest |

## 4. 白名单（3 项）

- `tool-agent-crawl4ai`
- `tool-agent-firecrawl`
- `tool-strategy-gap-analysis`

---
*审计脚本: `90_control/scripts/cross_domain_audit.py`*