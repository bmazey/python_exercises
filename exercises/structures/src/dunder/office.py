class Office(object):
    def __init__(self, employees, boss=None):
        self.employees = employees
        self.boss = boss

    # TODO - finish class using dunder methods!
    # let the length be the number of employees in the office
    def __len__(self):
        return len(self.employees)

    # get the employee in the given position
    def __getitem__(self, position):
        return self.employees[position]

    # add more employees to the office
    def __add__(self, friendo):
        newfriendo = self.employees+(friendo,)
        return Office(newfriendo, self.boss)





