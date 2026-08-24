---
id: 512
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-24T19:15:28.468694+00:00'
version: v0.2
instance: huangyaoshi
code_files:
- kdo-tools/daily-context-save.py
- kdo-tools/tests/test_daily_context_save.py
- 90_control/infrastructure-inventory.md
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

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：重打改覆盖写 + 存量 47 文件清理——①根因定位：cmd_save 本身 write_text 覆盖，但 `--file` 重打时把上次 save 产物（含 frontmatter+标题）原样包进新 frontmatter → 层叠；修复=新增 `_strip_existing_layers()`（循环剥 frontmatter 层+save 生成格式标题行，Truman 内容标题带后缀不匹配不误伤），重打=剥层后套新层=替换；②事件刷屏治理：`_write_l0_event` 去重签名改基于正文（剥层后 hash——重打只变 frontmatter 时间戳时签名不变，同内容重打不刷屏；正文真实变化正常留新事件）；③存量清理：全量扫描实测 **47 个多层文件**（2-30 层，远超审计 4 样本——申报范围已用户确认），保留最外层（实测时间戳证明最新层在最外，laowantong 15:31:44>15:31:05>15:30:00）+剥内层+重算 content_hash/updated_at；清单 NUL 分隔 UTF-8 + apply 后逐行复核 47/47（存在性/单层/yaml.safe_load）；agent复盘仓 path-scoped commit `a29c2d9` by huangyaoshi（该仓其他角色在制品文件未触碰）。

**交付物**：
- `kdo-tools/daily-context-save.py`（_strip_existing_layers + 事件去重签名）
- `kdo-tools/tests/test_daily_context_save.py`（新：4 例回归）
- 存量清理：agent复盘仓 47 文件（commit a29c2d9）+ 清理脚本 `_tmp/512_clean_multilayer.py` + 复核清单 `_tmp/512_multilayer_files.nul` / `_tmp/512_cleanup_result.json`
- `90_control/infrastructure-inventory.md`（daily-context-save 行更新）

**验证**：
- L1：`cd kdo-tools && python -m pytest tests/ -q` → **94 passed**（新增 4 例：重打单层覆盖/三层剥层保 Truman 标题/同内容重打 1 事件/内容变化重打 2 事件）
- L2 狗粮：laowantong 2026-08-24-hermes.md 清理后 yaml.safe_load 单层 dict 解析 ✅、session_id=laowantong-2026-08-24-hermes ✅、content_hash 在 ✅；与 git 历史版 diff 逐行核——删除行除 frontmatter 字段/标题行/空行外**零正文删除**；apply 后 47/47 复核通过
- L3 待活体：下次复盘打回重打，文件不再堆层、事件库不再 6 分钟 8 条（同内容重打零事件）

**边界**：只改重打语义与事件去重签名，自检门禁规则未动；存量清理限多层 frontmatter 文件（47 个全在 daily-context/，正常复盘未动）；content_hash/updated_at 重算=清理动作本身目的（元数据失真修复，已在用户确认的范围声明中）；agent复盘仓其他角色未提交的 in-progress 文件（技能进化日志等）未纳入 commit；#369 手改检测对清理后文件的 git_head 为历史值（最后一次 save 的 HEAD——保留未动，如欧阳锋要求可全量刷新但会制造元数据噪声）。

**需要谁动作**：欧阳锋终审本单；各角色知悉——重打复盘现在=覆盖写（旧文件直接 --file 重打即可，不再堆层）；风清扬复核清理后文件 YAML 元数据与事件库 grade 对齐。
