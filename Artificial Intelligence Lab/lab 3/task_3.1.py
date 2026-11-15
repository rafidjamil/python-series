import pandas as pd

data = {
    "name": ["Rafid", "Ali", "Sara", "Ahmed", "Hina"],
    "department": ["CS", "SE", "CS", "AI", "SE"],
    "cgpa": [3.5, 3.2, 3.8, 2.9, 3.6]
}

df = pd.DataFrame(data)

print("Students with CGPA above 3.0:")
print(df[df["cgpa"] > 3.0])

df = df.sort_values("cgpa", ascending=False)

print("\nStudents Sorted by CGPA:")
print(df)

df["honors"] = df["cgpa"] >= 3.5

print("\nFinal DataFrame:")
print(df)