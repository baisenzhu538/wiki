---
id: task_20260701_kdo-index-lint-wikilink-format-alignment
type: task
status: queued
assignee: 黄药师
priority: P1
created_at: 2026-07-01
updated_at: 2026-07-01
reviewer: 欧阳锋
source_refs:
- 60_feedback/tasks/task_20260629_kimi-lint-content-debt-by-domain.md
related:
- task_20260629_kimi-lint-content-debt-by-domain
---

# KDO index/lint wikilink 格式对齐任务编排建议书

## 背景

#28 `lint 内容债按 domain 分批清理` 在 strategy 域清理完成后发现：所有 strategy 卡片已通过 `kdo pre-submit`，真实内容问题已清零，但 `kdo lint --domain strategy --summary` 仍报告 148 个 "Wiki page not listed in 30_wiki/index.md" WARNING。

根因不是内容问题，而是 **KDO 内部两处代码对 wikilink 格式约定不一致**：

- `kdo index --rebuild`（`kdo/commands/curation.py::auto_update_index`）生成 **bare wikilink**：
  ```markdown
  - [[case-strategy-cool-boiled-water|...]]
  - [[tool-strategy-12-word-test|...]]
  ```
- `kdo lint`（`kdo/workspace.py::_lint_index_coverage`）解析 index.md 中的 wikilink 时：
  - 若含 `/`，按 `30_wiki/<path>.md` 解析
  - 若 bare，默认按 `30_wiki/concepts/<id>.md` 解析
- 结果：cases/、tools/、frameworks/ 等目录下的卡片被错误地认为不在 index.md 中，产生大量误报。

## 目标

统一 `kdo index --rebuild`、`kdo lint --fix-index` 与 `kdo lint` 的 wikilink 路径格式，使 strategy 域 148 个 WARNING 误报清零，并为 #28 后续 domain 清理提供干净的验证基线。

## 验收标准

- [ ] `kdo index --rebuild` 生成的 `30_wiki/index.md` 中，每个 wikilink 都使用相对 `30_wiki/` 的路径格式（如 `[[cases/case-strategy-cool-boiled-water|...]]`、`[[tools/tool-strategy-12-word-test|...]]`）
- [ ] `kdo lint --fix-index` 追加的缺失条目使用与 `--rebuild` 一致的格式
- [ ] 修复后，`kdo lint --domain strategy --summary` 的 "Wiki page not listed in 30_wiki/index.md" 从 148 降至 0
- [ ] 全量 `kdo lint --summary` 的 WARNING 基数下降约 700+（全库范围误报）
- [ ] 新增或更新至少 1 个单元测试，覆盖 `auto_update_index` 与 `_lint_index_coverage` 的格式一致性
- [ ] `python -m pytest tests/ -q` 不引入新的失败

## 实现建议

### 修改点 1：`kdo/commands/curation.py::auto_update_index`

当前代码（约第 388 行）：
```python
card_id = fm.get("id") or page.stem
lines.append(f"- [[{card_id}|{title}]] — source {ref_str}")
```

建议改为使用相对于 `30_wiki/` 的相对路径（去掉 `.md` 扩展名）：
```python
rel = page.relative_to(wiki_root)
wiki_path = rel.with_suffix("").as_posix()
card_id = fm.get("id") or page.stem
lines.append(f"- [[{wiki_path}|{title}]] — source {ref_str}")
```

示例输出：
```markdown
- [[cases/case-strategy-cool-boiled-water|凉白开案例]] — source ...
- [[tools/tool-strategy-12-word-test|十二字测试]] — source ...
- [[concepts/concept-strategy-evolution-cycle|战略演进周期]] — source ...
```

### 修改点 2：`kdo/workspace.py::sync_wiki_index`

当前代码（约第 1299-1310 行）把 `30_wiki/tools/tool-x.md` 写成 `[[concepts/tools/tool-x.md|...]]`，路径前缀错误。

建议改为：
```python
concept_path = page_rel.replace("30_wiki/", "", 1).replace(".md", "", 1)
```

或直接复用 `Path.relative_to` 计算：
```python
concept_path = page.relative_to(wiki_root).with_suffix("").as_posix()
```

### 修改点 3：验证 `kdo/workspace.py::_lint_index_coverage`

确保 lint 解析逻辑能正确识别新格式。当前逻辑已支持含 `/` 的路径，大概率无需改动，但需要回归验证。

### 修改点 4：测试

新增测试文件 `tests/test_index_wikilink_format.py`，覆盖：
- `auto_update_index` 为不同子目录卡片生成正确路径格式
- `_lint_index_coverage` 对正确格式的 index.md 不报 WARNING
- `sync_wiki_index` 追加的条目格式与 `--rebuild` 一致

## 风险与回退

- **风险**：若其他代码（如 Obsidian 插件、dashboard、link-suggest）依赖 index.md 的 bare wikilink 格式，路径化后可能受影响。
- **回退**：`30_wiki/index.md` 是自动生成的，随时可用 `git checkout 30_wiki/index.md && kdo index --rebuild` 重建。
- **缓解**：修改后抽样检查 dashboard 的 wikilink 解析和 link-suggest 是否正常工作。

## 建议调度

- **优先级**：P1（阻塞 #28 多个 domain 的真实清零验证）
- **预计工时**：0.5-1 人天（含测试）
- **依赖**：无
- **阻塞**：#28 strategy/yitang 等 domain 的后续清零验收
- **建议执行者**：黄药师（KDO 基建负责人）
- **建议开始时间**：尽快，可在 #28 暂停期间插队完成

## 关联任务

- #28 `task_20260629_kimi-lint-content-debt-by-domain`：本任务修复后，#28 的 strategy 域可真实清零

---

*编排建议：欧阳锋 · 2026-07-01*
