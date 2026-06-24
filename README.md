# Customer Churn Prediction & Portfolio Monitoring Platform

An end-to-end customer analytics and churn prediction platform built using **Snowflake, SQL, Python, PySpark, and Power BI**. The project demonstrates how data engineering, predictive analytics, and business intelligence can be combined to identify high-risk customers, monitor portfolio health, and generate actionable business insights.

## Project Overview

Customer retention is a critical business objective across banking, telecom, insurance, and subscription-based industries. This project processes customer data, engineers predictive features, trains a churn prediction model, and visualizes key portfolio health metrics through interactive dashboards.

The solution helps answer:

* Which customers are most likely to churn?
* What factors drive customer attrition?
* How healthy is the customer portfolio?
* Which customer segments require proactive retention efforts?

---

## Business Impact

* Processed **7,043 customer records** and **15+ customer attributes**
* Achieved **79.2% churn prediction accuracy**
* Generated churn probability scores for the entire customer base
* Created dashboards tracking **12+ portfolio health KPIs**
* Enabled identification of high-risk customer segments for targeted retention campaigns

---

## Tech Stack

### Data Engineering

* Snowflake
* SQL
* Python
* PySpark

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Visualization

* Power BI

### Development Tools

* Git
* GitHub
* VS Code

---

## Architecture

```text
Raw Customer Data
        │
        ▼
    Snowflake
(Data Storage Layer)
        │
        ▼
 Feature Engineering
(SQL + Python)
        │
        ▼
  Churn Prediction
   Machine Learning
        │
        ▼
 Prediction Output
        │
        ▼
 Power BI Dashboard
```

---

## Dataset

The project uses the Telco Customer Churn dataset containing:

* Customer demographics
* Contract information
* Payment methods
* Service subscriptions
* Monthly charges
* Tenure details
* Churn labels

Dataset Size:

* Rows: 7,043
* Features: 15+
* Target Variable: Churn

---

## Key Features

### Data Validation

* Missing value checks
* Data quality validation
* Schema consistency checks

### Feature Engineering

* Tenure groups
* Revenue segmentation
* Contract risk categorization
* Payment behavior analysis

### Predictive Analytics

* Customer churn prediction
* Risk segmentation
* Probability scoring

### Business Intelligence

* Portfolio health monitoring
* Retention trend analysis
* Revenue risk tracking
* Customer segment analysis

---

## Model Performance

| Metric                 | Value |
| ---------------------- | ----- |
| Accuracy               | 79.2% |
| Records Scored         | 7,043 |
| Features Engineered    | 10+   |
| Portfolio KPIs Tracked | 12+   |

---

## Dashboard Metrics

The Power BI dashboard includes:

* Churn Rate
* Customer Retention Rate
* Revenue Risk Exposure
* Customer Segment Distribution
* Contract Type Analysis
* Tenure Analysis
* High-Risk Customer Identification
* Monthly Revenue Trends

---

## Repository Structure

```text
Customer-Churn-Prediction-Pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── sql/
│   ├── stages.sql
│   ├── tables.sql
│   └── transformations.sql
│
├── src/
│   ├── load_data.py
│   ├── train_model.py
│   ├── predict.py
│   └── validation_runner.py
│
├── dashboards/
│
├── models/
│
└── README.md
```

---

## Key Learnings

* Building scalable analytics pipelines with Snowflake
* Feature engineering for customer analytics
* Machine learning model development and evaluation
* Data quality management and validation
* Dashboard design for business stakeholders
* Portfolio health monitoring and risk analysis

---

## Future Enhancements

* Real-time scoring pipeline
* Automated retraining workflow
* Snowflake Tasks & Streams integration
* Advanced ensemble models
* Customer lifetime value prediction
* Marketing campaign optimization analytics

---

## Author

**Anuja Ingale**

Business Analyst | Data Analytics | SQL | Python | Snowflake | Power BI

GitHub: https://github.com/anujaingale41-lab