---
id: task_20260906_duanwangye-datapack-weblogin
title: "DataPack 试点二：网络登录内容样本库（解析对照/反爬失败案例/字段抽取金标准，段王爷整理弹药）"
seq: 661
status: pending_review
assignee: duanwangye
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 老朱 09-06 点名（段王爷把处理网络登录内容的工作流整理成 datapack）
reviewer: 欧阳锋
instance: duanwangye
updated_at: '2026-09-06T04:54:46.778598+00:00'
evidence: 40_outputs/capabilities/datapacks/duanwangye-weblogin-samples/README.md
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
`40_outputs/capabilities/datapacks/duanwangye-weblogin-samples/` 四文件：`README.md`（四要素总入口+使用说明+脱敏红线）/ `gold-standard.md`（8 组金标准对照，超额完成 ≥5）/ `pitfalls.md`（14 条踩坑实录，全带锚点）/ `field-extraction.md`（字段三分类判定表+质量四级判定）。

**完成内容**
①金标准 8 组：公众号 HTML→MD、头条文章/视频 API→MD、抖音 CDP cookie→逐字稿、视频号 sph→逐字稿、微信 SQLCipher DB→结构化 MD、工具 profile 凭据传递（今早 hermes 建议书作首件）、逐字稿质量分级（🟢🟡🔴 实锤错词对照）。全部为库内真实产物，零编造。②踩坑 14 条：cookie 不全拒播/月级过期/DB 解密失败/WAL 未合并/IncompleteRead 限流/图片页 29h 空转（#608）/900s 固定超时/MITM 代理/加密视频 Invalid data/追踪参数穿透去重/env 凭据失效/exit 0 假成功/tiny 模型错词。③对照数据：保留 11 项/可弃 7 项/禁止入库 6 类 + 质量四级判定依据。④行为宪法落实：全包关键判断三级标注；负向判词附存在性核查（验证码/滑块类风控零命中实证 grep exit=1；cookies.txt 不在库已显式标注而非假断言）。

**验证**
YAML frontmatter 4/4 可解析；脱敏红线扫描（MS4wLjA/wxid_/cookie=/token=/passphrase）仅命中掩码示例与判定规则本身，零真实凭据；锚点自动化核验 21 个全路径锚全存在 + 库外 decrypt 脚本 2 个存在 + 简写引用映射核实；脚本默认路径引用（cookies.txt）已带"当前不在库"的显式存在性核查。

**边界（未做/不含）**
不含工作流步骤（步骤归 Skill《登录内容处理工作流》，本包只装陈述性弹药）；不含 channel/资产台账与 infrastructure-inventory 登记（对齐稿 §四.5 归王语嫣线）；媒体文件入库边界未触碰（mp4 留在采集目录，本包零复制）；"vod 直链存活期"未实测（标注【推断】）；微信反爬策略时效性为原厂书面承认"随时可能变化"。

**需要谁动作**
欧阳锋终审（reviewer）。王语嫣：DataPack 台账+infrastructure-inventory 登记是否纳入其线（对齐稿 §四.5）；老顽童：#658 T1 skill 壳如需引用本包，挂载点见 README「使用说明」。
