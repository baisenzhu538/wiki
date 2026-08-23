---
id: 456
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-23T07:47:40.556053+00:00'
version: v0.1
instance: huangyaoshi
---
# #456 记忆胶囊 agent_id 统一 + 审计器解析盲区修复（两小修复合一单）

- **任务号**：#456
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P2（两个小修复，合并避免碎片化；素材来自两份建议书编排决策）
- **立项**：2026-08-23 王语嫣（风清扬查询通道建议书建议 3 + 欧阳锋 #188 残留处置建议之审计器修复项）

## 任务 1：记忆胶囊 agent_id 统一（风清扬建议 3 采纳）

- 统一口径：拼音角色名 `fengqingyang / wangyuyan / ouyangfeng / laowantong / huangyaoshi / hongqigong / duanwangye`（无工具名、无中文）——与 #444 frontmatter assignee 角色名口径同族
- 库 `~/.kdo-memory/L0/activity_log.db`：清 `__test434__` 测试残留；`老顽童`（中文）历史事件改 `laowantong`（或迁移注明）
- 写入端对齐：daily-context-save 挂钩（#434）写入的 agent_id 以本口径为准，防继续混入
- 只动数据层与写入端口径；query 命令**不在本单**（挂 F-045 等老朱拍板 L1 开放口径）

## 任务 2：审计器解析盲区修复（欧阳锋 #188 处置建议采纳）

- `audit_queue_integrity.py`：行数异常的队列行**禁止静默跳过**——应报「无法解析」并列入报告（#188 实证：双列数异常行被跳过，掩盖 pending_review 残留，审计器报 0 不一致=假阴性）
- 修复后全量重跑审计，输出真实残留清单（可能不止 #188 一条）交王语嫣编排处置

## 验证（验证分层声明）

- L1：单测（agent_id 清洗用例/解析异常报错用例）
- L2：狗粮——修复后审计器跑出 #188（已知残留）= 盲区消除实证；agent_id 清洗后 status/verify 走通
- L3 待活体：下次真实 daily-context-save 写入的 agent_id 落库为新口径

## 边界

- 不做 query 命令（F-045 待拍板）；不动 memory_capsule.py 的 L0→L1 改名（F-044）；不碰队列状态机

## 执行报告（F-034 五字段+验证分层声明，complete 前必填）

（生产者填写）
