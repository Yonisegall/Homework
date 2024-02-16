from Worker import Worker


class Manager(Worker):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.job = Manager

    def __str__(self):
        return f'Name:{self.get_name()}Age:{self.get_age()}Job:{self.job}'

    def work(self, shift):
        for table in shift.table_list:
            if table.is_empty():
                continue
            table.pay()
            shift.get_money(self)
            shift.add_money(table.total_pay)
            shift.add_tip(table.total_tip)
            print(f"Thank you {table.group.get_customers_string()}! You paid {table.total_pay + table.total_tip}"
                  f" shekels. See you next time!")
        print(f"This is the end of the shift:\nShift number: {shift.shift_number}.\n"
              f"Total money: {shift.get_money(self)}, total tip: {shift.get_tip(self)}")
