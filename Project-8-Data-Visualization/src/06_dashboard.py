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

# -----------------------------
# Load Data
# -----------------------------
customers_df = pd.read_sql("SELECT * FROM customers", connection)
orders_df = pd.read_sql("SELECT * FROM orders", connection)
amazon_df = pd.read_sql("SELECT * FROM amazon", connection)
products_df = pd.read_sql("SELECT * FROM products", connection)

# -----------------------------
# Prepare Data
# -----------------------------

# Customer Gender
gender_count = customers_df["gender"].value_counts()

# Orders Over Time
orders_df["Order Date"] = pd.to_datetime(orders_df["Order Date"])
orders_per_day = (
    orders_df.groupby("Order Date")
    .size()
    .sort_index()
)

# -----------------------------
# Create Dashboard
# -----------------------------
fig = plt.figure(figsize=(16,10))
fig.suptitle(
    "Business Performance Dashboard",
    fontsize=20,
    fontweight="bold",
    color="darkblue"
)

# ==========================================================
# 1. Customer Gender Distribution
# ==========================================================
plt.subplot(2,2,1)

bars = plt.bar(
    gender_count.index,
    gender_count.values,
    color=["royalblue","orange","green"]
)

plt.title("Customer Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Customers")
plt.grid(axis="y", linestyle="--", alpha=0.4)

# Show values on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x()+bar.get_width()/2,
        height,
        int(height),
        ha="center",
        va="bottom",
        fontsize=10
    )

# ==========================================================
# 2. Orders Over Time
# ==========================================================
plt.subplot(2,2,2)

plt.plot(
    orders_per_day.index,
    orders_per_day.values,
    color="red",
    linewidth=2.5,
    marker="o",
    markersize=4
)

plt.title("Orders Over Time")
plt.xlabel("Order Date")
plt.ylabel("Orders")
plt.grid(True, linestyle="--", alpha=0.4)
plt.xticks(rotation=45)

# ==========================================================
# 3. Delivery Time Distribution
# ==========================================================
plt.subplot(2,2,3)

plt.hist(
    amazon_df["Delivery_Time"],   # Change this if your column name differs
    bins=12,
    color="skyblue",
    edgecolor="black"
)

plt.title("Delivery Time Distribution")
plt.xlabel("Delivery Time (Days)")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.4)

# ==========================================================
# 4. Unit Cost vs Unit Price
# ==========================================================
plt.subplot(2,2,4)

plt.scatter(
    products_df["Unit Cost USD"],
    products_df["Unit Price USD"],
    color="purple",
    alpha=0.6,
    s=35
)

plt.title("Unit Cost vs Unit Price")
plt.xlabel("Unit Cost (USD)")
plt.ylabel("Unit Price (USD)")
plt.grid(True, linestyle="--", alpha=0.4)

# -----------------------------
# Layout
# -----------------------------
plt.tight_layout(rect=[0,0,1,0.95])

# Save Dashboard
plt.savefig(
    "Project-8-Data-Visualization/charts/business_dashboard.png",
    dpi=300
)

# Show Dashboard
plt.show()

connection.close()