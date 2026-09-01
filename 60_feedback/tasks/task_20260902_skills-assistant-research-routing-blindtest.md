# Skill 路由面盲测：KDO 工厂 research 路由

> 测试条件：agent 未读任何 skill 正文，仅凭目录（名称 + 一句话 description）做路由判定。
> 测试时间：2026-09-02

---

## 请求A："帮我调研一下中国咖啡行业的市场规模和趋势，做个行业报告"

**应加载**: `research-core`（入口）→ 第三层武器库按需载 `research-industry-report`
**走层**: 第一层 OSCAR 意图路由（识别为调研/行业分析）→ 第二层纪律过门禁 → 第三层载入行业报告武器

理由：
- research-core description 触发词白名单明确含 **"调研"、"行业分析"**，请求原文"帮我调研一下…行业"双词命中，且"任何调研…任务先走本入口"，故第一层路由必进 research-core（research 薄壳虽也写"商业调研入口"，但其 description 自述"已并入 research-core…加载 research-core 获取三层完整路由"，仍指向同一入口，不产生分流）。
- 请求要"做个行业报告"，research-industry-report 的 description 为"【research-core 武器库·行业报告】**行业报告调研**——Doris四步法+搜索七技"，与"行业报告"精确对应，属第三层武器库按需载。

---

## 请求B："验证一下这个说法靠不靠谱：某某品牌市占率40%。帮我核实一下"

**应加载**: `research-core` → 第二层核心纪律·交叉验证，命中 `research-cross-validation`（主）+ `six-layer-cross-validation`（辅）
**走层**: 第一层意图路由（查证类）→ 第二层纪律分支：交叉验证

理由：
- research-core 触发词白名单含 **"查证、验证断言"**，请求原文"验证一下…靠不靠谱""帮我核实一下"即验证断言/查证，命中入口。
- 第二层纪律 description 为"交叉验证+质量门禁+深挖引擎"，本请求属**交叉验证**分支；research-cross-validation 的 description"每条核心结论≥**2个独立来源**"正对应核实"市占率40%"这一断言需多源互证；six-layer-cross-validation"从**来源/时间/逻辑/数据/反例/行动**六维度检验信息可信度"可作为叠加检验卡。

---

## 请求C："帮我深挖这个奶茶加盟项目到底能不能做，往深了看，风险画像"

**应加载**: `research-core` → 第二层核心纪律·深挖引擎，命中 `nine-layer-deep-dig`（主）+ `research-sats`（辅）
**走层**: 第一层意图路由（深挖/尽调类）→ 第二层纪律分支：深挖引擎

理由：
- research-core 触发词白名单含 **"深挖、尽调"**，请求原文"帮我深挖…往深了看"命中；奶茶加盟项目属商业尽调，亦命中"尽调"。
- 第二层纪律"深挖引擎"分支下：nine-layer-deep-dig description 为"九层深挖法——从业务公式到**决策框架**的自我纠错式迭代分析"，"到底能不能做"正是决策评估，主命中；"风险画像"对应 research-sats 的"CIA SATs 结构化分析——**Devils Advocacy/Red Team**"，对抗式找风险，叠加命中。

---

## 总评

**能 3 秒判断。** 路由面设计的关键杠杆有四个：① research-core 作为唯一入口并带**触发词白名单**（调研/查证/深挖/尽调/行业分析…），请求关键词可机械比对；② 每个纪律卡与武器卡都带**【层·职能】前缀**（纪律层·交叉验证 / 深挖引擎、武器库·行业报告），入口→层→卡的映射不需要正文；③ 第二层纪律内部职责互斥（验证 vs 深挖），请求动词即可分流；④ 薄壳卡自述"并入 research-core"，消除入口竞争。唯一轻微歧义在深挖引擎层内 nine-layer-deep-dig 与 research-sats 的分工需按"决策评估 vs 对抗分析"细分，但两卡同层可叠加，不影响秒判。
