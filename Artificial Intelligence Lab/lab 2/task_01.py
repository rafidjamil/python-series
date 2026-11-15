shopping_list = []

for i in range(5):
    item = input("Enter an item: ")
    shopping_list.append(item)

shopping_list.sort()

print("Shopping List:", shopping_list)
print("Total Items:", len(shopping_list))