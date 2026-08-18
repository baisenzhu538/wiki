---
title: 黄药师失忆恢复记录
updated_at: 2026-08-16
---

# 黄药师失忆恢复（重启后 3 分钟加载）

> **用户说"继续"时**：按最小恢复路径读文件 → 3 分钟回到全链状态。
> **⚠️ 2026-08-15 修订**：恢复路径以「目录内最新」为准，不采信写死的日期/路径——本文件各节是快照，目录实际状态是真相。

## 最小恢复路径

| 优先级 | 文件 | 作用 |
|:--|:--|:--|
| P0 | `.agent/huangyaoshi-context.md` | 身份、行为牌组 B1-B6、启动步骤、铁律 0（提审即流转） |
| P0 | `agent复盘/huangyaoshi/daily-context/` **目录内最新文件**（当前 2026-08-16.md） | 最近一次完整复盘（含差异栏）——⚠️ 不要读本表写死的旧日期，以目录内最新为准 |
| P0 | `20_memory/` 本文件 | 关键状态速查 |
| P1 | `cap_hub/features.json` | KDO 20 Feature 注册表（含 FEISHU_DOC_MCP） |
| P1 | `kdo-tools/mcp/config.yaml` | MCP deployments 部署记录（谁挂在哪） |
| P1 | `90_control/domain-mapping.md` | 域清单单一真相源 |

## 2026-08-17 校准补充（恢复会话 B1 门禁实证）

### 视频号采集管线（proj_20260816_wechat-collect）状态
- **楚门两种方式已对齐顶层文档**（§零）：方式一偶遇（口述稿 L2612/L2648-2652 AI 超级入口）+ 方式二博主定向（L2622-2630）——`--scan-wechat` 对应方式一、`--author` 对应方式二
- **断链已修复**：collect_wechat.py 补 import shutil / 下载带 Referer / processed.log normcase 去重 / 成功才记录；wechat_knowledge.py 覆盖保护+跳过已知识化+NO_PROXY
- **🆕 全自动偶遇链路打通（方式一终态，2026-08-17 实测）**：
  - `wechat_link_monitor.py`：微信 4.x 数据库解密（密钥=段王爷 build_keys.py passphrase，19/19）→ 文件传输助手 ZSTD 解压 → 链接提取 → **ltaoo wx_channels_download parse_sph**（元宝 Cookie）→ 直链下载 → WSL GPU 转写 → LLM 三层次 → 全部落 `00_inbox/wechat-collect/`
  - 服务：`wx_video_download.exe`（API 127.0.0.1:2022，config.yaml `cloudflare.sphCookie` 已配全量 Cookie）
  - 计划任务：`wx-channels-download`（登录自启）+ `wechat-link-monitor`（每 10 分钟）
  - 元宝 Cookie 有效期约 1 个月，失效后：Edge 调试端口 9222 → `kdo-tools/_tmp_get_cookie.py` 重新提取（需用户在元宝页面扫码）
- **res-downloader**（MITM 嗅探）降级为播放兜底
- **待办**：small/large-v3 模型升级（tiny 够用但质量一般）；视频标题语义化（文件名是 hash）；KDO 侧接入 30_wiki 前的 ingest/validate 流程



> 08-16 晚重大事件：**全量 Windows 迁移启动**（洪七公断连生产事故 → 用户拍板"以后全量 Windows"）——codex 主导 T0-T4（#342-346）+ #347 洪七公迁移（已完成，用户确认成功）+ #348 R 型调研 Partner 部署（原黄药师→改派 codex，飞书真机冒烟 PASS）。我的日常复盘只覆盖 08-16 凌晨两次会话，迁移大事件由 codex/王语嫣推进，未参与。

### 队列真实状态（2026-08-17 B1 门禁）
- 总 328：queued=6 / claimed=0 / pending_review=2
- pending_review：#347（洪七公迁移，codex）+ #348（R 型部署，codex）——均等欧阳锋终审
- **我的任务：#345 T3（duanwangye 飞书 Windows 就绪测试）queued/挂起**——触发条件：等老顽童 CLI 工作完成 + 用户命令
- 迁移系列 #342/#343/#344/#346 均 ⏸ 挂起（同触发条件）
- hermes MCP 修复：venv 误装 mcp 2.0.0 → 降级 1.28.1（isError 兼容）；**8 个运行中 gateway 待重启加载**（重启时机等用户）
- kdo_search 178s 慢已修复（王语嫣 O-15：search_index.py 进程级缓存 + graph 缓存）



### 基建状态
- **周期表 Feature 工具链 v1.0 全就位**：`feature_menu.py`（kdo-tools/）——list/query(--layer/--dimension/--scenario/--keyword 别名命中)/pick/info/stale/combo/by-layer；数据源 `10_raw/sources/feature-periodic-table-v1.0.json`（100 Feature，47 卡 aliases，13 条三级证据，25 verified）；组合种子 `kdo-tools/feature_combos.json`（4 实测组合）；测试 `test_feature_menu.py` 28 断言
- **MCP 双 server 已接入 3 个飞书 agent**（教练/开会/基本功）：kdo 检索型 + feishu_doc 操作型——重启 gateway 后生效（WSL 侧）
- **任务模式已真机验证跑通**：老朱拆书作业五节流程完整（背景→出口式多轮→三支柱检索→第一人称成稿→待确认）

### 队列状态（2026-08-16 B1 门禁实证）
- 队列 304 任务：queued=4 / claimed=0 / pending_review=0——我的任务全清
- #323（GBK 修复）终审 PASS A-；#325（统一检索层）终审 **PASS A**（六层 O3 全过零瑕疵）
- #304/#303 C1 已闭环（双助理飞书可用）；#298 reviewed 无待办
- 在产（非我）：#319 O-14 domain 清扫（王语嫣）、#320-322 销售卡组（老顽童）

### 待办/条件项
- ~~KDO 工作区 24 处未提交改动~~ ✅ **2026-08-16 已 commit**（2 个主题 commit：7fa95c0 检索与索引基建修复 + 8bc5645 历史累积+GBK；工作区 0 残留；pytest 561 passed 1 历史失败）
- Windows 侧 5 profile（duanwangye/hongqigong/laowantong/wangyuyan/note-coach）已挂 kdo MCP——**gateway 重启后各发一条飞书消息验证检索生效**（欧阳锋提示）
- 停车场：P-31 ✅ 已解决（08-15 内存 16→32GB）、P-3 事实核对门（等裁定）、P-2 domain 加权（等 domain 污染清零）、P-29 队列编码修复（归并待排）
- P2-DYN-01（新 agent 模板固化 + health-check MCP 巡检）已登记，P2 立项时执行（欧阳锋审）
- 快照迁移 P3 未立项

### 关键教训（E020 等）
- **回答前先检索验证**（TCPR 定义错误教训——SOUL 写错 = 全错）
- **实测 > 推断**（Flash 强于 Pro 预览版——用户实测修正）
- **先确认对象身份**（小昭是 WorkBuddy 不是 Codex——搜错地方）
- **查源码确认机制存在**（Hermes smart_model_routing 无实现）
- **2026-08-15 新增：记忆体系自身也是快照**——恢复时以目录内最新为准，不信写死日期（欧阳锋同日独立收敛同一结论）

## 关键数字
- 全库 YAML 100%
- cap_hub 20 Feature（含 FEISHU_DOC_MCP）
- 3 agent 已接 MCP（kdo + feishu_doc）
