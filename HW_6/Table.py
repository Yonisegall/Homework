from PyBarException import *
from Group import Group


class Table:
    def __init__(self, number, max_capacity):
        is_num = isinstance(number, int)
        is_max_cap = isinstance(max_capacity, int)
        if not is_num or not is_max_cap or number <= 0 or max_capacity <= 0:
            raise InvalidInputException

        self.number = number
        self.max_capacity = max_capacity
        self.group = None
        self.bill = {}
        self.each_pay = None
        self.total_pay = 0
        self.total_tip = 0

    def __str__(self):
        return f'Table number {self.number} has {self.max_capacity} seats'

    def __repr__(self):
        return f'Table number {self.number} has {self.max_capacity} seats'

    def __len__(self):
        return self.max_capacity

    def __lt__(self, other):
        if not isinstance(other, Table):
            raise InvalidInputException
        return self.max_capacity < other.max_capacity

    def is_empty(self):
        if self.group is None:
            return True
        else:
            return False

    def seat(self, group):
        if not isinstance(group, Group):
            raise InvalidInputException
        if len(group) > self.max_capacity:
            raise TooSmallTableException
        if not self.is_empty():
            raise OccupiedTableException
        self.group = group

    def order(self, menu):
        if self.is_empty():
            raise EmptyTableException
        for products in self.group.get_order():
            if products not in menu:
                print(f"Sorry we don't have {products}.")
            else:
                self.bill[products] = menu.get(products) * self.group.get_order()[products]
        print("Your bill is:")
        for products in self.bill:
            print(f"{products}..........{self.bill[products]}")

    def pay(self):
        if self.is_empty():
            raise EmptyTableException
        for pay in self.bill:
            self.total_pay += self.bill.get(pay)
        self.each_pay = self.total_pay / len(self.group.customers_list)
        for customer in self.group.customers_list:
            self.total_tip += customer.tip * self.each_pay
        return int(self.total_pay), float(round(self.total_tip, 3))
