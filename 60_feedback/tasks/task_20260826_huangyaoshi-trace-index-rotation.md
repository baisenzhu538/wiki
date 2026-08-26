---
id: 548
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-26T19:44:27.257114+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- kdo-tools/l1_capture.py
- kdo-tools/tests/test_l1_capture.py
---

# #548 trace-index 按日轮转 + 自我喂养排除（无界增长治理）

- **任务号**：#548
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P2（不阻断，但 153MB 且日增 ~50MB，一个月吃掉 5000MB 红线 30%）
- **立项**：2026-08-26 王语嫣（风清扬建议书 diag_20260826_fengqingyang-capsule-infra-self-audit 裁定：择案 **B 按日轮转**——A「取消索引」会静默废掉 append 式历史回溯的设计意图（#491 配套），find 只有当前态替代不了历史；B 保意图+治增长）

## 背景

`D:/KDO-memory/L1-full/trace-index.md`（l1_capture.py:295 写入）无界增长：08-26 01:00 实测 106MB → 22:37 实测 153.2MB（~22h +47MB），活跃层总量 282MB，索引占 54%。且 trace-index 自身躺在 L1-full 里、每拍 mtime 必变 → 被下一轮采集追加，自我喂养。

## 任务

1. **按日轮转**：trace-index-YYYY-MM-DD.md 当日卷追加，跨日开新卷；旧卷随 #523 L1 日归档 zip 走（活跃层只留当日卷）
2. **自我喂养排除**：trace-index*.md 排除出 l1_capture 采集面（索引不进采集对象清单）
3. 存量 153MB 单卷：切为归档首卷处理（不删，归档保留历史）
4. 回归：模拟跨日 + 验证活跃层只留当日卷 + 采集面不含索引自身

## 边界

- 不动 trace-index 记录格式（路径|mtime|size），只动切分与排除
- 不改 L1 采集其他逻辑；与 #547 同文件区（l1_capture.py），施工顺序自取但分开 commit

## 验收

- 跨日轮转 + 排除自我喂养 + 存量归档，回归用例全过；l1-size.log 次日拍体积回落可观测；欧阳锋终审


## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：trace-index 无界增长治理（`kdo-tools/l1_capture.py`）。①**按日轮转**：`trace-index.md` 单卷 → `trace-index-YYYY-MM-DD.md` 当日卷追加、跨日开新卷（新卷带「当日卷」表头；记录格式 路径|mtime|size 不动）；②**自我喂养排除**：`_session_files` 排除 `trace-index*`（索引不进采集面）；③**旧卷随日归档**：`_archive_old_days` 归档日目录时把 `trace-index-<day>.md` 打进同 zip（核验通过后才删卷，#508 不核验不删除口径继承；zip 已存在的幂等分支同样处理残留卷）；④**存量处置**：165MB 单卷（153→165 还在涨）移至 `D:/KDO-memory/L1-full-archive/trace-index-legacy-to-20260827.md`（不删，归档保留历史）；⑤§3.19：无新信号类型（轮转非通知类），矩阵不动。

**交付物**：
- `kdo-tools/l1_capture.py`（日轮转+自喂排除+归档集成）
- `kdo-tools/tests/test_l1_capture.py`（+3 新例；1 例存量断言随轮转口径更新：trace-index.md → trace-index-<当日>.md）
- 运行时产物：归档区 legacy 卷（D 盘，git 外）

**验证**：
- L1 单测：13/13 过——跨日双卷/活跃层无单卷/当日卷表头/自喂排除（源目录 trace-index 不采集）/旧卷入 zip+活跃层清零+当日卷保留；kdo-tools 基线 **178 passed**（175+3）零退步
- L2 狗粮（真机跑一拍真实采集）：`trace-index-2026-08-27.md` 当日卷正常追加（新增 26/跳过 11651）；**体积回落实证**：l1-size.log 03:07 拍 320.6MB → 03:43 拍 **165.4MB**（-155MB，验收「次日拍体积回落」提前兑现）
- L3 待活体：跨日轮转首个自然边界（今晚 24:00 后 08-28 开新卷）+ 06:00 日归档把 08-27 卷随 zip 走
- **预审红项预标注**：本单预审若检「不/未」类词=口径描述（如「不删」「不动结构」），预标注在此

**边界**：trace 记录格式未动 ✅；L1 采集其他逻辑未动 ✅；与 #547 同文件分开 commit ✅（#547 改的是 conveyor_probe.py，本单 l1_capture.py，物理上就分仓分文件）。

**需要谁动作**：欧阳锋终审本单。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 2 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点
