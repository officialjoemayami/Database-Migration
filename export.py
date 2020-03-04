#this py file is to export processed data into the required format.
#import libary.
import json
import pandas as pd
jsonFile = []

#create funtion to export data into json.
def teacherObject(teacher_name, username, email, password, birthday, gender, address,phoneNo):
    jsonFile.append({
        'username' : username,
        'email' : email,
        'password' : password,
        'fullName' : teacher_name,
        'birthday(year-month-day)' : birthday,
        'gender(female/male)' : gender,
        'address' : address,   
        'phoneNo' : phoneNo 
    })
    with open('teachers.js', 'w') as outFile:
        json.dump(jsonFile, outFile)
#create funtion to export data into json.
def studentObject(student_name, username, email, password, birthday, gender, address, phoneNo, admission_no, state_of_origin, student_class):
    jsonFile.append({
        'username' : username,
        'email' : email,
        'password' : password,
        'fullName' : student_name,
        'admission_no' : admission_no,
        'birthday(year-month-day)' : birthday,
        'gender(female/male)' : gender,
        'address' : address,
        'phoneNo' : phoneNo,
        'stateOrigin(Benue)' : state_of_origin,
    })
    with open('{studentClass}.js'.format(studentClass = student_class), 'w') as outFile:
        json.dump(jsonFile, outFile)
#create funtion to convert json data into excel.
def excelObject(student_class):
    with open('{studentClass}.js'.format(studentClass = student_class), 'r') as outFile:
        df = pd.read_json(outFile)
        df.to_excel('{studentClass}.xls'.format(studentClass = student_class), index=False)
#create funtion to convert json data into excel.
def excelObjectTeachers():
    with open('teachers.js', 'r') as outFile:
        df = pd.read_json(outFile)
        df.to_excel('teachers.xls', index=False)