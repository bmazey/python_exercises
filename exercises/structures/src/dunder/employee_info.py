class EmployeeInfo(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address

# TODO - add dunder methods?
    def __getitem__(self, position):
        return self.address[position]

    # def __add__(self, other):
    #      self.list = (self, other)
    #      return self.list

