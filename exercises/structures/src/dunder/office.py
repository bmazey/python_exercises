class Office(object):
    def __init__(self, employees, boss=None):
        self.employees = employees
        self.boss = boss

    def __len__(self):
        return len(self.employees)

    def __add__(self, other):
        self.employees + other
