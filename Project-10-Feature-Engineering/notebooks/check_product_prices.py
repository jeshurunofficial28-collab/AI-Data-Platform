import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CLEAN = BASE_DIR / "data" / "clean"

products = pd.read_csv(CLEAN / "products_clean.csv")

print(products[["Unit Cost USD", "Unit Price USD"]].head(20))