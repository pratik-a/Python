pos = -1

def search(list, n):

    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1
    return False


list = [20, 50, 40, 30, 70, 10, 100]
n = 70

if search(list, n):
    print("found at ", pos)
else:
    print("not found")
