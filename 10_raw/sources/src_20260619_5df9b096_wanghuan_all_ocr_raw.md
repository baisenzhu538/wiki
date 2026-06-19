# 王欢 AI 实战分享 — OCR 原始文本合并


## 王欢-AI实战分享-AI native定义-示意图

AINATIVE·定义
The Definition
AINative不是会用很多AI工具，
而是当你遇到问题时，
【默认把AI纳入流程】，
并把高频任务【沉淀成可复用的资产和系统】。
AI Native is not about mastering many AI tools - ①默认纳入 DefaultIntegration
it's about defaulting AI into your workflow, and 工作方式的转变
turning recurring tasks into reusable systems. ②沉淀成资产 AssetAccumulation
复利能力的建立


## 王欢-AI实战分享-AI业务档案的五个字段

AI业务档案·5个字段
Your AI Business Profile — 5 Fields
01 ·关于我 角色和核心职责
About Me Role&keyresponsibilities
02 我服务谁 WhoI Serve What they care about 客户/上级在乎什么
03 我的风格偏好 表达习惯
My Style Voice&preferences
04 行业暗规则 Tacit Rules ★ Unspoken defaults 不说但默认的事
05 我的输出标准 底线，不是格式
My Standards Red lines, not formats
每次新对话，第一步粘进去
Paste it into every new chat - Day 1.


## 王欢-AI实战分享-AI双角色教练训练-示例图

本周共情力提升12% 欢迎回来，张顾问销冠！
本周数据
8次 ★76分
训练次数 平均得分
90 得分趋势
80
70
60 周一 周一 周二 周二 周三 周三 周四 周四 周五 周五 周六周六 周日
场景完成度
电话邀约 80%
到店咨询 60%
价格异议 40%
开始训练→
11/80 38% + 国 一


## 王欢-AI实战分享-AI工具链四级台阶-示意图

AI工具链·四级台阶
The Four-Tier AI Tool Ladder
系统级·System Claude Code－Hooks + Sub-agents 指挥AI团队
自主级·Autonomous TraeSOLO－AI自己规划、执行、测试、部署
角色升级：操作员」导演」制片人
工程级·Engineering TraeIDE/Cursor－描述需求，AI写代码 ←今天目标
对话级·Dialogue 豆包/ChatGPT/Claude－你问它答


## 王欢-AI实战分享-AI能力五层跃迁-示意图

五层跃迁：从使用AI到掌控AI
从问问题，到做出系统级AI操作台
层级 命名 核心跃迁 晋级标准
第一层 问答层 从“问AI"到 能识别幻觉，
“验证 AI" 知道何时交叉验证
第二层 工作流层 从一次性对话到 口述输入、会议重构、
可复用上下文 项目化知识库已常态化
第三层 作品层 从辅助工作到 T|<> 能产出内容、代码、
产出真实作品 智能资产三类作品并被验证
第四层 产品/应用层 被人持续依赖 从单点作品到 有维护、有版本演进 有真实用户、有数据、
第五层 系统层 从单点产品到 有编排底座、技能库、
工程化的AI操作台 自动触发、反馈闭环
一句话主轴 第一层解决答案，第二层解决效率，第三层解决作品，第四层解决交付，第五层解决工程化。


## 王欢-AI实战分享-BTICOE框架-示意图

BTICOE框架
Six Slots to Eliminate Ambiguity
B T T C E
Background·背景 Task·任务 Instruction·指令 Constraint·约束 Output·输出 Example·示例
你是谁/你的处境 这次做什么 按什么逻辑做 不要做什么一最致命 什么格式 什么风格
不是公式，是消灭模糊的思维习惯
Not a formula, but the habit of killing ambiguity before you speak.


## 王欢-AI实战分享-GAN启发的三角色架构-示意图

GAN启发的三角色架构
三个不同公司。 灵感来自生成对抗网络（GAN）—生成器和判别器对抗进化，但这里判别器是四个，来自
用户 一句话or spec.md
Team Lead 当前Claude会话·负责编排
Claude Sonnet
 Phase 1 → Planning
只路一次·产品规划 Claude Opus Planner 技术栈选型 Tech Stack Selector
Phase 35 →> Sprint Iner Loop (Workflow)
每轮全新启动·“牛模式” Generator
写代码·commit·退出
VFunctional Tester Adversarial Tester
pouuos opnero 跑起来测验收标准Happypath Claude Sonnet 主动攻击·目标是找bug
Codex Evaluator 代码审查·专注安全边界 架构设计·原创性评分 Gemini Evaluator
OpenAl Codex Google Gemini
Sprint 边界→ Regression Net
Master Integration Tester
Claude Sonnet 跑所有已完成Sprint的验收标准·防回归
(adversarial）比被动审查能找到更多bug—它的成功标准就是找到你的问题。 为什么四个判别器？Codex（OpenAl）和Gemini（Google）来自完全不同的模型族，训练分布不同，盲区不重合。主动攻击


## 王欢-AI实战分享-harness的七个阶段-示意图

七个阶段，从规划到交付
Harness把一次构建分解为严格定义的阶段，每个阶段有明确的输入、输出和质量门控。
PHASE 0 初始化&预检
恢复。 创建harness/目录、检测CLI工具、生成budget.ymL（默认：50轮选代，8个Sprint，4小时墙时）。自动检测是否需要从checkpoint
PHASE 1 Planner:产品规划（Opus模型）
义等待解决。 用最强推理模型做产品规划—只跑一次，成本可控。输出product-spec.md（功能优先级、审美方向、送代计划），同时标出所有高风险歧
PHASE 1.5 TechStackSelector：技术栈选型（Opus模型）
未列出的顶层依赖。 Planner结束后立即确定技术栈。输出tech-stack.md一语言、框架、测试工具、构建工具、部署目标、选型理由。Generator不得自行引l入
PHASE2-5（循环) Sprint对抗循环
围。 每轮Sprint：写Sprint Contract→启动Workflow→Generator构建→四个Evaluator并行评分→决策引擎判断是继续、修复、还是裁剪范
评分通过条件：没有维度低于3分、加权平均≥4.0分（取两个代码审查者中更严那个）、零CRITICAL对抗发现。
PHASE 5.5 PolishSprint:审美精修
3，功能维度下调到1）。 所有PO功能完成后，自动插入一轮PolishSprint：空状态、错误状态、加载动画、字体节奏、微交互。评分权重自动切换（审美维度上调到
PHASE 6 ShipPipeline：最终交付
顺序执行，每步互为门控： ①AestheticReviewer（Opus）整体审美评分≥4.0才过
②文档生成器写README+CHANGELOG+KNOWN_LIMITATIONS并提交
④AuditTrail生成从spec到ship的完整旅程记录 ③FreshCloneTester从零克隆、按README操作，确认真的能跑


## 王欢-AI实战分享-OODA循环-示意图

OODA 闭环
The Decision Loop That Compounds
O·Observe·观察
See thefacts 看见事实 定位坐标 Find your position
A·Act·行动 OO·Orient·定向
Spins faster each loop 越转越快
Collect new info 采集新信息 可验证的决定 Verifiable decision
D·Decide·决策
你不需要确定，你只需要比上一圈快
You don't need certainty. You only need to be faster than your last loop.


## 王欢-AI实战分享-PACED框架-图-01

PACED框架
The 5 Dimensions a Sales Champion Judges in Every Consultation
P -C-ED
Pain·痛点 Authority·决策链 Capacity·消费能力 Expectation·期望 Decision·决策时机
孩子真实问题 谁拍板 付费意愿 提分／习惯 临考前/开学前
家长真实焦虑 谁影响 价格 vs 价值 名校路径 还在观望
教你看什么，不是教你说什么
Teaching you what to see, not what to say.


## 王欢-AI实战分享-医语轻记-示意图

11:52 80
vConsole医语轻记
Connected Vi..ore
2 1
今日接 本周接 理 患者管 随访管 理 理 订阅管
诊 诊
手机号(可查历史）
姓名 男 年龄 岁
标签： 复诊 过敏 高血压 糖尿病
录入方式
自由录入 标准问诊
语音/文字快速记录 10个维度系统采集
点击此处输入，或长按下方麦克风录音。例
林。 如：患者咳嗽三天，喉咙红，开了阿莫西
接诊 病历本


## 王欢-AI实战分享-导演的工作方式-图-01

导演的工作公式
The Director's Workflow
POAt
定义 AI执行 验收
DEFINE－开头 AIEXECUTES－中间（你不亲自做） REVIEW－结尾
导演=定义 (开头）+验收 (结尾)
Director = Define + Review
中间的执行交给 AI
Middle execution delegated to AI


## 王欢-AI实战分享-标准的力量-示意图

标准的力量
Standards Are Multipliers, Not Addends
←一乘数 (最关键)
最终质量=你的标准×AI执行力×迭代次数
Final Quality  =  Your Standards   ×   AI Execution   x  Iterations
标准是零，乘什么都是零
If standards = 0, the product = 0
导演的工作不是操作工具，是定义标准/Thedirectordefines standards,notoperatestools


## 王欢-AI实战分享-海报工具-示意图

万 万山AI WanshanAl 万山AI·海报工具 AI一键生成营销海报 已完成
海报工具 海报预览 已生成 历史
起名工坊
产品定价 一键识别 手动填写
品图片工具 AI落地诊断? 粘贴结构化的海报信息，点击「立即识别后将自动拆成可编辑的字段
AI聊天 业务翻译官
甲公众号排版 90-120分钟1对1深度共创，在你投入 AAt
L数据分析 第一步怎么做 真金白银之前，帮你判断值不值得做、 王欢 AI原生开发者
填入示例 清空 立即识别
如果你 ·有想法但不确定值不值得投入
·怕动手之后才发现方向错了 ·找开发却说不清自己到底要什么 必填信息 产品名称* 12/12
我会如何帮你 前置问卷筛选匹配，深度共创诊断，交付 含问题定义、MVP骨架及行动清单的落地蓝图 AI落地诊断·业务翻译官
·当场判定你的想法该不该现在做 产品描述 43/40
你将获得 ·理清你真正要解决的核心问题 ·拿到第一版MVP骨架和工具路径 ·获得7至14天可直接执行的行动清单 得做、第一步怎么做 90-120分钟1对1深度共创，在你投入真金白银之前，帮你判断值不值
·省掉几个月试错和几万块冤枉钱 用户痛点* 39/40
适合谁 ·有真实业务场景 愿意动手执行 填写问卷，匹配预约 有想法但不确定值不值得投入
怕动手之后才发现方向错了 找开发却说不清自己到底要什么
定价：￥2000 666夫：与古 产品解决方案· 39/40
动清单的落地蓝图 前置问卷筛选匹配，深度共创诊断，交付含问题定义、MVP骨架及行
产品预期效果· 73/75
草稿已自动保存 当场判定你的相法该不该现左做 228/500字
V1.0·更多功能即将上线 C换一张 下载海报 生成海报


## 王欢-AI实战分享-选场景五条标准-示意图

选场景·五条标准
Five Criteria for Choosing Your First Product
01一真实痛点/RealPain
你自己每周都在头疼的事
02－高频复用/High Frequency
每周至少用3次
03－30秒说清/30sPitch
能让陌生人一句话听懂
04－下周还会用/NextWeekTest
做完了下周还会打开吗？
05－你最熟的领域/YourDomain
行业知识=差异化优势
你是自己最好的目标用户
You are your own best user.


## 王欢-AI实战分享-飞轮第一圈-示意图

飞轮启动·第一圈
The Flywheel: First Loop
①AI业务档案 Business Profile ②Prompt模板库
Prompt Library
1st loop
③行业暗规则
Tacit Rules
第1圈·最难· >第3圈·模式浮现· 第10圈·你有系统
Loop 1: Hardest Loop 3: Pattern emerges Loop 10: You have a system
飞轮不怕慢，怕的是不转
Flywheels don't fear slowness -- only stillness.
