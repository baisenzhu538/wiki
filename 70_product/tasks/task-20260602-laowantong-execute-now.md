---
title: "【立即执行】老顽童：RAG 深度文章 + 暴露三个摩擦"
assigned_to: "老顽童"
priority: "P0"
created_at: "2026-06-02"
reviewer: "欧阳锋"
status: "pending"
---

# 立即执行

## 任务

用深度合成模板写一篇关于 RAG 的文章。

## 怎么做

**Step 1：读模板**
`90_control/templates/deep-synthesis-article.md`
注意：这跟你以前用的标准模板不一样。开头不是"XX 框架提出"，是"那个让我沉默的问题"。

**Step 2：读黄药师的文章（感受一下深度）**
`40_outputs/content/articles/art_20260602_kdo_data_autopsy_huangyaoshi.md`
注意看他怎么用"我不同意""KDO 的实践表明""我发现"——你也要这样写。

**Step 3：写文章**
文件名：`40_outputs/content/articles/art_20260602_laowantong_rag_judgment.md`
话题自选，和 RAG 相关即可。推荐话题：**"Graph RAG 在什么场景下不如向量 RAG？"**

**三个必须写的段落（缺一不可）：**
1. **自我应用**：用你选的话题框架分析 KDO 自身（"KDO 的实践表明……"）
2. **边界判断**：指出你不同意的地方（"我不同意……"）
3. **转换叙事**：一个具体的 before→after 认知转变

**Step 4：写 Feedback 段**
在 `## Feedback` 下面，至少写 2 个你在写作过程中遇到的真实问题。随意写，不用修饰。

## 完成标准

- [ ] 文章用了深度合成模板
- [ ] 有三段独立判断（自我应用/边界判断/转换叙事）
- [ ] Feedback 段有 ≥2 个真实问题
- [ ] 通知欧阳锋审查

## 注意

- 不用等审批，直接开写
- 写的过程中卡住的地方，记下来放在 Feedback 段
- 你不是在"交作业"，你是在"用自己的使用体验推动下一轮迭代"
