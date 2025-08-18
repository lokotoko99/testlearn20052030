"""
try:
    The thing that might cause an exception
catch a common exception:
    Explain the problem
catch Exception as e:
    Show the generic error message
else:
    Continue on here only if no exceptions raised
"""

try:
    # Open the file named people.csv
    the_file = open('peoplefinal.csv')
# Watch for common error and stop program if it happens.
except FileNotFoundError:
    print("Sorry, i don't see a file named peoplefinal.csv here")
# Catch any unexpected error.
except Exception as err:
    print(err)
# Otherwise, if nothing bad has happened by now, just keep going.
else:
    # File must be open by now if we got here.
    print( '\n') # Print a blank line.
    # Print each line from the file.
    for one_line in the_file:
        print(one_line)
    the_file.close()
    print("Success!")
