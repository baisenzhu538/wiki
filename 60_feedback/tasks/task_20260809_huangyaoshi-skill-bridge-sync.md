---
id: task_20260809_huangyaoshi-skill-bridge-sync
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-09
updated_at: 2026-08-09
priority: P1
claimed_at: 2026-08-09
---

## 执行报告（2026-08-09 黄药师）

### 交付物
1. **`kdo-tools/skill_bridge_sync.py`** — 双轨同步脚本（status / sync --apply / convert 三命令）
2. **17 个缺失 skill 全部补齐**（.claude/skills/ 可发现）
3. **`.claude/skills/README.md`** — 维护纪律文档（事实源声明 + 转换规则 + 纪律 5 条）
4. **cap_hub 登记**：SKILL_BRIDGE_SYNC（16 Feature）；scripts README 登记

### 同步结果（狗粮测试全过）
| 验证项 | 结果 |
|:---|:---|
| status 双轨一致 | shared 70 = .claude 70，缺失 0，漂移 0 |
| body 逐字节对比 | **70/70 一致**（frontmatter 之后部分） |
| 17 缺失补齐 | 17/17 存在且 frontmatter 有效（name/description/allowed-tools） |
| references 同步 | content-production + task-orchestration 两个 references/ 目录 diff 一致 |
| 幂等 | 复跑 sync → "待同步 0" |

### 转换规则（shared Hermes → .claude Claude Code）
- frontmatter：保留 name/version；description 转 `|` 块 + 从 body `## 触发词` 节提取追加；加固定 allowed-tools [Read, Write, Skill, WebSearch]；丢弃 metadata.hermes
- **body 逐字节不变**（只替换 frontmatter）
- references/ 子目录整体复制

### 过程中踩的坑（3 个，均已修复）
1. **校验误报**：read_fm 把列表字段 `allowed-tools` 解析为空串 → 校验判空误报 17 失败。修复：列表字段用"键存在"判断
2. **body 双空行**：新 frontmatter 后 body 开头空行 → diff 显示差异。修复：body.lstrip("\n")
3. **BOM 漂移误报**：shared 部分文件带 BOM（﻿）→ 正则不匹配 → hash 计算整个文件 → 51 个假漂移。修复：读文件先 _strip_bom()。**漂移检测升级为内容 hash（version 相同但 body 不同也检测）**——发现 kdo-self-attack 旧版 2026-06-21 vs 新版 2026-06-27 真漂移后已同步

### 说明
- 任务单背景说"52 个 .claude = shared 69 子集"，实测 53 vs 70（含 README 不计 skill）
- 维护纪律：先改 shared/（事实源）→ 跑 sync；禁止只改 .claude 侧（会被覆盖）

# 双轨 Skill 同步机制（B1）

## 任务目标

解决 .claude/skills 与 40_outputs/capabilities/skills/shared/ 双轨漂移：建立同步机制（脚本/工具），补齐 17 个缺失 skill，保证新 skill 双向可用。

## 背景（探索发现 2026-08-09）

- .claude/skills 52 个 = shared 69 个子集，独立物理副本，**无桥接/同步脚本**（kdo-tools/、scripts/ 均无）
- 格式不同：.claude 用 Claude Code 原生 frontmatter（allowed-tools），shared 用 Hermes 格式（metadata.hermes）
- 版本漂移：kdo-self-attack .claude 版 2026-06-21 vs shared 版 2026-06-27
- **17 个缺失**（只存在于 shared/）：agent-self-iteration（王语嫣最新资产）、self-evolution、six-layer-cross-validation、nine-layer-deep-dig、knowledge-collision、多模态 10 个（beikai-multimodal-pipeline/comfyui-local/cosyvoice-tts/drawio-mcp-diagrams/multi-page-article-capture/presenton-ppt-generator/vlm-image-describe-pipeline/wan-video-generation/visual-asset-analysis/visual-polish）、feishu-publish、pre-ship-check

## 规格

1. 同步方向：shared/ 为事实源，单向复制到 .claude/skills/（含 references/ 子目录）
2. 格式转换：Hermes frontmatter → Claude Code frontmatter（name/version/allowed-tools/description 块字符串），描述保留中文触发词
3. 交付：一个同步脚本（kdo-tools/ 下）+ 首次同步补齐 17 个缺失 + README 说明维护纪律
4. 后续新建 skill 纪律：双写（shared + .claude）或跑脚本

## 验收标准

- 脚本可重复运行，幂等（已同步的跳过）
- 同步后 .claude/skills 与 shared 版本号/内容一致（diff 抽查 5 个）
- 17 个缺失全部补齐，Claude Code 可发现（Skill 工具列表可见 task-orchestration/agent-self-iteration 等）
- 无死链（references 同步）

## 边界

- 不修改 shared/ 内容本身（只复制+格式转换）
- 不处理 skill 内容质量（那是 B4 审计任务）

## 终审记录（2026-08-09 欧阳锋）

**verdict: PASS A · blocking: 无 · methodology v2.2**

O3 独立验证全部通过：
1. status 实跑：shared 70 = .claude 70、缺失 0、漂移 0（与报告逐字一致）
2. 幂等实跑：复跑 sync → "待同步 0（缺失 0 + 漂移 0 + references 缺失 0）"
3. 17 缺失抽查 6/6 存在（agent-self-iteration/six-layer-cross-validation/nine-layer-deep-dig/self-evolution/knowledge-collision/pre-ship-check）
4. references diff 一致（content-production + task-orchestration，空输出）
5. body 逐字节抽查 3/3 一致（kdo-self-attack/task-orchestration/agent-self-iteration——含报告所述真漂移的 kdo-self-attack，确认已修复）
6. README 维护纪律文档齐全（事实源声明 + 命令 + 纪律 5 条）+ cap_hub SKILL_BRIDGE_SYNC 登记 + scripts README

亮点：漂移检测升级为**内容 hash**（version 相同但 body 不同也抓）——对"版本漂移"问题的根治性方案，且抓出 kdo-self-attack 真漂移后已修复；3 个坑（校验误报/双空行/BOM 漂移）如实记录，BOM 问题修在最险处（51 个假漂移 → 内容 hash）。报告数字全部可独立复现。

五维：溯源 95/逻辑 95/暗知识 85/可操作 95/表达 90 → 总分 93（A）
