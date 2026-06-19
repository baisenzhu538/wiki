# KDO 基建变更公告

> 更新：2026-06-19  
> 面向：所有 Agent  
> **每个 Agent 启动时必须读此文件了解最新基建变更。**

## 新增工具

| 工具 | 路径 | 用途 |
|:--|:--|:--|
| 卡片可用性模拟器 | `90_control/scripts/kcard-simulate-feedback.py --batch 5` | AI 扮演用户测试卡片能否用 |
| 新卡冲突检测 | `90_control/scripts/kcard-diff-new-vs-existing.py --new <id>` | 新卡入场自动对比旧卡 |
| 精修分级器 | `90_control/scripts/kcard-refinement-grader.py --card <id>` | A/B/C/D 四级精修深度评估 |
| 域摘要卡 | `30_wiki/domains/five-step-domain-digest.md` | 读一张读完一个域 |

## 新增模板

| 模板 | 用法 |
|:--|:--|
| BTICME | `kdo scaffold --template bticme` — 背景+任务+方法+约束+示例 |
| PACED | `kdo scaffold --template paced` — 决策链还原（暗知识专用） |
| Book | `kdo scaffold --template book` — 书籍拆解 |

## 规则变更

| 规则 | 变更内容 |
|:--|:--|
| KF-025 | 三问→四问：新增"④跨域共同模式——每完成两个域做跨域对比" |
| 知识冲突 SOP | `90_control/contradiction-resolution-sop.md` — 新素材与旧卡冲突的四种处理 |
| 批量操作 P-30 | 任何批量操作前必须在任务文件声明预期变更范围 |
| 精修分级 | 格式精修(30张/批) vs 内容精修(5张/批) — 验收时区分 |

## 新增管道

| 管道 | 说明 |
|:--|:--|
| `kdo ingest --batch <subdir> --auto-scaffold` | 批量素材→卡片骨架 |
| `kdo graph bridge <dom_a> <dom_b>` | 跨域桥接检测 |
| `kdo query --view needs-review` | 预设视图过滤 |
