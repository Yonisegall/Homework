from Person import Person
from abc import ABC, abstractmethod


class Worker(Person, ABC):

    def __int__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

    @abstractmethod
    def __str__(self):
        return f'Name:{self.get_name()},Age:{self.get_age()},Job:{self.job}'

    @abstractmethod
    def work(self, shift):
        pass
