class Office(object):
    def __init__(self, employees, boss=None):
        self.employees = employees
        self.boss = boss

    # TODO - finish class using dunder methods!

    def __len__(self):
        return len(self.employees)

    def __getitem__(self, item):
        return self.employees[item]

    def __add__(self, other):
        self.employees = self.employees + (other,)
        return self
