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

# Read Orders table
orders_df = pd.read_sql("SELECT * FROM orders", connection)

# Convert Order Date to datetime
orders_df["Order Date"] = pd.to_datetime(orders_df["Order Date"])

# Count orders by date
orders_per_day = (
    orders_df.groupby("Order Date")
    .size()
    .sort_index()
)

# Create Line Chart
plt.figure(figsize=(12, 6))

plt.plot(
    orders_per_day.index,
    orders_per_day.values,
    linewidth=2
)

plt.title("Orders Over Time")
plt.xlabel("Order Date")
plt.ylabel("Number of Orders")

plt.xticks(rotation=45)

plt.tight_layout()

# Save Chart
plt.savefig("Project-8-Data-Visualization/charts/orders_line_chart.png")

# Show Chart
plt.show()

# Close connection
connection.close()