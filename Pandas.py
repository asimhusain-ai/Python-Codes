import pandas as pd
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 28, 22],
        'City': ['New York', 'San Francisco', 'Seattle']}
df = pd.DataFrame(data)
data1 = [2, 3, 4, 6, 8]
d1 = pd.Series(data1)
print("Original DataFrame:- ")
print(df)

df['Salary'] = [50000, 60000, 55000]

print("\nDataFrame with Salary:- ")
print(df,"\n")
print(d1)