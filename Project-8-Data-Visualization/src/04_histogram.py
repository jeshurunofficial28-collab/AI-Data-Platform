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

# Read Amazon table
amazon_df = pd.read_sql("SELECT * FROM amazon", connection)

# Create Histogram
plt.figure(figsize=(10, 6))

plt.hist(
    amazon_df["Delivery_Time"],
    bins=10,
    edgecolor="black"
)

plt.title("Distribution of Delivery Time")
plt.xlabel("Delivery Time (Days)")
plt.ylabel("Frequency")

plt.tight_layout()

# Save Chart
plt.savefig("Project-8-Data-Visualization/charts/delivery_time_histogram.png")

# Show Chart
plt.show()

# Close connection
connection.close()