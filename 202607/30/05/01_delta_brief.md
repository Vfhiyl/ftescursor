# 增量简报｜2026-07-30 UTC 05h

## 1) 增量计数

| 通道 | 本小时 | vs 04h | 标记 |
|------|--------|--------|------|
| PubMed EDAT | **93** | 76 → **+17 NEW** | **ID 集变化**（DROPPED=0） |
| PubMed PDAT | **26** | 14 | ↑ |
| 临床向标题子集 | **20** | 16 | 含多条 FP（骶骨 SBRT / 前列腺 / 肺 LCNEC） |
| Crossref 标题过滤去重 | **82** | 112 | **+5 NEW DOI**；DROPPED 35（多为 04h 宽松 `liver` 过滤滚出 + 旁系，非撤回） |
| ClinicalTrials 相关 LastUpdate | **14**（focus 14） | 14 / 14 | NEW NCT = 0；DROPPED 0 |
| 预印本（medRxiv/bioRxiv/EPMC PPR） | **2**（EPMC） | 2 | NEW = 0；2 条 SEEN |
| EDAT ID 集与上一小时相同？ | **否** | — | 有索引增量；**无双信源必读** |

## 2) 本小时必读（≤5）

**无新增必读**（NEW 条目缺独立第二信源，或终点仅为 DCR/ORR/影像 CR）。

请继续看最近实质包：
- [`../../29/18/01_delta_brief.md`](../../29/18/01_delta_brief.md) — JLCA 转化定义；BTC CGD→手术；NI±仑伐（PFS≠OS）
- 成对提醒（UNCHANGED）：EMERALD-1 **终局 OS−** ↔ EMERALD-3 **PFS+/OS 未成熟**

## 3) 观察名单（≤10）

1. **NEW** PMID [42527085](https://pubmed.ncbi.nlm.nih.gov/42527085/) — DT 进展后仑伐替尼 vs 一线仑伐（多中心 RW；DCR 69.2% vs 69.1%，ORR 30.8% vs 38.2%）。**DCR/ORR ≠ OS**；单刊 *Anticancer Res*，未升权。
2. **NEW** PMID [42527069](https://pubmed.ncbi.nlm.nih.gov/42527069/) — 后上段 HCC：MILR vs OLR PSM（匹配后各 n=39）；围术期优势、OS/RFS 无显著差。单中心。
3. **NEW** PMID [42527617](https://pubmed.ncbi.nlm.nih.gov/42527617/) — 高比活度树脂 Y-90 节段切除单中心 n=60；3 月 CR 79%；剂量阈值探索。单信源，降权。
4. **NEW** PMID [42526847](https://pubmed.ncbi.nlm.nih.gov/42526847/) — 韩国 BTC 胚系致病变异多中心 n=172（iCCA/GBC）；咨询参考，非治疗标准。
5. **NEW** PMID [42527293](https://pubmed.ncbi.nlm.nih.gov/42527293/) — 阿拉伯世界 HCC 系统综述（Crossref 04h 已见）— 区域流行病学，不升国际标准。
6. **NEW Crossref** DOI [10.3389/fonc.2026.1907000](https://doi.org/10.3389/fonc.2026.1907000) — 多相 CT radiomics 鉴别孤立肝转移 vs iCCA；影像方法学。
7. CT：窗内 TACE±AtezoBev / HAIC / TITAN-HCC 等行政 LastUpdate，**无 results 新贴**。

## 4) 已过滤噪音（例）

- FP：骶骨 SBRT 勾画（42526598）；前列腺 GTV micro-boost（42526651）；肺 LCNEC+durvalumab 方案（42526918）；RCC pembro+仑伐（42527074 / Crossref `10.21873/anticanres.18305`）
- 撤稿/勘误：POU2AF1 撤稿（42527170）；Smilax 外泌体样纳米纠错（42527274）
- 降权：自身抗体综述（42526779）；C16orf74 机制+肽（42527075）；脊柱 CCA 转移 SRS（42527634）；VETC 分形影像（42527779）；低 CVP 肝切除述评（42527888）；支气管胆瘘个案综述（42527869）；DCTPP1 靶点综述（Crossref `10.3390/cimb48080770`）

## 5) 相对上一小时一句话

**EDAT 76→93（+17 NEW PMID），但多为 FP/单刊 RW/影像/撤稿；Crossref +5 非材料 DOI；CT/预印本/指南无实质变化——无双信源必读。**

## 6) previous_folder

→ [`202607/30/04`](../04/)

## 7) 预印本观察（未同行评议）

1. SEEN：DOI [10.21203/rs.3.rs-10395965/v1](https://doi.org/10.21203/rs.3.rs-10395965/v1) — 单中心机器人辅助肝切除学习曲线（见 03h）。
2. SEEN：DOI [10.20944/preprints202607.2078.v1](https://doi.org/10.20944/preprints202607.2078.v1) — HepG2 植物成分体外细胞毒（见 02h）。
3. medRxiv / bioRxiv details API 近窗主题命中：**0**（见 `raw_preprints.json`）。
