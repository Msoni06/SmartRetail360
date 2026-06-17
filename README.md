# SmartRetail360 – End-to-End Retail Analytics Platform

## Retail Analytics | Data Engineering | Machine Learning | Power BI

![Dashboard Preview](images/executive_dashboard.png)

---

## Project Overview

SmartRetail360 is an end-to-end Retail Analytics Platform built using SQL, PostgreSQL, Python, Machine Learning, and Power BI.

The project analyzes over 100,000+ e-commerce transactions from the Olist Brazilian E-Commerce Dataset to uncover customer behavior, sales trends, product performance, seller performance, and regional business insights.

The platform follows a real-world analytics workflow covering:

* Data Engineering
* Data Warehousing
* SQL Analytics
* Exploratory Data Analysis (EDA)
* Machine Learning
* Business Intelligence
* Executive Dashboarding

---

## Project Deliverables

✅ PostgreSQL Data Warehouse

✅ Star Schema Data Model

✅ ETL Data Pipelines

✅ SQL Analytics & Business Views

✅ Customer Churn Prediction

✅ Sales Forecasting

✅ Power BI Executive Dashboard

✅ Business Insights Report

✅ GitHub Documentation

---

# Business Problem

Retail businesses generate large volumes of transactional data daily. Without effective analytics, organizations struggle to:

* Identify high-performing products
* Understand customer purchasing behavior
* Track sales performance across regions
* Detect sales trends and seasonality
* Improve customer retention
* Support data-driven decision making

SmartRetail360 addresses these challenges through a centralized analytics solution.

---

# Dataset

### Source

Olist Brazilian E-Commerce Dataset

Dataset Link:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

### Records Analyzed

| Metric    | Volume   |
| --------- | -------- |
| Orders    | 100,000+ |
| Customers | 96,000+  |
| Products  | 32,000+  |
| Sellers   | 3,000+   |
| Reviews   | 100,000+ |

---

# Technology Stack

## Programming & Analytics

* Python
* SQL

## Data Analysis

* Pandas
* NumPy

## Machine Learning

* Scikit-Learn

## Visualization

* Power BI
* Matplotlib

## Database

* PostgreSQL

## Development Tools

* VS Code
* Git
* GitHub

---

# Solution Architecture

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
SQL Analytics Layer
    │
    ▼
Machine Learning Models
    │
    ▼
Power BI Executive Dashboard
```

---

# Project Workflow

## Phase 1 – Data Engineering

* Data extraction
* Data cleaning
* Missing value handling
* Data transformation
* Feature engineering
* Data quality checks

## Phase 2 – Data Warehouse

* Star Schema Design
* Dimension Tables
* Fact Tables
* Index Optimization
* SQL Views
* PostgreSQL Loading

## Phase 3 – Analytics

* Revenue Analysis
* Customer Analysis
* Product Analysis
* Regional Analysis
* Seller Performance Analysis

## Phase 4 – Machine Learning

### Customer Churn Prediction

* Customer feature engineering
* Classification modeling
* Churn scoring

### Sales Forecasting

* Historical trend analysis
* Revenue forecasting
* Future sales estimation

## Phase 5 – Business Intelligence

* KPI Monitoring
* Executive Dashboard
* Interactive Reporting
* Business Insights Generation

---

# Data Warehouse Design

The project follows a Star Schema architecture.

### Fact Table

* retail_fact_sales

### Dimension Tables

* retail_dim_customer
* retail_dim_product
* retail_dim_date
* retail_dim_region
* retail_dim_seller

### SQL Assets

Located in:

```text
database/schema/
├── 01_create_schema.sql
├── 02_dimension_tables.sql
├── 03_fact_tables.sql
├── 04_indexes.sql
└── 05_views.sql
```

---

# Key Business Insights

## Revenue Performance

* Revenue showed strong growth between 2017 and 2018.
* Significant seasonal variations were observed across months.
* Revenue concentration was observed in a few major states.

## Product Performance

* Home and lifestyle categories generated the highest revenue.
* Product category performance varied significantly.
* Top categories contributed a large share of total sales.

## Customer Insights

* Customer distribution was concentrated in key regions.
* Purchasing behavior varied across states.
* Review scores remained consistently positive.

## Regional Performance

* São Paulo (SP) generated the highest revenue.
* Regional revenue imbalance indicated market concentration.
* Seller performance differed significantly by location.

---

# Machine Learning Outputs

## Customer Churn Prediction

Objectives:

* Identify customers at risk of churn
* Improve retention efforts
* Support customer targeting strategies

Outputs:

* Customer churn scores
* Retention opportunity identification
* Customer risk segmentation

## Sales Forecasting

Objectives:

* Forecast future sales trends
* Support inventory planning
* Improve business forecasting

Outputs:

* Revenue forecasting
* Trend analysis
* Business planning support

---

# Executive Dashboard

The Power BI dashboard provides interactive business insights through KPIs, charts, maps, and filters.

## KPI Cards

| KPI                  | Value  |
| -------------------- | ------ |
| Total Revenue        | 20.42M |
| Total Orders         | 99K    |
| Average Order Value  | 206.93 |
| Average Review Score | 4.03   |
| Total Freight        | 2.26M  |

---

## Dashboard Visualizations

### Revenue Analytics

* Revenue by Month and Year
* Revenue Trend Analysis

### Geographic Analytics

* Revenue by State Map
* Top 10 States Revenue

### Customer Analytics

* Customer Distribution Treemap

### Product Analytics

* Best Performing Product Categories

### Seller Analytics

* Top Seller Regions

---

## Interactive Filters

* Year
* Month
* State

---

# Dashboard Preview

![Executive Dashboard](images/executive_dashboard.png)

---

# Sales Forecasting

Forecast generated using historical retail sales trends.

![Sales Forecast](reports/forecast_plot.png)

---

# Project Structure

```text
SmartRetail360
│
├── dashboard/
│   └── SmartRetail360.pbix
│
├── database/
│   ├── schema/
│   │   ├── 01_create_schema.sql
│   │   ├── 02_dimension_tables.sql
│   │   ├── 03_fact_tables.sql
│   │   ├── 04_indexes.sql
│   │   └── 05_views.sql
│   │
│   ├── indexes/
│   ├── procedures/
│   └── views/
│
├── docs/
│   ├── SmartRetail360 Retail Analytics Platform.docx
│   └── SmartRetail360 Retail Analytics Platform.pdf
│
├── images/
│   └── executive_dashboard.png
│
├── reports/
│   └── forecast_plot.png
│
├── data/
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

# Business Impact

* Analyzed 100,000+ retail transactions.
* Built a PostgreSQL star-schema data warehouse.
* Developed Machine Learning models for churn prediction and sales forecasting.
* Created an executive Power BI dashboard with interactive filters.
* Enabled customer, product, seller, and regional performance analysis.
* Supported data-driven decision-making through business insights.

---

# Future Enhancements

* Advanced Time Series Forecasting
* Customer Lifetime Value (CLV) Modeling
* Real-Time Retail Analytics
* Cloud Deployment (AWS/Azure)
* Automated Data Pipelines

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

End-to-End Retail Analytics Platform featuring:

* SQL Data Warehouse
* Data Engineering Pipelines
* Machine Learning Models
* Sales Forecasting
* Power BI Dashboard
* Business Reporting
* GitHub Documentation

```
```
