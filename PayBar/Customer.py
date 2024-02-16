from Person import Person
from PyBarException import *


class Customer(Person):
    def __init__(self, name, age, tip):
        if not isinstance(tip, float):
            raise InvalidInputException
        self.tip = tip
        if tip < 0:
            raise InvalidInputException
        super().__init__(name, age)

    def __str__(self):
        return f'Name:{self.get_name()},Age:{self.get_age()},Tip:{int(self.tip * 100)}%'
