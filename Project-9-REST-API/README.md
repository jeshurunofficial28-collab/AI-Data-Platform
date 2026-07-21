# 🌐 Project 9 - REST API Data Analysis

## 📌 Project Overview

This project demonstrates how to retrieve data from a REST API using Python, convert the JSON response into a Pandas DataFrame, perform basic data analysis, and export the data to a CSV file.

This project is part of my AI & Data Analyst Portfolio.

---

## 🎯 Objectives

- Connect to a REST API
- Fetch JSON data using the Requests library
- Convert JSON to a Pandas DataFrame
- Analyze the dataset using Pandas
- Export the cleaned data to a CSV file

---

## 🛠️ Technologies Used

- Python
- Pandas
- Requests
- REST API
- JSON

---

## 📂 Project Structure

```
Project-9-REST-API/
│
├── data/
│
├── output/
│   └── users.csv
│
├── src/
│   ├── 01_fetch_api.py
│   ├── 02_json_to_dataframe.py
│   ├── 03_data_analysis.py
│   └── 04_export_csv.py
│
├── requirements.txt
└── README.md
```

---

## 📖 Project Workflow

### Step 1: Fetch Data from REST API

Retrieve user data from the JSONPlaceholder API.

API Used:

https://jsonplaceholder.typicode.com/users

---

### Step 2: Convert JSON to DataFrame

Convert the JSON response into a structured Pandas DataFrame for analysis.

---

### Step 3: Analyze the Data

Basic analysis includes:

- Display first 5 records
- Dataset shape
- Column names
- User names
- Email addresses

---

### Step 4: Export to CSV

Save the processed dataset as:

```
output/users.csv
```

---

## 📊 Sample Output

```
=== Data Shape ===

(10, 8)

Columns:

id
name
username
email
address
phone
website
company
```

---

## ▶️ How to Run

Install dependencies

```bash
pip install -r requirements.txt
```

Run the scripts

```bash
python src/01_fetch_api.py

python src/02_json_to_dataframe.py

python src/03_data_analysis.py

python src/04_export_csv.py
```

---

## 📚 Skills Demonstrated

- REST API Integration
- HTTP GET Requests
- JSON Processing
- Data Analysis with Pandas
- CSV Export
- Python Scripting

---

## 🚀 Future Improvements

- Handle nested JSON fields
- Add exception handling
- Create visualizations
- Connect to real-world APIs
- Store API data in SQL databases

---

## 👨‍💻 Author

Solly

AI & Data Analyst Portfolio Project