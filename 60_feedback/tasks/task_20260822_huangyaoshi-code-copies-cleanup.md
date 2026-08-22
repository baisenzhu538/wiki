---
id: 414
assignee: huangyaoshi
status: queued
updated_at: '2026-08-22T12:05:06.524622+00:00'
---
# #414 清 4 处字节级代码副本（采集管线脚本）

- **任务号**：#414
- **状态**：queued
- **assignee**：huangyaoshi
- **优先级**：P0（会诊止血项）
- **立项**：2026-08-22 王语嫣（会诊 B4 批+W3 数字底座，decisions.md）

## 内容价值判断（#375 处置门禁补充节，2026-08-22 黄药师领取时补）

- **处置对象已读内容核实**：4 个文件在 `40_outputs/code/scripts/` 侧与 `kdo-tools/` 真身**字节级一致**（W3 核实 md5 全等，w3-verification.md 附输出）——删除副本**零内容损失**，真身保留
- **处置依据**：老朱会诊拍板（P0 止血项，decisions.md）；W3 数字 3 已由老朱确认
- **删除范围硬边界**：仅这 4 处字节级一致副本；同名不同字节的 2 处（活代码 vs 漂移候选）**只报告不处置**；若发现引用方依赖 40_outputs 侧路径 → 改指真身而非保留副本（E014 先查引用）
- **逐件老朱亲批**：本任务单即授权（会诊拍板 P0）；执行报告附 4 文件 md5 对比原文供复核

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

## 终审记录（2026-08-22 欧阳锋 · FAIL 退回，2 处动作未完成补件后复审）

**已达标（O3 独立验证）**：
- commit `ae2481e4c` 实锤：40_outputs 侧 4 文件删除（collect_wechat 407 行/douyin_cookie 76 行/douyin_user 100 行等）+ README 指针化（4 条目均"🔗 活代码单一真相源：kdo-tools/..."，#359 模式）✅
- 独立 md5 位置验证：4 文件现仅存在于 kdo-tools/（唯一真身），40_outputs 侧 0 副本 ✅
- cap_hub 改指（commit 含）✅

**① P1（阻断）**：**死引用未改指**——`40_outputs/code/scripts/wechat-serendipity-collect-guide.md` L53 表格仍写 `40_outputs/code/scripts/collect_wechat.py`（已删路径）。任务单动作 2「引用方改指真身」未覆盖文档引用。期望形态：guide 路径改 `kdo-tools/collect_wechat.py`（并 grep 全库确认无其他 40_outputs/code/scripts/collect_wechat|douyin 残留引用）。

**② P1（阻断）**：**W7 操作层边界句未落**——charter（原则层）L97 已有"唯一边界=不得打着一堂名义进行商业活动"✅，但任务单追加节明确「处置采集管线脚本时，顺带在采集管线规范文件加该边界句一行（操作层一行）」——采集管线规范文件（wechat-serendipity-collect-guide.md 等）grep 无该句。期望形态：采集管线规范文件加一行边界句（与 charter 措辞一致，以拍板原文为准）。

**③ 报告补全**：执行报告节缺失（commit message 有摘要但任务单未落执行报告）——补 md5 0 副本输出原文 + 引用方清单（含 guide 改指记录）。

**复审对照法**：补件后欧阳锋 FAIL 清单逐项 grep，3 分钟闭环。
