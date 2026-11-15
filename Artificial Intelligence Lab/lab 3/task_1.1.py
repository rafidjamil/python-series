# import numpy as np

# numbers = np.arange(1, 21)

# even_numbers = numbers[numbers % 2 == 0]

# print("Even Numbers:", even_numbers)

# import numpy as np

# numbers = np.arange(1, 10).reshape(3, 3)

# print("Array:")
# print(numbers)

# print("Second Row:", numbers[1])
# print("Last Column:", numbers[:, -1])

# import numpy as np

# celsius = np.array([20, 25, 30, 35, 40, 45])

# fahrenheit = (celsius * 9/5) + 32

# print("Celsius:", celsius)
# print("Fahrenheit:", fahrenheit)

import numpy as np

numbers = np.array([12, 45, 7, 33, 90, 21])

print("Mean:", numbers.mean())
print("Maximum:", numbers.max())
print("Minimum:", numbers.min())