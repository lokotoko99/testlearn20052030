# Passing in an arbitrary number of arguements

"""whatever you pass in becomes a tuple So if you want to change things you need to copy the tuple to a list
 and then work on that copy."""

def sorter(*args):
    """ Pass in any number of arguments separated by commas
    Inside the function, they treated as a tuple named args."""
    #Create a list from the passed-in tuple.
    newlist = list(args)
    # Sort and show the list.
    newlist.sort() #(key=lambda s: s.lower)
    print(newlist)

sorter(500,200,100,50,777,0.8)
sorter('zippo','ali','cookie','Sakura')

# Returning Values from Functions 

def alphabetize(original_list=[]):
    """ Pass any list in square brackets, displays a string with items sorted"""
    # Inside the function making a working copy of the list passed in.
    sorted_list = original_list.copy()
    # Sort the wroking copy.
    sorted_list.sort()
    # Make a new empty string for output
    final_list = ''
    # Loop through sorted list and append name and comma and space.
    for name in sorted_list:
        final_list += name + ', '
    #knock off the last comma
    final_list = final_list[:-2]
    #Return the alphabetized list.
    return final_list

random_list = ['McMullen', 'Keaser', 'Maier', 'Wilson', 'Yudt',
'Gallagher', 'Jacobs']

alpha_list = alphabetize(random_list)

print(alpha_list)



