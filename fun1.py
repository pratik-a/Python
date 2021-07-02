def add(x, y):
    c = x + y
    print(c)


add(2, 4)


def minus(x, y):
    c = x - y
    return c


minusv = minus(2, 4)
print(minusv)


def mul_div(x, y):
    c = x * y
    d = x / y
    return c, d


mul, div = mul_div(2, 4)
print(mul, div)
