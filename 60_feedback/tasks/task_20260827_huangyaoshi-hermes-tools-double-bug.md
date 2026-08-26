---
id: 558
assignee: huangyaoshi
status: queued
updated_at: '2026-08-27T02:05:00+00:00'
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
