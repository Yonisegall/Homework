from Customer import Customer
from Group import Group
from Manager import Manager
from Hostess import Hostess
from Waiter import Waiter
from Shift import Shift
from Table import Table
from Person import Person
from Worker import Worker

menu = {"Cola": 12, "Goldstar": 18, "French fries": 20, "Rice": 20, "Homus": 31, "Chicken": 37, "Borger": 52,
        "Steak": 86}


table_1 = Table(1, 2)
table_2 = Table(2, 2)
table_3 = Table(3, 3)

table_list = [table_1, table_2, table_3]

costumer_1 = Customer("Avi", 20, 0.17)
costumer_2 = Customer("Yoni", 21, 0.13)
costumer_3 = Customer("Tom", 25, 0.10)

# order_dict
order_dict_1 = {"Goldstar": 1, "Cola": 1, "French fries": 1, "Chicken": 2}

# groups
group_1 = Group([costumer_1, costumer_2, costumer_3], order_dict_1)
group_2 = Group([costumer_1, costumer_2], {"Goldstar": 1, "Cola": 1, "French fries": 1, "Chicken": 2})


group_list = [group_1, group_2]
# new workers
tom = Manager("Tom", 25)
noy = Waiter("Noy", 26)
essra = Hostess("Essra", 27)
worker_list = [essra, noy, tom]

# shift_1 = Shift(1, table_list, group_list, worker_list, menu)
# shift_1.get_tip(essra)
# Yoni = Person("yoni", 20)
# Yoni.get_age()
# Yoni = Customer("yoni", 20, 0.17)
# print(Yoni)

Yoni = Waiter("yoni", 20)
print(Yoni)
