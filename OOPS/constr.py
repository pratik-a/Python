class computer:

    def __init__(self):
        self.name = "Pratik"
        self.age = 22

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


comp1 = computer()
comp2 = computer()
comp3 = computer()
comp4 = computer()
comp4.age = 20

if comp1.compare(comp2):
    print("same")
else:
    print("not same")

if comp3.compare(comp4):
    print("same")
else:
    print("not same")
