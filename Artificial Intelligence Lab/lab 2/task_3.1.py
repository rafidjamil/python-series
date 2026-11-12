book = {
    "title": "Python Programming",
    "author": "John Smith",
    "year": 2020
}
print(book)



book["price"] = 1500
book["year"] = 2024
for key, value in book.items():
    print(key, ":", value)
    
    
    
key = input("Enter a key: ")

if key in book:
    print("Value:", book[key])
else:
    print("Key not found")