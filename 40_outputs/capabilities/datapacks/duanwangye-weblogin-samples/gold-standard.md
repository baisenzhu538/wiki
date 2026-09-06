---
id: datapack-weblogin-gold-standard
title: "登录内容金标准——7 组「原始内容 → 结构化解析输出」真实对照"
type: datapack
domain: [capture, publish]
owner: duanwangye
status: draft
updated: 2026-09-06
parent: README.md
---

# 金标准：好的解析输出长什么样

> 每组 = 真实输入形态 + 真实产物（库内文件锚点）+ 抽取路径 + 判定要点。
> 所有产物均为库内真实文件【实证】，可直接打开对照。个人身份参数已掩码。

## 样本 1｜公众号文章（HTML → 正文 MD）

| | 内容 |
|:--|:--|
| 原始输入 | `https://mp.weixin.qq.com/s?__biz=MzAxNDEw***&mid=2650545393&idx=1&sn=***&chksm=***&sharer_shareinfo=***`（单页 HTML 全量约 3.5MB，大头是内联资源） |
| 抽取路径 | `<h1>` 正则取标题 → `id="js_content"` 区块取正文 → 剥 HTML 标签换行 → 压缩 3+ 连续空行 → 正文截断 30000 字符【实证：`kdo-tools/wechat_link_monitor.py:437-457`】 |
| 真实产物 | `00_inbox/wechat-collect/src_wechat_article_1a718b23df7e860b.md` —— 首行 `# 重构协同：关于AI Native团队的思考`，第二行 `> 来源: <URL>（公众号·偶遇转发）`，之后正文 |
| 判定要点 | ①标题来自 `<h1>` 而非 `<title>`（后者带后缀噪声）【实证：代码只取 h1】；②产物头部两行结构（`# 标题` + `> 来源`）是固定契约，下游靠它做溯源；③作者/发布时间**本管线未抽取**——【实证：`fetch_mp_article` 只返回 `(title, body)` 两字段，锚 `wechat_link_monitor.py:409`】，非"页面无此信息"【该页面是否含稳定作者锚点未逐一验证，不设断言】 |

## 样本 2｜头条文章（info API JSON → 纯文本 MD）

| | 内容 |
|:--|:--|
| 原始输入 | `https://m.toutiao.com/article/7672617566786830875/?share_did=***&share_uid=***&share_token=***&utm_source=wechat...`（分享 URL 带 8+ 个追踪参数） |
| 抽取路径 | 剥 `&amp;` → 取路径中数字 gid → info API JSON 取 `data.title` + 正文 content → 落 MD【实证：`wechat_link_monitor.py:356-406`】 |
| 真实产物 | `00_inbox/wechat-collect/src_wechat_article_tt_569e12742cff2c52.md` —— `# 实测11.78亿Token 仅92元...` + 来源行 + 全文纯文本 |
| 判定要点 | ①正文是纯文本非 HTML，**不需要**剥标签，但保留原文数字/单位精度（"1,178,660,751 Token"、"¥92.08"原样保留）；②来源行保留完整原始 URL（含追踪参数）——溯源价值 > 洁癖，去重靠 canonical_key 另行处理【实证：`canonical_key`，`wechat_link_monitor.py:57-77`】 |

## 样本 3｜头条视频（info API → vod 直链 → mp4 → 逐字稿）

| | 内容 |
|:--|:--|
| 原始输入 | `m.toutiao.com/video/<gid>` → info API JSON → `data` 内 `MainPlayUrl`（两级 JSON，第二级是字符串需再 `json.loads` 一次）【实证：`wechat_link_monitor.py:312-350`】 |
| 真实产物 | mp4 + 逐字稿 `00_inbox/wechat-collect/src_wechat_tt_7666646931699367986.md` |
| 实锤直链形态 | `60_feedback/wechat-collect/_tt_play_url.txt` 存有真实 vod 直链：带 `a=13&cr=0&br=755&dy_q=1786996053` 等签名/时效参数 |
| 判定要点 | ①**直链禁止入库复用**——短时效签名 URL，过期即死，入库只存内容 ID（gid）【推断：签名参数+时间戳结构表明时效绑定，未做存活期实测】；②两级 JSON 嵌套（字符串里再藏一层 JSON）是头条 API 的固定形态，解析代码必须处理两次 loads |

## 样本 4｜抖音视频（CDP 匿名 cookie → yt-dlp → 逐字稿）

| | 内容 |
|:--|:--|
| 原始输入 | `https://www.douyin.com/video/7654610643165120177` + Edge CDP（`--remote-debugging-port=9223` + 独立 `--user-data-dir`）提取 douyin/iesdouyin 域匿名 cookie → Netscape cookies.txt 喂 yt-dlp【实证：`kdo-tools/douyin_cookie_extract.py` 全文】 |
| 真实产物 | `60_feedback/wechat-collect/douyin-dali/7654610643165120177.mp4` + 逐字稿 `00_inbox/wechat-collect/src_wechat_dy_7654610643165120177.md` |
| 抽取路径 | CDP `Network.getAllCookies` → 域过滤（`douyin`/`iesdouyin`）→ Netscape 格式落盘 → 转写头记元数据（`模型: tiny | 设备: cuda | 时长: 346s | 耗时: 30s`） |
| 判定要点 | ①**cookie 值不落 DataPack**，只记结构事实；②转写头部元数据行是金标准契约——模型名/设备/时长/耗时四项让下游能判断这份逐字稿可信度；③tiny 模型转写质量有实锤损伤，见样本 6 判定 |
| 脱敏说明 | cookies.txt 真实值留在采集目录，本包零复制【实证：`60_feedback/wechat-collect/douyin-dali/cookies.txt` 存在于采集目录，未在本包出现】 |

## 样本 5｜视频号 sph 短链（parse_sph → 直链 → 逐字稿）

| | 内容 |
|:--|:--|
| 原始输入 | `https://weixin.qq.com/sph/AWyGiJIRgc`（手机"复制链接"转发形态）→ 本地解析服务 `127.0.0.1:2022/api/channels/parse_sph`（持元宝登录态）【实证：`40_outputs/code/scripts/wechat-serendipity-collect-guide.md` §三/§六】 |
| 真实产物 | `00_inbox/wechat-collect/src_wechat_2404c1658025473c.md`（二手车/柠檬市场主题逐字稿，357s） |
| 判定要点 | ①只有"复制链接"形态可全自动；"直接转发卡片"微信不提供解析入口——**这不是反爬失败，是通道不存在**【实证：guide §五边界表】；②sph 短链本身不含追踪参数，canonical_key 原样保留【实证：`wechat_link_monitor.py:74-76` 兜底分支】 |

## 样本 6｜逐字稿质量分级（金标准 vs 引用禁区）

**这是本包最关键的判定**——同为"成功解析"，可信度差三个量级。

| 等级 | 特征 | 真实例证 |
|:--|:--|:--|
| 🟢 可引用 | 专有名词正确、句子完整 | 样本 2 头条文章（原文抓取非转写，零失真） |
| 🟡 仅检索索引 | 时间戳可用、主旨可辨、**术语错词** | `src_wechat_2404c1658025473c.md`：`1970年經濟學家喬治阿克爾`（=Akerlof）、`銀蒙市場`（应为柠檬市场【推断：上下文为 Akerlof 二手车信息不对称，即 lemons market】）、繁体混出 |
| 🔴 不可引用 | 错词破坏关键概念 | `src_wechat_dy_7654610643165120177.md`：`叫做刚中之导`（应为缸中之脑【推断：下文"这是一个水缸 养了一个大导"】）、`2015年的中循`（应为中旬【推断：上下文时间线】）、`一共五标 搞懂AI证`（关键概念失真） |

**判定规则**：转写产物（whisper）≠ 原文抓取。转写稿默认 🟡，**引用任何具体名词/数字前必须对照原视频**；原文抓取稿默认 🟢。【推断：依据上两例实锤 + 转写头部标注的模型名（tiny）推断模型等级与损伤正相关】

## 样本 7｜微信聊天记录（SQLCipher 加密 DB → 结构化 MD）

| | 内容 |
|:--|:--|
| 原始输入 | 微信 4.x 本地加密 SQLite（SQLCipher 4，passphrase + PBKDF2 密钥），非网络抓取而是**登录态本机快照**【实证：guide §二"解密微信 4.x 数据库（SQLCipher 4，密钥复用，约 10 秒）"】 |
| 抽取路径 | contact.db 群名 → wxid → MD5 → `Msg_<MD5>` 表名 → SQL 查询（时间范围 `create_time BETWEEN` 毫秒时间戳、上下文 `local_id±N`）→ 主题归类 → Markdown【实证：`30_wiki/skills/skill-duanwangye-wechat-extraction.md` 核心能力表】 |
| 真实产物 | 多账号结构【实证：skill 记载"大号 bacon****(34MB)+小号(3MB)"，本包已掩码 wxid】 |
| 判定要点 | ①解密产物是**静态快照**，非实时——最新消息要求微信当前在线【实证：skill 已知限制"需微信登录状态才能解密最新消息"】；②语音/图片/文件是二进制 blob 不可还原原文，需外挂转录（faster-whisper）；③WSL 下跨文件系统直读 DB 会 I/O 报错，先 `cp` 到 `/tmp`【实证：skill 已知限制】 |

## 样本 8｜工具身份凭据传递（命令行 → 角色实例）——首件：段王爷 09-06 建议书

> 严格说不是网页，但**同构**：都是"凭据/身份怎么传给目标会话"。放进来是因为它是「登录失效」在工具层的镜像案例。

| | 内容 |
|:--|:--|
| 原始输入 | `HERMES_PROFILE=<role> hermes -z "<prompt>" --yolo`（env 方式）vs `hermes -p <role> -z "<prompt>" --yolo`（flag 方式） |
| 真实产物 | `60_feedback/diagnosis/diag_20260906_duanwangye-hermes-headless-profile-flag.md`（P0 发现：env 方式三个非五绝 profile 全部错加载为发起者身份；flag 方式精确命中目标 profile） |
| 判定要点 | ①**凭据走显式参数，不走环境变量**——env 在无头单发链路不生效【实证：建议书证据 2/3，三组对照实测】；②"报错但 exit 0"是假成功，退出码不可单独作为成功判据【实证：建议书证据 4，`unrecognized arguments: -Q` 后仍退出 0】 |

---

## 自检清单（产物对照完打勾）

- [ ] 头两行是 `# 标题` + `> 来源: <URL>` 契约格式？
- [ ] 来源 URL 保留完整（溯源优先），去重已走 canonical_key？
- [ ] 短时效直链/cookie 值/token 没有被写进任何入库文件？
- [ ] 转写稿头部有 `模型/设备/时长/耗时` 元数据行？
- [ ] 引用转写稿中的专有名词前已对照原音视频？
- [ ] 个人身份参数（wxid/设备号/分享者 token）未随内容外流？
