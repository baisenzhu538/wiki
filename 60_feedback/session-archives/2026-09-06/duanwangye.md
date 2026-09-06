---
session_id: duanwangye-2026-09-06
agent_id: duanwangye
date: 2026-09-06
created_at: 2026-09-05T21:21:45.710453+00:00
updated_at: 2026-09-05T21:21:45.710453+00:00
git_head: cb69e771d
content_hash: 9dbd29480e7c
---

# duanwangye · 2026-09-06

# duanwangye · 2026-09-06（本日共 2 次会话）

## 差异栏（本次 vs 上次）
本次 vs 上次（09-05 妙记提取消耗战）：主旋律完全反转——上次是"同路反复重试 3 小时"的路径消耗战，本次是**决策树一次走完、全程零重试循环**的顺行局：开场即加载技能（遵循 08-27 老朱点名教训）、先查重+探活、L1 探测 403 后立即切 L3、登录态复用零扫码、单趟滚动提取一次成功、发布零失败，端到端约 10 分钟。被打破的隐含预期一个："L3 = 必然要扫码"——实际 Chrome CDP + profile 登录态复用已连续多次任务稳定工作，扫码已从常态退化为异常路径。复发模式检查：上次的核心病灶"失败后微调参数而非换路"本次未出现，因为失败点（脚本损坏、/json/new 语义）都是一次性修复型而非路径型失败。

## 概要
提取 yitang fs-doc《启动会：2026年全新AI大航海》逐字稿并存入飞书。链路：技能加载 → session_search 查重（无重复）→ CDP 探活（Chrome 存活+profile 在）→ L1 TAT raw_content 探测 403（1770032）→ L3 复用登录态零扫码开 tab → window 分段滚动提取 723 blocks（8 H1 + 23 H2，顺序=文档真实顺序）→ 转 Markdown 29.4k 字符 → 飞书发布 725 blocks 零失败 → raw_content 回读验证首尾完整。产物：`00_inbox/启动会-2026年全新AI大航海-逐字稿.md` + 飞书文档 HT0UdfpLLoGYprxQR8Ycwwbyn6e。

## 关键决策
| 决策 | 理由 | 结果 |
|------|------|------|
| 第一动作加载 feishu-doc-l3-extraction 技能 | 08-27 老朱点名"先查知识库再动手"，不重造轮子 | 决策树/陷阱表/模板全部直接复用 |
| 仍按纪律跑 L1 探测而非直接 L3 | 用户预告"预计 L3"≠权限事实，08-19/08-23 两次 L1 直达证明"先探测再定路径" | 403（1770032）实锤 → 切 L3 有据 |
| CDP 探活后再决定浏览器方案 | 技能卡 L3 第一动作 = 查 9222 存活 | Chrome 存活+profile 在 → 零扫码直达 |
| 自写单趟滚动脚本（挂 window 回收数据） | 技能模板需跑两趟滚动；CDP eval 局部变量不跨调用存活，挂 `window.__kdo_seen` 单趟即可 | 723 blocks 一次提取，顺序=文档顺序零重排 |
| write_file 损坏后弃修补、重写+python patch | 长内容生成质量不可靠时，修补不如重写+语法校验 | node --check 通过后一次跑通 |
| 发布用技能自带 publish_md_to_feishu.py | 09-01 实测 3 篇零失败的成熟管线 | 725 blocks 15 批全 OK，回读验证通过 |

## 思维盲点
1. **write_file 生成长 .cjs 脚本时内容损坏**——两次写入都出现乱码残片（"from_parent:" 之类无意义片段混入代码），若直接执行会得到难懂的语法错误。

**为什么漏掉**：本王默认 assume 生成内容的完整性，没有建立"长代码写入后立即语法校验"的前置动作（node --check 是后段才补上的）。根因是长内容生成时的注意力衰减，且第一反应是"继续修补损坏文件"而不是"质疑生成质量、重写+校验"。正确姿势：写完即校验，损坏即重写，不恋战。

2. **对 CDP `/json/new` 的 HTTP 语义按技能卡旧记录硬编码**——技能卡记录 GET 有效，本机 Chrome 147 已恢复 PUT 语义，首跑直接 FATAL。

**为什么漏掉**：把技能卡当真理而没意识到"工具行为随版本漂移"。根因：环境事实（Chrome 版本行为）与知识卡（写作时点快照）的时效差没有在卡里标注版本号。已识别需回写技能卡补版本适配注记。

3. **curl -o 写大响应体在 MSYS 下静默失败（exit 23）**——回读验证第一步用 curl -o 落盘再解析，白跑一轮。

**为什么漏掉**：验证环节图"落盘可复查"的方便，忽略了 MSYS curl 对大 body 写文件偶发失败的环境特性。根因：验证链路应该选最短路径（管道直读），落盘是可选增强而非必经步骤。

## 顿悟
1. **推翻了"提取脚本必须依赖 playwright-core / agent-browser 二进制"的旧认知**——Node 22 原生 WebSocket + fetch + `window.__kdo_seen` 全局挂载，约 100 行单文件脚本即可完成"开 tab→滚动→提取→回收"全链路，且单趟滚动即拿到文档顺序数据（旧模板要跑两趟或做章节重排）。零依赖方案 + window 挂载模式是比现有模板更简的形态，应回写技能卡。

2. **推翻了"L3 流程的主成本在突破登录墙"的隐含预期**——登录态复用连续多次任务零扫码后，L3 的实际瓶颈已转移到"脚本工程质量"（内容损坏、API 语义漂移、响应落盘）这类执行层细节。意味着技能卡的经验重心该挪位：扫码章节降权，脚本可靠性章节升权。

## 知识碰撞记录
- 任务到达即加载 `feishu-doc-l3-extraction` → 决策树（403 判据）、陷阱表（L3 第一动作查 CDP 存活）、window 分段滚动法 → **对得上**，全链路按卡执行
- `session_search` 查重 O50bd7qlBouT39xvJYbcCTC3nqc / "2026全新AI大航海" → 零命中 → 确认新文档，正常提取
- `review-gate-format` 技能 → 11 章格式 + 盲点根因格式 → **对得上**，本次复盘按卡执行
- 新发现（卡上没有）：Chrome 147 `/json/new` PUT 语义、`window.__kdo_seen` 单趟回收模式 → 待回写技能卡

## 本会话发现的问题（#458）
1. 现象：write_file 写 7.6KB 的 .cjs 脚本，两次输出均混入乱码残片。
   定位：长代码内容一次性生成的可靠性问题，非工具本身故障（重写后内容正常）。
   建议：长脚本 >3KB 时分步写或写完立即语法校验（node --check / python compile），把校验固化为"写代码文件"动作的收尾步骤。
2. 现象：技能卡记录的 `/json/new?<url>` GET 用法在 Chrome 147 报非 JSON 响应。
   定位：CDP 新版恢复 PUT 语义，知识卡是旧版本快照。
   建议：回写 feishu-doc-l3-extraction 陷阱表：GET 失败自动降级 PUT 的兼容写法（本次已在脚本内实现）。
3. 现象：curl -o 保存 28KB raw_content 响应 exit 23 无输出。
   定位：MSYS curl 写大响应体偶发失败，环境特性非权限问题。
   建议：验证类请求一律管道直读（curl | python -c），不做中间落盘。

## 过程资产
- `C:/Users/Administrator/Desktop/wiki/00_inbox/启动会-2026年全新AI大航海-逐字稿.md`（29.4k 字符，8 章 23 节）
- 飞书文档 HT0UdfpLLoGYprxQR8Ycwwbyn6e（725 blocks 零失败，yitanger 域，回读验证通过）
- `tmp/extract_launch.cjs`（零依赖单趟滚动提取脚本，argv 参数化可复用）
- `tmp/blocks_to_md_dahanghai.py`（本次 blocks→md 转换，含跨类型去重）
- `tmp/dahanghai_v5.json`（原始提取数据 723 blocks）
- 待回写：feishu-doc-l3-extraction 陷阱表补 Chrome 147 /json/new + window 挂载单趟回收模式

## 元反思
下次怎么做才能不一样：
1. **写代码文件的收尾动作固定化**：write_file 产出 .py/.cjs/.js 后，下一个动作永远是语法校验（node --check / python -m py_compile），不合格即重写——把"生成质量不可信"当作默认假设而不是意外。
2. **技能卡时效标注**：回写技能卡时给环境相关结论（CDP 端点行为、浏览器版本行为）标注"验证于 Chrome <版本>/<日期>"，让下次使用者能判断快照新旧。
3. **验证链路最短化**：回读/验证类请求管道直读，落盘只在需要留证时做——省掉环境差异带来的中间失败。

## Truman复盘
### 逐轮映射
| 轮次 | 人做什么 | AI做什么 |
|------|---------|---------|
| 1 | 发 fs-doc 链接 + 预告"预计 L3" | 加载技能 + session_search 查重 + CDP 探活（并行） |
| 2 | 等待 | L1 探测：TAT 换取 + raw_content → 403 实锤，决策树切 L3 |
| 3 | 等待 | 零扫码开 tab（登录态复用）→ 写提取脚本（损坏→重写+patch）→ 单趟滚动 723 blocks |
| 4 | 等待 | blocks→md 29.4k 字符 → publish 725 blocks 15 批零失败 |
| 5 | 等待 | raw_content 回读验证（首尾+锚点全命中）→ Truman 复盘沉淀 |

### 飞轮效应
本轮加速的是**登录态摊销回路**：一次扫码投入（历史会话）被本次第 N 次任务零成本复用，"扫码"环节已从 L3 主成本降为异常处理。同时**模板复用回路**继续转：发布管线（publish_md_to_feishu.py）.argv 即用零修改，本会话新增的单趟滚动脚本进入下一轮复用池。

### 对照实验
无人：任务不会被发现和启动，文档价值滞留。无 AI：人工打开文档逐章逐段复制 8 章 23 节 + 手工整理格式，约 1-2 小时且易漏段。合在一起：约 10 分钟端到端（含验证），零遗漏零重排，且产出同时落 inbox 知识库（可检索）与飞书（可分发）。

### 下次改进
- Agent 自身：固化"写代码即校验"收尾动作；验证请求管道直读不落盘。
- 方法论卡更新：feishu-doc-l3-extraction 陷阱表补两条——①Chrome 147 `/json/new` GET→PUT 兼容写法；②`window.__kdo_seen` 单趟滚动回收模式（替代两趟模板），并给环境类结论加版本/日期标注。

---

# duanwangye · 2026-09-06 第2次会话（听脑API+微信MCP双通道体检）

## 差异栏
本次 vs 凌晨会话（hermes headless -p flag 体检）：**横向体检对象从 hermes 通道换成听脑 API 与微信 MCP 两条外部工具通道**。核心差异：凌晨是"发现机制失效并报建议书"，本次是"发现失效直接修复"——微信 MCP 的 PYTHONPATH 污染与 KDO MCP 同根同源，直接照既有药方（清 PYTHONPATH 的 .cmd 启动器）修通，未送建议书。另一差异：听脑 API 在 wiki 检索与会话检索都搜不到，最终靠 meeting-assistant 的 state.db FTS 命中转写内容卡，顺藤摸到 90_control/itingnao-kit/——**跨 profile 状态库做全局检索的补充索引**是本次新方法。

## 概要
老朱要求核实"听脑 CLI/API"与"微信 MCP"两通道是否可用。听脑线：wiki/会话检索均无接入记录 → 从 meeting-assistant state.db 的 FTS 搜出"听脑 AI"转写内容 → 定位 90_control/itingnao-kit/（Node.js 工具包，API base https://api.itingnao.com，key 在 ~/.itingnao_api_key）→ 实测 test-connection + list-records 均成功（567 条录音，最新为 9 月数据）→ 通道正常。微信 MCP 线：hermes mcp list 显示 wechat ✗ disabled → mcp test 报 Connection closed → 直跑 mcp_server.py 复现根因 = PYTHONPATH 污染（hermes venv cp313 的 pydantic_core 无法在 Python312 cp312 加载）→ env -u PYTHONPATH 握手成功 → 照 run_kdo_mcp.cmd 药方写 run_wechat_mcp.cmd（set PYTHONPATH= + cd + python mcp_server.py）→ hermes mcp remove + add 指向新启动器（echo Y 过交互）→ mcp test Connected 1236ms，17 tools 全部发现 → 修复完成。

## 关键决策
| 决策 | 理由 | 结果 |
|------|------|------|
| state.db FTS 作为 wiki 检索失灵后的补充索引 | 听脑在 30_wiki 只有内容卡无接入卡；meeting-assistant 处理过转写任务，其 state.db 有 kdo_search 输出缓存 | 3 分钟定位工具包，避免全盘盲搜 |
| 微信 MCP 直接修复而非送王语嫣建议书 | PYTHONPATH 污染有先例（KDO MCP），药方现成，属既有 bug 修复非架构变更 | 修复完成且验证通过 |
| 修复用 .cmd 启动器而非改全局 PYTHONPATH | 全局改会破坏 hermes 自身运行环境（KDO 线已验证） | 隔离干净，与 KDO 修法一致 |
| hermes mcp remove+add 而非手改 config.yaml | CLI 改配置是既有纪律（改后需重启 gateway 生效） | 配置写入正确，17 tools 全启用 |

## 思维盲点
1. 首轮检索用"听脑"关键词在 wiki + 会话记录双搜均空手，差点回复老朱"查无此物"。

**为什么漏掉**：老朱说"给过你"，工具包实际叫 itingnao-kit（拼音 itingnao），而 wiki 内容卡里"听脑 AI"只是素材标签。检索时没做"中文名→拼音/英文名"的映射假设，也没想到去其他 profile 的 state.db 里找。以后检索无结果时应该：换同义词（tingnao/itingnao/转写）→ 查其他 profile 的状态库 → 查文件系统 find。

2. mcp test 失败后第一反应是检查 MCP 配置语法和启动脚本路径，没有第一时间直接跑底层 mcp_server.py 复现错误。

**为什么漏掉**："Connection closed"这个报错没有指向性，直觉先怀疑配置层；但根因在 Python 运行时环境（PYTHONPATH 注入）。分层排查应更果断：配置对→直接跑 server 脚本看原始 traceback→再回配置层。

3. 本机 shell 会话自带 PYTHONPATH 污染（hermes venv cp313 site-packages 注入所有 python 进程）这个环境事实，之前 KDO MCP 修复时已知并沉淀过，但微信 MCP 配置当时没有同步修——同款坑在两个 MCP 上发生两次。

**为什么漏掉**：KDO 修复时只修了自己的启动器，没有全局扫描"还有哪些 MCP 用 Python312 直跑"一并修复。修坑时应横向排查同型故障点。

## 顿悟
**"通道体检"的正确姿势是实测而非查配置**——hermes mcp list 显示 wechat disabled 是表象，直跑 server 握手成功才是真相（服务器代码完好，只是启动环境坏了）。反过来，听脑 API 配置完好不代表能用，实测 test-connection 拿到 567 条数据才算数。配置层与运行时层必须分开验证，任何一层都不能代表通道健康度。

## 过程资产
90_control/itingnao-kit/（听脑工具包，已验证可用：test-connection.js / list-records.js / batch-list.js / batch-detail.js）、C:/Users/Administrator/wechat-decrypt/run_wechat_mcp.cmd（新启动器，清 PYTHONPATH）、duanwangye profile config.yaml（wechat MCP 重新注册，17 tools enabled）、本复盘

## 元反思
下次通道体检：①先实测后下结论，list 状态≠实际健康度；②检索三轮法则：中文→拼音/英文→其他 profile state.db；③修一个 PYTHONPATH 坑时横向扫描所有同型 MCP 一次修完；④修复类任务先判断"有先例药方"还是"新故障"——有药方直接修并汇报，新故障才走建议书流程。

## Truman复盘
### 逐轮映射
| 轮次 | 人做什么 | 双三角 | AI做什么 | 双三角 |
|------|---------|--------|---------|--------|
| 1 接任务 | 发问：听脑+微信MCP两通道查状态 | 需求 | session_search×2 + search_files 双检索 | 诊断 |
| 2 深挖听脑 | 无 | — | meeting-assistant state.db FTS 命中 → 定位 itingnao-kit | 检索方法扩展 |
| 3 实测听脑 | 无 | — | test-connection + list-records 实测 567 条 | 执行 |
| 4 排查微信MCP | 无 | — | mcp test 失败 → 直跑 server 复现 PYTHONPATH 根因 | 根因定位 |
| 5 修复+验证 | 无 | — | 写 .cmd 启动器 → remove+add → test Connected 17 tools | 闭环 |
### 飞轮效应
KDO MCP 沉淀的 PYTHONPATH 药方直接复用到微信 MCP，修复时间从可能的半天缩到 15 分钟——**修坑沉淀的复利首次跨工具兑现**。同时本次新增"跨 profile state.db 补充检索"方法，回补检索飞轮。
### 对照实验
无人：两条通道状态无从问起，遇到"查无此物"就死局；无AI：老朱需自己翻文档确认 API key 位置、手动测 API、诊断 MCP 连接失败，约 2 小时；合在一起：约 20 分钟完成双通道体检+一处修复，微信 MCP 恢复可用。
### 下次改进
Agent 自身：检索失败立即三轮换词+跨 profile 库；修坑先横向排查同型点。基建：微信 MCP 配置变更需重启 gateway 才对本会话生效——下次会话该 MCP 工具可直接调用，应实测一轮微信查询确认端到端通。

## 本会话发现的问题
1. 【微信 MCP PYTHONPATH 污染】Python312 直跑 mcp_server.py 时被 shell 注入 hermes venv cp313 site-packages，pydantic_core 加载失败 → stdio 连接秒断。根因：KDO 修复时未横向排查同型 MCP。处置：run_wechat_mcp.cmd 清 PYTHONPATH，已验证 Connected + 17 tools。
2. 【检索盲区：中文名≠工具名】"听脑"工具包实际名 itingnao-kit，wiki/会话检索"听脑"零命中，靠跨 profile state.db FTS 才定位。根因：无中英文名映射检索习惯。处置：沉淀三轮检索法（中文→拼音→跨库）。
3. 【hermes mcp add 交互卡点】不接 stdin 时 "Enable all tools?" 交互提示导致静默 Cancelled。处置：echo Y 管道喂确认。
