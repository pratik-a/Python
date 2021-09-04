from time import sleep
from threading import *


class good(Thread):
    def run(self):
        for i in range(10):
            print("good")
            sleep(1)


class excellent(Thread):
    def run(self):
        for i in range(10):
            print("excellent")
            sleep(1)


obj1 = good()
obj2 = excellent()

obj1.start()
sleep(0.1)
obj2.start()

obj1.join()
obj2.join()

print("bye")
