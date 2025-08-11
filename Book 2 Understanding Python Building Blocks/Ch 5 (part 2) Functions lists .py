def alphabetize(original_list=[]):
    """Pass any list in square brackets, displays a string with items sorted"""
    # Inside the function make a working copy of the list passed in.
    sorted_list = original_list.copy()
    # Inside the function make a working copy of the list passed in.
    sorted_list.sort()
    # sort the working copy.
    final_list =''
    # Loop through sorted list and apend name and comma and space.
    for x in sorted_list:
        final_list += x + ', '
    # knock off comma and space
    final_list = final_list[:-2]
    
    print(final_list)


list1= ['joey','vince','amy']

alphabetize(list1)


numbers =[100,5,2,5689]
numbers.sort()

print(numbers)

