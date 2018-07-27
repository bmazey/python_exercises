class Office(object):
    def __init__(self, employees, boss=None):
        self.employees = employees
        self.boss = boss

    # TODO - finish class using dunder methods!

    def __len__(self):
        return len(self.employees)

    def __getitem__(self, position):
        return self.employees[position]

    def __add__(self, other):
        all_mails = self.employees + (other,)
        return Office(all_mails, self.boss)
