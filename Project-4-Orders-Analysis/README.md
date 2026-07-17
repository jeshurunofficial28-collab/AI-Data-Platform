# 📦 Project 4 - Orders Analysis

## 📌 Overview

This project analyzes an orders dataset to understand customer purchasing behavior, product demand, store activity, and order trends over time.

The project demonstrates data loading, cleaning, statistical analysis, visualization, and business insights using Python and Pandas.

---

## 📂 Dataset

**File:** `Sales.csv`

The dataset contains order information including:

- Order Number
- Line Item
- Order Date
- Delivery Date
- CustomerKey
- StoreKey
- ProductKey
- Quantity
- Currency Code

---

## 🛠 Technologies Used

- Python
- Pandas
- Matplotlib
- Pathlib

---

## 📁 Project Structure

```
Project-4-Orders-Analysis
│
├── README.md
│
├── data
│   ├── raw
│   │   └── Sales.csv
│   │
│   └── processed
│       └── Sales_Cleaned.csv
│
└── src
    ├── 01_read_data.py
    ├── 02_data_info.py
    ├── 03_missing_values.py
    ├── 04_statistics.py
    ├── 05_data_cleaning.py
    ├── 06_visualization.py
    └── 07_final_analysis.py
```

---

## 📊 Analysis Performed

### 1. Data Loading
- Loaded the dataset using Pandas.
- Used `pathlib` for cross-platform file handling.

### 2. Data Inspection
- Displayed dataset information.
- Checked rows, columns, and data types.

### 3. Missing Value Analysis
- Identified missing values.
- Found missing values only in the **Delivery Date** column.

### 4. Statistical Analysis
- Generated descriptive statistics.
- Counted unique customers, products, and stores.
- Analyzed currency distribution.

### 5. Data Cleaning
- Converted **Order Date** to datetime.
- Converted **Delivery Date** to datetime.
- Saved the cleaned dataset.

### 6. Data Visualization
Created:
- Orders by Currency (Bar Chart)
- Quantity Distribution (Histogram)
- Monthly Orders Trend (Line Chart)

### 7. Final Business Analysis
Calculated:

- Total Orders
- Total Quantity Sold
- Average Quantity per Order
- Unique Customers
- Unique Products
- Unique Stores
- Currency Distribution
- Top 10 Ordered Products
- Monthly Order Trends

---

## 📈 Key Findings

- Total Orders: **62,884**
- Total Quantity Sold: **197,757**
- Average Quantity per Order: **3.14**
- Unique Customers: **11,887**
- Unique Products: **2,492**
- Unique Stores: **58**
- Dataset covers **62 months** (January 2016 – February 2021).
- USD is the most frequently used currency.

---

## 🎯 Learning Outcomes

Through this project, I learned how to:

- Load datasets using Pandas.
- Inspect and understand dataset structure.
- Detect missing values.
- Generate descriptive statistics.
- Convert string columns to datetime.
- Save cleaned datasets.
- Create business visualizations using Matplotlib.
- Perform exploratory data analysis (EDA).
- Summarize business insights from transactional order data.

---

## 🚀 Future Improvements

- Analyze delivery performance.
- Calculate delivery times.
- Build interactive dashboards using Power BI.
- Develop sales forecasting models using Machine Learning.
- Integrate with SQL databases for advanced analytics.

---

## 👨‍💻 Author

**Solly**

AI Data Platform Portfolio Project