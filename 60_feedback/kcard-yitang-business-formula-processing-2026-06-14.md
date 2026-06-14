# 一堂「业务公式拆解」课程资料 KDO 处理完成报告

> 处理人：老顽童  
> 时间：2026-06-14  
> 输入：`00_inbox/关键假设C-拆解业务公式/` 下的 7 份材料  
> 输出：7 条 source 记录、5 张知识卡、1 张既有卡更新

---

## 一、输入材料清单

| 原文件 | 类型 | 处理后位置 |
|---|---|---|
| `孔源-业务公式-逐字稿01.txt` | 逐字稿 | `10_raw/sources/src_20260613_6b939d2b-yitang-business-formula-decomposition-transcript.md` |
| `孔源-业务公式拆解-笔记.txt` | 培训笔记 | `10_raw/sources/src_20260613_6edbf0af-yitang-business-formula-decomposition-notes.md` |
| `孔源-业务公式拆解-口述.txt` | 口述稿 | `10_raw/sources/src_20260613_a8bcfd38-yitang-business-formula-decomposition-oral.md` |
| `孔源-业务公式拆解-十大业务公式范式.png` | 模型图 | `10_raw/assets/yitang-business-formula/孔源-业务公式拆解-十大业务公式范式.png` |
| `孔源-业务公式拆解-6层逻辑关系图.png` | 模型图 | `10_raw/assets/yitang-business-formula/孔源-业务公式拆解-6层逻辑关系图.png` |
| `孔源-业务公式拆解-ABC模型图.png` | 模型图 | `10_raw/assets/yitang-business-formula/孔源-业务公式拆解-ABC模型图.png` |
| `孔源-业务公式拆解-冰山模型图.png` | 模型图 | `10_raw/assets/yitang-business-formula/孔源-业务公式拆解-冰山模型图.png` |

### OCR 派生输出

| 原图 | OCR 文本 |
|---|---|
| 十大业务公式范式图 | `10_raw/assets/yitang-business-formula/孔源-业务公式拆解-十大业务公式范式-ocr.md` |
| 6 层逻辑关系图 | `10_raw/assets/yitang-business-formula/孔源-业务公式拆解-6层逻辑关系图-ocr.md` |
| ABC 模型图 | `10_raw/assets/yitang-business-formula/孔源-业务公式拆解-ABC模型图-ocr.md` |
| 参数冰山图 | `10_raw/assets/yitang-business-formula/孔源-业务公式拆解-冰山模型图-ocr.md` |

---

## 二、Source 注册

已在 `.kdo/state.json` 和 `90_control/source-registry.yaml` 中注册 7 条 source：

- `src_20260613_6b939d2b`：逐字稿
- `src_20260613_6edbf0af`：培训笔记
- `src_20260613_a8bcfd38`：口述稿
- `src_20260613_8bfdc3d1`：十大业务公式范式图
- `src_20260613_0ab21e5e`：6 层逻辑关系图
- `src_20260613_91f90839`：业务公式 ABC 模型图
- `src_20260613_fa7b370d`：参数冰山图

同时关联了 itingnao 录音 source：`src_20260614_6d9f7671`（一堂业务公式拆解培训）。

---

## 三、知识卡产出

### 新建卡片（5 张）

| 文件 | 类型 | 标题 |
|---|---|---|
| `30_wiki/frameworks/yt-business-formula-abc-model.md` | framework | 业务公式 ABC 模型（Ambition-Basis-Connection） |
| `30_wiki/concepts/yt-business-formula-ten-paradigms.md` | concept | 一堂业务公式十大经典范式 |
| `30_wiki/concepts/yt-business-formula-parameter-iceberg.md` | concept | 业务公式参数冰山（L1-L6） |
| `30_wiki/concepts/yt-business-formula-six-level-logic.md` | concept | 业务公式六层逻辑关系（L1 模糊 → L6 动态） |
| `30_wiki/cases/case-toc-ecommerce-formula-misjudgment.md` | case | ToC 消费品电商：业务公式拆解误判导致放量亏损 |

### 更新卡片（1 张）

| 文件 | 更新内容 |
|---|---|
| `30_wiki/concepts/yt-management-business-formula.md` | 添加 domain、source_refs、confidence、trust_level，补充 5 个新卡片相关链接 |

---

## 四、索引更新

已在 `30_wiki/index.md` 顶部追加 5 张新卡的标准 Markdown 链接。

---

## 五、Lint 验证

运行 `kdo lint` 后，新产出的 6 张卡片（5 新 + 1 更新）未出现 ERROR/WARNING。

项目整体 lint 仍有大宗历史债务，与本次处理无关。

---

## 六、处理说明

1. **图片 OCR**：已在隔离虚拟环境 `_tmp/ocr_venv/` 中完成。修复了 onnxruntime + NumPy 版本兼容问题，使用 RapidOCR 对 4 张模型图进行 OCR，平均置信度 0.97+。OCR 文本已保存为 `-ocr.md` 文件，并注册为对应 image source 的 `derived_outputs`。
2. **source 格式**：文本类 source 从 `.txt` 转为 `.md`，符合 `10_raw/sources/` 既有命名规范。
3. **已有卡片去重**：发现 `yt-management-business-formula.md` 已存在且质量较高，本次未重复建卡，而是将其作为母卡，新模型作为子卡链接进去。

---

## 七、后续建议

1. 如需补充更多案例（私域电商、培训续费、口腔诊所），可从同一培训材料中提取。
2. 建议王语嫣对第二批 9 张复合卡的原文回填继续按原计划执行。
3. 建议欧阳锋评估是否需要把 `00_inbox/关键假设C-拆解业务公式/` 原始文件归档或删除，避免与 `10_raw/sources/` 重复。
