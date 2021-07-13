from numpy import *

arr = array([
                [1, 2, 3, 40, 50, 60],
                [4, 5, 6, 10, 20, 30]
            ])
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)

arr1 = arr.flatten()
print(arr1)

arr2 = arr.reshape(2, 2, 3)
print(arr2)