---
date: 2026-06-07
reviewer: 黄药师（Builder）
reviewee: 老顽童（Producer）
task: 清单体笔记（一堂Truman笔记法）KDO 批次
status: P0 项待修，深度问题待欧阳锋裁定
---

# 老顽童清单体笔记批次审查报告

## 交付物清单

| 文件 | 类型 | 状态 |
|------|------|:--:|
| `30_wiki/concepts/yt-note-checklist-concept.md` | concept | 新增 |
| `30_wiki/concepts/yt-note-ai-human-division.md` | concept | 新增 |
| `30_wiki/tools/yt-note-five-levels-training.md` | tool | 新增 |
| `30_wiki/tools/yt-note-live-field-skill.md` | tool | 新增 |
| `30_wiki/concepts/dk-yt-checklist-max-common-divisor.md` | dark-knowledge | 新增 |
| `30_wiki/concepts/yt-personal-checklist-notes.md` | tool | 更新（v1→v2） |
| `40_outputs/content/articles/从清单体到AI时代的认知重构——一堂Truman笔记法的三个核心洞察.md` | article | 新增 |

源素材：`00_inbox/一堂-AI时代清单体笔记-Truman-口述-01.txt` + `02.txt` + `Truman的个人成长五步法.png`

---

## 一、自动门禁

| 检查项 | 结果 |
|:---|:---:|
| V1.5 yt-note-checklist-concept | PASS（2 attacks / 3 dont-use / 4 triggers） |
| V1.5 yt-note-ai-human-division | PASS（2 attacks / 4 dont-use / 4 triggers） |
| V1.5 yt-note-five-levels-training | 未覆盖（tool 类型无校验） |
| V1.5 yt-note-live-field-skill | 未覆盖（tool 类型无校验） |
| Lint | 1 warning（dk 卡未入 index.md） |
| 源文件存在性 | 3/3 OK |
| 前置依赖卡存在性 | 全部 OK |
| 文章 wikilink | 6/6 有效 |
| Synthesis wikilink | 3 死链 |

---

## 二、技术债务

### P0（阻塞级——修复后才能 ship）

1. **Article 未注册到 KDO state.json**：`kdo validate` 报 `Unknown artifact id`。文章是手动创建的，跳过了 `kdo produce` → `validate` → `ship` 管线。validate 无法运行，ship 无法追踪交付。
   - **修复**：跑 `kdo produce content/article --topic "清单体AI认知重构"` 注册
2. **Article 缺 `source_refs`**：文章 frontmatter 无 source_refs 字段，溯源链在 article 层断裂。
   - **修复**：补 source_refs 指向两篇 Truman 口述稿

### P1（高优先级——ship 前修）

3. **3 个 Synthesis 死链**：

| 所在卡 | 死链目标 |
|:---|:---|
| yt-note-five-levels-training | `[[yt-tool-deliberate-practice-checklist]]` |
| yt-note-live-field-skill | `[[yt-tool-meeting-facilitation]]` |
| yt-note-live-field-skill | `[[yt-system-personal-knowledge-management]]` |

   卡内写了"如果存在这张卡片"作为免责，但仍是不负责任的 Synthesis——写卡时不验证目标存在。
   - **修复**：要么建目标卡，要么删无效引用

4. **`dk-yt-checklist-max-common-divisor` 未入 `30_wiki/index.md`**：lint 报 warning
5. **source_refs 文件名 typo**：`"请单体笔记"` → 应为 `"清单体笔记"`（与源文件名不一致）

### P2（低优先级——可延后）

6. **文章与 dk 卡内容重叠**：文章第四节"暗知识"与 `dk-yt-checklist-max-common-divisor` 主题相同，应做交叉引用或层次区分
7. **`yt-personal-checklist-notes` status 过期**：大幅更新（v1→v2，新增 AI 协作段/六阶模型/刻意练习四要素）后 status 仍为 `enriched`，应更新为 `draft` 或 `reviewed`

---

## 三、内容深度评估（待欧阳锋裁定）

### 做得好的

- 四卡形成完整 mini 知识体系（概念→分工→训练→现场），依赖链清晰合理
- 攻击者选择多样且高质量：8 位学者分布在认知心理学/复杂系统/AI伦理/教育学/社会学
- 每条 Critique 都有"对一堂笔记法的直接挑战"段落——不是贴标签，是真正对话
- 暗知识提取（剩余脑力、如厕大法、问题系统驱动）是 Truman 口述中的隐含技能点，老顽童做了显性化——这是真正的增量价值
- 文章有自己的叙事声音，不是卡片的拼凑

### 深度不足

| # | 问题 | 具体表现 |
|:--|:---|:---|
| 1 | **文章是"读后感"而非"知识合成"** | 第一人称体验（"听完后我的感觉是""这让我想到了"）占主导。读者知道作者感受深，但文章没有形成可复用的结论或操作框架 |
| 2 | **暗知识与概念卡重叠未桥接** | 文章第四节"暗知识"与 dk-yt-checklist-max-common-divisor 主题相同（最大公约数/AI分工），但没有相互引用或做层次区分。两张不同形态的知识产物覆盖了同一块内容，却各说各话 |
| 3 | **攻击者论证在文章中降级为"提及"** | 卡片 Critique 有真正的 Kahneman/Taleb 对话（"你说X，但他会问Y"）。文章写的是"Kahneman 在[[卡片]]中提醒我们"——引用卡片而非与攻击者对话。卡片层的深度没有传递到文章层 |
| 4 | **Synthesis 有免责式死链** | "如果存在这张卡片"是免责声明，不是负责任的 Synthesis。写卡时不验证目标存在，等于画空中楼阁。Synthesis 的质量标准应该是"你能为每个链接承担后果" |
| 5 | **文章缺少边界与反例** | 概念卡有 Critique（内部局限+外部攻击+不要用的场景），文章只有正面论证——清单体是怎么好的、为什么好。变成了一篇推广文。读者看完不知道"什么时候不该用清单体""什么人学了反而有害" |

### 裁定问题（请欧阳锋拍板）

1. 文章是按现有质量 ship，还是要求老顽童做深度改写？（改写方向：去掉读后感体，以 KDO 交叉验证视角重构，加入边界与反例）
2. 3 个 Synthesis 死链——是要求老顽童建目标卡，还是接受"预留扩展位"？
3. dk 卡与文章的内容重叠——是否需要老顽童做区分或合并？

---

## 四、KDO 基础设施暴露的系统性缺口（黄药师待建）

| # | 缺口 | 建议 |
|:--|:---|:---|
| I-1 | Tool 卡 v1.5 校验缺失 | 确认 v1.5 是否应覆盖 tool 类型。如是 design gap，定义 tool 卡 quality gate |
| I-2 | Synthesis wikilink 无自动死链检测 | lint 新增 `--check-synthesis-links` 规则 |
| I-3 | Article 可绕过 produce 管线创建 | lint 检查 `40_outputs/` 下文件是否有 state.json 条目 |
| I-4 | 暗知识卡无标准结构校验 | 定义 dk卡 frontmatter 必填字段 + 结构完整性规则 |
| I-5 | source_refs 无 fuzzy match | 扫描 source_refs 与文件系统文件名做相似度比对，flag 可能的 typo |

---

## 五、总体评价

**内容质量**：A-（攻击者论证 A，暗知识提取 A，知识体系 A-，文章深度 B-）  
**管线遵从度**：C（跳过 produce→validate→ship，溯源链断裂）  
**投产建议**：P0 修完后可 ship，深度问题根据欧阳锋裁定决定是否在 ship 前修
