---
id: task_20260816_laowantong-baozhashidiaochan-wave3
assignee: hermes
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-16
priority: P2
wsjf: 2.5
created_at: 2026-08-16
updated_at: '2026-08-15T22:45:11.089736+00:00'
source: 王语嫣编排（2026-08-16）；#332 终审 PASS A- 后 Wave 3
related: null
---

# 爆炸式调研 Wave 3：dk 暗知识 8 卡（#334）

## 背景

Wave 1/2 框架与案例入库后，本批 = 暗知识 8 卡（防坑向，dk 七段门禁）。

## 卡清单（8 张，锚点见生产任务清单 Wave 3 表）

| ID | 名称 | 关键要点（口述锚点） |
|:--|:--|:--|
| W3-1 | 饱和自证话术 | "让 AI 记数就不太会骗人"（相对上一轮新增多少/对体系有修正吗）+换 5-10 关键词逼饱和（下 L1540-1562） |
| W3-2 | 分类方案 MECE 手术台 | 3-5 套方案+归位判据句+人拍板（选认知习惯最接近的，可再写 5 个）（下 L1570-1596） |
| W3-3 | 打样纠偏三轮法 | 5-10 个样本定颗粒度，决定后面所有工作方向（一堂课表案例：地图级→课级纠偏）（下 L3762-3768） |
| W3-4 | 私有库调研总量锚定法 | 缺口清单逼近 vs 边际递减（167 门课/至少 170 漏什么/逼着捞全）（下 L3770-3774） |
| W3-5 | 建不了模型就建排行榜 | Top10 审美锚点（十个坑动态替换）（下 L2404-2438） |
| W3-6 | 信息拾荒者 vs 规律建筑师 | 随机调研=盲人摸象每周摸一下 vs 一次爆炸式换未来确定性（下 L4046-4058） |
| W3-7 | 重要的事应做必做 | 饱和式输出探索：与其让 AI 给三五个答案，不如一次给三五十个（下 L4022-4044） |
| W3-8 | AI 没时间观念 | 时间锚定：越接近时间内容质量越高（下 L3552-3556） |

## 验收标准

- 8 卡 dk 七段完整（含 Critique 外部攻击 ≥2）
- 每卡含失败模式/防坑场景（dk 定位）
- `kdo pre-submit` PASS + `kdo lint` 零 FAIL

## 边界

- 单角色单任务（E026）：老顽童生产，欧阳锋终审
- 依赖 #333（Wave 2）可并行（dk 锚点独立）

## 执行报告（老顽童 hermes 实例，2026-08-16）

### 产出（Wave 3 八卡全部完成）
| ID | 文件 | 关键内容 |
|:--|:--|:--|
| W3-1 | `30_wiki/dark-knowledges/dk-research-saturation-self-proof.md` | 让 AI 记数就不太会骗人；换 5-10 关键词逼饱和；问相对上一轮新增/对体系有修正 |
| W3-2 | `30_wiki/dark-knowledges/dk-research-classification-mece-table.md` | 3-5 套方案+归位判据句+人拍板；选认知习惯最接近的；再写 5 个；A 一级+B 二级揉入 |
| W3-3 | `30_wiki/dark-knowledges/dk-research-sampling-correction-three-rounds.md` | 5-10 个样本定颗粒度决定方向（一堂课表案例：地图级→课级纠偏） |
| W3-4 | `30_wiki/dark-knowledges/dk-research-total-anchor-private-library.md` | 167 门课/至少 170 漏什么→逼着捞全（缺口清单逼近 vs 边际递减） |
| W3-5 | `30_wiki/dark-knowledges/dk-research-ranklist-replaces-model.md` | 建不了模型就建排行榜；Top10 十个坑动态替换；审美锚点 |
| W3-6 | `30_wiki/dark-knowledges/dk-research-scavenger-vs-architect.md` | 随机调研=盲人摸象信息拾荒 vs 一次爆炸式换未来确定性（规律建筑师） |
| W3-7 | `30_wiki/dark-knowledges/dk-research-important-things-must-do.md` | 重要的事应做必做；饱和式输出探索三五十个 vs 三五个；重合度 20-40%→70-90% |
| W3-8 | `30_wiki/dark-knowledges/dk-research-ai-no-time-concept.md` | 时间锚定（今年 8 月）；越接近时间内容质量越高 |

### 素材精做
- 口述下 L1540-1596（W3-1/2）/L2404-2438（W3-5）/L3552-3556（W3-8）/L3762-3774（W3-3/4）/L4022-4058（W3-6/7）锚点区间逐字精读
- ASR 误识别对照已核对；精做笔记追加 W3 锚点节

### pre-submit 门禁（8/8 PASS 零 warning）
- 全部 Passed 1/Failed 0；dk 七段完整（原始表述/使用场景/操作方法/适用边界/为什么值钱/Critique/与其他知识的关联）
- 每卡含 Critique 外部攻击 ≥2；定位声明已加（属于五步法/饱和覆盖体系）
- related 全量脚本验证：9-11 条/卡，死链=0，跨域≥2

### 验收对照
- [x] 8 卡 dk 七段完整（含 Critique ≥2 攻击者）
- [x] 每卡含失败模式/防坑场景
- [x] kdo pre-submit 8/8 PASS

### 边界遵守
- 单角色单任务（E026）；与 #333 并行（dk 锚点独立）；正文零虚构（全卡行号锚点）
