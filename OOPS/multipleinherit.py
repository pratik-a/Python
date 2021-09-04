class A:

    def feature1(self):
        print("feature 1 started")

    def feature2(self):
        print("feature 2 started")


class B:

    def feature3(self):
        print("feature 3 started")

    def feature4(self):
        print("feature 4 started")


class C(A, B):

    def feature5(self):
        print("feature 5 started")


c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()