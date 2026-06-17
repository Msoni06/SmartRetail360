# SmartRetail360 – Retail Analytics Platform

## End-to-End Retail Analytics Platform using SQL, Python, Machine Learning and Power BI

![Dashboard Preview](images/executive_dashboard.png)

---

## Project Overview

SmartRetail360 is an end-to-end Retail Analytics Platform built using SQL, Python, Machine Learning, PostgreSQL, and Power BI.

The project analyzes over 100,000+ retail transactions to uncover customer behavior, sales trends, product performance, and regional insights. The platform follows a real-world analytics workflow including:

- Data Engineering
- Data Warehousing
- Exploratory Data Analysis
- Business Intelligence
- Machine Learning
- Executive Dashboarding

---

## Business Problem

Retail organizations generate massive amounts of transactional data every day. Without proper analytics, businesses struggle to:

- Identify high-performing products
- Understand customer purchasing behavior
- Monitor regional sales performance
- Detect sales trends and seasonality
- Improve customer retention
- Make data-driven decisions

SmartRetail360 addresses these challenges through an integrated analytics solution.

---

## Dataset

**Source:** Olist Brazilian E-Commerce Dataset

Dataset Link:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

### Records Analyzed

| Metric | Count |
|----------|----------|
| Orders | 100,000+ |
| Customers | 96,000+ |
| Products | 32,000+ |
| Sellers | 3,000+ |
| Reviews | 100,000+ |

---

# Technology Stack

## Programming

- Python
- SQL

## Data Analysis

- Pandas
- NumPy

## Data Visualization

- Power BI
- Matplotlib

## Machine Learning

- Scikit-Learn

## Database

- PostgreSQL

## Development Tools

- VS Code
- Git
- GitHub

---

# Project Architecture

```text
Raw Data
    │
    ▼
Data Cleaning
    │
    ▼
Feature Engineering
    │
    ▼
PostgreSQL Data Warehouse
    │
    ▼
Business Analytics
    │
    ▼
Machine Learning Models
    │
    ▼
Power BI Executive Dashboard
```

---

# Project Workflow

### Phase 1 – Data Engineering

- Data extraction
- Data cleaning
- Missing value handling
- Data transformation
- Feature creation

### Phase 2 – Data Warehouse

- Star Schema Design
- Fact Table Creation
- Dimension Tables
- PostgreSQL Loading

### Phase 3 – Analytics

- Revenue Analysis
- Product Analysis
- Customer Analysis
- Regional Analysis

### Phase 4 – Machine Learning

#### Churn Prediction

- Customer feature engineering
- Classification modeling
- Churn scoring

#### Sales Forecasting

- Historical sales analysis
- Revenue forecasting
- Trend prediction

### Phase 5 – Business Intelligence

- KPI Monitoring
- Executive Dashboard
- Interactive Reporting

---

# Key Features

## Sales Analytics

- Revenue Tracking
- Order Monitoring
- Average Order Value Analysis
- Freight Cost Analysis

## Customer Analytics

- Customer Distribution Analysis
- Regional Customer Insights
- Review Score Analysis

## Product Analytics

- Product Category Performance
- Top Revenue Generating Products
- Product Trend Analysis

## Geographic Analytics

- State-wise Revenue Analysis
- Seller Distribution Analysis
- Regional Performance Monitoring

## Machine Learning

- Customer Churn Prediction
- Sales Forecasting

---

# Executive Dashboard

The Power BI dashboard provides interactive business insights through KPIs, charts, maps, and filters.

---

## KPI Cards

| KPI | Value |
|------|------|
| Total Revenue | 20.42M |
| Total Orders | 99K |
| Average Order Value | 206.93 |
| Average Review Score | 4.03 |
| Total Freight | 2.26M |

---

## Dashboard Visualizations

### Revenue Analysis

- Revenue by Month and Year
- Revenue Trends

### Geographic Analysis

- Revenue by State Map
- Top States Revenue

### Customer Analytics

- Customer Distribution Treemap

### Product Analytics

- Best Performing Product Categories

### Seller Analytics

- Top Seller Regions

---

## Interactive Filters

- Year
- Month
- State

---

# Dashboard Preview

![Executive Dashboard](images/executive_dashboard.png)

---

# Project Structure

```text
SmartRetail360
│
├── dashboard/
│   └── SmartRetail360.pbix
│
├── docs/
│   ├── SmartRetail360 Retail Analytics Platform.docx
│   └── SmartRetail360 Retail Analytics Platform.pdf
│
├── images/
│   └── executive_dashboard.png
│
├── sql/
│   └── SQL Scripts
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── exports/
│
├── reports/
│   └── forecast_plot.png
│
├── src/
│   ├── etl/
│   ├── churn/
│   ├── forecasting/
│   └── analytics/
│
└── README.md
```

---

# Business Insights

### Revenue Growth

- Revenue increased significantly between 2017 and 2018.
- Strong sales growth trend observed.

### Product Performance

- cama_mesa_banho generated the highest revenue.
- Home and lifestyle categories dominated sales.

### Regional Performance

- São Paulo (SP) generated the highest overall revenue.
- Revenue distribution showed regional concentration.

### Customer Insights

- Customer concentration was highest in a few key states.
- Customer purchasing patterns varied across regions.

---

# Machine Learning Outputs

## Churn Prediction

- Customer-level churn risk scoring
- Retention opportunity identification
- Customer behavior analysis

## Sales Forecasting

- Revenue trend forecasting
- Future sales estimation
- Business planning support

---

# Business Impact

- Analyzed 100,000+ retail transactions.
- Built a PostgreSQL star-schema data warehouse.
- Developed Machine Learning models for churn prediction and sales forecasting.
- Created executive dashboards with 10+ KPIs and interactive filters.
- Enabled customer, product, seller, and regional performance analysis.
- Supported data-driven business decision making.

---

# Future Enhancements

- Advanced Time Series Forecasting
- Customer Lifetime Value Optimization
- Cloud Deployment (AWS/Azure)
- Real-Time Retail Analytics
- Automated Data Pipelines

---

# Installation

```bash
git clone https://github.com/Msoni06/SmartRetail360.git

cd SmartRetail360

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

# Author

## Milan Soni

B.Tech Computer Science Engineering

Data Analyst | SQL | Python | Power BI | Machine Learning

GitHub:
https://github.com/Msoni06

LinkedIn:
https://www.linkedin.com/in/milan-soni-3a69811ab

---

# Project Status

✅ Completed

End-to-End Retail Analytics Platform with:

- SQL Data Warehouse
- Python Analytics
- Machine Learning Models
- Power BI Dashboard
- Business Reporting
- GitHub Deployment
