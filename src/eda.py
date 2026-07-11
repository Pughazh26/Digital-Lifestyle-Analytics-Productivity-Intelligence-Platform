from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "cleaned" / "cleaned_dataset.csv"
FALLBACK_INPUT_FILE = ROOT / "data" / "cleaned" / "digital_lifestyle_cleaned.csv"
IMAGE_DIR = ROOT / "images"


print("Loading cleaned dataset...")

input_file = INPUT_FILE if INPUT_FILE.exists() else FALLBACK_INPUT_FILE
df = pd.read_csv(input_file)
df.columns = df.columns.str.strip().str.lower()
df["date"] = pd.to_datetime(df["date"])

print("Dataset Loaded Successfully!")
print(df.shape)

IMAGE_DIR.mkdir(exist_ok=True)

# Daily Screen Time Trend
daily = df.groupby("date")["usage_minutes"].sum()

plt.figure(figsize=(14, 5))
daily.plot()
plt.title("Daily Screen Time")
plt.xlabel("Date")
plt.ylabel("Usage Minutes")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "daily_screen_time.png")
plt.close()

print("Daily Screen Time Chart Saved")

# Top 10 Apps
top_apps = (
    df.groupby("app_name")["usage_minutes"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
top_apps.plot(kind="bar")
plt.title("Top 10 Apps by Usage")
plt.ylabel("Usage Minutes")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "top_apps.png")
plt.close()

print("Top Apps Chart Saved")

# App Category Distribution
category = df.groupby("app_category")["usage_minutes"].sum()

plt.figure(figsize=(8, 8))
category.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("App Category Distribution")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "category_distribution.png")
plt.close()

print("Category Chart Saved")

# Sleep Hours Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["sleep_hours"], bins=20)
plt.title("Sleep Hours Distribution")
plt.xlabel("Hours")
plt.ylabel("Users")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "sleep_distribution.png")
plt.close()

print("Sleep Distribution Saved")

# Weekend vs Weekday
day = df.groupby("day_type")["usage_minutes"].sum()

plt.figure(figsize=(6, 5))
day.plot(kind="bar")
plt.title("Weekend vs Weekday Usage")
plt.ylabel("Usage Minutes")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "weekend_vs_weekday.png")
plt.close()

print("Weekend Chart Saved")

print("\n========= SUMMARY =========")
print("Average Usage :", round(df["usage_minutes"].mean(), 2))
print("Average Sleep :", round(df["sleep_hours"].mean(), 2))
print("Average Notifications :", round(df["notifications"].mean(), 2))
print("Average Unlocks :", round(df["unlock_count"].mean(), 2))

print("\nEDA Completed Successfully!")
