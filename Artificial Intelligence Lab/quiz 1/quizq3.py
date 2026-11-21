import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([5, 10, 15, 20])


print("Shape of arr1:", arr1.shape)


print("Addition:", arr1 + arr2)


print("Element-wise multiplication:", arr1 * arr2)

print("Elements > 20:", arr1[arr1 > 20])