---
id: '323'
assignee: huangyaoshi
status: pending_review
claimed_at: 2026-08-15
submitted_at: 2026-08-15
priority: P2
---

# #323：脚本输出 GBK 终端崩溃族统一修复（P2，基建 0.5d）

## 任务目标

Windows GBK 终端下，print 含 emoji/中文的 Python 脚本 exit 1（UnicodeEncodeError）——统一修复全部受影响脚本入口，消除"脚本能跑但崩在输出"的问题族。

> 来源：停车场 P-30（欧阳锋 #269 终审 2026-08-09 扣分点 + #272 语境识别同源问题族）。
> 已知先例：skill_bridge_sync / feature_menu 已做 `sys.stdout.reconfigure(encoding="utf-8")`——本次扫描确认覆盖范围后按同一模式补齐。

## 受影响清单（初判，待扫描确认）

- `kdo-tools/generate-dashboard.py`（#269 终审 A- 扣分点——HTML 已生成不影响功能，但 print 崩溃）
- `kdo-tools/*.py` 中 print 含 emoji/中文且无 reconfigure 的入口脚本
- `40_outputs/code/scripts/*.py` 同族风险

## 修复方案

统一模式：脚本入口加
```python
sys.stdout.reconfigure(encoding="utf-8")
```
（import sys 后、首个 print 前；需兼容 Python <3.7 则 try/except 包裹）。

## 产出

- 全部风险脚本入口修复（diff 清单）
- GBK 终端实测：`chcp 936` 下运行脚本不崩溃、输出正常
- 相关回归：受影响脚本各自跑一遍冒烟（如 generate-dashboard.py 重跑）

## 验收标准

1. 扫描报告：全部脚本打印检查覆盖，无遗漏
2. GBK 终端（chcp 936）实测 exit 0，emoji/中文正常输出
3. 不影响非 GBK 环境（UTF-8 环境行为不变）

---

## 执行报告（2026-08-15）

### 交付：52 个脚本统一加 GBK 输出保护

**修复模式**（与 skill_bridge_sync/queue_transition 既有模式一致）——每个脚本首个 import 语句后插入：

```python
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
```

hasattr 保护 = Python <3.7 兼容；errors="replace" = 极端字符不崩只替换。

**覆盖范围（52 个，扫描口径 `reconfigure|PYTHONIOENCODING|PYTHONUTF8` 全部命中）**：

| 目录 | 数量 | 代表 |
|:--|:--|:--|
| kdo-tools/ | 5 | generate-dashboard.py（#269 扣分点）/watch_inbox/aesthetic-library-builder/dedup_sources/mcp-reachability-check |
| 40_outputs/code/scripts/ | 14 | auto-related/batch-domain-fix/describe-images×2/generate-images×2/ocr-images×2 + _前缀诊断脚本 8 个 |
| 90_control/scripts/ | 33 | vault-backup/vault-snapshot/check_dead_links/check_skill_cards/queue_gate/kcard-quality-gate 等 |

**扫描发现的 4 个既有 guard 文件不重复插入**：feature_menu.py / skill_bridge_sync.py / queue_transition.py / auto-related.py（auto-related 首扫误报，二次口径确认无 guard 已修）。

### 验证（三层全过）

1. **编译**：137 个 .py 全部 py_compile 通过，0 失败（2 个 SyntaxWarning 为历史遗留无效转义，与本次无关）
2. **GBK 崩溃对照实测**：`PYTHONIOENCODING=gbk` 下裸 `print("✅")` exit=1（UnicodeEncodeError '✅'）——修复后 generate-dashboard/vault-snapshot/feature_menu 同环境 exit=0 且 emoji 正常输出
3. **回归**：test_feature_menu.py 28/28 全过；generate-dashboard 重跑正常（302 任务统计不变）

### 变更清单

52 个文件，每个 +6 行（import sys + 4 行 reconfigure 块 + 空行），无逻辑改动。

### 遗留

- P-29（production-queue.md 文件编码混排）是文件编码问题不同域，本次未动——P-30 备注"与 P-29 归并一次清"，如要一起清需另开任务
- GBK 崩溃族根因（Windows 终端默认 GBK + Python 默认按终端编码输出）——reconfigure 是脚本侧兜底，如需根治可建议用户终端切 UTF-8（chcp 65001 或 Windows Terminal），但脚本侧保护仍应保留（换机/换终端仍可能遇到 GBK）

## 终审记录（2026-08-15 欧阳锋）

**verdict: PASS A- · methodology v2.3**

O3 独立验证（全部字节级重跑，不采信报告）：
1. 改动面：git/find 双证今日修改 = 52 个 .py，与报告一致 ✅
2. Coverage：52 个全部含 `reconfigure(encoding="utf-8", errors="replace")` 块，0 缺失 ✅
3. 无重复插入：新旧模式 comm 交集为空；feature_menu（历史 guard）今日 0 修改 ✅
4. 编译：137/137 全过（2 个 SyntaxWarning 历史遗留）✅
5. GBK 崩溃对照实测：裸 print("✅") PYTHONIOENCODING=gbk 下 UnicodeEncodeError 复现；修复后 generate-dashboard/vault-snapshot/watch_inbox 同环境 exit=0 正常输出 ✅
6. 回归：test_feature_menu 28/28 ✅
7. 报告"302 任务统计不变" vs 实测 303：非回归——队列期间新增 #319-322/324（王语嫣 08-15 入队），303=297+5+1 自洽 ✅

小瑕疵（记 TODO 不阻断）：
- 报告"4 个既有 guard"列举不精确（实际历史 guard ≥15，feature_menu/skill_bridge_sync 亦为 errors=replace 款）——行为正确仅口径描述不准
- generate-dashboard.py 双 import sys（新增块与原有重复）——无害

结论：PASS A-，GBK 终端崩溃族修复有效，验收通过。

### 瑕疵跟进（2026-08-15 黄药师）

- ✅ 双 import sys 已清：删重复行，compile OK + PYTHONIOENCODING=gbk 实测 exit 0（303 任务，与终审一致）
- 口径瑕疵：记录在案——实际历史 guard ≥15 个，扫描口径 `reconfigure|PYTHONIOENCODING|PYTHONUTF8` 对已 guard 文件全部跳过（feature_menu 等今日 0 修改已由终审 comm 验证），行为正确
