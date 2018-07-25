class Employee(object):
    def __init__(self, employee_info, mail):
        self.employee_info = employee_info
        self._mail = mail
        self.sender = employee_info.address

    def __getitem__(self, item):
        return self._mail[item]

