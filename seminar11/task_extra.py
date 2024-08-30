from abc import ABC, abstractmethod


class Human(ABC):
    @abstractmethod
    def get_name(self):
        return 'имя'


class Worker(Human):

    def get_name(self):
        return Human.get_name(self)


w1 = Worker()

print(w1.get_name())

