
import datetime as dt

#Define a new class name Member for making member objects.

class Member:
    """Create a member object """
    free_days = 90
    def __init__(self, user_name, full_name):
        # Define attributes and give them values
        self.user_name = user_name
        self.full_name = full_name
        # Default date_joined to today's date.
        self.date_joined = dt.date.today()
        # Set is_active to True intially. which is also defaulted
        self.is_active = True

    # A method to return a formatted string showing date joined.
    def show_date_joined(self):
        return f"{self.full_name} joined on {self.date_joined:%m-%d-%y}"
    
    """It helps to understand that a method is really just a function. What makes a
    method different from a function is the fact that a method is always associated
    with some class. So a method is not as generic as a function."""
    # Method to activate (True) or deactivate (False) account. (Passing parameters to methods)
    def set_is_active(self, input):
        """ True for active, False to make inactive"""
        self.is_active = input

    
# The class ends at the first un-indented line.

#Creating an instance of the Member class named new_guy.
new_guy = Member('Rambo', 'Rocco Moe')

# See the date the new guy joined
print(new_guy.show_date_joined())

#Calling a class method by class name
print(Member.show_date_joined(new_guy))

print(new_guy.is_active)

new_guy.set_is_active(False)

print(new_guy.is_active)

# Calling a class method by class name

