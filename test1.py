class Student:
    pass


class Marks:
    pass


stu = Student()
mrk = Marks()
print(isinstance(stu, Student))
print(isinstance(mrk, Student))
print(isinstance(mrk, Marks))
print(isinstance(stu, Marks))
print("Given class is sub class of object or not :")
print(issubclass(Student, object))
print(issubclass(Marks, object))
