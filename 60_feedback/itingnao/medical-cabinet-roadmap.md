# 药柜主题长程整理与纠偏路线图

## 项目定位

药柜（智能药柜 / 智慧药房 / 诊所药柜）是一个**长程、重线下调研、强合规敏感**的主题。当前知识库中药柜相关内容分散在多个草稿、诊断报告、纠偏文件和原始录音中，存在数据矛盾、合规夸大、招商口径污染等问题。

**本文件目标**：建立系统性的整理与纠偏框架，明确优先级、责任边界和线下验证清单，避免知识库被推销叙事污染。

---

## 一、现有资料盘点

### 1.1 已进入 `30_wiki/` 的知识卡
- `30_wiki/concepts/smart-medicine-cabinet-distribution.md`：智能药柜/智慧药房分销业态洞察（置信度 0.82）

### 1.2 `60_feedback/` 中的诊断报告
- `itingnao-executive-summary.md`：72 条药柜/医疗录音的整体诊断
- `itingnao-deep-dive-business-model.md`：商业模式诊断
- `itingnao-deep-dive-compliance.md`：合规诊断（重点：推销方"轻合规"倾向）
- `itingnao-deep-dive-supply-chain.md`：供应链/技术诊断
- `itingnao-deep-dive-corporate-risk.md`：公司/股权/资金风险
- `itingnao-deep-dive-platforms.md`：平台合作诊断
- `itingnao-deep-dive-digital-pharmacy.md`：数字药房/慢病生态诊断
- `medical-contamination-in-nonmed-report.md`：12 条被污染录音清单

### 1.3 已生成基础卡（`60_feedback/itingnao/medical-cabinet-longterm/`）

A 阶段共生成 **14 张基础卡**：

**第一阶段：止血型纠偏卡（已完成）**
- `concept-medical-cabinet-fraud-detection.md`：招商骗局识别
- `concept-medical-cabinet-compliance-redlines.md`：合规红线
- `concept-pitch-vs-regulation-misalignment.md`：推销口径 vs 监管口径对照

**第二阶段：基础事实卡（已完成）**
- `fact-national-policy-redlines.md`：48 号公告红线
- `concept-regional-policy-map.md`：全国政策三档分化
- `method-single-point-financial-model.md`：单点财务模型
- `fact-o2o-cost-structure.md`：O2O 平台费用结构

**第三阶段：深度洞察卡（已完成）**
- `insight-failure-patterns-case-library.md`：失败模式案例库
- `concept-clinic-cabinet-legal-relationships.md`：诊所+药柜法律关系
- `method-medical-cabinet-site-selection.md`：选址框架
- `insight-international-medical-cabinet-experience.md`：国际经验对照
- `insight-consumer-willingness-medical-cabinet.md`：消费者支付意愿
- `insight-giants-why-not-clinic-cabinet.md`：巨头为何不布局诊所药柜

**第四阶段：专项补充卡（部分完成）**
- `concept-medical-cabinet-hardware-technology.md`：硬件技术专题
- 待完成：`medical-shortvideo-compliance-for-clinics.md`

### 1.4 纠偏/深挖文件（`60_feedback/corrections/`）
- 约 20+ 份 `corr_20260613_smart-medicine-cabinet-iteration-*` 文件
- `corr_20260613_smart-medicine-cabinet-knowledge-gaps.md`：知识缺口与补卡建议
- `corr_20260613_smart-medicine-cabinet-research-gaps-and-validation-needs.md`：研究缺口与验证需求

### 1.5 外部调研资料
- `00_inbox/山西智慧药房新政深度调研报告.md`
- `00_inbox/doc_d85dd855150f_智能药柜-招商合作沟通_智能优化.txt`

### 1.6 被污染主题的 kcard 草稿
- `kcard-supply-chain-beverage-draft.md`（录音 6269640：药柜硬件开发）
- `kcard-finance-legal-business-draft.md`（录音 1483043：药店客户/药柜设备）
- `kcard-ai-methodology-tools-draft.md`（录音 1486162：智慧城市医疗）
- `kcard-industry-ai-cases-draft.md`（录音 2694971：药店软硬运营结合）
- `kcard-other-draft.md`（录音 6272697：药品恒温恒湿）
- `kcard-product-business-draft.md`（录音 4231073：疑似药柜设备）
- `kcard-yitang-methodology-draft.md`（录音 6311449：中医诊后管理）

---

## 二、已识别关键错误与矛盾（纠偏清单）

### 2.1 明显数据错误
| 问题 | 位置/来源 | 说明 | 纠偏状态 |
|------|----------|------|---------|
| "300 万 SKU" | 录音 1428540 | 与 800 SKU 目标、336 品规容量严重冲突，疑似转写/纪要笔误 | 待复核原文 |
| "泉州万达 24h 店月销 2000 万元" | 未注明来源 | 远超医药 O2O 单店产能常识，单位可能误读 | 待复核原文 |

### 2.2 核心逻辑矛盾
| 矛盾点 | A 说法 | B 说法 | 判断 |
|--------|--------|--------|------|
| 处方流转平台是否打通 | 已与省级/地市级医保中心电子处方流转平台对接 | 当前无大医院处方集中流转平台，只能手动拍照/扫码上传 | B 更可信，A 是规划/推销口径 |
| 医保支付方式 | 刷脸调用医保模块完成医保结算 | 主推原研药/进口药，不走医保报销 | 两种叙事无法同时成立 |
| 系统部署方式 | SaaS 云端部署 | 医保专网无法访问外网，必须本地化部署 | 存在架构张力，需两套方案 |
| 6 月 1 日上线性质 | 深圳龙岗区试点上线，10 台设备对外运行 | 6 月 1 日是内测上线，不能对外 | B 更可信 |

### 2.3 合规红线冲突
- **数字人药师审方**：涉嫌虚假审方/挂证。
- **"名义有人实际无人"**：冲击 GSP 和医保定点协议。
- **"先拿证照再分租"**：涉嫌经营场所与许可证不一致。
- **"大院处方、小院续方"**：小诊所医生"复制原方改签名"，违反《处方管理办法》。
- **医生药品提成 1%–5%**：涉嫌商业贿赂。
- **"药师考试包过/代考"**：涉嫌刑事违法。
- **社康药房承包/利润返点**：违反 2018 年国家卫健委药房托管禁令。

### 2.4 商业/战略矛盾
- 设备价格区间：3.5 万小机器 vs 10 万大机器，产品定位不清。
- 盈利模式：ToB 卖设备 vs ToC/加盟商运营，资源禀赋不同。
- 扩张速度：一年 500–1000 家 vs 先跑单店模型。
- 2027 目标 80 家药店 + 500 家诊所，但可联系客户仅四五十家。

### 2.5 平台合作口径冲突
- **阿里健康**：
  - 版本 A：设备投放 + 线上托管 + 不碰药店线下
  - 版本 B：药店必须用阿里健康的药 + 不打通 ERP
  - 判断：二者在商业逻辑和合规上无法自洽，需向阿里健康官方确认。

### 2.6 技术/供应链风险
- 4 月 20 日仍在解决机械结构问题，却要求 5 月 20 日样机、6 月上线。
- 断电状态丢失：无备用电源时无法保留出货状态。
- Windows 版/医保版本成熟度存疑。

### 2.7 公司/资金风险
- 资金链极度紧张，社保难缴、供应商欠款。
- 新港湾投资 100 万/70% 股权，投资款处理、股权代持存在法律和税务风险。
- 原公司存在股东诉讼、银行错账。

---

## 三、需要线下调研补充的知识点

### P0（最高优先级，必须线下验证）
1. **院外药柜真实日均销售额与回本周期**：公开网络无运营商真实数据。
2. **广东/广州诊所药柜医保个账支付口径**：需电话咨询医保局。
3. **设备真实成本曲线**：3.5 万元以下小机器的 BOM 清单、交付周期、故障率、售后成本。
4. **单点真实经营数据**：连续 3–6 个月记录单店/单机日均订单、客单价、毛利率、复购率、夜间订单占比、退货率、运维成本。
5. **200 台订单书面材料**：PO、客户名称、付款条件、交付周期。
6. **新港湾投资协议、资金/股权法律审查**。

### P1（重要补充）
1. 诊所+药柜真实落地规模与分成数据。
2. 消费者对智能药柜 specifically 的支付意愿。
3. 小型药柜运营商与连锁药店采购价差。
4. 院外药柜故障率/维修成本/实际寿命。
5. 陕西/成都/重庆/湖北政策最终状态。
6. 阿里健康官方合作方案与合同条款。
7. 深圳龙岗 6 月 1 日试点运行数据。

### P2（长期建设）
1. 医疗短视频在诊所场景的真实转化率。
2. 校园/社区/医院/交通枢纽等场景实地运营细节。
3. 设备供应商（艾隆科技、健麾信息、巨米智能等）真实产品和报价。
4. 冷链配送最后一公里成本细节。

---

## 四、知识卡整理优先级

### 第一阶段：止血型纠偏卡（✅ 已完成）
1. ~~药柜招商骗局识别卡~~ → `concept-medical-cabinet-fraud-detection.md`
2. ~~合规红线卡~~ → `concept-medical-cabinet-compliance-redlines.md`
3. ~~推销口径 vs 监管口径对照卡~~ → `concept-pitch-vs-regulation-misalignment.md`

### 第二阶段：基础事实卡（✅ 已完成）
4. ~~全国智能药柜政策地图卡~~ → `concept-regional-policy-map.md`
5. ~~48 号公告红线卡~~ → `fact-national-policy-redlines.md`
6. ~~单点财务模型卡~~ → `method-single-point-financial-model.md`
7. ~~O2O 平台费用结构卡~~ → `fact-o2o-cost-structure.md`

### 第三阶段：深度洞察卡（✅ 已完成）
8. ~~失败模式案例库卡~~ → `insight-failure-patterns-case-library.md`
9. ~~诊所+药柜法律关系卡~~ → `concept-clinic-cabinet-legal-relationships.md`
10. ~~选址框架卡~~ → `method-medical-cabinet-site-selection.md`
11. ~~国际经验对照卡~~ → `insight-international-medical-cabinet-experience.md`
12. ~~消费者支付意愿卡~~ → `insight-consumer-willingness-medical-cabinet.md`
13. ~~巨头为何不布局诊所药柜卡~~ → `insight-giants-why-not-clinic-cabinet.md`

### 第四阶段：专项补充卡（✅ 已完成）
14. ~~硬件技术专题卡~~ → `concept-medical-cabinet-hardware-technology.md`
15. ~~业务公式拆解与关键假设验证卡~~ → `method-medical-cabinet-business-model-decomposition.md`
16. ~~医疗短视频合规卡~~ → `concept-medical-shortvideo-compliance-for-clinics.md`

---

## 五、B 阶段完成情况

B 阶段三项任务：
1. ✅ 生成医疗短视频合规卡
2. ⏳ 复核 12 条被污染录音
3. ⏳ 建立线下调研任务清单

当前药柜主题长程整理共生成 **17 张基础卡**。

---

## 五、下一步行动建议

### A 阶段已完成（本轮）
1. ✅ 创建药柜主题专门工作目录：`60_feedback/itingnao/medical-cabinet-longterm/`
2. ✅ 生成 14 张基础卡，覆盖止血纠偏、基础事实、深度洞察、硬件技术专题。
3. ✅ 所有卡片均标注置信度、信任等级、来源引用、局限性和待核验问题。
4. ✅ 对"300 万 SKU"等异常数据在相关卡片中标记为待复核/降级。

### B 阶段建议（下一步）
1. **生成医疗短视频合规卡**：`medical-shortvideo-compliance-for-clinics.md`
2. **复核 12 条被污染录音**：确定是否正式移入药柜处理队列并生成对应卡片。
3. **建立"线下调研任务清单"模板**：分配验证责任，重点验证 P0 项目（单点销售额、医保个账口径、设备真实成本、200 台订单书面材料等）。
4. **复核已进入 `30_wiki/` 的药柜卡**：`smart-medicine-cabinet-distribution.md` 是否需要按新发现的矛盾点更新或降级。
5. **处理异常数据**：
   - "300 万 SKU" vs 800 SKU vs 336 品规
   - "泉州万达 24h 店月销 2000 万元"
   - 6 月 1 日深圳龙岗上线性质（内测 vs 对外运营）

### 长期（持续）
6. 每获得一项线下验证结果，更新对应知识卡并标注验证日期与来源。
7. 定期复核药柜卡，建议每 3 个月复核一次，政策和市场变化快。
8. 仅当卡片可信度 ≥ 0.78、来源清晰、经过外部交叉验证时，方可进入 `30_wiki/`。

---

## 六、风险提醒

1. **药柜主题涉及处方药、医保、执业药师等强监管领域，任何知识卡都必须以法规原文和官方口径为最高依据。**
2. **推销方录音存在系统性"轻合规"倾向，不能直接作为事实依据。**
3. **单点运营数据、设备成本、平台合作条款等关键数字，未经书面材料或第三方验证前，必须标注"待验证"。**
4. **所有进入 `30_wiki/` 的药柜卡应设置更短的复核周期（建议 3 个月），因为政策和市场变化快。**

---

*创建时间：2026-06-13*  
*状态：长程项目启动，本路线图为第一版规划，待线下调研结果迭代更新。*
