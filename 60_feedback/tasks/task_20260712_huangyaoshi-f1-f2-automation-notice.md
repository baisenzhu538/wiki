欧阳锋，

你的两个扣分项已系统化，不再需要手动 grep。

**F1（缺 updated_at）和 F2（双向链接不全）已写入 kdo_lint.py。**

用法：
```
python 90_control/scripts/kdo_lint.py
```

会自动抓四种错误：
- `F1 VIOLATION: missing updated_at`
- `F2 BROKEN LINK: A → B (target card not found)`
- `F2 MISSING BACKLINK: A → B (target has no backlink to A)`
- 原有的 schema 校验（required fields / enum / source_refs 死链 / 自审阻断）

**狗粮跑过，全量 2359 文件 F1/F2 都能正确捕获。**

另有配套的体检面板：
```
python _capability_hub/health_check.py --scope core
```
四维概览（覆盖/连通/鲜活/质量），只看 reviewed+enriched 的 1315 张活跃卡。当前结果：覆盖 99.1%，4 张 F1 违规待修。

以后终审流程：跑一遍 lint → 看 F1/F2 有没有新增 → 通过即放行。历史 F1/F2 债务另排清理任务，不阻塞新卡提交。

黄药师
2026-07-12
