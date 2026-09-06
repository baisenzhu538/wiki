---
id: datapack-weblogin-field-extraction
title: "字段抽取判定——保留/可弃/禁止入库 三分类对照表"
type: datapack
domain: [capture, publish]
owner: duanwangye
status: draft
updated: 2026-09-06
parent: README.md
---

# 对照数据：字段抽取判定

> 用途：解析产物出来后，逐字段对照判定——该留的留了吗？该弃的弃了吗？**禁止入库的有没有漏网？**
> 三分类：**保留**（丢了溯源/内容受损）· **可弃**（纯噪声/追踪器）· **禁止入库**（凭据/隐私/时效死链）。

## 总判定原则

1. **身份字段极简化**：能定位"哪篇内容"的最小字段集保留，能定位"谁分享的"的字段全部弃/掩码
2. **溯源优先于洁癖**：来源行保留完整原始 URL（含追踪参数），去重逻辑在 canonical_key 层做，不在产物层做【实证：`00_inbox/wechat-collect/src_wechat_article_tt_569e12742cff2c52.md` 来源行保留全参数，锚 `wechat_link_monitor.py:527` 产出格式】
3. **凭据零落库**：cookie/token/passphrase 只允许以"结构事实"描述，禁止出现值
4. **转写稿必须带元数据头**：模型/设备/时长/耗时四项决定可信度定级

## 表 A｜必须保留（丢了 = 内容或溯源受损）

| 通道 | 字段 | 判定依据 |
|:--|:--|:--|
| 公众号 | `__biz` + `mid` + `idx` 三元组 | 文章身份唯一键，去重靠它【实证：`canonical_key`，`wechat_link_monitor.py:63-67`】 |
| 公众号 | `<h1>` 标题 | 产物首行契约；`<title>` 带后缀噪声故不用【实证：代码只取 h1，`:437`】 |
| 公众号 | `id="js_content"` 正文 | 唯一正文锚，全文 3.5MB 中正文在前段【实证：`:417-419` docstring】 |
| 头条 | gid（`/video|group|article/(\d+)`） | 内容身份唯一键【实证：`canonical_key`，`:70-72`】 |
| 头条 | `data.title` + content 纯文本 | info API 的两个内容字段【实证：`:331,398`】 |
| 全部 | 来源行完整原始 URL | 溯源契约，下游 `> 来源:` 行格式【实证：产物文件第二行实态】 |
| 抖音 | 视频 ID（`/video/(\d+)`） | cookie 域过滤后唯一稳定身份【实证：`douyin_cookie_extract.py:63` 域过滤逻辑】 |
| 转写稿 | `[MM:SS]` 时间戳 | 检索定位回原音视频的唯一锚【实证：产物逐行时间戳实态】 |
| 转写稿 | 元数据头（模型/设备/时长/耗时） | 可信度定级依据【实证：`src_wechat_dy_*.md` 第二行实态】 |
| 微信DB | 群名→wxid→MD5→`Msg_<MD5>` 表链 | 查询路由链，断一环查不到【实证：`skill-duanwangye-wechat-extraction.md` 核心能力表】 |
| 微信DB | `create_time` 毫秒时间戳 | 时间范围过滤唯一依据【实证：skill 同上】 |

## 表 B｜可弃噪声（留着污染检索与去重）

| 通道 | 字段 | 弃置理由 |
|:--|:--|:--|
| 公众号 | `chksm` / `scene` / `srcid` / `mpshare` | 每次分享都变的追踪参数，入去重键必穿透【实证：P-11 整案】 |
| 头条 | `share_did` / `share_uid` / `share_token` / `timestamp` / `tt_from` / `utm_*` | 追踪器 + **分享者设备/用户身份**（隐私面）【实证：样本 2 来源行实态含 8+ 参数】 |
| 公众号 | HTML 内联资源（script/style/img） | 全文 3.5MB 的大头，剥标签后无信息量【实证：`fetch_mp_article` docstring"大半是内联资源"】 |
| 公众号 | 正文超过 30000 字符的尾段 | 截断契约，防超长垃圾【实证：`wechat_link_monitor.py:527` `body[:30000]`】 |
| 正文 | 3+ 连续空行 | 剥标签产生的排版噪声，压缩为双空行【实证：`:455,459` `\n{3,}` 压缩】 |
| vod 直链 | 签名/时效参数串 | 短时效死链，入库零价值【推断：签名参数+dy_q 时间戳结构；存活期未实测】 |
| 逐字稿 | 无（时间戳全保留） | 本通道无"噪声行"——错词是质量问题非噪声，处置走定级不走删改【实证：gold-standard 样本 6】 |

## 表 C｜禁止入库（脱敏红线，违者回滚）

| 类别 | 具体字段 | 处置 |
|:--|:--|:--|
| 凭据 | cookie 值（含 Netscape cookies.txt 全部 value） | 不复制进任何知识层文件；只可描述结构事实（如"全量 13 个含 hy_token"【实证：guide:102】） |
| 凭据 | `hy_token` 等主 token、passphrase（SQLCipher 密钥） | 同上；密钥只在本地 `wechat-decrypt/build_keys.py`【实证：guide §4.1"密钥：复用 …build_keys.py 的 PASSPHRASE"】 |
| 个人身份 | wxid（如 `bacon****` 已掩码） | 知识层一律掩码；原始值留在本地 DB |
| 个人身份 | 分享者设备/用户号（`share_did`/`share_uid`/`sharer_shareinfo`） | 产物来源行可含（溯源），**引用/转述时必须掩码** |
| 隐私内容 | 私聊/群聊中的个人言论原文 | 入知识层前先脱敏人名+账号，聊天记录只按主题归类产出【实证：skill"结构化输出：原始消息→主题归类→Markdown"】 |
| 时效死链 | vod/douyin 签名直链 | 只存内容 ID，不存直链 |

**判定动作**：产物入库前扫一遍——grep 目标文件是否含 `cookie=`、`token=`、`wxid_`、`MS4wLjA`（设备号前缀）等特征串；命中即回滚脱敏。

## 表 D｜产物质量分级（量化判定）

| 级别 | 判定条件 | 允许用途 | 实证 |
|:--|:--|:--|:--|
| 🟢 可引用 | 原文抓取（非转写），标题+正文齐全 | 直接引用、入 wiki 溯源 | `src_wechat_article_*.md` 系列 |
| 🟡 仅检索索引 | 转写产物（whisper），时间戳在、主旨可辨、含错词 | 检索/定位/主旨归纳；**禁止直接引用专有名词** | `src_wechat_2404c1658025473c.md`（繁体+银蒙市场） |
| 🔴 不可引用 | 关键概念失真，或元数据头缺失 | 仅作"存在过"线索，须回原音视频 | `src_wechat_dy_7654610643165120177.md`（缸中之脑→"刚中之导"） |
| ⚫ 无效 | 转写报错/空正文/加密视频误喂 | 不入产物区，走对应 P-xx 处置 | P-10 Invalid data 实案 |

> 🟡/🔴 的分界是**是否破坏关键概念**【推断：依据 gold-standard 样本 6 两组实锤归纳，非模型厂官方标准】。
