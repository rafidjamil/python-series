age = int(input("Provide me an age: \n"))
if age < 13:
    print("child")
elif age < 20:
    print("teen")
elif age < 59:
    print("adult")
else:
    print("senior")