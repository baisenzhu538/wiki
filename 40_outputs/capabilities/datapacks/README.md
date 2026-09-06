# DataPack 库（厂级领域弹药库）

> 依据：framework-encapsulation-methodology（六层形态最底层）+ diag_20260906_wangyuyan-datapack-alignment 对齐稿。
> DataPack=陈述性弹药（金标准/真实案例/踩坑实录/对照数据），Skill=程序性步骤。两者配合：Skill 引用 DataPack 自检。

## 规范四要素（每个 datapack 必备）
1. **真实样例**（金标准）：好的输出长什么样
2. **反例**（踩坑实录）：失败的样本与原因
3. **对照数据**：可量化的判断依据
4. **使用说明**：适用问题/何时挂载/更新日期/来源锚

## 目录约定
`<域>-<主题>/README.md`（frontmatter: type: datapack / domain / updated / source_refs）+ 样例文件

## 在库
| DataPack | 状态 | 说明 |
|:--|:--|:--|
| `hongqigong-vision-goldstandard/` | ✅ 已产（2026-09-06，#660） | 识图金标准库：6 组金标准 + 9 例踩坑实录 + 2 类无病例声明 + 置信三档对照 |
| `duanwangye-登录内容样本/`（待产） | ⏳ 试点二，段王爷整理 | 登录内容样本库（#661，脱敏入库） |
