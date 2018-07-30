class Office(object):
    def __init__(self, employees, boss=None):
        self.employees = employees
        self.boss = boss

    def __len__(self):
        return len(self.employees)

    def __getitem__(self, index):
        return self.employees[index]

    def __add__(self, employee):
        self.employees = self.employees + (employee,)
        return self




    # TODO - finish class using dunder methods!
