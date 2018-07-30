class Employee(object):
    def __init__(self, employee_info, mail):
        self.employee_info = employee_info
        self._mail = mail
        self.sender = 'pam.beesly@dundermifflin.com'

    def __getitem__(self, index):
        return self._mail[index]
    # TODO - finish this class using dunder methods!



