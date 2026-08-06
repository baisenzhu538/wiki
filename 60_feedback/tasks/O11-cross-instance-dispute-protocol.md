---
id: O11-cross-instance-dispute-protocol
title: "O-11 跨实例事实分歧裁决协议"
type: parking-lot
status: active
created_at: 2026-08-04
created_by: 欧阳锋（裁决） + 王语嫣（采纳）
domain: kdo
---

# O-11 跨实例事实分歧裁决协议

> **触发场景**：跨实例（飞书/Claude/Hermes等）对"文件原版状态 / 谁引入破坏"意见不一致时。

## 协议（3步）

1. **双方各自跑严格 git 验证**——字节级输出、明确提交 hash、严格 UTF-8 解码（禁止 errors='replace' 宽容模式）
2. **附时间线证据链**（如"#223 审查时 0 失败 → 某批后失败"）
3. **以字节证据为准**，不凭"谁说的"

## 触发案例

**#224 终审（2026-08-04）**：王语嫣质疑 dk-yi-tang-wishful-thinking-kills-startups 为"历史遗留损坏（7/27即坏）"——欧阳锋 O3 严格重验（字节级+UTF-8严格解码+yaml.safe_load）证明 7/27 原版健康（6587字节可解析），时间线证据（#223审查时dark-knowledges 0失败→#224批后失败）确认破坏为 hermes 引入。

**王语嫣错误根因**：初判用了 `errors='replace'` 宽容解码 + frontmatter 边界误匹配——把当前文件的损坏误读成"7/27即坏"。

## 相关

- 停车场编号：本协议为 **O-11**（O-10 已被"自查脚本 import 劫持"占用，见 #218 任务单）
- 教训：验证必须模拟真实读取路径（严格解码），不凭直觉/宽容模式
