from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

comparison = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Random Forest",
        "XGBoost",
        "LightGBM",
        "CatBoost"
    ],
    "MAE": [
        305.72,
        228.16,
        214.23,
        215.34,
        222.13
    ],
    "RMSE": [
        525.59,
        411.31,
        383.64,
        384.44,
        392.59
    ],
    "R2 Score": [
        0.7437,
        0.8431,
        0.8635,
        0.8629,
        0.8570
    ]
})

comparison = comparison.sort_values(
    by="R2 Score",
    ascending=False
)

print("=" * 60)
print("MODEL COMPARISON")
print("=" * 60)
print(comparison)

comparison.to_csv(
    OUTPUT_DIR / "model_comparison.csv",
    index=False
)

print("\nComparison report saved successfully!")