import pandas as pd

data = {
    "name": ["Rafid", "Ali", "Sara", "Ahmed", "Hina"],
    "department": ["CS", "SE", "CS", "AI", "SE"],
    "cgpa": [3.5, 3.2, 3.8, 2.9, 3.6]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nShape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDescription:")
print(df.describe())