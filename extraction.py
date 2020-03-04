#this py file is to extract data from the database.
import mysql.connector as conn #import mysql libary to access mysql connector.
# connect to mysql database 
mydb = conn.connect(host="DATABASE_HOST", user="DATABASE_USERNAME", password="DATABASE_PASSWWORD", database="DATABASE_NAME")
mycursor = mydb.cursor()

#create extract functions to extract data from the database.
def extract_teacher():
    mycursor.execute("select first_name from teachers")
    result = mycursor.fetchall()
    print(len(result))
    return result
#create extract functions to extract data from the database.
def extract_student():
    mycursor.execute("select * from students where class = 81")
    result = mycursor.fetchall()
    print(len(result))
    return result
 #create extract functions to extract data from the database.       
def extract_class():
    mycursor.execute("select * from class")
    result = mycursor.fetchall()
    return result