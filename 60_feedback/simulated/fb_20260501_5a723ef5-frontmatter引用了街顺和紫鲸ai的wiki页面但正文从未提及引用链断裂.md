---
feedback_id: "fb_20260501_5a723ef5"
kind: "simulated"
title: "frontmatter引用了街顺和紫鲸AI的wiki页面但正文从未提及——引用链断裂"
artifact_id: "art_20260430_447f2eea"
source: "kdo simulate-reader"
captured_at: "2026-04-30T16:58:11+00:00"
path: "60_feedback/simulated/fb_20260501_5a723ef5-frontmatter引用了街顺和紫鲸ai的wiki页面但正文从未提及引用链断裂.md"
---

# frontmatter引用了街顺和紫鲸AI的wiki页面但正文从未提及——引用链断裂

## Dimension

completeness

## Severity

high

## Location

frontmatter wiki_refs vs 正文内容

## Finding

frontmatter声明wiki_refs包含街顺和紫鲸AI，但正文全程只引用了YC wiki页面。街顺和紫鲸AI作为中国AI SaaS案例，本应是文章「中国语境」落地的最有力证据——紫鲸AI的六Agent管线就是「AI作为操作系统」的实例，街顺的云值守就是「人类middleware被替代」的实例。但读者在整篇文章中看不到这两家公司被提及。这是引用链的断裂：wiki_refs成了装饰性引用，而非论证的有机组成部分。

## Suggestion

1. 在Section 7（初创公司结构性优势）或Section 9（小微企业）中，嵌入紫鲸AI案例：6个Agent替代了内容营销团队
2. 在Section 5（中层管理变Markdown）中引用街顺的百人客服→AI替代的转型路径
3. 或者，如果决定文章聚焦YC框架不涉及中国案例，就从wiki_refs中移除街顺和紫鲸AI——保持frontmatter诚实
