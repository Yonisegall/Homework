from unittest import TestCase
from unittest.mock import patch
from Table import Table
from PyBarException import *
from Customer import Customer
from Group import Group
from io import StringIO

menu = {"Cola": 12, "Goldstar": 18, "French fries": 20, "Rice": 20, "Homus": 31, "Chicken": 37, "Borger": 52,
        "Steak": 86}

# Tables
table_1 = Table(1, 2)
table_2 = Table(2, 2)
table_3 = Table(3, 3)
table_4 = Table(4, 3)
table_5 = Table(5, 4)
table_6 = Table(6, 4)
table_7 = Table(7, 5)
table_8 = Table(8, 6)
table_9 = Table(9, 7)
table_10 = Table(10, 8)

# Costumers
costumer_1 = Customer("Avi", 20, 0.17)
costumer_2 = Customer("Yoni", 21, 0.13)
costumer_3 = Customer("Tom", 25, 0.10)
costumer_4 = Customer("Idan", 23, 0.11)
costumer_5 = Customer("Omer", 24, 0.2)
costumer_6 = Customer("Assaf", 21, 0.12)
costumer_7 = Customer("Ofek", 29, 0.14)
costumer_8 = Customer("Barak", 28, 0.15)
costumer_9 = Customer("Dor", 30, 0.14)
costumer_10 = Customer("Shay", 24, 0.10)

# Groups
group_2 = Group([costumer_1, costumer_5], {"Goldstar": 1, "Cola": 1, "French fries": 1, "Chicken": 2})
group_3 = Group([costumer_3, costumer_8, costumer_5], {"Goldstar": 2, "Cola": 1, "Homus": 1, "Chicken": 2, "Fish": 1})
group_4 = Group([costumer_6, costumer_7, costumer_8, costumer_4],
                {"Goldstar": 4, "Maccabi": 1, "French fries": 1, "Chicken": 4})
group_5 = Group([costumer_1, costumer_6, costumer_3, costumer_5, costumer_10],
                {"Goldstar": 2, "Cola": 3, "French fries": 2, "Burger": 3, "Fish": 2})
group_6 = Group([costumer_1, costumer_2, costumer_8, costumer_7, costumer_4, costumer_10],
                {"Maccabi": 2, "Cola": 4, "Rice": 3, "Burger": 4})

# seat
table_2.seat(group_2)
table_3.seat(group_3)
table_8.seat(group_6)


# order

class TestTable(TestCase):

    def test__init__(self):
        self.assertRaises(InvalidInputException, Table, 1, "4")
        self.assertRaises(InvalidInputException, Table, "2", 2)
        self.assertRaises(InvalidInputException, Table, 0, 2)
        self.assertRaises(InvalidInputException, Table, 2, 0)
        self.assertRaises(InvalidInputException, Table, "2", "3")

    def test__str__(self):
        self.assertEqual("Table number 1 has 2 seats", str(table_1))

    def test__repr__(self):
        self.assertEqual("Table number 2 has 2 seats", repr(table_2))

    def test__len__(self):
        self.assertEqual(3, len(table_3))

    def test__lt__(self):
        self.assertRaises(InvalidInputException, table_8.__lt__, costumer_5)
        self.assertEqual(False, table_9.__lt__(table_8))
        self.assertEqual(True, table_9.__lt__(table_10))

    def test_is_empty(self):
        self.assertRaises(InvalidInputException, Group, ["Avi"], {"Goldstar": 4, "Red Wine": 1})
        self.assertRaises(InvalidInputException, Group, ("Avi", "Dani"), {"Goldstar": 4, "Red Wine": 1})
        self.assertRaises(InvalidInputException, Group, ["Avi", "Dani"], ("Goldstar", "Red Wine"))

        self.assertEqual(True, table_1.is_empty())
        self.assertEqual(False, table_2.is_empty())
        self.assertEqual(False, table_3.is_empty())
        self.assertEqual(True, table_4.is_empty())
        self.assertEqual(True, table_5.is_empty())
        self.assertEqual(True, table_6.is_empty())
        self.assertEqual(True, table_7.is_empty())
        self.assertEqual(False, table_8.is_empty())
        self.assertEqual(True, table_9.is_empty())
        self.assertEqual(True, table_10.is_empty())

    def test_seat(self):
        table_9.seat(group_5)
        self.assertRaises(TooSmallTableException, table_1.seat, group_4)
        self.assertRaises(OccupiedTableException, table_9.seat, group_6)
        self.assertRaises(InvalidInputException, table_5.seat, costumer_5)

    def test_order(self):
        self.assertRaises(EmptyTableException, table_5.order, group_5)
        expected_1 = "Your bill is:\nGoldstar..........18\nCola..........12\nFrench " \
                     "fries..........20\nChicken..........74\n"
        with patch('sys.stdout', new=StringIO()) as real_out:
            table_2.order(menu)
            self.assertEqual(expected_1, real_out.getvalue())
        expected_2 = "Sorry we don't have Fish.\nYour bill " \
                     "is:\nGoldstar..........36\nCola..........12\nHomus..........31\nChicken..........74\n"
        with patch('sys.stdout', new=StringIO()) as real_out:
            table_3.order(menu)
            self.assertEqual(expected_2, real_out.getvalue())

    def test_pay(self):
        table_2.order(menu)
        table_3.order(menu)
        table_8.order(menu)

        self.assertRaises(EmptyTableException, table_5.pay)
        self.assertEqual((124, 22.94), table_2.pay())
        self.assertEqual((153, 22.95), table_3.pay())
        self.assertEqual((108, 14.4), table_8.pay())
