---
type: debt
created: 2026-08-28
source_task: "#567"
owner: 段王爷（外部挂起，不派活——E058 边界；修复等老朱触发或转老顽童代理）
severity: P2
---

# 挂账：段王爷系 5 张 skill 卡虚构 capability 路径 source_refs

#567 门禁施工副产品（pre-submit 接入 check-source-refs missing 检测后这批全部会出 WARNING）。

| 卡片 | 虚构引用 | 卡片 status |
|:--|:--|:--|
| `30_wiki/skills/skill-duanwangye-prezi.md` | `capability/duanwangye/prezi` | draft |
| `30_wiki/skills/skill-duanwangye-feishu-publishing.md` | `capability/duanwangye/feishu-publishing` | **reviewed（被放行）** |
| `30_wiki/skills/skill-duanwangye-kdo-pipeline.md` | `capability/duanwangye/kdo-article-pipeline` | **reviewed（被放行）** |
| `30_wiki/skills/skill-duanwangye-wechat-extraction.md` | `capability/duanwangye/wechat-mcp` | **reviewed（被放行）** |
| `30_wiki/skills/skill-feishu-doc-l3-extraction.md` | `capability/duanwangye/feishu-doc-l3-extraction` | **reviewed（被放行）** |

- 检出方式：`check-source-refs.py check_card` 逐卡复核（exists=False 实证），非凭印象
- 修复口径：5 张卡的 source_refs 指向真实素材路径（口述稿/诊断记录），或改 src_id 注册
- 注意：reviewed 卡改 source_refs 触发复审流——修复者需重新送欧阳锋终审
- 立项口径备注：诊断书称「2 张已 reviewed」，实测为 **4 张 reviewed + 1 张 draft**（以本表为准）
