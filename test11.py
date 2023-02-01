import datetime
# import random
# import string


class User:
    id = 0
    user_list = []

    def create_user(self, _id, f_name, l_name, age, email, password, gender, address):
        userInfo = {
            # ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=9)),
            "id": _id,
            "f_name": f_name,
            "l_name": l_name,
            "age": age,
            "email": email,
            "password": password,
            "gender": gender,
            "address": address,
            "created_at": str(datetime.datetime.now()),
            "updated_at": str(datetime.datetime.now()),
        }
        self.id += 1
        self.user_list.append(userInfo)

    # data is type of dictionary

    def update_user(self, f_name, l_name, age, address):
        user.user_list[0]['f_name'] = f_name
        user.user_list[0]['l_name'] = l_name
        user.user_list[0]['age'] = age
        user.user_list[0]['address'] = address
        user.user_list[0]['update_at'] = str(datetime.datetime.now())

    def update_password(self, password):
        user.user_list[1]['password'] = password
        user.user_list[1]['update_at'] = str(datetime.datetime.now())


user = User()
user.create_user(0, "Kuldeep", "Bisnoi",  18, "ashish@gmail.com",
                 "1234", "male", "ABC road, Hisar, Haryana(125001)")
user.create_user(1, "Adarsh", "Kumar", 20, "adarsh@gmail.com",
                 "123456", "male", "BCA road, Hisar, Haryana(125001)")
data = user.user_list

print(user.user_list)
for i in data:
    for j in i:
        print(j, "=", i[j])
user.update_user()
print(user.user_list)
user.update_password()
print(user.user_list)
