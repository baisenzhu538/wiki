# Sprint 12 Batch C — Concept 层编译

## 任务方：黄药师

## 背景

Batch A（25 framework 卡 v1.5 回溯）✅、Batch B（77 tool 卡 v1.5 回溯）✅。Batch C 是概念层——跨域提炼的最高抽象 ~30 张 `type: concept` 卡。

## 任务

在 `30_wiki/concepts/` 下编译约 30 张 concept 卡。concept 卡是**跨多域抽象**，不是 tool 的"怎么用"，是"这是什么元概念、它在 vault 里的位置、它连接了哪些域"。

### Step 1：盘点已有 concept 卡

先跑 `kdo cards --type concept` 看 vault 里已有哪些 concept 卡，对齐编号。

### Step 2：确认待编译清单

concept 卡覆盖以下跨域元概念（非最终清单，先盘点再确认）：

| 概念簇 | 示例 |
|--------|------|
| 武器库 | yt-concept-weapon-kit（已完成） |
| IPO 模型 | agent 输入-处理-输出通用框架 |
| 链路 | capture→ingest→enrich→produce→validate→ship 的端到端概念 |
| 质量门 | quality gate 的通用概念（非具体门） |
| 复合编译 | 三步编译法 + 交叉验证的元概念 |
| 反馈闭环 | feedback→improve 跨域通用概念 |
| 溯源 | source→wiki→artifact 可追溯性元概念 |
| token 经济 | KF-024 对应的"知识密度 vs token 预算"概念 |

### Step 3：编译

每张 concept 卡按标准三步编译法（浓缩→质疑→对标），但 concept 层对标必须**跨 ≥3 个域**引用。单域引用 = 降级为 tool 卡。

### v1.5 标准

- 外部攻击：≥1 真实学者/思想家的具体论证
- 不要用场景：≥2 行表格，含失效机制 + 替代方案
- Action Triggers：≥3 个，三列（触发场景 + 第一动作 + 可验证成功指标）
- KF-024：concept 卡 estimated_tokens ≤3500，>5000 强制拆分

## 附带 P0

```bash
pip install pytest
cd "C:\Users\Administrator\Knowledge Delivery OS 0.0.1"
pytest
```

如果测试不过，修到过。这是 P0——KDO CLI 至今 11 个测试文件没跑过。

## 附带 P1

KDO 源码备份到坚果云（删 `.git/` + `__pycache__/` + `build/`，压缩后放到坚果云同步目录）。

## 交付物

1. ~30 张 concept 卡，全部通过 `kdo lint`
2. pytest 跑通
3. KDO 源码 zip 在坚果云

## 完成标志

发消息 @欧阳锋，附 concept 卡清单（表：id / title / 跨域引用数）。
