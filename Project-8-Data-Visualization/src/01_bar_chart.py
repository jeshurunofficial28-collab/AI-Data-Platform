import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ai_data_platform"
)

# Read Customers table
customers_df = pd.read_sql("SELECT * FROM customers", connection)

# Count customers by gender
gender_count = customers_df["gender"].value_counts()

# Create Bar Chart
plt.figure(figsize=(8,5))

plt.bar(gender_count.index, gender_count.values)

plt.title("Customer Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")

plt.tight_layout()

# Save Chart
plt.savefig("Project-8-Data-Visualization/charts/customer_gender_bar_chart.png")

# Show Chart
plt.show()

connection.close()