# 📦 Project 5 - Shipment Analysis

## 📌 Overview

This project analyzes a real-world healthcare supply chain shipment dataset to understand shipment operations, delivery methods, vendor performance, and logistics trends.

The project covers data loading, cleaning, exploratory data analysis (EDA), visualization, and business insights using Python.

---

## 📂 Dataset

**File:** `Raw_Data.csv`

The dataset contains **10,324 shipment records** with **35 columns**, including:

- Shipment Information
- Project Codes
- Countries
- Vendors
- Shipment Modes
- Delivery Dates
- Product Groups
- Freight Cost
- Insurance
- Line Item Values

---

## 🛠 Technologies Used

- Python
- Pandas
- Matplotlib
- Pathlib

---

## 📁 Project Structure

```text
Project-5-Shipment-Analysis
│
├── README.md
│
├── data
│   ├── raw
│   │   └── Raw_Data.csv
│   └── processed
│       └── Shipment_Cleaned.csv
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
- Loaded the shipment dataset using Pandas.
- Used `pathlib` for platform-independent file paths.

### 2. Data Inspection
- Examined dataset structure.
- Reviewed column names and data types.
- Checked dataset dimensions.

### 3. Missing Value Analysis
- Identified missing values.
- Found missing values in Shipment Mode, Dosage, Insurance, Load_Date, and Source_System.

### 4. Statistical Analysis
- Calculated descriptive statistics.
- Counted unique countries, vendors, and project codes.
- Analyzed shipment modes and product groups.

### 5. Data Cleaning
- Renamed the corrupted `ID` column.
- Removed unnecessary metadata columns (`Load_Date` and `Source_System`).
- Converted shipment-related date columns to datetime format.
- Saved the cleaned dataset.

### 6. Data Visualization
Created:
- Shipment Mode Distribution
- Top Destination Countries
- Product Group Distribution
- Monthly Shipment Trend

### 7. Final Business Analysis
Generated insights for:
- Total Shipments
- Countries
- Vendors
- Project Codes
- Shipment Modes
- Product Groups
- Top Destination Countries
- Top Vendors
- Monthly Shipment Trends
- Financial Summary

---

## 📈 Key Findings

- Total Shipments: **10,324**
- Countries: **43**
- Vendors: **73**
- Project Codes: **142**
- Most Used Shipment Mode: **Air**
- Dominant Product Group: **ARV**

### Financial Summary

- Total Line Item Value: **$1,627,584,457.29**
- Average Line Item Value: **$157,650.57**
- Average Pack Price: **$21.91**
- Average Unit Price: **$0.61**

---

## 🎯 Learning Outcomes

Through this project, I learned how to:

- Perform exploratory data analysis (EDA)
- Handle missing values
- Clean real-world datasets
- Convert date columns into datetime format
- Remove irrelevant columns
- Create business visualizations
- Analyze logistics and shipment data
- Generate business insights from supply chain data

---

## 🚀 Future Improvements

- Delivery delay analysis
- Vendor performance dashboard
- Shipping cost optimization
- SQL integration
- Power BI dashboard
- Machine Learning for shipment prediction

---

## 👨‍💻 Author

**Solly**

AI Data Platform Portfolio Project