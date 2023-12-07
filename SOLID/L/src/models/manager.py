from src.models.users import User

class Managers(User):

    def __init__(self, usarname, email):
        super().__init__(usarname, email)
    