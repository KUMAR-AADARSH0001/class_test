class Student:
    stu_id = int(input('Enter student id :'))
    stu_name = input('Enter student name :') 
print("Original Value :")
a=Student
print(a.stu_id)
print(a.stu_name)
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} = {value}')
print("\nAfter adding the stu_class :")
Student.stu_class =input('Enter student class :')
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} = {value}')
print("\nAfter removing the stu_name:")
del Student.stu_name
#delattr(Student, 'stu_name')
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} = {value}')