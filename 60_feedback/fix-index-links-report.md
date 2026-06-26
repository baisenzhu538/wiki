# `kdo index` 索引链接格式修复报告

> 角色：黄药师（wiki 基建 / lint / 索引脚本）  
> 时间：2026-06-26  
> 任务：修复 `kdo index --rebuild` 生成的 `30_wiki/index.md` 与 `30_wiki/links/index.md` 的 wikilink 格式，消除 Obsidian Graph View 灰色死链云。

---

## 1. 排查结论

- `kdo` 命令对应的是一个 PyInstaller 打包的 Windows 二进制：`C:\Program Files\Python312\Scripts\kdo.exe`。
- 在仓库内未找到 `kdo index` 子命令的可修改源码（`grep` 未命中 `Backlinks Index` / `links/index` 等生成逻辑）。
- 因此采用**后处理兜底脚本**方案：每次 `kdo index --rebuild` 之后运行 `scripts/fix-index-links.py`，把索引文件中的坏格式统一修正确。

---

## 2. 修复脚本

- **新增脚本**：`C:/Users/Administrator/Desktop/wiki/scripts/fix-index-links.py`
- 修复规则（对 `30_wiki/index.md` 与 `30_wiki/links/index.md` 中的所有 `[[...]]` 生效）：
  1. 反斜杠 `\` → 正斜杠 `/`；
  2. 去掉开头的 `30_wiki/`（大小写不敏感）；
  3. 去掉文件名的 `.md` 后缀（保留 `#heading` / `^block-id` 锚点）；
  4. 保留 `|别名` 不变；
  5. 全程使用 UTF-8 读写，保护中文文件名。

执行命令：

```bash
cd C:/Users/Administrator/Desktop/wiki
kdo index --rebuild
python scripts/fix-index-links.py
```

---

## 3. `links/index.md` 修复示例

### 文件前 5 行（修复前后一致，已为正斜杠无 `.md`）

```markdown
# Backlinks Index

_Auto-generated index of `[[wikilink]]` references across wiki pages._

## [[2026-05-17-深夜感想]]
```

### 本次实际修复的残留坏链示例

| 修复前 | 修复后 |
|---|---|
| `[[concepts/bad/link.md\|test]]` | `[[concepts/bad/link\|test]]` |

> 注：本次 `kdo index --rebuild` 生成的 `links/index.md` 主体已是正斜杠、无 `30_wiki/` 前缀、无 `.md` 后缀，仅剩上述 1 处 `.md` 残留；脚本同时作为历史坏格式兜底，可处理 `[[30_wiki\\路径\\文件名.md\|别名]]` 等全部情况。

---

## 4. `30_wiki/index.md` 修复示例

### 文件前 5 行（修复前后一致）

```markdown
# Wiki Index


_Last updated: 2026-06-26T20:18:01+00:00_

```

### 格式扫描结果

- 修复前 `30_wiki/index.md` 中 wikilink 带 `.md` / 反斜杠 / `30_wiki/` 前缀的数量：**0**（当前生成版本已无此前缀问题）。
- 修复后 `30_wiki/index.md` 中 wikilink 带 `.md` / 反斜杠 / `30_wiki/` 前缀的数量：**0**。

> `index.md` 当前主要使用卡片 ID 链接（如 `[[session-...\|...]]`），脚本对这类链接无侵入；仅在后缀/前缀/反斜杠出现时进行清理。

---

## 5. `kdo lint` 验证

| 指标 | 修复前（`kdo index --rebuild` 后） | 修复后（运行 fix 脚本后） | 变化 |
|---|---|---|---|
| `ERROR:` 行数 | 1273 | 1273 | **0 新增** |
| `WARNING:` 行数 | 48251 | 48251 | **0 新增** |
| Summary | 1273 new error(s), 48251 new warning(s) (1837 accepted) | 1273 new error(s), 48251 new warning(s) (1837 accepted) | 完全一致 |

结论：修复脚本没有引入任何新的 lint ERROR 或 WARNING。

---

## 6. Obsidian Graph View 验证

- CLI 环境无法直接打开 Obsidian GUI，因此以**格式坏链扫描**作为客观代理指标：
  - `30_wiki/links/index.md` 中 `.md` 后缀、反斜杠、`30_wiki/` 前缀的 wikilink 数量：**0**
  - `30_wiki/index.md` 中 `.md` 后缀、反斜杠、`30_wiki/` 前缀的 wikilink 数量：**0**
- 人工确认步骤（请在 Obsidian 中执行）：
  1. 打开 Obsidian，进入本仓库；
  2. 打开 `30_wiki/links/index.md`；
  3. 打开 Graph View，观察 `links/index.md` 节点；
  4. 预期结果：不再出现以 `links/index.md` 为中心的灰色大圆点死链云，所有出链均指向有效卡片。

---

## 7. 变更文件清单

- `scripts/fix-index-links.py`（新增）
- `30_wiki/links/index.md`（修复 1 处 `.md` 后缀）
- `30_wiki/index.md`（无变更，当前生成版本已合规）
- `60_feedback/fix-index-links-report.md`（本报告）

---

## 8. 后续建议

1. 在 `kdo index --rebuild` 的调用处（如 Makefile、PowerShell 脚本、定时任务）追加 `python scripts/fix-index-links.py`，确保每次重建后自动兜底。
2. 若后续拿到 `kdo` 源码，建议直接修复生成逻辑中的 `os.path` / `pathlib` 输出，使索引文件原生合规，从而可以移除本后处理脚本。
