# Side Stepping Errors: these arent for xiing bugs in your code,fixing errors in environment in which program is running

try:
# Open the file that's in this same folder.
    the_file = open('peoplefinal.csv')
    # Show the file name.
    print(the_file.name)
except Exception:
    print("Sorry, I don't see a file anmed peoplefinal.csv here")
"""
Traceback (most recent call last):
  File "c:\\Users\\Focus-Mode\\Desktop\\AIO Python\\Book 2 Understanding Python Building Blocks\\CH 7 (part 1(=) sidestepping errors.py", line 4, 
in <module>
    the_file = open('peoplefinasl.csv')
FileNotFoundError: [Errno 2] No such file or directory: 'peoplefinasl.csv'
"""