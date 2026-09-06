---
id: task_20260906_duanwangye-datapack-weblogin
title: "DataPack 试点二：网络登录内容样本库（解析对照/反爬失败案例/字段抽取金标准，段王爷整理弹药）"
seq: 661
status: reviewed
assignee: duanwangye
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 老朱 09-06 点名（段王爷把处理网络登录内容的工作流整理成 datapack）
reviewer: 欧阳锋
instance: duanwangye
updated_at: '2026-09-06T05:29:58.520322+00:00'
evidence: 40_outputs/capabilities/datapacks/duanwangye-weblogin-samples/README.md
reviewed_by: 欧阳锋
review_date: '2026-09-06'
grade: A-
---

# #661 DataPack 试点二：登录内容样本库（段王爷）

## 规格
`40_outputs/capabilities/datapacks/duanwangye-weblogin-samples/`（规范见 datapacks/README）：
1. **金标准**：≥5 组典型登录态页面的「原始内容→结构化解析输出」对照
2. **踩坑实录**：反爬/验证码/登录失效/编码问题的失败案例与处置
3. **对照数据**：字段抽取判定依据（哪些字段必须保留/哪些噪声可弃）
4. **使用说明**：适用问题/挂载时机/更新日期

## 边界
- 真实案例不编造；敏感凭据脱敏；你今天早上的 hermes 建议书经验可直接入库
- 隐私面：涉及个人账号内容一律脱敏后入库

## 执行报告（段王爷 2026-09-06）

**交付物**
40_outputs/capabilities/datapacks/duanwangye-weblogin-samples/README.md（四要素总入口+使用说明+脱敏红线）；40_outputs/capabilities/datapacks/duanwangye-weblogin-samples/gold-standard.md（8 组金标准对照，超额完成 ≥5）；40_outputs/capabilities/datapacks/duanwangye-weblogin-samples/pitfalls.md（14 条踩坑实录，全带锚点）；40_outputs/capabilities/datapacks/duanwangye-weblogin-samples/field-extraction.md（字段三分类判定表+质量四级判定）。

**完成内容**
①金标准 8 组：公众号 HTML→MD、头条文章/视频 API→MD、抖音 CDP cookie→逐字稿、视频号 sph→逐字稿、微信 SQLCipher DB→结构化 MD、工具 profile 凭据传递（今早 hermes 建议书作首件）、逐字稿质量分级（🟢🟡🔴 实锤错词对照）。全部为库内真实产物，零编造。②踩坑 14 条：cookie 不全拒播/月级过期/DB 解密失败/WAL 未合并/IncompleteRead 限流/图片页 29h 空转（#608）/900s 固定超时/MITM 代理/加密视频 Invalid data/追踪参数穿透去重/env 凭据失效/exit 0 假成功/tiny 模型错词。③对照数据：保留 11 项/可弃 7 项/禁止入库 6 类 + 质量四级判定依据。④行为宪法落实：全包关键判断三级标注；负向判词附存在性核查（验证码/滑块类风控零命中实证 grep exit=1；cookies.txt 不在库已显式标注而非假断言）。

**验证**
YAML frontmatter 4/4 可解析；脱敏红线扫描（MS4wLjA/wxid_/cookie=/token=/passphrase）仅命中掩码示例与判定规则本身，零真实凭据；锚点自动化核验 21 个全路径锚全存在 + 库外 decrypt 脚本 2 个存在 + 简写引用映射核实；脚本默认路径引用（cookies.txt）已带"当前不在库"的显式存在性核查。

**未做项/边界**
不含工作流步骤（步骤归 Skill《登录内容处理工作流》，本包只装陈述性弹药）；不含 channel/资产台账与 infrastructure-inventory 登记（对齐稿 §四.5 归王语嫣线）；媒体文件入库边界未触碰（mp4 留在采集目录，本包零复制）；"vod 直链存活期"未实测（标注【推断】）；微信反爬策略时效性为原厂书面承认"随时可能变化"。

**需要谁动作**
欧阳锋终审（reviewer）。王语嫣：DataPack 台账+infrastructure-inventory 登记是否纳入其线（对齐稿 §四.5）；老顽童：#658 T1 skill 壳如需引用本包，挂载点见 README「使用说明」。


## 终审记录（欧阳锋 2026-09-06 13:47）

**verdict**：PASS
**grade**：A-
**methodology_version**：v2.3
**blocking**：无

**O0 溯源自检**：通读 README / gold-standard / field-extraction / pitfalls 四文件；抽查 12 处来源锚/产物/脚本全部存在；对全包跑敏感特征扫描（cookie=/token=/passphrase/wxid_/MS4wLjA/hy_token），确认零真实凭据入包。

**实证核对（四要素 + 来源锚 + 脱敏重点核）**：
- 四要素齐：①金标准 8 组（≥5）✅ ②踩坑 14 例（≥5）✅ ③对照数据（保留 11/可弃 7/禁止 6 类 + 质量四级）✅ ④使用说明 + 脱敏红线 ✅
- 敏感脱敏【实证】：全包敏感特征扫描仅命中掩码示例（`share_token=***` 等）与判定规则本身，零真实 cookie/token/passphrase/wxid 值；`cookies.txt`「当前不在库」已显式标注（find 全采集目录 cookies*.txt 零命中），非假断言
- 12 处产物/脚本/建议书锚全存在（含 5 个真实产物文件、wechat_link_monitor.py、douyin_cookie_extract.py、guide、skill、diag 建议书、duplicates-archive）【实证】

**发现问题**：
- 🔵 gold-standard.md 标题写「7 组」，正文实为 8 组（第 8 组为工具凭据镜像案例）——标题计数与执行报告「8 组」不一致【实证：frontmatter title vs 样本 1-8】
- 🔵 datapacks 索引 README 仍留 `duanwangye-登录内容样本/`（待产）陈旧条目，与实际交付目录 `duanwangye-weblogin-samples/`（已产、pending_review→reviewed）不符——去向：待王语嫣（infrastructure/index 登记归其线，#661 未做项已声明归王语嫣线）【实证：40_outputs/capabilities/datapacks/README.md 在库表】

**审查结论**：登录内容样本库四要素齐全、来源锚可复现、敏感信息脱敏重点核验通过（零真实凭据入包）、反爬风控面诚实声明（未遇验证码/滑块类主动风控，非假装有），达到 DataPack 试点标准。

**residual_risks**：①vod 直链存活期未实测已标【推断】；②微信反爬策略时效为原厂书面承认「随时可能变化」；③whisper tiny 转写稿定级 🟡 的「错词应为」属上下文推断，引用专名前须回原音视频。

**五维评分**：溯源完整 24/25、逻辑骨架 23/25、暗知识密度 19/20、可操作性 14/15、表达质量 13/15（标题计数小瑕），合计 93/100 → A-
