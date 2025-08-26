import pandas as pd

df = pd.read_csv("C:\\Users\\Acer\\OneDrive\\Desktop\\students.csv")

# view first five rows
print("First 5 rows:\n", df.head())

#info about columns
print("\nColumn Info:\n", df.info())

# Describe numeric columns
print("\nSummary statistics:\n", df.describe())

# Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# Count unique values for categorical columns
for col in df.select_dtypes(include='object'):
    print(f"\nUnique values in '{col}':\n", df[col].value_counts())