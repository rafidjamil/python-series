import numpy as np

arr = np.array([10, 20, 30, 40, 50])

normalised = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

print("Original Array:", arr)
print("Normalised Array:", normalised)
