import pandas as pd
from pathlib import Path

base_path = Path(r"C:\Users\solly\OneDrive\Desktop\AI-Data-Platform")

datasets = {
    "Amazon Delivery": base_path / "Project-1-Amazon-Delivery" / "data" / "raw" / "amazon_delivery.csv",
    "Customer Analysis": base_path / "Project-2-Customer-Analysis" / "data" / "raw" / "customers.csv",
    "Product Analysis": base_path / "Project-3-Product-Analysis" / "data" / "raw" / "Products.csv",
    "Order Analysis": base_path / "Project-4-Orders-Analysis" / "data" / "raw" / "Sales.csv",
    "Shipment Analysis": base_path / "Project-5-Shipment-Analysis" / "data" / "raw" / "Raw_Data.csv",
}

for name, file in datasets.items():
    print(f"\n{'='*60}")
    print(name)
    print(f"{'='*60}")

    try:
        df = pd.read_csv(file)
        print(df.columns.tolist())
    except Exception as e:
        print(f"Error: {e}")