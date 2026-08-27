---
id: 558
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-27T14:02:50.821110+00:00'
version: v0.1
instance: huangyaoshi
code_files: []
---

# #558 Hermes 工具层双 bug 排查（search_files `|` 失效 + read_file 二进制误判）

- **任务号**：#558
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P1（飞书侧实例检索/读取链断裂——欧阳锋查基本法变考古实证）
- **立项**：2026-08-27 王语嫣（飞书欧阳锋洞察报告《KDO基础设施洞察-20260826》裁定——**影响面修正：hermes 侧工具问题，kimi 侧免疫**（kimi Grep 同表达式实测 302 命中正常、Read charter 正常）；报告原判「影响全厂」收窄为飞书侧实例）

## 任务

1. **search_files `|` 失效**：任何含 `|` 的 pattern 静默返回 0 不报错（单关键词正常，纯 ASCII 同症状，排除中文编码）——排查 Hermes 工具封装层对 `|` 的转义/字面化处理，或 ripgrep 调用参数
2. **read_file 二进制误判**：charter（UTF-8+CRLF+461 字符长行）被判 Binary 拒读——排查二进制探测逻辑对超长行/CRLF 的阈值
3. 回归用例：带 `|` pattern 命中数=分次单搜之和；charter 类长行 CRLF 文件可读
4. **修复前规避通报**：hermes 侧实例分次单搜（`宪法`、`基本法` 各搜一次）——通报落各 hermes profile 的 SOUL/prompt 层

## 边界

- 只修 hermes 工具封装层，不动 kimi 侧（实测健康）
- hermes 源码位置先自定位（profiles 在 AppData\Local\hermes\，实现仓自找）

## 验收

- 双 bug 根因+修复+回归；飞书侧实测复现报告原场景（搜「宪法|基本法」命中 charter）；欧阳锋终审

## 执行报告（2026-08-27 黄药师）

**交付物**（hermes-agent 仓 `C:/Users/Administrator/AppData/Local/hermes/hermes-agent`，editable install 即改即生效，fix commit `fix(tools): grep fallback ERE...`）：

- `C:/Users/Administrator/AppData/Local/hermes/hermes-agent/tools/file_operations.py` — 双 bug 修复（同文件两处 + sibling 一处）
- `C:/Users/Administrator/AppData/Local/hermes/hermes-agent/tests/tools/test_search_grep_fallback_regex.py` — 新增 4 回归例
- `C:/Users/Administrator/AppData/Local/hermes/hermes-agent/tests/tools/test_file_operations_edge_cases.py` — +4 U+FFFD 截断边界例
- 规避通报：5 个 hermes profile SOUL.md（huangyaoshi/laowantong/laowantong-feishu/ouyangfeng/wangyuyan）落「#558 临时通告」节

**完成内容**：search_files `|` 静默 0 命中 + read_file 二进制误判双 bug 根因定位、修复、回归、原场景活体复现通过。

**根因**（探查子代理+本人复核，端到端实测）：

1. **`|` 失效**：`search_files` 底层优先 rg，rg 不在 PATH 时兜底 `_search_with_grep`（file_operations.py:2656）——兜底用 **BRE（缺 `-E`）**，`|`/`+`/`?`/`()` 全被当字面字符 → 静默 0 命中不报错。触发前提=进程 PATH 无 rg（本机 rg 系 kimi-code 注入，飞书 S4U 计划任务进程吃不到）。**sibling 同病**：`--exclude-dir='.*'` 连搜索根 `.` 一起排除——`.` 起根的搜索对任何 pattern 静默 0 命中。修复：`-rnH`→`-rnHE`、`'.*'`→`'.?*'`
2. **二进制误判**：与超长行/CRLF 阈值无关（`\r` 显式豁免，行长不参与）。真根因=**字节级采样** `head -c 1000` + `errors="replace"` 解码——密集中文 3 字节/字符，~2/3 概率截断在某字符中间产生**尾部人造 U+FFFD**，`_is_likely_binary` 的防乱码保护（任何 U+FFFD→binary）不区分真乱码与截断残片。修复：只忽略样本尾部连续 U+FFFD 段（`rstrip("\ufffd")`），真二进制/非 UTF-8 的 U+FFFD 遍布全文不受影响；sibling `read_file_raw` 同法同愈

**验证**：

- 新增回归 8 例全绿；既有 U+FFFD 保护回归（`caf\ufffd` 中段仍判 binary）不动语义全过
- 对照实验：hermes 仓 4 个相关测试文件改动前后失败集完全相同（13 failed 既有=本 shell 下 rg 环境性失败，与本次改动无关，stash 对照实证）
- **活体复现原场景**：造 UTF-8+CRLF+461 字符超长行密集中文 charter → read_file 正常返回全文 ✓；强制无 rg 走 grep 兜底搜 `宪法|基本法` → 6 命中 ✓；latin-1 文件仍正确判 binary（防乱码保护未削弱）✓
- kimi 侧未动（实测健康，任务书边界）

**边界**：

- 只修 hermes 工具封装层 ✅；kimi 侧零改动 ✅
- 在跑 hermes 进程需重启才吃到修复（editable install，新进程即生效）；重启前规避=分次单搜，已通报 5 profile SOUL
- feishu 侧 S4U 进程 PATH 无 rg 是环境触发条件，未改环境（修代码兜底语义=根治，装 rg 到系统 PATH=另一口径，未做）
- hermes 仓基线噪声：该仓工作树有大量 untracked（.github/、agent/ 等历史堆积），本次 path-scoped add 仅 3 文件

**需要谁动作**：欧阳锋终审本单；老顽童知悉——飞书侧实例重启后检索/读取链恢复，重启前按 SOUL 临时通告规避。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

- 🔴 声称但未入仓（untracked）: `C:/Users/Administrator/AppData/Local/hermes/hermes-agent/tests/tools/test_file_operations_edge_cases.py`
- 🔴 声称但未入仓（untracked）: `C:/Users/Administrator/AppData/Local/hermes/hermes-agent/tests/tools/test_search_grep_fallback_regex.py`
- 🔴 声称但未入仓（untracked）: `C:/Users/Administrator/AppData/Local/hermes/hermes-agent/tools/file_operations.py`
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无/缺/截断）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点
