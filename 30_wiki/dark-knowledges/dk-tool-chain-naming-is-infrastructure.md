---

id: dk-tool-chain-naming-is-infrastructure
title: 命名不规范会让整条工具链"失明"
type: dark-knowledge
dark_knowledge_type: cross-domain-pattern
status: enriched
domain:
- master
- kdo
- yitang
source_person: KDO 团队复盘
source_context: 第26-27节精修中反复出现：source ID、文件名、正则边界、YAML 命名导致解析失败
source_refs: []
related:
  - '[[dk-small-format-error-cascades-to-system-failure]]'
  - '[[dk-p18-yaml-parser]]'
  - '[[dk-p19-quote-yaml]]'
  - '[[proposal-yaml-frontmatter-standardization]]'
  - '[[dk-f13-handwritten-yaml-parser]]'
  - '[[dk-f10-broken-source-refs]]'
  - '[[dk-f8-phony-wikilink]]'
  - '[[dk-p11-regex-cutoff]]'
  - '[[dk-p19-quote-yaml]]'
  - '[[dk-f13-handwritten-yaml-parser]]'
bridges_to:
- dk-f10-broken-source-refs
- dk-f8-phony-wikilink
- dk-p11-regex-cutoff
- dk-p19-quote-yaml
author: 老顽童
reviewed_by: 欧阳锋
review_date: '2026-06-19'
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: 新增 source 文件后，gate 报"source ID 未注册"，但文件确实存在
  framework_lens: 命名超出正则
  follow_up_question: 这个命名能否被当前工具链的正则/解析器唯一识别？如果不能，是否需要改名或改规则？
- signal: 批量脚本对一部分卡片有效，对另一部分 silently 失败
  framework_lens: 命名边界不一致
  follow_up_question: 失效卡片的命名是否与有效卡片存在字符长度、分隔符、编码差异？
- signal: 链接/引用在人工阅读时正确，但机器解析时 dangling 或截断
  framework_lens: 人眼与机器解析不一致
  follow_up_question: 是否有别名、特殊字符、过长 ID 导致解析器只能识别前半段？
---# 命名不规范会让整条工具链"失明"

## 原始表述 / 核心洞察

在第 26、27 节精修中，同一类问题反复出现：

- F-10：`source_refs` 里的文件名命名不符合 `src_YYYYMMDD_8hex` 规范，`source_id_map` 只能识别前半段，溯源链断裂。
- F-8：phony wikilink 检测规则因为人眼与机器对"看起来像链接"的判断不一致，导致误报/漏报。
- P-11：regex 在 `###` 处截断，本质上是因为没有为正则划定严格的命名/结构边界。
- P-19：中文引号被 YAML 解析器误认为是字符串定界符，说明命名/符号系统与解析器预期冲突。
- F-13：手写 YAML 解析器无法处理嵌套结构，说明开发者假设所有字段都是"简单 key-value"，没有为复杂命名/结构预留空间。

**核心洞察**：命名不是"怎么好读怎么写"的装饰，而是工具链能够识别、索引、校验、链接的基础设施。一旦命名超出正则、解析器、链接器的能力边界，整条工具链就会"失明"——它看不到完整信息，只能看到前半段、错误段，或者根本看不到。人眼觉得对，机器已经错了。

## 使用场景

- 新增 source ID、文件名、卡片 id、锚点、字段名时。
- 设计正则、解析器、validator、链接检查器时。
- 发现批量脚本对部分数据失效，但原因不明时。
- 从旧系统迁移数据到新系统时。
- 制定团队命名规范时。
- 评估"这个命名能不能被机器处理"时使用。

## 操作方法

1. **先定义解析规则，再命名**：在创建新的 id/文件名/字段前，先写出能匹配它的正则。如果正则写不出来，说明命名不规范。
2. **强制通过 gate/正则验证**：新增命名必须先跑一次工具链检查，确认能被唯一识别。
3. **避免使用解析器的保留字符**：
   - YAML：`"`、`:`、`#`、`*`、`&`、`|`、`>` 等在未加引号时有特殊含义。
   - 正则：`.`、`*`、`+`、`?`、`[`、`]`、`(`、`)` 等需要转义。
   - 路径/ID：避免空格、中文全角符号、连续下划线、过长无意义字符串。
4. **保持命名空间一致性**：卡片 id、文件名、source id、wikilink 目标使用同一套字符集和分隔规则。
5. **为人眼可读性使用元数据，而不是命名**：
   - 不要把标题/描述塞进 id 或文件名；id 保持简短规范，标题放在 frontmatter/body。
   - 例如 `src_20260618_a1b2c3d4.md` + `title: 鑫港湾周会 2026-06-18`，而不是 `src_20260618_xingangwan-weekly-meeting-20260618.md`。
6. **为旧数据设置兼容层**：如果历史命名不规范，集中一次迁移/重命名，而不是让解析器不断打补丁。

## 适用边界

- **适用于**：任何依赖机器解析命名的系统（知识库、数据管道、CI/CD、API、文件系统）。
- **不适用于**：纯人工阅读、不会被脚本处理的文档。
- **不要为了规范而牺牲语义**：id 可以无意义，但标题、注释、相关字段必须清晰。
- **警惕"临时命名"**：很多命名一开始说是临时的，最后成了事实标准。

## 常见失败模式

| 失败模式 | 典型症状 | 根因 | 修复方法 |
|:---|:---|:---|:---|
| **ID 过长且含描述** | source_id_map 只能识别前半段 | 命名超出正则长度/字符预期 | id 与标题分离，id 简短规范 |
| **使用保留字符** | YAML 解析失败或正则匹配错误 | 命名中包含解析器保留字符 | 转义、加引号、或避免使用 |
| **人眼可读但机器读错** | 链接看起来对但 dangling | 别名、特殊符号、编码差异 | 用 gate 验证机器视角 |
| **新旧命名混用** | 批量脚本对部分数据失效 | 没有统一迁移，兼容补丁太多 | 集中迁移，统一命名空间 |
| **假设所有字段都是简单字符串** | 手写解析器在嵌套结构上失败 | 命名/结构假设过于简单 | 用成熟库，不要手写解析器 |

## 为什么值钱

- **把命名从"风格问题"提升为"基础设施问题"**：命名错误会让整个工具链失效，而不是仅仅不好看。
- **减少批量事故的根因**：大量"脚本突然失效"的故障，根因是新增了一个不规范命名。
- **降低新人 onboarding 成本**：清晰的命名规范让新成员知道"怎么写才能被系统识别"。
- **与知识管理强相关**：卡片 id、source id、wikilink 是知识库的地址系统，地址系统不稳定，知识就找不到。

## 与其他知识的关联

- [[dk-f10-broken-source-refs]] — source 命名不规范导致 source_id_map 失明。
- [[dk-f8-phony-wikilink]] — 链接检测因为人眼与机器判断不一致而失效。
- [[dk-p11-regex-cutoff]] — 正则没有为正则边界预留空间，导致截断。
- [[dk-p19-quote-yaml]] — 中文引号等符号与 YAML 解析器冲突。
- [[dk-f13-handwritten-yaml-parser]] — 手写解析器假设所有字段都是简单 key-value，无法处理复杂结构。
