---
name: multi-page-article-capture
description: "多页文章自动抓取拼接。模仿 Kimi WebBridge 模式——浏览器遍历目录/分页 → DOM文本提取（非截图OCR）→ 去重拼接 → 输出完整 Markdown 文章。适用：付费墙后内容、分页文章、目录式连载、反爬受保护页面。"
version: 1.0.0
category: creative
metadata:
  hermes:
    tags: [browser-automation, content-extraction, web-scraping, article-capture, dom-extraction, kimi-webbridge]
    related_skills:
      - beikai-multimodal-pipeline
      - vlm-image-describe-pipeline
      - batch-paddleocr-js
---

# 多页文章自动抓取拼接

> "截图 OCR 是笨办法——人家 Kimi WebBridge 直接读 DOM，一页页点过去，跟真人翻书一样。叫花子手里也有 browser 工具，这套功夫得学。" — 洪七公

## 定位

解决「文章无法复制、分页太多、只能截图」的痛点——**不截图，直接操控浏览器抓 DOM 文本**。

```
旧路子（截图OCR）:
  第1页截图 → OCR → 文字1 ─┐
  第2页截图 → OCR → 文字2 ─┼→ 拼接 → 有 OCR 误差
  第3页截图 → OCR → 文字3 ─┘

新路子（WebBridge 模式）:
  浏览器打开目录页
    → 点击第1条 → browser_snapshot 抓 DOM 文本
    → 点击第2条 → browser_snapshot 抓 DOM 文本
    → ...
    → 去重拼接 → 完整文章（零 OCR 误差）
```

## 触发条件

- "把这个目录下的文章全扒下来"
- "这个系列有 10 页，帮我抓成一篇"
- "这篇文章分页了，拼成完整的"
- "扒这个网站的内容" / "抓取这个连载"
- "这个页面没法复制，帮我提取"

## 核心工具

| 工具 | 作用 | Kimi WebBridge 对应 |
|:--|:--|:--|
| `browser_navigate` | 打开目标 URL | 浏览器导航 |
| `browser_snapshot(full=true)` | 提取页面完整文本 | DOM 内容读取 |
| `browser_click` | 点击链接/按钮 | 自动点击操作 |
| `browser_scroll` | 滚动加载更多 | 懒加载内容触发 |

## 工作流

### 模式 A：目录遍历（有目录页）

```
Step 1: browser_navigate(目录URL)
Step 2: browser_snapshot → 识别所有文章链接
Step 3: 逐个 browser_click(链接) → browser_snapshot(full=true) → 提取正文
Step 4: 去重拼接 → 保存 {系列名}.md
```

**适用**：课程目录、连载文章、知识库索引

### 模式 B：分页遍历（文章有"下一页"）

```
Step 1: browser_navigate(第1页URL)
Step 2: browser_snapshot(full=true) → 提取正文
Step 3: 检测"下一页"按钮 → browser_click → 重复 Step 2
Step 4: 直到无"下一页" → 拼接保存
```

**适用**：分页文章、论坛长帖、帮助文档

### 模式 C：滚动加载（无限滚动）

```
阶段一：探底摸底（10秒）
  browser_navigate(URL)
  browser_scroll(down) × N → 滚到底
  → 回报用户："全文约 X 字，预计 N 轮提取，每轮 ~2 分钟"

阶段二：分批提取 + 里程碑通知
  browser_scroll(up) → 回到顶部
  browser_snapshot(full=true, 第1段) → 提取
  → 通知用户："[1/4] 已提取前 2000 字 ✅"
  browser_scroll(down) → 第2段
  browser_snapshot(full=true, 第2段) → 提取
  → 通知用户："[2/4] 已提取 2000-4000 字 ✅"
  ...直到全文提取完成

阶段三：拼接保存
  → 通知用户："全文 X 字，已保存至 {路径}"
```

**适用**：Medium、公众号、动态加载页面

> ⚠️ 无限滚动是三种模式中唯一"不可预知终点"的。**必须先探底再分批**，不让用户干等。

## 分批汇报机制

> 来自实战教训：用户丢 URL 后去忙别的，不能让他不知道进度。

### 三阶段通知规范

| 阶段 | 通知内容 | 时机 |
|:--|:--|:--|
| **开工** | "开始抓取 {标题}，{模式}模式，预计 {条数/页数}" | 第一条/第一页开始前 |
| **里程碑** | "[3/12] {章节标题} ✅ ({字数}字)" | 每条/每页完成后 |
| **交付** | "全文 {总字数} 字，已保存至 {路径}" | 拼接完成后 |

### 异常中断通知

```markdown
⚠️ 抓取中断
- 已完成: 5/12
- 失败位置: 第6章 (链接失效/需要登录/超时)
- 已保存: 前5章 → partial_抓取_2026-06-21.md
- 建议: [具体修复建议]
```

### 长任务回血策略

```markdown
如果抓取超过 10 页/条:
  → 每 5 条存一次中间文件 (防止会话中断丢数据)
  → 中间文件命名: {系列名}_WIP_N.md
  → 全部完成后合并删除中间文件
```

## 核心处理逻辑

### 1. 正文提取（去噪）

```python
"""从 browser_snapshot 输出中提取纯净正文"""
import re

def extract_body(snapshot_text: str) -> str:
    """去掉导航、页脚、广告等噪音"""
    # 移除 ref 标记（如 @e5, @e12）
    text = re.sub(r'@e\d+', '', snapshot_text)
    
    # 移除明显的导航文本
    noise_patterns = [
        r'首页|关于我们|联系我们|登录|注册|搜索',
        r'Copyright.*|All Rights Reserved',
        r'分享到|点赞|收藏|评论\s*\d+',
        r'上一篇|下一篇|返回目录',
    ]
    for pat in noise_patterns:
        text = re.sub(pat, '', text)
    
    # 压缩多余空行
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()
```

### 2. 相邻页去重

```python
def dedup_adjacent(page1: str, page2: str, overlap_chars: int = 100) -> str:
    """去重：相邻页重叠部分（如页眉、上一页末句=下一页首句）"""
    if not page1 or not page2:
        return page2
    
    # 取 page1 末尾 N 字符，看是否出现在 page2 开头
    tail = page1[-overlap_chars:]
    idx = page2.find(tail)
    if idx >= 0:
        # 从重叠位置之后截取
        return page2[idx + len(tail):]
    
    # 无重叠，直接拼接
    return page2

def merge_pages(pages: list[str], separator: str = '\n\n---\n\n') -> str:
    """拼接多页内容，自动去重"""
    result = pages[0]
    for i in range(1, len(pages)):
        next_part = dedup_adjacent(pages[i-1], pages[i])
        result += separator + next_part
    return result
```

### 3. 标题层级修复

```python
def fix_headings(text: str, base_level: int = 1) -> str:
    """统一 Markdown 标题层级"""
    # 找到原文最高层级，调整为 base_level
    headings = re.findall(r'^(#{1,6})\s', text, re.MULTILINE)
    if not headings:
        return text
    
    min_level = min(len(h) for h in headings)
    if min_level == base_level:
        return text
    
    shift = min_level - base_level
    def replace_heading(m):
        current = len(m.group(1))
        new_level = max(1, current - shift)
        return '#' * new_level + ' ' + m.group(2)
    
    return re.sub(r'^(#{1,6})\s+(.*)', replace_heading, text, flags=re.MULTILINE)
```

## 实战示例

### 示例 1：抓取课程目录

```
用户: "把 https://example.com/course/chapters 这个课程目录下所有章节抓成一篇"

执行:
  1. browser_navigate("https://example.com/course/chapters")
  2. browser_snapshot → 识别出 12 个章节链接
  3. 逐个:
     browser_click(@chapter1_link)
     browser_snapshot(full=true) → 提取正文
     browser_back → 回到目录
  4. 12 章拼接 → 保存为 "课程笔记.md"
```

### 示例 2：抓取分页文章

```
用户: "这篇文章分了 8 页 https://example.com/article?page=1"

执行:
  1. browser_navigate("https://example.com/article?page=1")
  2. browser_snapshot(full=true) → 提取第1页正文
  3. browser_click(@next_page_button) → 第2页
  4. 重复直到无"下一页"
  5. 8页拼接去重 → 保存为 "完整文章.md"
```

### 示例 3：付费墙后内容（已登录）

```
用户: "帮我把这个付费专栏的 5 篇文章全扒下来"

前提: 用户的 Chrome/Edge 已登录该网站
执行:
  1. 用已登录浏览器打开专栏目录
  2. 逐篇点击提取（因为已登录，能看全文）
  3. 拼接保存
```

## 与截图 OCR 流程的对比

| 维度 | 截图 OCR 流程 | WebBridge 模式（本技能） |
|:--|:--|:--|
| 准确性 | 95-99%（OCR 误差） | **100%**（DOM 直取） |
| 格式保留 | 仅纯文本 | **保留标题/列表/链接** |
| 表格处理 | OCR 可能错位 | **完整表格结构** |
| 速度 | 每页 10-15 秒 | **每页 3-5 秒** |
| 登录态 | 不需要 | **需要浏览器已登录** |
| 反爬 | 无影响 | 可能在部分网站受限 |
| 适用场景 | 图片/PDF/扫描件 | **网页文章/分页内容** |

## 决策树

```
丢给我的 URL 是——
│
├── 有登录墙（跳转SSO/微信扫码/飞书文档）
│   → 🔴 本技能无法处理 → 建议用户用 Kimi WebBridge
│      （WebBridge 操控用户已登录的 Chrome，能过登录墙）
│
├── 有目录页（章节列表）→ 🟢 模式 A：目录遍历（最优）
│     可预知总数，逐章汇报进度
│
├── 有"下一页"按钮   → 🟢 模式 B：分页遍历（次优）
│     可预知页数，逐页汇报进度
│
├── 只有滚动加载      → 🟡 模式 C：无限滚动（先探底再分批）
│     不可预知终点，必须先滚到底摸底 → 分批提取+里程碑通知
│     每 5 段存一次中间文件防丢
│
└── 根本无法复制/只有图片 → 🔴 走截图 OCR 流程
      → vlm-image-describe-pipeline / batch-paddleocr-js
```

## 输出规范

### 单篇文章输出结构

```markdown
# 文章标题

> 来源: [原始URL]
> 抓取时间: 2026-06-21
> 方式: WebBridge 模式 · browser_snapshot
> 页数: 8页

---

[正文内容...]
```

### 系列文章输出结构

```markdown
# 系列总标题

> 来源: [目录URL]
> 篇章数: 12
> 抓取时间: 2026-06-21

## 第1章 标题
[正文...]

## 第2章 标题
[正文...]
```

## 常见坑点

### Pitfall 1: browser_snapshot 截断
`browser_snapshot` 默认是紧凑模式（只显示交互元素）。全文提取必须用：
```
browser_snapshot(full=true)
```

### Pitfall 2: 动态加载内容
部分网站用 JS 懒加载，直接 snapshot 只能看到首屏。解决：
```python
# 先滚动到底部触发加载
browser_scroll(direction="down")  # 重复 3-5 次
# 再提取全文
browser_snapshot(full=true)
```

### Pitfall 3: 弹窗/登录墙
如果页面弹出登录框或广告：
```python
# 先关闭弹窗
browser_click(@close_button_ref)
# 再提取内容
```

### Pitfall 4: 页面重定向
点击链接后可能跳转到登录页（session 过期）：
```python
# 检查 snapshot 是否包含正文关键词
if "请登录" in snapshot_text:
    # 暂停，等待用户重新登录
```

### Pitfall 5: 编码/特殊字符
DOM 文本提取的编码通常正确，但少数网站可能有非标准字符。用 Python 的 `ftfy` 库修复：
```bash
python3 -m pip install ftfy
```

### Pitfall 6: 同一页面内容重复
部分网站正文区在 DOM 中出现多次（如 mobile + desktop 两套）。提取时注意选择唯一容器。

## 与 Kimi WebBridge 的异同

| | Kimi WebBridge | 本技能 |
|:--|:--|:--|
| 底层 | Chrome DevTools Protocol | Hermes browser 工具 |
| 工作流 | Skill + CLI 固化 | 逐个工具调用 |
| 可重复性 | 一句话重跑 | 每次需描述流程 |
| 部署 | 需安装扩展 | **零安装** |
| 提取精度 | DOM 全量 | snapshot 全量 |

> **后续升级方向**：将常见网站的抓取模式固化为脚本，做到"一句话重跑"。

## 验证清单

- [ ] browser_navigate 能打开目标 URL
- [ ] browser_snapshot(full=true) 能提取完整正文
- [ ] 多页拼接无重复段落
- [ ] 标题层级保留正确
- [ ] 输出 Markdown 格式规范
- [ ] 来源 URL 和时间戳已记录

## 参考资料

- Kimi WebBridge: https://www.kimi.com/features/webbridge
- Kimi WebBridge 原理: Chrome DevTools Protocol + 本地服务
- 设计灵感: Kimi WebBridge 的"目录遍历→DOM提取→拼接"模式
