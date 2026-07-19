# 老朱个人域 (personal-os)

> 这是 KDO 知识库中属于老朱个人的区域。
> 它不是方法论卡——它是老朱的**使用说明书**。

## 文件

| 文件 | 内容 | 维护人 | 更新频率 |
|:---|:---|:---|:---|
| `README.md` | 本索引 + 更新规则总览 | 王语嫣 | 文件增删时 |
| `zhu-time-os.md` | 时间配置、双峰安排、任务深度分级 | 老朱 + 王语嫣 | 节奏变化时 |
| `zhu-domain-index.md` | 各域使用频率、调用过的框架 | 自动（kdo capture） | 每次决策 |
| `zhu-feedback-patterns.md` | 重复出现的偏好、盲区、决策习惯 | 王语嫣 | 每次对话 |
| `zhu-project-board.md` | 多条项目线分泳道看板（防混线） | 王语嫣 | 项目变化时 |
| `zhu-strategic-conclusions.md` | 已确认/待确认战略结论 | 王语嫣 | 产生战略判断时 |
| `wangyuyan-working-protocols.md` | 王语嫣工作协议集（长素材分层读取协议等） | 王语嫣 | 规则变化时 |
| `zhu-network-resources.md` | 关键关系、资源禀赋、合作方档案 | 王语嫣 | 关系变化时 |
| `zhu-lessons-learned.md` | 过往经验教训案例库 | 王语嫣 | 重大经验输入时 |
| `zhu-weekly-reflections.md` | 周度所思所想汇编 | 王语嫣 | 每周 |
| `zhu-future-directions.md` | 未来10年方向蓄水池（来源+状态+关键假设+验证动作） | 王语嫣 | 老朱想到新方向时 |

## 数据库

| 表 | 位置 | 内容 |
|:---|:---|:---|
| `zhu_decisions` | `.kdo/state.sqlite` | 结构化决策记录 |

## 内容入域规则

| 内容类型 | 进入哪里 | 示例 |
|:---|:---|:---|
| 基础身份/背景更新 | `20_memory/user-insight-profile.md` | 新身份、新公司、团队变化 |
| 决策记录 | `.kdo/state.sqlite` + `zhu-domain-index.md` | "决定 OPC 先做控制系统输出" |
| 偏好/盲区/习惯 | `zhu-feedback-patterns.md` | "口述稿优先"、"每次只问一条" |
| 战略方向 | `zhu-strategic-conclusions.md` | "利润优先于规模" |
| 项目进展 | `zhu-project-board.md` | 鑫港湾、OPC、EC 代码库状态 |
| 关键关系 | `zhu-network-resources.md` | 袁总、供应商、潜在客户 |
| 经验教训 | `zhu-lessons-learned.md` | 巨米失败、成本定价教训 |
| 日常所思 | `zhu-weekly-reflections.md` | 本周对 OPC 模式的判断 |
| 时间/能量 | `zhu-time-os.md` | 新作息、新时间分配原则 |

## 脱敏与隐私规则

1. **personal-os 内文件**：可保留真实人名、公司名、具体数字。**不对外发布**，仅本地 Agent 使用。
2. **进入 30_wiki 的案例卡**：必须脱敏。
   - 人名：用「某总」「创始人」或化名
   - 公司名：用「某智能设备公司」「某医药科技公司」
   - 具体数字：可保留区间或比例，但隐去绝对金额（除非公开信息）
   - 地域：可保留到省/市级别，必要时模糊化
3. **边界**：涉及未公开法律纠纷、个人隐私的内容只进 personal-os，不进 30_wiki。

## 持续更新工作流

### 每次对话结束时（王语嫣执行）

1. 回顾本次对话产生了哪些关于老朱的新信息
2. 分类写入：
   - 决策 → `kdo capture --kind decision --domain <域> "<决策内容>"`
   - 偏好/盲区 → `zhu-feedback-patterns.md`
   - 战略结论 → `zhu-strategic-conclusions.md`
   - 项目状态 → `zhu-project-board.md`
   - 新关系/资源 → `zhu-network-resources.md`
   - 重大经验教训 → `zhu-lessons-learned.md`
3. 写 Truman 复盘并运行 `daily-context-save.py`

### 每周一次（周末协作峰）

1. 读本周 daily-context 复盘 + `zhu_decisions` 最近记录
2. 提炼主题写入 `zhu-weekly-reflections.md`
3. 核对 `zhu-project-board.md` 各泳道

### 每月一次

1. 通读 personal-os 全目录，标记过期信息
2. 更新 `20_memory/user-insight-profile.md`
3. 检查 `zhu-domain-index.md` 是否反映真实域使用频率

## 如何使用

### 记录一次决策
```bash
kdo capture "今天做了X决策，用了Y框架，结果是Z" --kind decision --domain sales
```

### 查看决策历史
```bash
python -c "import sqlite3; db=sqlite3.connect('.kdo/state.sqlite'); [print(r) for r in db.execute('SELECT ts,domain,decision FROM zhu_decisions ORDER BY ts DESC LIMIT 10')]"
```

### 王语嫣查个人域
王语嫣启动时自动读本目录下所有文件 + 查 zhu_decisions 表最近 10 条。
