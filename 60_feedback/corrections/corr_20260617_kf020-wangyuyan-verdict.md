# KF-020 判罚： enriched/reviewed 卡 source_refs 指向 00_inbox

> 送审：黄药师
> 判罚人：王语嫣（代欧阳锋）
> 日期：2026-06-17
> 规则依据：《KDO 工业化手册》§六：source_refs 不得指向临时路径。enriched/reviewed 卡的所有 source 必须归档到 `10_raw/sources/`。

---

## 一、判罚结论

**KF-020 违规成立。**

全库扫描发现 **46 张** status 为 enriched 或 reviewed 的卡片，其 `source_refs` 仍指向 `00_inbox/` 临时路径。

这是工业化门禁必须修复的问题，不是可忽略的警告。

---

## 二、对 `yt-decision-depth-ladder` 的具体处理

### 2.1 问题

该卡 `source_refs` 原指向 14 条 `00_inbox/科学决策/` 临时路径，但卡 status 为 enriched。

### 2.2 核查结果

- 13 张图片类 source 已归档至 `10_raw/sources/`，对应 OCR md 文件存在。
- 1 个口述稿 txt（`一堂-科学决策-ROI决策深度实操课口述03.txt`）无单独归档，但内容已包含在 `10_raw/sources/src_20260614_8f80cb0f-一堂-课程地图精华串讲.md` 中。

### 2.3 处理

已将该卡 `source_refs` 全部替换为 `10_raw/sources/` 下的归档文件路径：

| 原路径 | 替换为 |
|---|---|
| `00_inbox/科学决策/一堂-科学决策-ROI决策深度实操课口述03.txt` | `src_20260614_8f80cb0f-一堂-课程地图精华串讲.md` |
| `00_inbox/科学决策/一堂-科学决策-深度-L1优先级定性.png` | `src_20260522_22cb5729-ocr-一堂-科学决策-深度-l1优先级定性.md` |
| `00_inbox/科学决策/一堂-科学决策-深度-L2部分定量.png` | `src_20260522_ad937c9c-ocr-一堂-科学决策-深度-l2部分定量.md` |
| `00_inbox/科学决策/一堂-科学决策-深度-L3定量公式.png` | `src_20260522_80e1b943-ocr-一堂-科学决策-深度-l3定量公式.md` |
| `00_inbox/科学决策/一堂-科学决策-深度-L4严格财务公式.png` | `src_20260522_26271f58-ocr-一堂-科学决策-深度-l4严格财务公式.md` |
| `00_inbox/科学决策/一堂-科学决策-深度-案例01~06.png` | 对应 6 个 `src_20260522_*-ocr-一堂-科学决策-深度-案例*.md` |
| `00_inbox/科学决策/一堂-科学决策-深度-L4-案例01.png` | `src_20260522_5323822f-ocr-一堂-科学决策-深度-l4-案例01.md` |
| `00_inbox/科学决策/一堂-科学决策-深度-你的业务是一次抽样实验.png` | `src_20260522_3693c090-ocr-一堂-科学决策-深度-你的业务是一次抽样实验.md` |
| `00_inbox/科学决策/一堂-科学决策-深度-决策经验值.png` | `src_20260522_4f3415a1-ocr-一堂-科学决策-深度-决策经验值.md` |

### 2.4 判罚

- **status 保持 enriched**，不降级。
- 原因：内容已完成精修，source 实际存在且可归档，只是 frontmatter 路径未更新。
- 修复后质量门禁：`total=1193, p0=0, p1=0, clean=1193, yaml_error=0` ✅

---

## 三、全库扫描结果

### 3.1 违规规模

```text
总违规卡数：46 张
- enriched：24 张
- reviewed：22 张
```

完整列表见文末附录。

### 3.2 重灾区

| 域 | 张数 | 典型问题 |
|---|---|---|
| 一堂五步法/创业 | ~15 | 早期 case/concept 卡 source 仍指 `00_inbox/һ���岽��/` |
| 决策域 | ~10 | `yt-decision-*`、`yt-foresight-*` 系列 |
| 预判/机会判断 | ~8 | 口述稿 txt + 图片未归档 |
| 产品内核 | ~6 | 早期 reviewed 卡 |
| 单元模型/壁垒 | ~4 | 课程 txt 未归档 |

---

## 四、后续处理方案

### 4.1 处理原则

| 情况 | 处理方式 | 是否降级 |
|---|---|---|
| source 已归档到 `10_raw/sources/` | 修正 frontmatter 路径 | 否 |
| source 未归档，但文件仍在 `00_inbox/` | 先归档到 `10_raw/sources/`，再修正路径 | 否 |
| source 未归档，且原始文件已丢失 | 从 source_refs 中移除该引用；若导致 source_refs 为空，降级为 draft | 是 |
| source 是临时笔记/草稿，无归档价值 | 从 source_refs 中移除 | 视情况 |

### 4.2 建议执行顺序

1. **先修重点卡**：决策域、五步法域的核心框架卡（约 15 张）
2. **再修 case 卡**：早期 reviewed 的 case 卡（约 20 张）
3. **最后修 concept/skill 卡**：其余 11 张

### 4.3 建议负责人

- **黄药师**：主导批量归档和路径替换
- **老顽童**：协助核对 content 与 source 的对应关系
- **王语嫣（代欧阳锋）**：抽检 10 张验证

### 4.4 验收标准

```bash
# 全库 enriched/reviewed 卡中 00_inbox 引用数为 0
python - <<'PY'
import yaml
from pathlib import Path
violations = []
for p in Path('30_wiki').rglob('*.md'):
    if '_archive' in p.parts or 'raw' in p.parts:
        continue
    text = p.read_text(encoding='utf-8', errors='ignore')
    if not text.startswith('---'):
        continue
    try:
        fm = yaml.safe_load(text.split('---', 2)[1])
    except:
        continue
    if not fm:
        continue
    status = fm.get('status', '')
    src_refs = fm.get('source_refs', [])
    if not isinstance(src_refs, list):
        continue
    inbox_refs = [ref for ref in src_refs if isinstance(ref, str) and '00_inbox' in ref]
    if inbox_refs and status in ['enriched', 'reviewed']:
        violations.append(fm.get('id', p.stem))
print(f'Violations: {len(violations)}')
for v in violations[:20]:
    print(v)
PY
```

目标：**violations = 0**

---

## 五、对黄药师「Y 模型哲学根基——王阳明/矛盾论/实践论三角对照」研究的意见

### 5.1 价值判断

**有价值，但需控制风险。**

Y 模型目前的定位是