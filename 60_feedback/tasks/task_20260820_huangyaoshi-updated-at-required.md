---
id: 395
assignee: huangyaoshi
status: pending_review
title: 卡片生产线 frontmatter updated_at 必填收口（P3，#391 终审观察立项）：promote 管线产物 7 张缺 updated_at——模板/门禁双查
priority: P3
dependency: []
code_files:
- kdo-tools/wechat_promote.py
- kdo-tools/wechat_knowledge.py
- kdo-tools/skill_crystallize.py
- C:/Users/Administrator/Knowledge Delivery OS 0.0.1/kdo/commands/curation.py
- C:/Users/Administrator/Knowledge Delivery OS 0.0.1/kdo/commands/delivery.py
updated_at: '2026-08-20T13:11:51.751226+00:00'
---

# #395 卡片生产线 updated_at 必填收口

## 来源

#391 终审观察（欧阳锋）：case-wechat-* 7 张（08-19 新卡，promote 质量门管线产物）缺 `updated_at`——**生产线模板字段缺口**：新卡一出生就欠账，清扫类任务（#385/#388/#391/#394）会永远扫不完。

## 任务目标

让卡片生产线（promote 管线为切入点）产出的卡自带 updated_at，从源头关闭这类欠账。

## 执行范围

1. **查模板**：promote 管线（kdo-tools/wechat_promote.py）产卡 frontmatter 模板——补 updated_at 字段（值=生成日期）
2. **查同类**：全厂其他产卡入口（kdo 命令行/其他脚本）是否有同样缺口，出清单；量小一并修，量大只列清单
3. **评估门禁**：pre-submit 对缺 updated_at 目前是 warning——评估是否对**新卡**（created_at ≥ 本单落地日）升 ERROR；老卡不动避免误伤存量（评估结论入报告，改动需说明理由）
4. 顺手把现存 7 张 case-wechat-* 缺 updated_at 的清单交给 #394 合并处理（本单不改卡，只改生产线）

## 边界

- 只改生产线模板/门禁代码，不改存量卡片
- pre-submit 规则改动须前后对比实测（新卡拦截/老卡不误伤）
- 完成后 commit 入档（E040）；MCP 长驻进程重启事项入报告（不擅自杀进程，#361 模式）
- 欧阳锋终审

## 内容价值判断（PROTOCOL §7 合规声明）

- 仅生产线代码修正，无卡片删除/移动

## 验收标准

1. promote 新产卡自带 updated_at（正向实测：跑一张测试卡验证后清理夹具）
2. 同类产卡入口缺口清单
3. pre-submit 规则如改动：新卡拦截实测 + 存量不误伤实测

## 交付

1. 代码 diff + 正反向实测 + 缺口清单
2. 送欧阳锋终审

---

## 执行报告（2026-08-20 黄药师）

### 根因定位
wechat_promote.py 只做搬运+校验，**产卡模板真源在上游 `wechat_knowledge.py`**（LLM 三层次卡生成器，frontmatter 只有 created_at）。7 张欠账卡全部出自该模板。

### 改动清单（模板 4 处 + 兜底 1 处）
| 文件 | 改动 |
|:---|:---|
| `kdo-tools/wechat_knowledge.py` | 产卡模板补 `updated_at`（=生成日） |
| `kdo-tools/wechat_promote.py` | promote_case 加归一化兜底：缺 updated_at 的卡落待编排区前自动补（值=created_at，次选今日）；写入改 write_text（归一化内容落待编排区，**inbox 原件不动**）；顺序在"已流转跳过"检测之后，避免噪声 |
| `kdo-tools/skill_crystallize.py` | 补 updated_at + 顺手修硬编码 `created_at: 2026-08-09`（同族出生字段欠账，所有结晶卡生日都是错的） |
| KDO仓 `kdo/commands/curation.py:592` | 产卡模板补 `updated_at: {now}` |
| KDO仓 `kdo/commands/delivery.py:449` | query 卡模板补 `updated_at` |

### 同类产卡入口普查（执行范围②）
| 入口 | updated_at |
|:---|:---|
| kdo templates.py（3 模板）/ digest.py / encapsulate.py / quality.py(scaffold) / ingestion.py / curation.py:878 | ✅ 已有 |
| kdo curation.py:592 / delivery.py:449 | ❌→已修 |
| wechat_knowledge.py / skill_crystallize.py | ❌→已修 |
| aesthetic-library-builder.py:149 | N/A（写的是 config.json 不是卡） |
| daily-context-save.py | ✅ 已有 |

量小（4 处），按任务单一并修完，无遗留清单。

### pre-submit 门禁评估（执行范围③）——结论：**无需改动**
任务单前提"缺 updated_at 是 warning"不成立：kdo pre-submit Gate 1（pre_submit.py:161）对缺 updated_at **已是 ERROR**（`Missing required field: updated_at`）。
- 实测 A：缺 updated_at 新卡 → 🔴 ERROR 拦下 ✓
- 实测 B：新模板产物（带 updated_at）→ 该字段不再报错（存量经 #391 已归零，ERROR 级不误伤老卡）✓
- **真正的缺口不是门禁级别，是 promote 管线产物从未经过 pre-submit**——已从源头（模板）+ 入口（归一化）双侧关闭，门禁维持现状即可

### 正向实测
- 生成器：fixture 逐字稿 → 骨架卡 frontmatter 自带 `updated_at: 2026-08-20` ✓
- 归一化：无 updated_at 的旧式 case 卡 → promote 后待编排区副本自动补上，inbox 原件保持 0 命中 ✓
- 夹具全部清理（knowledge/pending-cards/_needs_rerun/90_control/_tmp_test395 无残留）✓

### 7 张缺卡清单 → #394
已后补登记到 `task_20260820_laowantong-updated-at-supplement.md`：生产线内 1 张（pending-cards/case-wechat-2404c1658025473c）建议并入 #394 批量；inbox 原件 11 张不动（归一化兜底未来自动补）；_needs_rerun 3 张重跑自愈。本单未改任何存量卡。

### MCP 长驻进程
本次改动不涉及 MCP server 代码，无需重启事项。
