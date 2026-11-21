
import pandas as pd

names = ["Ali", "Sara", "Ahmed", "Hina"]
marks = [85, 65, 90, 55]

names.append("Usman")
marks.append(78)

students = {
    "name": names,
    "marks": marks
}

df = pd.DataFrame(students)

print(df)


print("Students who scored 70 or more:")
print(df[df["marks"] >= 70])


print("Total number of students:", len(df))
