---
id: 473
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-23T11:30:44.990674+00:00'
version: v1.0
doc_id: D-20260823-021
instance: huangyaoshi
---
# #473 文件流转 lint 遗留三项收口（#450 终审🟠🔵项）

- **任务号**：#473
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P2（欧阳锋终审遗留项，`diag_20260823_ouyangfeng-file-flow-lint-residuals.md` 采纳）
- **立项**：2026-08-23 王语嫣

## 范围（三项按优先级）

1. **🟠 wiki 卡侧 L9 扫描**：30_wiki 2000+ 卡 frontmatter 队列号/doc_id 混用检查——纯 frontmatter 正则全库一次跑（分钟级，成本可控，一次扫描即可非分批）
2. **🟠 冻结基线动态化**：采用无状态方案（file-flow-check 运行时以 PROPOSAL-PENDING 段+探针登记历史动态生成基线——比基线自动更新更稳，无同步漂移）
3. **🔵 kdo lint 集成**：file-flow-check 挂 kdo lint 检查类或 pre-submit 钩子（文件纪律进入既有质量门）

## 验证（验证分层声明）

- L1 单测三项；L2 狗粮=构造混用卡+已冻结改动各一例全被拦；L3 待活体=下次 lint 日常流程自动含文件流转检查

## 边界

- 只收口三项遗留；不动 #449 规范本体；kdo lint 集成若改动大可拆出（P2 可缓原则）

## 执行报告（F-034 五字段+验证分层声明，complete 前必填）

（生产者填写）
