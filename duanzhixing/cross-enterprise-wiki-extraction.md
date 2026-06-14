# 段王爷：跨企业飞书Wiki内容提取 → 问答对过滤 → 飞书发布

> 最后更新：2026-06-15 | 段王爷（南帝）  
> 适用：五绝全体（黄药师、洪七公、周伯通均可调用）

---

## 能力概述

从任意飞书企业空间的 Wiki 页面提取完整内容，智能过滤（如 AMA 场景下只保留"问题+教练回答"），生成结构化飞书文档。

**实战战绩：** 一堂企业空间《精益测试关键问题》AMA，1005 blocks → 32 个问答对 → 570 blocks 文档，12 批零失败。

---

## 调用方式（其他 Agent 用）

需要段王爷执行时，告诉周伯通或直接在飞书群 @段王爷：

```
@段王爷 把这个 Wiki 的内容提取出来，写入我的飞书文档：
https://xxx.feishu.cn/wiki/LAHswpbzFi6RNCkYcMjccOSZnlh
要求：只要问题和张磊的回答，不要学员回答
```

段王爷会自动：
1. 判断同企业/跨企业
2. 同企业 → tenant token API 直读
3. 跨企业 → 生成 OAuth 链接 → 用户授权 → user token API 直读
4. 提取 → 过滤 → 构建 blocks → 分批写入飞书文档
5. 返回文档链接

---

## 全流程分步拆解

### Phase 1: 获取文档数据

| 场景 | 方法 | 前提 |
|------|------|------|
| 同企业空间 | `docx/v1/documents/{id}/blocks` + tenant token | 应用有 `docx:document:readonly` |
| 跨企业空间 | 同上，但必须 OAuth user token | 用户在目标企业有账号 |
| Wiki SSR（零API） | `browser_navigate` → `window.DATA` → block_map | 页面可公开访问 |

**OAuth 关键参数：**
- 端点：`https://open.feishu.cn/open-apis/authen/v1/authorize`
- scope：`docx:document:readonly`（只用单个，不能用逗号分隔多个，否则 20043）
- 换 token 端点：`/authen/v1/access_token`（不是 oidc 端点）
- Authorization 头：`Bearer {app_access_token}`（不是 Basic Auth）

### Phase 2: 提取问答对（并行策略）

大文档（>800 blocks）用 `delegate_task` 双 agent 并行：

```
Agent A: 提取前半部分 QA pairs（前 500 blocks）
Agent B: 提取后半部分 QA pairs（后 500 blocks）
→ 合并去重（按问题前50字符）
```

**过滤规则：**
- 教练回答：带 `一、二、三` / `第X步` / `首先` / `核心` 等结构化标记
- 学员回答（丢弃）：`我做了这些工作` / `我的案例` / `行业机会：` 等个人经验叙述
- 口头提问（标记）：问题原文未记录时保留回答但标注

### Phase 3: 构建飞书文档 blocks

```python
# 结构模板
blocks = [
    h1("标题"),
    pg("共 N 个问题 — 原载{来源}", bold=True),
    divider(),
    # 每个 QA：
    h2(f"Q{i}：{问题摘要}"),
    pg(f"完整提问：{问题全文}"),  # 仅长问题展示
    pg(回答段落1),
    bullet(列表项),
    pg(加粗子标题, bold=True),
    divider(),
]
```

### Phase 4: 分批写入

- JSON 预存 blocks → `write_file` 写启动脚本 → `terminal` 执行
- 每批 50 blocks，时间间隔 0.3 秒
- 批次失败 → 逐块重试
- 避开 `write_file` 截断：脚本中不出现 `json.loads(urlopen(...))` 等模式

---

## 核心坑与绕过

| 陷阱 | 症状 | 绕过 |
|------|------|------|
| OAuth scope 逗号分隔 | `20043 scope有误` | 只用单个 scope |
| OAuth 错误端点 | `20014 token invalid` | 用 `/authen/v1/access_token`，Bearer 头 |
| write_file 截断 | 脚本语法错误 `json.l...` | JSON 预存 + 极简启动脚本 |
| 大文档超时 | 提取脚本 timeout | delegate_task 双 agent 并行 |
| 跨域文档打不开 | 用户看到「文件不存在」 | 设置 `anyone_readable` + `external_access` |
| SSR 子文档缺失 | block_map 缺少 doxcn 子文档 | 侧边栏点击逐板块提取 或 OAuth API |

---

## 依赖

- **段王爷飞书应用**：`cli_a97d962dfbf8dbb3`（yitanger.feishu.cn 域）
- **必须权限**：`docx:document`、`docx:document:readonly`、`drive:drive`
- **OAuth 回调**：`https://api.hermes-chat.com/v1/callback/feishu/oauth`
- **参考技能**：`feishu-publishing` (productivity/)
