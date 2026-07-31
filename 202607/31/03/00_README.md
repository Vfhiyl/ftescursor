# HCC delta pack — 202607/31/03

- **Trigger UTC**: `2026-07-31T03:00:31.034Z`
- **Window**: last 24h from trigger (`2026-07-30T03:00:31.034000+00:00` → `2026-07-31T03:00:31.034000+00:00`)
- **Previous**: [`202607/31/02`](../02/)
- **Mode**: delta filter（本小时无实质增量）
- **Collector**: `scripts.hcc_collect`

## Files

| File | Role |
|------|------|
| `01_delta_brief.md` | 主读：增量计数 + 必读/观察 |
| `02_new_high_signal.md` | 仅 NEW/UPDATED 高信号 |
| `03_guidelines_watch.md` | 指南哨兵 |
| `04_news_watch.md` | 专业媒体近窗 |
| `05_trials_stats.md` | CT 增量 |
| `meta.json` | 机器可读元数据 |
| `collect_summary.json` | 采集计数与 ID 集合 |
| `raw_*.json` | 原始采集追溯 |
