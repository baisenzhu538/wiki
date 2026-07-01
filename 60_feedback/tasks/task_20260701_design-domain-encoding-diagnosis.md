---
id: task_20260701_design-domain-encoding-diagnosis
type: task
status: reviewed
assignee: kimi
priority: P1
created_at: 2026-07-01
updated_at: '2026-07-01T13:43:36.007038+00:00'
reviewer: 欧阳锋
source_refs:
- 60_feedback/tasks/task_20260629_kimi-lint-content-debt-by-domain.md
related:
- task_20260629_kimi-lint-content-debt-by-domain
reviewed_by: 欧阳锋
review_date: '2026-07-01'
---

# design domain 编码损坏诊断任务编排建议书

## 背景

#28 `lint 内容债按 domain 分批清理` 在推进 design domain 时遇到硬阻塞：

- 大量 design domain 中文文件名/标题显示为乱码
- 用 utf-8、gbk、gb2312 均无法正确解码
- 继续用常规文本工具读取或改写这些文件，可能加剧损坏

目前不确定这是：
1. **终端显示层问题**：文件本身完好，只是 Git Bash / Windows Terminal 编码配置导致显示乱码
2. **文件真实损坏**：字节流被错误编码写入，内容已不可恢复
3. **混合编码**：同一目录下部分文件 UTF-8、部分 GBK/GB18030/BIG5

在明确根因前，**禁止批量修改 design domain 文件**。

## 目标

在不修改任何 design domain 文件的前提下，完成编码损坏根因诊断，并给出后续处理建议：
- 若只是显示问题：给出正确的读取/显示方法
- 若是真实损坏：给出能否从备份恢复、是否需要弃用重建
- 若是混合编码：给出安全批量转换方案

## 验收标准

- [x] 输出一份诊断报告（Markdown，存放于 `60_feedback/reviews/design-encoding-diagnosis-20260701.md`）
- [x] 报告中包含：抽样文件清单、字节序检测、编码推测、与备份对比结果、损坏程度评估
- [x] 对 design domain 下所有 `.md` 文件给出分类标签：`healthy` / `display-only` / `recoverable` / `corrupted`
- [x] 报告中给出下一步明确建议：继续清理 / 批量恢复 / 批量转换 / 弃用重建
- [x] 整个诊断过程中**不修改任何原始文件**（只读操作）
- [x] 若发现 content 本身已无法恢复，列出需要重新生产的卡片清单（结果：0 个 corrupted）

## 执行结果

### 已产出

| 文件 | 路径 | 说明 |
|---|---|---|
| 诊断报告 | `60_feedback/reviews/design-encoding-diagnosis-20260701.md` | 完整诊断报告，含结论、方法、数据、抽样验证、建议 |
| 分类数据 | `60_feedback/reviews/design-encoding-classification-20260701.json` | 196 个文件的详细检测数据 |

### 核心结论

- **总文件数**：196
- **healthy**：196
- **display-only**：0
- **recoverable**：0
- **corrupted**：0

**根因**：design domain 文件没有真实编码损坏。所谓"乱码"是 Windows Git Bash 终端用 GBK 编码显示 UTF-8 中文导致的显示层问题。所有文件内容均可正常 UTF-8 解码，git 历史可追溯，文件从首次提交起即为 UTF-8。

### 验证

```text
Pre-Submit Gate Report
Files checked: 1
Passed:        1
Failed:        0
All gates passed. Ready for human review.
```

### 下一步建议

- design domain 文件可以安全加入 #28 清理列表。
- 清理时需使用 UTF-8 环境（Python 脚本），避免在 GBK 终端中直接操作中文文件名。
- 建议统一行尾符为 LF（当前多为 CRLF）。

## 实现建议

### 步骤 1：范围界定

1. 列出 `30_wiki/design/` 下所有 `.md` 文件
2. 记录每个文件的：文件名、文件大小、修改时间、当前 git 状态
3. 用 Python 脚本批量检测每个文件的字节特征：
   - BOM 标记（UTF-8-BOM / UTF-16 LE / UTF-16 BE）
   - 是否包含空字节 `\x00`
   - 高字节分布（判断是否为 GBK/GB18030/BIG5）

### 步骤 2：编码推测

对每个文件尝试用以下编码解码，记录最佳候选：
- `utf-8`
- `utf-8-sig`
- `gb18030`（兼容 gbk/gb2312）
- `big5`
- `latin-1`（兜底，不会抛错）

可使用 `chardet` 或 `charset-normalizer` 辅助判断，但不要仅依赖库输出，需人工抽检。

### 步骤 3：与备份/历史版本对比

1. 检查 `.kdo/backups/` 或 git 历史是否有未损坏版本
2. 对比当前文件与最近一次正常备份的 hash
3. 若 git 历史中有正常版本，用 `git show <commit>:30_wiki/design/<file>` 读取并对比

### 步骤 4：抽样人工验证

1. 从 `healthy`、`display-only`、`recoverable`、`corrupted` 四类中各选 2-3 个样本
2. 用正确的编码打开，检查 frontmatter 是否完整、body 是否可读
3. 截图或复制关键片段到诊断报告中

### 步骤 5：输出报告

报告结构建议：
```markdown
# design domain 编码损坏诊断报告

## 结论摘要
- 总文件数：N
- healthy：N
- display-only（仅显示乱码，内容完好）：N
- recoverable（编码错误但可转换恢复）：N
- corrupted（内容已不可恢复）：N

## 下一步建议
（继续清理 / 批量恢复 / 批量转换 / 弃用重建）

## 详细检测数据
| 文件 | 大小 | 推测编码 | 分类 | 备注 |
| ... |

## 抽样验证
...

## 恢复/转换方案（如适用）
...
```

## 参考脚本

```python
from pathlib import Path
import chardet

for p in sorted(Path("30_wiki/design").rglob("*.md")):
    raw = p.read_bytes()
    guess = chardet.detect(raw)
    print(p, guess)
```

## 风险与禁忌

- **禁忌 1**：诊断完成前，禁止用 `write_text` 覆盖任何 design domain 文件
- **禁忌 2**：禁止在编码未明确前用 `errors="replace"` 批量回写，会永久丢失原始字节
- **风险**：若文件真实损坏且没有备份，可能需要人工重新生产卡片
- **回退**：本次任务只读，不存在回退问题

## 建议调度

- **优先级**：P1（阻塞 #28 design domain 清理，且涉及数据安全）
- **预计工时**：0.5-1 人天
- **依赖**：无
- **阻塞**：#28 design domain 的内容清理
- **建议执行者**：老顽童(WorkBuddy) 或擅长文件编码/数据恢复的实例
- **建议开始时间**：可与 KDO index/lint 基建任务并行；但必须在 design domain 清理前完成

## 关联任务

- #28 `task_20260629_kimi-lint-content-debt-by-domain`：本诊断完成后，design domain 才能安全加入 #28 的清理列表

---

*编排建议：欧阳锋 · 2026-07-01*
