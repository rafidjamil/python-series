students = {
    "S101": {"name": "Ali", "marks": [80, 75, 90]},
    "S102": {"name": "Ahmed", "marks": [70, 85, 80]},
    "S103": {"name": "Sara", "marks": [90, 95, 85]}
}

student_id = input("Enter student ID: ")

if student_id in students:
    print("Current marks:", students[student_id]["marks"])

    marks = []

    for i in range(3):
        mark = int(input("Enter new marks: "))
        marks.append(mark)

    students[student_id]["marks"] = marks

    print("Marks updated successfully")
else:
    print("Student not found")
    
    
    
    
highest = 0
top_student = ""

for student_id, details in students.items():
    total = sum(details["marks"])

    if total > highest:
        highest = total
        top_student = details["name"]

print("Top Student:", top_student)
print("Highest Marks:", highest)