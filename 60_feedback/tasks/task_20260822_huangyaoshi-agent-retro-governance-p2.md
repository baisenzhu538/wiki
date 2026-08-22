---
id: 424
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-22T15:17:27.564346+00:00'
---
# #424 agent复盘 治理 P2（T7 归档结构统一 + T9 目录白名单固化）

- **任务号**：#424
- **状态**：queued
- **assignee**：huangyaoshi（T9 规则文案王语嫣审）
- **优先级**：P2
- **依赖**：#418/#422（归并完成后统一结构）
- **立项**：2026-08-22 王语嫣（风清扬审计 T7/T9，T8 已并入 #422）

## 范围

- **T7**：各拼音目录 `cn-track-archive-20260819` 归档结构统一（README+每日复盘+五件套），补齐缺失 README
- **T9 命名铁律目录级固化**：`agent复盘/README` 或 90_control/AGENTS.md 固化目录白名单——只允许角色拼音+助理中文名；工具名目录清零后的拦截规则（新目录违规有提醒）

## 验收

- 6 个 archive 结构一致（清单对比输出）
- 白名单规则落盘+引用位置登记
- 欧阳锋终审；commit 入档

## 内容价值判断（#375 处置门禁补充节，2026-08-22 黄药师领取时补）

- **本任务为结构治理**：archive 目录补 README + 白名单规则落盘——**只增不删**（补文档/建 README），无素材处置动作
- 不移动、不删除任何既有文件；archive 结构统一=对比清单+补缺 README
- 白名单规则为文档固化，不触发任何删除

## 执行报告（2026-08-22 黄药师）

**T7 归档结构统一**：
- 5 个 `cn-track-archive-20260819` 目录结构对比清单（附输出）：duanwangye（README+五件套+模板）/hongqigong（同）/huangyaoshi（README 已补+历史资产 3）/laowantong（README 已补+复盘 4）/ouyangfeng（README+每日复盘系列）
- 补齐缺失 README 2 份：`huangyaoshi/cn-track-archive-20260819/README.md`（历史资产说明：架构提案/能力复盘/技能萃取设计）+ `laowantong/cn-track-archive-20260819/README.md`（复盘历史索引）——统一后 5 个 archive 全有 README，只增不删
- wangyuyan/fengqingyang/codex 无旧轨历史故无 archive（拼音轨直接现行），已在对比清单注明

**T9 目录白名单固化**：
- 新建 `agent复盘/README.md`：白名单（角色拼音 8 + 助理中文名 4 + _archive 归档区 + 中文旧轨 DEPRECATED 观察期）；禁止项=工具名目录清零后禁止重建（#422 T5 模式）；新目录违规提醒规则落盘
- 规则文案待王语嫣审（任务单 assignee 注明）

**验收对照**：archive 结构一致（清单对比输出 ✅）/ 白名单规则落盘+引用位置登记（agent复盘/README.md，角色 context 启动步骤引用处待王语嫣决定是否加指针）/ commit 入档

**边界**：只增不删；未移动任何既有文件；PROTOCOL §7 零触碰
