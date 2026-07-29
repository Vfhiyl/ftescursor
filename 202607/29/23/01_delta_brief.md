# 增量简报｜2026-07-29 UTC 23h

## 1) 增量计数

| 通道 | 本小时 | vs 22h | 标记 |
|------|--------|--------|------|
| PubMed EDAT | **176** | 170 | **+6 NEW PMID**（ID 集变化） |
| PubMed PDAT | **51** | 49 | +2 |
| 临床向标题子集 | **43** | 40 | 含假阳性/机制滚入 |
| Crossref 标题过滤去重 | **128** | 128 | NEW DOI = 0 |
| ClinicalTrials 相关 LastUpdate | **28**（focus 21） | 24 / 21 | NEW/再入 5；滚出 1；**无 results** |
| 预印本（medRxiv/bioRxiv/EPMC PPR） | **0** | 0 | 近窗无命中 |
| EDAT ID 集与上一小时相同？ | **否** | — | 有索引增量，**无实质临床升权** |

## 2) 本小时必读（≤5）

**无新增必读。** 6 条 NEW PMID 均未达升权门槛（假阳性 / 机制 / 机房物理 / 地方会议摘要且无第二信源）。

请继续看最近实质包：
- [`../18/01_delta_brief.md`](../18/01_delta_brief.md) — JLCA 转化定义共识（42524660）；BTC CGD→手术 RW（42524843）；NI±仑伐 RW PFS+/OS−（42524515）
- 成对提醒（UNCHANGED）：EMERALD-1 **终局 OS−** ↔ EMERALD-3 **PFS+/OS 未成熟**
- 更早锚点：[`../11/`](../11/) *Ann Surg* QI；[`../05/`](../05/) BILCAP-Real 等——不重写

## 3) 观察名单（≤10）

1. **NEW→PubMed** radioproteomic 早复发模型 PMID [42525890](https://pubmed.ncbi.nlm.nih.gov/42525890/)（DOI 已在 21h Crossref）— 预测模型，**无第二信源**，不升权。
2. **NEW→PubMed** 机械传感机制 PMID [42525956](https://pubmed.ncbi.nlm.nih.gov/42525956/)（DOI 已在 21h Crossref）— 机制，降权。
3. **NEW** CCA 美国死亡趋势摘要 PMID [42525995](https://pubmed.ncbi.nlm.nih.gov/42525995/)（*South Dakota Med*）— 流行病学摘要，无 DOI/双信源。
4. **NEW** HCV-HCC NIS 住院结局摘要 PMID [42526003](https://pubmed.ncbi.nlm.nih.gov/42526003/) — 同上，地方期刊摘要。
5. CT 再入（行政/外周）：biobank [NCT00034216](https://clinicaltrials.gov/study/NCT00034216)；CRCLM+HAIC [NCT06199232](https://clinicaltrials.gov/study/NCT06199232)；futibatinib continuation [NCT06506955](https://clinicaltrials.gov/study/NCT06506955)；黑色素瘤肝转移 [NCT07281924](https://clinicaltrials.gov/study/NCT07281924)；PCOS 脂肪肝 [NCT07731373](https://clinicaltrials.gov/study/NCT07731373) — **均无 results**。
6. 18h 必读延续：JLCA 转化定义；BTC CGD 二次手术；NI±LEN（PFS≠OS）。

## 4) 已过滤噪音（例）

- PMID [42525921](https://pubmed.ncbi.nlm.nih.gov/42525921/) COMMIT — **dMMR 转移性结直肠癌**（atezolizumab 宽词假阳性），非 HCC
- PMID [42525523](https://pubmed.ncbi.nlm.nih.gov/42525523/) 6MV FFF 机房 commissioning — SBRT 物理，非临床 HCC
- CT：采血 biobank / CRCLM HAIC / 黑色素瘤 Hepzato / PCOS 脂肪肝 / futibatinib 延续给药 — LastUpdate ≠ 疗效证据
- Crossref：NEW DOI=0；既有降权项继续降权

## 5) 相对上一小时一句话

**EDAT 170→176（+6 NEW PMID）：2 条为 21h Crossref 已见之 radioproteomic/机制现入 PubMed，余为结直肠假阳性、FFF 物理与地方摘要；Crossref NEW DOI=0；CT related 24→28（外周再入为主）、focus 21 不变、无 results；预印本 0；指南/新闻无改版——无升权必读。**

## 6) previous_folder

→ [`202607/29/22`](../22/)

## 7) 预印本观察（未同行评议）

**近 24h 无 medRxiv / bioRxiv details API / Europe PMC（SRC:PPR）主题命中**（见 `raw_preprints.json`）。
