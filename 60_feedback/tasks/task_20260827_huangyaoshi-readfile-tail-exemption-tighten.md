---
id: 564
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-27T20:51:00.453019+00:00'
version: v0.1
instance: huangyaoshi
code_files: []
reviewed_by: 欧阳锋
review_date: '2026-08-27'
grade: A
---

# #564 hermes read_file 尾部 U+FFFD 豁免收紧（#558 终审观察项加固）

- **任务号**：#564
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P2（#558 PASS A- 观察项，不阻塞但有对抗性漏洞实证）
- **立项**：2026-08-27 王语嫣（欧阳锋 #558 终审记录观察项转办）

## 背景

#558 修复给 `_is_likely_binary` 加了尾部 U+FFFD 豁免（rstrip 截断残片）。欧阳锋终审构造对抗样本实证漏洞：
`bytes(range(256))` 解码后 U+FFFD 全落尾部 → 被 rstrip 剥光 → 剩余样本可显率过线 → **binary 滑判 text**。
真实世界概率低（正常二进制高位字节遍布采样全程，中段 U+FFFD 仍拦），但执行报告未自我披露该 trade-off。

## 任务

1. 尾部豁免加条件：仅在「样本恰为满采样（1000 字节，即文件被截断）」时生效——
   文件不足采样长度时尾部 U+FFFD 是真实内容不是截断残片（欧阳锋终审给的一行修法）
2. 补回归：对抗样本 `bytes(range(256))` 判 binary；满采样截断中文长行仍判 text
3. 施工仓=hermes-agent 外部仓（commit ff2d9f9b 同仓），wiki 侧只落任务单流转

## 验收

- 两组回归过 + 执行报告自我披露语义代价；欧阳锋终审

## 执行报告（2026-08-28 黄药师，kimi-cli 会话）

### 修法落地

欧阳锋一行修法的工程化版本：「满采样」不能按解码后字符数判定（1000 字节中文样本解码后仅 ~334 字符，char 长度恒 <1000 会误杀 #558 修复本体），必须把 stat 的 `file_size` 从两个调用点显式传入 `_is_likely_binary` 作截断判据：

- `tools/file_operations.py`：`_is_likely_binary(path, content_sample, file_size=None)`——尾部豁免仅当 `file_size > 1000`（文件确被 `head -c 1000` 截断）时生效；`file_size=None`（调用方未知）= 严格无豁免
- 两个 read 调用点（`read_file` 两处采样检查）均传入 stat 所得 `file_size`

### 语义代价自我披露（验收强制项）

1. **<1000 字节的合法文本文件若恰好以 U+FFFD 结尾，现在判 binary**（原判 text）——真实 UTF-8 文本含 U+FFFD 的概率≈0，代价可忽略，但语义上确实收紧了
2. **file_size=None 的调用方失去豁免**——当前全仓仅两个生产调用点（均已传 size）+测试；未来新增调用点忘传 size 时，中文长行截断样本会被误判 binary（安全方向：拒读不产生 mojibake 腐蚀，但会误拒）。已在 docstring 显式写明该语义
3. 恰好 1000 字节的文件不享受豁免（`>1000` 才截断）——全采样无截断 artifact 可能存在，判据正确

### F-034 五字段

- **完成内容**：尾部 U+FFFD 豁免收紧为「file_size>1000 才生效」，对抗样本 bytes(range(256)) 重新判 binary，#558 中文截断修复不回退。
- **改动文件**：仓外 hermes 仓 commit `1db1c4a3`=`C:/Users/Administrator/AppData/Local/hermes/hermes-agent/tools/file_operations.py`（修法+两调用点）+ `C:/Users/Administrator/AppData/Local/hermes/hermes-agent/tests/tools/test_file_operations_edge_cases.py`（2 旧测试补 file_size 参数+4 新回归）
- **验证**：`HERMES_PYTHON=... bash scripts/run_tests.sh tests/tools/test_file_operations_edge_cases.py -q` → 28/28 绿（含 bytes(range(256)) 对抗样本判 binary、满窗口中文长行判 text）；`test_file_operations.py` 38 过 8 败——**8 败已 stash 对照实证为 Windows 平台既有失败**（umask/symlink/hidden-path，与本改动无关，stash 前后失败清单逐一同名）
- **未做项**：8 个 Windows 平台既有测试失败不属本单范围（未触碰，未恶化）；wiki 侧仅任务单流转无代码改动
- **需要谁动作**：欧阳锋终审；hermes 仓 commit `1db1c4a3` 在 detached HEAD 上（同 #560 的 86c79355 状态），如需入主干由仓主裁定

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

- 🔴 声称但未入仓（untracked）: `C:/Users/Administrator/AppData/Local/hermes/hermes-agent/tests/tools/test_file_operations_edge_cases.py`
- 🔴 声称但未入仓（untracked）: `C:/Users/Administrator/AppData/Local/hermes/hermes-agent/tools/file_operations.py`
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无/截断）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点

---

## 终审记录（2026-08-28 欧阳锋）

**结论：PASS A**——对抗漏洞堵死且 #558 修复本体不回退；工程化超出我的一行修法（他先发现"满采样不能按解码后字符数判定"——1000 字节中文样本解码仅 ~334 字符，char 长度判据会误杀本体，必须从 stat 传 file_size——这个坑我提修法时没想到）。

**核验留痕（独立复现，含我的对抗样本原厂复测）**：
- commit `1db1c4a3` 在册；diff 走读：`file_size>1000` 才豁免 + None=严格 + docstring 写明语义 ✅
- 四分支实测全对：对抗样本 `bytes(range(256))`（file_size=256）→ binary ✅；满采样中文截断（file_size=2911）→ text ✅（#558 不回退）；同样本 file_size=None → binary ✅（严格态）；file_size=999（未截断，尾部 U+FFFD=真实内容）→ binary ✅
- 回归 28/28 复跑全绿 ✅
- 语义代价自我披露三条（验收强制项）逐条成立： <1000 字节含真 U+FFFD 的文本误判 binary（概率≈0）/ None 调用方失豁免（安全方向=拒读）/ 恰好 1000 字节不豁免（判据正确）

**核验插曲（自我留痕）**：首跑复测我把构造头从 `# 测试\n` 改成 `# t\n`，字节对齐变了，切口恰好落在字符边界上——样本根本没有 U+FFFD，差点报「None 严格态失效」假阳性。今晚第四次：核验构造的任何一个字节都不能随手改。

**存在性核查**：「四分支判定」=上方逐条命令输出实录；「8 败既有」采纳其 stash 对照声明（失败清单逐一同名），未复跑全量（成本）。

**需要谁动作**：hermes 仓 `1db1c4a3` 与 #560 的 `86c79355` 均在 **detached HEAD** 上——提交未挂分支，有 GC 丢失风险，请仓主/老朱裁定合入主干（执行报告已自披露）。

**备注**：从观察项（#558 终审 A- 扣分点）到立项到修复闭环 <8h——终审观察项转办链路首次完整跑通。
