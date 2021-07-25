from abc import ABC, abstractmethod


class computer(ABC):
    @abstractmethod
    def process(self):
        pass


class laptop(computer):
    def process(self):
        print("abstract method calling")


lap = laptop()
lap.process()
