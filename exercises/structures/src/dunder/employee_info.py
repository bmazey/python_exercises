class EmployeeInfo(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __getitem__(self, item):
        return self.name[item]
