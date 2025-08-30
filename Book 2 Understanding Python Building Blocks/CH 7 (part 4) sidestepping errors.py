# Custom exception handler inherits from Exception class.
class CustomException(Exception):
    def __init__(self, message = "A custom exception occured"):
        self.message = message
        super().__init__(self.message)
# A variable that starts out False.
file_is_open = False



try:
    # Open the file named people.csv
    the_file = open("test.csv")
    # Count the number of lines in file.
    line_count = len(the_file.readlines())
    print(f"Line count: {line_count}")
    # If there are fewer than 2 lines. raise exception.
    if line_count < 2:
        raise CustomException('Not enough rows!')

# Handles missing file rror.
except FileNotFoundError:
    print('\nThere is no peoplefinal.csv file here')

# Handles the custom exception (if any)
except CustomException as ce:
    print(f"\nCustom Exception: {ce}")

# Handles all other exceptions
except Exception as e:
    print('\n\nAn unexpected error occured.')

# Otherwise, if nothing bad has happened by now, just keep going.
else:
    # File must be open by now. Set the open status to True.
    file_is_open = True
    the_file.seek(0) # Reset the file pointer to the beginning of the file.
    for one_line in the_file:
        print(one_line)

finally:
    #This executes no matter what. So the file is closed if it was open.
    if file_is_open:
        the_file.close()
    print("File is closed now")