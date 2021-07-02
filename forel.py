nums = [10, 20, 30, 40, 50]

for num in nums:
    if num % 11 == 0:
        print("div by 11")
        break
else:
    print("not found")