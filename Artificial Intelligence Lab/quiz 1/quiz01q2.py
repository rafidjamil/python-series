
import pandas as pd

names = ["Ali", "Sara", "Ahmed", "Hina"]
marks = [85, 65, 90, 55]


filteredmarks = [mark for mark in marks if mark >= 50]


print("marks greater or equal to 50:")
print(filteredmarks)


data = {
    "names": names,
    "marks": marks
}
df = pd.DataFrame(data)
print("First two rows:")
print(df.head(2))


dfsort = df.sort_values(by="marks", ascending=False)


print("sort dataframe in descending order:")
print(dfsort)























