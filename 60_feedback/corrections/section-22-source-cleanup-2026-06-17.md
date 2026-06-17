# 第二十二节 13 张卡 source_refs 残留清理报告

**处理时间**：2026-06-17  
**负责人**：老顽童  
**处理原则**：
- hash 前缀 src_ID 补全为 `10_raw/sources/` 下完整相对路径；
- `00_inbox/` 路径的源文件复制归档到 `10_raw/sources/`，并采用 `src_YYYYMMDD_8hex` 命名；
- 不修改卡片 body；
- 不为了保持 enriched 而填虚假 source 或删除 source_refs。

## 变更明细

### `concept-minto-pyramid-principle`
- src_20260614_8269ccdb -> 10_raw/sources/src_20260614_8269ccdb-一堂-建模能力培训-truman-口述.md

### `yt-note-expert-interview-modeling`
- src_20260606_575627a4 -> 10_raw/sources/src_20260606_575627a4-一堂-AI时代清单体笔记-Truman-口述-01.md
- src_20260606_db4fc211 -> 10_raw/sources/src_20260606_db4fc211-一堂-AI时代请单体笔记-Truman-口述-02.md

### `yt-research-intelligence-map`
- src_20260504_13783111 -> 10_raw/sources/src_20260504_13783111-一堂调研武器库课程原文润色.md

### `yt-note-extensive-research-input`
- ARCHIVED: 00_inbox/一堂-AI时代请单体笔记-Truman-口述-02.txt -> 10_raw/sources/src_20260617_c5e5fb8e-一堂-ai时代请单体笔记-truman-口述-02.txt

### `yt-note-fact-pattern-insight`
- src_20260606_db4fc211 -> 10_raw/sources/src_20260606_db4fc211-一堂-AI时代请单体笔记-Truman-口述-02.md

### `concept-半肥猫-ai-learning-toolification-methodology`
- ARCHIVED: 00_inbox/半肥猫-AI学习落地-口述.md -> 10_raw/sources/src_20260617_f1830fa6-半肥猫-ai学习落地-口述.md
- ARCHIVED: 00_inbox/AI俱乐部-AI学习落地-半肥猫-笔记.txt -> 10_raw/sources/src_20260617_26d0ee0b-ai俱乐部-ai学习落地-半肥猫-笔记.txt
- ARCHIVED: 00_inbox/AI俱乐部-AI学习落地-半肥猫-口述.txt -> 10_raw/sources/src_20260617_205eaa9b-ai俱乐部-ai学习落地-半肥猫-口述.txt

### `concept-纪浩-ai-collaboration-methodology`
- ARCHIVED: 00_inbox/纪浩-AI协作方法论-口述.md -> 10_raw/sources/src_20260617_627a8803-纪浩-ai协作方法论-口述.md
- ARCHIVED: 00_inbox/AI俱乐部-人和AI协作-纪浩-五层结构-结构化.md -> 10_raw/sources/src_20260617_50e2866a-ai俱乐部-人和ai协作-纪浩-五层结构-结构化.md
- ARCHIVED: 00_inbox/AI俱乐部-人和AI协作-纪浩-参考案例-结构化.md -> 10_raw/sources/src_20260617_15ca3bb2-ai俱乐部-人和ai协作-纪浩-参考案例-结构化.md

### `case-半肥猫-course-to-skill`
- ARCHIVED: 00_inbox/AI俱乐部-AI学习落地-半肥猫-口述.txt -> 10_raw/sources/src_20260617_2b8a01ce-ai俱乐部-ai学习落地-半肥猫-口述.txt
- ARCHIVED: 00_inbox/AI俱乐部-AI学习落地-半肥猫-笔记.txt -> 10_raw/sources/src_20260617_629e996c-ai俱乐部-ai学习落地-半肥猫-笔记.txt

### `case-纪浩-from-zip-to-five-layers`
- src_20260606_6ea91aa8 -> 10_raw/sources/src_20260606_6ea91aa8-纪浩-AI协作方法论-口述.md
- src_20260606_592137a7 -> 10_raw/sources/src_20260606_592137a7-AI俱乐部-AI协作方法论-纪浩-笔记.md
- src_20260609_9223aac2 -> 10_raw/sources/src_20260609_9223aac2-ocr-ai俱乐部-人和ai协作-纪浩-参考案例-图片02.md

### `yt-business-analysis-cognitive-biases`
- ARCHIVED: 00_inbox/一堂五步法/一堂-一堂五步法-序言-口述.txt -> 10_raw/sources/src_20260617_670c28d4-一堂-一堂五步法-序言-口述.txt
- ARCHIVED: 00_inbox/一堂五步法/一堂-一堂五步法-落地实操-口述.txt -> 10_raw/sources/src_20260617_3c05beda-一堂-一堂五步法-落地实操-口述.txt

### `yt-five-step-level-blindspots`
- src_20260611_d913eb1d -> 10_raw/sources/src_20260611_d913eb1d-一堂-一堂五步法-序言-口述.md
- src_20260611_c0e6e182 -> 10_raw/sources/src_20260611_c0e6e182-一堂-一堂五步法-单元模型-口述.md
- src_20260611_f500a6ea -> 10_raw/sources/src_20260611_f500a6ea-一堂-一堂五步法-落地实操-口述.md

### `yt-lean-false-model-ai`
- 已因 KF-021 缺失 source 降级为 draft，source_refs 为空，未改动

## 归档的新 source 文件

| 新 source ID | 原 `00_inbox` 路径 | 新 `10_raw/sources/` 路径 |
|:---|:---|:---|
| `src_20260617_c5e5fb8e` | `00_inbox/一堂-AI时代请单体笔记-Truman-口述-02.txt` | `10_raw/sources/src_20260617_c5e5fb8e-一堂-ai时代请单体笔记-truman-口述-02.txt` |
| `src_20260617_f1830fa6` | `00_inbox/半肥猫-AI学习落地-口述.md` | `10_raw/sources/src_20260617_f1830fa6-半肥猫-ai学习落地-口述.md` |
| `src_20260617_26d0ee0b` | `00_inbox/AI俱乐部-AI学习落地-半肥猫-笔记.txt` | `10_raw/sources/src_20260617_26d0ee0b-ai俱乐部-ai学习落地-半肥猫-笔记.txt` |
| `src_20260617_205eaa9b` | `00_inbox/AI俱乐部-AI学习落地-半肥猫-口述.txt` | `10_raw/sources/src_20260617_205eaa9b-ai俱乐部-ai学习落地-半肥猫-口述.txt` |
| `src_20260617_627a8803` | `00_inbox/纪浩-AI协作方法论-口述.md` | `10_raw/sources/src_20260617_627a8803-纪浩-ai协作方法论-口述.md` |
| `src_20260617_50e2866a` | `00_inbox/AI俱乐部-人和AI协作-纪浩-五层结构-结构化.md` | `10_raw/sources/src_20260617_50e2866a-ai俱乐部-人和ai协作-纪浩-五层结构-结构化.md` |
| `src_20260617_15ca3bb2` | `00_inbox/AI俱乐部-人和AI协作-纪浩-参考案例-结构化.md` | `10_raw/sources/src_20260617_15ca3bb2-ai俱乐部-人和ai协作-纪浩-参考案例-结构化.md` |
| `src_20260617_2b8a01ce` | `00_inbox/AI俱乐部-AI学习落地-半肥猫-口述.txt` | `10_raw/sources/src_20260617_2b8a01ce-ai俱乐部-ai学习落地-半肥猫-口述.txt` |
| `src_20260617_629e996c` | `00_inbox/AI俱乐部-AI学习落地-半肥猫-笔记.txt` | `10_raw/sources/src_20260617_629e996c-ai俱乐部-ai学习落地-半肥猫-笔记.txt` |
| `src_20260617_670c28d4` | `00_inbox/一堂五步法/一堂-一堂五步法-序言-口述.txt` | `10_raw/sources/src_20260617_670c28d4-一堂-一堂五步法-序言-口述.txt` |
| `src_20260617_3c05beda` | `00_inbox/一堂五步法/一堂-一堂五步法-落地实操-口述.txt` | `10_raw/sources/src_20260617_3c05beda-一堂-一堂五步法-落地实操-口述.txt` |

## 验证结果

```bash
python 90_control/scripts/kcard-quality-gate.py
```

结果：

```text
total=1193, p0=0, p1=18, clean=1175, yaml_error=0
```

- **P0 = 0**：无阻塞问题。
- **P1 = 18**：全部为 KF-021 处理后因降级为 `draft` 导致 `source_refs` 为空的卡片，与本清理任务无关。
- **13 张目标卡 source_refs 中已无 `00_inbox/` 路径或 hash 前缀 src_ID。**
- **YAML 错误 = 0**。
