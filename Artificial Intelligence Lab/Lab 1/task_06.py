num = int(input("Enter an integer: "))

if num > 0:
    print("Number is Positive")

    if num % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")

elif num < 0:
    print("Number is Negative")

else:
    print("Number is Zero")