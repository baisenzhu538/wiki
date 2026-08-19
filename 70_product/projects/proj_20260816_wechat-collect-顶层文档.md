---
project_id: "proj_20260816_wechat-collect"
name: "微信视频号定向采集管线（kdo collect-wechat）"
goal: "让 KDO 智能体可按博主定向收集视频号内容 → 转逐字稿 → 沉淀为知识资产，实现楚门课程'偶遇自动采集'机制的 KDO 版"
owner: "黄药师"
status: "active"
stage: "design"
path: "70_product/projects/proj_20260816_wechat-collect-顶层文档.md"
created_at: "2026-08-16"
updated_at: "2026-08-16"
source: "楚门 AI×知识管理探索营（00_inbox/AI知识库/）——'偶遇自动采集五通道'之一"
related: "#338 PatrolKit 设计（L3 采集层）"
---

# 顶层文档：微信视频号定向采集管线

> **本文件解决什么问题**：楚门课程里两种方式——①"偶遇自动采集"（刷到视频号 → 自动转逐字稿 → 分类 → 进知识库）；②"这个小导演不错，给我拉一圈"（指定博主 → 智能体定向采集 → 逐字稿 → 研究文档）。这是 KDO 工厂"偶遇自动采集"能力的落地，也是 #338 PatrolKit 设计的 L3 采集层实现。
> **有且只有一个**：本文件是项目最顶层文档，所有子文档/任务/代码从这里索引。

## 零、楚门两种方式对齐（口述稿锚点）

来源：`00_inbox/AI知识库/楚门-AI知识管理探索营-口述.txt`（L2580-2870 第五次飞跃·体系自动化）

| 方式 | 楚门机制 | 口述稿锚点 | KDO 落地 |
|:--|:--|:--|:--|
| **方式一：偶遇→自动采集** | 日常偶遇碎片自动进知识库：公众号/知乎→Cubox 转 Markdown→Obsidian（两三分钟）；**视频号→自动转文字稿→可视化编排→分类→存 Cubox 月份文件夹** | L2602/L2604（文章通道）、**L2612**（视频号通道"需要点黑科技"）、L2648-2652（AI 超级入口：扔任何视频→2 分钟→Cubox 月份文件夹+逐字稿） | `--scan-wechat`（PC 微信接收目录扫描）+ `--url`（链接入口）+ 转写 + 知识化——**下载环节由 res-downloader 嗅探完成**（见 §二） |
| **方式二：博主/主题定向** | 看到好作者→"这个小导演不错，给我拉一圈"→智能体获取产品清单+代表作 5-10 条→视频存本地 NAS→转逐字稿→**沉淀一篇研究文档** | L2622-2630（创作者定向）、L2632-2636（选题→深度调研 Skill→1-3 天报告） | `--author "<博主名>"`：搜索→下载→转写→研究文档（`--min-likes` 按点赞筛选代表作） |
| 替代通道（无技术能力） | 腾讯官方"元器"转逐字稿（不稳定，短的可以） | L2668-2672 | `--import-text`（手机小程序转好文字稿直接入库） |

**楚门关键机制（KDO 版可复用）**：AI 超级入口形态（一个入口收一切偶遇）、单点学习（一年 100+ 随手扔给 Agent）、饱和话术（"不要给我省任何投入，30-50 篇写不出来不许提交"）、事实核查（LLM 研究后指出错误）、120 万字零人工撰写。

## 一、目标与非目标

### 目标
1. `kdo collect-wechat --author "<博主名>"` 一条命令完成：搜索博主 → 拉视频列表 → 下载 → 转逐字稿 → 沉淀知识资产（**方式二**）
2. `kdo collect-wechat --scan-wechat` 偶遇通道：PC 微信接收目录 + res-downloader 下载目录 → 新视频自动转写 → 知识化（**方式一**）
3. 产出：逐字稿入 `10_raw/sources/` + 研究文档（顶层文档式）入 `30_wiki/`
4. 可复用：任何博主、可批量、可定时

### 非目标
1. 本轮不做直播回放（后续迭代）
2. 本轮不违反版权（仅个人学习用途）
3. 本轮不接入抖音/小红书等（架构预留，先跑通视频号）

## 二、技术方案（调研结论，2026-08-16）

### 下载环节三入口（2026-08-17 设计定稿——不再依赖 TikHub token）

| 入口 | 技术 | 用户操作 | 状态 |
|:--|:--|:--|:--|
| **① res-downloader 嗅探（主力·偶遇）** | MITM 代理（127.0.0.1:8899），putyy 19.2k★；播放视频号时自动嗅探下载 mp4 到配置目录 | 打开 res-downloader → 启动代理 → 微信里播放视频号 → 自动下载；**手机转发链接到文件传输助手 → PC 打开链接播放 → 同样触发嗅探** | ✅ 软件已下载（桌面 res-downloader.exe，2026-08-17 00:36）待接入管线 |
| **② API 解析+Referer（主力·定向）** | 元宝扫码登录态（公共 Worker 已失效 1042）或 gkgy curl 五步：解析链接→带 `Referer: https://channels.weixin.qq.com/` 下载 | 扫码一次建立登录态 | 代码已备（`download_via_referer`），登录态待建 |
| **③ TikHub API（备选·定向）** | `GET api.tikhub.dev/api/v1/wechat_channels/fetch_search_latest?keywords=博主名` → 视频列表 → 直链下载 | 注册 token | 需 token，免费额度有限 |

> **为什么主力是 res-downloader**：微信视频号视频本体不落盘（流式播放），转发到文件传输助手产生的是链接文本——任何"链接→直接解析下载"方案都受反爬影响（公共 Worker 失效实证）。MITM 嗅探是**播放即下载**，绕开解析，是楚门"黑科技"的零代码实现。

### 转写引擎
- **faster-whisper**（本地，免费，WSL GPU 已实测：tiny/cuda，5s 音频 4s 完成）
- 模型现状：tiny ✅ 就绪；small 残缺（59M）待补；large-v3 未下载（中文精度最佳，后续）
- ffmpeg 提取音频（WSL 转写脚本内部处理）

### 沉淀链路
```
【方式一·偶遇】手机转发链接→文件传输助手 → PC 微信落盘 msg/file/*.txt → scan 提取链接
  → 微信打开链接播放 → res-downloader 嗅探下载 mp4 → scan 发现新视频
【方式二·定向】--author 博主名 → TikHub/API解析 → 视频列表（按点赞筛选）→ 下载
  → 统一：ffmpeg 提取音频 → faster-whisper 转逐字稿 → 10_raw/sources/（source_id 登记）
  → LLM 三层次总结（事实/规律/洞察，楚门框架）→ 研究文档（五段模板）→ 30_wiki/cases/
  → kdo ingest → 可检索（kdo query）
```

## 三、实施阶段

### Phase 1：MVP（先跑通，1-2 天）
- [x] `kdo collect-wechat` CLI 骨架（参数：--author / --limit / --min-likes / --import-local / --scan-wechat）——三通道齐备（2026-08-16）
- [x] **爆炸式调研完成（2026-08-16，research-explosion-partner）**：`00_inbox/视频号逐字稿调研/视频号逐字稿自动化工作流-爆炸式建模.md`——下载两路线（MITM/API解析）、转写三引擎、完整链路样板 weixin-favor-kb
- [x] **下载路线落地**：代码加路线 A（MITM 备用，scribe-transcribe）+ 路线 B（API 解析+Referer 主力）+ 路线 C（TikHub 降级备选）——**不再依赖 TikHub token**
- [x] **知识化模板落地**：weixin-favor-kb 模板（frontmatter+要点+行动+原文折叠）接入 build_knowledge_note()
- [x] faster-whisper 1.2.1 安装完成（WSL，阿里云镜像）；GPU CUDA 12.3 可用
- [x] **tiny 模型就位**（wget 断点续传下载 72MB）+ 辅助文件（config/tokenizer/vocabulary）；small 残缺（59M）已跳过
- [x] **端到端狗粮通过（2026-08-16 23:09）**：`--import-local` → WSL GPU 转写（tiny, cuda, 8s 音频 6s 完成）→ 逐字稿入 `10_raw/sources/src_wechat_test_audio.md`——MVP 全链路跑通
- [x] 逐字稿入 `10_raw/sources/` + 登记（真实视频 2 个已入）
- [x] **偶遇通道（新增，用户核心需求）**：`--scan-wechat` 扫描 `D:/Backup/Documents/xwechat_files/*/msg/video/`（PC 微信接收目录）——手机转发到"文件传输助手"即自动采集
- ⚠️ **2026-08-17 已知断链（重启前发现）**：①链接文件（.txt/.html）扫描后**只记录不下载**——豆包扫码/链接转发均无法提取视频本体；②`processed.log` 重复记录 + 部分视频（1ad47349/bcbb8a）无转写产物；③`--author` 下载未带 Referer（微信 CDN 必拒）。**修复见 §八 变更记录（2026-08-17）**

### Phase 2：知识化（1 天）
- [x] **LLM 三层次总结（事实/规律/洞察——楚门框架）**：`kdo-tools/wechat_knowledge.py`——DeepSeek v4-flash 调用，自动读 Hermes config 的 API key，无正文时防幻觉阻断（已实测：正弦波逐字稿被 LLM 正确识别"无正文不编造"）
- [x] **研究文档自动生成**：weixin-favor-kb 五段模板 + 三层次落 `30_wiki/cases/`（已实测生成 case-wechat-test_audio.md + 真实视频 case）
- [x] **真实场景端到端全通（2026-08-16 23:24）**：D 盘微信真实视频 2 个（169s 升学宴致辞 + 15s 短视频）→ 转写（GPU 17s/10s）→ LLM 三层次知识化（事实/规律/洞察精准，含"仪式文案生成"商业洞察）——**偶遇采集→知识入库闭环验证完成**

### Phase 3：智能化（后续）
- [ ] 批量博主管理（一个作者一个目录）
- [ ] 定时巡检（新视频自动补采）
- [ ] 对接 #338 PatrolKit L3 采集层（候选池自动沉淀）
- [ ] **res-downloader 接入后补**：一键命令 `--scan-all`（微信目录 + res-downloader 目录合并扫描 → 转写 → 知识化全自动）；下载目录配置化

## 四、验收标准

1. `kdo collect-wechat --author "X"` 端到端跑通：搜索 → 下载 ≥3 个视频 → 逐字稿生成 → 入 sources
2. `kdo query "X 的观点"` 能检索到沉淀内容
3. 研究文档落盘（含视频清单 + 洞察）
4. 无 token 时方案 B 可用（手动下载兜底）

## 五、依赖与前提

| 依赖 | 状态 | 说明 |
|:--|:--|:--|
| **res-downloader** | ✅ 桌面 res-downloader.exe（2026-08-17 00:36） | 代理 127.0.0.1:8899；需装证书+启动代理；下载目录待配置并告知管线 |
| TikHub API token | ⏸ 降级为备选 | 定向通道①（API 解析+Referer）跑通前不必须 |
| faster-whisper | ✅ 已装（WSL，1.2.1） | tiny 模型就绪；small 残缺待补；large-v3 中文最佳后续下 |
| ffmpeg | ✅ Windows 有 / WSL 转写脚本内部处理 | 已确认 |
| 网络 | ✅ | api.tikhub.dev 国内可用（非 .io） |

## 六、风险与边界

1. **版权**：仅个人学习用途，不传播下载内容
2. **反爬**：视频号有强反爬——MITM 嗅探（res-downloader）播放即下载，最稳；任何"链接解析"方案都可能随时失效（公共 Worker 1042 实证）
3. **GBK 编码**：Windows 终端跑脚本需 PYTHONIOENCODING=utf-8（#323 同族）；文件路径含中文注意
4. **费用**：TikHub 免费额度有限，批量前确认计费
5. **转写质量**：tiny 模型短视频可转（5s→1 句），长视频/口语场景建议补 small/large-v3 模型

## 七、子文档索引（本文件为唯一入口）

| 文档 | 用途 |
|:--|:--|
| 本文件 | 顶层文档（项目总览） |
| `00_inbox/视频号逐字稿调研/视频号逐字稿自动化工作流-爆炸式建模.md` | 调研资产（四环节×双路线矩阵、12 工具全景） |
| `30_wiki/tools/tool-wechat-transcript-automation-workflow.md` | 工具卡（老顽童产，欧阳锋已审，time_valid 2027-02） |
| `30_wiki/frameworks/framework-serendipity-five-channels.md` | 偶遇五通道框架卡（楚门方法论） |
| `kdo-tools/collect_wechat.py` / `wechat_knowledge.py` / WSL `transcribe.py` | 管线代码 |
| `60_feedback/wechat-collect/` | 中间产物（pending_links / processed.log / test_audio.wav） |
| `60_feedback/tasks/task_20260816_laowantong-wechat-transcript-tool-card.md` | 工具卡生产任务 |

## 八、变更记录

### 2026-08-19（黄药师：去重修复 + 文章知识化 + inbox 监工迁移）
- **链接规范化键去重**：公众号按 `__biz+mid+idx`、头条按 gid 定内容身份，追踪参数（chksm/scene/pass_ticket 等）全剥——修复同一文章多次分享被重复采集（《重构协同》一文曾采 3 份，已合并归档至 `60_feedback/wechat-collect/duplicates-archive/`）
- **文章接入知识化**：公众号/头条文章入库后自动走 LLM 三层次（此前只入库无研究文档，洪七公 §五-1 闭环）；`wechat_knowledge.py` prompt 泛化为"逐字稿或文章正文"
- **inbox 监工迁移 Windows**：`watch_inbox.py` 原依赖 WSL cron，WSL 不常驻 → cron 静默失效（08-17 23:50 后停止）——已建计划任务 `kdo-inbox-watch`（每 10 分钟）；P2 项从"只 print 无人消费"改为落 dispatch 文件；排除 `wechat-collect/` 目录（自有管线）
- 文件命名改用规范化键 hash（同一内容重采 = 覆盖同一文件，幂等）
- **抓取健壮性（狗粮实测抓到）**：公众号全文 3.5MB，微信限流断流（IncompleteRead）是常态——`fetch_mp_article` 重试 3 次 + 部分响应含正文标记即降级使用；文章抓取失败不再记 seen（与视频同语义：成功才记录，失败下轮自动重试）——修复"瞬时断网 = 文章永久丢失"缺陷

### 2026-08-18（主链路定稿：复制链接转发全自动）
- **用户操作定稿**：手机"复制链接"转发（`weixin.qq.com/sph/xxx`）→ 全自动。直接转发卡片（无链接）微信不给解析入口，仅兜底（电脑播放拦截）
- **二次实测通过**：AWyGiJIRgc（WorkBuddy 海报批量生成，99s）复制链接转发 → 自动解析下载转写知识化 → 00_inbox，零人工
- **技术文档重写**：`40_outputs/code/scripts/wechat-serendipity-collect-guide.md`（看懂版：用户操作/系统链路/部署/运维/边界）
- **Skill v1.1.0**：主链路 + 边界 + 故障速查更新
- **cap_hub**：F_SERENDIPITY_COLLECT 描述更新（主链路：复制链接转发）

### 2026-08-17（黄药师恢复会话）
- **楚门两种方式对齐**：§零 新增——方式一偶遇（L2602/L2612/L2648-2652）+ 方式二博主定向（L2622-2630）+ 替代通道（L2668 元器）
- **下载环节定稿（v2）**：主力 = **元宝登录态解析（ltaoo/wx_channels_download parse_sph）——链接→直链，无人值守全自动**；res-downloader MITM 降级为播放兜底；TikHub 备选
- **断链修复**：collect_wechat.py ①补 import shutil ②下载带 Referer ③链接文件扫描增强 ④processed.log 成功才记录 ⑤res-downloader 目录扫描 ⑥一键串联
- **🆕 全自动偶遇链路打通（方式一终态）**：
  1. `wechat_link_monitor.py`——解密微信 4.x 数据库（SQLCipher 4，密钥复用段王爷 build_keys.py）→ 读文件传输助手消息（ZSTD 解压）→ 提取视频号链接 → 调 parse_sph（元宝 Cookie）→ 下载直链 → WSL GPU 转写 → LLM 三层次知识化 → 全部落 `00_inbox/wechat-collect/`
  2. **实测通过（2026-08-17）**：WorkBuddy 视频（"WorkBuddy 省钱实操｜DeepSeek + GPT 双模型接入教程"，146s）全链自动完成
  3. **自动化固化**：计划任务 `wx-channels-download`（登录自启解析服务）+ `wechat-link-monitor`（每 10 分钟跑监控）
  4. 元宝 Cookie 有效期约 1 个月，失效后重新登录 yuanbao.tencent.com 提取（CDP 脚本 `kdo-tools/_tmp_get_cookie.py`）

---
*黄药师 · 2026-08-16 · 顶层文档制度（楚门课程）首次实践*
