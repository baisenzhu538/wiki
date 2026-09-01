---
id: task_20260902_huangyaoshi-scatter-relocation-misc
title: 散点归位杂项（散点审计 R7，P1）：假盘符树 + Harness 重复对 + mp4 归位
seq: 604
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
priority: P1
updated_at: '2026-09-01T21:48:52.571527+00:00'
instance: huangyaoshi-kimi
evidence: 60_feedback/tasks/task_20260902_huangyaoshi-scatter-relocation-misc.md
---

# #604 散点归位杂项

## 背景

风清扬审计 P1 三项归位杂项。

## 范围（三件）

1. **`C\uf03a/` 假盘符目录树**：WSL 写 `C:\...` 路径事故产物（`:` 被写成 Unicode PUA 字符）。核查内容是否全为重复垃圾 → 确认无独有内容后删除（有独有内容先归档隔离区）。
2. **Harness 重复对**：`00_inbox/Harness Engineering-….md` vs `00_inbox/Harness Engineering：….md`（md5 相同）——保留文件名规范的一份，另一份移隔离区。
3. **mp4 归位**：`60_feedback/wechat-collect/*.mp4` 6 个约 120MB 移 `10_raw/` 对应素材目录（反馈层不放素材）。若移动影响 wechat 管线脚本的路径假设，先 grep 脚本引用再动；有影响则在任务单执行报告中标注，不硬移。

## 安全栏

- 每件操作前先 grep 引用对账（含 30_wiki source_refs）。
- 假盘符树删除前列出完整文件清单入执行报告（证明无独有内容）。
- 批量三问。

## 交付物

三项处置结果 + 引用对账 + 执行报告五字段。

## 验收

欧阳锋终审：假盘符树清零 + Harness 重复对收敛 + mp4 归位且管线引用未断（或已标注）。

---

## 执行报告（2026-09-02 huangyaoshi-kimi）

**交付物**：`10_raw/assets/wechat-collect/`（6 个 mp4，git mv 保历史）+ 14 处转写稿源引用改指（10_raw/sources 8 处入仓、00_inbox 6 处本就 gitignore 不入仓）；工作 commit `e05395857`。隔离区落位（gitignore 不入仓，#600 口径）：`90_control/.sandbox/quarantine-20260902/fake-drive-tree/`（假盘符树 1 目录+2 散落 PUA 文件）、`Harness-Engineering-hyphen-dup.md`。

**完成内容**：
1. **假盘符树核查清除**：`C\uf03a/` 树仅 1 文件（kcard-quality-gate-report-2026-06-15.md，574B 截断版，md5 b9d28e08 ≠ 真实文件 65919B 版 3e7b15dc，内容为「扫描范围 0 张」的坏跑输出）+ 散落 PUA 文件 2 个（git_verify.txt 6.7KB 卡 frontmatter dump、pq_git.txt 108KB 队列 dump）——三者均 untracked、无独有内容（逐件 md5/内容比对），移隔离区 fake-drive-tree/（等效删除，留查）。
2. **Harness 重复对收敛**：三份 md5 全同（f6c9a2ea）——顶层连字符版移隔离区；保留顶层全角冒号版（`30_wiki/decisions/plan_20260621_kdo-quality-harness-upgrade.md:10` 功能引用它）与 `Harness Engineering/` 目录（doc_ 版+images）。
3. **mp4 归位**：6 个 mp4（约 125MB，git tracked）git mv → `10_raw/assets/wechat-collect/`。管线引用核查：`wechat_link_monitor.py` 的 WORK_DIR 只写新下载（L496 下载即转写，无回读存量），移动不断管线；存量 14 处转写稿「源」行引用旧路径（10_raw/sources 8 + 00_inbox 6），全部改指新位置（纯字符串替换，dry-run 14 处=apply 14 处=复核 0 残留）。

**验证**：根目录 `C\uf03a*` 清零（os.listdir 复核）；Harness 连字符版原位不存在、全角版在；6 mp4 新位置 ls 逐项在、旧位置清零；引用 grep 复核 0 残留；git mv 历史可追溯（rename 100%）。

**边界**：douyin-dali/ 子目录 mp4 及 6725b942182f6277/AWyGiJIRgc/f4faadff37c0b43b/7666646931699367986 等**不在本单 6 件范围**的旧 mp4 引用未动（它们指向的文件早已不在原位，属历史陈旧引用，与本单无关）；00_inbox 副本 6 处已改指但不入仓（00_inbox 在 .gitignore）；未碰 dispatch 台账（那是 #605 范围）。

**需要谁动作**：欧阳锋——终审 #604（验收点：假盘符树清零、Harness 重复对收敛、mp4 归位且引用未断——均已留证）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

⚪ 无路径级交付物声明（纯文档/诊断类或未用反引号标注路径）——差集无检查面
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（不存在）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）
