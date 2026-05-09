---
title: "用这个免费API，让你的 Agent 拥有「看」的能力"
source: "https://mp.weixin.qq.com/s/uCCuxYGh05Ydlgj7drv3wg"
author:
  - "阿橙"
published:
created: 2026-05-06
description: "别再说Agent没法上网了"
tags:
  - "clippings"
---
阿橙 *2026年5月5日 18:32*

大家好，我是橙哥，现在我每天都在跟 Agent 打交道。

Claude Code 写代码，OpenClaw 跑自动化，Hermes 管多终端。这些工具各有各的本事，但它们都有一个共同的短板：跟互联网之间总是隔着一层纱。

你想让 Claude Code 帮你查一下最新的 API 文档变了啥，它得去网上找。你想让 Hermes 帮你每天早上看一眼 V2EX 热帖然后推送到微信，它得能抓网页。你想让 OpenClaw 帮你比价，它得能搜索能读页面。

![图片](https://mmbiz.qpic.cn/mmbiz_png/hBIict2nry2lu0RfTPR3mNlUiaJQ4hu8P3ZAiaOTX0o7z8PlOTbe7tBzvo0icI13ydVDDiaYvLn4zr8ia5e87UcZhsF1Lc00wUpKjtibiby4jeCCYiaY/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

这些操作，搜索和读取网页内容，对人类来说就跟呼吸一样自然，但对 Agent 来说，一直是个麻烦事。你要么自己搭爬虫，要么花钱买第三方 API。

很多想做 Agent 的人卡就卡在这儿。

昨天刷到一条消息，TinyFish 把 Search 和 Fetch 两个 API 免费了。不是限时试用或者送几次额度那种，是彻底免费。拿个API Key，Search 每分钟 5 次，Fetch 每分钟 25 个 URL。

这事本身不算什么惊天大新闻，搜索 API 也不止它一家。但我琢磨了一下，觉得有点意思。因为这个事踩中了一个特别好的时间点。

你们可能也感觉到了，最近半年 Agent 这个赛道突然加速。Claude Code、Codex、Cursor Agent、OpenClaw、Hermes，各种框架和工具井喷一样往外冒。Agent 的核心能力是什么？帮你做事。但帮你在哪做事？绝大部分事都跟互联网有关。查资料、读文档、监控价格、抓数据、对比信息。这些操作的底层就两件事，搜索和读取页面。

这两个东西就是 Agent 和互联网交互的原语。现在有人把它免费了，对于折腾 Agent 的人来说，基础设施的门槛又降了一档。

我今天自己试了一下，聊几个我觉得比较有意思的玩法。

第一个，接 Claude Code。

TinyFish 支持 MCP 协议，你把它的 MCP Server 丢进 Claude Code 的配置里，Claude 就能直接搜索和抓取网页了。之前 Claude Code 想查一个库的最新文档，要么靠内置的搜索，要么让你手动贴链接。现在它自己就能搜、自己就能读，拿到干净的 Markdown 内容直接放进上下文里。

这个对写代码的影响是实打实的。你的编程助手终于有了「自己查资料」的能力，不用每次都跟你说「我无法访问互联网」了。

我自己用了一阵子，查最新的 API 变更日志，搜某个 npm 包的当前版本兼容性问题，比之前方便太多了。之前每次都得我自己打开浏览器搜完再粘给它，现在直接让它自己去查就行。

第二个，给 Hermes 加上「眼睛」。

Hermes 是做个人自动化的，定时任务、多终端推送这些它很擅长。但涉及网页信息的部分一直比较弱。现在通过 REST API 把搜索和抓取能力接进去，一个很自然的场景就跑通了。

比如每天早上让 Hermes 跑一个定时任务，搜索你关注的几个关键词的最新资讯，抓取摘要，推送到微信或者飞书。之前要做这事，你得自己写爬虫逻辑处理各种乱七八糟的 HTML。现在就是两个 API 调用的事，搜一下拿到 URL，抓一下拿到干净的 Markdown，喂给大模型总结就完事了。

我自己跑了一个监控 Claude 相关资讯的小任务，每天早上 9 点搜一圈推到飞书，已经跑了好几天了，效果比我想象的好。返回的内容是干净的正文，大模型总结的时候不会把导航栏和广告也读进去，准确率高了很多。

第三个玩法更有意思一点。

TinyFish 的 Fetch 不是简单的 HTTP GET，它是用真实浏览器渲染的。JavaScript、SPA、动态加载的内容都能处理。配合它的 Agent API，就是一个完整的「看网页」加「操作网页」的能力组合。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E) ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

而且它还有个 stealth 模式，能过 Cloudflare 这种反爬检测。

我自己写爬虫写了好几年，说真的，处理反爬、渲染 JavaScript、清理 HTML 这些脏活累活，每次都从头搞一遍，烦得要死。现在有人把这些基础设施做好了还免费，说实话没理由不用。你的 Agent 终于不用怕被网站封了。

当然免费的速率限制是有的，Search 每分钟 5 次，Fetch 每分钟 25 个 URL。轻度使用完全没问题，跑大批量任务的话还是得升级。但对个人开发者和想试试看的人来说，这个额度已经够了。

我有时候觉得，AI Agent 这个方向发展到今天，最大的瓶颈其实不是模型不够聪明。

模型已经很聪明了。Claude Opus 4.7、GPT-5 这些你丢一个复杂指令过去，它理解得明明白白。瓶颈在于 Agent 能触达的世界太小了。它被关在一个没有浏览器的房间里，你喂什么它看什么，自己啥也看不到。

现在有人把这扇窗户打开了。不管你用的是 Claude Code 还是 OpenClaw 还是 Hermes 还是自己从零搭的 Agent，你都能零成本地让你的 Agent 拥有搜索和阅读互联网的能力。

免费的基建，开放的接口，加上越来越聪明的模型。

这三样东西凑在一起的时候，会发生什么？

谢谢你看我的文章，我们，下次再见。

想深入研究？可以点击阅读原文查看

《TinyFish 零基础玩转指南》

》

阅读原文

继续滑动看下一个

开发者阿橙

向上滑动看下一个