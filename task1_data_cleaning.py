import pandas as pd

# ==========================================
# TASK 1: DATA CLEANING AND PREPROCESSING
# Dataset: Customer Personality Analysis
# Tool: Python (Pandas)
# ==========================================

# 1. Load the raw dataset
df = pd.read_csv("archive/marketing_campaign.csv", sep="\t")

print("Dataset loaded successfully!")
print("Original dataset shape:", df.shape)

# 2. Display first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# 3. Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# 4. Check duplicate rows
print("\nDuplicate rows before cleaning:")
print(df.duplicated().sum())

# 5. Remove duplicate rows
df = df.drop_duplicates()

# 6. Standardize column names
df.columns = (
    df.columns
    .str.lower()
    .str.strip()
    .str.replace(" ", "_")
)

print("\nCleaned column names:")
print(df.columns.tolist())

# 7. Convert Income to numeric
df["income"] = pd.to_numeric(df["income"], errors="coerce")

# 8. Fill missing Income values with median
df["income"] = df["income"].fillna(df["income"].median())

# 9. Convert customer date to datetime
# Original dataset uses day-month-year format
df["dt_customer"] = pd.to_datetime(
    df["dt_customer"],
    format="%d-%m-%Y",
    errors="coerce"
)

# 10. Standardize text values
df["education"] = (
    df["education"]
    .str.strip()
    .str.title()
)

df["marital_status"] = (
    df["marital_status"]
    .str.strip()
    .str.title()
)

# 11. Check date conversion
print("\nDate data type:")
print(df["dt_customer"].dtype)

# 12. Handle invalid/missing dates
# Use the most frequent valid date as a replacement
if df["dt_customer"].isnull().sum() > 0:
    date_mode = df["dt_customer"].mode()[0]
    df["dt_customer"] = df["dt_customer"].fillna(date_mode)

# 13. Final missing-value check
print("\nFinal missing values:")
print(df.isnull().sum())

# 14. Final duplicate check
print("\nFinal duplicate count:")
print(df.duplicated().sum())

# 15. Final dataset shape
print("\nFinal dataset shape:")
print(df.shape)

# 16. Final data types
print("\nFinal data types:")
print(df.dtypes)

# 17. Save cleaned dataset
df.to_csv("cleaned_customer_data.csv", index=False)

print("\n==========================================")
print("Cleaning completed successfully!")
print("Cleaned dataset saved as:")
print("cleaned_customer_data.csv")
print("==========================================")