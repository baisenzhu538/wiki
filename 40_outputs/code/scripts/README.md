# KDO 可复用脚本索引

> 本目录存放经洪七公（Multimodal Arbiter）验证的可复用脚本。  
> 处理多媒体任务前，先查本索引，避免重复造轮子。  
> 详细选型指南见：`40_outputs/capabilities/skills/image-understanding-pipeline/SKILL.md`

---

## 图像识别与理解

### `ocr-images-easyocr.py`
- **功能**：批量 OCR 图片中的中文/英文文字
- **输出**：每张图 `${stem}.md` + `${stem}.json` + `README.md`
- **使用场景**：PaddleOCR 失败时的本地 fallback
- **依赖**：WSL + Python + easyocr
- **运行**：
  ```bash
  python3 40_outputs/code/scripts/ocr-images-easyocr.py \
    -i "00_inbox/某个目录" \
    -o "00_inbox/某个目录"
  ```

### `describe-images-minimax.py`
- **功能**：用 MiniMax-M3 VLM 批量生成图片的结构化描述
- **输出**：每张图 `${stem}_vlm_desc.md` + `README-VLM描述汇总.md`
- **使用场景**：需要理解画面语义、风格、用途时
- **依赖**：MiniMax API key（格式 `sk-api-...`）
- **运行**：
  ```bash
  export MINIMAX_API_KEY=你的key
  python3 40_outputs/code/scripts/describe-images-minimax.py \
    -i "00_inbox/某个目录" \
    -o "00_inbox/某个目录"
  ```

### `describe-images-siliconflow.py`
- **功能**：用 SiliconFlow Qwen-VL 批量生成图片的结构化描述
- **输出**：同 MiniMax 版本
- **使用场景**：MiniMax 不可用时的备选
- **依赖**：SiliconFlow API key（格式 `sk-...`）
- **运行**：
  ```bash
  export SILICONFLOW_API_KEY=你的key
  python3 40_outputs/code/scripts/describe-images-siliconflow.py \
    -i "00_inbox/某个目录" \
    -o "00_inbox/某个目录"
  ```

---

### `batch-ocr-long-image-windows.py`（Windows 场推荐 · 2026-08-16 登记）

- **功能**：长图/截图批量 OCR+VLM（MiniMax-M3，自动切 600px 段+30px 重叠，断点续跑）
- **输出**：每张图 `OCR_{文件名}.md` 直落素材目录（Obsidian 可见）
- **使用场景**：Windows 场批量图片识别（WSL/Hermes 场用 long-image-ocr skill 原版脚本）
- **依赖**：`wiki/.env` 的 MINIMAX_API_KEY（经 `cap_hub/config.py` 加载，零配置）+ PIL
- **运行**：
  ```bash
  python 40_outputs/code/scripts/batch-ocr-long-image-windows.py "00_inbox/某个目录" \
    --context-file 术语上下文.md   # 可选：注入术语表防误读，自带 E025 禁令
  ```
- **备注**：配套 skill 卡 `40_outputs/capabilities/skills/long-image-ocr/SKILL.md`（v2.1，含流程纪律 10 条+坑位表）；实战样本 `00_inbox/爆炸式调研/`（47 图 173 段零失败）、`00_inbox/AI知识库/`（25 图 42 段零失败）。注意：prompt/上下文变更后需作废旧 OCR 输出再续跑（断点续跑不区分 prompt 版本）。

---

## 图像生成

### `generate-images-minimax.py`（推荐 · 国内可直接支付）
- **功能**：用 MiniMax Image-01 国内 API 文生图
- **输出**：指定路径图片 + `*_metadata.json`
- **使用场景**：需要批量生成封面/海报/信息图，且 fal.ai 无法充值时
- **依赖**：MiniMax API key（与 VLM 共用同一个 key）
- **运行**：
  ```bash
  export MINIMAX_API_KEY=你的key
  python3 40_outputs/code/scripts/generate-images-minimax.py \
    -p "一张极简商务风格的信息图，主题是科学决策" \
    -o "40_outputs/content/images/generative/test.png" \
    -r 16:9
  ```
- **备注**：`MINIMAX_API_KEY` 与 `describe-images-minimax.py` 相同；支持 16:9 / 1:1 / 3:4 / 21:9 等比例，可选画风参数 `--style`。

### `generate-images-fal.py`
- **功能**：用 fal.ai FLUX 把文章标题转成封面图
- **输出**：`40_outputs/content/images/generative/`
- **使用场景**：需要批量生成文章封面/信息图
- **依赖**：fal.ai API key（注意：当前账户余额不足，需充值）
- **状态**：余额耗尽，已降级为备用方案

---

## 文档解析

### `download-mineru-models.sh`（WSL）
- **功能**：下载 MinerU 所需模型权重
- **使用场景**：WSL 首次部署 MinerU
- **依赖**：WSL + Python + modelscope

> MinerU 主命令是 `magic-pdf`，不是本脚本。配置详见 `document-parsing-toolkit` skill。

---

## 本地已部署工具（不在本目录）

| 工具 | 位置 | 用途 |
|---|---|---|
| PaddleOCR v5 | `C:\Users\Administrator\ocr-pipeline\` | 本地批量 OCR（node.js） |
| MinerU | WSL `/home/dministrator/.local/bin/magic-pdf` | PDF/复杂图文解析 |
| Marp | 全局安装 | Markdown → 幻灯片 PDF |
| edge-tts | Windows Python | 文本 → 播客/配音 MP3 |

---

## 使用原则

1. **先查索引再动手**：本 README 和 `image-understanding-pipeline` skill 是首选入口
2. **优先用本地已部署工具**：PaddleOCR、MinerU、edge-tts 都已配好
3. **云端工具需确认 key 状态**：fal.ai 当前余额不足，MiniMax/SiliconFlow 需确认额度
4. **输出放原图目录**：便于其他 agent 发现和复用

---

## 维护记录

- 2026-06-19：洪七公创建本索引，汇总图像识别/理解/生成相关脚本。


## Feature 周期表查询

### `kdo-tools/feature_menu.py`
- **功能**：从 周期表 Feature 中按层级/维度/场景过滤点菜 + **#272 新鲜度 SLA（stale 检查）**
- **命令**：`python kdo-tools/feature_menu.py list|query|pick|info|stale`
- **使用场景**：#251 Agent 部署的数据源 / 消费端协议试点 / 老顽童 W1 生产点菜 / #272 认证到期检查
- **运行**：
  ```bash
  python kdo-tools/feature_menu.py list                    # 全量 Feature
  python kdo-tools/feature_menu.py query --layer L2        # 按层级过滤
  python kdo-tools/feature_menu.py query --dimension A     # 按维度过滤
  python kdo-tools/feature_menu.py pick --n 5 --seed 42    # 随机点菜（可复现）
  python kdo-tools/feature_menu.py info F001               # 单 Feature 详情（含认证日期/复审期限）
  python kdo-tools/feature_menu.py stale                   # #272 超期未复验检查
  ```
- **登记日期**：2026-08-08（#272 扩展 2026-08-09）

## Skill 生命周期管理

### `kdo-tools/skill_lifecycle.py`
- **功能**：Skill draft→published→deprecated 三态管理 + eval 门禁（能力 eval / 回归 eval / baseline 对比）
- **命令**：`python kdo-tools/skill_lifecycle.py list|status|set|eval|stats`
- **使用场景**：#267 Skill 生命周期化 / 季度 skill 体检清理 / 交欧阳锋审查前的 skill 状态标注
- **运行**：
  ```bash
  python kdo-tools/skill_lifecycle.py list                          # 全量状态一览
  python kdo-tools/skill_lifecycle.py status <skill>                # 单 skill 状态
  python kdo-tools/skill_lifecycle.py set <skill> --status published --owner <who> --version 1.0.0 [--apply]  # 改状态（默认 dry-run）
  python kdo-tools/skill_lifecycle.py eval <skill> [--apply]        # 能力+回归+baseline eval（默认 dry-run）
  python kdo-tools/skill_lifecycle.py stats                         # 生命周期统计
  ```
- **数据源**：`40_outputs/capabilities/skills/*/SKILL.md` frontmatter（唯一真相，set 带 round-trip 校验）
- **登记日期**：2026-08-09

## Lint 审查基建 R1 四类规则（#271）

### `kdo lint` 内置（kdo/workspace.py）
- **功能**：欧阳锋人工 grep 的三类结构问题固化为 lint 规则（E009/E012 实证）
- **命令**：`kdo lint` 直接输出（无单独入口）
- **规则**：
  - R1-a：`status: reviewed` 缺 `reviewed_by`/`review_date` → **ERROR**（E012 三批 19 张）
  - R1-b：重复节名（两个 `## Critique`）→ **ERROR**（E009 #214）
  - R1-c：source_refs 指向仓库外（桌面等）→ **WARNING**（08-07 复盘）
  - R1-d：source_refs 行号超源文件总行数 → **WARNING**（#213/#250 旧行号）
- **基线**：`60_feedback/diagnosis/baseline_20260809_huangyaoshi-lint-r1.md`（R1-a 461 / R1-b 37 / R1-c 10 / R1-d 0）
- **登记日期**：2026-08-09

## 双轨 Skill 同步（#267）

### `kdo-tools/skill_bridge_sync.py`
- **功能**：shared/（Hermes 事实源）→ .claude/skills/（Claude Code 格式）单向同步——frontmatter 格式转换 + 内容 hash 漂移检测 + references 子目录同步
- **命令**：`python kdo-tools/skill_bridge_sync.py status|sync [--apply]|convert <skill>`
- **使用场景**：新建/修改 skill 后同步双轨；季度检查双轨一致性
- **运行**：
  ```bash
  python kdo-tools/skill_bridge_sync.py status          # 差异总览（缺失/漂移）
  python kdo-tools/skill_bridge_sync.py sync --apply    # 同步（幂等）
  ```
- **维护纪律**：见 `.claude/skills/README.md`——先改 shared/，再跑 sync
- **登记日期**：2026-08-09

## 经验→技能自动结晶（#279）

### `kdo-tools/skill_crystallize.py`
- **功能**：jarvis 模式——扫描错误模式库/技能进化日志/复盘，同主题出现 ≥2 次 → draft skill 候选（**不自动 publish**，人审后走 skill_lifecycle）
- **命令**：`python kdo-tools/skill_crystallize.py scan [--min-count N] [--apply] | list`
- **使用场景**：#279 经验结晶——把"重复出现的有效做法"从复盘文本变成可复用 skill
- **运行**：
  ```bash
  python kdo-tools/skill_crystallize.py scan              # dry-run 预览候选
  python kdo-tools/skill_crystallize.py scan --apply      # 生成 draft 候选（crystallized-candidates/ + crystallized-*/）
  python kdo-tools/skill_crystallize.py list              # 列出已结晶候选
  # 人审发布：python kdo-tools/skill_lifecycle.py set crystallized-<name> --status published --apply
  ```
- **登记日期**：2026-08-09

## 决策记录模板化（#275）

### `kdo-tools/decision_add.py`
- **功能**：decisions.md 新条目模板化（D1-D4 分类 + claim-state + D4 批准人强制）
- **命令**：`python kdo-tools/decision_add.py add "标题" --type D1|D2|D3|D4 --claim observed|attested [--approver 王语嫣] [--dry-run]`
- **使用场景**：#275 决策分类机制化——D4 自我修改（Agent 改自己 context/skill/配置）必须批准人
- **运行**：
  ```bash
  python kdo-tools/decision_add.py template                       # 打印模板
  python kdo-tools/decision_add.py add "建新域" --type D3 --claim observed
  python kdo-tools/decision_add.py add "改铁律" --type D4 --claim attested --approver 王语嫣
  ```
- **登记日期**：2026-08-09

## 看板终审评级显示（2026-08-09 欧阳锋增量）

### `kdo-tools/generate-dashboard.py`
- **功能**：生产看板 dashboard.html 生成——待领取/审查中/进行中/已完成四组
- **2026-08-09 增量**：① 已完成组渲染有终审等级的任务卡片（此前只显示统计数字不渲染卡片）② 等级徽章：从队列注释列解析 `PASS A/A-/B+/C`（含条件 PASS ⚠ 标记），A 绿 / B+ 黄 / C·FAIL 红
- **命令**：`PYTHONIOENCODING=utf-8 python kdo-tools/generate-dashboard.py`（GBK 终端需 UTF-8 前缀，否则 print ✅ 崩溃）
