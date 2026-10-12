# age = int(input("Whats your age: \n"))
# date = str(input("What date is it: \n"))
# if age >= 18 and date == "wed":
#     print("Please pay $",12 - 2)
# elif age >= 18:
#     print("Please pay $12")
# elif age < 18 and date == "wed":
#     print("Please pay $",8 - 2)
# elif age < 18:
#     print("Please pay $8")

age = int(input("whats your age"))
day = input("whats day: ")

price = 12 if age >= 18 else 8


if day == "Wednesday":
    price = price - 2

    # price -= 2

print("Ticket price for you is $",price)