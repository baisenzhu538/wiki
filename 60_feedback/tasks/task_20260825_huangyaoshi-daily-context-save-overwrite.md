---
id: 512
assignee: huangyaoshi
status: queued
updated_at: '2026-08-24T16:20:00+00:00'
version: v0.1
---

# #512 daily-context-save 重打改覆盖写 + 存量多层 frontmatter 清理

- **任务号**：#512
- **状态**：queued
- **assignee**：huangyaoshi（复盘保存脚本修复+存量清理；欧阳锋终审）
- **优先级**：P1（元数据层失真中——3 角色 4 文件实测多层堆叠，事件库 grade 与文件头对不上）
- **立项**：2026-08-25 王语嫣（风清扬晚间审计 `diag_20260824_fengqingyang-l1-l2-evening-audit.md` F1 裁定采纳）

## 背景

`daily-context-save.py` 自检打回重打时**追加而非覆盖** → 复盘文件多层 frontmatter 堆叠（实测：laowantong/2026-08-24-hermes.md 三层+三标题串联；huangyaoshi/duanwangye 08-24 各两层）。YAML 解析只认第一层 → 审计/索引/事件登记元数据全部失真（事件库 grade 记最后一层，文件头是第一层）。连带：事件层被重打刷屏（老顽童同一文件 6 分钟 8 条 review_saved）。自检门禁本身在工作（C→A 收敛，正向），但首次通过率低。

## 任务

1. `kdo-tools/daily-context-save.py` 重打改**覆盖写**（同 agent 同日同文件重打=替换，不追加）
2. 存量多层堆叠文件一次性清理：保留末层完整内容（最新自检通过版），逐文件清理前列清单+逐条确认（中文文件名铁律：清单 NUL 分隔 UTF-8，apply 后 Path.exists() 逐行复核）
3. 回归用例：构造重打场景 → 文件只有一层 frontmatter；事件库不重复刷条

## 验证（验证分层）

- L1：单测——重打=覆盖；存量清理 dry-run 清单与实际变更新旧对照
- L2 狗粮：拿 laowantong 2026-08-24-hermes.md 实测清理后 YAML 解析 grade 与内容一致
- L3 待活体：下次复盘打回重打，事件库不再 6 分钟 8 条

## 边界

- 只改重打语义（追加→覆盖），不改自检门禁规则本身（C→A 收敛逻辑保留）
- 存量清理限多层 frontmatter 文件，不动正常复盘文件
- 覆盖写要先留 git 历史兜底（复盘在 agent复盘 独立仓，#430 已 git 化——清理前先确认该仓 HEAD 干净）

## 关联

- 风清扬晚间审计 F1（含实测文件清单与根因）
- #430（agent复盘 git 化——覆盖写前的安全网）/ E044（Edit 大块替换未读回同族）
- F-041（事件层扩展钩子；本单顺带治事件刷屏）

## 需要谁动作

- **黄药师**：脚本修复 + 存量清理（先清单后动手）
- **欧阳锋**：终审本单
