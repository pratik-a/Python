def fact(n):
    mult = 1
    for i in range(1, n + 1):
        mult = mult * i

    return mult


n = int(input("enter number for finding fibonacci : "))
result = fact(n)
print("fact : ", result)
