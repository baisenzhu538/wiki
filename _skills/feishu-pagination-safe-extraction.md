# 飞书文档分页安全提取

> **P0 级技能**：适用于所有需要从飞书文档提取内容的 Agent。
>
> 来源：段王爷（南帝）2026-06-23 实战 Bug 修复 + 老板纠偏后固化。

## 一句话

飞书 Docx API 的 `page_size=500` 是硬上限，超过必须分页。**不处理分页 = 内容静默截断，API 不报错。**

## 触发条件

任何 Agent 在执行以下操作时必须加载本技能：
- 从飞书文档/Wiki 提取内容（SSR 或 API 方式）
- 使用 `/open-apis/docx/v1/documents/{id}/blocks/{id}/children` 接口
- 处理超过 500 blocks 的飞书文档

## 核心代码：分页安全版 fetch_children

```python
def fetch_children(parent_id, doc_id, token, block_ids, all_blocks):
    """⚠️ 必须用 while has_more 循环翻页到底"""
    new_items = []
    page_token = ''
    page_count = 0
    while True:
        page_count += 1
        url = (f"https://open.feishu.cn/open-apis/docx/v1/documents/"
               f"{doc_id}/blocks/{parent_id}/children?page_size=500")
        if page_token:
            url += f'&page_token={page_token}'
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
        resp = json.loads(urllib.request.urlopen(req, timeout=15).read())
        if resp.get('code') != 0:
            break
        for item in resp['data']['items']:
            if item['block_id'] not in block_ids:
                block_ids.add(item['block_id'])
                all_blocks.append(item)
                new_items.append(item)
        if not resp['data'].get('has_more'):
            break
        page_token = resp['data'].get('page_token', '')
    if page_count > 1:
        print(f"  ⚠️ 分页警告：{page_count} 页，{len(new_items)} 个子节点")
    return new_items
```

## 虚拟滚动 → 流式提取映射

| 浏览器虚拟滚动 | API 对应操作 |
|---|---|
| 只渲染可视区域 | `page_size=500` 逐页获取 |
| 滚动触发加载 | `has_more=True` → 下一页 |
| 滚动位置 | `page_token` 保持游标 |
| DOM 回收 | 处理完一页释放内存 |

## 防御检查清单

- [ ] `fetch_children()` 内部有 `while has_more` 循环
- [ ] 超过 1 页打印 `⚠️ 分页警告`
- [ ] 提取完后打印总 block 数供人工复核
- [ ] 子节点递归用队列，不用 `for b in list(all_blocks)`

## 事故案例

拆书会第208期：1188 根级 blocks（3页）→ 遗漏 688 blocks → 故事四~附录三全部消失。
用户反馈后修复，避免后续所有长文档重现。

## 相关资源

- 段王爷 `feishu-publishing` 技能
- wiki: `feishu-docx-pagination-extraction` (30_wiki/skills/)
- 概念卡: `concept-feishu-api-pagination-trap`
- 概念卡: `concept-streaming-extraction-pattern`
