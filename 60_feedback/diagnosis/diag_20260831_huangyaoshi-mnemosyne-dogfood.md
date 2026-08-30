---
id: diag_20260831_huangyaoshi-mnemosyne-dogfood
title: Mnemosyne 记忆缓存层狗粮测试——50卡真实语料 A/B 对比与试点场景判定
type: diagnosis
status: REVIEW-PENDING
author: 黄药师
reviewed_by: pending
created_at: '2026-08-31'
task_ref: '60_feedback/tasks/task_20260831_huangyaoshi-mnemosyne-memory-cache-pilot.md (#583)'
domain:
  - kdo-infra
related:
  - "[[diag_20260831_wangyuyan-inbox-automation-fix-mnemosyne-verification]]"
  - "[[method-kdo-inbox-annotation]]"
source_refs:
  - 60_feedback/diagnosis/assets_20260831_mnemosyne-dogfood/ (全部脚本+原始数据可复现)
---

# 诊断：Mnemosyne 狗粮测试——用 KDO 真实卡片测「记忆缓存层」成色

> **一句话结论**：Mnemosyne 在 KDO 真实语料上**自然语言检索质量超过现产线 kdo query**（hit@5 100% vs 80%，延迟 1/12），但**作为「检索后注入上下文」的机制 token 成本爆炸**（k=5 全文 25,637 tok vs 标题路由 146 tok，差 175 倍）；压缩层实测无效（-5.4%）。**判定：部分采用——采用场景①「Agent 会话记忆缓存」，但注入策略必须取标题+摘要路由而非全文注入**；场景②不采用（kdo query 词法已够）；场景③不采用（B 组硬伤+无增量价值）。

---

## 0. 实验设置（全部真实跑出，可复现）

| 项 | 值 |
|---|---|
| 引擎 | mnemosyne-os 7.0.0（pip，MIT，零额外依赖） |
| 对照组 | `kdo query`（vault 全库生产索引，词法+frontmatter 打分，LightRAG 未装自动降级） |
| 语料 | 30_wiki 真实卡片 50 张（frameworks 12 / concepts 14 / cases 12 / dark-knowledges 8 / methods 4），固定种子 20260831 分层抽样，排除 index/digest 索引卡，共 222,880 字符 |
| 查询集 | A 组 10 条自然语言（mnemo 预期强项）/ B 组 10 条精确术语+卡片ID（任务单标注的已知弱项），每条带 ground truth 目标卡 |
| 量具 | token 计数 = tiktoken cl100k_base（真实安装，非估算）；延迟 = perf_counter 实测 |
| 隔离 | mnemo 实验库独立目录（assets_*/mnemo_store/，5.5MB，不入 git），project=kdo-dogfood-583；kdo 用生产库只读 |
| 公平性 | mnemo k=5 vs kdo --limit 5；双方查前暖场；mnemo 查询 ~102ms、kdo 查询 ~1253ms（CLI 冷启动基线 235ms，净检索 ~973ms） |
| 复现 | `python sample_corpus.py && python ingest_mnemosyne.py full && python run_ab_test.py`（脚本+manifest+原始 JSON 全部在 assets 目录） |

**纪律声明**：本轮曾出现一次方法论事故并已修复——首跑 ingest 的「幂等清库」只有注释没有实现，probe 2 张+full 50 张导致 2 张卡重复入库污染排名。发现后改为真清库（rmtree 重建）并全量重跑，本文所有数字以干净库复跑为准。这本身就是狗粮的价值：没有真实使用，发现不了自己的 bug。

## 1. A/B 四维对比总表（干净库，20 查询×2 引擎）

| 维度 | 引擎 | A组·自然语言(10条) | B组·精确术语(10条) |
|---|---|---|---|
| **命中率 hit@1** | mnemo | **0.8** | 0.3 |
| | kdo | 0.7 | 0.3 |
| **命中率 hit@5** | mnemo | **1.0** | 0.4 |
| | kdo | 0.8 | 0.4 |
| **MRR** | mnemo | **0.875** | 0.325 |
| | kdo | 0.733 | 0.35 |
| **中位延迟** | mnemo | **102ms** | **84ms** |
| | kdo | 1253ms（净~973ms） | 1209ms（净~973ms） |
| **送入 LLM 的 token/查询** | mnemo（k=5 全文） | 18,406 | 16,288 |
| | mnemo（k=5 compress_text L2 后） | 17,410（-5.4%） | 15,424（-5.4%） |
| | mnemo（标题路由，见 §3） | **146** | **146** |
| | kdo（结果块全文） | 1,055 | 634 |

## 2. 关键发现（狗粮吃出来的）

### F1 · 自然语言检索质量：mnemo 真实反超产线（重要修正）
王语嫣 08-31 初测的「80% 压缩」数字成立，但那是会话记忆场景；**在 KDO 卡片检索场景，mnemo 的 BM25+TF-IDF+近因融合对中文自然语言问题的召回显著优于 kdo query 的词法+frontmatter 打分**：A 组 hit@5 100% vs 80%，MRR 0.875 vs 0.733。A4（专家访谈十步法）kdo 完全 miss 而 mnemo rank=1；A8（单元模型六段）mnemo rank=4、kdo 前 30 名都没有。

### F2 · 精确术语/拉丁 ID：两边都烂，mnemo 没有特别加分
B 组 hit@5 双方都只有 0.4。卡 ID 直查（B2 `yt-unit-model-ladder`）mnemo 排到第 8、kdo 前 30 名都捞不到——**kdo 的 frontmatter 打分对「查 ID 找卡」这个动作基本失能**。但 mnemo 靠的也主要是「近期写入 boost」而非词法（王语嫣初测「拉丁+数字混合实体 0/10」的结论在本语料上部分复现：混合实体能召回但排不进 top5）。双方都解决不了精确 ID 检索，这活该 grep/文件名直查干。

### F3 · compress_text 压缩层对卡片语料无效
论文口径 79.9% 压缩在「对话轮次」语料上成立，但对**信息密度极高的知识卡片**只压掉 5.4%（17,410 vs 18,406 tok）——卡片没有多少语气词/停用词可删。**「Mnemosyne 能省 token」在卡片检索场景不成立**，这是本轮最重要的负结论。

### F4 · 真正的 token 杠杆在注入策略，不在检索引擎
同一查询 k=5：全文注入 25,637 tok → 只取标题行 146 tok（**175 倍差**）→ 标题+frontmatter 摘要约 400-600 tok（估算，量级参考）。mnemo 的 value 在**对自然语言 queries 的精准排序能力**（hit@1 0.8），把它当「路由器」用——先小 k 定位卡，再按需 load_file——token 成本从万级降到百级。

### F5 · 延迟差一个数量级
mnemo 84-102ms（进程内），kdo 1209-1253ms（CLI 冷启动 235ms+全库扫描）。对「会话内高频记忆查询」这个场景，1.2s 的单查延迟放大到长会话里不可忽略。

### F6 · 已知行为/坑（接入设计必读）
- recall 返回 `(score, record, reasons[])` 三元组；`reasons` 含「近期」标签的得分含近因 boost，**每次查询后近期集合变化，k=5 与 k=50 的融合排序不一致**（B1 在 k=5 miss、k=50 排第 5）
- remember() 幂等靠调用方保证：重复 remember 同一 content 产生多条记录（本轮事故根因）
- 库写入 50 卡/2.1s（0.04s/卡），冷启动加载可接受
- tiktoken 在 PyPI 主源 3.13 轮子下载超时（代理），换清华镜像可装；不装 tiktoken 则 mnemo 退化为「4字符≈1 token」启发式

## 3. 试点场景判定（三选一）

| 候选场景 | 判定 | 依据 |
|---|---|---|
| **① Agent 会话记忆缓存**（诊断/裁定结论走 mnemo 预检索） | ✅ **采用（附条件）** | F1 召回质量反超+F5 延迟 1/12 完美命中该场景；条件=注入策略走标题路由（F4），禁全文注入（F3 已证压缩无效） |
| **② 看板状态问答**（「#582 什么状态」走记忆层） | ❌ 不采用 | 看板是强结构化单文件，正则/直读 200KB 比维护一份会过期的记忆副本更准更省；且 F2 表明精确 ID 类查询恰是 mnemo 弱项 |
| **③ 卡片检索辅助层**（与 kdo query 并行 fallback） | ❌ 不采用 | fallback 语义=mnemo 兜 kdo 的失败查询，但 B 组证明两者失败面高度重叠（F2），兜不住；A 组 kdo 已 80 分、增量有限，双引擎运维成本>收益 |

**接入点设计（场景①，仅设计不施工——施工需欧阳锋终审）**：

```
Agent 长会话启动
  → MnemosyneMemory(base_dir=<vault>/90_control/mnemo_cache/, k=3)
  → 历史诊断/裁定文档 remember() 入库（source=diag_id, project=按角色隔离）
  → 会话中需要历史结论时: recall(query, k=3) 取 record.meta.wiki_path
  → 只注入 标题+一句话摘要（~150 tok/条），需要细节再 load_file
  → 禁用: recall 全文直接塞 prompt / compress_text 当压缩层依赖
```

预期收益（按本测试量级推算，需试点期实测校准）：单次历史查询注入成本从「读全文档 5-10k tok」降到「~450 tok 路由+按需加载」，长会话 10 次历史查询约省 50-90% 的记忆上下文 token。

## 4. 边界遵守声明

- 未改 queue_transition.py / conveyor_probe.py 等产线主链 ✅（全部实验在 60_feedback/diagnosis/assets_* 旁路目录）
- 未引入 numpy 等重依赖 ✅（mnemosyne-os 零额外依赖可跑；tiktoken 仅测试量具）
- 产线未受影响：mnemo 实验库独立目录不入 git（.gitignore 已置）✅
- CRLF 保持 ✅（本文件及 assets 内 .py 均为 CRLF）

## 5. 可复现命令

```bash
cd 60_feedback/diagnosis/assets_20260831_mnemosyne-dogfood
pip install mnemosyne-os
pip install tiktoken -i https://pypi.tuna.tsinghua.edu.cn/simple   # 量具，主源代理超时
python sample_corpus.py          # 抽50卡 -> corpus_manifest.json
python ingest_mnemosyne.py full  # 入库（幂等：rmtree重建）
python run_ab_test.py            # A/B 20查询 -> ab_results.json + 控制台summary
```

---

*狗粮结论不论正负都登记——本轮最有价值的产出恰是 F3（压缩层对卡片语料无效）和 F6 的四个坑：这些是读论文读不出来的。*
