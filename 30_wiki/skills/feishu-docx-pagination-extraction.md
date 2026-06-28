---
id: feishu-docx-pagination-extraction
title: 飞书 Docx API 分页安全提取 + 流式处理模式
type: skill
status: enriched
confidence: 0.95
trust_level: high
domain:
- src_unknown
- src_unknown
- src_unknown
source_person: 段王爷
source_context: 拆书会第208期《AI 2041》逐字稿提取——因API分页遗漏导致内容静默截断，用户纠偏后定位+修复+固化
source_refs:
- src_unknown
- src_unknown
created_at: '2026-06-23'
updated_at: '2026-06-28'
author: 段王爷（南帝）
reviewed_by: 欧阳锋
review_date: '2026-06-23'
related:
- pending_unknown
diagnostic_signals:
- framework_lens: API分页遗漏——fetch_children()没有检查has_more+page_token
  follow_up_question: 你的提取脚本在调用/blocks/{id}/children后，有没有检查resp['data']['has_more']？
- framework_lens: 流式提取模式——逐页拉取→逐页转换→逐批写入，类比浏览器虚拟滚动
  follow_up_question: 你的提取是等全部加载完再处理，还是一页一页流式处理？

---
# 飞书 Docx API 分页安全提取 + 流式处理模式

> **P0 级别**：不处理分页会导致内容**静默截断**（API 不报错，数据悄悄少一半）。
>
> 实战案例：拆书会第208期 1188 根级 blocks（3页）→ 旧代码仅取第1页 500 个 → 遗漏 688 blocks（故事四~附录三全部消失）。

---

## 一、分页安全版 `fetch_all_blocks()`

```python
import json, urllib.request

def fetch_all_blocks(doc_id, token):
    """
    获取文档所有blocks（包括嵌套子节点，自动处理分页）。

    ⚠️ P0 修复（2026-06-23）：
    飞书 Docx API 的 page_size=500 是硬上限，超过必须分页。
    此函数使用 while has_more 循环翻页到底，打印分页警告。
    """
    all_blocks = []
    block_ids = set()

    def fetch_children(parent_id):
        """获取 parent_id 的所有子 blocks（自动翻页到底）"""
        new_items = []
        page_token = ''
        page_count = 0
        while True:
            page_count += 1
            url = (f"https://open.feishu.cn/open-apis/docx/v1/documents/"
                   f"{doc_id}/blocks/{parent_id}/children?page_size=500")
            if page_token:
                url += f'&page_token={page_token}'
            req = urllib.request.Request(
                url,
                headers={"Authorization": f"Bearer {token}"}
            )
            resp = json.loads(urllib.request.urlopen(req, timeout=15).read())
            if resp.get('code') != 0:
                break
            for item in resp['data']['items']:
                if item['block_id'] not in block_ids:
                    block_ids.add(item['block_id'])
                    all_blocks.append(item)
                    new_items.append(item)
            has_more = resp['data'].get('has_more', False)
            if not has_more:
                break
            page_token = resp['data'].get('page_token', '')
        if page_count > 1:
            print(f"  ⚠️ 分页警告：{parent_id[:12]}... 有 {page_count} 页，"
                  f"共 {len(new_items)} 个子节点")
        return new_items

    # 1. 获取根级节点（自动分页）
    print(f"正在读取文档 {doc_id[:12]}...")
    root_new = fetch_children(doc_id)
    print(f"  根级: {len(root_new)} blocks")

    # 2. 队列递归获取所有嵌套子节点
    # ⚠️ 关键：不能用 for b in list(all_blocks)，必须用队列
    queue = list(root_new)
    while queue:
        block = queue.pop(0)
        for child_id in block.get('children', []):
            if child_id not in block_ids:
                new_items = fetch_children(block['block_id'])
                queue.extend(new_items)

    print(f"  总计: {len(all_blocks)} blocks（含嵌套子节点）")
    return all_blocks
```

---

## 二、流式提取模式（虚拟滚动到 API 的映射）

**类比：**

| 浏览器虚拟滚动 | API 流式提取 |
|---|---|
| 只渲染可视区域 | `page_size=500` 逐页获取 |
| `IntersectionObserver` 触发加载 | `has_more=True` 触发下一页 |
| `scrollTop` 保持位置 | `page_token` 保持游标 |
| 离视口 DOM 回收 | 处理完一页即释放内存 |

**流式提取流程：**

```
while has_more:
    fetch_page(500 blocks)      # 视口加载
    → convert_to_feishu()       # 渲染当前页
    → batch_write(每50个)       # 写入缓冲区
    → page_token 推进游标       # scrollTop 前进
```

**内存对比：**
- src_unknown
- src_unknown

---

## 三、P0 事故复盘

| 项目 | 内容 |
|---|---|
| 事故 | 提取拆书会第208期逐字稿，只拿到前半部分（552/1329 blocks） |
| 症状 | API 返回 code=0，不报错，内容悄悄少一半 |
| 根因 | `fetch_children()` 没有 `while has_more` 循环 |
| 发现方式 | 用户反馈"文章很长，十个故事，后面还有大量解读" |
| 修复 | 添加 `while has_more` + `page_token` 循环翻页 |
| 预防 | 所有 API 分页调用统一检查 `has_more`；提取后打印 block 总数 |

---

## 四、防御性编码检查清单

- src_unknown
- src_unknown
- src_unknown
- src_unknown
