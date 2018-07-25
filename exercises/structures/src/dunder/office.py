class Office(object):
   def __init__(self, employees, boss=None):
       self.employees = employees
       self.boss = boss

   def __add__(self, other):
       return Office((self.employees + (other,)), self.boss)

   def __len__(self):
       return len(self.employees)

   def __getitem__(self, position):
       return self.employees[position]
