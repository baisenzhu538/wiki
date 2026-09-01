---
title: vault 观感崩坏三症联诊：重复源文件散点 + Obsidian 配置全丢 + 采集链疑似中断
author: huangyaoshi
created_at: 2026-09-02
type: diagnosis
status: pending_review
trigger: 老朱 09-02 凌晨报三症：Obsidian 大量散点 / 图谱点全变黑 / 偶遇采集链全部断掉
---

# 建议书：vault 观感崩坏三症联诊（散点 / 黑点 / 断链）

## 一、结论速览（TL;DR）

| 症状 | 真实根因 | 严重度 |
|:--|:--|:--|
| Obsidian 大量散点 | `wechat_promote.py:59` 去重 bug：文件名带当天日期，每天全量重入库，17 篇素材累积 **146 份字节级重复**孤儿笔记 | 🔴 每天 +14 散点，持续恶化中 |
| 图谱点全变黑 | **08-31 02:00 事故的附带损失**：`.obsidian/` 整目录被删（git 不跟踪 → 王语嫣手工恢复带不回来），Obsidian 重建默认配置，colorGroups 清空、4 个插件全丢 | 🟠 已部分恢复（见下），配色原件不可恢复 |
| 采集链"全部断掉" | **误诊——链是活的，是没料了**。老朱最后一次转链接 = 08-31 20:04，之后 29h 零输入，监控每 10 分钟空转 | 🟢 无需修，但暴露一个真 bug（死循环重试） |

## 二、实证（每条可复跑）

### 症状 1：散点 = 146 份重复源文件

- `10_raw/sources/` 下 `src_2026-<日期>_wechat_<hash>.md`：同一 hash 出现 9-12 次（08-19 起每天一份），共 163 份 / 17 篇唯一素材
- 逐字节 diff 验证：08-31 与 09-02 同名 hash 文件内容 IDENTICAL
- 根因定位 `kdo-tools/wechat_promote.py:59-60`：
  ```python
  target = SOURCES_DIR / f"src_{date.today().isoformat()}_wechat_{hash_id}.md"
  if target.exists():  # ← 明天日期变了，exists 永远 False → 全量重拷
  ```
- 引用约束（清理红线）：`30_wiki` 有两处引用了**特定日期版**文件名（`src_2026-08-19_wechat_e7536…`、`src_2026-08-20_wechat_2404c…`），清理时必须保住被引用版本

### 症状 2：`.obsidian` 配置整体被抹

- 现状：`.obsidian/` 只剩 5 个 json，全部 09-02 01:03 重新生成；`app.json`/`appearance.json` 为 2 字节 `{}`；`plugins/` 目录整个不存在
- git 历史证明原配置含 4 插件（claudian 2.0.10 / dataview / obsidian-excalidraw / obsidian-git）+ templates.json + 自定义 colorGroups
- 时间线归责：08-31 02:00 事故删除序列含工作树顶层（见 `60_feedback/tasks/report_20260901_huangyaoshi-vault-incident-rootcause.md`），`.obsidian` 自 05-02 起不在 git 跟踪（ab2bd33ba），恢复 commit 时带不回来 → 之后某次打开 Obsidian 静默重建默认配置
- 备份面穷尽核查：坚果云沙箱清单无 wiki（41393 条事件镜像 0 命中）、VSS 最新 05-15、File History 未启用、每日 bundle 只含 git 跟踪文件——**`.obsidian` 是全厂备份盲区，本次实锤**
- 已恢复：plugins 四件 + community-plugins/core-plugins/templates/appearance 从 `ab2bd33ba^` 恢复；colorGroups 无备份（git 里仅 5 月版 1 条规则），已按目录职能重配 9 条（30_wiki 红沿用原色），老朱拍板"配色不用管"即定稿

### 症状 3：采集链体检（亲跑，非推断）

| 环节 | 实测 | 证据 |
|:--|:--|:--|
| 计划任务 wechat-link-monitor | ✅ 每 10min 在跑，result 0 | schtasks 全量表 |
| 微信库解密 + 链接提取 | ✅ 正常 | 手动跑一轮：解密成功，扫到 10 条链接 |
| LLM 知识化（DeepSeek v4-flash） | ✅ 正常 | 实测调用返回三层次输出（402 已解除） |
| parse_sph 服务（127.0.0.1:2022） | 🟡 进程活着 HTTP 200，真实解析未实证（无新链接可测；元宝 Cookie 08-17 配，有效期约 1 个月） | curl 实测 |
| 最后真实输入 | 08-31 20:04 两条头条视频 → 当晚 22:10 转写、23:25 出卡，全链跑通 | filehelper 解密库 + 产物 mtime |

- **附带真 bug**：08-31 00:14 的 3 条 `t=pages/image_detail` 图片分享链接——非文章页永远抓不到正文，但脚本"失败不记 seen"，已**每 10 分钟重试、循环失败 ~29 小时**

### 附带散点清单（同批清理）

- `60_feedback/inbox-queue/dispatch_*.md` 49 份残留（含 08-31 state 重建洪水 10 份；SOFT_CAP 修复已上线，存量待归档）
- vault 根目录 `_tmp_oyp_brief.txt` / `_tmp_oyp_review.py` / `_tmp_skill_health.json`；`kdo-tools/tmp_*` 一次性脚本 18 个；空目录 `C/`
- `__pycache__` / `.search_cache` 未入 .gitignore
- 更正前判：`60_feedback/wechat-collect/*.mp4` 是管线设计内 WORK_DIR 产物，**非错放，不动**

## 三、方案（待裁定后执行）

| # | 动作 | 归属建议 |
|:--|:--|:--|
| 1 | 修 `wechat_promote.py`：去重改按 hash 全局 glob（`src_*_wechat_<hash>.md`），不再带日期 | 黄药师，基建单 |
| 2 | 清 146 份重复源文件：按 hash 分组，保被引用版/最早版，dry-run 清单先行（P-30 纪律：声明范围+完整路径清单） | 黄药师 |
| 3 | 修 image_detail 死循环：识别该类型直接 mark_seen 跳过 | 随 #1 同单 |
| 4 | dispatch 49 份迁 `inbox-queue/archive/`；tmp/杂项清理；补 .gitignore | 黄药师 |
| 5 | 清完后 `kdo index --rebuild` 消检索层污染 | 黄药师 |
| 6 | **备份盲区堵口**：`.obsidian/`（至少 graph.json/community-plugins.json/插件 data.json）纳入每日 02:30 bundle 或独立快照——本次配置全丢零兜底，是这个盲区的第一次实爆 | 黄药师，需欧阳锋终审方案 |
| 7 | 采集链不改代码，建议老朱随手转一条链接做端到端活体验证（顺便实证 parse_sph Cookie 有效性） | 老朱动作 |

## 四、待王语嫣裁定项

1. 是否立项为基建单（建议合并为 1 单：#1-#5 修复清理包 + #6 备份方案分开）
2. 146 份重复文件处置口径：直接删（git 有历史兜底）还是移 `_archive/`
3. 配色方案已定稿不重议（老朱 09-02 口径"配色不用管"），仅备案

## 五、元教训（供方法论沉淀）

- **症状群≠事故群**：三个症状两个根因（promote bug 累积 + 08-31 事故附带损失），第三个是误判。分症归因比统一归因重要
- **不跟踪的配置 = 事实上的易失品**：`.obsidian` 05-02 移出 git 时没人补备份机制，4 个月后实爆。任何"移出版本控制"的动作都应强制回答"那它归谁备份"
- **"失败不记 seen"策略需要类型白名单兜底**：对所有失败一律重试 = 对永久性失败（不支持的类型）制造死循环
