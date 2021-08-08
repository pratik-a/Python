class value:

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def get_v1(self):
        return self.v1

    def get_v2(self):
        return self.v2

    def set_v1(self, val):
        self.v1 = val

    def set_v2(self, val):
        self.v2 = val


va1 = value(1, 2)

print(va1.get_v1())
print(va1.get_v2())

va1.set_v1(10)
va1.set_v2(20)

print(va1.get_v1())
print(va1.get_v2())