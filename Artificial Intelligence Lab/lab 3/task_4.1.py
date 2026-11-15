import pandas as pd
import numpy as np

data = {
    "name": ["Ali", "Sara", "Omar", "Hina", "Ahmed"],
    "age": [20, np.nan, 19, 22, np.nan],
    "city": ["Karachi", None, "Lahore", "Karachi", None]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

df["age"] = df["age"].fillna(df["age"].median())

df["city"] = df["city"].fillna("Unknown")

print("\nCleaned Data:")
print(df)