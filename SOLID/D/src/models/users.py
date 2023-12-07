class User():

    def __init__(self, usarname, email):
        self._usarname = usarname
        self._email = email

    def work(self):
        raise NotImplementedError