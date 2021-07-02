def update(lst):
    print(id(lst))
    lst[1] = 25
    print(id(lst))
    print("lst : ", lst)


lst = [10, 20, 30, 40, 50]
print(id(lst))
update(lst)
print(lst)

def updatea(a):
    print(id(a))
    a = 25
    print(id(a))
    print("a : ", a)


a = 10
print(id(a))
updatea(a)
print(a)