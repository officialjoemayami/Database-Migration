#this py file is to auto generate data required in this project.
#import libaries.
import random
import string
from datetime import datetime as dt

username = [] #decalare a username array to store generated username.

#create a function to auto generate random id for username.
def id(size=7,chars=string.ascii_uppercase + string.digits):
    return validate(''.join(random.choice(chars) for _ in range(size)))
#create a function to validate if username already exist in our array list.
def validate(user):
    if not (len(username) > 0):
        return user
    if user not in username:
        username.append(user)
        return user
    return id()
#create a function to auto generate eamil address.
def email(name):
    if not (len(name) > 1):
        return False
    name = name.split(" ")
    first_letter = name[0][0]
    three_letters_surname = name[-1][:3]
    number = '{:03d}'.format(random.randrange(1, 999))
    email = first_letter + three_letters_surname + number + '@jive.com'
    return email
#create a function to auto generate date.
def date():
    return dt.today().strftime('%Y-%m-%d')