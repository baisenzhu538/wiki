---
id: 583
task_id: task_20260831_huangyaoshi-mnemosyne-memory-cache-pilot
assignee: huangyaoshi
status: pending_review
created_at: 2026-08-31
created_by: 王语嫣
trigger: 老朱 08-31 直令（「立项让黄药师试点，同时需要他跑狗粮测试来验证」）
priority: P1
batch: true
depends: 无（#582 是老顽童生产单，与本单无阻塞关系）
instance: huangyaoshi
updated_at: '2026-08-30T19:00:10.522708+00:00'
evidence: 60_feedback/diagnosis/diag_20260831_huangyaoshi-mnemosyne-dogfood.md
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

- [x] 狗粮对比表 4 维度数据齐（命中率/召回质量/延迟/token）
- [x] A/B 两组查询集各 10 条真实跑过，命令可复现
- [x] 试点场景有明确判定（三选一）
- [x] diagnosis 落盘 + queue_transition complete 提审

## 执行报告（黄药师 08-31）

**结论：部分采用。** 采用场景①「Agent 会话记忆缓存」（附条件：标题路由注入，禁全文注入）；场景②看板状态问答不采用；场景③卡片检索辅助层不采用。接入点设计已出，施工待欧阳锋终审。

### 四维对比（A 自然语言 10 条 / B 精确术语 10 条，各对 mnemo 与 kdo query 实跑）

| 维度 | mnemo A/B | kdo A/B |
|---|---|---|
| hit@5 | **100%** / 40% | 80% / 40% |
| hit@1 | **80%** / 30% | 70% / 30% |
| 中位延迟 | **102ms** / 84ms | 1253ms / 1209ms |
| token/查询 | k=5 全文 18.4k；压缩后 17.4k（-5.4%）；标题路由 **146** | 1055 / 634 |

### 关键发现
- F1 中文自然语言召回 mnemo 真实反超产线（A4 kdo 全 miss / mnemo rank=1）
- F2 精确 ID 检索两边都弱（B 组 hit@5 均 40%），该活归 grep/直查
- F3 compress_text 对高密度卡片语料只压 5.4%——「省 token」在卡片场景不成立
- F4 真 token 杠杆=注入策略：k=5 全文 25,637 tok vs 标题路由 146 tok（175 倍）
- F6 坑：recall 三元组返回/近因 boost 致 k=5 与 k=50 排序不一致/remember 无幂等/重复入库污染排名（本轮自踩自修）

### 纪律与证据
- 全部数字真实跑出可复现：`assets_20260831_mnemosyne-dogfood/`（sample_corpus.py 种子 20260831 / ingest_mnemosyne.py / run_ab_test.py / ab_results.json / corpus_manifest.json）
- 量具 tiktoken cl100k_base 真实安装（主源超时，清华镜像）；未动产线主链；实验库 5.5MB 已 .gitignore
- 事故披露：首跑 ingest 幂等清库未实现致 2 卡重复入库，已修复并干净库全量重跑，本文数字以复跑为准

**交付物**：`60_feedback/diagnosis/diag_20260831_huangyaoshi-mnemosyne-dogfood.md`（四维对比表+三选一判定+场景①接入点设计）+ `60_feedback/diagnosis/assets_20260831_mnemosyne-dogfood/`（sample_corpus.py / ingest_mnemosyne.py / run_ab_test.py / corpus_manifest.json / ab_results.json 全套可复现）
**完成内容**：50 张真实卡语料狗粮测试完成——A/B 各 10 条查询对 Mnemosyne 与 kdo query 实跑四维对比（mnemo A组 hit@5 100%/延迟102ms；kdo 80%/1253ms），判定场景①Agent会话记忆缓存采用（条件：标题路由注入）、场景②③不采用。
**验证**：`cd 60_feedback/diagnosis/assets_20260831_mnemosyne-dogfood && python sample_corpus.py && python ingest_mnemosyne.py full && python run_ab_test.py`——输出 summary 显示 mnemo A组 hit@1=0.8/hit@5=1.0/MRR=0.875、B组 hit@5=0.4；kdo A组 0.7/0.8/0.733、B组 0.3/0.4/0.35；token 实测（tiktoken cl100k_base）k=5 全文 18,406 / 压缩后 17,410 / 标题路由 146 vs kdo 1,055；延迟中位 102ms vs 1253ms。
**边界**：产线主链零改动（queue_transition/conveyor_probe 未触碰）；未装 numpy 等重依赖；tiktoken 仅测试量具不进产线；mnemo 实验库 5.5MB 已局部 .gitignore 不入 git；场景①接入点仅设计未施工；kdo CLI 延迟含 235ms 冷启动已注明。
**需要谁动作**：欧阳锋终审 #583；终审 PASS 后场景①接入点设计（90_control/mnemo_cache/ + 标题路由注入）方可立项施工。
**diagnosis**：`60_feedback/diagnosis/diag_20260831_huangyaoshi-mnemosyne-dogfood.md`

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 1 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
