numbers = [10, 20, 30, 40, 50]

print("First item:", numbers[0])
print("Last item:", numbers[-1])
print("Middle three items:", numbers[1:4])




numbers.append(60)
numbers.remove(30)
numbers.sort()
print("Updated list:", numbers)



total = 0
largest = numbers[0]

for num in numbers:
    total = total + num

    if num > largest:
        largest = num

print("Sum:", total)
print("Largest number:", largest)