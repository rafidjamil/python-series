def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(10))
print(is_even(7))



def average(numbers):
    total = 0

    for num in numbers:
        total = total + num

    return total / len(numbers)

print(average([10, 20, 30]))
print(average([40, 50, 60]))




cube = lambda n: n ** 3

print(cube(3))
print(cube(5))