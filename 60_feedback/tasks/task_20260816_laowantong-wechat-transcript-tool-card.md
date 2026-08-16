---
id: task_20260816_laowantong-wechat-transcript-tool-card
assignee: hermes
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-17
priority: P1
wsjf: 3.0
created_at: 2026-08-16
updated_at: '2026-08-16T15:07:30.665153+00:00'
source: R 型 Partner 首战资产报告（欧阳锋终审 A 级零编造）+ 欧阳锋转卡建议（2026-08-16）；用户方向确认
related: null
---

# 视频号→逐字稿自动化工作流 tool 卡生产（#349）

## 背景

R 型爆炸式调研 Partner 首战（视频号→逐字稿自动化工作流，欧阳锋发起）产出资产报告 `00_inbox/视频号逐字稿调研/视频号逐字稿自动化工作流-爆炸式建模.md`——欧阳锋 O0 溯源抽查 4 项全过（star 数×2/blog.md 原文/config.yaml 规格），**零编造 A 级**。建议转 tool 卡入库。

## 任务

**素材已资产化（报告即终端资产），跳过诊断，直接生产**：

1. **tool 卡主卡**：视频号→逐字稿自动化工作流——四环节×双路线矩阵（下载 MITM/API 解析 × 转写本地/商业 × 知识化模板/三件套 × 编排一键/Skill/手动）+ 工具全景（12 有效工具 + 3 生态位）+ 反爬情报（Referer 必带/证书坑/公共 Worker 失效）+ DataPack
2. **verified 分级保留**：实测/引用/推演三档标注不得抹平（报告 §6/§10 为依据）；未实证项（BibiGPT 视频号/秒转工具箱/sph 404/商业服务）如实保留
3. **时效标注**：工具类知识 ≤6 个月时效——frontmatter 加 `time_valid: 2027-02` 复核提醒（2026-08 锚定）
4. （可选，视内容密度）dk 卡：免费公共解析有保质期（Worker 失效归纳）——若并入 tool 卡则不出

## 依赖

- 资产报告（素材）✅ 已就位 + 欧阳锋抽查 ✅
- 引用锚点：楚门口述 L2612/L2642（素材章节 §1.1）

## 验收标准

- tool 卡落盘（四环节矩阵/工具全景/反爬/DataPack 四要件）
- 数据与报告一致（star 数/规格/链接——O0 核对源报告）
- verified 分级 + 时效标注在卡
- 未实证清单如实保留（不冒充已验证）
- 欧阳锋终审

## 边界

- 单角色单任务（E026）：老顽童生产，欧阳锋终审（王语嫣编排）
- 卡化只承载"案头调研知识"（引用级可信），**不做 KDO 自身验证声明**——collect_wechat.py 接入验证属欧阳锋管线任务，验证后如需 case 卡另立
- Cubox 模板迁移（报告 §11）不入本任务（楚门场景，另议）

## 回滚

删除卡 + 索引回退（kdo index 增量）

## 执行门禁

✅ 已授权（欧阳锋建议 + 用户方向确认）

## 执行记录（2026-08-16 老顽童）

- **产出**：`30_wiki/tools/tool-wechat-transcript-automation-workflow.md`（1 张 tool 卡）
- **pre-submit**：✅ PASS 一次通过（YAML/WIKILINK/DOMAIN/OUTLINK/ALIASES/POSITION/SOURCE_REACHABILITY 全 0 issues）
- **related**：8 条 / 死链 0 / 跨域 ≥2（case-cross-xingangwan-pharma + bridge-how-to-know-person-to-business 实判；verify-related.py 报 cross=8 为脚本对多行数组 domain 旧卡解析为空的假阳性）
- **verified 分级**：实测（star 数/404/工具存在）+ 引用（README 原文）+ 推演（Worker 失效→自持）三档保留；未实证 4 项如实列卡
- **时效**：frontmatter `time_valid: 2027-02` 已加
- **边界遵守**：只承载案头调研知识，collect_wechat.py 接入验证未并入
- **队列**：claimed-hermes → pending_review（2026-08-16）

## 终审记录（2026-08-17 欧阳锋）

**verdict: PASS A- · methodology v2.3**

O0 溯源 + O3 独立验证：
1. **转卡保真**：verified 分级（实测/引用/推演）保留不抹平 ✅；未实证 4 项（BibiGPT/秒转工具箱/sph 404/商业服务）诚实列卡 ✅；time_valid: 2027-02 时效标注 ✅
2. **source_refs 溯源链完整**：资产报告（00_inbox/视频号逐字稿调研/）+ 楚门口述——R 型报告我已抽查零编造（star 27/119、261/955/13 全命中），卡与报告一致
3. **related 8 条死链 0** ✅（全部真实存在）；跨域 ≥2 达标（case-cross-xingangwan-pharma 医药案例 + bridge-how-to-know-person 人域桥接——verify-related.py 报 8 是 parse_domain 假阳性，实判达标）
4. **结构**：四环节×双路线矩阵 + 12 工具全景 + 反爬情报 + DataPack 四要件全含

**覆盖事故裁定**：老顽童 write_file 覆盖 2026-08-16-full.md（复盘文件）——①事故性质：复盘文件非生产资产，影响有限；②如实上报无隐瞒 ✅；③三补救（盲点自检记录/重写 A 级复盘/patch pre-submit-self-check 防复发）充分 ✅。**裁定：认可处理，不追责，不要求追回**（session-archives 已有当日复盘存档）。防复发 patch 是正确机制化——"复盘类文件宁可 append"。

**结论**：PASS A-，视频号→逐字稿工作流 tool 卡入库。KDO 首张由 R 型 Partner 调研产出的卡，资产报告→转卡链路走通。
