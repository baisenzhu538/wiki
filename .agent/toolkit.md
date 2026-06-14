# 本地武器库

**任何欧阳锋 session 启动时必须读这个文件**。这里是已经部署好的、可以直接调用的本地工具和能力。不要重新调研、不要重新造轮子——先查这里。

---

## 一、OCR / 图片文字提取

### 首选：PaddleOCR v5（已部署，纯本地）

| 方式 | 命令 | 适用 |
|------|------|------|
| Node.js 直接 | `node C:\Users\Administrator\ocr-pipeline\ocr-paddle.cjs <image>` | 单张，最快 |
| PowerShell 单张 | `powershell 40_outputs/capabilities/skills/image-ocr/ocr-image.ps1 <image>` | 单张，PowerShell 环境 |
| PowerShell 批量 | `powershell 40_outputs/capabilities/skills/image-ocr/ocr-image.ps1 "*.png" -Batch` | 批量处理 |

输出：同目录下生成 `*_paddle_ocr.txt`

> **位置**：`C:\Users\Administrator\ocr-pipeline\`（models ~20MB + node_modules ~670MB，不进 git）
> **教训**：dict 索引不能 filter 空行
> **参见**：`40_outputs/capabilities/skills/image-ocr/SKILL.md`

### 素材预处理铁律

新域素材消化第一步：扫描文件夹 → 如有 PNG/JPG，**强制 OCR 全部后再读文本**。不要相信任何人说"没有图片需要 OCR"——独立验证。

---

## 二、KDO CLI 完整速查

### 知识管线

| 命令 | 用途 |
|------|------|
| `kdo init [path]` | 初始化 KDO 工作空间 |
| `kdo capture <input> [--title] [--kind]` | 捕获文本/URL/文件到 00_inbox |
| `kdo fetch-url <url> [--title] [--timeout]` | 抓取 URL 并提取文本到 00_inbox/links |
| `kdo import-chat <path> [--title] [--format]` | 导入 AI 对话到 00_inbox/ai-chats |
| `kdo ingest [--limit N] [--dry-run]` | 编译 inbox → raw sources + wiki 骨架 |
| `kdo enrich [--wiki-path] [--all] [--dry-run]` | 自动填充 wiki 骨架中的 TODO 占位 |
| `kdo query <question> [--limit N]` | 语义+图检索（LightRAG），回退到 BM25 → 关键词 |
| `kdo produce <content\|code\|capability>/<subtype> --topic <topic>` | 创建 artifact 骨架到 40_outputs |
| `kdo validate [artifact_id] [--advisory] [--write-report]` | 按质量门校验 artifact |
| `kdo ship <artifact_id> --channel <channel> [--url]` | 记录交付事件到 50_delivery |
| `kdo feedback <text> [--kind] [--artifact-id]` | 记录反馈信号到 60_feedback |
| `kdo improve [--output] [--print] [--apply]` | 从反馈生成改进计划到 30_wiki/decisions |
| `kdo brief --topic <topic> \| --artifact-id <id>` | 生成交接简报纸到 50_delivery/briefs |

### Graph RAG

| 命令 | 用途 |
|------|------|
| `kdo graph rebuild` | 重建 Graph RAG 索引（内容变更后运行） |
| `kdo graph query <question> [--json]` | 直接查 Graph RAG，输出实体+关系+chunks（调试/脚本用） |

### 质量与检查

| 命令 | 用途 |
|------|------|
| `kdo lint [--strict] [--baseline <ref>] [--diff] [--accept-baseline] [--structure-report]` | 检查工作空间结构完整性 |
| `kdo validate --v15 [--domain] [--type] [--card] [--json]` | v1.5 三信号校验（external-attacks / dont-use / action-triggers） |
| `kdo cards [--type] [--domain] [--has] [--missing] [--count]` | 按条件列出/统计概念卡片 |
| `kdo card-diff <id> --since <ref>` | 节级别变更摘要（新增/删除/修改） |
| `kdo review --sample 5 --domain <domain>` | 随机抽检卡片，输出理解门禁摘要 |
| `kdo status` | 显示工作空间库存盘点 |

### 工具与自动化

| 命令 | 用途 |
|------|------|
| `kdo scaffold --card <id> \| --batch A\|B\|C\|D\|E \| --from-plan [--write]` | 为缺失 v1.5 信号的卡生成升级骨架 |
| `kdo clean-transcript <file>` | ASR 转录稿清理（去噪+去口头禅+分段+术语标注） |
| `kdo validate --v15 --watch` | 文件保存自动重检（2s 防抖，Ctrl+C 退出） |
| `kdo llm-check` | LLM 连通性自检 |
| `kdo build [--check] [--version] [--release]` | KDO 构建系统 |
| `kdo backup [--output <dir>]` | 备份 KDO 源码到 zip（去 .git/__pycache__/build） |

### 项目管理

| 命令 | 用途 |
|------|------|
| `kdo project <name> [--goal] [--set-status] [--set-stage]` | 产品项目管理 |
| `kdo task <title> [--project-id] [--priority] [--done]` | 产品任务管理 |
| `kdo connector <name> [--kind] [--target] [--run]` | 外部连接器管理 |
| `kdo eval <capability_artifact_id> --input --expected [--actual]` | 记录/评分 capability 评测 |
| `kdo dashboard [--output] [--view] [--serve]` | 生成静态 HTML dashboard |

### 视频管线

| 命令 | 用途 |
|------|------|
| `kdo video init <article>` | 创建视频项目骨架（_spec.md + 模板） |
| `kdo video validate <dir>` | 三层质量门（L1 结构/L2 内容/L3 管线） |
| `kdo video render --audio <dir>` | TTS 口播生成（edge-tts） |
| `kdo video render --compose <dir>` | ffmpeg 帧+音频合成（动态帧时长） |
| `kdo video ship <dir>` | 交付：draft→final + delivery record |

> **Graph RAG 是纯本地**：sklearn HashingVectorizer，查询时零 API 调用。索引在 `.kdo/graph_index/`。

---

## 三、Git 命令速查

| 场景 | 命令 |
|------|------|
| 查看最近变更文件 | `git diff --name-only HEAD~N..HEAD` |
| 从历史 commit 找回文件 | `git show <commit>:<path>` |
| 查看某人的提交 | `git log --oneline --since="YYYY-MM-DD" --all` |
| 回滚某个文件 | `git restore <path>` |

> vault 有 Obsidian git 插件每 3 分钟自动 commit。改坏了随时回滚。

---

## 四、WSL / Windows 桥接

| 场景 | 怎么做 |
|------|------|
| 黄药师启动 | `wsl` → `cd /mnt/c/Users/Administrator/Desktop/wiki` → `tmux new -s huangaoshi` → `claude` |
| WSL 里跑 Windows 命令 | 路径前缀 `/mnt/c/...` |
| PowerShell 从 WSL 调 | `powershell.exe -Command "..."` |
| 飞书 agent 重启 | `systemctl --user restart hermes-gateway-*` |

---

## 五、内置 Skills

| Skill | 路径 | 什么时候用 |
|-------|------|-----------|
| Knowledge Curator | `40_outputs/capabilities/skills/knowledge-curator/SKILL.md` | Capture → ingest → wiki |
| Delivery Producer | `40_outputs/capabilities/skills/delivery-producer/SKILL.md` | Wiki → article/artifact |
| System Linter | `40_outputs/capabilities/skills/system-linter/SKILL.md` | Vault 健康检查 |
| Image OCR | `40_outputs/capabilities/skills/image-ocr/SKILL.md` | 图片文字提取 |
| Deep Image Parser | `40_outputs/capabilities/skills/deep-image-parser/SKILL.md` | 多模态 AI 深度解析图片（表格/公式/视觉标记） |
| Document Parsing Toolkit | `40_outputs/capabilities/skills/document-parsing-toolkit/SKILL.md` | PDF/图片→结构化 Markdown 引擎选型 |
| Design Prompt Iteration | `40_outputs/capabilities/skills/design-prompt-iteration/SKILL.md` | 人反馈视觉问题 → agent 翻译为 prompt 修改 |
| AI Image Prompt Engineering | `40_outputs/capabilities/skills/ai-image-prompt-engineering/SKILL.md` | 通用 AI 图像生成 prompt 工程 |
| Visual Prompt System | `40_outputs/capabilities/skills/visual-prompt-system/SKILL.md` | SROM Visual OS：视角+美学宪章+拼贴海报 |
| Markdown to Presentation | `40_outputs/capabilities/skills/markdown-to-presentation/SKILL.md` | Markdown → Marp/Slidev/reveal.js 幻灯片 |
| Audio Production Pipeline | `40_outputs/capabilities/skills/audio-production-pipeline/SKILL.md` | TTS / 配音 / 音乐 / 音频后期 |
| AI Design Assets | `40_outputs/capabilities/skills/ai-design-assets/SKILL.md` | 设计资产管理规范 |

---

## 六、常见操作模式

### 审查新域素材

1. `ls` 扫描文件夹 → 有图片？→ OCR 全部
2. 读文本 + OCR 输出
3. `kdo query "相关主题"` 查 vault 已有覆盖
4. 提案 → 等待拍板 → 写卡

### 审查 agent 交付物（三段式审查框架 v2）

#### Phase 1：读文件（理解交付物）
1. `git diff --name-only HEAD~N..HEAD` 看变更范围
2. 读关键文件（代码/卡片/方案），建立基线认知
3. 交叉验证引用完整性：related 文件是否真实存在？路径是否正确？

#### Phase 2：交叉验证（找矛盾）
1. 逐卡读 → 外部攻击者是否真实学者？不要用场景是否有失效机制？
2. `kdo lint --diff` 检查格式
3. 对比源文件和交付物的一致性——不要只信报告，要跟源文件逐条对
4. **如果涉及 YAML frontmatter 操作**：必须做 round-trip 校验——用 `yaml.safe_load()` 读回来，确认嵌套结构无损

#### Phase 3：独立测量（最重要的环节）
1. **永远不做"相信报告"的审查**——P-15 的教训
2. 对任何"声称完成"的交付物，必须有可重复的测量脚本
3. 持续类指标（准确率/覆盖率/数量）必须自己跑一遍，不能看"修复前→修复后"对照表
4. 如果涉及自动标注/分类管线：用 Gold Standard 做 blind comparison，不要只看报告里的数字
5. "完成"的判定标准 = 代码已提交 + 数据已变更 + 验证已通过，缺一不可

#### Phase 4：记录
1. 更新评估 + `.agent/` 文件
2. 新坑追加到 `pitfalls.md`
3. 修复方案写入 `30_wiki/decisions/` 让执行者可直接取用

### 做基础设施决策前（黄药师专属）

1. `kdo graph query "..."` 保持对 vault 内容的体感
2. 检查不破坏现有卡片格式和链接
3. 改完跑 `kdo lint --diff`

---

## 七、不要重复造轮子

下列东西**已经存在且可用**，不要重新调研、重新部署：

- ✅ OCR：PaddleOCR v5（`C:\Users\Administrator\ocr-pipeline\`）
- ✅ 语义检索：LightRAG（`.kdo/graph_index/`）
- ✅ 测试框架：pytest 9.0.3（182/182 passing）
- ✅ 备份：坚果云 sandbox（`C:\Users\Administrator\Nutstore\1\我的坚果云\`）
- ✅ Graph RAG 依赖：纯本地 sklearn，零外部 API
- ✅ 权限：`.claude/settings.json` vault 全路径免批
- ✅ 网络搜索：`kdo-tools/web_search.py`（free, zero-config） — 见下方 §九

---

## 九、联网搜索

| 方式 | 命令 | 适用 |
|------|------|------|
| JSON 输出（agent 调用） | `python kdo-tools/web_search.py "query" --json` | Agent 交叉验证 |
| Markdown 输出（人读） | `python kdo-tools/web_search.py "query"` | 终端直接看 |
| 指定后端 | `python kdo-tools/web_search.py "query" --backend cn_bing` | 强制必应 |

**后端优先级**：SearXNG（JSON API）→ cn.bing.com（免费直连）→ Bing API（需 Azure key）

**缓存**：同 query 1 小时内不重复请求。缓存在 `kdo-tools/.search_cache/`

---

## 八、Hermes Provider 迁移 SOP（P-5/P-6 教训）

> 切 API（如 Kimi→DeepSeek）必须同步更新三层，漏一层就全挂。

### 迁移检查表

| # | 层 | 路径 | 操作 |
|:--|:--|:--|:--|
| 1 | .env | `~/.hermes/.env` + `~/.hermes/profiles/*/.env` | 换 `API_KEY` 环境变量 |
| 2 | auth.json ⚠️ | `~/.hermes/profiles/*/auth.json` | **删掉或清空 credential_pool 中旧 provider 条目**（P-3 教训：Hermes 优先读缓存，认为旧 key 已死就跳过） |
| 3 | config.yaml | `~/.hermes/config.yaml` + profiles | 改 `model.default`、`provider`、`base_url` |
| 4 | 清 session | `~/.hermes/profiles/*/sessions/` | 删旧 session（P-6 教训：残留旧 session ID 导致静默空响应） |
| 5 | 重启 | `systemctl --user restart hermes-gateway-*` | |
| 6 | 验证 | `journalctl --user -u hermes-gateway-* --no-pager -n 20 \| grep -i "401\|auth\|error"` | 确认无认证错误 |

### DeepSeek（Anthropic 协议）

```
model: deepseek-v4-pro
provider: deepseek
base_url: https://api.deepseek.com              ← 注意：deepseek provider 走 OpenAI 协议，不用 /anthropic
# ⚠️ 改 provider 前先查 models_dev_cache.json 确认 npm 字段：
#    npm: @ai-sdk/anthropic → base_url 用 /anthropic
#    npm: @ai-sdk/openai-compatible → base_url 用根路径
env: DEEPSEEK_API_KEY=sk-...
```

### Kimi（Anthropic 协议，注意 Base URL）

```
model: kimi-for-coding
provider: kimi-coding
base_url: https://api.kimi.com/coding/v1       ← 这是 Anthropic endpoint
# Anthropic Base URL 实际是 https://api.kimi.com/coding/，但在 Hermes 中写 /v1 才能正确拼接 /messages
env: KIMI_API_KEY=sk-kimi-...
```

> ⚠️ 2026-06-12：K2.7 发布首日 Anthropic 协议 tool call 全挂（`finish_reason='length'`）。症状：纯对话正常，一调用工具就 `Model generated invalid tool call`。官方 Kimi CLI（Node.js 新版）正常。临时方案：切 DeepSeek。等 Kimi 修复后切回 `kimi-for-coding`。

### 禁止事项

- 不要只改 .env 不改 auth.json
- 不要混用 Kimi 和 DeepSeek 的 key（一个 profile 一个 provider）
- 不要同时跑两个同 channel 的 gateway（飞书消息会被抢）
