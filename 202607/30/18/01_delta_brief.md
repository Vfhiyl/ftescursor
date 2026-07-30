# 增量简报｜2026-07-30 UTC 18h

## 1) 增量计数

| 通道 | 本小时 | vs 17h | 标记 |
|------|--------|--------|------|
| PubMed EDAT | **119** | 119 | NEW=0 / DROPPED=0 |
| PubMed PDAT | **40** | 40 | 同窗 |
| 临床向标题子集 | **32** | 30 | 评分边界微差，非新 PMID |
| Crossref 标题过滤去重 | **132** | 125 | NEW DOI=10（无双信源必读） / DROPPED=3 |
| ClinicalTrials 相关 LastUpdate | **17**（focus 16） | 18 / 16 | DROPPED `NCT06786429`；focus 连续 |
| OpenAlex（publication_date） | **2** works / **8** preprint(7d) | 2 / 8 | works/preprint NEW DOI=0 |
| 预印本（medRxiv/bioRxiv/EPMC PPR） | 0+**2**+**2** | 0+2+2 | 谱系 SEEN；+organoid；NSCLC/neuro FP |
| EDAT ID 集与上一小时相同？ | **是** | — | **无实质增量** |

## 2) 本小时必读（≤5）

无新增必读。延续上一小时：TORCH III 期已入 EDAT（[PMID 42530948](https://pubmed.ncbi.nlm.nih.gov/42530948/) / [42530952](https://pubmed.ncbi.nlm.nih.gov/42530952/)），见 [`../17/`](../17/)。

成对提醒（UNCHANGED）：EMERALD-1 **终局 OS−** ↔ EMERALD-3 **PFS+/OS 未成熟**

## 3) 观察名单（≤10）

1. Crossref NEW（降权）：MASLD/FGF21、肝纤维化机制、急性肝损伤动物/TCM — 非 HCC 决策信号
2. Crossref NEW（外周）：LT 再移植 IVC 狭窄个案；肝结核脓肿病例
3. bioRxiv NEW（降权）：[10.64898/2026.07.28.741157](https://doi.org/10.64898/2026.07.28.741157) — 肝类器官成熟比较
4. 17h 观察延续：Deep Response 终点、老年切除全国研究、JHEP ICI-pre-LT、机器人 Glissonean 技术文
5. 既往必读延续：TORCH、M2BPGi SR/MA — 见 [`../17/`](../17/)、[`../11/`](../11/)

## 4) 已过滤噪音（例）

- CT 窗回闪：`NCT06638502`（CRC 肝转移术后肝再生药，非 HCC）— hard-FP 不进 related
- melanoma 肝转移 / PCOS steatosis 仍在原始窗，已剔除
- medRxiv：Stage III NSCLC durvalumab 动力学（假阳性）
- bioRxiv：brain-liver 葡萄糖调节（神经代谢假阳性）
- Crossref DROPPED×3：良性肝病 textbook / 机器人费用 SR / 营养指数病例（窗滑动）

## 5) 相对上一小时一句话

**EDAT 119 完全相同；Crossref/CT/预印本仅有噪音或窗滑动，无新双信源临床结论。**

## 6) previous_folder

→ [`202607/30/17`](../17/)

## 7) 预印本观察（未同行评议）

1. SEEN bioRxiv：[10.64898/2026.07.13.738237](https://doi.org/10.64898/2026.07.13.738237) — HCC/ICC 谱系机制
2. NEW bioRxiv（降权）：[10.64898/2026.07.28.741157](https://doi.org/10.64898/2026.07.28.741157) — hiPSC 肝类器官 vs liver-on-chip
3. SEEN EPMC：[10.21203/rs.3.rs-10395965/v1](https://doi.org/10.21203/rs.3.rs-10395965/v1) — 机器人肝切除学习曲线
4. SEEN EPMC：[10.20944/preprints202607.2078.v1](https://doi.org/10.20944/preprints202607.2078.v1) — HepG2 体外细胞毒
5. OpenAlex preprint（7d）主题过滤集合同 17h（NEW DOI=0）；medRxiv 主题命中：0（NSCLC 已剔）
