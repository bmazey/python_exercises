class Office(object):
    def __init__(self, employees, boss=None):
        self.employees = employees
        self.boss = boss

    # TODO - finish class using dunder methods!
    def __len__(self):
        return len(self.employees)

    def __add__(self, other):
        All = [self.employees[0], self.employees[1], other]

        return All

    def __getitem__(self, position):
        return self.employees[position]

    def __eq__(self, other):
        self.boss.employee_info.name = other.employee_info.name



