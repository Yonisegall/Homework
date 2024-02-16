from Worker import Worker


class Waiter(Worker):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.job = Waiter

    def __str__(self):
        return f'Name:{self.get_name()}Age:{self.get_age()}Job:{self.job}'

    def work(self, shift):
        for table in shift.table_list:
            if table.is_empty():
                continue
            print(f"Hey {table.group.get_customers_string()}! My name is {self.get_name()} and I'm your waiter.")
            table.order(shift.menu)
            print("")
