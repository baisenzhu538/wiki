## 30_wiki/concepts/yt-entrepreneur-unit-model.md

- 问题：frontmatter 存在重复 `source_refs` 键，且 `author: "老顽童"---` 缺少换行导致 YAML 解析失败
- 处理：合并去重 source_refs，修复 frontmatter 格式
- 剩余：移除未注册的 source ID `src_20260609_d7793c3f`
- 待确认：`reviewed_by` 与 `author` 同为"老顽童"，属于自审
