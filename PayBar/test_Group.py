from unittest import TestCase
from Group import Group
from PyBarException import *
from Customer import Customer

# Costumers
costumer_1 = Customer("Avi", 20, 0.17)
costumer_2 = Customer("Yoni", 21, 0.13)
costumer_3 = Customer("Tom", 25, 0.10)

# order_dict
order_dict_1 = {"Goldstar": 1, "Cola": 1, "French fries": 1, "Chicken": 2}
order_dict_2 = {"Goldstar": 1, "Cola": 1, "French fries": 1}

# groups
group_1 = Group([costumer_1, costumer_2, costumer_3], order_dict_1)
group_2 = Group([costumer_2, costumer_3], order_dict_2)


class TestGroup(TestCase):

    def test__init__(self):
        self.assertRaises(InvalidInputException, Group, [costumer_1], order_dict_1)
        self.assertRaises(InvalidInputException, Group, "Avi", order_dict_1)
        self.assertRaises(InvalidInputException, Group, 23, order_dict_1)
        self.assertRaises(InvalidInputException, Group, {"avi": 1}, order_dict_1)
        self.assertRaises(InvalidInputException, Group, (12, 13, 14), order_dict_1)
        self.assertRaises(InvalidInputException, Group, [costumer_1, costumer_2], (1, 2, 3))
        self.assertRaises(InvalidInputException, Group, [costumer_1, costumer_2], [1, 2])
        self.assertRaises(InvalidInputException, Group, [costumer_1, costumer_2], "dddd")
        self.assertRaises(InvalidInputException, Group, [costumer_1, costumer_2], 123412)

    def test_get_order(self):
        self.assertEqual({"Goldstar": 1, "Cola": 1, "French fries": 1, "Chicken": 2}, group_1.get_order())
        self.assertEqual({"Goldstar": 1, "Cola": 1, "French fries": 1}, group_2.get_order())

    def test__str__(self):
        self.assertEqual("The group has 3 members, their order: {'Goldstar': 1, 'Cola': 1, 'French fries': 1, "
                         "'Chicken': 2}", str(group_1))
        self.assertEqual("The group has 2 members, their order: {'Goldstar': 1, 'Cola': 1, 'French fries': 1}",
                         str(group_2))

    def test__repr__(self):
        self.assertEqual("The group has 3 members, their order: {'Goldstar': 1, 'Cola': 1, 'French fries': 1, "
                         "'Chicken': 2}", repr(group_1))
        self.assertEqual("The group has 2 members, their order: {'Goldstar': 1, 'Cola': 1, 'French fries': 1}",
                         repr(group_2))

    def test__len__(self):
        self.assertEqual(3, len(group_1))
        self.assertEqual(2, len(group_2))

    def test__lt__(self):
        self.assertRaises(InvalidInputException, group_2.__lt__, costumer_1)
        self.assertEqual(False, group_1.__lt__(group_2))
        self.assertEqual(True, group_2.__lt__(group_1))

    def test_get_customers_string(self):
        self.assertEqual("Avi, Yoni and Tom", group_1.get_customers_string())
        self.assertEqual("Yoni and Tom", group_2.get_customers_string())
