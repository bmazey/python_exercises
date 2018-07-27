class Employee(object):
    def __init__(self, employee_info, mail):
        self.employee_info = employee_info
        self.sender = self.employee_info.address
        self._mail = mail

    def __getitem__(self, item):
        return self._mail[item]

    # TODO - finish this class using dunder methods!
