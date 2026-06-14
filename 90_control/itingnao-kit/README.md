# 听脑 API 工具包（Kimi Code CLI 适配）

为 Kimi Code CLI 工具链优化的本地工具包，不依赖 OpenClaw。

## 安装

API key 已写入 `~/.itingnao_api_key`，脚本会自动读取。也可通过环境变量 `ITINGNAO_API_KEY` 覆盖。

## 命令

```bash
cd 90_control/itingnao-kit

# 测试连通性
node src/test-connection.js

# 列出最近 5 条
node src/list-records.js --size 5

# 获取单条详情（含原文+纪要）
node src/get-record-detail.js --id 8038241

# 批量拉取所有元数据
node src/batch-list.js

# 批量拉取所有详情（默认 500ms 延迟，自动断点续传）
node src/batch-detail.js
```

## 输出位置

- 元数据：`10_raw/itingnao/metadata-latest.json` 和 `metadata-latest.csv`
- 详情：`10_raw/itingnao/details/<id>.json`
- 进度：`10_raw/itingnao/detail-progress.json`

## 批量处理原则

1. 先跑 `batch-list.js` 拿到全部 300+ 条元数据
2. 按名称/标签/主题做第一轮粗分类
3. 优先对药柜、医疗、客户访谈类录音跑 `batch-detail.js` 拉原文+纪要
4. 所有诊断层输出只写入 `60_feedback/`，不直接污染 `30_wiki/`
