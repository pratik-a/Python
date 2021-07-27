pos = -1

def search(list, n):
    l = 0
    u = len(list) - 1
    i = 0
    while l <= u:
        mid = ( l + u) // 2
        if list[mid] == n:
            globals()['pos'] = i
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
        i = i + 1
    return False


list = [20, 50, 40, 30, 70, 10, 100]
n = 70

if search(list, n):
    print("found at ", pos)
else:
    print("not found")

