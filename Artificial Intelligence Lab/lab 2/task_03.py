marks = [70, 85, 70, 90, 85, 60, 90]

unique_marks = set(marks)

unique_marks = sorted(unique_marks, reverse=True)

duplicates = len(marks) - len(unique_marks)

print("Unique Marks:", unique_marks)
print("Duplicates Removed:", duplicates)