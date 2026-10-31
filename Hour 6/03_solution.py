Total_marks = int(input("what are the total marks? \n"))
if Total_marks >= 90 or Total_marks == 100:
    print("A")
elif Total_marks >= 80 or Total_marks == 89:
    print("B")
elif Total_marks >= 70 or Total_marks == 79:
    print("C")
elif Total_marks >= 60 or Total_marks == 69:
    print("D")
else:
    print("F")