import pandas as pd
import numpy as np

messy_data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106],
    'Name': ['Ahmed', 'Zara', 'Kamran', 'Nida', 'Tariq', 'Sana'],
    'Department': ['IT', 'HR', np.nan, 'IT', 'Finance', np.nan],
    'Salary': [65000, np.nan, 72000, 68000, np.nan, 75000]
}
df = pd.DataFrame(messy_data)

print("Missing Values Count:")
print(df.isnull().sum())

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])

print("\nCleaned Table:")
print(df)
