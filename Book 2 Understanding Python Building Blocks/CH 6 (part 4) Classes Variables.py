import datetime as dt

# Define a new class named Member.
class Member:
    # Default number of free days.
    free_days = 365

    """ Create a new member,"""
    def __init__(self,user_name, full_name):
        self.user_name = user_name
        self.full_name = full_name

        # Set date_joined to today's date.
        self.date_joined = dt.date.today()
        # Set expiration date.
        # you can use self.free_days or Member.free_days but you have to reference back to the class
        self.free_expires = dt.date.today() + dt.timedelta(days = self.free_days) 
    
# The class ends at the first un-indented line.
Member.free_days = 90
# Create an instance of the Member class named wilbur.
wilbur = Member('wblomgren', 'Wilbur Blomgren')

print(wilbur.date_joined)
print(wilbur.free_expires)
print(wilbur.user_name)
print(wilbur.full_name)