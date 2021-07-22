def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


n = int(input("enter number for finding fibonacci : "))
result = fact(n)
print("fact : ", result)
