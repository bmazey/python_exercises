class Office(object):
    def __init__(self, employees, boss=None):
        self.employees = employees
        self.boss = boss

    def __len__(self, other):

