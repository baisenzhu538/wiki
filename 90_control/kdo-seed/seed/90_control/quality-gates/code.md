# Code Quality Gate

A code artifact is ready for ship when ALL of the following pass:

## P0 — 阻塞合并

- [ ] **self-check 通过**：`kdo self-check --dry-run` 返回 0 issues
- [ ] **lint 通过（ERROR 级）**：`kdo lint` 返回 0 errors（warnings 不阻塞）
- [ ] **安装路径已文档化**：README 或 SKILL.md 中有 `pip install` 或等效说明
- [ ] **无硬编码密钥**：无 API key、密码、token 在源码中

## P1 — 合并前修复

- [ ] **Example usage 存在**：CLI 命令或代码示例可复制粘贴运行
- [ ] **失败模式已命名**：代码中已知的失败路径有文档记录（参考 failure-modes.md）
- [ ] **版本路径已声明**：pyproject.toml 或等效文件中版本号已更新

## P2 — 建议改进

- [ ] **测试或手动验证步骤存在**：他人可按步骤独立验证
- [ ] **日志输出有目的地**：print/logging 输出到可追踪的位置（文件或 stdout with flush）

## 禁止事项

| 禁止 | 原因 | 失败模式 |
|------|------|:--------:|
| 禁止从非 wiki 根目录执行 pipeline 命令 | find_workspace() 可能找错目录 | F-KDO-004 |
| 禁止在 state.json 被其他进程持有时执行写操作 | 覆盖写竞态 | F-KDO-003 |
| 禁止对中文内容执行 `kdo enrich --all` | regex extractor 不支持 CJK | F-KDO-001 |
