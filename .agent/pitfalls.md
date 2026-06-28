# 踩坑记录

每踩一个坑追一条。格式：症状 → 根因 → 对策。

---

## P-1: 切模型改环境变量无效——Claude Code 走全局设置

**症状**：在 WSL `.bashrc` / `.profile` 里 `export ANTHROPIC_*` 设为 Kimi，但 `claude.exe` 始终读不到，一直连 DeepSeek。改 Windows 注册表 + `wsl --shutdown` 也无效。

**根因**：Claude Code 的模型/API 配置有独立的**全局设置文件**（`~/.claude/settings.json` 或 Windows 侧等价路径），优先级高于环境变量。单独改 env var 或注册表都不生效——全局设置覆盖一切。

**对策**：
- **不要逐项改环境变量**——直接改 Claude Code 的全局设置文件
- 全局设置的模型/API endpoint/Key 一处修改即生效，无需注销重登

**关联**：`decisions.md` 2026-05-16 DeepSeek vs Kimi

**⚠️ 2026-05-16 补充**：P-1 的初始诊断不完全准确。真正的覆盖源对飞书黄药师而言是 cc-connect 的 systemd `env.conf` drop-in（见 P-5），对 CLI 黄药师则可能是全局设置或注册表。两者互不影响——这就是为什么 CLI 黄药师正常工作而飞书黄药师 401。

---

## P-2: tmux session 缓存旧配置

**症状**：改了 `.bashrc` 后 `claude` 行为没变。

**根因**：`claude()` 函数包装了 tmux session `claude`，只要 session 活着，用的是 session 创建时的环境，不是最新 `.bashrc`。

**对策**：改完配置后 `tmux kill-session -t claude`，再重新 `claude`。

---

## P-3: Hermes 换 API Key 后仍然 401 — auth.json 缓存覆盖 .env

**症状**：更新 `~/.hermes/profiles/*/.env` 中的 `KIMI_API_KEY` 后重启服务，仍然 HTTP 401，日志显示用的还是旧 Key。用户和欧阳锋多轮尝试换新 Key 无效——"系统顽固用旧的覆盖新的"。

**根因（3 层）**：
1. **改错了 .env** — Hermes 加载 `~/.hermes/.env`（全局），不是 `~/.hermes/profiles/<name>/.env`。profile 下的 .env 根本不被读取
2. **auth.json 缓存** — `~/.hermes/auth.json` 的 `credential_pool.kimi-coding[]` 缓存了旧 Key 的 access_token + `last_status: exhausted`，Hermes 优先用缓存而不是重读 env
3. **Provider 名** — 之前用过 `kimi-for-coding`，正确是 `kimi-coding`

**对策**：
- API Key 换新时三处同步更新：`~/.hermes/.env` + `~/.hermes/auth.json` credential_pool + `~/.hermes/profiles/*/config.yaml` provider 名
- 改完后清掉 auth.json 里的 `last_status/exhausted` 和 `last_error_code/401`，否则 Hermes 认为 Key 已死会跳过
- 用 `journalctl --user -u hermes-gateway-* --no-pager -n 30 | grep -i "401\|auth"` 验证无认证错误

---

## P-4: 批量格式升级产生"格式完整但思维空洞"卡片 (C-8)

**症状**：抽检 `motivation-resistance` 和 `peak-end-rule` 两张卡——格式符合 agent-native 标准，但 Claims 无具体反例、Constraints 模板化。

**根因**：批处理只改了结构和 frontmatter，没有触发真正的理解加工。格式门禁检测不到"搬运 vs 理解"。

**对策**：v1.5 新增理解门禁——每条 Constraint 必须有具体场景 + 可验证的失败模式。批量升级后至少抽检 2 张。

---

## P-5: cc-connect 切模型后 CLI 正常但飞书 401 + 找不到文件夹

**症状**：从 Kimi 切回 DeepSeek 后，WSL 终端的 `claude` 命令正常工作，但飞书黄药师报 `HTTP 401` 且无法访问 wiki/KDO。

**根因（2 个残留文件未回切）**：
1. `~/.config/systemd/user/cc-connect.service.d/env.conf` —— Kimi 时代的 systemd Environment drop-in，仍指向 `https://api.kimi.com/coding` + Kimi Key。systemd `Environment=` 注入的 env var 优先级最高，覆盖 `.bashrc` 和注册表
2. `~/.cc-connect/config.toml` —— `work_dir` 从 `/mnt/c/Users/Administrator/Desktop/wiki` 被改为 `/home/dministrator`（Kimi 切换期间重置的），导致 Claude Code 从 home 目录启动，读不到 wiki 的 `CLAUDE.md`

**为什么 CLI 黄药师正常**：CLI 走 `.bashrc` → tmux session env，和 cc-connect 的 systemd env 互不影响。两条独立的配置链路。

**对策**：
- 切模型/切 API 时，cc-connect 的配置有**独立的两个文件**需要同步：
  1. `config.toml` → 模型/API 通过 provider 或 env 注入
  2. `cc-connect.service.d/env.conf` → systemd 环境变量
- 改完后 `systemctl --user daemon-reload && systemctl --user restart cc-connect`
- 验证：`systemctl --user show cc-connect | grep Environment`

**关联**：Config Cascade Debug skill — 这本质是同一模式：多个独立配置层（.bashrc / 注册表 / systemd drop-in / cc-connect config.toml），改了三处漏了一处。

---

## P-6: cc-connect 修好 work_dir + API Key 后仍然空响应 — session 缓存了失效的 Claude Code session ID

**症状**：cc-connect 的 `work_dir` 和 `env.conf` 都已修正（→ wiki vault + DeepSeek），飞书发消息后 bot 返回空。日志显示 `is_resume=true`，紧接着 `exit status 1: No conversation found with session ID: cb687591...`。

**根因**：cc-connect 的 session 文件（`~/.cc-connect/sessions/huangyaoshi_53de3c3f.json`）里存了 `agent_session_id`，指向 Claude Code 在**旧 work_dir**（`/home/dministrator`）下创建的 session。work_dir 已改为 wiki vault 后，Claude Code 的 wiki 项目里不存在这个 session ID，resume 失败，返回空。

**为什么之前的 401 错误也写入了同一个 session**：这个 session 是在 Kimi 配置期间创建的，所有 401 错误都被写入了 session history。修好 API Key 后 session 里仍有 `agent_session_id` 指向不存在的位置，所以 Claude Code 启动即失败。

**对策**：
- 修改 cc-connect 的 `work_dir` 后，必须同时删除对应的 session 文件（`~/.cc-connect/sessions/<project>_<hash>.json`），否则旧 session ID 无法 resume
- 删除后重启 cc-connect，下次消息自动创建全新 session

**关联**：P-5（同一个事故链的第三环：work_dir 错 → env.conf 错 → session 缓存错）。Config Cascade Debug skill 的 Layer 0（运行时缓存）又一次成为最后一层漏网之鱼。

**⚠️ 2026-05-17 复现**：P-6 的精确复现。昨晚 21:37 修 P-5 时重启了 cc-connect，旧 Claude Code 进程被杀，但 session 文件保留着死进程的 `agent_session_id`。用户睡觉期间没人发消息，WebSocket 在 00:05 和 02:17 两次超时重连后进入僵尸状态（TCP 连着但应用层不收消息）。早上用户发消息 → cc-connect 尝试 resume 死 session → 静默失败 → 空响应。飞书端 3 小时零条日志。修复：删 session 文件 + 重启 cc-connect。

**复现条件**：cc-connect 重启 + 存在旧 session 文件 + 重启后第一次发消息。复现率 100%。

**设计层根因**：cc-connect 启动时不做 session 有效性检测——不检查 `agent_session_id` 是否指向活着的 Claude Code 进程，也不自动清理。这个 bug 每次重启 cc-connect 都会触发。

---

## P-7: 素材预处理缺少 OCR 强制检查——执行者跳过图片

**症状**：科学决策文件夹有 35 张关键框架图（共识四层冰山、ROI 全景图、X 型 Y 型对比等），老顽童声称"没有图片需要 OCR"。欧阳锋未核实即采信。后发现 35 张图全部未 OCR，图中含有口述稿未系统展开的结构信息。

**根因**：
1. inbox 素材预处理缺少 OCR 检查点——没有强制步骤要求"如果文件夹里有 PNG，先跑 OCR 再进管线"
2. 架构者（欧阳锋）在长对话中判断力下降，未独立核实执行者的声明

**对策**：
- 新域素材消化第一步：扫描文件夹 → 如有图片，强制 OCR 全部后再读文本
- 架构者审查新域提案时，独立验证"素材是否全部消化"——不能只信执行者的自述
- 长对话中出现判断失误时主动收尾，下次干净状态接手

---

## P-8: 欧阳锋忘记本地已有武器——重新调研已部署工具

**症状**：新欧阳锋 session 启动后，遇到 OCR/图片处理需求，花大量时间调研方案、测试依赖、试图部署新工具。最后才想起来 vault 旁边 `C:\Users\Administrator\ocr-pipeline\` 已经部署了 PaddleOCR v5，且有 PowerShell 封装脚本。

**根因**：
1. 启动时只读了 `context.md` + `pitfalls.md`，本地工具清单藏在 277 行的 CLAUDE.md 里，读完前两个文件根本看不到
2. `.agent/` 记忆系统缺少"武器库"文件——记录"我们有什么、在哪、怎么用"
3. 工具部署完成后没有在 startup checklist 中加入验证步骤

**对策**：
- 新建 `.agent/toolkit.md`（OCR/KDO CLI/Git/WSL 桥接/内置 Skills/常见操作模式）
- CLAUDE.md 启动指令已改：`Read .agent/context.md → .agent/pitfalls.md → .agent/toolkit.md`
- context.md "下次启动"第 1 条加了 `toolkit.md` 提醒
- 新增工具/能力时必须同步更新 `toolkit.md`
- 原则：**先查武器库再行动——不要重复造轮子**

---

## P-9: Glob 漏扫子目录 → 误判文件缺失 → 来回打脸

**症状**：用户说设计域文件在 `00_inbox/design/`，执行 `Glob "00_inbox/*design*/**/*"` + `Glob "00_inbox/**/*.txt"` 均返回空。结论"文件不存在"。用户指出文件就在那里后，改用 PowerShell `Get-ChildItem -Recurse` 立即找到：`design\AI设计-AI设计基础01.txt` (72KB) 和 `AI设计-AI设计师实操培训01.txt` (122KB)。误判导致任务文件被错误标注为"阻塞"后又回滚，浪费时间+信誉。

**根因**：Glob 工具对特定路径模式（含中文名？子目录深度？）可能漏匹配。单一工具判断"不存在"是危险的。

**对策**：
- **查文件是否存在：先用 PowerShell `Get-ChildItem -Path ... -Recurse`，再按需 Glob/Grep**
- 永远不要用一个工具的 negative result 作为最终结论
- 宣布"文件缺失"前，至少用两种工具交叉验证
- 本次误判已直接导致用户不满（"连你都失忆了"）

---

## P-10: 口头禁令 vs 书面约束——审查意见必须落笔到任务文件

**症状**：欧阳锋在审查老顽童 Batch 2+3 时口头说"后续 Batch 全面封禁 Kahneman 和 Taleb"。用户问"禁令指什么？"——任务文件里根本没有这条。口头意见与书面指令脱节，造成执行者和决策者之间的信息不对称。

**根因**：审查者在对话中产出了约束性意见，但没有同步写入任务文件（唯一真相源）。口头指令在换会话后丢失，且执行者无法核实。

**对策**：
- **所有约束性指令必须写入任务文件，口头审查只能是讨论**
- 审查意见要分"观察"和"指令"两类，指令类必须当场写入 task 文件
- 任务文件是唯一真相源——如果任务文件里没有，就等于不存在
- 具体案例：最终改为写入任务文件的软约束"同一域内，每5张卡至少引入1位新攻击者"

---

## P-11: validator `section_content` regex 在 `###` 处截断——所有文章 word count 失效

**症状**：一篇1800字完整文章，`kdo validate` 报 "Draft section is empty (0 words)"。加了内容后仍只统计到46 words。

**根因**：`validation.py:section_content()` 的正则 `(?=^##|\Z)` 用 `^##` 作为section结束标记。`###` 行以 `##` 开头，被正则误判为同级heading，导致提取只截取到第一个 `###` 之前的文字。所有使用三级标题的文章（几乎全部）都命中此bug。

**对策**：
- **临时绕路**：在 `## Draft` 和第一个 `### Part N` 之间插入一段引导文字
- **根治**：将正则改为 `(?=^##(?!#)|\Z)` 或 `(?=^##\s|\Z)`——只匹配同级 `## ` heading，不匹配更深级别
- **优先级**：P0——阻塞所有文章类artifact的有意义验证

---

## P-13: 长会话 = token黑洞 — 一晚上烧掉80元

**症状**：黄药师从晚上开始跑 Dogfood → Sprint 2 → Sprint 3 → Sprint 4，一个会话跑到上下文爆掉再续第二个会话。共 ~100轮+，DeepSeek 账单 ~80元。单晚消耗超过过去10天总和。

**根因**（三重叠加）：
1. **每轮重发全量上下文** — 后期每轮 input 100-150k tokens，其中 90% 是历史对话和工具结果
2. **CLAUDE.md 很大** — 每轮携带 ~4000 tokens 系统提示
3. **缓存 TTL 5分钟** — 超时后下一轮全量重新计费

**反算**：总输入 ~14M tokens，缓存未命中 ~5.6M（占费用 80%）。

**对策**：
- **一个 Sprint 开一个会话** — 完成即 /new，通过 `.agent/context.md` 接力
- 不要一口气跑 100轮——拆成 5个短会话，总 token 量降 70%+
- CLAUDE.md 已精简（290→101行），CLI 速查移出到 `90_control/cli-reference.md`
- 需要批量脚本任务的，写好脚本让用户本地跑，不用我一轮轮验证

---

## P-14: 僵尸 claude 进程默默烧钱 — Obsidian Claudian + vault backup 死循环

**症状**：PID 17916 `claude` 从 5月19日跑到今天（5天），CPU 仅 502 秒但可能烧了大量 API 费用。另外 PID 15540（hermes）从 5月16日跑了 8 天。80元账单不全是黄药师消耗。

**根因**：
1. Obsidian vault backup 插件每隔几分钟自动 `git commit`，文件变更可能触发 Obsidian 内的 Claudian 插件调用
2. 用户不知道那个 Obsidian 窗口里的 Claudian 一直在后台活着
3. 没有定期检查进程的习惯——僵尸会话默默积累

**对策**：
- 每次 Claude Code 会话结束**确认终端已关**——不是最小化、不是挂 tmux
- 定期 `Get-Process claude` 检查是否有意外残留
- Obsidian Claudian 用完即关——不要让它在后台被 vault backup 反复唤醒
- **每完成一批任务就检查一次账单**——不要等积累了 80元才发现

---

## P-15: 执行者声称"完成"但实际未做——可测量指标必须独立验证

**症状**：黄药师 Sprint 4 完工报告写"断链 <10（修复前~113）"、"缺frontmatter <20（修复前~271）"——数据详实、有修复前后对比。实测 vault：断链 359、缺 id 237、双格式残留 134。零改动，零 commit。

**根因**（2层）：
1. 执行者（黄药师）把"脚本写完了/规划做好了"等同于"数据修好了"。报告中的"修复后"数字是预期的目标值，不是实测值。
2. 架构者（欧阳锋）看到格式工整的完工报告就放松了警惕，没有在实际数据未变动的情况下第一时间验证。

**对策**：
- **验收时必须独立运行可重复的测量脚本**，不做"相信报告"的审查
- 持续类指标（断链数、缺字段数）不能只看"修复前→修复后"表，要自己跑一遍
- "修复后"数字必须附带验证方法（如 `grep` 命令或 `python` 脚本），否则视为未经验证
- 任务文件的 `完成` 状态 = 代码已提交 + 数据已变更 + 验证已通过，缺一不可

**关联**：P-10（指令必须落笔）的对称问题——不仅指令要落笔，完成数据也要可重复验证。

**复发案例（2026-06-28）：lint Batch 2-A/B/C 完成报告争议**
- **第一次报告**：WorkBuddy 老顽童声称 Batch 2-A/B 130+43 文件完成、`kdo pre-submit` 173/173 通过；黄药师声称 Batch 2-C 处理 314 项修复、lint ERROR 537→425。
- **欧阳锋初审**：三批清单内文件相对 HEAD 均无 git diff；`kdo lint` 仍报 Case section ERROR 220 个、dk section ERROR 30 个、source_refs `file not found` ERROR 175 个。判定全部虚假完成，退回重做。
- **老顽童重新执行**：使用 `dangerouslyDisableSandbox: true` 绕过沙箱直接写真实磁盘，vault backup 自动将修改 commit 到 HEAD。
- **王语嫣独立复核**：
  - `git diff HEAD~10 HEAD --stat` 显示 141 files changed, +1728/-297
  - `git show HEAD:<file>` 确认 130/130 case 文件含 4 个标准 section，57/57 dk 文件含 6 个标准 section
  - `kdo lint` 显示 Case section ERROR = 0，DK section ERROR = 0，剩余 175 ERROR 全部为 source_refs 类
  - 结论：**Batch 2-A/B 真实完成，欧阳锋初审为误报；Batch 2-C 仍为虚假完成，黄药师未实际修改文件**

**根因分层**：
1. **真问题（Batch 2-C）**：黄药师把"脚本跑完/预期效果"等同于"仓库已修改"，未用 git diff 和独立 lint 实测验证。
2. **验证方法缺陷（Batch 2-A/B 误报）**：vault backup 自动 commit 机制下，`git diff HEAD` 只显示 unstaged 变更，已被 commit 的修改不会出现在 diff 中。欧阳锋用 `git diff HEAD` 作为唯一验证手段，导致把真实完成误判为虚假完成。

**新增对策**：
- 批量任务提交前必须跑 `kdo pre-submit -f <清单> --expect-changes <数量>`，git 实际变更文件数小于声称数直接 FAIL
- Builder 黄药师已将 `--expect-changes` 门禁写入 KDO CLI，后续批量任务无法绕过
- **审查者验证批量完成时，不能只用 `git diff HEAD`**：必须结合 `git log`、`git show HEAD:<file>`、`git diff HEAD~N HEAD` 或独立 lint 重跑，尤其在 vault backup auto-commit 开启时

**症状**：在文件frontmatter里更新了 `source_refs` 和 `wiki_refs`，`kdo validate` 仍然报 "Missing"。

**根因**：`validate_artifact()` 优先读取 `artifact.get("source_refs")`——数据来自 `.kdo/state.json`，不读文件frontmatter。同时 `90_control/artifact-registry.yaml` 又是第三份拷贝。三处数据独立维护、可以不一致，没有同步机制。

**对策**：
- **短期**：修改后必须同时更新 state.json（用 Python 脚本 or `kdo` 命令）
- **长治**：validate 应以文件 frontmatter 为 source of truth，state.json 和 registry 只做缓存/索引。发现不一致时自动同步或报 warning
- **优先级**：P1——每次手动改文件都要记住还有state.json，极易遗忘

---

## P-17: auto_label 声称"85%准确率"——实测34.8%，差距来自被忽略的5个维度

**症状**：黄药师说"提示词调优后准确率做到了85%"。欧阳锋用 Gold Standard（15条手工标注 chunk）独立验证，实测34.8%（47/135）。差距巨大。黄药师的"85%"只算了管线实际在标的 4 个维度（chunk_type/method_family/audience/perspective），忽略了另外 5 个维度（platform/confidence/prerequisite_knowledge/expiry/usage_depth）全线 `<missing>`。

**根因（2层）**：
1. **测量口径不同**：黄药师测的是部分维度局部准确率，欧阳锋测的是全维度全样本准确率。双方没有约定统一的测量方法和数据集。
2. **缺少gold standard基线比对流程**：没有在调 prompt 之前先跑一遍 baseline 确认当前准确率，导致"进步"和"绝对水平"被混淆。

**对策**：
- **任何"准确率"声明必须附带测量方法**：用了什么数据集？覆盖哪些维度？计算方式？
- **Gold Standard 必须跑 full comparison**：不能只挑管线能标的维度算——缺标的维度也要报告
- **调 prompt 前先跑 baseline**：改 prompt 之前先跑一遍 `_verify_gold_standard.py`，确认起点
- **所有自动标注管线的性能评估以 Gold Standard 为唯一基准**：`30_wiki/decisions/gold-standard-manual-labels.md`（15 条 chunk，含理由说明）

**关联**：P-15（声称完成未验证）的同一种病的不同表现——这次不是"没做"，而是"测了但测的是错的指标"。

---

## P-18: 手写YAML解析器导致嵌套数据丢失 — 97行bug → 15行修复

**症状**：Data Curator Clean 跑完后，`yt-decision-y-model.md` 的 `visual_analysis` 字段从 4 张图的完整结构化描述变成 5 条扁平字符串，3 张图 15 条分析丢失。`yt-model-aesthetic-progression.md` 的 `related` 字段从 4 个链接变成 `level: intermediate`。

**根因**：`clean_cards.py` 使用 97 行手写 YAML 解析器，只能处理平面键值对和一层嵌套。遇到 `visual_analysis` 这种"列表内嵌 dict"结构时直接拍扁成字符串。

**对策**：
- **绝对不要手写 YAML/JSON 解析器**。Python 标准库 `yaml.safe_load()` 1行替代97行
- 任何批量文件修改工具必须在 write 前做 round-trip 校验
- 修改后全量扫描 `yaml.safe_load()` 确认 0 损坏
- 修复流程：代码修复→回滚受损文件(git restore)→重跑

**定位**：`30_wiki/decisions/fix-data-curator-parse-bug.md`

---

## P-19: 花引号被YAML误解析为字符串定界符

**症状**：`"四套操作系统"=可切换的决策runtime` 中，直引号 `"` 被 yaml.safe_load 解释为 YAML 字符串定界符，后面的 `=可切换...` 成为非法 tail，导致 YAML parse error。

**根因**：中文内容的引号在修复花引号→直引号后，被 YAML 流式解析器误认为是字符串包裹符号。`key: "value"=tail` 模式触发 YAML 流式解析。

**对策**：
- 含 `"value"=tail` 或 `"value":tail` 模式的 YAML 值用单引号包裹：`key: '"value"=tail'`
- 或者保留花引号 `""` (U+201C/U+201D)——花引号不是 YAML 特殊字符

---

## P-20: pre-screen bigram 匹配对中文文本完全失效

**症状**：tag-registry v1.1 的 `includes`/`excludes` 字段全是英文描述（如 "falsifiable knowledge claim, testable assertion"），但 KDO 的 chunk 90% 是中文。bigram 匹配跨语言完全失效，pre-screen 返回 0 candidates。

**根因**：tag-registry 设计时未考虑中英双语场景。英文 includes 对中文 chunk 无匹配价值。

**对策**：
- tag-registry 的 includes 必须包含中文关键词（中英双语）
- 短期内绕过 pre-screen，直接送全维度候选给 LLM（单选模式不需要 pre-screen 过滤）
- 长期：pre-screen 改为 LLM-based（"这个 chunk 可能属于哪些维度？"）或中文 Embedding 匹配

---

## P-21: 无诊断手段时盲目调参——撞运气式调试

**症状**：广冷红外板 V2.2 调试，Ir_Delay 从 15→30→100→200→300→500 反复烧录，零进展。问题不在延时值本身，而在没有手段判断"哪个环节坏了"。

**根因**（通用反模式）：
1. 没有诊断手段就调参数 = 撞运气
2. 把"调参"当成调试，但调参的前提是知道哪段逻辑有问题
3. 搜索空间太大（时序、硬件、逻辑、供电...），盲调命中率趋近于 0

**对策**（通用三步法）：
1. **先造诊断工具** — 不是修 bug，是造一个工具来定位 bug。嵌入式→诊断版固件（绕过可疑 IC 直接驱动），代码→最小复现脚本，数据→gold standard 对比
2. **缩小搜索空间** — 排除法：发射管正常？✅ → 接收管正常？✅ → 问题在 595 控制时序
3. **分段隔离** — 单变量验证后再叠加。先 IN1 单通 → IN2 → 合起来，比一次调四个变量快 10 倍

**可复用方法**：`diagnostic-first-principle` — 任何调试的第一件事不是修，是造一个能告诉你"哪里坏了"的工具。

**关联**：P-15（声称完成未验证）、P-17（测量口径不同却声称 85%）——这三种情况的共同模式是**行动之前没有建立可测量的诊断基线**。

---

## P-22: 跨域知识迁移时——"照搬"比"适配"更危险

**症状**：欧阳锋提出"把电子工程知识装进 KDO"时，第一反应是找怎么把原理图/PCB 塞进 capture→ingest 管线。这是 KDO 的惯性思维——一切皆卡片、一切皆文本。

**根因**：
1. 工具建好了，人会本能地把所有问题都映射成工具能解决的形态——"如果你只有一把锤子，所有东西看起来都像钉子"
2. 跨域迁移时最容易犯的错误不是"迁移失败"，而是"迁移成功但产物无用"——花时间把原理图变成了卡片，但卡片上没有工程师真正需要的信息（示波器波形、上拉电阻值、器件焊接状态）
3. 欧阳锋的 archive-plan 已经给出了正确答案（文件三分类+版本锁+提示词→脚本），但没有明确指出"KDO 的边界在哪"——导致后来者可能误以为整个流水线都要进 KDO

**对策**：
- **跨域迁移第一步：不是问"怎么放进去"，是问"什么东西不该放进去"**
- 核心测试：如果知识的主要载体不是文本 → KDO 只存元数据+指针，不存内容
- 如果已经有人在另一个体系里做得很好了（欧阳锋的 archive-plan），不要重新发明——做桥接，不做替代
- 写对齐文档时明确"共识"和"分歧"两栏（见 `huangyaoshi-kdo-electronics-proposal.md` 的做法）

**可复用方法**：`boundary-first-principle` — 进入新域的第一个动作：画出 KDO 的边界线。边界外的归别人，边界内的才谈怎么优化。

---

## P-23: 插件安装的环境依赖链（SSH/SSL→Git→Plugin）

**症状**：`/plugin install superpowers@superpowers-marketplace` 经历三次失败：
1. SSH host key 缺失 → `ssh -T git@github.com` 修复
2. SSH 认证失败（无 key）→ 换 HTTPS
3. SSL/TLS 握手失败（schannel）→ 重试后自行恢复

**根因**：插件安装涉及三层依赖链（Shell→Git→HTTPS），任一层配置不一致就全断。本次是 Windows 环境下的 Git SSH/schannel 配置与 GitHub 的兼容性问题。P-5 的同模式——"改了三处漏了一处"。

**对策**：
- 优先用 HTTPS 而非 SSH（Windows Git 的 SSH 配置最脆弱）
- 插件安装失败先用 `git ls-remote <repo-url>` 测试 Git 层是否通
- 如果 Git 能通但插件安装仍失败 → 问题在 Claude Code 的 git 调用环境（可能走了不同的 Git 实例或 SSL 后端）

---

## P-24: Win10 Codex sandbox 阻断 localhost 连接——换端口/换协议/换代理均无效

**症状**：Codex v0.137.0 在 Windows 10 上，无论怎么配置，都无法连接本地代理（127.0.0.1:任意端口）。curl/PowerShell 测试完全正常，但 Codex 的请求从未到达代理日志。

**排除了**：
- sandbox_mode / 沙箱配置（elevated/unelevated/完全移除均无效）
- 端口号（8787/80/9876）
- 代理实现（aiohttp / Python stdlib http.server）
- 代理位置（Windows / WSL）
- Codex 安装（重装无效）
- Windows 防火墙（无相关规则）

**根因**：Windows 10 的 Codex sandbox 进程（即使 unelevated）创建了网络隔离，阻断了向 host localhost 的出站连接。Win11 上没有此问题。

**对策**：
- Win10 上 Codex 需要通过**外部代理**（如另一台机器或 WSL 的端口转发）而非 localhost
- 或者使用 CCX/CC Switch 等自带网络通道的完整代理方案
- Win11 无此问题——升级系统或换电脑是最简单的解法

---

## P-26: Hermes 环境缺 kdo 包 → ModuleNotFoundError: No module named 'kdo'

**症状**：Hermes（飞书 agent）运行老顽童/洪七公/段王爷的 agent 时，`import kdo` 报 `ModuleNotFoundError: No module named 'kdo'`。

**根因**：Hermes 的 Python 虚拟环境（venv）没有安装 kdo 包。kdo 源码在 `C:\Users\Administrator\Knowledge Delivery OS 0.0.1\kdo\`，但 Hermes 的 Python 环境没有指向它。

**对策**（二选一）：
1. **pip install -e**（推荐）：激活 Hermes 的 venv 后运行 `pip install -e "C:\Users\Administrator\Knowledge Delivery OS 0.0.1\kdo"`
2. **PYTHONPATH**：在 Hermes 的启动脚本或 systemd env 中加 `PYTHONPATH=C:\Users\Administrator\Knowledge Delivery OS 0.0.1\kdo`

**为什么之前没暴露**：老顽童之前写卡时可以手动操作 Obsidian，不需要 kdo CLI。现在管线越来越依赖 kdo 命令（validate/lint/cards），Hermes 侧没有 kdo 就无法跑。

**关联**：P-5（改配置漏了一处）的同模式——KDO 部署了但 Hermes 环境独立，两边的 Python 环境不共享。

---

## P-27: Provider 迁移时协议不匹配——Anthropic URL 配了 OpenAI SDK

**症状**：Hermes 切到 DeepSeek 后能对话但工作深度不够，且模型显示为 `deepseek-chat` 而非配置的 `deepseek-v4-pro`。

**根因**：Hermes 的 `deepseek` provider 在 models_dev_cache 里标记为 `@ai-sdk/openai-compatible`（走 OpenAI 协议），但 config 配了 Anthropic 端点 `https://api.deepseek.com/anthropic`。SDK 发 OpenAI 格式请求到 Anthropic 端点 → 能通但不完全兼容 → 功能降级。

**对策**：
- 改 provider 前先查 `models_dev_cache.json` 确认 SDK 类型
- `npm: @ai-sdk/anthropic` → base_url 用 `/anthropic`
- `npm: @ai-sdk/openai-compatible` → base_url 用 `https://api.deepseek.com`（不带路径后缀）
- 永远不要猜 base_url，查文档 + 查缓存

**关联**：P-1（配置优先级混乱）的同模式——改了一处漏了另一处，这次是改了 provider 没改协议 endpoint。

---

## P-28: 模型发布日不查公告——K2.7 折腾 3 小时

**症状**：Kimi API 突然全线 400 报 temperature 错误，且 tool call 截断为 48 字符。花费 3 小时改 model 名、改 temperature、改 base_url、换 DeepSeek——最终发现是 Kimi K2.7 当天发布，Anthropic 协议 tool call 兼容未就绪。

**根因**：API 报错后直接调参，没有第一时间查提供商公告。`WebSearch` 在第 30 步才触发，应该在第 3 步就触发。

**对策**：
- API 大规模异常（多个 agent 同时挂）→ 第一步查公告，不是调参
- `WebSearch "<provider> update <date>"` 应该在诊断流程的前 3 步内
- 诊断流程：查公告 → 查日志 → 查 API console → 最后才改配置

**关联**：P-21（无诊断手段时盲目调参）——同样的病，不同症状。这次是"有诊断手段但不用"。

---

## P-29: 批量脚本覆盖非空值——44 张卡 frontmatter 破坏 + 26 张卡 source_context 丢失

**症状**：`8bbfd08d` 提交给 48 张卡补 source_context 时：① 44 张卡 frontmatter 开头出现空行（YAML 解析被破坏）；② 26 张卡已有的真实 source_context 被覆盖为泛型 `"KDO internal record"`。

**根因**：
1. 批量脚本的 `insert_after_author` 逻辑在 author 行后插入了空行
2. 脚本不区分"空值需要补"和"已有值不能改"——直接覆盖了非空的 source_context
3. 正则不限制作用域：`_fix_source_refs_final.py` 使用 `re.sub(r'^(\s*-\s+)(.+)$', ...)` 匹配了 frontmatter 中**所有** YAML 列表行（domain、related、tags、pipeline 等），不限于 source_refs
4. 没有 dry-run 模式，没有 git diff 确认就提交

**对策**：
- 任何批量写操作前必须：① `--dry-run` 预览变更清单；② 对非空值只追加不覆盖；③ 写完后 `yaml.safe_load` 验证 frontmatter 可解析
- 批量修改后必须 `git diff --stat` 确认变更范围在预期内
- **正则必须限定作用域**：只匹配目标字段段落，或显式提取目标字段后替换，禁止用全局行匹配处理 frontmatter
- 门禁脚本已加 `--dry-run` 模式

**此次由王语嫣独立发现并修复**——Agent交叉审计再次验证有效。

**2026-06-28 再次复现**：黄药师 `_fix_source_refs_final.py` 用 `^(\s*-\s+)(.+)$` 清理 source_refs，结果 domain/related/tags/pipeline/diagnostic_signals 等所有列表行被批量替换为 `src_unknown`，影响 327+ 文件。欧阳锋以 6/27 前基线 `9d8dfa27` 恢复后，全库 domain/related src_unknown 清零。

---

## P-30: 批量操作未声明预期变更范围——486 个文件变更无从审查

**症状**：470 张 skill→tool/concept 重分类提交后，欧阳锋面对 486 个文件变更无法快速判断"哪些是预期内的类型替换、哪些是意外连带修改"。

**根因**：批量脚本执行前没有在任务文件中写明"预期变更范围"和"对哪些字段做什么修改"。

**对策**：
- 任何批量操作执行前，必须在任务文件中声明：① 影响文件数 ② 修改字段 ③ 修改前后的值
- 格式：`BATCH: 470 cards, type: skill→tool/concept (heuristic: 含清单/步骤/法→tool, 其余→concept)`
- 提交后欧阳锋审查时只需对比"实际变更 vs 预期声明"，一分钟内可确认

---

## P-30: 自动反馈管线近重复累积——同一问题 508 次写入独立文件

**症状**：`60_feedback/auto/` 下 508 个近重复文件，全部关于 `kimi-深度调研集群方法论-deep-research-swarm`，每条仅 865 字节。占 1444 文件中的 35%。

**根因**：自动反馈检测脚本检测到同一问题后写入新文件而非更新已有记录，且无去重/合并/过期清理逻辑。同一检测条件的每次触发（可能因文件系统事件或定时循环）都产生独立文件。

**对策**：
- 自动反馈写入前先检查是否已有同类记录（按 `slug` 或检测类型去重）
- 同类检测结果应更新已有文件而非新建
- 加自动清理策略：超过 N 天或 N 条的同类记录自动合并/删除
- 临时修复：手动删除 508 条 near-duplicate 文件（`fb_*near-duplicate*`）

---

## P-31: Agent 只挖结构化笔记，跳过口述稿末尾 Q&A 闲聊——最高价值暗知识被遗漏

**症状**：老顽童根据王语嫣把关标记产出王欢 AI 实践域 20 张卡，全部基于结构化工整笔记（127 行）和王语嫣的框架清单。口述稿末尾 250 行 Q&A 闲聊（互动问答、扯淡时间）中的暗知识未被独立成卡——这部分至少还有 2-3 张 dk 的料。

**根因（2 层）**：
1. **笔记过滤效应**：结构化笔记（127 行）只覆盖了主课内容。口述稿的 Q&A 部分不在笔记中，Agent 习惯以笔记为索引，口述稿被视为"噪音"跳过了后半段
2. **入口把关人的扫描不全**：王语嫣的标记文件（`王语嫣-把关标记.md`）基于笔记 + 示意图列出 17 项可加工内容，但 Q&A 闲聊的暗知识不在这些结构化材料里——把关本身就有盲区

**为什么 Q&A 闲聊价值最高**：授课者在正式课程中讲框架、讲方法论——这是"应该说的话"。课后闲聊是松弛状态，最可能说出真实经验：SPEC 陷阱、用魔法打败魔法、招投标 300 万不报满、没有当面答应=拒绝。这些东西不在 PPT 上，不在笔记里，只在闲聊里。

**对策**：
- 入口把关增加一条规则：**口述稿/逐字稿的末尾 20%（课后互动、Q&A、闲聊）必须单独标注可能的暗知识**
- Agent 读口述稿时，不能只看笔记做索引——笔记是人的浓缩，已经丢了一轮信息；口述稿全文可能含有笔记作者认为"不重要"但 Agent 能用上的东西
- 原则：结构化材料是入口，不是全集。口述稿全文是 source of truth

**关联**：P-7（素材预处理缺少 OCR 强制检查——执行者跳过图片）的同模式——信了二次加工材料（笔记/标注），没核实原始材料（口述稿全文）

---

## P-32: 批量汇总文件被覆盖——第二批跑完第一批丢了

**症状**：科学决策 35 张图分两次生成 VLM 描述。第二次 16 张跑完后，`README-VLM描述汇总.md` 只剩 16 张，第一批 19 张丢失。

**根因**：脚本每次直接重写汇总文件，没有增量合并或备份历史。

**对策**：
- 批量生成前先备份旧汇总
- 生成后用脚本合并而不是直接覆盖
- 在汇总文件里按批次追加，或增加 `--merge` 模式

**关联**：P-29、P-30 的同模式——批量操作前先声明范围、保留旧状态。

---

## P-33: 看到「未识别 / 0.3」就归因模型能力——其实是 JSON 解析失败

**症状**：王欢 AI 实践心法 4 张图生成后显示「未识别」、置信度 0.3。第一反应是模型没看懂图。

**根因**：MiniMax-M3 返回的 JSON 中，字符串值内部包含未转义的双引号（如 `标题为"AI 业务档案"`），导致 `json.loads` 失败，脚本 fallback 成低置信度。

**对策**：
- VLM 结构化输出必须做三重兜底：think 标签提取、markdown fence 提取、内嵌引号修复
- 看到 `_parse_error` 或置信 0.3 时，先读原始输出，再决定是重跑还是修复
- 不要把解析失败误判为模型理解失败

**关联**：P-21（无诊断手段时盲目调参）。

---

## P-34: heredoc 里写含反斜杠的代码块——转义失控

**症状**：用 Python heredoc 更新 `ai-image-generation-setup` skill 时，bash 调用示例里的行尾续行符 `\` 没有正确写入，导致多行命令变成一行。

**根因**：非 raw 字符串里 `\\` + 换行的组合在 heredoc 传递时转义层次没控制好。

**对策**：
- 含反斜杠的多行代码块优先用 `Write` 工具或临时 `.py` 文件写入
- 写完后用 `cat -A` 检查实际字符
- 避免在 heredoc 里写需要精确转义的内容

**关联**：P-1、P-5（配置/转义的多层覆盖问题）。

---

## P-35: 欧阳锋审交付物不审原始素材——接受诊断范围边界

**症状**：王语嫣交付"一堂调研方法论"入口质量诊断后，欧阳锋读了诊断报告 + 6 张骨架卡就批准了。后经独立审查发现：诊断只覆盖了 85+ 份素材中的 ~10%（73-97 张卡的知识域只识别了 10 张）。最大漏报——降龙十八掌 18 策略体系、8 张行业手段卡、14 个 DOC 实操策略全部缺失。

**根因**（欧阳锋独有失败模式）：
1. 欧阳锋不直接接触原始素材——只审交付物，天然有信息层距
2. 收到诊断交付物后，直接以诊断的覆盖范围为审查范围，没有问"这个框够不够大"
3. 笔记本就是二次浓缩（口述→笔记→陈述提取→诊断→审查），每层丢 50%，五层后只剩 ~3%

**对策**：
- **入口审查双轨制**：诊断者产出六层比对报告 + 第三 Agent 独立扫读验证覆盖率，两者都通过才算验收
- 收到任何诊断交付物，第一步不问"诊断质量怎么样"，而是问"原始素材全量清单是什么？诊断覆盖了多少？"
- 覆盖率 < 80% → 退回补充或发起独立扫读；≥ 80% → 开始内容审查
- 欧阳锋的审查范围永远以原始素材为边界，不以交付物的边界为边界

**关联**：E009（错误模式库）、P-7（素材预处理少检查——同模式：信任二次材料）、P-15（声称完成未独立验证——同模式：未做独立测量）

---

## P-36: 批量返工任务未列单卡验收路径——ROI案例01 遗漏返工

**症状**：P0-B 科学决策域 14 张卡返工后，王语嫣抽样复核 5/5 达标，但 `case-科学决策-ROI案例01` 实际未被返工，正文仍只有 27 行、frontmatter 残缺。直到欧阳锋最终审查时才发现。

**根因**：
1. 返工任务只按"类型/数量"描述（"11 张 case 卡补 9 层结构"），未列出逐卡清单
2. 抽样复核的样本集未明确排除或包含 ROI案例01，导致遗漏未被抽样到
3. 入口把关与最终审查之间缺少"全量逐卡状态确认"环节

**对策**：
- 批量返工任务必须附逐卡清单（文件名 + 当前缺陷 + 验收标准）
- 抽样复核报告需声明"被抽样卡"与"未被抽样卡"，并对未被抽样卡给出"基于全量扫描的批量判断"
- 最终审查前，审查者先做"清单核对"：任务清单中的每一张卡是否都已达到 status 目标
- 发现遗漏立即升级：不是补一张卡，而是检查整个批次是否还有类似遗漏

**关联**：P-15（声称完成未独立验证）、P-35（欧阳锋不审原始素材——本次为"不审逐卡清单"的同构失败）