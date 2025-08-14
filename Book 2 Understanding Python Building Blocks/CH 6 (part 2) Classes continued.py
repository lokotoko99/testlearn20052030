#Creating a Class

"""
The convention for naming things in classes suggests using an initial cap for the
class name. Attributes, however, should follow the standard for variables, which is
all lowercase with an underscore to separate words within the name.
"""

import datetime as dt

#Define a new class name Member for making member objects.
class Member:
    """ Create a member from uname and fname"""
    def __init__(self, user_name, full_name):
        # Define attributes and give them values
        self.user_name = user_name
        self.full_name = full_name

        # Default date_joined to today's date.
        self.date_joined = dt.date.today()
        # Set is_active to True intially. which is also defaulted
        self.is_active = True

    

# The class ends at the first un-indented line.

#Creating an instance of the Member class named new_guy.
new_guy = Member('Rambo', 'Rocco Moe')

# See what's in the instance, as well as its individual attributes.
print(new_guy)
print(new_guy.user_name)
print(new_guy.full_name)
print(type(new_guy))

# Changing the value of an attribute
new_guy.user_name = "Princess"

print(new_guy.user_name)
print(new_guy.full_name)
print(new_guy.date_joined)
print(new_guy.is_active)



