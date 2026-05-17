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

## 二、KDO CLI 核心命令

| 命令 | 用途 |
|------|------|
| `kdo query "..."` | 语义+图检索（LightRAG），回退 BM25 → 关键词 |
| `kdo graph rebuild` | 重建 Graph RAG 索引（内容变更后） |
| `kdo graph query "..." --json` | 直接查 Graph RAG（调试/脚本用） |
| `kdo lint --diff` | 只报告 HEAD~1 后的新增 lint 问题 |
| `kdo lint --baseline <ref>` | 只报告指定 ref 后的新增 lint 问题 |
| `kdo cards --type <t> --domain <d>` | 按类型/域查询卡片 |
| `kdo cards --count` | 只出数量 |
| `kdo card-diff <id> --since <ref>` | 节级别变更摘要 |
| `kdo review --sample 5 --domain <domain>` | 随机抽检卡片 |
| `kdo status` | 库存盘点 |

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
| Design Prompt Iteration | `40_outputs/capabilities/skills/design-prompt-iteration/SKILL.md` | 人反馈视觉问题 → agent 翻译为 prompt 修改 |

---

## 六、常见操作模式

### 审查新域素材

1. `ls` 扫描文件夹 → 有图片？→ OCR 全部
2. 读文本 + OCR 输出
3. `kdo query "相关主题"` 查 vault 已有覆盖
4. 提案 → 等待拍板 → 写卡

### 审查 agent 交付物

1. `git diff --name-only HEAD~N..HEAD` 看变更
2. 逐卡读 → 外部攻击者是否真实学者？不要用场景是否有失效机制？
3. `kdo lint --diff` 检查格式
4. 更新评估 + `.agent/` 文件

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
