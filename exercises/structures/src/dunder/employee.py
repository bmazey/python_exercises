class Employee(object):
    def __init__(self, employee_info, mail):
        self.employee_info = employee_info
        self._mail = mail
        self.sender = employee_info.address

    # TODO - finish this class using dunder methods!

    def __getitem__(self, position):
        return self._mail[position]






