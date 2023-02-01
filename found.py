# 11. Create a class with the name User.
# Define 9 keys(_id, createdAt, updatedAt, password) for the user and
# an empty list(This can be a class variable) of users inside the class.
# Define one function to create users e.g. create_user(This function will take 9 keys for the user information)
# and another update_user to update user information.
# update_user takes _id to find the user from the list and other information that needs to be updated.
# id is a random string with length 9 and type [0-9a-zA-Z!@#$%^].
# Create Functions to update passwords, this takes user _id to identify the user.
# When a key is updated, the following updatedAt key should be updated.
import datetime


class User:
    id = 0
    user_list = []

    def create_user(
        self,
        f_name,
        l_name,
        password,
        age,
        email,
        gender,
        address,
        dob,
    ):
        userInfo = {
            "id": self.id,
            "f_name": f_name,
            "l_name": l_name,
            "password": password,
            "age": age,
            "email": email,
            "gender": gender,
            "address": address,
            "dob": dob,
            "created_at": str(datetime.datetime.now()),
            "updated_at": str(datetime.datetime.now()),
        }
        self.id += 1
        self.user_list.append(userInfo)

    # data is type of dictionary
    def update_user(self, data):
        # {"first_name": "New Name", "id": 8, }
        # 1. Find the index of object from user_list user user "id"
        # 2. Update the object data as per the "data" argument
        # 3. Update updated_at key with new Date value i.e. datetime.datetime.now()
        pass

    def update_password(self, id, newpass):
        # 1. Find the index of object from user_list user user "id"
        # 2. Update the user password
        # 3. Update updated_at key
        pass


user = User()
user.create_user(
    "Kuldeep",
    "Bisnoi",
    "1234",
    18,
    "ashish@gmail.com",
    "male",
    "ABC road, Hisar, Haryana(125001)",
    "09-06-2005",
)
user.create_user(
    "Adarsh",
    "Kumar",
    "123456",
    20,
    "adarsh@gmail.com",
    "male",
    "BCA road, Hisar, Haryana(125001)",
    "08-11-2003",
)

print("hello")
