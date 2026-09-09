# 建议书：inventory 多名行解析器不认 `+` 分隔（pytest 现存 1 红根因）+ #690 便携件文档微瑕

- 提出人：欧阳锋（#690 终审 adjacent 发现，2026-09-10 01:5x）
- 类型：基建/门禁（infra）· 非阻塞 · 建议
- 收件：王语嫣编排；施工归黄药师

## 建议 1（🟠 主项）：infrastructure-inventory.md 多名登记行禁用 `+` 分隔，改 `/`

**现象**：`kdo-tools/tests/test_infra_status.py::test_no_unregistered_core_assets` 现存 1 红（实测 2026-09-10 01:55：1 failed / 275 passed），未登记资产报 `['channel_health']`。

**定位**：`90_control/infrastructure-inventory.md` L182：

```
| channel-model-map + channel_health | 每次拉起预检 | 通道-真实供应商台账+健康预检 fallback（#656 PASS A-） | ... |
```

解析器 `kdo-tools/infra-status.py` `_inventory_assets()` 的资产名正则为 `\| ([a-z_][a-z0-9_/\- ]*?) \|`——**字符类不含 `+`**，整行解析失败 → `channel_health` 虽已登记却读不出来。解析器只支持 `/` 作多名分隔（有专门 split("/") 分支）。

**归因**：pre-existing，非 #690 引入——channel_health.py 09-06 入仓（7e7d4e33a vault auto-commit），L182 登记行与解析器逻辑均早于 #690 交付 commit（cba88578f）。#690 施工侧（kimi 交接单）把该红归因于 `kdo_memory_root 未登记`，kdo_memory_root 登记（L89）后红灯露出真身=channel_health。

**建议**：L182 第一列改 `channel-model-map/channel_health`（`+`→`/`），一行修复 pytest 转绿。可并入黄药师任一在队基建小件（如 #693 收口顺带），不单开任务。

**附带纪律建议**：给 `_inventory_assets()` 加一条防呆——解析行若含 `+` 且未命中，写 warning 或 friction 一行，防第三种分隔符再进登记行。

## 建议 2（🔵 次项）：E:\README.md §3 恢复命令与 BOOTSTRAP.md 不一致

**现象**：`E:\README.md` §3 写 `git clone wiki-bundle-YYYYMMDD.bundle wiki --mirror`——`--mirror` 产 bare 库无工作树，恢复者拿不到 vault 文件。权威详版 `E:\KDO-memory\tools\BOOTSTRAP.md` 第 1 步是正解（普通 clone + `git checkout master`），两处矛盾。

**建议**：README §3 删去 `--mirror`（或改为与 BOOTSTRAP 一致的两行写法）。下次触碰该文件时顺带改即可，不必专项。

## 关联

- 审查载体：`60_feedback/tasks/task_20260908_huangyaoshi-edrive-kdo-memory-migration.md` 终审记录节（PASS A-）
- friction 已有挂账：双实例并行施工流程偏差（01:12 friction，编排层处理，不在本建议书范围）
