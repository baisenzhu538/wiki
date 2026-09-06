---
id: task_20260906_duanwangye-datapack-weblogin
title: "DataPack 试点二：网络登录内容样本库（解析对照/反爬失败案例/字段抽取金标准，段王爷整理弹药）"
seq: 661
status: queued
assignee: duanwangye
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 老朱 09-06 点名（段王爷把处理网络登录内容的工作流整理成 datapack）
reviewer: 欧阳锋
instance: duanwangye
updated_at: '2026-09-06T12:50:00+08:00'
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
