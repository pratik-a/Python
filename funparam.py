def person(name, age=18):
    print(name)
    print(age)


person(age=20, name="Pratik")
person("Awasthi")


def sum(*b):
    c = 0
    for i in b:
        c += i
    print("sum : ", c)


sum(10, 20, 30, 40, 50)
