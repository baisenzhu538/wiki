---
id: plan-kdo-infrastructure-disaster-prevention
title: "黄药师：KDO 基础设施防灾与韧性建设建议"
type: improvement-plan
status: draft
author: 王语嫣
target_reviewer: 黄药师 + 欧阳锋
created_at: 2026-06-29
updated_at: 2026-06-29
domain:
  - kdo
  - infrastructure
  - disaster-recovery
source_refs:
  - incident-impact-assessment-hermes-wiki-2026-06-29
  - kdo-system-manual
  - kdo-infrastructure-audit-2026-06-10
related:
  - [[incident-impact-assessment-hermes-wiki-2026-06-29]]
  - [[kdo-system-manual]]
  - [[kdo-infrastructure-audit-2026-06-10]]
  - [[kdo-card-architecture-proposal]]
---

# 黄药师：KDO 基础设施防灾与韧性建设建议

> 收件人：黄药师（Builder）
> 抄送：欧阳锋（Architect）、老顽童（Producer）
> 背景：[[incident-impact-assessment-hermes-wiki-2026-06-29]]
>
> 目标：把“单次配置错误就能让全厂停摆”的脆弱系统，改造成可灰度、可回滚、可自愈的知识工厂。

---

## 一、现状诊断（一句话）

KDO 工厂当前是**“高可用幻觉”**：Git 每天备份、Hermes 能跑、卡片在磁盘上，但配置无隔离、schema 无门禁、工具链无健康探针。一次模型切换就同时击穿 Agent 层、知识层、工具链层。

---

## 二、三层防灾目标

| 层级 | 目标 | 核心指标 |
|:---|:---|:---|
| **L1 生存层** | 单点故障不扩散 | 一个 Hermes profile 崩了，其他 profile 不受影响 |
| **L2 恢复层** | 故障后 5 分钟内可回滚 | 配置变更可一键还原到上一个稳定快照 |
| **L3 进化层** | 故障后知识库不降级 | 坏卡片进不了库，坏链接出不了 Obsidian |

---

## 三、具体工程措施

### 3.1 Hermes 配置隔离与变更门（P0）

**问题**：所有 Hermes 实例共享 WSL Python venv，一次 provider 切换配置污染全局。

**建议**：

1. **每个 profile 独立 venv（首选）或至少独立配置快照目录**
   ```bash
   ~/.hermes/profiles/{laowantong,duanwangye,wangyuyan,beikai}/
   ├── config.yaml          # 当前生效配置
   ├── config.yaml.bak      # 上次稳定配置
   └── venv/                # 可选：独立 Python 环境
   ```

2. **配置变更脚本化，禁止手改**
   ```bash
   hermes-profile-switch <profile> --provider deepseek --model deepseek-v4-pro
   # 脚本自动：备份 → 修改 → doctor → 回滚 or 提交
   ```

3. **灰度顺序**
   ```
   1. 在临时 profile（如 kimi-test）验证
   2. 在低频实例（老顽童 CLI）验证
   3. 在飞书实例逐个 rollout（段王爷 → 洪七公 → 王语嫣）
   4. 全量切换前保留 24h 观察期
   ```

4. **MCP 变更单独开关**
   每个 MCP server 必须显式 `enabled: true/false`，禁用状态也要有注释说明原因。

### 3.2 Git 备份 → 可验证备份（P0）

**问题**：Rust 系列 8 张卡 6 月 2 日被删，27 天后才被发现。

**建议**：

1. **每日备份后加一条“完整性断言”**
   在 commit message 或 CI 里记录：
   - 总卡片数
   - frontmatter 错误数
   - src_unknown 数量
   - 不可解析 wikilink 数量

2. **每周随机抽查 10 张卡 + 1 个主题簇**
   抽查方式：从 `30_wiki/index.md` 随机选一个主题，确认相关卡片存在且能打开。

3. **关键主题簇保护清单**
   把高价值主题（如 Rust、九层深挖法、六层交叉验证、OODA、KDO 系统 manual）写入 `.kdo/protected_topics.json`，每周强制校验一次。

### 3.3 frontmatter Schema 硬门禁（P0）

**问题**：91 张卡（4.2%）frontmatter 解析失败，直接影响 Graph RAG 和 kdo lint。

**建议**：

1. **入库前强制 `kdo lint --strict`**
   任何新卡/改卡进入 `30_wiki/` 前必须通过；error 直接阻断，warning 必须清零或显式接受 baseline。

2. **source_refs / domain 列表统一缩进规则**
   当前大量错误都是列表缩进不一致导致。制定规则：
   ```yaml
   source_refs:
     - src_20260629_xxxx-xxx.md
     - src_20260629_yyyy-yyy.md
   domain:
     - kdo
     - infrastructure
   ```
   并在 lint 里加一条专门规则检查。

3. **body 中 `src_unknown` 不能长期停留**
   设置阈值：单卡 `src_unknown` 出现 >3 处即 error；全库总量下降趋势纳入周报。

### 3.4 kdo 工具链韧性（P1）

**问题**：`kdo` 二进制在 PATH，但运行 `kdo lint` 报 “No KDO workspace found”。

**建议**：

1. **明确工作区识别逻辑**
   检查 `.kdo/` 目录下是否缺少 `config.yaml` 或 `workspace.yaml`。修复后把识别规则写进 `kdo-system-manual`。

2. **工具链健康探针**
   每天运行一次：
   ```bash
   kdo doctor          # 工作区识别 + 依赖检查
   kdo lint --summary  # 质量快照
   ```
   输出写入 `90_control/daily-health.log`。

3. **CLI 与项目源码解耦**
   当前 `kdo` 安装在系统 Python（`/c/Program Files/Python312/Scripts/kdo`），与项目源码 `C:/Users/Administrator/Knowledge Delivery OS 0.0.1/` 可能版本不一致。建议：
   - 要么用项目 venv 里的 kdo；
   - 要么明确系统 CLI 与项目源码的同步策略。

### 3.5 Obsidian 图网络保护（P1）

**问题**：自动生成的 `30_wiki/index.md` 和 `30_wiki/links/index.md` 曾引入 11,740 个死链。

**建议**：

1. **索引文件生成器加校验**
   生成 `index.md` 后必须跑一轮 wikilink 解析，确保所有 `[[id|alias]]` 里的 `id` 在 `30_wiki/` 中存在。

2. **索引文件与内容文件分离**
   考虑把自动索引放到 `30_wiki/_indices/` 下，不参与 Graph RAG 核心召回，只作为导航。

3. **Obsidian 死链监控**
   每周导出一次 Obsidian 的 “Unlinked mentions” / “Broken links” 数量，>100 时告警。

### 3.6 运行时监控与告警（P2）

**建议**：

1. **Hermes 实例心跳**
   每个 gateway profile 每 5 分钟 self-ping 一次，失败则写入 `~/.hermes/logs/heartbeat.log`。

2. **WSL 健康检查**
   因为 Hermes 跑在 WSL，增加：
   ```bash
   wsl -d Ubuntu-22.04 -e echo wsl_ok
   ```
   作为开机和定时检查项。

3. **一键状态看板**
   黄药师可以维护一个 `90_control/kdo-factory-status.md`，每天手动或脚本更新：
   - Hermes 各 profile 状态
   - kdo lint 错误/警告数
   - frontmatter 错误数
   - src_unknown 总数
   - Obsidian 死链数

---

## 四、实施优先级

| 优先级 | 事项 | 负责人 | 预期完成时间 |
|:---:|:---|:---|:---:|
| **P0** | Hermes profile 配置快照 + 切换脚本 | 黄药师 | 3 天 |
| **P0** | 恢复 Rust 系列 8 张卡 | 黄药师 | 1 天 |
| **P0** | 批量修复 91 个 frontmatter 错误 | 黄药师 | 2 天 |
| **P0** | 入库前 `kdo lint --strict` 门禁 | 黄药师 + 欧阳锋 | 5 天 |
| **P1** | 修复 kdo 工作区识别 + 每日健康探针 | 黄药师 | 5 天 |
| **P1** | 索引文件生成器加 wikilink 校验 | 黄药师 | 3 天 |
| **P2** | Hermes 心跳 + WSL 健康检查 | 黄药师 | 7 天 |
| **P2** | 一键状态看板 | 黄药师 | 7 天 |

---

## 五、验收标准

每项 P0 完成后必须满足：

1. **配置隔离**：修改一个 profile 的 provider，其他 profile 的 `hermes doctor` 仍全绿。
2. **可回滚**：任意配置变更能在 1 条命令内回滚到变更前状态。
3. **schema 门禁**：`kdo lint --strict` 返回 0 error，warning 数量不高于当前 baseline。
4. **Rust 卡恢复**：`git status` 显示 8 张 Rust 卡重新加入工作树，且 frontmatter 解析成功。
5. **图网络健康**：Obsidian 不可解析 wikilink = 0。

---

## 六、需要欧阳锋拍板的问题

1. 是否接受“每个 Hermes profile 独立 venv”的架构改动？（会增加磁盘占用，但隔离性最好）
2. `kdo lint --strict` 是否作为所有卡片入库的硬门禁？（会短期阻塞部分低质量卡片入库）
3. 是否把 `src_unknown` 总量下降纳入每周工厂例会指标？

---

## 七、最小可执行路径（本周内）

如果资源只够做 3 件事，按这个顺序：

1. **恢复 Rust 8 张卡**（挽回可确认损失）。
2. **写一个 frontmatter 修复脚本**，把 91 个缩进错误一次性修好（恢复 Graph RAG 召回）。
3. **给每个 Hermes profile 加 `config.yaml.bak`**，并写一条 `hermes-profile-rollback <profile>` 命令（防止再次雪崩）。

这三件事做完，KDO 工厂就从“脆弱”进入“基本可用”状态。

---

**关联评估**：[[incident-impact-assessment-hermes-wiki-2026-06-29]]
