from Manager import Manager
from Waiter import Waiter
from Hostess import Hostess
from PyBarException import *
import copy


class Shift:
    def __init__(self, shift_number, table_list, groups_list, workers_list, menu):
        is_shift_num = isinstance(shift_number, int)
        is_table_list = isinstance(table_list, list)
        is_groups_list = isinstance(groups_list, list)
        is_workers_list = isinstance(workers_list, list)
        is_menu = isinstance(menu, dict)
        if not is_menu or not is_workers_list or not is_groups_list or not is_table_list or not is_shift_num:
            raise InvalidInputException
        if not isinstance(workers_list[0], Hostess) or not isinstance(workers_list[1], Waiter) or not isinstance(
                workers_list[2], Manager) or len(workers_list) != 3:
            raise InvalidInputException
        self.shift_number = shift_number
        self.table_list = table_list
        self.groups_list = groups_list
        self.workers_list = workers_list
        self.menu = menu
        self.__total_money = 0
        self.__total_tip = 0

    def __str__(self):
        return f'Shift number: {self.shift_number}'

    def __repr__(self):
        return f'Shift number: {self.shift_number}'

    def add_money(self, money):
        if money < 0:
            raise InvalidInputException
        self.__total_money += money

    def add_tip(self, tip):
        if tip < 0:
            raise InvalidInputException
        self.__total_tip += tip

    def get_money(self, manager):
        if not isinstance(manager, Manager):
            raise AccessDeniedException("Only a manager can access the money")
        return copy.deepcopy(self.__total_money)

    def get_tip(self, manager):
        if not isinstance(manager, Manager):
            raise AccessDeniedException("Only a manager can access the tip")
        return copy.deepcopy(self.__total_tip)

    def shift_day(self):
        for worker in self.workers_list:
            worker.work(self)
            print("________________________________________")
