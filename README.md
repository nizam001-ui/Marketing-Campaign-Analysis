

# 📈 Marketing Funnel & Ad Spend ROI Dashboard

## 📑 Table of Contents

* [Project Overview](https://www.google.com/search?q=%23-project-overview)
* [Business Questions Answered](https://www.google.com/search?q=%23-business-questions-answered)
* [Data Pipeline & Methodology](https://www.google.com/search?q=%23-data-pipeline--methodology)
* [Visual Insights](https://www.google.com/search?q=%23-visual-insights)
* [Project Structure](https://www.google.com/search?q=%23-project-structure)
* [Author](https://www.google.com/search?q=%23-author)

---

## 🚀 Project Overview

Marketing departments generate vast amounts of data across multiple channels but frequently struggle to connect top-of-funnel metrics (impressions) to bottom-line impact (revenue). This project synthesizes cross-platform advertising data to build an automated diagnostic dashboard. By tracking customer acquisition pathways, this tool enables stakeholders to calculate exact Return on Ad Spend (ROAS) and optimize future marketing budgets.

## 🎯 Business Questions Answered

The objective was to identify inefficiencies in the marketing funnel and determine which advertising platforms yielded the highest net profitability by answering three core questions:

1. **Campaign Performance:** Which specific campaigns are driving the highest volume of purchases and generating the most revenue?
2. **Platform Efficiency & ROI:** What is the exact Return on Investment (ROI) for each advertising dollar spent across platforms like Google Ads, Meta, and TikTok?
3. **Funnel Conversion Rates:** Where are users dropping off in the acquisition pipeline (Impressions $\rightarrow$ Clicks $\rightarrow$ Leads $\rightarrow$ Purchases)?

## ⚙️ Data Pipeline & Methodology

### 1. Funnel Analytics (Python & Pandas)

* Extracted raw advertising logs and utilized Python (`marketing_campaign_analysis.py`) to engineer advanced conversion rate metrics.
* Programmatically calculated Click-Through Rates (CTR) and terminal purchase conversion percentages to locate pipeline drop-off points.

### 2. Profitability Aggregation (SQL)

* Aggregated spend and revenue variables to isolate the most profitable marketing initiatives.
* Established baseline ROI benchmarks across multiple digital channels prior to visual ingestion.

### 3. Visual Engineering (Power BI)

* **Funnel Visualization:** Designed a multi-variable clustered bar chart illustrating the step-by-step decay from ad impressions to final purchases.
* **Dynamic ROI Tracking:** Engineered custom DAX measures to track precise profitability percentages, visualized through campaign-specific column charts.
* **Efficiency Mapping:** Built a scatter plot correlating ad spend directly with revenue generation to rapidly identify high-efficiency platforms.

## 📊 Visual Insights

### Marketing Funnel Overview

*(Illustrating step-by-step conversion decay and platform efficiency)*




### Campaign ROI Analysis

*(Isolating highly profitable campaigns vs. underperforming ad spend)*




### Interactive Dashboard Demonstration

*(Click to view the cross-filtering capabilities by ad platform)*





[View Interactive Dashboard Demo](https://www.google.com/search?q=Media/dashboard_demo.mp4)

## 📁 Project Structure

```text
├── Data/
│   └── marketing_campaign_data.csv          # Raw marketing dataset
├── Python_Scripts/
│   └── marketing_campaign_analysis.py       # CTR and ROAS calculation logic
├── Dashboard/
│   └── marketing_campaign_data.pbix         # Power BI project file
├── Media/
│   ├── dashboard_overview.png               # UI Screenshot
│   └── campaign_roi_analysis.png            # UI Screenshot
└── README.md

```

## 👨‍💻 Author

**Nizam ud din** *B.S. Computer Science*

* Data Analyst & Visualization Expert
* Specializing in Python, SQL, and Power BI solutions.
