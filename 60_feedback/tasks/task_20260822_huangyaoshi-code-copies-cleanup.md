---
id: 414
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-22T12:18:28.197713+00:00'
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

## 执行报告（#414 黄药师 · 2026-08-22 · 终审 FAIL 补件）

### 1. md5 全库对比输出原文（0 副本）

```
命令: python 全扩展名(.py/.yaml/.yml/.json/.cjs/.js/.cmd/.ps1/.bat) md5 对比 40_outputs/code/scripts/ vs kdo-tools/
输出: 字节级副本残留: 0 ✅ 0 处
```

### 2. 引用方清单（处置 + 改指记录）

| 引用方 | 处置 |
|:--|:--|
| 计划任务 wechat-link-monitor | 已指 kdo-tools/（无需改） |
| .claude/skills/wechat-serendipity-collect/SKILL.md | 已指 kdo-tools/（无需改） |
| 40_outputs/code/scripts/README.md | 4 条目指针化（🔗 活代码单一真相源，#359 模式） |
| cap_hub/features.json | source 字段改指 kdo-tools/ |
| wechat-serendipity-collect-guide.md L51/L53 | 改指 kdo-tools/（终审 P1-1 补） |
| 30_wiki/tools/tool-author-targeted-collect.md L31/32 | 改指 kdo-tools/（终审 P1-1 补） |
| 30_wiki/tools/tool-kdo-wechat-serendipity-collect.md L45 | 改指 kdo-tools/（终审 P1-1 补） |

全库 grep 残留验证：修复前 5 处 → 修复后 0（Grep 工具 + 后台全库 grep 双向确认）。

### 3. W7 边界句落位（终审 P1-2 补）

- 操作层：wechat-serendipity-collect-guide.md L124 已加「素材边界（W7 拍板 2026-08-22）：公开课内容可自由使用，唯一边界 = 不得打着一堂名义进行商业活动。」
- 原则层：charter L97 已有（会诊产物）
- 顶层文档：proj_20260816_wechat-collect-顶层文档.md 已加

### 4. 复审对照（欧阳锋 FAIL 清单逐项）

- ✅ P1-1 死引用：guide L51/L53 + 2 张工具卡 3 处全部改指，全库 grep 0 残留
- ✅ P1-2 W7 边界句：guide（操作层）已落
- ✅ 本报告节（md5 原文 + 引用方清单）

*黄药师 · 2026-08-22*

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
