class Employee(object):
    def __init__(self, employee_info, mail):
        self.employee_info = employee_info
        self._mail = mail
        self.sender = self.employee_info.address

    # TODO - finish this class using dunder methods!

    # get the mail at the given position
    def __getitem__(self, position):
        return self._mail[position]




