---
session_id: duanwangye-2026-09-03
agent_id: duanwangye
date: 2026-09-03
created_at: 2026-09-03T11:50:29.739452+00:00
updated_at: 2026-09-03T11:50:29.739452+00:00
git_head: b3bc2f083
content_hash: 74b0eaa28430
---

# duanwangye · 2026-09-03

# duanwangye · 2026-09-03（本日共 2 次会话）

## 差异栏
本次 vs 上次：核心差异是**复用了本机 CDP 登录态 profile 实现零扫码 L3 提取**——上次复盘（09-01）聚焦 token 脱敏腐蚀，本次聚焦"fs-doc 403 文档如何用 L3 武器库稳定提取"，验证了登录态跨会话复用 + 分段滚动提取法在**新场次（77/86场）**依然有效；同时踩到**虚拟列表块去重 key 设计**新坑（code 块因首字符 \u200b 差异未被去重、DOM 父子嵌套导致同一 code 被选两次），需要沉淀。上次"先探测 API 再决定是否 L3"的纪律继续有效（两篇均 403 后立即切 L3，未在 API 上死磕）。
## 概要
提取并发布两篇 yitang fs-doc 逐字稿到飞书：①第77场Candy（国帅课程创作心路历程，17章 8.3k 字 → doc C2ladsaN2oDrzLxCPaIcwSKBnSh）；②第86场Candy（kinda 龙虾员工实践+Agent 白皮书模版，351 blocks → doc U49vdq1zRoDfLjxqeRfcZSpnnuc，模版 code 块原样保留）。两篇均 TAT raw_content 403 → L3 CDP 复用登录态零扫码 → 分段滚动提取 → 飞书发布 → raw_content 回读验证首尾完整。同时回答老朱：86场与 8/19 处理过的"龙虾员工实践"是不同场次（新链接 doc_id 不同）；模版可原样复刻为 code block。
## 关键决策
| 决策 | 理由 | 结果 |
|------|------|------|
| 两篇 403 后直接切 L3（CDP），不在 API 上重试 | 技能决策树明确：403 = 文档级权限收紧，OAuth 也绕不过 | 复用本机 chrome-yitang 登录态，零扫码直达 |
| 分段滚动提取（window 容器）而非逐节点击 | 滚动顺序=文档顺序，虚拟列表天然顺序正确 | 77场 112 blocks / 86场 351 blocks 全部按序 |
| 86场模版 code 块以 code block 原样发布 | 老朱要求"模版原样复刻格式不动方便应用" | 附录 Agent 工作白皮书模版完整可复制 |
| blocks JSON → 自行转换 md（非源文档转 md） | 源 DOM 提取的 blocks 含 UI 残留与虚拟列表噪声 | 正文 12.3k 字干净发布 |
## 思维盲点
1. 虚拟列表提取的**去重 key 设计**：key 用 `type + text[:150]`，但同一 code 块被 DOM 父子两层各命中一次（wrapper + 内部 container），且首字符 \u200b 差异导致 text[:150] 不同，去重失效 → JSON 里同一模版出现两份（27KB×2），初版 md 转换后看起来像"模版重复 4 次 + 100 组表格"。

**为什么漏掉**：把"去重 key 相同文本"当作充分条件，没意识到 DOM 树里同一内容会挂在多个层级节点上（外层容器 innerText 包含内层），且不可见控制字符（\u200b）会破坏前缀相等判断。应先检查 block 的祖先层级，只取最内层叶子块，或对 key 做规范化（去零宽字符后再截断）。

2. 首次尝试 headless Chrome `--dump-dom` 渲染 SPA **超时 120s 无输出**后才想起查 CDP 端口——其实本机 chrome-yitang profile + 9222 CDP 一直在运行，浪费一轮。

**为什么漏掉**：记忆里"浏览器兜底 Playwright chromium_headless_shell"是渲染 SPA 的兜底，但没把"先查 9222 CDP 是否存活"列为 L3 第一步——登录态复用应该优先于任何新开渲染进程。L3 技能 Step 2.5 明确写了检查顺序，执行时没按技能走查。

3. md → 飞书转换时遇到模版 code 块**内含 ``` 围栏**（8 处），若简单包进 ``` 会撕裂结构——初版直接把 code 文本塞进 md，blocks_to_md 后变成 4 份白皮书+100 表格组假象。

**为什么漏掉**：先入为主认为"提取到的 md 可以直接走 md_to_feishu"，没先检查 code 块内容是否含围栏冲突。Code 块应作为 block_type=14 单独处理，不走 md 中间格式。
## 顿悟
L3 提取的**核心资产不是"能打开文档"，而是"登录态 profile 的跨会话复用"**——chrome-yitang profile 从 8/27 保存至今，本次两篇 fs-doc 全部零扫码直接进，**推翻了"每次 L3 都要用户扫码配合"的旧认知**：扫码只需一次，之后同域文档 agent 全自主。这使 L3 从"人机配合的重型武器"降级为"agent 可独立运行的常规路径"。
## 本会话发现的问题
1. 【虚拟列表去重失效】同一 code 块被 DOM 父子两层各命中一次，且 \u200b 差异破坏 text[:150] key → 模版重复两份。根因：去重 key 未做祖先层级过滤与零宽字符规范化。处置：改用 listitem 容器维度提取（item-N 序号 + 仅取叶子块），code 块去重后仅 1 份真身。
2. 【headless dump-dom 超时】SPA 渲染兜底首选 dump-dom，120s 超时无输出才想起 CDP 已在跑。根因：未按 L3 技能 Step 2.5 走查"先查 9222 + profile"。处置：本复盘元反思固化"L3 第一动作=查 CDP"。
3. 【code 块内含围栏撕裂 md】模版 code 含 8 处 ``` 围栏，塞进 md 后转 blocks 会撕裂成假表格/重复标题。根因：先入为主走 md 中间格式。处置：code 块一律 block_type=14 单独追加，不走 md。
## 过程资产
C:/Users/Administrator/Desktop/wiki/00_inbox/AI落地Live77-国帅课程创作心路历程-逐字稿.md（77场本地档）、C:/Users/Administrator/Desktop/wiki/00_inbox/AI落地Live86-Candy-kinda龙虾员工实践+Agent创建模版-逐字稿.md（86场本地档）、飞书 C2ladsaN2oDrzLxCPaIcwSKBnSh（77场）、飞书 U49vdq1zRoDfLjxqeRfcZSpnnuc（86场）
## 元反思
下次遇 fs-doc 403：①立即查 9222 CDP + profile 是否存活（零扫码优先）②分段滚动提取前先检查去重 key 的祖先层级问题与 \u200b 规范化 ③code 块一律 block_type=14 单独处理，不塞进 md 中间格式 ④先用 item 序号小样验证提取完整性再全量跑。
## Truman复盘
### 逐轮映射
| 轮次 | 人做什么 | 双三角 | AI做什么 | 双三角 |
|------|---------|--------|---------|--------|
| 1 提取77场 | 发 yitang 链接 | 需求 | TAT raw_content 403 → 查 SSR 无数据 | 盲点暴露 |
| 2 切L3 | 追问"用哪层工具" | 反馈 | 诊断 1770032 → 查 CDP/profile 存活 → 零扫码开页 | 路径切换 |
| 3 提取77场正文 | 无 | 反馈 | 探测滚动容器 → 分段滚动 → 112 blocks 按序 | 执行 |
| 4 提取86场 | 追问"86场处理过没"+"模版能否原样" | 需求澄清 | 查历史=不同场次 → CDP 提取 351 blocks → 发现 code 块重复 | 纠偏 |
| 5 发布+验证 | 无 | 反馈 | 正文 md + 模版 code block 发布 → raw_content 回读验证 | 闭环 |
### 飞轮效应
加速"L3 提取资产化"回路：登录态 profile 复用 → 零扫码 → 提取耗时从小时级降到分钟级 → 更多 fs-doc 可自主处理 → 技能/记忆更完善。模版 code block 发布方法沉淀后，下次带模版的场次（Candy 系列）直接套用。
### 对照实验
无人：AI 无法确认老朱要哪层工具（"L1~L3你用哪层"的追问是关键纠偏），且 86场是否处理过需人确认；无AI：老朱需手动复制两份长文+排版+保留模版格式，约 30 分钟/篇；合在一起：两篇共 ~15 分钟完成提取+发布+验证，且模版格式零损失。
### 下次改进
Agent 自身：L3 流程第一动作=查 CDP 存活（curl 127.0.0.1:9222/json/version），profile 存在即零扫码；提取前用 item 序号小样验证。方法论卡：feishu-doc-l3-extraction 技能补充"去重 key 祖先层级 + \u200b 规范化 + code 块单独处理"三条陷阱；feishu-publishing 增加"模版 code 块 block_type=14 原样发布"模式。


---

---

# duanwangye · 2026-09-03 第2次会话（Live261 提取发布）

## 差异栏
本次 vs 早前会话（77/86场）：**首次完整走通"API 全灭 → OAuth 用户授权 → 仍 403 → L3 CDP"三级链路**，且 OAuth 阶段暴露新认知：老朱（阿海）**本人飞书账号也无该文档权限**（yitang.top 分享靠一堂 SSO，不靠飞书 ACL）——推翻了"用户发链接 = 用户有权限 → OAuth 可读"的隐含假设。另踩两个早前会话未遇新坑：**H5/H6 标题降级**（md_to_blocks 只支持 #{1,4}，发布后回读才发现）与 **batch_delete end_index exclusive** 语法。

## 概要
提取并发布 Live261《一堂战略笃定作业 candy》逐字稿（路禹开放麦+星哥科学营销分享，21k 字）：TAT raw_content 403 → 生成 OAuth 链接，老朱手机授权两次（code 一次性+过期）→ UAT 仍 403（阿海无文档 ACL 权限）→ 切 L3：CDP 9222 存活 + chrome-yitang profile 登录态零扫码直达 → 分段滚动 listitem 提取 334 blocks → md 21k 字 → 飞书发布 509 blocks 零失败 → 回读发现 5 处 H5 被降级为带 "##### " 前缀段落 → 删段+原位插 heading5 修复（含 1 处误删补插）→ registry 登记。

## 关键决策
| 决策 | 理由 | 结果 |
|------|------|------|
| OAuth 授权链接发给用户（而非死磕 API/逆向签名） | TAT 403 后按决策树走 UAT；yitang main.js 签名依赖登录态 TOKEN，逆向成本高 | code 换 UAT 成功（user: 阿海），确认文档级权限问题 |
| UAT 403 后立即切 L3 CDP（不重试/不逆向） | UAT 读已知公开文档成功 → 证明 scope 没问题，是文档 ACL；L3 技能决策树明确 | 复用 chrome-yitang profile 零扫码直达 |
| 发布后 raw_content 回读 + blocks 类型抽样双重验证 | 回读只验证文本首尾，类型降级（H5→段落）必须查 block_type | 发现 5 处 H5 降级 + 1 处误删，全部修复 |
| batch_delete 用 curl subprocess 而非 urllib | urllib DELETE+body 偶发 SSL 断连；实测 end_index 是 exclusive | `{"start_index":idx,"end_index":idx+1}` 删单块成功 |
| 修复 H5：删除 text 段 + 原位插 heading5（从后往前） | 飞书不支持改 block_type，只能删旧插新；倒序避免索引漂移 | 4 处脚本修复 + 1 处补插，0 残留 # 前缀 |

## 思维盲点
1. **"用户发链接 = 用户对该文档有飞书权限"是隐含假设**。实际 yitang.top/fs-doc 是第三方分享代理：老朱能看是因为一堂 SSO/分享链接，与飞书 ACL 无关——他的 UAT 读文档照样 403（1770032）。浪费了两轮 OAuth 授权（用户手机操作 + code 过期）。

**为什么漏掉**：把"用户能打开链接"与"用户在源系统有权限"混为一谈。fs-doc 的 acl 段（第一段 32hex）就是分享凭证——页面能 200 打开说明 acl 有效，与飞书权限解耦。早前 Live260 已有 UAT 403 先例（skill 有记录），但没提炼成"yitang fs-doc 文档飞书 ACL 基本都读不了，直接 L3"的硬规则。

2. **发布模板 md_to_blocks 只支持 H1-H4**：53 个标题里混着 5 个 H5（#####），全部落为普通段落且带 "#" 前缀。发布脚本 md→blocks 后直接 append，没做类型抽样就宣布完成。

**为什么漏掉**：数了标题总数却没核对"标题级别分布 × 转换器支持范围"这对组合。回读 raw_content 时尾部看起来正常（文本都在），直到查 blocks 类型才暴露。教训：md 源里出现 `^#{5,6}` 应先告警或确认转换器支持。

3. **手机端 OAuth 交互成本高**：老朱手机看不到长链接、授权后不知道要复制 code URL，来回 3 轮。第一次 code 因 clarify 等用户 10 分钟过期。

**为什么漏掉**：把桌面浏览器心智套到手机场景。二维码约 5 分钟过期的教训在 L3 技能有（扫码场景），但 OAuth code 同样 5 分钟——没有"发码前确认用户就绪"的同等纪律。而且"手机点授权后要复制地址栏 code"对非技术用户是隐藏步骤，应预先说明或引导跳转飞书 App。

## 顿悟
**发布验证必须区分"内容完整"与"结构正确"两层**。raw_content 回读只证明文本层完整（字符数接近、首尾在），但 H5→段落降级、block_type 错误这类结构问题完全隐身。真正有效的验证是 **blocks API 类型分布抽样**（count by block_type vs 预期）+ 尾部 15 块逐块看类型。这解释了为什么 skill 里多次"回读验证通过"仍被用户挑出格式问题——验证深度不够。

## 过程资产
C:/Users/Administrator/Desktop/wiki/00_inbox/Live261-一堂战略笃定作业candy-逐字稿.md（本地档 21k 字）、50_delivery/published/del_20260903_live261_candy/manifest.yaml + md 副本、飞书 https://yitanger.feishu.cn/docx/UKxidTr0aoWOJ0xgxb2chnhvncg（509 blocks）、delivery-registry.md 已登记（11 条）

## 元反思
下次 fs-doc 任务：① **yitang fs-doc 一律先查 9222 CDP + profile**（多数非公开文档 TAT/UAT 都 403，OAuth 多数白费——除非确认用户在一堂域有 ACL）；② 发 OAuth/扫码链接前先确认用户就绪，说明手机操作步骤（含"复制地址栏 code"）；③ md 转 blocks 前先 `grep -c '^#{5,6}'` 防 H5 降级；④ 发布后验证升级为 blocks 类型分布抽样，不止 raw_content 首尾。

## Truman复盘
### 逐轮映射
| 轮次 | 人做什么 | 双三角 | AI做什么 | 双三角 |
|------|---------|--------|---------|--------|
| 1 接链接 | 发 yitang fs-doc 链接 | 需求 | 加载技能+curl 探测+raw_content 403 | 诊断 |
| 2 OAuth | 手机点授权（2次，code 过期1次） | 配合 | 生成授权链→换 UAT→读文档仍 403 | 假设检验 |
| 3 切L3 | 等待/授权配合 | 反馈 | 查 CDP 存活→profile 零扫码开页→确认无登录墙 | 路径切换 |
| 4 提取 | 无 | — | 探测滚动容器→分段滚动 listitem 334 blocks→转 md | 执行 |
| 5 发布 | 无 | — | 509 blocks 零失败→回读→发现 H5 降级→修复→registry | 闭环+纠偏 |
### 飞轮效应
加速"L3 提取资产化"回路第二轮：登录态 profile 跨会话复用再次零扫码成功（上轮 77/86 场沉淀直接复用）；新增**发布后结构验证**节点（block_type 分布），把"发布即完成"升级为"发布+结构验证才完成"——降低用户挑格式毛病的返工概率。
### 对照实验
无人：无法获知手机授权 code（3 轮交互全靠人）；且"文档是否真需要 OAuth"无人确认会多绕 2 轮。无AI：老朱需自己复制 2.1 万字+排版+修正 5 处标题，约 1 小时；合在一起：约 40 分钟全流程（含 2 次授权等待），且 509 blocks 结构干净。
### 下次改进
Agent 自身：fs-doc 文档先 L3 探测（CDP/profile），OAuth 仅当用户明确"我在一堂飞书有权限"才走；发布验证加 block_type 分布抽样。方法论卡：feishu-doc-l3-extraction 已补 H5 降级 + batch_delete exclusive 两坑；feishu-publishing 模板 md_to_blocks 已修为 #{1,6}。
