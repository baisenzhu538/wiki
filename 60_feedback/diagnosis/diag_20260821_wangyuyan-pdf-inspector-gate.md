---
title: 门禁判定——PDF-Inspector 双卡（偶遇管线 case + 外部 agent tool 草稿）
created_at: 2026-08-21
type: diagnosis/gate-decision
agent: wangyuyan
---

# 门禁判定：PDF-Inspector 双卡（2026-08-21）

## 一、来料清单（全量，无遗漏）

| # | 文件 | 来源 | 说明 |
|:--:|:---|:---|:---|
| 1 | `00_inbox/wechat-collect/src_wechat_fe60439837f4c93e.md` | 偶遇管线（微信视频 40s，tiny ASR） | 一等素材：PDF 转 Markdown 工具短视频逐字稿，ASR 错字密度高（A枕=AI、流暖器=浏览器、贷马快=代码块、多兰=多栏、低头跟消耗=低 token 消耗） |
| 2 | `00_inbox/pending-cards/case-wechat-fe60439837f4c93e.md` | 偶遇管线自动产卡（08-21 14:41 登记 INBOX-PENDING） | case 草稿：事实层基本还原原意，"洞察"层为管线 LLM 泛化 |
| 3 | `00_inbox/pending-cards/tool-pdf-inspector.md` | **小昭（外部 agent）越权写入**（08-21 22:51，未登记 INBOX-PENDING） | tool 草稿：Firecrawl PDF-Inspector，结构完整，附黄药师狗粮实测 |

## 二、门禁判定

### 判定 1：case 卡 → **合并，不入正式层**

- 信息覆盖：case 卡全部事实（20ms 分类 / 200ms 出 Markdown / 200 PDF 2.8s / Rust 本地 / 无大模型无云服务）已含于 tool 卡，且 tool 卡有官方源核验与实测补强
- case 卡"洞察"层（"先结构化再喂模型"）为管线泛化，无一手新增
- 同主题双卡只留精做一张（#120/#121 合并先例）
- 处置：frontmatter `status: superseded` + `superseded_by: tool-pdf-inspector`，已 git 固化（E037 三步走：判定→隔离→固化）

### 判定 2：tool 卡 → **入库精做，立项 #407（老顽童）**

**质量面（过门禁的理由）**：
- L7 查重：30_wiki 无 pdf-inspector 卡，真实缺口；与已有 `mineru-pdf-parsing-setup` 互补不替代（对比表清晰）
- 结构齐：aliases/tags/related/diagnostic_signals/失败模式表/质疑节（Doug Cutting 视角）/安装四入口
- 实测背书：黄药师 2026-08-21 狗粮 5 份 KDO 真实 PDF 5/5 通过（分类 conf 0.875–1.0，0.2–0.42s/份，中文无乱码，混合页正确标出）
- source_refs 三个官方源（GitHub/PyPI/Firecrawl blog）

**风险面（任务单必须覆盖的核验项）**：
1. **author 虚标**：卡面 `author: 老顽童`，实为小昭（外部 agent）产物——E018 变体（身份标注不实）。老朱已明示亲自规范小昭；本厂侧纪律：外部 agent 产物一律按"建议稿"对待，须 KDO 生产链核验 + 欧阳锋真实终审后方可转正（08-19 铁律：外部 agent 只观察审查不动手）
2. **超源内容待核**：benchmark 数字（200 PDF 0.47s、54% 文本层统计、150ms 直提、10–50ms 分类、heading 0.788 vs liteparse 0.811）均超出源视频，来自官方源转述——入库前须逐一核验官方源并回填 verified（三方法轻量版：P1 卡至少一次外部对标）
3. **定位声明**：正文开头须补定位声明（与 mineru 的互补关系/classify-then-route 在 KDO 进料链的位置），#199 门禁规则
4. **双向回链**：`mineru-pdf-parsing-setup` 加反向 related（只增不改，#384/E017 模式）

## 三、纪律记录

- 小昭本次直接写入 `00_inbox/pending-cards/`（22:51），绕过 INBOX-PENDING 登记——编排门禁照常受理（管线 A 方案：pending-cards 一律过王语嫣门禁），但越权行为本身由老朱规范，本诊断不替小昭定性
- 编排门禁=王语嫣，终审=欧阳锋（老朱 08-20 定界）——本判定为门禁级，非终审

## 四、产出

- 任务单：`60_feedback/tasks/task_20260821_laowantong-pdf-inspector-card-finalize.md`（#407，queued，老顽童）
- INBOX-PENDING 段对应行划掉
