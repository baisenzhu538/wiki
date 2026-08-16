---
id: task_20260809_huangyaoshi-feishu-doc-mcp
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-10
updated_at: 2026-08-09
priority: P0
wsjf: 4.0
claimed_at: 2026-08-09
---

## 执行报告（2026-08-09 黄药师）

### 交付物（对照规格 1-3）
1. **`kdo-tools/mcp/feishu_doc_server.py`** — 操作型 MCP server（FastMCP + stdio/SSE，参照 kdo server.py 模式）：
   - `feishu_doc_create` — 创建文档（title + markdown 内容）
   - `feishu_doc_fetch` — 读取文档内容（按 token/URL）
   - `feishu_doc_update` — 更新文档（append/overwrite，markdown 格式）
   - `feishu_doc_search` — 搜索文档/Wiki/表格（关键词）
2. lark-cli 定位：`C:\Users\Administrator\.workbuddy\binaries\node\cli-connector-packages\node_modules\@larksuite\cli\bin\lark-cli.exe`（v1.0.81，认证 ready：bot + user 双身份）

### 全链路冒烟（验收标准 ✅ 全过）
| 步骤 | 结果 |
|:---|:---|
| 创建文档 | ✅ document_id 生成（WwjtddlnxofROgxo4Y0cMx1Xnfc） |
| 写入内容 | ✅ revision 2→3, result: success（markdown → XML 自动转换） |
| 读取回验 | ✅ 内容完整回读（标题 + 三验证点全在） |
| 搜索 | ✅ 搜到测试文档（total 1，含创建时间/用户） |

### 过程中修正（1 处）
- lark-cli `+update` 的 flag 是 `--doc`（URL/token）+ `--command append` + `--doc-format markdown`，不是猜测的 `--doc-token`/`--mode`——按实际接口修正（P-38 教训：先查工具真实参数再写封装）

### 遗留
- 测试文档保留在飞书（`MCP冒烟测试-黄药师-2305`，URL: https://my.feishu.cn/docx/WwjtddlnxofROgxo4Y0cMx1Xnfc）——删除属 high-risk-write 需确认，请用户/王语嫣决定是否清理

### 边界遵守
- 只封装 lark-cli 已授权能力（4 工具全只读+写，无 high-risk 操作）
- 未扩展 lark-cli 本身，未做权限扩张

## 建议书合并（黄药师 diag_20260809_huangyaoshi-feishu-agent-mcp-upgrade.md——#C 并入本任务）

**#C MCP 部署记录补全**：kdo MCP 挂载点/配置/客户端全部登记——config.yaml 实际部署节 + toolkit.md 登记（工具登记四步法）

### #C 完成（2026-08-10 黄药师，C1 闭环）
| 登记处 | 内容 | 验证 |
|:--|:--|:--|
| cap_hub features.json | FEISHU_DOC_MCP（20 features）——含权限模型标注（写操作仅限授权空间，无 delete） | ✅ 欧阳锋观察项已覆盖 |
| kdo-tools/mcp/config.yaml | `deployments:` 节——4 客户端清单（WorkBuddy ✅ / Claude Code ✅ / 飞书 agent 待 #308 / 任意客户端 feishu-doc） | ✅ |
| .agent/toolkit.md | MCP 服务表（kdo 检索型 + feishu-doc 操作型 + 挂载点 + "先查 config.yaml 别搜错地方"提示） | ✅ |

# 飞书文档 MCP server（#306 · WorkBuddy 借鉴——操作层基建）

## 任务目标

从"检索型 MCP（kdo_search）"扩展出"**操作型 MCP**"：飞书文档读写——让飞书 agent 从"给建议"升级为"交付物"（WorkBuddy 最强点：说人话→干活→交付物）。

## 规格

1. 复用 lark-cli 已有全套能力（im/doc/base/drive——小昭实测 v1.0.81 全套可用）→ 封装为 MCP server（stdio 或 sse，参照 kdo_search MCP 模式）
2. 能力：读写飞书文档/表格/云文档——生成模板文档、写入纪要、创建议程、更新清单
3. 注册：cap_hub 登记 + README（工具登记四步法）

## 验收标准

- MCP 冒烟：创建一页纸文档 → 写入内容 → 读取回验（全链路）
- cap_hub list 可见 + README 登记
- 安全：仅操作授权文档空间（不越权）

## 依赖

- 无（lark-cli 能力已在）

## 边界

- 只封装已授权能力，不扩展 lark-cli 本身
- 不做权限扩张（飞书应用权限保持现状）


## 建议书合并（黄药师 diag_20260809_huangyaoshi-feishu-agent-mcp-upgrade.md——#C 并入本任务）

**#C MCP 部署记录补全**：kdo MCP 挂载点/配置/客户端全部登记——config.yaml 实际部署节 + toolkit.md 登记（工具登记四步法）

## 终审记录（2026-08-10 欧阳锋）

**verdict: PASS（条件）A- · blocking: 🟠1 · methodology v2.2**

O3 独立验证：
1. feishu_doc_server.py 存在（6750B，FastMCP stdio/SSE）+ 4 工具全实现：feishu_doc_create（L77）/ feishu_doc_fetch（L97）/ feishu_doc_update（L112，command append/overwrite）/ feishu_doc_search（L131）
2. 真实参数验证（P-38 教训遵守）：update 用 --doc + --command + --doc-format markdown + --content（L124-125）——先查工具真实参数再封装
3. 冒烟证据链完整（document_id 生成 → revision 2→3 → 内容回读 → 搜索命中）——操作型 MCP 从 0 到 1
4. 测试文档保留诚实标注（"删除属 high-risk-write 需确认"）——写操作边界自觉

条件项/待办：
- C1 #C 登记：cap_hub 登记 + config.yaml 实际部署节 + toolkit.md（任务单并入项，黄药师下一步补）
- C2 测试文档处置（用户决定）："飞书MCP冒烟测试-黄药师-2305"删除或保留

🟢 观察：操作型 MCP（真实写飞书）——部署后权限模型（谁能调 create/update）建议在 cap_hub 登记时标注，防误用写操作

五维：溯源 90/逻辑 90/暗知识 85/可操作 90/表达 85 → 总分 88（A- 上限——#C 登记待补）

## 条件项跟踪（2026-08-10 欧阳锋复核）

- **C1 ✅ 已闭环（三处登记实测命中）**：① cap_hub FEISHU_DOC_MCP（20 features）+ 权限模型标注（create/update 写操作仅限授权空间，无 delete——覆盖欧阳锋 🟢 观察项）② config.yaml deployments 节（WorkBuddy/Claude Code active，飞书 agent 待 #308）③ toolkit.md MCP 服务表（feishu-doc 操作型 + 挂载点 + E020 提示"先查 config.yaml 别搜错地方"）
- **C2 ✅ 已闭环（2026-08-10 用户确认删除）**：`drive +delete`（high-risk 需 --yes）删除测试文档 WwjtddlnxofROgxo4Y0cMx1Xnfc——dry-run 预览确认目标 → 执行（deleted: true, status: success）→ 独立验证（fetch 报 3380003 "Document page has been deleted"）→ 三重复核完成
