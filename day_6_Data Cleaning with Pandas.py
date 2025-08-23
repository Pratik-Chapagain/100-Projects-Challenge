import pandas as pd

#load dataset
df = pd.read_csv("C:\\Users\\Acer\\Downloads\\employees_day5.csv")
print(df.head())

#count missing values per column
print(df.isna().sum())

# non-null values + datatypes
print(df.info())


#fill missing values 
df['BonusPercent'] = df['BonusPercent'].fillna(0)
print(df['BonusPercent'])

# Drop rows with missing values
df_cleaned = df.dropna()

# fill with mean/median (numeric) or mode (categorical)
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])

#find duplicates
duplicates = df[df.duplicated()]
print(duplicates)

#remove duplicates
df_no_duplicates = df.drop_duplicates()

