class User():

    def __init__(self, usarname, email):
        self._usarname = usarname
        self._email = email

    def pay_bill(self):
        raise NotImplementedError

    def code(self):
        raise NotImplementedError