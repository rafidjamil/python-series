import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"

df = pd.read_csv(url)

print("Dataset Shape:")
print(df.shape)

print("\nFirst Five Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nDataset Description:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

df["age"] = df["age"].fillna(df["age"].median())

df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

df = df.drop(columns=["deck"])

print("\nCleaned Data:")
print(df.isnull().sum())

print("\n1. Number of Passengers:")
print(df["survived"].value_counts())

print("\n2. Survival Percentage:")
print(df["survived"].mean() * 100)

print("\n3. Survival Rate by Sex:")
print(df.groupby("sex")["survived"].mean())

print("\n4. Survival Rate by Ticket Class:")
print(df.groupby("pclass")["survived"].mean())

print("\n5. Average Fare Per Class:")
print(df.groupby("pclass")["fare"].mean())

print("\n6. Five Oldest Passengers:")
print(df.sort_values("age", ascending=False).head(5)[["sex", "age", "pclass", "survived"]])

print("\n7. Children Under 12 Who Survived:")
children = df[(df["age"] < 12) & (df["survived"] == 1)]

print(len(children))