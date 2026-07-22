import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ======================================
# Paths
# ======================================
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT = BASE_DIR / "output"
CHARTS = OUTPUT / "charts"

CHARTS.mkdir(exist_ok=True)

# ======================================
# Load Sales Dataset
# ======================================
sales = pd.read_csv(OUTPUT / "sales_master_dataset.csv")

# ======================================
# Top 10 Categories
# ======================================
category_sales = (
    sales.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
category_sales.plot(kind="bar")
plt.title("Top 10 Categories by Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(CHARTS / "top_categories_revenue.png")
plt.close()

# ======================================
# Top 10 Brands
# ======================================
brand_profit = (
    sales.groupby("Brand")["Total Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
brand_profit.plot(kind="bar")
plt.title("Top 10 Brands by Profit")
plt.xlabel("Brand")
plt.ylabel("Profit")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(CHARTS / "top_brands_profit.png")
plt.close()

# ======================================
# Quantity Distribution
# ======================================
plt.figure(figsize=(8, 5))
sales["Quantity"].hist(bins=10)
plt.title("Order Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(CHARTS / "quantity_distribution.png")
plt.close()

print("=" * 60)
print("✅ VISUALIZATIONS CREATED")
print("=" * 60)
print("Charts saved to:")
print(CHARTS)