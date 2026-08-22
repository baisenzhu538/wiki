---
id: 414
assignee: huangyaoshi
status: queued
updated_at: '2026-08-22T18:45:00+08:00'
---
# #414 清 4 处字节级代码副本（采集管线脚本）

- **任务号**：#414
- **状态**：queued
- **assignee**：huangyaoshi
- **优先级**：P0（会诊止血项）
- **立项**：2026-08-22 王语嫣（会诊 B4 批+W3 数字底座，decisions.md）

## 范围

W3 核实（w3-verification.md）的 4 处字节级副本：`40_outputs/code/scripts/` vs `kdo-tools/` —— collect_wechat.py / douyin_cookie_extract.py / douyin_user_videos.py / wechat_link_monitor（全为微信/抖音采集管线脚本）。

## 动作

1. **先查引用**（E014）：grep 全库+配置（脚本/cron/hermes profiles）谁调用了 `40_outputs/code/scripts/` 侧这 4 个文件
2. **处置**：kdo-tools/ 为唯一真身；40_outputs 侧删除并留指针 README（kdo-tools/mcp 指针引用模式，#359 先例）；引用方改指真身
3. **验收**：md5 全库对比输出 0 字节级副本（附命令+输出原文）；引用方功能回归（采集管线跑一次实测）
4. commit 入档（E040）；欧阳锋终审抽"指针模式真实性"

## 边界

- 只动这 4 处；同名不同字节的 2 处（活代码 vs 漂移候选）列入报告不处置（另议）
- 不动 kdo-tools/ 真身内容

---

## 追加（2026-08-22 王语嫣）：W7 素材来源边界句落操作层

> 来源：风清扬编排审计待修①，decisions.md 勘误。W7 拍板（老朱 08-22）：公开课内容可自由使用，**唯一边界=不得打着一堂名义进行商业活动**；不建登记册。

- **动作**：处置采集管线脚本时，顺带在采集管线规范文件加该边界句一行（一行，不展开）
- **定位**：操作层一行；原则层表述由 #416 基本法承载（两边措辞一致，以拍板原文为准）
