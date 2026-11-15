import numpy as np

marks = np.array([78, 85, 92, 64, 71, 88, 95, 59, 82, 76])

mean_marks = np.mean(marks)
highest_marks = np.max(marks)
lowest_marks = np.min(marks)
std_dev = np.std(marks)

above_mean = np.sum(marks > mean_marks)

print("Student Marks:", marks)
print(f"Mean: {mean_marks:.2f}")
print("Highest:", highest_marks)
print("Lowest:", lowest_marks)
print(f"Standard Deviation: {std_dev:.2f}")
print("Students scoring above mean:", above_mean)
