# 📊 Project 10 – Feature Engineering Pipeline

> "Commit to the Lord whatever you do, and He will establish your plans."
>
> **Proverbs 16:3**

---

# 📖 Project Overview

This project demonstrates a complete **Feature Engineering and Data Preparation Pipeline** for a retail sales analytics use case.

The objective was to transform raw datasets into clean, business-ready datasets that can be used for:

- Business Intelligence
- Data Analysis
- Machine Learning
- Dashboard Development
- Predictive Analytics

The project follows a real-world ETL workflow including data cleaning, feature engineering, dataset integration, exploratory data analysis, visualization, and validation.

---

# 🎯 Objectives

- Load multiple raw datasets
- Clean inconsistent and missing data
- Engineer new business features
- Merge related datasets
- Generate business metrics
- Perform exploratory data analysis (EDA)
- Create business visualizations
- Validate the final dataset
- Produce a machine learning-ready dataset

---

# 📂 Project Structure

```
Project-10-Feature-Engineering/
│
├── data/
│   ├── raw/
│   └── clean/
│
├── notebooks/
│   ├── load_data.py
│   ├── data_overview.py
│   ├── data_types.py
│   ├── master_schema.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── create_sales_dataset.py
│   ├── eda_summary.py
│   ├── data_visualization.py
│   └── data_validation.py
│
├── output/
│   ├── sales_master_dataset.csv
│   ├── amazon_features.csv
│   ├── customer_features.csv
│   ├── order_features.csv
│   ├── product_features.csv
│   ├── shipment_features.csv
│   └── charts/
│
├── sql/
│
├── requirements.txt
└── README.md
```

---

# 📊 Datasets Used

### 1. Amazon Delivery Dataset

Used for delivery performance analysis.

Features include:

- Delivery Time
- Agent Rating
- Weather
- Traffic
- Vehicle
- Area

---

### 2. Customer Dataset

Used for customer information.

Features include:

- Customer Details
- Registration Date
- Preferred Channel

---

### 3. Product Dataset

Used for product information.

Features include:

- Product Name
- Brand
- Category
- Unit Cost
- Unit Price

---

### 4. Orders Dataset

Used for sales transactions.

Features include:

- Order Number
- ProductKey
- Quantity
- Currency
- CustomerKey

---

### 5. Shipment Dataset

Used for logistics and shipment analysis.

Features include:

- Shipment Mode
- Vendor
- Country
- Product Group
- Freight Cost

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- VS Code
- Git
- GitHub

---

# 🔄 Project Workflow

## Step 1

Load all raw datasets.

---

## Step 2

Inspect

- Data Types
- Missing Values
- Duplicate Records

---

## Step 3

Clean the data

- Remove duplicates
- Handle missing values
- Convert data types
- Prepare numerical columns

---

## Step 4

Feature Engineering

Created new business features including:

- Fast Delivery
- High Rated Agent
- Age Group
- Profit
- Large Order
- High Value Shipment

---

## Step 5

Dataset Integration

Merged:

Orders Dataset

+

Products Dataset

using

ProductKey

Result:

```
sales_master_dataset.csv
```

---

## Step 6

Business Metrics

Created

- Revenue
- Total Profit

---

## Step 7

Exploratory Data Analysis

Performed:

- Summary Statistics
- Missing Value Analysis
- Brand Analysis
- Category Analysis
- Revenue Analysis
- Profit Analysis

---

## Step 8

Visualization

Generated charts:

- Top Categories by Revenue
- Top Brands by Profit
- Quantity Distribution

---

## Step 9

Validation

Validated:

- Duplicate Records
- Missing Values
- Revenue Calculation
- Profit Calculation

---

# 📈 Final Dataset

```
sales_master_dataset.csv
```

Rows

```
62,884
```

Columns

```
22
```

Business Metrics

- Revenue
- Profit
- Total Profit
- Large Order

---

# 📊 Output

Generated files

```
sales_master_dataset.csv

amazon_features.csv

customer_features.csv

order_features.csv

product_features.csv

shipment_features.csv
```

Generated Charts

- Top Categories by Revenue
- Top Brands by Profit
- Quantity Distribution

---

# 💡 Key Skills Demonstrated

- Data Cleaning
- Feature Engineering
- Data Validation
- Data Integration
- Exploratory Data Analysis
- Business Analytics
- Data Visualization
- Python Programming
- ETL Pipeline Development

---

# 🚀 Future Improvements

- Build Machine Learning models
- Deploy predictive models
- Automate ETL pipeline
- Add Power BI dashboard
- Cloud deployment using Azure or AWS

---

# 🙏 Acknowledgement

This project was completed as part of my journey toward becoming a professional Data Analyst and Machine Learning Engineer.

Every challenge during development helped strengthen my understanding of data preparation, debugging, and feature engineering.

---

# 👨‍💻 Author

**Solly**

Aspiring Data Analyst | Machine Learning Enthusiast
