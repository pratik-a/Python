class A:

    def __init__(self):
        print("init in a")

    def feature1(self):
        print("feature 1 started")

    def feature2(self):
        print("feature 2 started")


class B:

    def __init__(self):
        super().__init__()
        print("init in b")

    def feature3(self):
        print("feature 3 started")

    def feature4(self):
        print("feature 4 started")


class C(A, B):

    def __init__(self):
        super().__init__()
        print("init in c")

    def feature5(self):
        super().feature1()
        print("feature 5 started")


c1 = C()
c1.feature5()
