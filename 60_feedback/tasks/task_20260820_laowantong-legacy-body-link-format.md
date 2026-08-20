---
id: 386
assignee: hermes
status: reviewed
title: 全库 10 处历史遗留 body 关联节格式清理（#384 R2 全库复扫另立项）
priority: P3
dependency: []
updated_at: '2026-08-20T02:47:15.093656+00:00'
reviewed_by: 欧阳锋
review_date: '2026-08-20'
grade: A
---

# #386 全库 10 处历史遗留 body 关联节格式清理

## 来源

#384 R2 修复时全库复扫发现：**10 处历史遗留**（非 #384 引入）——body"与其他知识的关联"节内存在 frontmatter 风格行：行首 `- '[[`（单引号 wikilink），与 body 关联节法定格式（`- \`dk-xxx\`：说明`）不一致。已知涉及 yt-five-step-method / yt-personal-ipo-learning 等 yt-* 系列。

## 任务目标

全库 body 关联节 `- '[[` 前缀行归零（历史遗留部分），格式统一为反引号+说明。

## 执行范围

1. 全库扫描：body（`---` 分隔符后）行首匹配 `- '[[` 的行，产出清单（预期 ≈10 处，以实扫为准）
2. 逐处转 body 法定格式：`- \`卡名\`：一句说明`（说明从上下文推断，推断不出就标"关联待补说明"）
3. 只改格式不改语义，不删除任何关联

## 边界

- 批量三问（dry-run 预览清单+范围声明+非空不覆盖）
- 只动 body 关联节的格式行，frontmatter 零改动，正文其他段落零改动
- 修复后**全量复扫**确认归零（铁律：修复了≠清干净了，#384 三轮教训）
- 改完逐卡 `kdo pre-submit` 0 ERROR；diff 贴执行报告
- 欧阳锋随下批 spot-check 复终审

## 内容价值判断（PROTOCOL §7 合规声明)

- 仅格式转换，无删除/移动，关联关系全保留

## 验收标准

1. 全库 body `- '[[` 前缀行 = 0
2. 转换后每行有句说明或"关联待补说明"标注
3. pre-submit 0 ERROR，diff 只动格式行

## 交付

1. 扫描清单 + diff + pre-submit 输出
2. 送欧阳锋终审（随下批 spot-check）

---

## 执行报告（2026-08-20 老顽童 hermes 实例）

### 完成概要
全库 10 处历史遗留 body 关联节 frontmatter 风格行清理完成（#384 R2 全库复扫另立项），**全库 body `- '[[` 前缀行归零**。

### 扫描清单（dry-run 10 处 → 全部转换）
| # | 文件 | 原行 → 新行 |
|:--|:--|:--|
| 1 | case-five-step-fake-vs-real-barriers | `- '[[framework-一堂五步法-壁垒]]'` → `- \`framework-一堂五步法-壁垒\`：五步法壁垒环节（案例关联）` |
| 2 | yt-five-step-method | `- '[[framework-一堂五步法]]'` → `- \`framework-一堂五步法\`：五步法总框架` |
| 3 | yt-model-personal-pitch-toolkit | `- '[[framework-一堂-个人表达力]]'` → `- \`framework-一堂-个人表达力\`：个人表达力总框架` |
| 4 | yt-model-questioning-practice-canvas | `- '[[framework-个人学习方法-科学提问]]'` → `- \`framework-个人学习方法-科学提问\`：科学提问方法` |
| 5 | yt-personal-ipo-learning | `- '[[framework-个人学习方法总框架]]'` → `- \`framework-个人学习方法总框架\`：个人学习方法总纲` |
| 6 | yt-personal-knowledge-extraction | `- '[[framework-个人学习方法-知识萃取]]'` → `- \`framework-个人学习方法-知识萃取\`：知识萃取方法` |
| 7 | yt-personal-scientific-expression | `- '[[framework-一堂-表达力火箭模型]]'` → `- \`framework-一堂-表达力火箭模型\`：表达力火箭模型` |
| 8 | yt-personal-thinking-models | `- '[[framework-个人学习方法-思维模型]]'` → `- \`framework-个人学习方法-思维模型\`：思维模型方法` |
| 9 | framework-一堂五步法-泛产品设计 | `- '[[framework-一堂五步法]]'` → `- \`framework-一堂五步法\`：五步法总框架` |
| 10 | yt-five-step-method-complete | `- '[[framework-一堂五步法]]'` → `- \`framework-一堂五步法\`：五步法总框架` |

### 边界合规
- 只改 body 关联节格式行，frontmatter 零改动，正文其他段落零改动，关联关系全保留
- 批量三问：dry-run 清单 ✅ / 范围=10 行格式转换 ✅ / 非空不覆盖 ✅

### 验证
- **全量复扫全库：body `- '[[` 前缀行 = 0**（E017 铁律：修复了≠清干净了）
- pre-submit 8/10 PASS；**2 个 ERROR 为历史遗留**（非本任务引入）：yt-model-questioning-practice-canvas / yt-personal-thinking-models 缺 updated_at——任务边界"frontmatter 零改动"故未补，建议另立项（同 #385 模式）

### 待欧阳锋
- 随下一批 spot-check 复终审
- 历史遗留建议另立项：2 张 yt-* 卡补 updated_at

---

## 欧阳锋终审（2026-08-20 · 独立全库复扫）

**裁定：PASS A。**

**O3 独立验证**：
- **全库复扫（30_wiki 全部 md）：body `- '[[` 前缀行残留 0**——归零达成（与报告一致，非采信）✓
- 转换抽查（case-five-step-fake-vs-real-barriers）：`- \`framework-一堂五步法-壁垒\`：五步法壁垒环节（案例关联）`——反引号格式 + 说明完整，关联保留 ✓
- 边界：frontmatter 零改动 / 正文其他段落零改动 / 10 行转换清单 dry-run 留痕 ✓

**纪律加分**：E017 铁律"修复了≠清干净了"主动执行（全量复扫而非点名卡）——#384 三轮教训的直接吸收；2 个历史遗留（yt 卡缺 updated_at）按边界不动、建议另立项（同 #385 模式）✓
