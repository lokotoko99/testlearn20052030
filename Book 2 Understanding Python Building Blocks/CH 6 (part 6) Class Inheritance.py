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
        # Default secret code is nothing
        self.secret_code =""

    # Method in the base class.
    def show_expiry(self):
        return f"{self.first_name} {self.last_name} expires on {self.expiry_date}"
    
    def get_status(self):
        return f"{self.first_name} is a Member"
    


joe = Member('Joe','Anybody')
print(joe.first_name)
print(joe.last_name)
print(joe.expiry_date)
print(joe.get_status())

# Defining a subclass

# Subclass for Admins.
class Admin(Member):
    # Admin accounts don't expire for 100 years.
    expiry_days = 365.2422 * 100
    def __init__(self,first_name, last_name,secret_code):
        # any parameters that belong to the base class Member need to be set up super() reference to parent class(superclass) 
        # treats the current object as thought it from made from parent class
        # Pass the Member parameters up to Member class.
        super().__init__(first_name,last_name)
        # Assign the remaining parameters to this Admin object.
        self.secret_code = secret_code

    #method inside a subclass will overpower the one in the baseclass if same name
    def get_status(self):
        return f"{self.first_name} is a Admin"
    
# Subclass for Users
class User(Member):

    #method inside a subclass will overpower the one in the baseclass if same name
    def get_status(self):
        return f"{self.first_name} is a Regular User"
    

# Outside the class now.
ann = Admin('Annie','Angst','PRESTO')
print(ann.first_name)
print(ann.last_name)
print(ann.expiry_date)
print(ann.secret_code)
print(ann.show_expiry())
print(ann.get_status())
print(Admin.__dict__)



uli = User('Uli','Ungula')
print(uli.first_name)
print(uli.last_name)
print(uli.expiry_date)
print(uli.secret_code)
print(uli.show_expiry())
print(uli.get_status())

# help(Admin)
