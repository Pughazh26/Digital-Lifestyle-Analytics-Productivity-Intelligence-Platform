import pandas as pd
import numpy as np

print("Loading cleaned dataset...")

df = pd.read_csv("data/cleaned/cleaned_dataset.csv")

# -----------------------------
# Productivity Score (0-100)
# -----------------------------
df["Productivity_Score"] = np.where(
    df["App_Category"] == "Productivity",
    np.random.randint(70, 101, len(df)),
    np.random.randint(20, 70, len(df))
)

# -----------------------------
# Digital Addiction Score (0-100)
# -----------------------------
df["Digital_Addiction_Score"] = (
    (df["Usage_Minutes"] / 180) * 40 +
    (df["Unlock_Count"] / 25) * 30 +
    (df["Notifications"] / 80) * 30
)

df["Digital_Addiction_Score"] = (
    df["Digital_Addiction_Score"]
    .clip(0, 100)
    .round(1)
)

# -----------------------------
# Screen Time Category
# -----------------------------
df["Screen_Time_Category"] = pd.cut(
    df["Usage_Minutes"],
    bins=[0, 60, 120, 180],
    labels=["Low", "Medium", "High"]
)

# -----------------------------
# Sleep Category
# -----------------------------
df["Sleep_Category"] = pd.cut(
    df["Sleep_Hours"],
    bins=[0, 6, 8, 12],
    labels=["Poor", "Good", "Excellent"]
)

# -----------------------------
# User Type
# -----------------------------
df["User_Type"] = np.where(
    df["Occupation"] == "Student",
    "Student",
    "Working Professional"
)

# -----------------------------
# Save Dataset
# -----------------------------
df.to_csv(
    "data/cleaned/final_dataset.csv",
    index=False
)

print("\nFeature Engineering Completed Successfully!")
print(df.head())

print("\nFinal Shape :", df.shape)
