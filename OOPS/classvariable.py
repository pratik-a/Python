class cars:

    gear = 5

    def __init__(self):
        self.mil = 10
        self.com = "TATA"


c1 = cars()
c2 = cars()

print(c1.mil, c1.com, c1.gear)
print(c2.mil, c2.com, c2.gear)

c1.mil = 12
cars.gear = 2

print(c1.mil, c1.com, c1.gear)
print(c2.mil, c2.com, c2.gear)