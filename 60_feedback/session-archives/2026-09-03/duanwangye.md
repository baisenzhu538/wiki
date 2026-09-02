---
session_id: duanwangye-2026-09-03
agent_id: duanwangye
date: 2026-09-03
created_at: 2026-09-02T16:34:09.642311+00:00
updated_at: 2026-09-02T16:34:09.642311+00:00
git_head: 14419df03
content_hash: 7eea2c8488e7
---

# duanwangye · 2026-09-03

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
