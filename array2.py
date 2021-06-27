from array import *

arr = array('i', [])

n = int(input("enter number of element "))

for i in range(n):
    x = int(input("enter value at index "))
    arr.append(x)

print(arr)

srh = int(input("enter number for search "))

k = 0
for i in arr:
    if srh == i:
        print("found at ", k)
    k += 1

print(arr.index(srh))