---
id: datapack-duanwangye-weblogin-samples
title: "DataPack·登录内容样本库（段王爷）"
type: datapack
domain: [capture, publish]
owner: duanwangye
status: draft
updated: 2026-09-06
task: task_20260906_duanwangye-datapack-weblogin
source_refs:
  - 60_feedback/wechat-collect/_dl_log.txt
  - kdo-tools/wechat_link_monitor.py
  - kdo-tools/douyin_cookie_extract.py
  - 40_outputs/code/scripts/wechat-serendipity-collect-guide.md
  - 30_wiki/skills/skill-duanwangye-wechat-extraction.md
  - 60_feedback/diagnosis/diag_20260906_duanwangye-hermes-headless-profile-flag.md
  - 00_inbox/wechat-collect/
related:
  - "[[skill-duanwangye-wechat-extraction]]"
  - "[[framework-serendipity-five-channels]]"
---

# DataPack·登录内容样本库

> **一句话**：登录态/半登录态网页内容（公众号·视频号·头条·抖音·微信DB·工具profile）从「原始内容」到「结构化产物」的真实对照库——给 AI 弹药，不教步骤（步骤归 Skill）。
> **分工**：Skill《登录内容处理工作流》= 怎么做（抓取→解析→清洗→结构化）；**本包 = 依据什么判断**（好的解析长什么样 / 失败长什么样 / 哪些字段必须留）。

## 文件清单

| 文件 | 要素 | 内容 |
|:--|:--|:--|
| `gold-standard.md` | ① 真实样例 | 8 组「原始内容 → 结构化解析输出」真实对照（含逐字稿质量分级） |
| `pitfalls.md` | ② 反例（踩坑实录） | 14 条实测失败案例 + 处置，全部带锚点 |
| `field-extraction.md` | ③ 对照数据 | 字段抽取判定表（必须保留 / 可弃噪声 / 禁止入库） |

## 使用说明（要素④）

### 适用问题

- 其他 agent 需要处理**带登录态/凭据的内容源**时：公众号文章、视频号、抖音、头条、微信聊天记录、工具 profile 拉起
- 要判断「这个解析产物算不算成功」「这个字段该不该留」「这个失败是限流还是凭据失效」
- 要对逐字稿/抓取正文的质量做分级判断（能不能直接引用）

### 何时挂载

- 触发词：抓取 / 采集 / 登录态 / cookie / 解析失败 / 逐字稿 / 公众号 / 视频号 / 头条 / 抖音 / 微信DB
- 挂载时机：**动手写抓取/解析逻辑之前**读 `field-extraction.md`（先知道要留什么）；**解析产物出来之后**对照 `gold-standard.md` 自检；**解析失败时**先查 `pitfalls.md` 的症状表再动手改代码

### 隐私与脱敏红线（不协商）

- **敏感凭据一律不入库**：cookie 值、token、passphrase 在本包中只出现「结构事实」（如"全量 13 个 cookie 含 .tencent.com 域的 hy_token"），不出现真实值
- **个人账号内容一律脱敏**：wxid、设备号（share_did/share_uid）、分享者身份参数（share_token/sharer_shareinfo）在本包中以掩码形式出现；原始值留在库内真实产物文件中，本包只给锚点不复制全文
- 内容版权边界：公开课/公开文章按 W7 拍板（2026-08-22）可用，唯一边界 = 不得打着一堂名义商业活动（锚：`40_outputs/code/scripts/wechat-serendipity-collect-guide.md` §五）

### 断言标注约定

本包所有关键判断按行为宪法三级标注：【实证】= 有文件/行号锚点；【推断】= 有间接证据的解读；【猜测】= 待验证。**引用本包结论时请连同标注一起引用**。

### 更新纪律

- 每次真实采集/解析出现**新失败模式**或**新金标准形态**，追加对应文件并在 frontmatter `updated` 改日期
- 对照产物（`00_inbox/wechat-collect/`）是活体证据，路径失效时先核查文件是否迁位再决定删除条目

## 来源锚（本包弹药出处）

| 弹药 | 来源 |
|:--|:--|
| 采集链路 + 故障排查表 | `40_outputs/code/scripts/wechat-serendipity-collect-guide.md`（黄药师，2026-08-18/19） |
| 解析/去重/降级代码 | `kdo-tools/wechat_link_monitor.py` |
| 抖音 cookie 提取 | `kdo-tools/douyin_cookie_extract.py` |
| 微信 DB 解密与查询 | `30_wiki/skills/skill-duanwangye-wechat-extraction.md`（段王爷，欧阳锋 06-29 审） |
| 工具身份凭据传递实证 | `60_feedback/diagnosis/diag_20260906_duanwangye-hermes-headless-profile-flag.md` |
| 真实产物 | `00_inbox/wechat-collect/*.md`、`60_feedback/wechat-collect/` |
