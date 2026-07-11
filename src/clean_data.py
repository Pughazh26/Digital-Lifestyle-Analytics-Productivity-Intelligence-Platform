import pandas as pd

print("Loading dataset...")

# Read raw dataset
df = pd.read_csv("data/raw/digital_lifestyle_dataset.csv")

print("Original Shape:", df.shape)

# ----------------------------
# Check Missing Values
# ----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# ----------------------------
# Remove Duplicates
# ----------------------------
duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows: {duplicates}")

df = df.drop_duplicates()

# ----------------------------
# Convert Data Types
# ----------------------------
df["Date"] = pd.to_datetime(df["Date"])

numeric_cols = [
    "Age",
    "Usage_Minutes",
    "Unlock_Count",
    "Notifications",
    "Battery_Usage",
    "Sleep_Hours",
    "Steps"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# ----------------------------
# Remove Missing Values
# ----------------------------
df = df.dropna()

# ----------------------------
# Remove Invalid Records
# ----------------------------
df = df[df["Usage_Minutes"] > 0]

df = df[df["Sleep_Hours"].between(3,12)]

df = df[df["Battery_Usage"].between(1,100)]

df = df[df["Unlock_Count"] >= 0]

# ----------------------------
# Reset Index
# ----------------------------
df = df.reset_index(drop=True)

print("\nCleaned Shape:", df.shape)

# ----------------------------
# Save Clean Dataset
# ----------------------------
df.to_csv("data/cleaned/cleaned_dataset.csv", index=False)

print("\n✅ Cleaned dataset saved successfully!")