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

# Create Pie Chart
plt.figure(figsize=(8, 8))

plt.pie(
    gender_count.values,
    labels=gender_count.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Customer Gender Distribution")

# Save Chart
plt.savefig("Project-8-Data-Visualization/charts/customer_gender_pie_chart.png")

# Show Chart
plt.show()

# Close connection
connection.close()