# # marks = [10,20,40,38,29]
# # print(marks[-3])
# # print(len(marks))

# temp = [22.5, 23.1, 24.1, 27.2, 30.5, 32.1, 31.4, 29.9, 27.5, 25.0, 23.8, 22.9]
# print(min(temp))
# print(max(temp))
# print(sum(temp))
# print(len(temp))

# print(temp[4:5])
# print(temp[-3:])

# print(temp[::2])

# print(temp[::-1])

# fahrenheit = []

# for i in temp:
#     fahrenheit.append((i * 9/5) + 32)
# print(fahrenheit)

# temp.append(26.5)

# temp.remove(min(temp))

# temp.sort(reverse=True)

# print(temp)

Students_class = {
    "S101": {"name": "Ali", "marks": [70, 80, 90]},
    "S102": {"name": "Anas", "marks": [100, 85, 90]},
    "S103": {"name": "Ahmed", "marks": [72, 75, 80]},
    "S104": {"name": "Adnan", "marks": [60, 65, 70]},
    "S105": {"name": "Afnan", "marks": [20, 30, 40]}
}
for student_id, details in Students_class.items():
    name = details["name"]
    marks = details["marks"]

    total = sum(marks)
    avg = total / len(marks)

    print("Name:", name)
    print("Total Marks:", total)
    print("Average Marks:", avg)
    print()



