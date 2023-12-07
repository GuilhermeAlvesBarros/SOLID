from src.models.users import User

class Members(User):

    def __init__(self, usarname, email):
        super().__init__(usarname, email)

    @staticmethod
    def members():
        return ['username1', 'username2', 'team1']
