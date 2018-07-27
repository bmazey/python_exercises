class Employee(object):
    def __init__(self, employee_info, mail):
        self.employee_info = employee_info
        self._mail = mail
        self.recipient = mail
        self.sender = 'pam.beesly@dundermifflin.com'

    # TODO - finish this class using dunder methods! test
    def __getitem__(self, item):
        return self.recipient[item]
