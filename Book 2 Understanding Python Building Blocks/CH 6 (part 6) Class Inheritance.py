# Class Inheritance

# Class is used for all kinds of people
import datetime as dt

# Base class is used for all kinds of Members.

# Creating the base (main) class

class Member:
    """ The Member class attributes and methods are for everyone"""
    # By Default, a new account expires in one year (365 days)
    
    expiry_days = 365

    # Intialize a member object.
    def __init__(self, first_name, last_name):
        # Attributes (instance variables) for everybody.
        self.first_name = first_name
        self.last_name = last_name
        # Calculate expiry date today's date.
        self.expiry_date = dt.date.today() + dt.timedelta(days = self.expiry_days)

joe = Member('Joe','Anybody')
print(joe.first_name)
print(joe.last_name)
print(joe.expiry_date)

# Defining a subclass

# Subclass for Admins.
class Admin(Member):
    # Admin accounts don't expire for 100 years.
    expiry_days = 365.2422 *100
    pass

# Subclass for Users
class User(Member):
    pass

# Outside the class now.
ann = Admin('Annie','Angst')
print(ann.first_name)
print(ann.last_name)
print(ann.expiry_date)
print()

uli = User('Uli','Ungula')
print(uli.first_name)
print(uli.last_name)
print(uli.expiry_date)
