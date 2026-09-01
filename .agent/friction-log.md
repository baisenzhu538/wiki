---
type: friction_log
created_at: 2026-08-09
owner: 全角色共享（王语嫣建立，黄药师 #276 机制化）
updated_at: 2026-08-09
---

# 摩擦日志（Friction Log）

> **机制**（#276 · herd-core 模式）：遇摩擦/阻塞/返工/被打回时**当下**追加一行，不等会话结束。
> 周报合成：王语嫣每周一 #265 通道 4 读本文件 → 升级为复盘/任务/知识库进化信号。
> 规则：一行一摩擦；根因初判即可（不用完整诊断）；写错不删，追加修正。

## 记录格式

| 时间 | 角色 | 场景 | 摩擦 | 根因初判 |
|:--|:--|:--|:--|:--|

## 记录

| 2026-08-09 | 王语嫣 | 队列状态流转 | queue_transition complete --force 对 queued 任务被 O-3 锁内 re-check bug 拦截 | 脚本 expected 恒为 claimed-{instance}，force 分支未改锁内判断（O-3 家族）→ 手动 patch 兜底 |
| 2026-08-09 | 王语嫣 | 建议书编号 | 黄药师交付用建议书编号（#267s/#268s），队列编号不同（#273/#274），需内容映射 | 建议书编号是建议性的，入队统一分配编号的约定未写进建议书模板 → 建议：建议书模板加"编号以队列为准"字样 |
| 2026-08-09 | 王语嫣 | 双轨 skill | 探索发现 .claude/skills 与 shared 无桥接脚本，17 个缺失、格式漂移 | 同步机制从未建立（B1 #267 待做）；生命周期工具管 39 个（shared 侧），.claude 侧仍待同步 |
| 2026-08-09 | 黄药师 | #267 同步脚本 | read_fm 解析列表字段 allowed-tools 为空串 → 校验误报 17 失败 | 解析器只提取标量值，列表字段键存在≠值非空——校验逻辑应区分"键存在"与"值有效" |
| 2026-08-09 | 黄药师 | #267 同步脚本 | shared 部分文件带 BOM（﻿）→ 正则不匹配 → 51 个假漂移 | 编码细节（BOM）未在读取层统一处理——读文件先 _strip_bom()，hash/正则/转换共用 |
| 2026-08-09 | 黄药师 | #272 schema | 7 个 schema 的 review_date 块格式不同（含 description 行 vs 裸字段）→ 批量插入脚本 dry-run 时 dark-knowledge 漏匹配 | 批量改 schema 前应先扫全部变体格式（P-29 教训在 schema 域复现） |
| 2026-08-09 | 老顽童(kimi) | production-queue 解析 | claim #285 报"任务不在队列"——王语嫣前次修复把注释块移出表格但仍夹在 #284/#285 行之间，parse_queue 遇非表格行提前 break，#285-288 不可见 | 修复后未跑解析验证（看 diff 觉得对≠解析通过）。已二次修复：注释移至文件末尾表格之后，267 行全通。建议：queue 文件任何编辑后跑 `queue_transition.py status` 验证总数 |
| 2026-08-09 | 王语嫣 | #282 spec related | agent-spec-review-coach 死链复发（#268 C1 已修过一次，旧 id 复用；同错误第二次实证）+ tool-yitang-daily-weekly-meeting-host 拼写错误（实为 -hosting） | spec related 字段引用的卡 id 未做存在性校验（#268 C1 修复未沉淀为检查动作）；拼写未核对真实文件名 → 修复：写 spec 时 related 逐项 grep 存在性（C2 已修，friction-log 记录防第三次） |
| 2026-08-09 | 黄药师 | 部署 #303/#304 SOUL | TCPR 写成 Thinker/Coach/Practitioner/Reviewer，KDO 正确定义是 Teach/Consult/Practice/Research（agent-os §1）——全链污染至飞书 | 虚假熟悉感（四字母+四英文词形态触发常见术语填充）+ 未执行域知识检索铁律（定义就在 agent-os.md 我一步没查）+ spec 上游也错未交叉验证 → E020 记录 + #263 流水线加编译期验证 |

---

## 2026-08-10 黄药师：SOUL.md 模型先验覆盖

**现象**：SOUL.md 写入新 TCPR 定义（Teach/Consult/Practice/Research），gateway 重启，agent 三次回复都是老版 TCPR（Thinker/Coach/Practitioner/Reviewer + Assistant 默认身份）。

**根因**：deepseek-v4-flash 对 
| 2026-08-13 | 黄药师 | #317 verified 提审 | 提审汇总表数字与最终产物不一致（报告"实测6/引用2/推演5"，JSON 实际"7/2/4"）——狗粮测试抓出 F022 漂移修正后报告未同步；队列备注数字正确 | O-11 家族教训 +1：报告是快照，JSON 是真相——审查必须重数不信表格。建议：下批提审汇总表以 JSON 为准复写，交付时先 diff 报告数字 vs 产物再提审 |
| 2026-08-15 | 黄药师 | 记忆恢复 | 技能进化日志乱序——08-03/04 段（22 行）跑到 `# 技能进化日志` 标题上方，08-10/08-13 尾挂底部 | 历次编辑累积：08-03/04 插入时误置文件头、后续追加未按"最上方追加"约定（P-30 家族：批量/连续编辑后未验证结构）。已重排为降序（08-15→06-07），内容逐字保留 |
| 2026-08-15 | 黄药师 | 记忆恢复 | amnesia 锚点 P0 表写死"读 2026-08-10.md"但目录实际已到 08-13——快照过期，照抄会读到旧状态 | 08-13 更新锚点时只改了快照节没同步 P0 指引表（声明"已更新"≠全文件逐节核实）。已改"目录内最新"原则；欧阳锋同日发现同类问题（恢复指引写死 08-09） |
| 2026-08-15 | 黄药师 | 记忆恢复 | huangyaoshi-context.md 技能进化日志路径漂移——写 `agent复盘/huangyaoshi/技能进化日志.md`（英文目录，不存在），实际在 `agent复盘/黄药师/daily_cognitive_review/`（中文目录） | 中文目录是 6 月旧体系、英文目录是 Phase 1 新体系，context 更新时只改了路径字符串没验证目标存在（B3 先查已有文件的反面）。改 context 属 D4 自我修改，需王语嫣/欧阳锋批准——已记录待拍板 |
| 2026-08-15 | 黄药师 | D4 修正执行 | 欧阳锋裁决批准路径修正（D4 例外：纯路径纠错属事实性修正）——context L69 路径已改正确，顺带把格式描述"追加一行表格"对齐为实际文件的 Keep/Improve/Add/Stop 段落格式 | 裁决先例：D4 门禁防的是"自我修改审查纪律/绕过审查"，纯路径纠错不涉判断可直接批准。格式描述与实际文件不符同属"动作落空"根因，一并修正 |
| 2026-08-16 | 黄药师 | #325 快照 agent 指令 | CLAUDE.md 检索指令初稿写 `python kdo-tools/query.py`——实测该文件不存在（CLI 入口是全局 `kdo query`） | 凭"kdo-tools/ 里应该有个 query 脚本"惯性命名，没先实证命令入口——写进文档的命令必须先跑 --help/--version 实证（落盘前抓住，未造成返工） |
| 2026-08-16 | 黄药师 | #325 MCP 验收 | 协议级实测 tools/list 首次无响应——漏发 MCP 协议 `notifications/initialized` 通知 | 凭 HTTP"一请求一响应"直觉，未按 MCP 生命周期（initialize→initialized→requests）走——协议类验收按协议规范步骤执行 |
| 2026-08-16 | 黄药师 | #326 狗粮 | WSL 侧 kdo_search 空结果根因=跨平台路径 bug：Windows 侧构建的 BM25 索引存 `C:/...` 格式，WSL 侧 `root / path` 拼接畸形路径 → `_filter_by_trust` 全滤空 | delivery.py `_filter_by_trust` 无跨平台路径处理——已 patch（Windows 盘符路径转 `/mnt/<盘符>/`，POSIX 下生效）。狗粮抓出，非配置问题 |
| 2026-08-16 | 黄药师 | #326 狗粮 | check-agent-config.py `open(config_path)` 无 encoding——Windows Python 默认 GBK 读 WSL UTF-8 config → 8 个 P0 误报中 5 个是编码误报 | 与 #323 同族（GBK 默认编码）；已修 `encoding="utf-8"`。教训：读文件一律显式 encoding，不依赖系统默认 |
| 2026-08-16 | 黄药师 | #326 狗粮 | test_cli_smoke 的 subprocess `text=True` 无 encoding——GBK 下 decode 中文输出崩 → stdout=None | 测试基础设施同族问题；已修 `encoding="utf-8"`。遗留：state.json `sources` 断言过期（SQLite 迁移后键已移入 state.sqlite）——历史失败，记队列待排 |
| 2026-08-16 | 黄药师 | #326 狗粮 | WSL 系统 `python3` 无 `mcp` 包——模板渲染 `command: python3` 会挂；Hermes venv python 含 mcp | 模板 WSL 侧 command 已改为 Hermes venv python 绝对路径。教训：模板渲染的命令必须逐侧实测（不能假定两侧环境一致） |
| 2026-08-16 | 黄药师 | #267 sync 漂移修复（洪七公纠偏） | task-orchestration 双轨同版本号 1.0.0 但内容不同（.claude 侧缺 E028 索引纪律节）——版本机制发现不了同版本漂移 | 改了一侧没同步（或改了没升版本号）；已收敛（shared 为准 sync --apply）+ 升 1.0.1 让漂移可被版本机制发现。可选：bridge status 加"同版本内容不同"周检（洪七公建议 4） |
| 2026-08-16 | 王语嫣 | #327 试点验证 | `kdo index --rebuild` 提前 return 0 跳过 search_index.json 重建（--rebuild 语义与直觉相反：只重建 index.md/backlinks，不带 --rebuild 才 build search_index）——#325/#326 文档 Step 4 写的 `kdo index --rebuild` 用法错误，8-16 新卡 4 小时检索不到 | cmd_index 分支逻辑：rebuild 分支 return 0 在 build() 之前。已用 `kdo index`（无 --rebuild）修复并验证 5/5 新卡 HIT。需修正：#263 Step 4 文档命令 → `kdo index`；KDO 源码 cmd_index 行为建议黄药师评估（可加 --search-only 或合并逻辑） |

## 2026-08-16 KDO commit 督促（欧阳锋→黄药师）
- **背景**：今天 3 个 KDO 源码修复（delivery.py WSL 跨平台路径 / search_index.py --rebuild 全重建 / test_cli_smoke encoding）均在未提交工作区（共 24 处改动，含历史累积 460 行）
- **用户拍板**：commit。执行人：黄药师（欧阳锋不越界提交 KDO 源码——非审查者产物）
- **要求**：按主题拆分或 message 注明范围；commit 后通知用户/欧阳锋验证
- **风险**：若不 commit，今天验证过的修复只有工作区副本——机器重启/清理后丢失
| 2026-08-16 | 王语嫣 | #331 名称混用 | 任务书/执行报告把"一堂基本功教练"（管理域组织能力基本功，agent-一堂-基本功教练.md）写成"AI基本功教练"——实际 AI基本功教练（basic-skills-coach）是另一 agent（非快照型，Feature 周期表+MOC 导航+ #308 检索已就位），不在 38 盘点内 | 名称未核实即写入交付文档（E027 同族：术语传播前必须核实指代对象）。用户质询暴露。已澄清：通用基本功域迁移有效；AI基本功教练无需三步走 |
| 2026-08-16 | 王语嫣 | #331 审查链污染（升级） | 完整错误链：①#331 任务书写"先行：AI基本功教练（basic-skills-coach，快照型）"——前提错误（basic-skills-coach 非快照型，CLAUDE+system-prompt 独立部署）②实际迁移 agent-一堂-基本功教练.md（管理域拆建推练编译产物，孤儿：agents/ 无对应部署）③欧阳锋按表述终审了孤儿产物——审查对象错位被误导 | 名称未核实指代对象即写入任务书（E027 家族升级：从"传播错误定义"到"审查链污染"）。更正：AI基本功教练（basic-skills-coach）无需快照迁移（#308 MCP+6 MOC 导航已就位）；孤儿产物 agent-一堂-基本功教练.md 待核查处置（引用指向修正或归档）；请欧阳锋在审查校准记录标注此案 |
| 2026-08-16 | 王语嫣 | task-orchestration 双轨核验 | 洪七公报告双轨漂移（同版本号内容不同）——核验：当前正文 100% 一致+版本同步 1.0.1，差异仅 frontmatter 格式（双系统预期适配）；其"版本机制发现不了差异"洞察成立（内容单侧更新不升版本号则检测不到）→ 采纳周检防复发 + 建议 #267 桥接脚本补内容 hash 校验 | 教训：diff 用进程替换 <(cat) 在 git bash 输出不可靠（误导 2 次判断），直接文件 diff 为准；核验类结论必须重跑验证 |
| 2026-08-16 | 黄药师 | 技能丢失排查（老顽童迁移后） | ①shared 70 技能只有 19 个被 Hermes 加载——`platforms: [cli, feishu]` 是 KDO 接口语义，Hermes 只认 OS（macos/linux/windows）→ 51 个全判 unsupported（含 kdo-self-attack 生产门禁）②老顽童记忆技能（pre-submit-self-check 等）在 WSL 全局 `~/.hermes/skills/`（35 个）未迁 Windows ③**双实例澄清**（用户）：laowantong CLI（AppData/Local/hermes，hermes.bat 启动）vs laowantong-feishu（WSL）是两个独立实例——#325 挂 MCP 到 `.hermes/profiles/laowantong` 对 CLI 无效（CLI 用 AppData）④**laowantong-feishu HERMES_HOME 实证**（gateway.pid）：= `AppData\Local\hermes\profiles\laowantong-feishu`——全局技能在 profile 级 skills/（非 AppData/Local/hermes/skills/），先复制错位置，已修正 | ①platforms 已改 [linux, macos, windows]（70/70 可注册，官方 CLI 实测 duanwangye 154 技能全 enabled）②35 技能合并入 AppData 全局（不覆盖，157 SKILL.md/148 可加载，pre-submit-self-check 恢复）③**CLI 实例 kdo MCP 已补挂**（AppData laowantong config，备份 .bak-mcp-20260816）④**laowantong-feishu 35 技能已合并入 profile 级 skills/**（152 SKILL.md/146 可加载，pre-submit-self-check 就位）⑤**CLI 实例（laowantong）35 技能已合并入 profile 级 skills/**（192 SKILL.md/182 可加载，skills list 189→250 enabled，pre-submit-self-check 就位）⑥**洪七公（beikai）Windows 侧修复**（codex 迁移配合）：35 技能合并入 profile 级 skills（195 SKILL.md/184 可加载，vision/creative/media 全在）+ external_dirs 从 WSL 路径改 Windows 路径（原指向 /home/、/mnt/c/ 在 Windows 无效）——多模态管线技能（comfyui/cosyvoice/wan-video 等）齐备 |
| 2026-08-16 | 黄药师 | wechat-collect 管线（proj_20260816） | ①模型下载：HF/ModelScope 大文件网络不稳（41-108KB/s）——多次中断，最终 wget -c 断点续传 + 无限重试成功（tiny 72MB）；small 残缺跳过 ②`_win_to_wsl` 只处理 C: 盘符——D 盘微信视频路径转换失败（ProtocolNotFoundError），已修任意盘符 ③**master-moc.md 是 UTF-16 编码**（0xff 开头）——kdo index 崩溃，已转 UTF-8（历史遗留顺手修） | ①网络限速 → wget -c 续传是最稳路径 ②路径转换必须覆盖任意盘符（不只 C:）③索引扫描遇非 UTF-8 文件会崩——UTF-16 文件需先转码。管线已全通：D 盘真实视频（169s+15s）→ GPU 转写 → LLM 三层次 → 可检索（E028 闭环） |
| 2026-08-16 | Codex(观察者) | #348 R型Partner 真机 | kdo_search 300s 超时 ×2——R型Partner 状态2 时反复重试死循环（726s 才挣脱），靠 /steer + grep 兜底恢复。O-16 已标"全厂 friction-log 无此记录、记录在 R 型自身 memories 未上浮" | kdo MCP 每次冷加载 585MB 索引+graph+3vdb 超 300s 上限（O-15 同族）；按 O-16 要求本次上浮到全厂 friction-log |
| 2026-08-16 | Codex(观察者) | #348 R型Partner 状态2 | GitHub API 未认证限流 10 次/分钟——6 工具存在性验证被限流（自报"GitHub API 未认证限流了…再查也白搭"）；状态 3 饱和送高频搜 GitHub 必卡 | 未配 GITHUB_TOKEN；已立 O-17 停车场（进状态3前配 token） |
| 2026-08-18 | 黄药师 | #350 MCP UTF-8 修复回归 | Python 客户端(FastMCP anyio)连 Python server 在 Windows 卡死——协议级验证需走 Go 客户端(Hermes) | 非修复引入;Windows anyio 管道兼容问题;协议验证归 #351 gateway 重启 |
| 2026-08-18 | Codex(观察者) | 段王爷 kdo MCP 检索 | kdo_search 冷加载→300s 超时→gateway 重启 kdo MCP→缓存清零→再冷加载的死循环：02:37:10 与 02:43:24 两次 query 打进 server 均无返回，02:40:41 keepalive TimeoutError（connected→degraded），02:49:18 kdo_search 300.02s 超时，02:49:32 新 server 进程又被拉起；段王爷飞书侧表现为"卡着不动" | search_index.json 538MB（08-16 构建）每个新进程整读整解析 + graph_index（07-04 陈旧）冷加载 >300s（O-15/O-16 家族）；get_shared_index 缓存是进程级、server 被重启即清零；11 个 server.py 并存争抢同一 538MB 文件 I/O。只读诊断，未改系统 |
| 2026-08-18 | 黄药师 | #351 MCP 检索卡死三连 | ①to_thread 无 running loop→LightRAG 崩 ②后台 loop 线程 daemon 静默死→run_coroutine_threadsafe 永久等待 ③warmup create_task 挂 get_event_loop() 死 loop(mcp.run 用自己的 loop) | 最终方案=主线程同步 warmup+同步执行(LightRAG worker 依赖主线程 get_event_loop);另:多次 NSSM 重启不杀子进程→旧 server 残留 |
| 2026-08-18 | 黄药师 | #356 条件项 onboard 索引化 | ①测试读错字段名(framework_cards vs framework)误判"全 0" ②domain-routes 部分卡 domain=null → 匹配崩被 except 吞 ③缓存 key 未含 search_dirs 跨域污染 | 修:null 容错(fm.get("domain") or [])+ 缓存 key 含目录集 + 字段名对照返回结构 |
| 2026-08-19 | 王语嫣 | queue_transition complete --force | --force 从 queued 直跳 pending_review 必败：锁内重检 L260 仍要求 status==claimed-<instance>，没考虑 force 路径（queued 合法）——报错文案"加锁期间发生变化"误导成竞争重试；历史上"queue_transition被拦+手动流转"同根因 | 临时绕行=claim --force + complete 两步（合规）；根治=修锁内重检（黄药师基建，建议随 #358/#359 批后排期） |
| 2026-08-19 | 黄药师 | #372 PARA 库处置（重大摩擦） | 我基于"英文库从未消化"旧报告+文件名统计，把 PARA 库（Handle the business 等 4 库 2128 文件 270M——实际是知识库核心内容，含一堂口述稿/已消化汇编）归类"垃圾候选"，处置建议给出"归档/删除"选项。用户拦停："你差点坏了大事，把最重要的核心删除掉了"。**未执行任何移动/删除（零损失）**，但建议方向完全错误 | 根因：未消化≠不重要（核心资产待消化 vs 垃圾）；抽查少量样本下结论（B5 牌违背）；处置建议默认姿态是"清理"而非"保守保留"。已修：处置建议文档重写（原位保留）+ #375 claim 处置门禁（缺"内容价值判断"节拒绝领取）+ 教训记入技能日志/Truman 复盘。PROTOCOL §7 从文案落地为工具 |
| 2026-08-19 | 黄药师 | #366 启动指针 v2 | b4d466ee0 提交 v2 指针 3 分钟内被 .kdo/capsule_sync.py（time-capsule.db 再生器）覆盖回 v1——欧阳锋终审 FAIL P0（#362 三问第 2 问"生效了吗"答否） | 静态约定文件与自动再生器冲突：任何"单文件真相源"交付前必须 grep 同路径生成器。已修 capsule_sync v2 兼容（保留头部仅再生角色段）+ 复审 PASS |
| 2026-08-19 | 黄药师 | #371 元数据扫描脚本 | ①_no_dup 构造器 node.value 是 (key,value) 元组——`k.value` 崩，files=0 假象两轮 ②heredoc `\n` 转义破坏 vault-snapshot 字符串（SyntaxError）③bash cut -c9-12 取到 "_202" 而非月份（135 单归档错位修两次） | 长脚本先 5 文件小样本验证再全量；mv 前 echo 验证目标路径；heredoc 复杂字符串用 Edit 工具而非 shell 拼接 |
2026-08-19 03:5x / 黄药师 / 排查 inbox 自动化为何不工作 / watch_inbox.py 挂 WSL cron，WSL 不常驻导致 cron 静默失效 2 天无人察觉 / 根因初判：全量 Windows 迁移只迁了前台服务，WSL 侧定时任务无健康监控，静默死亡无告警
| 2026-08-21 | 黄药师 | #399 claim | claim 传序号 "399" 报"任务不在队列"——queue_transition 的 task_id 参数是完整任务文件名，非序号（find_task 按 task_id 字段匹配） | CLI 用法与直觉不符：`claim <task-id>` 应写完整文件名。建议：main() 支持按 seq 前缀匹配（量小，低优先） |
| 2026-08-21 | 黄药师 | #401/#402 claim | 连续两单被 #375 处置门禁拦截（"盘点/试点"命中处置关键词族），各需补「内容价值判断」节才能领——门禁关键词族偏宽，盘点/试点类分析任务也被要求处置声明 | 门禁语义是"素材处置"，关键词族命中面比语义宽；补节成本低（合规声明），但后续可评估关键词族收窄（如仅"删除/清理/归档"族触发） |
| 2026-08-21 | 黄药师 | #401 JSON 输出 | rule-gate-inventory --json 因规则文本含不可见字符 → JSONDecodeError（两次修复） | 教训复现：涉及不可见字符的代码必须 ensure_ascii/转义写法+读回验证（08-20 U+FFFD 教训同族） |
| 2026-08-21 | 黄药师 | 提审命令 | bash cd 到 KDO 仓后 queue_transition 相对路径找不到脚本，提审命令报错 2 次（工作目录漂移） | queue_transition 应用绝对路径调用或脚本内 resolve 自身路径（脚本已有 __file__ resolve，问题是调用方 cwd）——记习惯：提审前 pwd 确认在 wiki 根 |
| 2026-08-22 | 黄药师 | #418 T2 双轨合并事故 | bash 中文路径下执行 mv/rmdir 链式命令：sales-dialogue-assistant/daily-context/2026-08-16.md 丢失（全盘+快照无恢复源）。bash 对中文目录的 ls 输出与文件系统实际不一致（MSYS2 编码问题）——rmdir 删除的可能是空目录，文件或从未在 bash 看到的路径上。根因初判：中文路径文件操作必须用 Python（os.rename/os.walk）不用 bash mv/ls；批量移动前先 Python 枚举核实 + 逐文件 mv | 
| 2026-08-22 | 黄药师 | #421 claim | claim 被 #375 处置门禁拦截（任务单含"处置"字样——测试建议书"由王语嫣裁定处置"） | 同 08-21 记录：关键词族命中面偏宽，补内容价值判断节即过；与 #412/#421 两次补节实证合并评估收窄 |
| 2026-08-22 | 黄药师 | #421 去重 | PROPOSAL-PENDING 段按文件名去重重写，误删同文件第二条历史裁定记录（orchestration-audit 双裁定） | 段重写不得按"文件名唯一"清理历史行——同文件可有多次独立裁定；只防新增，历史行全保留；已 git HEAD 恢复 |
| 2026-08-22 | 黄药师 | #421 计划任务 | schtasks 注册 kdo-conveyor-probe 被权限分类器拦截（常驻机制需用户确认） | 自动化持久化动作（计划任务/服务）默认需用户明确授权——执行前先问；待用户拍板后注册 |
| 2026-08-22 | 黄药师 | #422/#424 claim | #375 处置门禁关键词族第 4/5 次误拦（"归类/清理/白名单"命中）——每次补内容价值判断节即过 | 累计 5 次实证（08-21×2 + 08-22×3），关键词族命中面明显宽于"素材处置"语义；建议评估收窄（仅"删除/清理/归档"族触发），并进 F-033 同族讨论 |
| 2026-08-22 | 黄药师 | 停车场 F-034 登记 | 想登记"agent复盘 git 化"为 F-034，发现王语嫣已登记 F-034/035（编号到 F-035），改 F-036 | 写停车场前先 grep 当前最大编号；多角色并行维护的共享文件存在编号竞态 |
| 2026-08-22 | 黄药师 | 终端中文输出 | bash python -c 传中文长字符串：GBK 终端乱码 + 引号转义 SyntaxError | 中文内容写入一律 Write/Edit 工具或 heredoc，不用 python -c 内联长字符串 |
| 2026-08-23 | 黄药师 | #421 飞书通知假成功 | 签名算法与飞书官方不符（code 19021）+ _send_hook 只查 HTTP 200 未查业务码 → 全部消息假发送且消耗幂等配额，用户报告"群里没看到"才发现 | ①外部 API"成功"必须解析响应 body 业务码（飞书失败也返 200）②用户未确认收到=未验证（P-15 同族，昨天执行报告"用户确认收到"写法错误）③sign 类算法先查官方示例实测再上线 |
| 2026-08-23 | 黄药师 | 改已 resolved 建议书 | 用户指示"L1/L2/L3/待活体四态精确化"后，我直接 Edit 了已 resolved 的验证分层建议书——违反"已交文件不再回头改"协作纪律，被用户纠偏 | ①协作文件只增不改：后续内容另起新文件（日期+原因+叙述）②resolved/已交文件=冻结 ③改文件前先想"这文件别人可能也在读/已处理" |
| 2026-08-23 | 黄药师 | #444 测试隔离首版失效 | 改 qt.QUEUE_PATH 属性隔离失败——parse_queue 默认参数在 queue_gate 模块定义时绑定，改属性不影响 | 测试隔离三选：①环境变量+模块重载 ②函数级 monkeypatch（qt.parse_queue=构造 rows，正解）③mock find_task；改模块属性=无效（默认参数绑定坑） |
| 2026-08-23 | 黄药师 | #460 插桩声称 5 处实际 4 处 | python str.replace 静默失败（处置硬门禁插桩模式不匹配没报错）——执行报告声称 5 处，欧阳锋 grep 实测 4 处，FAIL 退回 | 批量改代码后必须 grep 计数验证（grep -c 调用点）；"声称"必须落盘验证（P-15 同族，今天第二次：飞书假成功+插桩缺失） |
| 2026-08-23 | 黄药师 | 占位节替换 3 次失败 | python replace "（生产者填写）\n\n" 猜换行数不匹配（实际单个 \n）——complete 被五字段门禁拦 3 次 | 占位节直接用 Edit 工具删（精确文本），不用 python 猜换行 |
| 2026-08-23 | 黄药师 | 测试污染全量跑失败 | #461 全量跑失败——旧测试（TestReviewBoardBatchReregister）改 queue_transition.QUEUE_PATH 不恢复，污染后续测试 | 测试 patch 模块属性必须 try/finally 恢复；函数级 mock（patch 函数）优于改属性 |
| 2026-08-23 | 黄药师 | #444 隔离首版失效 | 改 qt.QUEUE_PATH 属性无效——parse_queue 默认参数在 queue_gate 模块定义时绑定 | 测试隔离三选：函数级 monkeypatch / 显式传 rows / 环境变量+模块重载；改模块属性=无效 |
| 2026-08-23 | 黄药师 | heredoc 转义吞反斜杠 | bash heredoc 处理 \n 层级混乱，python 源码字符串被破坏（SyntaxError/字面化） | 中文/转义敏感内容一律 Write/Edit 工具，不用 heredoc/python -c 内联 |
| 2026-08-23 | 黄药师 | 飞书假成功（签名错误） | _feishu_sign 算法与官方不符（code 19021）+ _send_hook 只查 HTTP 200——全部消息假发送且消耗幂等配额，用户报告"群里没看到"才发现 | 外部 API 成功必须验响应 body 业务码；用户未确认收到=未验证 |
| 2026-08-24 | 黄药师 | #488 队列行错位到 PROPOSAL 段后 | 新任务行被加在主表外（PROPOSAL-PENDING 段之后 L263），parse_queue 只解析第一个表→complete 报"不在队列中"，手动移行回主表修复 | 队列新任务行必须加在主表区（REVIEW-PENDING-BEGIN 之前）；parse_queue 只认第一个表是设计（后续表=标记段） |
| 2026-08-24 | 黄药师 | #488 补丁直接提交未入队 | 用户质询后补"登记纪律 lint 拦截"直接改总表+infra-status+commit，未走任务制入队（上板冻结纪律/E019 同族）——用户裁定"特例，下不为例" | 基建补丁也必须先入队再交付；特例后一律任务制（用户 08-24 拍板） |
| 2026-08-24 | 黄药师 | #491 任务书执行期间收紧未重读 | 任务书任务2从"可分期"收紧为硬性（老朱指令+风清扬建议），我提审时只交付旧范围（去镜像/去重/归档），漏硬性项（日增量结构）——补做+执行报告追加后才闭环 | 领任务时记下任务书 updated_at/版本；执行中途若任务书被改（编排/拍板收紧），重读最新态再继续；提审前对照任务书全任务逐项核 |
| 2026-08-24 | 黄药师 | 占位节残留致 complete 五字段拦截 ×3 | 任务书模板含"## 执行报告（F-034…）\n（黄药师填写）"占位节，append 新报告后门禁提取到旧占位空节→缺字段拦截（#489/#491/#492 连续三次） | 写执行报告必须替换占位节（Edit 旧节→新报告），不 append；或门禁 _extract_exec_report 改取最后节 |
| 2026-08-25 | 老顽童 | 失忆锚点 §4 状态误标 | 锚点写 #470/#498 "→ reviewed"，队列实测均 queued（未闭环返工单）——锚点快照滞后/误记第 N 次同族 | 锚点只作线索不作真相；涉及任务状态一律 queue_transition.py status 实测后再断言 |
| 2026-08-25 | 黄药师 | #508 归档幂等分支删未验证内容（事故） | _archive_old_days 旧实现"zip 存在即 rmtree 目录"——存量迁移把平铺树（含 zip 未覆盖的 474 增量文件）移入 2026-08-24/ 后被幂等分支直接删除；473 从源恢复，1 文件真丢失（hermes/wangyuyan/.skills_prompt_snapshot.json） | 删除类操作先核验内容被覆盖再执行（_zip_covers_dir 门禁化：rel 集+大小逐文件比对）；幂等≠安全，"已处理过"的判断必须基于内容核验不是路径存在；批量移动/删除前枚举核实+before/after（E022 同族第 N 次） |
| 2026-08-26 | 老顽童 | 时钟扫描漏报 #531 终审落点 | myqueue 只读快照不覆盖 pending_review→reviewed 事件，连续数拍报"无可领"被老朱抓包；初判为个人 prompt 缺陷就地修，未上浮基建层（通知机制缺"结果触发"事件） | 局部修复代替系统上报（E017 同族：吸收停在字面）；监控类"没有新任务"≠"没有状态变化"；已写建议书 diag_20260826_laowantong-review-landed-notification-gap |
| 2026-08-26 | 黄药师 | 时钟巡检漏检 #528（队列里躺两天未发现） | 巡检用 grep 序号模式（盯预期中的单号）而非全表视图——按预期扫描反模式 | 角色时钟巡检必须走 myqueue 全表视图（#472 现成机制我没接上）；禁止 grep 序号模式当扫描器 |
| 2026-08-27 00:3x | huangyaoshi | #543 complete 提审 | E040 拦：交付物节写省略路径（tests/xxx、kdo/xxx）被判 untracked——门禁读执行报告交付物节而非 frontmatter code_files，路径必须全称（跨仓带 Knowledge Delivery OS 前缀） | 门禁启发式路径提取与书写习惯不匹配；写交付物节时每个路径都写全 |
| 2026-08-27 | 老顽童 | #551 complete 三连拦 | ①pre-submit ALIASES 检查读搜索索引——新卡未入索引时 aliases 写得再对也必 FAIL，须先 `kdo index --incremental`；且索引后警告仍残留（在库卡 bridge-lightning 同款），误报 ②F-034 五字段锚点=闭合粗体精确匹配，`**改动文件清单**` 不含 `**改动文件**`（闭合 `**` 被后缀阻断）③E040 交付物节边界=`\n**` 行首，字段行带 `- ` 前缀则节延展吞掉后续验证命令行，反引号命令被判成未入仓交付物 | 门禁锚点与书写习惯三层不匹配；机械门禁的"想当然格式"没有文档化；已落最小建议书 diag_20260827_laowantong-gate-anchor-format-pitfalls |
| 2026-08-27 02:36 | huangyaoshi | #546 complete 提审 | E040 再拦：gitignore 的运行时文件（.kdo/active-instances.json）写进交付物节被判 untracked——交付物节只放 git 可核验路径，运行时状态挪节外说明 | 同族第二次（#543 省略路径→本次 gitignore 路径），规则吃透：交付物节=纯 git 可跟踪清单 |
| 2026-08-27 | 老顽童 | #557 收尾 commit 误扫他方改动 | `git add -A 30_wiki` 扫入 6 个他方未提交改动（含 zhu-time-os.md 未提交审查记录）——前 16 批都枚举显式路径，最后一批图省事破功；且批次报告写"教训已记 friction-log"实际没记（自己踩穿 A1：声称-落地差集） | 批次 commit 永远枚举显式路径禁 -A；friction-log「已记」类措辞写前先 grep 验证落盘 |
| 2026-08-27 | 老顽童 | #557 批次报告数字转抄失真 | 报告表写 refs_line_anchor 728（转抄自收尾清理前的中间扫描），终态 771——被欧阳锋对账抓出 🟡 | 报告数字一律取终态扫描值，转抄中间态=失真源；交付前最后一次测量的值才进报告（L5 同族） |
| 2026-09-01 | 黄药师 | #588 claim 被拦 | 老朱直令派活撞上 #504「审查等待期不接新单」——#590 pending_review 占位阻塞 claim，机制无法区分「自主接单」和「老板直令」；走 --force 留痕绕过 | #504 缺「老朱直令豁免」通道（候选：任务单加 directive:true 字段跳过等待期检查，同 batch:true 模式） |
| 2026-09-01 15:05 | 黄药师 | #593 执行报告提审 | E040 拦截：交付物清单写缩写路径 `shared/deep-debug/manifest.yaml`，门禁按仓根解析不到判未入仓 | 初判：清单书写规范缺口——门禁按仓根解析相对路径，交付物清单必须全路径，已改全路径一次过 |
| 2026-09-01 14:35 | 黄药师 | #593 真机冒烟 | `hermes --profile skills-assistant` 报 profile 不存在——config+SOUL 落在 `.hermes/profiles/` 旧树，现行数据根=AppData/Local/hermes/profiles/；sync/check 脚本常量同源漂移（巡检报 [MISS] windows/wangyuyan 而其在跑） | 初判：0.20 迁移后脚本常量未跟进，本单双树对齐保可用，根治需另立项 |
