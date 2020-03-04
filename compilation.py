#This py file is to process data been extracted from the db.
#import libary.
import extraction as ext
import generator as gen
import export as exp
import json
#create function to process data.
def teachers():
    teachers = ext.extract_teacher()
    for teacher in teachers:
        teacher_name = teacher[0]
        username = gen.id()
        email = gen.email(teacher_name)
        password = "123456"
        birthday = gen.date()
        gender = "female/male"
        address = "address"
        phoneNo = "08000000000"
        exp.teacherObject(teacher_name, username, email, password, birthday, gender, address, phoneNo)
    exp.excelObjectTeachers()
#create function to process data.
def students():
    students = ext.extract_student()
    for student in students:
        student_name = student[1].strip()
        username = gen.id()
        email = gen.email(student_name)
        password = "123456"
        birthday = gen.date()
        gender = validate(student[8])
        address = "command school"
        phoneNo = validate_phone(student[6])
        admission_no = username
        state_of_origin = "Lagos"
        student_class = validate_class(student[2].strip())
        exp.studentObject(student_name, username, email, password, birthday, gender, address, phoneNo, admission_no, state_of_origin, student_class)
    exp.excelObject(student_class)
#create function to validate gender data and return male or female if conditions are met or return both if both condidtions are not met.
def validate(gender):
    if (gender == "1"):
        return "male"
    if (gender == "2"):
        return "female"
    return "male/female"
#create function to validate student class data and return class name with matched class id.
def validate_class(classID):
    classData = ext.extract_class()
    for data in classData:
        if(data[0] == int(classID)):
            return data[1]
#create function to vaidate phone number data and return a dummy number if null number is found.
def validate_phone(number):
    if not (len(number) > 0):
        return "08000000000"
    else:
        return number

students()