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

# Read Products table
products_df = pd.read_sql("SELECT * FROM products", connection)

# Create Scatter Plot
plt.figure(figsize=(8, 6))

plt.scatter(
    products_df["Unit Cost USD"],
    products_df["Unit Price USD"]
)

plt.title("Unit Cost vs Unit Price")
plt.xlabel("Unit Cost (USD)")
plt.ylabel("Unit Price (USD)")

plt.tight_layout()

# Save Chart
plt.savefig("Project-8-Data-Visualization/charts/unit_cost_vs_unit_price_scatter.png")

# Show Chart
plt.show()

# Close connection
connection.close()