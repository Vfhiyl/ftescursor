# 统计数据与临床试验更新

## 1. 本窗文献流统计（采集层）

| 指标 | 数值 |
|------|------|
| PubMed EDAT 命中 | **119** |
| PubMed PDAT 同窗（对照） | **31** |
| 临床向标题过滤 | **77** |
| Crossref 去重（标题关键词过滤） | **84** |
| ClinicalTrials.gov 条件相关且 LastUpdate∈近 24h | **26** |

原始文件：`raw_pubmed.json` / `raw_crossref.json` / `raw_clinicaltrials.json`。

---

## 2. 本窗论文 / 会议中可引用的关键数字（摘录）

| 来源 | 关键统计 |
|------|----------|
| PMID 42512110 TriNetX | 匹配后 OS 16.3 vs 22.5 月；HR 0.89（0.76–1.0） |
| PMID 42504321 | n=553；AFP+PIVKA-II 双阳性预后最差 |
| PMID 42504325 | n=1281 BCLC 0–B；HALP 切点 47；低 HALP n=457 |
| PMID 42518346 | RCT n=300；早期 HCC 微创 ± YFJP；主要终点 RFS（48 周） |
| PMID 42505057 | Finotonlimab+Bev vs 索拉非尼；中国支付方 WTP ≈ $27,906/QALY |
| PMID 42519234 | CLEAR-2 计划 n=35（方案文，无结果） |
| PMID 42506349 | PDF/CCA SR-MA；纳入研究数有限，效应估计宜保守 |
| EMERALD-1 终局 OS（新闻层） | D+B+TACE 29.9 / D+TACE 33.6 / TACE 33.3 月；HR 1.10 / 0.93 |
| EMERALD-3（新闻层） | n=760；PFS HR≈0.70–0.71；OS 未成熟；ORR 三联 38.9% / STRIDE+TACE 40.8% / TACE 27.0%（DCO2） |

---

## 3. ClinicalTrials.gov｜LastUpdate 2026-07-27–28（肝胆相关摘录）

完整 **26** 条见 `raw_clinicaltrials.json`。以下挑与 **HCC / 肝切除 / 胆道 / 肝移植路径** 更直接者：

### 高相关（HCC / 肝切除 / 胆道肿瘤）

| NCT | 状态 | 标题要点 |
|-----|------|----------|
| [NCT07059494](https://clinicaltrials.gov/study/NCT07059494) | RECRUITING | Atezo+Bev + Y-90 用于 HCC 肝移植场景（IV 期） |
| [NCT07729618](https://clinicaltrials.gov/study/NCT07729618) | NOT_YET_RECRUITING | AI 引导不可切除 HCC 一线免疫方案选择 |
| [NCT07479485](https://clinicaltrials.gov/study/NCT07479485) | RECRUITING | MRG006A 联合治疗晚期 HCC（I/II） |
| [NCT07724951](https://clinicaltrials.gov/study/NCT07724951) | NOT_YET_RECRUITING | 多纳非尼 + PD-1/L1 + TACE 或 HAIC |
| [NCT07729592](https://clinicaltrials.gov/study/NCT07729592) | NOT_YET_RECRUITING | 达格列净加用于伴代谢综合征的不可切除 HCC（II 期） |
| [NCT06710223](https://clinicaltrials.gov/study/NCT06710223) | ACTIVE_NOT_RECRUITING | 冷冻消融 + 动脉灌注 SD-101 + Durva+Treme |
| [NCT03298451](https://clinicaltrials.gov/study/NCT03298451) | ACTIVE_NOT_RECRUITING | Durva+Treme 一线晚期 HCC（HIMALAYA 相关长期更新语境） |
| [NCT07727759](https://clinicaltrials.gov/study/NCT07727759) | NOT_YET_RECRUITING | CT 容积 + 肝血管形变预测肝切除后肝衰竭 |
| [NCT07719933](https://clinicaltrials.gov/study/NCT07719933) | COMPLETED | 术中持续特利加压素输注与术后严重并发症 |
| [NCT07729917](https://clinicaltrials.gov/study/NCT07729917) | NOT_YET_RECRUITING | 胆道肿瘤精准整合策略伞形试验（II 期） |
| [NCT05727176](https://clinicaltrials.gov/study/NCT05727176) | RECRUITING | Futibatinib：FGFR2 融合/重排晚期胆管癌 |
| [NCT07359820](https://clinicaltrials.gov/study/NCT07359820) | RECRUITING | Lirafugratinib：非 CCA 实体瘤 FGFR2 融合/重排 |
| [NCT06066138](https://clinicaltrials.gov/study/NCT06066138) | RECRUITING | 基于 TDM 的 Atezo 给药 |
| [NCT07729033](https://clinicaltrials.gov/study/NCT07729033) | NOT_YET_RECRUITING | Sacituzumab tirumotecan + 恩沃利单抗（TROP 语境探索） |
| [NCT07607769](https://clinicaltrials.gov/study/NCT07607769) | RECRUITING | MONTEROSA：意大利多中心观察——至临床肝相关结局时间 |

### 相关但非原发 HCC（肝转移 / 肝炎 / 肝损伤）

| NCT | 备注 |
|-----|------|
| NCT07715903 | 肝动脉灌注 Carfilzomib：肝转移瘤 |
| NCT06199232 | HAIC + 替雷利珠：晚期结直肠肝转移（COMPLETED） |
| NCT02772003 | HCV DNA 疫苗 |
| NCT05044819 | Epidiolex 潜在慢性肝损伤评估 |
| NCT07731373 | PCOS 相关肝脂肪变性青少年生物标志物 |
| 等 | 见 JSON |

---

## 4. 流行病学 / 生存率数字（二手来源，慎用）

部分中文科普称中国肝癌 5 年生存率由约 12% 升至近 20%、日韩约 30–35%。此类数字**未在本窗官方登记处复核**，汇总时仅作背景假设，**不宜作为本小时核心统计结论**。优先引用指南原文与注册试验。

---

## 5. 统计解读备忘

1. **PFS 阳性 + OS 阴性/未成熟** → EMERALD-1 已示范 surrogate 失效风险；EMERALD-3 仍待成熟 OS。  
2. **RW PSM 等效**（A+B vs STRIDE）≠ 证明生物等效，只支持个体化选择。  
3. **Trials.gov “LastUpdate”** 可能只是行政更新，不等于宣布结果。  
4. Crossref `created-date` 是注册/索引时间，可能晚于或异于期刊在线首发日。  
5. 本小时 EDAT **119** vs PDAT **31**：大量“可见新增”是索引/录入事件，而非全部当日正式发表。  
6. 成本效果阳性结论对药价与效用权重敏感，不能替代疗效终点审评。
