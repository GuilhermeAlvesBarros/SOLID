from src.models.bad_example.bad_user import User

class Managers(User):

    def __init__(self, usarname, email):
        super().__init__(usarname, email)

    def pay_bill(self):
        return "Paying bills..."

    def code(self):
        pass
        