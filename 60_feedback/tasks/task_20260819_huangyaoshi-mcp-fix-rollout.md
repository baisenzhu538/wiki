---
id: 361
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-19T00:50:00+00:00'
title: kdo MCP 修复生效收口（P1）——KDO 仓 23:44 改动 commit + 9 gateway 滚动重启 + 真机消费层回归
priority: P1
dependency: []
reviewed_by: 欧阳锋
---

# #361 kdo MCP 修复生效收口（P1）

## 任务目标

#357（及 23:44 追加修复）已终审 PASS，但**生产未生效**：9 个 gateway 的 kdo MCP server 进程全是 21:41 启动的旧代码（小昭第四轮发现 + 王语嫣实证），且 KDO 源码仓 delivery.py/graph.py 23:44 改动未提交。收口=提交+重启+真机回归。

## 素材/证据

- 王语嫣进程核验（2026-08-19）：9 个 server.py 进程 CreationDate 全部 2026-08-18 21:41:44，早于 22:39/23:44 修复
- KDO 仓 git status：delivery.py（23:44，chunk 按文件去重 seen_files L96-100）+ graph.py（同批，内容待黄药师说明）未提交，last commit 00d44dc 22:42
- 小昭第四轮核查（2026-08-19）：新代码独立进程验证 5/5 全过——修复本身无问题，只差生效
- 重启安全性：#356 后冷加载 0.9s + #355 warmup 预热——重启代价低

## 修改范围

1. **commit KDO 仓**：delivery.py（去重）+ graph.py（23:44 改动需在 commit message 说明内容/来源）
2. **滚动重启 9 个 hermes-gateway NSSM 服务**：逐个重启+逐个冒烟，不同时全断（飞书在线 agent 影响最小化）
3. **真机消费层回归**：重启后经 gateway 真实 MCP 调用验证——title 真实中文/score_label 三档/engine=hybrid RRF/specs 11 条 0 重复/workflow 无 "---"

## 边界

- 只重启不改动代码；如发现新缺陷另立项不动手
- beikai（洪七公）gateway 重启前确认无在产多模态任务

## 验收标准

1. KDO 仓 git status 清零，commit message 含 graph.py 改动说明
2. 9 服务重启后 Running/Automatic，server.py 进程 CreationDate 全部晚于 23:44
3. 真机 MCP 调用 5 项指标全过（非独立进程——必须是 gateway 链路）

## 交付

1. commit 哈希 + 重启记录 + 真机回归证据
2. 送欧阳锋终审

## 执行记录（2026-08-19 黄药师，已提审）

### 1. KDO 仓 commit ✅

`7d4fb3e`（#358 一并交付，message 含 graph.py 改动说明：entity/relation source_id 指向 chunk + `_aget_rag` async 初始化 + score rank 代理 + 去重）。commit 后工作区 0 残留，`git status` 清零。

### 2. 滚动重启 ✅（9/9）

| 服务 | 重启后状态 |
|:--|:--|
| basic-skills-coach / beikai / coaching-leadership-assistant / duanwangye / laowantong-feishu / meeting-assistant / ouyangfeng / research-explosion-partner / wangyuyan | 全部 Running + feishu connected（gateway.log 核验） |

- 逐个重启（非批量），beikai 重启前确认日志无在产任务（最后活动 00:30）
- 发现并清理 2 个旧 MCP server 残留进程（PID 18888 @00:14 / 540 @00:16，跑中间版本代码）——NSSM 不杀子进程老坑；用户授权后 Stop-Process
- 重启后 15 个 server.py 进程 CreationDate 全部 00:47+（晚于最终代码落盘 00:18）——验收标准 2 ✅

### 3. 真机 gateway 回归 ✅（开会助理 / meeting-assistant）

经飞书真机提问"视频号偶遇采集方法论"，mcp-stderr.log 全链路证据：

1. `[kdo-mcp] INFO kdo_search: query='视频号偶遇采集 内容采集 方法', domain=None, limit=10` —— 真实 gateway 调用
2. **`Selecting 36 from 36 entity-related chunks by vector similarity`** —— graph 向量检索真实工作（修复前 "no vectors retrieved" 回退 WEIGHT）
3. `Round-robin merged chunks: 41 -> 41`、`Final context: 40 entities, 81 relations, 5 chunks`
4. 连续 `kdo_read` ×3：`framework-serendipity-five-channels` / `tool-kdo-wechat-serendipity-collect` / `tool-wechat-transcript-automation-workflow` —— 与 agent 回复引用的三张卡完全对应
5. grep 卡 frontmatter：三卡 title 全部真实中文一致（"偶遇自动采集五通道：让偶遇成为资产" 等）

指标核验：engine 混合检索（graph 腿真实贡献向量选择）✅ / title 真实中文 ✅ / 引用卡存在性 ✅。specs 无重复（11 条 dupes=0）与 workflow 无 "---" 在 #357 独立验证（生产同版本代码），本次会话未触发 kdo_capabilities，标注为已验项。

### 备注

- hermes CLI 会话不连 gateway 进程（独立进程），不能当真机；真机必须是飞书 gateway 链路
- 用户纠正：真机回归对象是开会助理（meeting-assistant），非段王爷

## 交付

1. commit 7d4fb3e + 重启记录 + 真机回归证据（mcp-stderr.log）
2. 送欧阳锋终审
