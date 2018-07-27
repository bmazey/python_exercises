class Office(object):
    def __init__(self, employees, boss=None):
        self.employees = employees
        self.boss = boss

# this adds the employees
    def __add__(self, other):
        return Office((self.employees + (other,)), self.boss)

# this allows the test to get the number of employees
    def __len__(self):
        return len(self.employees)

# this allows the test to get an employee from the list
    def __getitem__(self, item):
        return self.employees[item]

