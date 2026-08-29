---
id: case-20260829-zhanlue-dingding-l3-extraction
title: 「案例：战略笃定篇逐字稿提取——window分段滚动法，滚动顺序=文档顺序」
type: case
status: draft
confidence: 0.9
trust_level: medium
domain:
- feishu
- extraction
- browser-automation
author: 段王爷（南帝）
source_context:
  - 2026-08-29 提取 yitang.top/fs-doc 《我用一堂做一堂-战略笃定篇》逐字稿并发布飞书
  - yitang
source_refs:
- capability/duanwangye/feishu-doc-l3-extraction
source_person: 段王爷（南帝）实战
reviewed_by: 待审查
aliases:
- 战略笃定篇提取
- window分段滚动
- 滚动顺序=文档顺序
- L3新范式
- 虚拟列表提取
discoverable_by:
- 分段滚动提取
- 虚拟列表
- 文档顺序
- 顺序乱序
- 重复标题
- 登录态复用
related:
- skill-feishu-doc-l3-extraction
- skill-duanwangye-feishu-publishing
- case-feishu-live259-l3-extraction
- case-feishu-minutes-extraction-attempt
tags:
- method:browser-automation
- method:feishu-extraction
- scene:content-acquisition
- audience:executor
- content-format:case
- source-person:agent
- evidence:observed
created_at: 2026-08-29
updated_at: 2026-08-29
quality_labels:
- insight
- actionable
- reusable
- paradigm-shift
diagnostic_signals:
- signal: 逐节点击提取后章节顺序与侧边栏不一致
  lens: 懒加载时序导致 DOM 加载顺序 ≠ 文档顺序
  follow_up: 改用 window 分段滚动提取（滚动顺序=文档顺序）
- signal: 页面 innerText 长度不变但 scrollHeight 巨大（如 105k）
  lens: 虚拟列表按视口渲染，滚动容器可能是 window 而非 page-main
  follow_up: 探测滚动容器（scrollHeight > clientHeight 的元素），分段滚动提取
- signal: 同一标题出现多次（如"如果带入背景"×6）
  lens: 去重 key (type, text[:200]) 会把重复标题吞掉，无法精确分组重排
  follow_up: 分段滚动天然保留每次出现，不纠结去重
review_date: 2026-08-29
---

> 本卡是 [[skill-feishu-doc-l3-extraction]] 的第二范式实证——在逐节点击+目录重排之外，发现 **window 分段滚动提取法**：滚动顺序天然=文档顺序，一步到位绕开"加载顺序乱序 + 重复标题被吞"两大陷阱。与 [[case-feishu-live259-l3-extraction]]（逐节点击范式）互为补充。

# 战略笃定篇逐字稿提取：window 分段滚动法

> 一句话：提取《我用一堂做一堂-战略笃定篇》（yitang fs-doc，46 目录项长文档），L1 TAT 403 → L3 登录态复用零扫码。逐节点击提取到 585 blocks 但**顺序=加载顺序≠文档顺序**（"开始上课"跑到第 7 位）；改 **window 分段滚动提取**（滚动容器探测 + 60% 视口步长分段滚动 + 每段提取去重），同样 585 blocks 但**顺序=文档真实顺序，零重排** → 567/567 blocks 零失败发布飞书 → registry 登记 + 技能沉淀。

---

## 过程（起点→尝试→转折→结果）

### 起点：老朱发来一篇长文档

老朱发来链接 `https://yitang.top/fs-doc/6cc61cd78884167e31402ed42fc23268/UrApd3CbcoosFAxDdfpcG0eJnJg`，要求提取逐字稿写入飞书，明确提示"你用L3技能试试"。

### 尝试：L1 探测

TAT + raw_content → **403 forBidden**（1770032）。文档非公开，按决策树切 L3。缓存 token 400 = 过期，刷新后 403 = 权限收紧——明确信号。

### 转折 1：登录态复用零扫码

检查 CDP：`curl http://127.0.0.1:9222/json/version` 返回 Chrome 147 存活！且已有两个 yitang tab（Live260 遗留）。playwright-core connectOverCDP 直开目标文档 → **标题正常渲染（"🎯特别计划：我用一堂做一堂-战略笃定篇"），无登录墙**。Live260 的 profile 隔 6 天仍有效——登录态复用验证第三次成功。

### 转折 2：识别虚拟列表渲染模式

滚动测试：`window.scrollTo` 后 body innerText 从 10209 **收缩**到 2357——不是滚动懒加载，是**虚拟列表**（只渲染可视区）。初始 SSR 只渲染中间区域（scrollHeight 105408 但 innerText 仅 9752）。目录 46 项（Element UI 树 `.el-tree-node__content`）。

### 转折 3：逐节点击提取——顺序乱序

playwright 原生 click 逐节点击 46 项 + 每轮提取 blocks 去重累积 → **585 blocks、30 heading、25216 字符**。但 heading 顺序 = **加载顺序 ≠ 文档顺序**："初始手牌"在[1]位、"开始上课"跑到第12位。原因是初始 SSR 从文档中间渲染，点击才加载其他章节。

### 转折 4：分组重排尝试——发现重复标题陷阱

按 heading 分组 + 目录重排时发现：**重复标题被去重吞掉**（"如果带入背景"在目录出现 6 次，blocks 里只剩 1 个 heading；"我的决策过程"同样）。无法精确分组重排，只能接受"标题减少、正文完整"。

### 转折 5：⭐ window 分段滚动提取——滚动顺序=文档顺序

关键洞察：**滚动容器是 window 不是 page-main**！探测：`document.documentElement.scrollHeight=105458` vs `window.innerHeight=2849`（page-main 的 scrollH==clientH==105408，不滚动）。

分段滚动脚本：
- STEP = 60% 视口（1709px），总 64 步
- 每步 `window.scrollTo(0, i*STEP)` + 700ms + 提取可视区 docx blocks 去重累积
- 滚动 6 步后出现 +82（第一段新内容），之后每 ~6 步 +70~80

**结果：585 blocks（与逐节点击数量完全一致），但 heading 顺序 = 文档真实顺序**（开始上课→快速回顾→为什么要学→预热思考题→提前划重点→这节课很特别→初始手牌→Before→After→角色推演→第一轮~第七轮→重新理解和回顾→作业→活动），与侧边栏目录完全一致，**零重排**！

### 结果：发布零失败 + 三重复核

- 清理：去零宽空格 U+200B、去 `- -` 残留、修 `1. 1.` 双编号（merged 列表行删除）
- 本地 MD：23.5k 字符、30 标题、1020 行 → `00_inbox/我用一堂做一堂-战略笃定篇-逐字稿.md`
- 发布飞书：**567/567 blocks / 12 批零失败**，`anyone_readable` 公开权限
- 验证：`raw_content` 回读 22701 字符，首尾完整（"开始上课 Hello大家好啊" → "冲榜挑战...学年反馈"）
- registry：`del_20260829_7b3d2c41` 登记，Delivered 2
- 沉淀：skill 卡更新 + 本 case 卡 + MOC 注册

---

## Claims / Evidence

| Claim | 证据 | 证据状态 |
|:---|:---|:---|
| 滚动容器不一定是 page-main，可能是 window | page-main scrollH==clientH==105408（不滚动），window scrollH=105458 vs clientH=2849 | 实测 |
| 虚拟列表按视口渲染：innerText 长度不变 ≠ 无内容 | innerText 一直 9752，但 scrollHeight 105408；blocks 提取到 585 | 实测 |
| 逐节点击提取的 blocks 顺序=加载顺序≠文档顺序 | "开始上课"在 blocks 第12位，目录却在第1位 | 实测 |
| 重复标题被去重 key (type, text[:200]) 吞掉 | "如果带入背景"目录6次，blocks 只剩1个 heading | 实测 |
| **window 分段滚动：滚动顺序=文档顺序** | 分段滚动后 heading 顺序与侧边栏目录完全一致，零重排 | 实测 |
| 登录态跨任务复用：同一 user-data-dir 重启即恢复 | Live260 profile 隔 6 天仍有效，零扫码直进 | 实测 |

## 关键数字

| 数据 | 来源 | 状态 |
|:---|:---|:---|
| 46 目录项（Element UI 树） | 实战日志 | 实测 |
| 逐节点击 585 blocks / 30 heading / 25216 字符 | v2 提取 | 实测 |
| window scrollH=105458 / clientH=2849 | 滚动容器探测 | 实测 |
| 分段滚动 585 blocks（与逐节一致）但顺序正确 | v5 提取 | 实测 |
| 发布 567 blocks / 12 批零失败 | 发布日志 | 实测 |
| raw_content 回读 22701 字符，首尾完整 | 验证日志 | 实测 |

## 双三角六要素映射

| 三角 | 要素 | 案例对应 |
|:---|:---|:---|
| 人的三角 | 判断力 | 逐节点击顺序乱序后不硬凑重排，转而探索"有没有天然顺序的提取法" |
| 人的三角 | 体系 | L1 探测→L3 决策树；滚动容器探测→分段滚动，先诊断再动手 |
| 人的三角 | 创造力 | "滚动顺序=文档顺序"——把虚拟列表的渲染机制变成提取武器 |
| AI 三角 | 场景 | yitang 长文档（46 目录项）逐字稿提取（登录态复用+虚拟列表双重挑战） |
| AI 三角 | 数据 | DOM block 提取（docx-xxx-block 类名），滚动驱动的可视区数据 |
| AI 三角 | 基本功 | playwright-core CDP、滚动容器探测、虚拟列表机制理解、去重累积 |

## Critique

**内部局限（自指）**：分段滚动依赖页面真实滚动（window 可滚）；若页面无滚动条（内容全渲染）或滚动容器极深嵌套，需重新探测；每次提取后需等渲染（700ms/步），64 步约 45 秒——比逐节点击快但非秒级；对页面结构变化（类名/渲染模式）仍敏感。

**外部攻击者 1（Kahneman 式——可用性偏差）**：逐节点击是 Live259/260 验证过的成功范式，惯性下很容易"继续用+补重排"。本案例证明**先探测滚动容器再选路径**是更优起点——若一开始就检查 scrollHeight vs clientHeight，可省 3 版脚本踩坑。

**外部攻击者 2（Taleb 式——反脆弱）**：虚拟列表的"只渲染可视区"看似是提取障碍，实际是**文档顺序的天然编码**——滚动驱动渲染，渲染顺序=滚动顺序=文档顺序。把平台的"限制"转化为"特征"，是提取技术的反脆弱设计。

## Synthesis

本次突破的核心机制：**滚动是虚拟列表的文档顺序指针**。逐节点击范式解决"单章节渲染"（点击才加载），但引入"顺序乱序"副作用；window 分段滚动范式直接利用虚拟列表的滚动驱动渲染特性，**提取顺序天然=文档顺序**，零重排、零标题去重问题。两个范式互补：**先探测滚动容器**（可滚→分段滚动；不可滚→逐节点击），比"默认逐节点击+事后重排"更优。跨案例收敛：与 [[case-feishu-live259-l3-extraction]] 的"登录墙不是死路是协作入口"同构——**平台的限制（虚拟列表/登录墙）都藏着可被利用的机制（滚动顺序/扫码入口）**。机制层见 [[skill-feishu-doc-l3-extraction]] Step 3.5。

## Action Triggers

1. 任何 yitang/飞书长文档提取，**先探测滚动容器**：`scrollHeight > clientHeight + 100` 的元素，window 也是候选
2. 滚动容器可滚 → **window 分段滚动提取**（60% 视口步长 + 每段提取去重），滚动顺序=文档顺序
3. 登录态复用：CDP 存活 + profile 在 → 零扫码直进；Chrome 死但 profile 在 → 同 user-data-dir 重启即恢复
4. innerText 长度不变 ≠ 无内容：用 blocks 数（querySelectorAll）判断，不用 innerText
5. 提取后若用逐节点击，必须按侧边栏目录重排；重复标题被吞可接受（正文完整）

## 失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| 滚动 page-main 无效 | 滚动后 innerText/blocks 无变化 | 探测滚动容器，window 可能是真容器 |
| innerText 误判 | 长度不变就以为点击无效/无内容 | 用 blocks 数判断，虚拟列表只渲染可视区 |
| 逐节点击顺序乱序 | "开始上课"跑到第12位 | 用 window 分段滚动（滚动顺序=文档顺序） |
| 重复标题无法分组 | "如果带入背景"×6 只剩1个 heading | 分段滚动天然保留；或接受标题减少 |
| 死磕分组重排 | 手工重排复杂易错 | 直接换分段滚动，别硬凑 |
