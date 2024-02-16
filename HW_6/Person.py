from PyBarException import *
from abc import ABC, abstractmethod
import copy


class Person(ABC):

    def __init__(self, name, age):
        if not isinstance(name, str) or not isinstance(age, int) or len(name) == 0 or age < 18:
            raise InvalidInputException

        self.__name = name
        self.__age = age

    @abstractmethod
    def __str__(self):
        return f'Name:{self.__name},Age:{self.__age}'

    def get_name(self):
        return copy.deepcopy(self.__name)

    def get_age(self):
        return copy.deepcopy(self.__age)
