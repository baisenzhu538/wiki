# 老朱个人域 (personal-os)

> 这是 KDO 知识库中属于老朱个人的区域。
> 它不是方法论卡——它是老朱的**使用说明书**。

## 文件

| 文件 | 内容 | 维护人 |
|:---|:---|:---|
| `zhu-time-os.md` | 时间配置、双峰安排、任务深度分级 | 老朱 + 王语嫣 |
| `zhu-domain-index.md` | 各域使用频率、调用过的框架 | 自动（kdo capture） |
| `zhu-feedback-patterns.md` | 重复出现的偏好、盲区、决策习惯 | 王语嫣 |
| `zhu-project-board.md` | 多条项目线分泳道看板（防混线） | 王语嫣 |

## 数据库

| 表 | 位置 | 内容 |
|:---|:---|:---|
| `zhu_decisions` | `.kdo/state.sqlite` | 结构化决策记录 |

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
