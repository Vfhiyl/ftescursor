# 增量简报｜2026-07-30 UTC 22h

## 1) 增量计数

| 通道 | 本小时 | vs 21h | 标记 |
|------|--------|--------|------|
| PubMed EDAT | **119** | 119 | NEW=0 / DROPPED=0 |
| PubMed PDAT | **40** | 40 | 同窗 |
| 临床向标题子集 | **23** | 27 | 评分边界微差，非新 PMID |
| Crossref 标题过滤去重 | **126** | 142 | NEW DOI=1（噪音） / DROPPED=17（窗/过滤 churn，非撤证） |
| ClinicalTrials 相关 LastUpdate | **15**（focus 15） | 15 / 15 | NEW=0 / DROPPED=0（HAI carfilzomib 已 force-include） |
| OpenAlex（publication_date） | **2** works / **4** preprint(7d) | 2 / 4 | works NEW=0；preprint NEW=0 |
| 预印本（medRxiv/bioRxiv/EPMC PPR） | **1**+**4**+**2** | 1+4+2 | 实质全 SEEN；NSCLC/非肝假阳性已剔 |
| EDAT ID 集与上一小时相同？ | **是** | — | **无实质增量** |

## 2) 本小时必读（≤5）

无新增必读。延续：TORCH III 期已入 EDAT（[PMID 42530948](https://pubmed.ncbi.nlm.nih.gov/42530948/) / [42530952](https://pubmed.ncbi.nlm.nih.gov/42530952/)），见 [`../17/`](../17/)。

成对提醒（UNCHANGED）：EMERALD-1 **终局 OS−** ↔ EMERALD-3 **PFS+/OS 未成熟**

## 3) 观察名单（≤10）

1. 21h 观察延续：SLA 六段切除 `10.1097/sla.0000000000007166`、PNI 肝切除 `10.3329/jssmc.v17i1.92339` — 见 [`../21/`](../21/)（本小时 Crossref 过滤未再入集）
2. 20h 观察延续：利比亚 HCC 生物标志物 `10.65405/rg255s55` — 见 [`../20/`](../20/)
3. 19h 观察延续：CT0180 GPC3-TCR I 期（`10.1158/1078-0432.ccr-26-1084`）— 见 [`../19/`](../19/)
4. 18h/17h 观察延续：Deep Response 终点、TORCH、M2BPGi SR/MA — 见 [`../18/`](../18/)、[`../17/`](../17/)

## 4) 已过滤噪音（例）

- Crossref NEW：`10.9734/jammr/2026/v38i86179` — 肝移植候选者根尖周炎牙髓个案（endodontic LT），非 HCC 决策
- Crossref DROPPED×17：多为 21h 已标 MASLD/AI/术式外设项的标题过滤/窗滑动 churn
- medRxiv：Durvalumab + Stage III **NSCLC** 假阳性已剔除
- bioRxiv：非洲人群树拓扑 / 糖皮质激素受体动力学等非肝假阳性已剔除
- HAS 首页 keyword_hits=1 为页面噪声串，非肝癌意见

## 5) 相对上一小时一句话

**EDAT 119 完全相同；Crossref 仅牙科移植个案噪音 + 过滤计数下滑；试验/OpenAlex/预印本/指南均无实质新增。**

## 6) previous_folder

→ [`202607/30/21`](../21/)

## 7) 预印本观察（未同行评议）

1. SEEN bioRxiv：[10.64898/2026.07.13.738237](https://doi.org/10.64898/2026.07.13.738237) — HCC/ICC 谱系机制（DOI 连续性）
2. SEEN bioRxiv：[10.64898/2026.07.28.741157](https://doi.org/10.64898/2026.07.28.741157) — 肝类器官成熟比较（降权）
3. SEEN EPMC：[10.21203/rs.3.rs-10395965/v1](https://doi.org/10.21203/rs.3.rs-10395965/v1) — 机器人肝切除学习曲线
4. SEEN EPMC：[10.20944/preprints202607.2078.v1](https://doi.org/10.20944/preprints202607.2078.v1) — HepG2 体外细胞毒
5. SEEN medRxiv（降权/非 HCC 决策）：[10.64898/2026.07.28.26359152](https://doi.org/10.64898/2026.07.28.26359152) — 光子计数 CT 肝脂肪定量
