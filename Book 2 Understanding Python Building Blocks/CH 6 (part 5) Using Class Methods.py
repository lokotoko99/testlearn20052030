# Using class Methods

"""
As with class variables, you don’t need the self keyword with class methods
because that keyword always refers to the specific object being manipulated at
the moment, not to all objects created by the class. So for starters, if you want
a method to do something to the class as a whole, don’t use def name(self)
because the self immediately ties the method to one object.
"""

import datetime as dt

# Define a new class named Member.
class Member:
    # Default number of free days.
    free_days = 365

    """ Create a new member """
    def __init__(self,user_name,full_name):
        self.user_name = user_name
        self.full_name = full_name
        self.date_joined = dt.date.today()
        # Set an expiration date.
        self.free_expires = dt.date.today() + dt.timedelta(Member.free_days)

    # a @ is something that alters or extends the functionality of that to which it is applied
    # cls is a reference to class as a whole
    
    @classmethod 
    def set_free_days(cls, days):
        cls.free_days = days

    @staticmethod
    def current_time():
        now = dt.datetime.now()
        return f"{now:%I:%M %p}"

Member.set_free_days(90)

wilbur = Member('wblomgren', 'Wilbur Blomgren')

print(wilbur.date_joined)

print(wilbur.free_expires)

print(wilbur.current_time())