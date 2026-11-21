def mean(data):
    return sum(data) / len(data)

def maximum(data):
    largest = data[0]
    for num in data[1:]:
        if num > largest:
            largest = num
    return largest

def minimum(data):
    smallest = data[0]
    for num in data[1:]:
        if num < smallest:
            smallest = num
    return smallest

numbers = [42, 18, 75, 29, 91, 54, 63, 37]
print("Dataset:", numbers)
print(f"Mean: {mean(numbers):.2f}")
print("Maximum:", maximum(numbers))
print("Minimum:", minimum(numbers))
