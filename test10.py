import random
import string
import datetime


class User:
    def __init__(self):
        self._id = ''.join(random.choices(
            string.ascii_letters + string.digits + string.punctuation, k=9))
        self.fname = input('Enter yuor first name :')
        self.lname = input('Enter yuor last name :')
        self.gender = input('Enter your gender :')
        self.age = input('Enter you age :')
        self.gmail = input('Enter your gmail :')
        self.pswrd = input('Enter your password :')
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def update_password(self):
        self.password = input('Enter your new password :')
        self.updatedAt = datetime.datetime.now()


newUser = User({"name": 'something'})

# Create 5 users
users = []
for i in range(2):
    users.append(User())
