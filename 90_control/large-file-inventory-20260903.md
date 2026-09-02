# #625 存量大文件清单（>15MB git 跟踪文件）

> 2026-09-03 黄药师，#625 任务 1 第三层（存量处置方案）。
> **红线遵守：只出清单+处置建议，不动任何文件。处置归王语嫣编排/老朱拍板。**
> 扫描口径：`git ls-files -z` 全量 + 工作区 st_size，阈值 >15MB（与第二层 WARNING 同口径）。

## 清单（17 个文件，合计 346.8MB）

| 大小 | 文件 | 类别 |
|---:|:--|:--|
| 46.6MB | `10_raw/assets/wechat-collect/346efef2737b383b.mp4` | 视频号采集 |
| 25.6MB | `60_feedback/wechat-collect/douyin-dali/7654610643165120177.mp4` | 抖音采集 |
| 24.8MB | `10_raw/itingnao/details/7091957.json` | itingnao 明细 |
| 21.7MB | `10_raw/itingnao/details/7095114.json` | itingnao 明细 |
| 21.2MB | `10_raw/assets/wechat-collect/2404c1658025473c.mp4` | 视频号采集 |
| 19.5MB | `10_raw/assets/wechat-collect/68004aecb3d913a5.mp4` | 视频号采集 |
| 19.3MB | `10_raw/assets/wechat-collect/e7536bf1d8f1a7b1.mp4` | 视频号采集 |
| 18.7MB | `10_raw/itingnao/details/4092592.json` | itingnao 明细 |
| 18.6MB | `10_raw/itingnao/details/6249248.json` | itingnao 明细 |
| 18.1MB | `10_raw/itingnao/details/7356146.json` | itingnao 明细 |
| 16.9MB | `10_raw/itingnao/details/4273172.json` | itingnao 明细 |
| 16.8MB | `logs/headless-huangyaoshi-20260902-044139.log` | headless 日志 |
| 16.4MB | `10_raw/itingnao/details/6951012.json` | itingnao 明细 |
| 16.3MB | `10_raw/itingnao/details/4410138.json` | itingnao 明细 |
| 16.2MB | `10_raw/itingnao/details/2222280.json` | itingnao 明细 |
| 15.3MB | `10_raw/itingnao/details/4288010.json` | itingnao 明细 |
| 15.0MB | `60_feedback/wechat-collect/douyin-dali/7666832665312982138.mp4` | 抖音采集 |

## 风险判读

- **当前全部 <100MB**，push 无即时风险；最大 46.6MB，按采集管线节奏约 1 年内自然越线（老顽童建议书同判）。
- 三个增长源：微信视频号 mp4（`10_raw/assets/wechat-collect/`）、抖音 mp4（`60_feedback/wechat-collect/`）、itingnao 明细 json（`10_raw/itingnao/details/`）——均为**持续增长**管线产物，不是一次性存量。
- headless 日志 16.9MB 一例：`logs/` 无大小管理，长跑会越积越大。

## 处置建议（供王语嫣编排/老朱拍板，本单不执行）

1. **首选：不动存量**（采纳老顽童建议书待裁定项 3 的「前者」口径）——远小于 100MB 能正常推；第一层 .gitignore 已断新增，第二层门禁兜底越线。**建议采纳**。
2. 若要减重：三类管线产物可批量 `git rm --cached` + 移 D:\KDO-memory\ 归档（历史仍在，filter-repo 才清得掉——391MB zip 处置已验证该链路）。**不建议为本批做 filter-repo**（动历史代价 >> 收益）。
3. `logs/` 建议另立日志滚动/忽略规则（超出本单范围，可另开单）。

## 数字可复跑

```bash
git ls-files -z | xargs -0 -I{} sh -c 'wc -c < "{}"' # 或本单任务单执行报告内 python 一行流
```
