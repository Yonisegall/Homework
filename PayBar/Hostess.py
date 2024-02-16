from Worker import Worker


class Hostess(Worker):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.is_place = None
        self.job = Hostess

    def __str__(self):
        return f'Name:{self.get_name()}Age:{self.get_age()}Job:{self.job}'

    def work(self, shift):
        sorted_groups_list = sorted(shift.groups_list)
        sorted_table_list = sorted(shift.table_list)
        for group in reversed(sorted_groups_list):
            self.is_place = False
            for table in sorted_table_list:
                if len(table) >= len(group) and table.is_empty():
                    table.seat(group)
                    print(f"{group.get_customers_string()} you can seat on table {table.number} please.")
                    self.is_place = True
                    break
            if not self.is_place:
                print(f"Sorry {group.get_customers_string()}, we don't have place for {len(group)} people.")
