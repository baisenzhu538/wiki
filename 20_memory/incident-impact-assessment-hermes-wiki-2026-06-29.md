---
id: incident-impact-assessment-hermes-wiki-2026-06-29
title: "Hermes/WSL/Wiki 事件影响评估（2026-06-29）"
type: assessment
status: enriched
author: 王语嫣
created_at: 2026-06-29
updated_at: 2026-06-29
confidence: 0.88
domain:
  - kdo
  - infrastructure
  - post-mortem
source_refs:
  - hermes-doctor-output-2026-06-29
  - git-log-wiki-30_wiki-deletions
  - kdo-lint-current-txt-2026-06-29
  - framework-yitang-nine-layer-deep-dig
  - framework-yitang-six-layer-cross-validation
related:
  - [[kdo-infrastructure-audit-2026-06-10]]
  - [[kdo-system-manual]]
  - [[framework-yitang-nine-layer-deep-dig]]
  - [[framework-yitang-six-layer-cross-validation]]
  - [[plan-kdo-infrastructure-disaster-prevention]]
---

# Hermes/WSL/Wiki 事件影响评估（2026-06-29）

> 触发：Hermes 从 Kimi 切换 DeepSeek 时配置出错，导致多个 Hermes 实例崩溃；同期发现 wiki 知识库出现大量 Obsidian 死链、frontmatter 解析错误、src_unknown 占位。
>
> 方法：六层交叉验证核实事实 + 九层深挖法评估对 KDO 工厂的影响。

---

## 一、事件快照

| 时间 | 事实 |
|:---|:---|
| 2026-06-02 | Git 提交 `dbdfb634` 删除 Rust 系列 8 张卡（共 469 行），原因待查。 |
| 2026-06-19 ~ 06-29 | Hermes 模型切换引发配置错误，四实例（老顽童 CLI / 段王爷 / 洪七公 / 王语嫣）不同程度失效。 |
| 2026-06-29 | 修复 Hermes 配置（移除错误 `prefill_messages_file`、升级 `_config_version` 到 v29、禁用故障 MCP）。 |
| 2026-06-29 | 修复 Obsidian 图视图死链：从 11,740 个不可解析节点降到 0。 |
| 当前 | Hermes `doctor` 全绿；wiki 工作树干净；kdo CLI 在 PATH 但工作区识别失败。 |

---

## 二、六层交叉验证

### L1 来源验证

- 文件系统直接扫描：2,181 张卡、35,401 处 `src_unknown`。
- Git 历史：`git log --diff-filter=D` 确认 8 张 Rust 卡删除。
- Hermes doctor v0.16.0 自诊断：DeepSeek/Kimi/MiniMax 连通，config v29。
- kdo lint 日志：`_tmp/kdo_lint_current.txt` 共 3,230 行警告。

### L2 时间验证

- Rust 卡丢失比 Hermes 崩溃早约 20 天，说明二者可能不是同一根因，但属于同一波系统不稳定期。
- frontmatter 缩进错误是长期 schema drift，不是单次事件造成。
- 6 月 28–29 日仅删除 `pending_unknown.md` 1 张，无近期批量删除。

### L3 逻辑验证

- “丢了很多卡”：过度悲观。确认永久丢失仅 8 张；更多是 frontmatter/链接损坏造成的“感知丢失”。
- “Hermes 全挂了”：已不成立，doctor 通过。
- “kdo 工具链废了”：部分成立，二进制存在但工作区识别失败。

### L4 数据验证

| 指标 | 数值 |
|:---|---:|
| 30_wiki 卡片总量 | 2,181 张 |
| 确认永久删除 | 8 张，469 行 |
| frontmatter 解析失败 | 91 张（4.2%） |
| src_unknown 占位 | 35,401 处 |
| Obsidian 死链 | 11,740 → 0 |
| kdo lint 警告行数 | 3,230 行 |

### L5 反例验证

- Git working tree 干净，无大量未知文件丢失。
- 许多 lint 警告（L2 body 太短、缺 review_date）是历史债务，非本次事件新增。
- Hermes 已恢复，说明“全厂停摆”的感知已经过去。

### L6 行动验证

导出 5 条立即行动：
1. 从 Git 历史恢复 8 张 Rust 卡。
2. 批量修复 91 个 frontmatter 缩进错误。
3. 处理 src_unknown backlog。
4. 修复 kdo 工作区识别问题。
5. 为 Hermes 配置变更建立 rollback + 灰度机制。

**验证强度：B 级（4–5 层通过）**，可指导行动，但 Hermes 实例级状态仍需单独抽查。

---

## 三、九层深挖法：KDO 工厂影响画像

### L1 表面业务公式

```
工厂产出 = Σ(Agent 在线时长 × 知识检索准确率 × 卡片质量 × 流水线吞吐)
```

本次事件同时压低了四个因子：Agent 短期掉线、检索因死链/frontmatter 错误下降、卡片质量因 src_unknown 下降、质检线（kdo lint）不可用。

### L2 假设审计

| 假设 | 审计结果 |
|:---|:---|
| “我们丢了很多内容” | 过度悲观。真丢失仅 8 张。 |
| “Hermes 切换模型容易出大事” | 成立。一次配置错误拖垮所有实例。 |
| “wiki 还能正常检索” | 不成立。91 张 frontmatter 失败会直接影响 Graph RAG。 |
| “kdo 可用来验证修复” | 不成立。工作区识别损坏。 |

### L3 政策/合规/监管边界

外部监管无影响。内部政策缺口：
- 配置变更没有 rollback SOP。
- frontmatter schema 没有硬门禁。
- 没有“备份完整性”验证机制。

### L4 失败模式库

1. **单点配置错误 → 全实例雪崩**：所有 Hermes 实例共享 WSL Python venv，缺乏隔离。
2. **自动索引污染图网络**：`30_wiki/index.md` 里的路径前缀链接造成 11,740 个 Obsidian 不可解析节点。
3. **备份 ≠ 可恢复**：Rust 卡被删 27 天未被发现。
4. **Schema drift 沉默破坏下游**：91 个 frontmatter 错误让 Graph RAG 跳过这些卡。
5. **工具链可用性漂移**：kdo 在 PATH 但工作区识别失效，说明没有健康探针。

### L5 隐性成本与替代方案

- 恢复时间成本：数小时人工救火，而非一键 rollback。
- 认知负荷：需要人工区分“真丢失 / 链接坏 / frontmatter 坏”。
- 替代方案：独立 venv/容器、入库前 `kdo lint --strict`、每周完整性抽查。

### L6 人与组织执行能力

| 角色 | 影响 |
|:---|:---|
| 老顽童 Producer | 暂停生产救火；无一键恢复剧本。 |
| 欧阳锋 Architect | 暴露配置架构缺少版本化与灰度。 |
| 黄药师 Builder | kdo 工具链局部失效，无法靠 lint/index 验证。 |
| 洪七公 Multimodal | WSL/Python 不稳会连带影响多模态 pipeline。 |
| 段王爷 Publisher | 飞书实例恢复后可工作，但发布前校验受阻。 |
| 王语嫣 Consultant | 检索质量下降直接削弱咨询能力。 |

### L7 市场情绪/资本/招商骗局

反向信号：AI agent / 知识库 hype 下，容易低估 agent 和知识库的脆弱性。对外要管理预期，对内要警惕“修好了就万事大吉”的情绪。

### L8 边界案例与反例

- 边界 A：若 Git history 没有 Rust 卡，则 8 张卡真丢失。
- 边界 B：若 frontmatter 错误 >10%，Graph RAG 将大面积失效。
- 边界 C：若事件发生在交付前 1 小时，即使 90% 卡片完好也会导致交付失败。
- 反例：“反正最后都修好了，影响不大”——SOP 缺失本身就是高杠杆风险。

### L9 决策框架

| 决策 | 条件 |
|:---|:---|
| **Go** | 恢复 Rust 卡 + 修复 91 个 frontmatter + 修复 kdo 工作区识别 + 全量 lint 通过。 |
| **No-go** | 在未建立 Hermes 配置变更 SOP 前再次切换 provider/model。 |
| **条件通过** | 可先恢复生产，但 7 天内补齐：配置快照、schema lint gate、每周完整性检查。 |

**最大风险点**：
1. 配置变更雪崩效应会复发。
2. frontmatter/schema 损坏导致 Graph RAG 静默漏召回。
3. kdo 工具链不可用使质量门失效。

**重新评估触发信号**：
- Hermes 切换 provider/model 前必须先通过 `hermes doctor` 和一次测试对话。
- kdo lint 新增 error 时立即冻结入库。
- Obsidian 不可解析节点 >100 时启动复盘。

---

## 四、综合结论

| 维度 | 当前状态 | 严重程度 | 已修复？ |
|:---|:---|:---:|:---:|
| Hermes 实例可用性 | doctor 全绿 | 中（曾高） | ✅ |
| 知识卡片丢失 | 8 张 Rust 卡可恢复 | 中 | ❌ |
| frontmatter/元数据健康 | 91 张解析失败 | 高 | ❌ |
| 内容溯源完整性 | 35,401 处 src_unknown | 高 | ❌ |
| 图视图/链接网络 | 死链 0 | 低 | ✅ |
| kdo 工具链 | CLI 在 PATH，工作区识别失败 | 高 | ❌ |
| 配置变更 SOP | 缺失 | 高 | ❌ |

**总体判断**：直接损失可控，但暴露了 KDO 工厂的 3 个单点故障——配置管理、schema 治理、质量门工具链。不补 SOP，下一次同类事件可能在交付窗口期让工厂停摆。

**后续卡片**：[[plan-kdo-infrastructure-disaster-prevention]]
