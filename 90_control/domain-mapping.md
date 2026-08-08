# KDO 域清单映射表（单一真相源）

> 卡导航视图（domains/ 19 卡）与检索路由视图（domain-routes.yaml 10 路由）的统一映射。新增域必须三处登记：路由 + 卡 + 此表。
> 统计日期：2026-08-09（卡片数为该日快照；"—"= 无对应卡或未统计）
> 双轨设计（2026-08-09 裁定）：本表回答"KDO 有哪些域"（域清单真相源）；各域 MOC/digest 回答"怎么查该域方法论"（知识导航）——两个问题两个入口，不冲突。

## 两视图映射

| 路由视图（domain-routes.yaml） | 卡导航视图（domains/） | 中文域（白名单） | 卡片数 |
|:--|:--|:--|:--|
| AI协作 | ai-collaboration-domain-digest | — | 262 |
| KDO | kdo-moc | — | 52 |
| 五步法 | five-step-domain-digest | — | 45 |
| 内容生产 | （无对应 digest） | 内容 | 21 |
| 发布 | （无对应 digest） | — | — |
| 多模态 | （无对应 digest） | — | — |
| 战略 | strategy-domain-digest | — | 139 |
| 销售管理 | （无对应 digest） | 销售 | 23 |
| 调研 | yitang-research-domain-digest | — | 192 |
| 需求分析 | domain-demand-analysis-index | — | 25 |

## 仅有卡导航（无路由）的域

| 卡 | 说明 |
|:--|:--|
| business-formula-domain-digest | 业务公式域 |
| conversion-rate-domain-digest | 转化率域 |
| decision-science-domain-digest | 科学决策域 |
| design-moc | 设计域 MOC |
| human-ai-collaboration-double-triangle | 人机协作双三角 |
| innovation-domain-digest | 创新域 |
| lean-startup-domain-digest | 精益创业域 |
| management-domain-digest | 管理域 |
| master-moc | 通用方法论 MOC |
| product-moc | 产品域 MOC |
| retrospective-moc | 复盘主题 MOC |
| ai-basic-domain-digest | AI基本功域 |

## 中文域白名单（15 个，独立于路由+卡导航）

见 `90_control/routing-rules.md` § 中文域名白名单。

## 新增域登记规则

1. 路由侧：`90_control/domain-routes.yaml` 加条目
2. 卡侧：`30_wiki/domains/<name>-domain-digest.md` 建卡
3. 映射侧：本文件追加映射行

三处缺一不可。

> 登记：2026-08-09 黄药师 | #261 域清单对齐
