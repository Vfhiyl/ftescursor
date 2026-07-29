# 统计数据与临床试验更新

## 1. 本窗文献流统计（采集层）

| 指标 | 数值 |
|------|------|
| PubMed EDAT 命中 | **90** |
| PubMed PDAT 同窗（对照） | **18** |
| 临床向标题过滤 | **36** |
| Crossref 去重（标题关键词过滤） | **52** |
| ClinicalTrials.gov 条件相关且 LastUpdate∈近 24h | **16**（聚焦子集约 **12**） |

原始文件：`raw_pubmed.json` / `raw_crossref.json` / `raw_clinicaltrials.json`。

> 相对上一小时（UTC 03h：EDAT 90 / Crossref 57 / CT 16·12）：PubMed `EDAT` **ID 集合未变**（同日历日窗口）；Crossref 过滤后 57→52；Trials.gov 条数持平。多为索引/行政刷新，不等于新结果公布。

---

## 2. 本窗论文 / 会议中可引用的关键数字（摘录）

| 来源 | 关键统计 |
|------|----------|
| PMID 42512110 TriNetX | 匹配后 OS 16.3 vs 22.5 月；HR 0.89（0.76–1.0）；基线池 2819→PSM 1536 |
| PMID 42512363 | n=98；复合终点 12.2%；PHLF 3%；HVPG AUC 0.778 |
| PMID 42508157 OPTN | 候名单 HCC n=8358；DDL 22.4%；MP 相关中心 DDL 风险更低 |
| PMID 42512383 意大利登记 | 31 登记处 / 约 47% 人口；2018 患病 53/10 万；HCC cure prevalence 23.3% |
| PMID 42516535 日本 NCD | n=210 初次肝切除；预测死亡风险 ≥3% 与长期预后关联 |
| PMID 42508275 LI-RADS TRA | 143 灶；LR-TR Viable Se 66.3% / Sp 95.2%；+AF 后 Se 87.1% |
| PMID 42520023 | Ate-Bev n=47；中位 PFS 4.3 月 |
| PMID 42519550 | CTP-B SBRT n=31；1/2 年 LC 96%/50%；中位 OS 14 月 / PFS 9 月 |
| PMID 42517902 | n=30；可评估 24；ORR 37.5% / DCR 75% |
| PMID 42513363 | n=41 CIRT±免疫 RW |
| PMID 42518346 YFJP RCT | 可评估 135 vs 137；48 周 RFS 改善（p=0.016） |
| EMERALD-1 终局 OS（新闻层） | D+B+TACE 29.9 / D+TACE 33.6 / TACE 33.3 月；HR 1.10 / 0.93 |
| EMERALD-3（新闻层） | n=760；PFS HR 0.70；OS 未成熟 |
| Nature C-CAR031（背景，非 EDAT） | n=36；ORR 44.4%；mPFS 4.2；mOS 14.2 月 |

> 注：ACLF 移植 SR-MA（PMID 42510070）仍在窗外；数字见 `202607/29/01`。

---

## 3. ClinicalTrials.gov｜LastUpdate 2026-07-28–29（肝胆相关摘录）

完整列表见 `raw_clinicaltrials.json`。以下挑与 **HCC / 肝切除 / 胆道 / 肝移植路径** 更直接者：

### 高相关（HCC / 肝切除 / 胆道肿瘤）

| NCT | 状态 | 标题要点 |
|-----|------|----------|
| [NCT07059494](https://clinicaltrials.gov/study/NCT07059494) | RECRUITING | Atezo+Bev + Y-90 用于 HCC 肝移植场景（PHASE4） |
| [NCT07479485](https://clinicaltrials.gov/study/NCT07479485) | RECRUITING | MRG006A 联合治疗晚期 HCC（I/II） |
| [NCT06710223](https://clinicaltrials.gov/study/NCT06710223) | ACTIVE_NOT_RECRUITING | 冷冻消融 + 动脉灌注 SD-101 + Durva+Treme（PHASE1） |
| [NCT07727759](https://clinicaltrials.gov/study/NCT07727759) | NOT_YET_RECRUITING | CT 容积 + 肝血管形变预测肝切除后肝衰竭 |
| [NCT07719933](https://clinicaltrials.gov/study/NCT07719933) | COMPLETED | 术中持续特利加压素输注与术后严重并发症 |
| [NCT06066138](https://clinicaltrials.gov/study/NCT06066138) | RECRUITING | 基于 TDM 的 Atezo 给药（PHASE1） |
| [NCT07729917](https://clinicaltrials.gov/study/NCT07729917) | NOT_YET_RECRUITING | 胆道肿瘤精准整合策略伞形试验（PHASE2） |
| [NCT05727176](https://clinicaltrials.gov/study/NCT05727176) | RECRUITING | Futibatinib：FGFR2 融合/重排晚期胆管癌（PHASE2） |
| [NCT07359820](https://clinicaltrials.gov/study/NCT07359820) | RECRUITING | Lirafugratinib：非 CCA 实体瘤 FGFR2 融合/重排（PHASE2） |

### 相关但非原发 HCC（肝转移 / 肝炎等）

| NCT | 备注 |
|-----|------|
| NCT07715903 | 肝动脉灌注 Carfilzomib：肝转移瘤 |
| NCT02772003 | HCV DNA 疫苗（ACTIVE_NOT_RECRUITING） |
| NCT00034216 | 癌症患者血液采集（宽泛，弱相关） |

---

## 4. 流行病学 / 生存率数字（二手来源，慎用）

- **优先本窗注册研究**：意大利 cure fraction（PMID 42512383）有明确方法与覆盖范围。  
- 部分中文科普称中国肝癌 5 年生存率由约 12% 升至近 20%、日韩约 30–35%。此类数字**未在本窗官方登记处复核**，汇总时仅作背景假设，**不宜作为本小时核心统计结论**。优先引用指南原文与注册试验。

---

## 5. 统计解读备忘

1. **PFS 阳性 + OS 阴性/未成熟** → EMERALD-1 已示范 surrogate 失效风险；EMERALD-3 仍待成熟 OS。  
2. **RW PSM 等效**（A+B vs STRIDE）≠ 证明生物等效，只支持个体化选择。  
3. **Trials.gov “LastUpdate”** 可能只是行政更新，不等于宣布结果。  
4. Crossref `created-date` 是注册/索引时间，可能晚于或异于期刊在线首发日。  
5. 本小时 vs 03h：同一日历日 EDAT 窗口下 ID 集静止，属预期现象；勿解读为“文献枯竭”。
