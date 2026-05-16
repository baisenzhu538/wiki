---
updated: 2026-05-17
active_branch: main
active_task: 双线并行——黄药师 Sprint 12 Batch B（demand 收尾）+ 老顽童科学决策域编译
blockers: []
---

## 你是谁

**欧阳锋（Architect）**——KDO 知识工作空间的架构者。负责规则设计、审查产出、任务分配、技术决策。审而不改。

## 关键路径

| 用途 | 路径 |
|------|------|
| Vault 根目录 | `C:\Users\Administrator\Desktop\wiki\` |
| KDO CLI 源码 | `C:\Users\Administrator\Knowledge Delivery OS 0.0.1\kdo\` |

## 模型与环境

- **模型**：DeepSeek V4 Pro（直连 `api.deepseek.com/anthropic`）
- **运行方式**：WSL2 Ubuntu-22.04 终端 → `claude`（tmux session `claude`）
- **关键教训**：切模型时涉及五层配置（`.bashrc` / 注册表 / systemd drop-in `env.conf` / `cc-connect config.toml` / cc-connect session 缓存）。2026-05-16 切 Kimi 再切回 DeepSeek 后，漏了 env.conf + config.toml work_dir + session 缓存，导致飞书黄药师 401 + 找不到 wiki + 空响应。已修复。详见 `pitfalls.md` P-5/P-6。

## 当前状态

### Sprint 进度
- v1.6 工业化手册定案，卡片层三要件
- Sprint 11 / 12 Batch A / A-2 / 13 → 全部 completed ✅
- **Sprint 12 Batch B** → entrepreneur 23/23 + panproduct-execution 18/18 完成
- **demand 域 11 张**：Action Triggers 已有，缺 外部攻击+不要用场景（黄药师本轮）
- 剩余：personal(~8) / pitch(10) / aesthetic(4) / prompt(4)
- Batch C（~30 concept 卡）待 Batch B 完成后

### 新域：科学决策（老顽童负责）
- 素材：6 口述稿 ~16,000 行 + 35 张 PNG（全待 OCR）
- 老顽童试工通过 ✅（yt-decision-y-model / canvas / ai-partner，B+→A-）
- 架构从 21 张收缩到 9 张（2 framework + 7 tool）
- 本轮：01 审美拉升 → yt-decision-habit-shift（X型→Y型诊断转换）
- 顺序：01→02→03→04→05，每模块 ≤2 张 tool 卡

### KDO CLI 状态
- 42 .py 文件，11,635 行，11 测试文件，pytest 未安装
- `kdo cards/lint/card-diff/review` 正常；Graph RAG 依赖未装（战略要补齐）
- 待办：pytest 安装 / lint --quiet / cards --missing 多值 / Graph RAG 跑通
- 备份：KDO 源码放坚果云（单机灾备，非 git）

## 新增工具

| 命令 | 用途 |
|------|------|
| `kdo lint --diff` | 只报告 HEAD~1 之后新增的 lint 问题 |
| `kdo lint --baseline <ref>` | 只报告指定 ref 之后新增的 lint 问题 |
| `kdo cards --type <t> --domain <d>` | 按类型/域查询卡片 |
| `kdo cards --type tool --missing "Action Triggers"` | 找出缺失指定节的卡片 |
| `kdo cards --count` | 只出数量 |
| `kdo card-diff <id> --since <ref>` | 节级别变更摘要（新增/删除/修改） |
| `kdo review --sample 5 --domain yitang` | 随机抽检卡片，输出理解门禁摘要 |

## 最近决策

### 2026-05-17：欧阳锋会话
- **老顽童上岗**：试工通过（科学决策 3 张卡），独立负责科学决策域编译。架构从 21 张收缩到 9 张。产出后出文章。
- **双线并行**：黄药师 Batch B + 老顽童科学决策域，互不阻塞。
- **KDO 备份**：坚果云单机灾备（删 .git/ + 排除 __pycache__），不用 GitHub。
- **Graph RAG**：战略保留，补齐依赖+跑通验证，为 MCP server 铺路。

见 `decisions.md`

## 下次启动

1. 读 `pitfalls.md`
2. 核查黄药师 demand 域进度（外部攻击+不要用场景是否补齐）
3. 核查老顽童 01 模块产出（yt-decision-habit-shift）
4. 关注：KDO pytest 是否安装 / 科学决策图片是否 OCR

## ⚠️ 会话结束前（MUST）

- [ ] 更新 `updated:` 日期
- [ ] 更新 `active_task` 和 `blockers`
- [ ] 更新 ## 当前状态（完成数、剩余数、新发现的问题）
- [ ] 有新坑？追加到 `pitfalls.md`
- [ ] 有决策？追加到 `decisions.md`
- [ ] **禁止用 `/memory` 替代上述更新**——`/memory` 不是项目公共记忆。
