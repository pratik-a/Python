x = int(input("enter a number "))

for i in range(2, int(x/2)):
    if x % i == 0:
        print("not prime")
        break
else:
    print("prime")
