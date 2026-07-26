---
id: task_20260726_wangyuyan-aliases-source-lint
task_id: 209
assignee: huangyaoshi
status: queued
created_at: 2026-07-26
domain: system
priority: P1
---

# 牌L9：aliases 源材料名检查

## 规则

> 源材料名必须出现在 aliases 中。否则用户搜"坏世界研究"找不到叫"协作底层哲学"的卡。

## 检查逻辑

```
source_refs 含 "坏世界研究/赵汀阳-坏世界研究-拆书-口述.txt"
  → 提取源材料名: "坏世界研究"
  → aliases 是否含 "坏世界研究"?
  → 没有 → WARNING
```

与 #199 定位声明 lint 同级（WARNING，不阻断），同文件实现——黄药师在 `kdo/pre_submit.py` 加 `_check_aliases_has_source_name()`。

## 验收

新建一张卡：source_refs 引用了"某某拆书.txt"但 aliases 没有"某某"→ pre-submit 报 WARNING。

## 边界

- 存量卡不触发（同 #199 规则）
- source_refs 无法提取可读名称时（如纯 hash 路径）→ 跳过
