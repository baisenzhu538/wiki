# Capability Quality Gate

A capability (skill/workflow/playbook) artifact is ready for ship when ALL of the following pass:

## P0 — 阻塞发布

- [ ] **任务边界明确**：说清楚这个 capability 做什么、不做什么
- [ ] **输入/输出已声明**：输入什么格式的数据/文件，输出什么
- [ ] **工具权限已声明**：需要哪些 CLI 命令、文件系统权限、API 访问

## P1 — 发布前修复

- [ ] **失败处理已文档化**：如果中途失败，如何恢复？哪些状态需要回滚？
- [ ] **Eval 用例存在或已计划**：至少有一个可验证的"正确执行"测试场景
- [ ] **运行时日志有目的地**：执行过程中的输出去哪里（stdout/文件/state.json）

## P2 — 建议改进

- [ ] **与其他 capability 的边界清晰**：不重复已有能力的功能
- [ ] **可组合**：输出格式能被下游 capability 消费（如 produce 的输出能被 ship 使用）

## 禁止事项

| 禁止 | 原因 |
|------|------|
| 禁止 capability 依赖未文档化的外部状态 | 下一个 Agent session 可能无法复现 |
| 禁止静默失败 | 任何失败路径必须有可见输出（stderr/log/exit code ≠ 0） |
