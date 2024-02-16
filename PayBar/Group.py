from PyBarException import *
import copy


class Group:
    def __init__(self, customers_list, order_dict):
        if not isinstance(customers_list, list) or not isinstance(order_dict, dict) or len(customers_list) < 2:
            raise InvalidInputException

        self.customers_list = customers_list
        self.__order_dict = order_dict

    def get_order(self):
        return copy.deepcopy(self.__order_dict)

    def __str__(self):
        return f'The group has {len(self.customers_list)} members, their order: {self.get_order()}'

    def __repr__(self):
        return f'The group has {len(self.customers_list)} members, their order: {self.get_order()}'

    def __len__(self):
        return len(self.customers_list)

    def __lt__(self, other):
        if not isinstance(other, Group):
            raise InvalidInputException
        return len(self) < len(other)

    def get_customers_string(self):
        name_list = [customer.get_name() for customer in self.customers_list]
        return_string = ", ".join(name_list[:-1]) + " and " + name_list[-1]
        return return_string
