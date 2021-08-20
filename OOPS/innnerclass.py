class students:

    def __init__(self, name, rollnum):
        self.name = name
        self.rollnum = rollnum
        self.lap = self.laptop()

    def show(self):
        print(self.name, self.rollnum)
        self.lap.show()

    class laptop:

        def __init__(self):
            self.brand = "Dell"
            self.cpu = "i7"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = students("Pratik", 1)

s1.show()

lap1 = s1.lap
