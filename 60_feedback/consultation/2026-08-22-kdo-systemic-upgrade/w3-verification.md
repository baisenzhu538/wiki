# W3 口径核实报告（会诊硬前置）

- **任务**：#412（P1，会诊关键路径：数字未出，B4 批表态冻结）
- **执行**：黄药师 · 2026-08-22 · 只读核实（未改任何文件）
- **方法**：风清扬自己的纪律——每数字附命令+输出原文，结论三态（属实/口径差异/不属实）

---

## 数字 1：「1354 卡 888 draft（65.6%）」分母口径

### 工具重跑输出

```
命令: find . -name "*.md" -not -path "./.git/*" -not -path "./_tmp/*" -not -path "./node_modules/*" | wc -l
输出: 12379          （全库 markdown 文档数）

命令: find 30_wiki -name "*.md" | wc -l
输出: 2865           （30_wiki 卡/文档数）

命令: grep -rl "status: draft" 30_wiki --include="*.md" | wc -l
输出: 803            （30_wiki 内 draft 文件数）

命令: grep -rl "status: draft" --include="*.md" . --exclude-dir=.git --exclude-dir=_tmp --exclude-dir=node_modules --exclude-dir=60_feedback --exclude-dir=00_inbox --exclude-dir=10_raw | wc -l
输出: 878            （全库[除 60_feedback/00_inbox/10_raw] draft 文件数）

命令: python yaml 级解析 30_wiki 全部 2865 张卡的 status 字段
输出: reviewed 1362 / draft 798 / enriched 641 / pending_review 32 / superseded 24 / stable 4 / deprecated 4
```

### 结论：**口径差异**（1354/888 组合无法从当前库精确复现）

| 声称 | 最近候选口径 | 差 |
|:--|:--|:--|
| 1354 卡 | 30_wiki reviewed 卡数 **1362**（yaml 解析） | −8 |
| 888 draft | 全库 grep draft **878**（排除 60_feedback/00_inbox/10_raw） | −10 |
| 65.6% | 888/1354 = 65.58% 数学吻合 | — |

- **65.6% 的比例数学成立**（888/1354），但两个分子的当前实测值（1362/878）均无法与声称值精确匹配——**疑为建议书写作时点的快照**（数字可能来自更早的统计，或使用不同的目录排除规则）
- 当前真实口径（供 B4 批用）：30_wiki 共 **2865 卡**，draft **798**（27.9%），reviewed 1362（47.5%），enriched 641（22.4%）
- 补充：`kdo cards --count` = 509（KDO 工具自身的"卡"口径，与上述均不同——工具口径本身需另议）

---

## 数字 2：production-queue.md 体积（声称 207KB）

### 工具重跑输出

```
命令: ls -la 70_product/tasks/production-queue.md | awk '{print $5}'
输出: 202741         （当前，mojibake 修复后）

命令: wc -c < 70_product/tasks/production-queue.md
输出: 202741

命令: ls -la 70_product/tasks/production-queue.md.bak-before-mojibake-fix | awk '{print $5}'
输出: 218056         （08-22 mojibake 修复前快照）
```

### 结论：**不属实**（量级对，数字不对）

- 当前实测 **202,741 字节**（198 KiB / 203 KB）
- 修复前快照 **218,056 字节**（213 KiB）
- 声称 207KB（= 211,968 B 或 207,000 B）与两个实测值均不匹配；KB 进制换算（1024/1000）也解释不了差异——**建议书写作时点可能更早，但按当前可验证数据不属实**

---

## 数字 3：5 处字节级副本清单（声称维度 5）

### 工具重跑输出

```
命令: python 全扩展名(.py/.yaml/.yml/.json/.cjs/.js/.cmd/.ps1/.bat) md5 对比 40_outputs/code/scripts/ vs kdo-tools/
输出: 同名文件字节级一致 = 4 处：
  - collect_wechat.py
  - douyin_cookie_extract.py
  - douyin_user_videos.py
  - wechat_link_monitor.py
```

### 结论：**不属实**（4 处，非 5 处）

- **字节级一致副本 4 处**（md5 全等），全部是微信采集/抖音采集管线脚本
- 另有同名不同字节 py 2 处（`40_outputs/code/scripts/` 与 `kdo-tools/` 均有但内容不同——活代码 vs 副本漂移候选）；单侧独有：A 侧 29 个、B 侧 39 个（多为 `_tmp_*` 调试脚本和 kdo-tools 工具）
- 注：`kdo-tools/mcp/` 的 server.py 等曾因漂移被 #359 收口删除副本（指针引用模式已建立）——本次 4 处一致的副本是否符合"指针引用"约定，待 B4 批裁决（本报告只列事实）

---

## 三数字汇总（供 B4 批表态）

| # | 声称 | 结论 | 当前实测 |
|:--|:--|:--|:--|
| 1 | 1354 卡 888 draft（65.6%） | **口径差异** | 2865 卡 / draft 798（27.9%）；候选口径 reviewed 1362、grep-draft 878 |
| 2 | queue 207KB | **不属实** | 202,741 B（修复后）/ 218,056 B（修复前） |
| 3 | 5 处字节级副本 | **不属实** | 4 处（collect_wechat / douyin_cookie_extract / douyin_user_videos / wechat_link_monitor） |

*黄药师 · 2026-08-22 · 每数字附命令+输出原文（风清扬纪律）*
