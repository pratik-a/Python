from numpy import *

arr = array([
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ])

m = matrix(arr)
print(m)
print(diagonal(m))
print(m.min())
print(m.max())

arr1 = array([
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ])
m1 = matrix(arr1)

m2 = m + m1
print(m2)

m3 = m * m1
print(m3)