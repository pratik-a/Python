def fun():
    print("function")
    
fun()
print(fun())
print(fun)

def fun1(x, y):
    print(x," ",y)
    
fun1(2,3)
print(fun1(2,3))

def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result
    
    
print(power(2))
print(power(4,5))

def multiadd(*args):
    result = 0
    for x in args:
        result = result + x
    return result
    
    
    
print(multiadd(2,2,2,2,2))
