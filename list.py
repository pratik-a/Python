from typing import List

nums = [52, 23, 45, 6, 78]

print(nums)
nums.sort()
nums.insert(4, 100)
nums.remove(100)
del nums[4:]
nums.extend([20, 30])
print(nums)

print(max(nums))

print(nums[0])

print(nums[2:])

print(nums[-2])

names = ["apple", "mango", "orange"]

print(names)

data = ["apple", 2, "kg", 24.5]

print(data)

coll = [names, data]

print(coll)
