def square():

    n = 1

    while n <= values:
        sq = n * n
        yield sq
        n += 1


values = int(input("enter number to find square values : "))

value = square()

for i in value:
    print(i)
