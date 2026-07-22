from pathlib import Path
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Project directory
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Dataset path
DATA_PATH = PROJECT_DIR / "data" / "sales_master_dataset.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

# Target
TARGET = "Revenue"

# Drop unwanted columns
DROP_COLUMNS = [
    "Revenue",
    "Total Profit",
    "Profit",
    "Order Number",
    "Line Item",
    "CustomerKey",
    "StoreKey",
    "ProductKey",
    "Delivery Date"
]

X = df.drop(columns=DROP_COLUMNS)
y = df[TARGET]

# Encode categorical columns
categorical_columns = X.select_dtypes(include=["object", "string"]).columns

encoder = LabelEncoder()

for column in categorical_columns:
    X[column] = encoder.fit_transform(X[column].astype(str))

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("=" * 60)
print("TRAIN TEST SPLIT")
print("=" * 60)

print(f"Training Features : {X_train.shape}")
print(f"Testing Features  : {X_test.shape}")

print(f"Training Target   : {y_train.shape}")
print(f"Testing Target    : {y_test.shape}")