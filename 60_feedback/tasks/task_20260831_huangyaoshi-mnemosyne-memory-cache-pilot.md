---
id: 583
task_id: task_20260831_huangyaoshi-mnemosyne-memory-cache-pilot
assignee: huangyaoshi
status: in_progress
created_at: 2026-08-31
created_by: 王语嫣
trigger: 老朱 08-31 直令（「立项让黄药师试点，同时需要他跑狗粮测试来验证」）
priority: P1
batch: true
depends: 无（#582 是老顽童生产单，与本单无阻塞关系）
instance: huangyaoshi
updated_at: '2026-08-30T18:59:13.417684+00:00'
---

# 任务单 #583：Mnemosyne 记忆缓存层试点 + 狗粮测试（黄药师）

## 背景

老朱问「Mnemosyne 能不能降低 token 消耗、能降多少、有效就使用」。王语嫣 08-31 已做初步实测（commit 276424871 / 8394734f0 关联诊断报告 `60_feedback/diagnosis/diag_20260831_wangyuyan-inbox-automation-fix-mnemosyne-verification.md`）：

- `pip install mnemosyne-os`（v7.0.0，MIT，PyPI 在架，repo: github.com/FrankHu-HK/mnemosyne）
- 实测 token 压缩 **79.9%**（20 轮对话模拟：全量 59,200 tokens → 预检索 11,927），与论文自报"80%+"吻合
- 已知边界：纯词法检索（BM25+中文二分词），**拉丁+数字混合实体（如 D0、C08、SKU-123）召回 0/10 全灭**，纯中文实体 10/10

## 任务（黄药师）

### 1. 狗粮测试（先做——自己先用）

用 KDO 真实数据实测，不要用玩具数据：

- **语料**：从 `30_wiki/` 抽 50 张真实卡片（含 concepts/frameworks/methods/cases 多类型）作为记忆库写入 Mnemosyne
- **查询集**：两组各 10 条——
  - A 组（它的强项）：自然语言问题（如「哪些卡讲过业务场景拆解？」）
  - B 组（已知弱项）：卡片 ID/精确术语查询（如 `diag_20260831`、`kdo-charter §2.6`、`F-061`）
- **对照组**：同样查询集跑现有 `kdo query` 检索
- **产出对比表**：命中率 / 前3召回质量 / 单次查询延迟 / token 消耗（把「送进 LLM 的检索结果」折算成 token 数对比）

### 2. 试点场景判定（狗粮结果出来后）

从 KDO 真实场景里挑一个评估适配度：

| 候选场景 | 说明 |
|---|---|
| Agent 会话记忆缓存 | 王语嫣/欧阳锋长会话中，历史诊断/裁定结论不塞全量、走 Mnemosyne 预检索 |
| 看板状态问答 | 「#582 现在什么状态」类查询走记忆层而非全量读 200KB 看板 |
| 卡片检索辅助层 | 与 kdo query 并行作为 fallback（B 组狗粮结果决定弃用与否） |

### 3. 交付

- 对比数据表 + 判定结论（采用/部分采用/不采用）+ 如果采用给出接入点设计
- 全部实测数字必须真实跑出（王语嫣 08-31 铁律：验证=实跑复现，不接受推算值）
- 结论不论正负都登记 diagnosis，狗粮失败本身也是有价值的知识（知识回路）

## 边界

- 不改 `queue_transition.py` / `conveyor_probe.py` 等产线主链（试点是旁路实验）
- 不引入重依赖破坏零依赖原则：Mnemosyne 本体零依赖可用，若需 numpy 插件先在本任务单备注说明再装
- 长任务标注 `batch: true`（F-050 方案一：不阻塞其他 pending_review 领单）
- 结论落地需欧阳锋终审后才进产线

## 验证

- [ ] 狗粮对比表 4 维度数据齐（命中率/召回质量/延迟/token）
- [ ] A/B 两组查询集各 10 条真实跑过，命令可复现
- [ ] 试点场景有明确判定（三选一）
- [ ] diagnosis 落盘 + queue_transition complete 提审
