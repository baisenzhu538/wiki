---
title: "kdo watch 定时巡检层技术说明"
author: "审查者欧阳锋"
role: "知识架构师 (Knowledge Architect)"
created_at: "2026-05-04"
status: proposed
implementor: "黄药师 (Builder)"
dependency: "已有 kdo watch（inbox 监听 + 自动 ingest → enrich → 重建索引）"
---

# kdo watch 定时巡检层技术说明

> kdo watch 已解决了"新素材进来自动走流水线"的问题。
> 本文件定义缺失的那一半——已有知识库的健康状态持续监控。

---

## 零、当前状态 vs 目标

| 已有 | 缺失 |
|------|------|
| 监听 inbox → 自动 ingest → enrich → index rebuild | 定时健康检查（不会周期性扫描 stale TODO） |
| 1.5 秒防抖，过滤临时文件 | 主动推送（没有"3 个页面超期未更新"提醒） |
| 单次任务触发 | 周期性巡检（每天/每小时） |

---

## 一、巡检项（6 项）

### 1. 残留 TODO 占位符

扫描 `30_wiki/concepts/` 中所有 `.md` 文件，检查是否包含 `TODO:` 前缀（精确匹配，不含冒号后的描述性文本）。

- **阈值**：> 0 个 TODO → 告警
- **输出**：文件名 + TODO 所在行 + 该文件最后更新日期

### 2. 低信任源

扫描 `10_raw/sources/` 中所有源文件的 frontmatter，检查 `trust_level` 字段。

- **阈值**：`trust_level: low` → 告警
- **输出**：源文件名 + trust_level + 依赖它的 wiki 页面列表

### 3. 孤立页面

扫描 `30_wiki/` 所有页面，检查是否有任何其他页面通过 `[[wikilink]]` 指向它。没有任何入链的页面为"孤立"。

- **排除**：`index.md`、`log.md`、`contradictions.md`（基础设施文件）
- **阈值**：> 0 个孤立 → 告警

### 4. 超期未更新

扫描 `30_wiki/` 所有页面的 frontmatter `updated_at`，超过 30 天未更新的标记。

- **阈值**：> 0 个超期 → 提示（非告警）
- **输出**：文件名 + 最后更新日期 + 距今多少天

### 5. 矛盾未解决

检查 `30_wiki/contradictions.md` 中的表格，统计 `Current judgment` 列包含"待检查"或"未解决"的条目。

- **阈值**：> 0 条未解决 → 告警
- **输出**：矛盾主题 + 涉及页面 + next check 日期

### 6. 重复页面检测

扫描 `30_wiki/concepts/` 中 title 相似度高的页面（如 `紫鲸AI...` 的两个版本）。

- **方法**：提取所有页面的 title 字段（frontmatter），对 title 做最小编辑距离比较。
- **阈值**：编辑距离 < title 长度的 30% → 告警

---

## 二、输出格式

### 控制台输出

```
kdo watch --health

KDO 健康巡检 — 2026-05-04 14:30
┌──────────────────────────────────────┐
│ ⚠️  TODO 残留: 1                      │
│ ⚠️  孤立页面: 3                       │
│ ⚠️  矛盾未解决: 1                     │
│ ℹ️  超期未更新: 2                     │
│ ✅  低信任源: 0                       │
│ ✅  重复页面: 0                       │
└──────────────────────────────────────┘
综合评分: 3/6 项异常，建议关注。
```

### 写入文件（用于 Agent 消费）

巡检结果自动写入 `60_feedback/eval-results/health_YYYY-MM-DD.md`，每次覆盖当天文件。

---

## 三、触发方式

两种模式：

```
kdo watch --health            → 手动跑一次巡检，输出到控制台 + 文件
kdo watch --health --cron 24h → 后台定时模式，每 24 小时自动巡检
```

定时模式不弹窗，静默写入文件。Agent 下次启动时读取最新健康报告。

---

## 四、实现约束

| 约束 | 说明 |
|------|------|
| 纯标准库 | 不引入新依赖（wikilink 解析用 regex） |
| 不阻塞主流水线 | 巡检和 inbox 监听是独立线程/进程 |
| 不修改文件 | 只读扫描，不自动修复（修复由 Agent 决定） |
| 当天覆盖 | 同一天的巡检结果覆盖前一次，不堆积历史文件 |

---

## 五、与现有 kdo watch 的接线

```
kdo watch 现有线程:
  → 监听 inbox → 新文件 → ingest → enrich → graph rebuild

kdo watch 新增线程（独立，不互锁）:
  → 定时触发 → 跑 6 项巡检 → 写入 health_YYYY-MM-DD.md
```

---

## 六、触发策略（最终方案）

### 生产环境

```
WSL crontab（黄药师机器）
  → 每天凌晨跑一次 kdo watch --health
  → 静默写入 60_feedback/eval-results/health_YYYY-MM-DD.md
```

**为什么选 crontab 而不是 kdo watch 内置 cron：**

| 维度 | crontab | kdo watch --cron |
|------|:-------:|:----------------:|
| 进程依赖 | 无（系统级调度） | watch 进程必须常驻 |
| 终端关闭后存活 | ✅ | ❌ |
| 重启后恢复 | ✅ 自动 | ❌ 需手动重启 watch |
| 故障排查 | 系统日志 | 需自行实现 |

### 消费端

```
欧阳锋（Architect Agent）
  → 每次会话启动时读取当天 health_*.md
  → 发现异常直接告知用户
  → 用户零操作，被动接收健康状态
```

### 手动触发（保留）

用户可随时在飞书让黄药师跑：
```
kdo watch --health
```
适用于刚修完一批问题，想立刻看效果。

---

*技术说明完成时间：2026-05-04*
*审查者欧阳锋*
