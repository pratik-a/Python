from numpy import *

arr = array([1, 2, 3, 4, 5])
arr = arr + 5
print(arr)

arr1 = array([10, 20, 30, 40, 50])
arr2 = arr + arr1
print(arr2)

print(sin(arr))
print(log(arr))
print(sum(arr))
print(max(arr))

print(concatenate([arr, arr1]))

arr3 = arr
print(arr3)

print(id(arr))
print(id(arr3))

arr4 = arr.view()
arr[2] = 100
print(arr4)

arr5 = arr.copy()
arr[2] = 200
print(arr5)
