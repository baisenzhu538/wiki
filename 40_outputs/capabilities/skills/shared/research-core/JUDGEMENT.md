# P1 三层判定书——调研能力层整合（#594，2026-09-02 Skills 助理）

> 老朱 09-02 拍板：调研能力是最基础的必备能力，17 skill 综合深挖为全 agent 基础能力层。
> 判定原则（SPEC §四 P1）：可执行化（有步骤/触发/失败模式）→ Go；功能重叠 → 合并为单节点双源；独立场景 → 保留独立武器；认知型/非调研 → 明确不并入。

## 三层结构裁定

```
research-core（新产：统一入口层）
├── 第一层 意图路由：OSCAR 分类 → 判断调用哪类子能力（吸收原 research 入口）
├── 第二层 核心纪律（所有调研必经）：
│   ├── 交叉验证（research-cross-validation + six-layer-cross-validation 合并判定→单节点双源）
│   ├── 质量门禁（research-quality-gate）
│   └── 深挖引擎（nine-layer-deep-dig + research-sats 合并判定→单节点双源）
└── 第三层 专项武器库（按需载入，渐进式披露第三层）：
    行业报告/财报/专家访谈/替代数据/OSINT/爬虫/Dorking/媒体验证/多Agent/CI情报
```

## 17 skill 逐一归属

| # | skill | 判定 | 归属 | 理由 |
|:--|:--|:--|:--|:--|
| 1 | research | 改造后 Go | 入口层（并入 research-core） | 原统一入口已有 OSCAR 意图分类骨架，直接吸收进 research-core 第一层；原文件改薄壳重定向（防旧引用断裂） |
| 2 | research-cross-validation | Go | 纪律层·交叉验证（双源一） | 信源层级 L1-L6 + 多重身份验证，可执行步骤+失败模式齐全 |
| 3 | six-layer-cross-validation | Go | 纪律层·交叉验证（双源二） | 六维验证（来源/时间/逻辑/数据/反例/行动）与 #2 功能重叠 → 合并为单节点双源，执行互补 |
| 4 | research-quality-gate | Go | 纪律层·质量门禁 | 六维门禁可执行化最高，BLOCKING 语义清晰 |
| 5 | nine-layer-deep-dig | Go | 纪律层·深挖引擎（主框架） | 九层深挖自我纠错迭代，L1-L9+停止条件+禁止项，深挖主框架 |
| 6 | research-sats | Go | 纪律层·深挖引擎（分析技术） | CIA SATs 四项技术为深挖引擎的分析增强（KAC/魔鬼代言人/Red Team/Indicators）→ 与 #5 合并为单节点双源 |
| 7 | research-industry-report | Go | 武器库·行业报告 | Doris 四步法+搜索七技，独立场景 |
| 8 | research-financial-report | Go | 武器库·财报 | 财报/招股书深度解读，独立场景 |
| 9 | research-expert-interview | Go | 武器库·专家访谈 | 黄金十步法+5 陷阱，独立场景 |
| 10 | research-alt-data | Go | 武器库·替代数据 | 按预算分级数据源，独立场景 |
| 11 | research-osint | Go | 武器库·OSINT | 工具链矩阵+决策树，独立场景 |
| 12 | research-web-scraping | Go | 武器库·爬虫 | 10 工具+合规红线，独立场景 |
| 13 | research-google-dorking | Go | 武器库·Dorking | 高级搜索+域名情报，独立场景 |
| 14 | research-media-verification | Go | 武器库·媒体验证 | 反向搜索→元数据→天气阴影链，独立场景 |
| 15 | research-multi-agent | Go | 武器库·多Agent | 四架构+OSCAR Pipeline 实现，独立场景 |
| 16 | research-ci-framework | Go | 武器库·CI情报 | 持续竞争情报循环，独立场景 |
| 17 | knowledge-collision | Go（改造后） | 明确不并入（保留独立，前置纪律） | 产出前碰撞知识库——适用写作/分析/咨询等所有综合任务，非调研专属；research-core 纪律层引用为「调研启动前知识碰撞」可选前置，不并入本层主体 |

## 反触发结论

- 非调研任务（纯写卡/纯施工/纯格式整理）：不路由进本层（research-core 触发条件反触发已写死）
- knowledge-collision 为通用产出纪律，保留独立挂载（王语嫣既有引用），research-core 仅引用不吞并

## 边界遵守

- ✅ 只动入口（research-core 新产 + research 改薄壳）+ 子策略 frontmatter（description 对齐路由面）
- ✅ 子策略正文一律不动（除 research 薄壳重定向）
- ✅ 不扩军：武器库 10 个保持原样，只整合不新增
