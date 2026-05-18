---
id: quality-gate-automation-v15
title: "质量门自动化 — kdo validate --v15"
status: pending
priority: P1
assigned_to: 黄药师
reviewer: 欧阳锋
created: 2026-05-19
depends_on: P1-B（结构多样性报告 ✅）
---

## 背景

当前 v1.5 三要件（外部攻击 ≥2、不要用场景 ≥2、Action Triggers ≥3）全靠人工审查。P1-B 结构报告已揭示了 6 种卡片结构并存，现在可以基于结构类型设计自动化校验规则。

## 目标

`kdo validate --v15` 自动检测每张卡的 v1.5 三要件是否齐全，输出结构化报告。不是替代人工审查，是**把机械检查自动化，让人专注内容质量**。

## 校验矩阵

每种结构类型 × v1.5 三信号的适用性：

| 结构类型 | 外部攻击 ≥2 | 不要用场景 ≥2 | Action Triggers ≥3 | 适用性 |
|---------|------------|-------------|-------------------|--------|
| standard-concept | ✅ 在 [Critique] 节 | ✅ 在 Synthesis | ✅ 在 Action Triggers 节 | 全检 |
| pan-product | ✅ 在 [Critique] 节 | ✅ 在 Synthesis | ✅ 在 Action Triggers 节 | 全检 |
| pan-product-upgraded | ✅ 已在 [Critique] | ✅ 已在 Synthesis | ✅ 已在新节 | 全检（验证未退化） |
| research | ✅ 在 [Critique] 节 | ⚠️ 在 Synthesis（若无 Synthesis 则警告） | ⚠️ 同左 | 降级检查 |
| catalog-index | ⚠️ 仅检查对组织逻辑的攻击 | ❌ 豁免 | ❌ 豁免 | 最低检查 |
| other | ⚠️ 警告：人工审查 | ⚠️ 警告：人工审查 | ⚠️ 警告：人工审查 | 仅报告 |

### 检查粒度

**外部攻击（≥2）**：
- 在 [Critique] 节中搜索引证格式 `*领域 学者名*`（斜体包裹）的段落
- 计数 ≥2 → pass
- 检测同一学者被重复使用（去重）

**不要用场景（≥2）**：
- 在对应节中搜索含"不要用"/"不适用"/"不适合"/"避免"关键词的表格行或列表项
- 每行/每项需同时含：场景描述 + 失效原因 + 替代方案（三列完整的才算一条）
- 计数 ≥2 → pass

**Action Triggers（≥3）**：
- 搜索 `### Action Triggers` 或 `### Action Triggers` 节
- 节内搜索三列完整（触发场景 + 第一动作 + 可验证成功指标）的行
- 计数 ≥3 → pass

## 命令行接口

```bash
kdo validate --v15                          # 全库检查，输出报告
kdo validate --v15 --domain yitang          # 按域过滤
kdo validate --v15 --type tool              # 按类型过滤
kdo validate --v15 --card yt-decision-width-method  # 单卡检查
kdo validate --v15 --json                   # JSON 输出（给 CI/脚本）
```

### 输出格式

```
v1.5 Quality Gate Report
========================
Total: 198 cards | Passed: 185 | Failed: 5 | Warning: 8

FAILED (5):
  yt-research-osl-framework (research)
    ✗ 外部攻击: 1/2 (missing 1)
    ✗ Action Triggers: 0/3 (missing section)
  ...

WARNING (8):
  yt-system-course-catalog (catalog-index)
    ⚠ catalog-index 结构豁免 Action Triggers 检查
  ...
```

## 技术实现

- 位置：`kdo/commands/quality.py`（扩展现有 `cmd_validate`）
- 复用 `_classify_structure()`（已在 system.py 中实现）判断结构类型
- 复用 `kdo lint --structure-report` 的 heading 解析逻辑
- ~150-200 行代码
- 需新增测试（~5 test cases：每种结构的通过/失败场景）

## 验收标准

- [ ] `kdo validate --v15` 六个结构的校验逻辑实现
- [ ] 单卡检查模式（`--card`）可用
- [ ] JSON 输出模式（`--json`）可用
- [ ] 外部攻击去重逻辑（同一学者不重复计数）
- [ ] 不要用场景三列完整性检测（不是仅关键词匹配）
- [ ] Action Triggers 三列完整性检测
- [ ] pytest 新增 ≥5 个 test cases，全绿
- [ ] 对 198 张真实卡运行报告，无假阳性崩溃

## 不做

| 候选项 | 理由 |
|--------|------|
| 攻击者质量判断（是否稻草人、是否跨范式） | 语义判断，暂不自动化 |
| Action Triggers 成功指标可验证性判断 | 语义判断，暂不自动化 |
| 自动修复 | 超出 scope——这是检查工具，不是修复工具 |

## 相关

- [[kdo-infrastructure-backlog-proposal]] — P1-B 结构报告是此前置
- [[sprint-12-backfill-card-behavioral-requirements]] — v1.5 三要件定义
- [[domain-digest-cards]] — P3，排在 validate --v15 之后
