def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


def count_vowels(text):
    count = 0

    for char in text:
        if char.lower() in "aeiou":
            count += 1

    return count


print("Prime:", is_prime(7))
print("Prime:", is_prime(10))

print("Factorial:", factorial(5))
print("Factorial:", factorial(4))

print("Vowels:", count_vowels("Rafid"))
print("Vowels:", count_vowels("Python Programming"))