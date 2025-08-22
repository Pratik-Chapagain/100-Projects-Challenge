import pandas as pd

df = pd.read_csv("C:\\Users\\Acer\\Downloads\\employees_day5.csv")

print("Our datafrane------", df)


#Show the first 5 rows
print(df.head(5))

#how many employees are there in total
print(len(df))

#what are the unique values in the region and department columns
print(df['Region'].unique())
print(df['Department'].unique())

#emloyees with salary greater than 60,000
print(df[df['Salary'] > 60000])

#employess in the IT department with more than 5 years of experience
print(df[(df['Department'] == 'IT') & (df['Experience'] > 5)])

#employees whose bonuspercent is missing
print(df[df['BonusPercent'].isna()])

#Average salary per department
print(df.groupby('Department')['Salary'].mean())

#Maximum experience per region
print(df.groupby('Region')['Experience'].max())

#Total salary expense per Region and Department
print(df.groupby(['Region', 'Department'])['Salary'].sum())