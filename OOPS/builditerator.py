class iterator:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= value:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values = iterator()

value = int(input("enter number to print values : "))

print(next(values))

for i in values:
    print(i)
