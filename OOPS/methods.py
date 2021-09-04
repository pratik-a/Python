class students:

    school = "IT"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def inf():
        print("student details")


s1 = students(75, 70, 80)
s2 = students(65, 75, 70)

print(s1.avg())
print(s2.avg())

print(students.getschool())

students.inf()
