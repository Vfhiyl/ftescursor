# 统计数据与临床试验更新

## 1. 本窗文献流统计（采集层）

| 指标 | 数值 |
|------|------|
| PubMed EDAT 命中 | 75 |
| PubMed PDAT 同窗（对照） | 23 |
| 临床向标题过滤 | 17 |
| Crossref 去重（标题关键词过滤） | 69 |
| ClinicalTrials.gov 条件相关且 LastUpdate∈近 24h | 27 |

原始文件：`raw_pubmed.json` / `raw_crossref.json` / `raw_clinicaltrials.json`。

---

## 2. 本窗论文中可引用的关键数字（摘录）

| 来源 | 关键统计 |
|------|----------|
| PMID 42512110 TriNetX | 匹配后 OS 16.3 vs 22.5 月；HR 0.89（0.76–1.0）；基线池 2819→PSM 1536 |
| PMID 42512363 | n=98；复合终点 12.2%；PHLF 3%；HVPG AUC 0.778 |
| PMID 42504321 | n=553；AFP+PIVKA-II 双阳性预后最差 |
| PMID 42504325 | n=1281 BCLC 0–B；HALP 切点 47 |
| PMID 42517902 | n=30；ORR 37.5%；DCR 75%（小样本） |
| PMID 42513363 | n=41 CIRT±免疫 RW |
| EMERALD-3（新闻层） | n=760；PFS HR 0.70；OS 未成熟 |

---

## 3. ClinicalTrials.gov｜LastUpdate 2026-07-27–28（肝胆相关摘录）

完整 27 条见 `raw_clinicaltrials.json`。以下挑与 **HCC / 肝切除 / 胆道 / 肝移植路径** 更直接者：

### 高相关（HCC / 肝切除 / 胆道肿瘤）

| NCT | 状态 | 标题要点 |
|-----|------|----------|
| [NCT07059494](https://clinicaltrials.gov/study/NCT07059494) | RECRUITING | Atezo+Bev + Y-90 用于 HCC 肝移植场景 |
| [NCT07729618](https://clinicaltrials.gov/study/NCT07729618) | NOT_YET_RECRUITING | AI 引导不可切除 HCC 一线免疫方案选择 |
| [NCT07479485](https://clinicaltrials.gov/study/NCT07479485) | RECRUITING | MRG006A 联合治疗晚期 HCC（I/II） |
| [NCT07724951](https://clinicaltrials.gov/study/NCT07724951) | NOT_YET_RECRUITING | 多纳非尼 + PD-1/L1 + TACE 或 HAIC |
| [NCT07729592](https://clinicaltrials.gov/study/NCT07729592) | NOT_YET_RECRUITING | 达格列净加用于伴代谢综合征的不可切除 HCC |
| [NCT06710223](https://clinicaltrials.gov/study/NCT06710223) | ACTIVE_NOT_RECRUITING | 冷冻消融 + 动脉灌注 SD-101 + Durva+Treme |
| [NCT03298451](https://clinicaltrials.gov/study/NCT03298451) | ACTIVE_NOT_RECRUITING | Durva+Treme 一线晚期 HCC（HIMALAYA 相关长期更新语境） |
| [NCT07727759](https://clinicaltrials.gov/study/NCT07727759) | NOT_YET_RECRUITING | CT 容积 + 肝血管形变预测肝切除后肝衰竭 |
| [NCT07719933](https://clinicaltrials.gov/study/NCT07719933) | COMPLETED | 术中持续特利加压素输注与术后严重并发症 |
| [NCT07729917](https://clinicaltrials.gov/study/NCT07729917) | NOT_YET_RECRUITING | 胆道肿瘤精准整合策略伞形试验 |
| [NCT05727176](https://clinicaltrials.gov/study/NCT05727176) | RECRUITING | Futibatinib：FGFR2 融合/重排晚期胆管癌 |
| [NCT07359820](https://clinicaltrials.gov/study/NCT07359820) | RECRUITING | Lirafugratinib：非 CCA 实体瘤 FGFR2 融合/重排 |

### 相关但非原发 HCC（肝转移 / 肝炎 / 肝损伤）

| NCT | 备注 |
|-----|------|
| NCT07715903 | 肝动脉灌注 Carfilzomib：肝转移瘤 |
| NCT06199232 | HAIC + 替雷利珠：晚期结直肠肝转移 |
| NCT02772003 | HCV DNA 疫苗 |
| NCT05044819 | Epidiolex 潜在慢性肝损伤评估 |
| 等 | 见 JSON |

---

## 4. 流行病学 / 生存率数字（二手来源，慎用）

部分中文科普称中国肝癌 5 年生存率由约 12% 升至近 20%、日韩约 30–35%。此类数字**未在本窗官方登记处复核**，汇总时仅作背景假设，**不宜作为本小时核心统计结论**。优先引用指南原文与注册试验。

---

## 5. 统计解读备忘

1. **PFS 阳性 + OS 未成熟** → 可改变讨论，慎改指南措辞。  
2. **RW PSM 等效**（A+B vs STRIDE）≠ 证明生物等效，只支持个体化选择。  
3. **Trials.gov “LastUpdate”** 可能只是行政更新，不等于宣布结果。  
4. Crossref `created-date` 是注册/索引时间，可能晚于或异于期刊在线首发日。
