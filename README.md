# ftescursor

肝胆外科 / 肝癌（HCC）小时级**资讯过滤器**（增量 digest，非全量百科）。

**最新小时包（UTC）**: [`202608/01/04`](202608/01/04/) — 主读 [`01_delta_brief.md`](202608/01/04/01_delta_brief.md)

## Collectors（固化脚本）

站点抓取逻辑已固化在仓库：[`scripts/hcc_collect/`](scripts/hcc_collect/)。  
Automation 每小时应 **调用脚本**，不要重写 scraper。

```bash
export OPENALEX_API_KEY='…'   # 只放 prompt / 运行时环境，勿提交仓库
python -m scripts.hcc_collect --trigger-utc "$TRIGGER_UTC" --out YYYYMM/DD/HH
```

说明见 [`scripts/README.md`](scripts/README.md)。
