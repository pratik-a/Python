a = 5
b = 0

try:
    print(a/b)

except ZeroDivisionError as e:
    print("Errror : ", e)

try:
    inp = int(input("enter a number : "
                    ""))

except ZeroDivisionError as e:
    print("Errror : ", e)

except ValueError as e:
    print("Error : ", e)


finally:
    print("Bye")