class Student:
    stu_name = 'AADARSH KUMAR'
    marks = 80 
print('Original Value :') 
print(f"Student Name: {getattr(Student, 'stu_name')}")
print(f"Marks: {getattr(Student, 'marks')}")
setattr(Student, 'stu_name', 'KUMAR AADARSH')
setattr(Student, 'marks', 50)
print('Modified Value :')
print(f"Student Name: {getattr(Student, 'stu_name')}")
print(f"Marks: {getattr(Student, 'marks')}")