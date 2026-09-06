# 队列完整性审计报告

- 审计范围: `C:\Users\Administrator\Desktop\wiki\60_feedback\tasks`, `C:\Users\Administrator\Desktop\wiki\70_product\tasks`
- reviewed 任务单总数: 588
- 任务单元数据异常数: 36
- 队列/任务单状态不一致数: 3
- 队列解析行数: 229
- 无法解析队列行数: 0（#456：行数异常禁静默跳过，列此清单）

## 任务单元数据异常列表（缺 review_date / reviewer / review 文件）
- `task_20260804_wangyuyan-dk-lu-gui-lv-review`: reviewed 但缺少 review_date
- `task_20260804_wangyuyan-dk-lu-gui-lv-review`: reviewed 但缺少 reviewer/reviewed_by
- `task_20260806_huangyaoshi-deadlink-lint-gate`: reviewed 但缺少 review_date
- `task_20260806_huangyaoshi-deadlink-lint-gate`: reviewed 但缺少 reviewer/reviewed_by
- `task_20260806_huangyaoshi-deadlink-lint-gate`: reviewed 但无对应 review/audit 文件且无review_date
- `task_20260806_huangyaoshi-kdo-moc`: reviewed 但缺少 review_date
- `task_20260806_huangyaoshi-kdo-moc`: reviewed 但缺少 reviewer/reviewed_by
- `task_20260806_huangyaoshi-kdo-moc`: reviewed 但无对应 review/audit 文件且无review_date
- `task_20260806_huangyaoshi-master-moc`: reviewed 但缺少 review_date
- `task_20260806_huangyaoshi-master-moc`: reviewed 但缺少 reviewer/reviewed_by
- `task_20260806_huangyaoshi-master-moc`: reviewed 但无对应 review/audit 文件且无review_date
- `task_20260806_huangyaoshi-product-moc`: reviewed 但缺少 review_date
- `task_20260806_huangyaoshi-product-moc`: reviewed 但缺少 reviewer/reviewed_by
- `task_20260806_huangyaoshi-product-moc`: reviewed 但无对应 review/audit 文件且无review_date
- `task_20260806_wangyuyan-deep-review-backlink`: reviewed 但缺少 review_date
- `task_20260806_wangyuyan-deep-review-backlink`: reviewed 但缺少 reviewer/reviewed_by
- `task_20260806_wangyuyan-deep-review-core-frameworks`: reviewed 但缺少 review_date
- `task_20260806_wangyuyan-deep-review-core-frameworks`: reviewed 但缺少 reviewer/reviewed_by
- `task_20260808_wangyuyan-feature-consumption-pilot`: reviewed 但缺少 review_date
- `task_20260808_wangyuyan-feature-consumption-pilot`: reviewed 但缺少 reviewer/reviewed_by
- `task_20260808_wangyuyan-feature-consumption-pilot`: reviewed 但无对应 review/audit 文件且无review_date
- `task_20260808_wangyuyan-feature-thinking-w3w4`: reviewed 但缺少 review_date
- `task_20260808_wangyuyan-feature-thinking-w3w4`: reviewed 但缺少 reviewer/reviewed_by
- `task_20260808_wangyuyan-feature-thinking-w3w4`: reviewed 但无对应 review/audit 文件且无review_date
- `task_20260809_huangyaoshi-e018-and-protocol-fixes`: reviewed 但缺少 review_date
- `task_20260809_huangyaoshi-e018-and-protocol-fixes`: reviewed 但缺少 reviewer/reviewed_by
- `task_20260809_huangyaoshi-e018-and-protocol-fixes`: reviewed 但无对应 review/audit 文件且无review_date
- `task_20260809_laowantong-agent-production-pipeline`: reviewed 但缺少 review_date
- `task_20260809_laowantong-agent-production-pipeline`: reviewed 但缺少 reviewer/reviewed_by
- `task_20260809_laowantong-agent-production-pipeline`: reviewed 但无对应 review/audit 文件且无review_date
- `task_20260809_wangyuyan-external-agent-feedback-loop`: reviewed 但缺少 review_date
- `task_20260809_wangyuyan-external-agent-feedback-loop`: reviewed 但缺少 reviewer/reviewed_by
- `task_20260809_wangyuyan-external-agent-feedback-loop`: reviewed 但无对应 review/audit 文件且无review_date
- `544`: reviewed 但缺少 review_date
- `544`: reviewed 但缺少 reviewer/reviewed_by
- `544`: reviewed 但无对应 review/audit 文件且无review_date

## 队列/任务单状态不一致（双向）
### 队列已 reviewed，但任务单未 reviewed
- `task_20260815_wangyuyan-agent-spec-domain-cleanup`: 队列 status=reviewed 但任务单 status=pending_review
- `task_20260815_huangyaoshi-gbk-output-fix`: 队列 status=reviewed 但任务单 status=pending_review
- `task_20260816_wangyuyan-snapshot-migration-rollout`: 队列 status=reviewed 但任务单 status=pending_review
