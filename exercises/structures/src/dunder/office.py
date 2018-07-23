class Office(object):
    def __init__(self, employees, boss=None):
        self.employees = employees
        self.boss = boss

    def __len__(self):
        return len(self.employees)

    def __getattr__(self, item):
        return self.employees[item]

    # TODO - finish class using dunder methods!
