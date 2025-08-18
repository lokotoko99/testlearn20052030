# Side Stepping Errors: these arent for xiing bugs in your code,fixing errors in environment in which program is running

try:
# Open the file that's in this same folder.
    the_file = open('peoplefinal.csv')
    # Print a couple blank lines then the first line from the file.
    print('\n\n', the_file.readline())
    # Show the file name.
    print(the_file.name)
    # Close the file
    print(the_file.wookems())
except FileNotFoundError:
    print("Sorry, I don't see a file named peoplefinal.csv here")
except Exception as xa:
    print(xa)
    print("Sorry, something else is wrong")
"""
Traceback (most recent call last):
  File "c:\\Users\\Focus-Mode\\Desktop\\AIO Python\\Book 2 Understanding Python Building Blocks\\CH 7 (part 1(=) sidestepping errors.py", line 4, 
in <module>
    the_file = open('peoplefinasl.csv')
FileNotFoundError: [Errno 2] No such file or directory: 'peoplefinasl.csv'
"""

"""
Again, if you’re thinking about handling the .wookems error, that’s not an
exception for which you’d write an exception handler. Exceptions occur when
something outside the program upon which the program depends isn’t available.
Programming errors, such as nonexistent method names, are errors inside the
program and have to be corrected there by the programmer who wrote the code.
"""