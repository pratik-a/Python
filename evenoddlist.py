lst = [20, 23, 30, 45, 56, 65, 34, 67, 65, 21, 69, 97]


def count(lst):
    odd = 0
    even = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd, even


odd, even = count(lst)
print("even : {} and odd : {}".format(even, odd))
