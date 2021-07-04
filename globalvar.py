a = 10
print(id(a))


def updatevalue():
    a = 20
    print("in fun : ", a)

    x = globals()['a']
    print(id(x))

    globals()['a'] = 15

updatevalue()
print("outside : ", a)
