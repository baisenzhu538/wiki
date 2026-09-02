# #626 领取前置精读笔记（#431 岗位纪律：逐字读口述稿+笔记落盘）

> 时间：2026-09-03 01:3x · 老顽童 · 任务单 task_20260903_laowantong-live77-live86-candy-cards
> claim 前置：素材消费率 ≥80%。三份素材已逐字读完，笔记如下。

## 素材 1：Live77 国帅课程创作心路历程（P0 一手口述，223 行/21.9KB，逐字读完）

**定性**：国帅复盘《Problem OS》+《谁在思考》两节课的**生产过程**（不是课程内容简介）。核心主张：「这两节课不是让 AI 写出来的，是用 AI 时代的工作方式炼出来的：人负责开题，机器负责加工，人负责判断。」

### 全链结构（L1-L14 节 → 15 节拆 11 条方法 → 16-17 节收束）

| 节 | 内容 | 关键数字/事实 |
|---|---|---|
| L1 | 真疑点火：先有困惑再有题目 | Problem OS 的困惑=「为什么有人明明在问问题，高手却只想关掉窗口」；《谁在思考》的困惑=「AI Coding 越来越强，为什么我反而觉得哪里不对」 |
| L2 | 旧文拆根脉：ESR 拆书会→四层能力栈定位（L1 问题定义/L2 信息获取/L3 信息研判/L4 组织驱动），ESR 归 L1 | 材料=ESR 原文+中文译本+一堂已有提问课+ChatGPT 讨论记录+已有逐字稿体例 |
| L3 | VPN 案例点燃抽象框架 | 「线下数据库同步线上主库」案例：提问者没吃透词汇、把焦虑发给别人；回答者被迫在效率与温度间选 |
| L4 | 豆包对话触发（修正主义视频→VibeCoding） | 豆包早期发散好用但太顺着人，「太精准了」式迎合 |
| L5 | 抓豆包会话接口（工程化存材料） | 分页=index_in_conv-1；agw-js-conv 数字变字符串；content_type=9999 文本在 content_block/tts_content；脚本 metadata/fetch_doubao_chat.py；131→169 条；扩成 all_chats.json+topic_index.json |
| L6 | Claude 给豆包回复做补充评论（claude_supplements.json→merged_conversation.json） | 「豆包负责流动，Claude 负责冷却；一个点火，一个控温」 |
| L7 | 长谈拆 5 篇：VibeCoding=编程修正主义/技术中立是谎言/去技能化陷阱/下一代程序员/当劳动变成特权 | 拆法不看聊天顺序看问题，「每篇只打一重靶」 |
| L8 | 理论加厚：伯恩斯坦/列宁三把刀/考茨基/九评/布雷弗曼去技能化/航海学徒制/苏联 27 年惯性 | 「每个理论都要回答：它在这里解决了什么论证难题？不能解决问题的引用，删」 |
| L9 | 多模型挑刺：ChatGPT/Grok/DeepSeek/Gemini/豆包，Claude 做裁判，人做最终主编 | ChatGPT 提防工程保守主义；Grok 提 Karpathy 原意是 weekend project；DeepSeek 提有意识妥协留空间；「多模型不是投票器，是盲区探测器」 |
| L10 | 发布后反馈长出第 6 篇《当编程变成审美》 | V2EX 反馈+体感「AI 一分钟写完，你花两小时 review，san 值归零」 |
| L11 | 六篇重熔→brief 收束为一个 O 的问题：AI 时代谁在思考 | 「Problem OS 讲 I（问题定义），《谁在思考》讲 O（答案判断），中间 P 由 AI 承担」 |
| L12 | AI俱乐部分享关键重构：IPO 位移先行，判断力正面价值先行，VibeCoding 降为案例 | 「再好的案例也不能抢主线」 |
| L13 | 图片产品化：Markdown 占位+中文提示词+Gemini 生图+上传 CDN+保留提示词 | 细节：·改丨（生图易出错）；「三根拐杖」中文错重绘；「品味」改「审美」重做；「有罪推定」改「默认存疑」 |
| L14 | 口语化：从已上线逐字稿提炼口语化规则→instruction.md→before 备份→改写→润色对比 | 「书面稿给眼睛，直播稿给耳朵」；例句改写对比（L151） |

### 11 条方法口诀（15 节，原话精要）
1. 真疑先把题眼开——不从「我要写什么」从「我一直解释不清什么」开始
2. 顺手工具先发散——早期最怕的不是乱，是没火
3. 聊天记录要存下——好材料不要死在聊天窗口里（灵感→生产资料）
4. 一边发散催火势，一边冷判验虚实——低摩擦模型陪你跑，强判断模型把你拉回来
5. 长谈莫急缝长文，问题先分成簇——每篇只打一重靶
6. 理论若能破难题，留下便是好兵器——答不上「它解决什么论证难题」就删
7. 多方挑刺照盲区，最后落锤在人手——别把主编位置让出去
8. 真实案例点明火——一个 VPN 案例胜过十句「提问很重要」
9. 文章可以铺开讲，课程必须收成线——课程必须重新确定主问题
10. 图片互动都算数——它们不是美化，是理解路径
11. 写得完整还不够，讲得出口才算成——书面稿解决「说得完整」，口语稿解决「听得进去」

### 与 KDO 生产线同构点（任务单指出的互链方向）
- 思想生产线 vs KDO 素材→卡→审查→入库管线：都是「人开题/机加工/人判断」
- 多模型审稿+人做主编 vs KDO 自攻击（多路 Agent 攻击）+欧阳锋终审
- 口语化规则文件（instruction.md）vs KDO content-production-polish skill
- 「聊天记录变生产资料」vs KDO 10_raw→30_wiki 素材管线

### 先例双查结果（动手前查，L1/L7 牌）
- **framework-candy-transcript-workflow**（reviewed，6-21 批）：Candy 逐字稿九步法——覆盖**单篇逐字稿生产**（搭参考系/差异化定位/框架成立/案例激活/案例服务结构/标题主语/配图结构/口语化/AI 协作者）
- **tool-candy-positioning-canvas**（reviewed）：差异化定位四象限
- **case-candy-problem-os-vpn**（reviewed）：VPN 案例单卡
- 主题词 grep「思想生产线/人开题/课程创作八步/创作八步」全库 **0 命中**
- **增量判定**：存量九步法=单篇稿子怎么写；Live77=**多文档课程产品的思想生产线**（困惑寻题眼→多模型审稿→六篇拆靶→brief 收束→发布反馈再生第六篇）。差异轴：①起点（困惑 vs 参考系）②规模（六篇系列+两节课 vs 一篇）③多模型审稿引擎（ChatGPT/Grok/DeepSeek/Gemini/豆包五家+Claude 裁判——存量卡无）④聊天记录工程化（接口抓取/索引/素材库——存量卡无）⑤发布后反馈再生（存量卡无）。→ 真增量成立，可产 2-3 张

### 传播限制
grep「外传/内部/密级/不要传」**0 命中**→ 无密级标注需求

## 素材 2：Live86 Candy kinda 龙虾员工实践 + Agent 创建模版（作业奖励加餐，680 行根目录版 + 1231 行合集版，两版逐字读完）

**版本对账（关键事实）**：根目录版 `00_inbox/AI落地Live86-Candy-kinda龙虾员工实践+Agent创建模版-逐字稿.md` L680 为「## 二、kinda实测好用Agent的创建模版」**空标题，正文缺失**；合集版 `00_inbox/学习candy合集/🍬AI落地Live第86场 Candy...（逐字稿）.md` L731-1225 含**完整模版附录**（注：源文档含两份相同副本，合集版保留一份）。→ 对账以合集版为准。

### 主体（L10-728）与 08-19 第一版十卡的重叠面
- kinda 实践叙事（ComfyUI→训虾→架构师/运维专家/龙虾版飞书/财务助手/提炼建模专家/十指讲香/AIGC）已被 #379 批 case-kinda-digital-employees-fullview 等十卡覆盖
- Feature 五能力（清晰表达需求/AI 适配化/评判 AI 内容/最佳数据源/AI 人效）已各有 dk/tool 卡
- MCP/gateway 洞察、项目经理 Agent 失败教训已有 dk-project-manager-agent-failure

### 模版附录（L737-1225）结构——对账核心
11 节全生命周期白皮书模版（含占位符可复制）：
- §0 使用方法：白皮书=workspace 初始化/tools 权限/BOOT.md/registry/openclaw.json 的**唯一权威来源**；填写流程「kinda 填需求摘要→大虾补技术细节→kinda 确认定稿」；定稿后从 ONBOARDING 模版复制创建入职简报
- §1 基础信息：Agent ID/显示名/定位语/创建原因/工作区路径/是否前端可见
- §2 职责与边界：核心职责表/**不做什么（边界界定）**「明确不做的事比做什么更重要」/协作感知规则（自查 registry.yaml→A2A 对接，不经中转）/自驱维护规则/知识库预检规则
- §3 通用技能 12 项（全体标配）：图片阅读/上下文压缩/记忆索引/模型实时调配/自驱优化/重启恢复/协作感知/网络搜索/复盘/项目文档/文件识别/知识库与技能预检
- §4 专属技能+代码能力（exec 限定命令/读写范围/安全约束）
- §5 任务分级（S/A/B/C 模型路由：deepseek-v4-pro $1.74 vs flash $0.14，Pro 贵 12 倍；图片理解 Qwen2.5-VL 免费额度/moondream 兜底/SD3.5/FLUX）
- §6 知识库（scope: self/all）
- §7 Agent 画像（基础身份/核心四象限/语气风格/阻塞处理优先级/「绝不等 kinda 来问进度」）
- §8 技术配置（compaction 8000/contextPruning 5m/memory bge-m3/session 30d/500、权限三层：自动跑/需审批/禁止、Sub-Agent 规则「基于已有 Agent 能力镜像，做完即销毁」）
- §9 协作流程（分工域/协作协议/A2A 超时 600s 勿设小/流水线 R1-R5/「短期 BOOT.md 强制预处理，长期 Gateway 层注入」）
- §10 初始化清单 16 步（含**灵魂校验三问**：有让人记住的标签吗/有核心信念吗/说得出「它是什么样的人」吗——三个「没有」→ 不准定稿；身份断言写入 AGENTS.md；建桥仪式：大虾统一发 A2A 通知所有 Agent 主动联系新 Agent）
- §11 变更日志+附录（配置文件修改分工「大虾出方案→Mat 动手改（大虾有多次写坏记录）→大虾验证」；各改动类型是否需重启 Gateway 表；改 JSON 前先备份）

### 先例双查
- **tool-agent-white-paper-five-elements**（pending_review，08-19 批）：五要素定义（名字/职责/能力/数据库/虚拟人格）——**定义层，无边界界定/无通用技能标配/无任务分级/无权限三层/无初始化清单/无灵魂校验**
- **framework-truman-agent-team-architecture**：Truman 龙虾架构（模版来源侧引用）
- 增量判定：**模版附录=真增量**（11 节全生命周期工程化模版 vs 五要素定义卡），补 1 张 tool 卡：`tool-agent-whitepaper-full-lifecycle-template`
- 传播限制：L6「内容开放复制权限，**自己练习，不要外传！**」→ 按 #322 口径双标注（source_context ⚠️ + 正文密级声明），模版结构可引，业务细节脱敏

## 素材 3：WorkBuddy 流水线 pending 卡（任务 3 门禁判定）

- 卡：`00_inbox/pending-cards/case-wechat-article_tt_af50baaada5fc2f2.md`（3942B，楚门三层次框架）
- 源文：`00_inbox/wechat-collect/src_wechat_article_tt_af50baaada5fc2f2.md`（今日头条·偶遇转发，全文已读）
- 事实层验证：卡内 5 事实+5 规律+5 洞察逐条对源——6h（选题1/查资料1/写稿2/排版配图1/分发1）✓；「跑一下今天的选题」指令+20min 终审 ✓；四步 60→2/90→4/40→2/20→2 分钟 ✓；22 篇+40% 阅读量（归因稳定更新）✓；首次配置清单 5 项 ✓
- **卡结构缺陷**：「✅ 可行动建议」节为空（TODO 占位）；「规律/洞察」两节是空壳（内容挤在事实节）；无 aliases/related/quality_labels；domain: pending-domain
- #380 机制：pending 卡不进 30_wiki，王语嫣编排门禁判定→不够格退回/够格转正走生产流。本卡=**素材事实层扎实但未达 case 卡成品标准**→ 判定：**补齐转正**（补 frontmatter/行动建议/结构归位后转正提审）——任务单明示「过了就补齐 frontmatter 归位转正提审」

## 建模方案（L1 出牌）

组件链：`[素材牌] → [边界牌] → [结构牌] → [过程牌] → [质量牌]`
- **[素材牌 L2]**：Live77 223 行逐字读 ✓ / Live86 合集版 1231 行逐字读（含模版附录全文）✓ / pending 卡+源文全文 ✓（本笔记即证物）
- **[边界牌 L7]**：与 framework-candy-transcript-workflow（九步法，单篇）/ tool-agent-white-paper-five-elements（五要素定义）精确切边——Live77 卡=生产线级（多文档+多模型引擎），Live86 卡=全生命周期模版（11 节工程化）
- **[结构牌 KF-024]**：framework 卡=适用边界+失败模式+When NOT to Use；method 卡=操作步骤+判断标准；tool 卡=使用步骤+When NOT to Use+失败模式；case 卡=关键数字+证据表
- **[过程牌 W6]**：①WebSearch——Live77 关键概念「思想生产线/Problem OS/多模型审稿」国际术语对齐；②六层交叉——Live77/86 均单一来源口述，如实降级标注；③九层深挖在卡内执行
- **[质量牌]**：逐卡 kdo pre-submit → 自攻击 → L12 git status → complete → L9 双验证

## 卡片规划（任务1 卡 2-3 张 + 任务2 补 1 张 + 任务3 转正 1 张）

1. **framework-course-thought-production-line**（ai-collaboration）：国帅思想生产线——人开题/机加工/人判断全链 11 环（困惑寻题眼→…→口语化），含 11 方法口诀、与 KDO 生产线同构映射、When NOT to Use
2. **method-course-creation-eleven-steps**（或并入 1，视篇幅）:11 条方法口诀操作化——每条=触发信号+动作+判断标准
3. **dk-course-starts-from-unavoidable-question**：「课从绕不过去的问题开始，不从知识开始」——含 ESR 定位案例（凭什么单独开一节→四层栈 L1）、反例（知识转述/概念搬运）
4. **tool-agent-whitepaper-full-lifecycle-template**（Live86 任务2，ai-collaboration/knowledge-management）：Agent 工作白皮书 11 节全生命周期模版——五要素卡的升级引用+边界界定/通用技能 12 项/权限三层/初始化 16 步/灵魂校验三问；#322 双标注
5. **case-wechat-article_tt_af50baaada5fc2f2 转正**（任务3）：补 frontmatter（domain→ai-collaboration、aliases/related/quality_labels）+填可行动建议+结构归位→pending_review

> 注：#431 状态细分——claim 后落 in_progress 证据；批次纪律——任务3 转正卡单独 pre-submit。
